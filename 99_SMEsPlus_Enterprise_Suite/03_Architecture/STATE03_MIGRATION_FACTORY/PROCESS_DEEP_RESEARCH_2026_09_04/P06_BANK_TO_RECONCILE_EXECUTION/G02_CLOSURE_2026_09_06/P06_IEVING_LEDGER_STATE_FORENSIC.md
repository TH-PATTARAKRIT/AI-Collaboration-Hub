# P06_IEVING_LEDGER_STATE_FORENSIC.md

**Prompt:** `[SMEPLUS-26-09-06-G02-P06-B2R-P10-DELTA-DOMAIN-PURE-CLOSURE-003]`
**Session:** P06 — G02 P10-DELTA DOMAIN-PURE BOUNDED CLOSURE (CP-P06G06)
**Classification:** LAYER 2 — AUDIT QUARANTINE

> **THIS FILE CLOSES `P06-OQ-112` — the query this package named, in `58_` §6, as *"the highest-value unrun query in the package."***
> It was raised by AAS-03 expert `E2-G-02` as a determinable fact the round had declined to determine. It was then determined.
> **NOTHING WAS MUTATED.** Every command below is a read of a `dump.sql` file already in evidence. **No database was connected to, restored, loaded or written. No destructive path was executed.**

---

## 1. What `58_` predicted

> *"Querying `iEVING`'s dump for the predicted orphan signature — `account_full_reconcile` rows with zero surviving `account_partial_reconcile` children, `account_move_line.full_reconcile_id` pointing at them … **would convert 'the tool was installed' into 'the tool was fired, and here is the damage.'**"* — `58_P06_DEPLOYED_MODULE_REGISTRY_PROOF.md` §6

## 2. Method, declared before the result

| Field | Value |
|---|---|
| **Artefact** | `/Volumes/iMacSys/95_BHPRO_PROJECT/DOCUMENT/iEVING_2026-03-31_06-48-41/dump.sql` — 62,458,228 B, `db_name: iEVING`, `version: 19.0+e`, dated 2026-03-31. **The only Odoo backup on the volume** (`58_` DMR-F-01) |
| **Access mode** | **READ-ONLY.** A streaming parser over the `COPY … FROM stdin` blocks. No `psql`, no restore, no connection |
| **POPULATION** | **all 848 tables** in the dump, counted, not a chosen subset |
| **UNIT** | table row |
| **PATTERN** | `COPY public.<table> (…) FROM stdin;` … `\.` — data lines counted between the header and its terminator |
| **POSITIVE CONTROL** | the parser must return large non-zero counts for tables that certainly have rows, and the row counts must **vary** |
| **NEGATIVE CONTROL** | it must return zero for tables that certainly have none |
| **STOP CONDITION** | the ledger tables and their chatter counterparts are counted. **Do not** reconstruct business meaning from the surviving master data; that is not P06's question |

**Positive control, executed:**
```
TOTAL TABLES IN DUMP : 848
TABLES WITH >0 ROWS  : 223
TABLES WITH 0 ROWS   : 625
top by row count: ir_model_data 34164 · ir_model_fields 14736 · res_city 7426 · ir_model_constraint 3361 …
```
**The instrument returns large, varied, plausible counts. It is not returning zeros because it cannot see its inputs.**

> **This control was added because the first attempt at this query failed silently.** A field-indexed extractor returned `account_move = 0 rows` alongside `account_full_reconcile = 1`, which is incoherent. Rather than publish the zero, the header line was inspected directly (`grep -n "^COPY public.account_move ("` → line 88405; terminator at 88406). **The zero was real.** The whole-dump control above was then built so that no single zero in this file rests on an uncontrolled instrument.

## 3. The result

| Table | Rows |
|---|---|
| `account_account` | **241** |
| `account_journal` | **9** |
| `res_partner` | **39** |
| `res_users` | 33 |
| `res_company` | 2 |
| `product_product` | **849** |
| `product_template` | 36 |
| `mail_message` | **1,748** |
| `ir_attachment` | 921 |
| `ir_module_module` | 1,494 |
| — | — |
| **`account_move`** | **0** |
| **`account_move_line`** | **0** |
| **`account_payment`** | **0** |
| **`account_bank_statement`** | **0** |
| **`account_bank_statement_line`** | **0** |
| **`account_partial_reconcile`** | **0** |
| **`account_full_reconcile`** | **1** |
| `sale_order` / `sale_order_line` | **0 / 0** |
| `purchase_order` / `purchase_order_line` | **0 / 0** |
| `stock_move` / `stock_picking` | **0 / 0** |
| `ir_logging` | **0** |

**IEV-F-01 — The master data is intact and the entire transactional ledger is empty.** 241 accounts, 9 journals, 39 partners, 849 product variants, 1,748 chatter messages — and **not one journal entry, journal item, payment, bank statement, bank statement line or partial reconcile.** `FACT VERIFIED`.

**IEV-F-02 — One `account_full_reconcile` row survives, and it is structurally impossible.**
```
account_full_reconcile: id=1  create_uid=2  write_uid=2  create_date=2026-03-30 06:20:19.595243
```
A full reconcile is created **only** as the closure of a set of `account.partial.reconcile` rows over `account.move.line` rows. **There are zero of each.** This row cannot have been created in the state the database is now in. It was created on **2026-03-30 06:20**, one day before the dump. `FACT VERIFIED`.

**This is exactly the orphan signature `58_` predicted, and `P06-OQ-112` is closed by it.**

**IEV-F-03 — Forty-four orphaned chatter rows point at five now-empty transactional models.**

| `mail_message.model` | Chatter rows | Target table rows | |
|---|---|---|---|
| `purchase.order` | **15** | 0 | **ORPHANED** |
| `account.move` | **13** | 0 | **ORPHANED** |
| `stock.picking` | **11** | 0 | **ORPHANED** |
| `sale.order` | **3** | 0 | **ORPHANED** |
| `account.payment` | **2** | 0 | **ORPHANED** |
| *(control)* `product.product` | 851 | 849 | consistent |
| *(control)* `account.account` | 415 | 241 | consistent |

**The two control rows are the point.** Where the target table still has rows, the chatter is consistent. Where the target table is empty, the chatter survives and dangles. **A model whose records were removed through the ORM would not leave this pattern; `unlink()` cascades the chatter.** `FACT VERIFIED`.

## 4. The mechanism, matched line-for-line

`om_data_remove` (v19.0.1.1 — the **installed** version, per `58_` DMR-F-01) at
`/Volumes/iMacSys/CLAUDE AI/SMEsPlus/SMEsPlus_19.0.20260418/SMEsPlus_19.0.20260418/01_extra/addons_extra/om_data_remove/models/model.py`
builds table names by string substitution and issues unfiltered SQL:
```python
t_name = obj_name.replace('.', '_')      # :21
sql = "delete from %s" % t_name
self._cr.execute(sql); self._cr.commit()
except Exception as e: _logger.warning(...)
```

**Its declared target lists, and what `iEVING` shows for each:**

| Module line | Models deleted | `iEVING` |
|---|---|---|
| `:45-46` | `sale.order.line`, `sale.order` | **0, 0** |
| `:92-93` | `purchase.order.line`, `purchase.order` | **0, 0** |
| `:148-150` | `stock.picking`, `stock.picking.batch` | **0** |
| `:167-174` | `account.bank.statement.line`, `account.payment`, `account.move.line`, `account.move` | **0, 0, 0, 0** |
| `:221-224` | `account.move.line`, `account.payment`, `account.bank.statement` | **0, 0, 0** |
| **`:344`** | **`mail.message`** — **in a separate list, i.e. a different action** | **1,748 rows SURVIVE** |

**IEV-F-04 — The observed state matches the module's transactional-removal lists exactly, and matches the non-execution of its separate chatter list exactly.** Every model on the transactional lists is empty; the model on the separate chatter list is populated; and the residue is 44 orphans pointing from the surviving list to the emptied ones. `FACT VERIFIED` as a pattern match.

**IEV-F-05 — And a remediation module written by this programme documents this precise condition.** `om_data_remove_fix/__manifest__.py:1-5`, sitting **inside the V18E core addons directory**:
> *"Fixes 'Missing Record' errors caused by `om_data_remove` (orphan `mail.message`, `mail.notification`, `mail.activity`, `bus.bus`, `ir.attachment`, `ir.model.data` references)"* … *"`om_data_remove` uses **raw SQL** (`DELETE FROM <table>`) to wipe transactional data. Because the deletes bypass the ORM, none of the following references are cleaned up"*

**The module names orphan `mail.message` references as the damage it exists to repair. The database contains orphan `mail.message` references.**

## 5. Classification, stated carefully

**The alternatives were enumerated before the conclusion, not after.**

| Hypothesis | Test | Verdict |
|---|---|---|
| **H1 — the destructive path was executed** | Predicts: transactional tables empty, master data intact, chatter surviving and orphaned, an ORM-impossible reconcile remnant. **All four observed** | **SUPPORTED on four independent predictions** |
| **H2 — a fresh install, master data loaded, no transactions yet** | Predicts: no `account_full_reconcile` row (it cannot exist without move lines); no orphaned chatter on `account.move`, `sale.order`, `purchase.order`, `stock.picking`. **Both observed to the contrary** | **CONTRADICTED by `IEV-F-02` and `IEV-F-03`** |
| **H3 — a filtered or partial dump** | Predicts: missing tables or missing blocks. **All 848 tables present with headers; 223 populated; the parser reads them** | **CONTRADICTED** |
| **H4 — records removed through the ORM by an operator** | Predicts: chatter cascaded, no orphans, no impossible reconcile row | **CONTRADICTED by `IEV-F-03`** |

**CLASSIFICATION: `SUPPORTED INTERPRETATION` — that `om_data_remove`, or a mechanism behaving identically to it, was executed against the `iEVING` database on or about 2026-03-30.**

**It is NOT `FACT VERIFIED`, and the reason is stated rather than glossed:** `ir_logging` has **0 rows**, no `odoo.log` and no journald artefact was located (`P06-OQ-114`, still open). **There is no execution record.** What is `FACT VERIFIED` is the *state*: `IEV-F-01`, `IEV-F-02`, `IEV-F-03` and the pattern match `IEV-F-04` are all direct reads. **What remains an interpretation — a strong one, surviving four falsification attempts — is the causal attribution.**

## 6. What changes

| Item | Before | **After** |
|---|---|---|
| `P06-OQ-112` | *"the highest-value unrun query in the package"* | **CLOSED — EXECUTED.** The orphan signature is present |
| `P06-B-50` reachability | `REACHABLE — DEPLOYMENT VERIFIED` (installed, on a v19 database not confirmed to be the SMEsPlus target) | **REACHABLE — DEPLOYMENT VERIFIED, AND A DATABASE IN THIS PROGRAMME'S EVIDENCE IS IN THE POST-EXECUTION STATE.** Severity was already **CRITICAL** on `C1, C2, C4, C6`; **it does not rise, because there is no rank above it. What rises is the evidential basis** |
| *"a documented destructive path was used in anger"* (`58_` DMR-F-04) | `SUPPORTED INTERPRETATION`, resting on **one** artefact — a manifest docstring | **`SUPPORTED INTERPRETATION`, now resting on four independent observations in the database itself**, with three competing hypotheses tested and contradicted |
| `P06-OQ-98` — installed on the **SMEsPlus target**? | `HOLD` | **STILL `HOLD`. `iEVING` is a BHPRO-programme database. This finding does not reach the SMEsPlus target and is not claimed to** |
| `P06-OQ-114` — execution proof | open | **STILL OPEN, and now sharper: `ir_logging` has 0 rows in the one database where the effect is visible.** Whether that is because logging was off, or because the log table is itself in a delete list, is undetermined |

## 7. What this file does not claim

- **Not** that the SMEsPlus production or UAT database is affected. `iEVING` is not it (`P06-OQ-98`).
- **Not** that a named person executed anything. `create_uid = 2` on the orphan row is the creator of that reconcile, **not** evidence of who ran a deletion.
- **Not** that the data is unrecoverable elsewhere — no statement is made about other backups.
- **Not** a `FACT VERIFIED` causal attribution. See §5.
- **No mutation of any kind was performed**, and none is proposed.
