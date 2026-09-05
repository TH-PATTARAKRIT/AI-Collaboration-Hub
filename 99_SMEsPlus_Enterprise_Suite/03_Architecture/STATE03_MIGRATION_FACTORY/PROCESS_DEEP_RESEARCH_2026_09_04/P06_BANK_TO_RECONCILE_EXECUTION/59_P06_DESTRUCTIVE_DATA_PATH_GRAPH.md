# P06_DESTRUCTIVE_DATA_PATH_GRAPH.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S05)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Anchor:** all code analysis below is against **V18E (18.0+e.20250608)**. The installation evidence is from an **Odoo 19** database (`58_`). **The two are not the same system** — see §7.

---

## 1. The graph

```
  RPC  /web/dataset/call_kw   auth="user"
        │  get_public_method — blocks only _private / @api.private
        ▼
  res.config.settings.remove_all()          ← 13 of 17 methods chained
        │
        ├──► remove_account()        9 model slots
        ├──► remove_account_chart() 11 model slots
        └──► remove_message()        3 model slots
                │
                ▼
        remove_data(o, s)
                │  ir.model._get(line) → skip if absent from ir_model
                │  t_name = obj._table  (or model.replace('.','_'))
                ▼
        cr.execute("delete from <table>")     ← NO WHERE
        cr.commit()                            ← per table, durable
        except Exception → _logger.warning     ← swallowed (v18 copies)
                │
                ▼
   ┌────────────┴───────────────────────────────────────────┐
   │  POSTGRES FK RESOLUTION — the ORM is NOT in this path  │
   └────────────┬───────────────────────────────────────────┘
        ┌───────┼────────────────┬──────────────────────────┐
        ▼       ▼                ▼                          ▼
    RESTRICT  CASCADE        SET NULL                   NO FK AT ALL
    refuses   silently       dangling refs              company_dependent
    (swallowed) destroys     left behind                (17 on account_account,
                more rows                                 3 on account_journal)
```

**DPG-F-01 — Because the ORM is bypassed, Postgres resolves the graph, not Odoo.** Every `ondelete` becomes a database-level outcome with no Python hook, no `unlink()` override, no reversal, and no log.

---

## 2. Denominators, executed

| Unit | Value |
|---|---|
| `remove_data` call sites | **16** |
| public `remove_*` methods | **17** |
| model-name slots passed to `remove_data` | **89** |
| slots NOT resolvable in V18E | **13 of 89** |
| resolution PATH SET | V18E, **9,431 `*.py` scanned**, 1,533 distinct model names |
| methods chained by `remove_all` | **13 of 17** |

**No accounting model overrides `_table`** — PATTERN `_table = ` filtered to account/mail/payment/partner_bank: 2 hits, neither accounting. So table = model with `.`→`_` throughout.

---

## 3. The accounting deletion set

**`remove_account` — 9 slots, 8 accounting:** `payment.transaction` · `account.bank.statement.line` · `account.payment` · `account.analytic.line` · `account.analytic.account` · `account.partial.reconcile` · `account.move.line` · `hr.expense.sheet` · `account.move`

**`remove_account_chart` — 11 slots, 8 resolvable:** `res.partner.bank` · `account.move.line` · ~~`account.invoice`~~ *(dropped since v13 — NOT FOUND)* · `account.payment` · `account.bank.statement` · ~~`account.tax.account.tag`~~ *(m2m relation, not a model)* · `account.tax` · ~~`account.account.account.tag`~~ *(m2m relation)* · ~~`wizard_multi_charts_accounts`~~ · `account.journal` · `account.account`

**`remove_message` — 3, all audit trail:** `mail.message` · `mail.followers` · `mail.activity`

**Also reached, outside P06's prior scope:** `stock.valuation.layer` (the inventory valuation ledger — **P03/P04 territory**), `pos.payment`, `pos.order`, `pos.session`, `hr.payslip`, `hr.payslip.run`.

**DPG-F-02 — The blast radius is wider than P06 reported.** Round 3 named the bank and payment tables. It also destroys **the inventory valuation ledger, payroll runs, POS payments, and the analytic ledger** — four other processes' domains.

---

## 4. Foreign-key resolution — what Postgres actually does

> **PROVENANCE NOTE (AAS-03 E2-S-01).** The ORM default-resolution rule below is **quoted verbatim and independently checkable in seconds**. The per-table FK counts were produced by a single automated pass over 9,431 files and have **not been verified by a second, independent pass**. Treat the rule as `FACT VERIFIED` and the counts as `SUPPORTED INTERPRETATION`. `P06-OQ-119`.

Effective `ondelete` derived from `ODOO_CORE/fields.py:3189-3197`:
```
if not self.ondelete:
    comodel = model.env[self.comodel_name]
    if model.is_transient() and not comodel.is_transient():
        self.ondelete = 'cascade' if self.required else 'set null'
    else:
        self.ondelete = 'restrict' if self.required else 'set null'
```
and emitted at `fields.py:3222-3234` — **except that `company_dependent=True` emits no FK at all.**

| Target table | m2o refs | cascade | set null | **restrict** | no FK |
|---|---|---|---|---|---|
| `account_move` | 34 | **5** | 29 | 0 | 0 |
| `account_move_line` | 9 | 2 | 5 | **2** | 0 |
| `account_payment` | 7 | 0 | 7 | 0 | 0 |
| `account_bank_statement` | 2 | 0 | 2 | 0 | 0 |
| `account_bank_statement_line` | 4 | 0 | 4 | 0 | 0 |
| `account_partial_reconcile` | 1 | 0 | 1 | 0 | 0 |
| **`account_full_reconcile`** | **2** | 0 | **2** | 0 | 0 |
| `mail_message` | 20 | **11** | 9 | 0 | 0 |
| `mail_followers` | **0** | — | — | — | — |
| `res_partner_bank` | 6 | 1 | 2 | **3** | 0 |
| `account_journal` | 61 | 8 | 41 | **9** | **3** |
| `account_account` | 119 | 6 | 86 | **10** | **17** |
| `account_analytic_line` | **0** | — | — | — | — |

### DPG-F-03 — Three outcomes, and each is a distinct failure

**(a) CASCADE — collateral destruction with no hooks.**
`delete from account_move` cascades to **`account_move_line`** (`account_move_line.py:33-40`, `required=True, ondelete="cascade"`) and **`account_bank_statement_line`** (`account_bank_statement_line.py:24-29`). **Deleting journal entries wipes their lines and the bank statement lines by database action alone.**
`mail_message` cascades to **10** non-transient children including **`mail_tracking_value` — the field-level audit trail.** The record of *what changed* is destroyed with the messages.

**(b) RESTRICT — refused, and the refusal is swallowed.**
`res_partner_bank` carries **3 restricts** and is the **first** entry in `remove_account_chart`. It will be refused whenever any move or payment carries `partner_bank_id`. `account_move_line` carries **2 restricts** from `account_partial_reconcile` (`required=True`). **In `remove_account_chart` there is no prior partial-reconcile delete**, so that statement raises, is swallowed to a warning, **and the run continues to delete `account_journal` and `account_account`.**
**DPG-F-04 — Partial destruction is the normal outcome, not the exceptional one.** Some tables refuse, the refusals are invisible, each success is committed, and the run proceeds. The resulting state is neither the old database nor a clean one.

**(c) SET NULL and NO FK — dangling references, silently.**
**`account_full_reconcile`: both inbound references are SET NULL, and the arrow points partial→full.** So `delete from account_partial_reconcile` leaves **every full-reconcile row intact with zero parts** — an orphaned reconciliation head — and `account_move_line.full_reconcile_id` still pointing at it.
**And 17 references to `account_account` and 3 to `account_journal` have no FK at all** because they are `company_dependent=True` (product and partner property fields). Those stored values point at deleted account ids **with no database protection whatsoever**.

---

## 5. `account.full.reconcile` — the finding round 3 missed

**DPG-F-05 — It is in NO remove list, in ANY of the copies.** PATTERN `full.reconcile|full_reconcile` over all four examined copies: **NOT FOUND**.

Consequences, in order:
1. Full-reconcile rows **survive** the deletion of their parts.
2. `account_move_line.full_reconcile_id` keeps pointing at them.
3. **The ORM compensation is never reached.** `account_full_reconcile.py:13-36` exists precisely to reverse exchange-difference moves on removal — `moves_to_reverse = self.exchange_move_id … _reverse_moves(default_values_list, cancel=True)`. **Raw SQL never invokes it. Exchange-difference entries are never reversed.**
4. The ORM constraint at `account_move_line.py:1340-1356` (`matching_number` must agree with `full_reconcile_id`) is **Python, not Postgres** — so the database is left in a state the ORM will reject on the next write to those lines.

**This is the sharpest illustration of the whole finding: the operation leaves the ledger in a shape the application itself considers invalid.**

---

## 6. Requirements

| ID | Requirement |
|---|---|
| `DPG-R-01` | No path may write to the ledger outside the object layer. **Adopted from P08 `P08-T0-08`, which stated it first.** |
| `DPG-R-02` | A destructive operation must be atomic. Per-table commit inside a loop makes partial destruction durable. |
| `DPG-R-03` | A failure in a destructive operation must abort it, never be logged and stepped over. |
| `DPG-R-04` | Referential compensation belongs in the domain layer and must not be delegated to database `ondelete`. |
| `DPG-R-05` | The audit trail may never be a deletion target, and never a cascade victim. |

---

## 7. Version boundary on this file

**Every FK count, `ondelete` resolution and table mapping above is anchored to V18E.** The installation evidence in `58_` is from **Odoo 19**. `account.full.reconcile` ondelete behaviour and `account.move` numbering **have not been re-derived against v19** and must be before this analysis is applied to `iEVING`. Recorded as `P06-OQ-116`.
