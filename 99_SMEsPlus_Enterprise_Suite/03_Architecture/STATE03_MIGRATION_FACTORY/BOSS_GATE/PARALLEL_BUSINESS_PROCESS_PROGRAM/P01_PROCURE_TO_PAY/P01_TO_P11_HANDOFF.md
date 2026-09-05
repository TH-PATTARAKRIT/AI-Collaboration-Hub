# P01 → P11 (CORE RECONCILIATION) — CONTROLLED HANDOFF AT RESEARCH-SCOPE FREEZE

Session: `SMEPLUS-26-09-05-G01-P01-P2P-CONTROLLED-SCOPE-FREEZE-HANDOFF-001`
Checkpoint `CP-05` · Baseline `a02ec8b`

> This **supplements and does not replace** `P01_CORE_RECON_HANDOFF_PACK.md`,
> `P01_P11_EVIDENCE_VERSION_DEPLOYMENT_SUPPLEMENT.md`, `P01_P11_S18_DIRECT_VERIFICATION_SUPPLEMENT.md` and
> `P01_S16_P11_HANDOFF.md`. All remain in force. **P01 has not started P11 work.**

---

## 1. THE ITEM P11 MUST TAKE FIRST — IT REACHES TWO EARLIER ROUNDS

### `S16-B-05` — a deletion reproduces a zero P01 has twice explained another way

Schema-verified, with controls (584 `ON DELETE CASCADE` / 1,741 `ON DELETE SET NULL` in the same schema):

```
stock_valuation_layer_account_move_id_fkey FOREIGN KEY (account_move_id)
    REFERENCES public.account_move(id) ON DELETE SET NULL;
```

`om_data_remove 16.0.1.0.1` is **installed** and performs raw `DELETE FROM <table>` + `commit()` — **no ORM,
no lock-date check, no company filter, no log**; 10 of 20 destructive buttons carry no confirmation.
Peer **P06** independently reports this module deletes ledger data without authorisation.

> **Deleting journal entries silently NULLs `account_move_id` on every valuation layer that referenced them —
> reproducing exactly the "0 of N valuation layers linked" signature P01 published for the series-18 OCC
> deployment (0 of 47,801) and the series-19 estate (0 of 14,441).**

**Neither finding is overturned.** The series-18 periodic policy was proved positively and independently —
126 of 126 categories, both storage locations read, source gate closed. **What is new is that a competing
explanation exists and was never excluded**, and the programme has read those zeros as *"never posted"* when
*"posted and later deleted"* is observationally identical.

No evidence the module ran in the series-16 deployment (every target table populated, low minimum ids) —
**with the stated limit** that two target tables are empty and the module leaves no trace by design.

**Owner: P06 (module) + P11 (reconciliation reliance). Exact next action in §6.**

---

## 2. WHAT SURVIVES AS AUTHORITATIVE

| Finding | Basis |
|---|---|
| Receipt→valuation→GL **executes** in series 16 — 57,863 of 74,982 layers | the programme's only positive control for this mechanism |
| Valuation policy is a genuine **mixed population** (15 of 30 categories `real_time`); policy explains the linkage split | both `ir_property` scopes read; coverage control 0 of 74,982 |
| GRNI account: **13,666 posted items, posted-only net −฿7,048,692.08**; `reconcile='f'` | a swept suspense account, not an item-matched bridge |
| Correction is **immutable reversal** — 5,115 pairs, 0 unresolvable originals | healthiest correction profile measured in the estate |
| **No period lock of any kind** on 169,143 posted entries | — |
| AP **97.89% reconciled**; open residual splits by state (§4 of the P08 handoff) | positive control: 0 of 52,996 reconciled items carry a residual |
| Cost-explosion root cause is **`purchase_stock/_get_price_unit`** — P01's own path, conditions live | source read line by line |
| Price differences **capitalised into inventory**, no P&L variance line observed | 1,267 fired / 1,123 material |
| WHT: a rate record **named `WHT3%` valued `0`**, 2,038 payments, ฿21,556,228.06 posted after zeroing — **amounts hand-entered** | verified |
| Receipt→bill identity is **document text, not a foreign key** | structural |

---

## 3. WHAT IS WITHDRAWN OR SUPERSEDED — LINEAGE PRESERVED, NOTHING DELETED

| Withdrawn | Replaced by | Record |
|---|---|---|
| GRN net **฿72,097,814.25** | posted-only **−฿7,048,692.08** (opposite sign) | `ERR-P01-45` |
| *"The price-difference engine has never fired"* | 1,267 firings / ฿2,246,313,274.64 material | `ERR-P01-46` |
| Residual B = 1,209 policy violations | bill-created price-difference layers (1,194 have no stock move) | `ERR-P01-47` |
| *"Policy change refuted by time distribution"* | the change **happened**; `ir_property` cannot see reverted rows | round-6 challenge |
| *"The general ledger is intact and sane"* | **8 posted items > ฿1bn**; ฿39.2m misallocated | round-6 challenge |
| Cost explosion owned by **P03** | owned by **P01** | this handoff, §1 of the P03 handoff |
| BE leakage = 30 rows in one column | materially wider; **extent disputed** | §4 |
| Earlier: *"no deployed series-18 database exists"*; *"the series-16 core is a VERIFIED ABSENCE"* | both false | `ERR-P01-23`, `ERR-P01-41` |

---

## 4. UNRESOLVED — WITH THE REASON, NOT JUST THE LABEL

| Item | Why it is unresolved |
|---|---|
| **Buddhist-era extent** | Two experts, two methods, two answers — **484 values / 14 columns / 11 tables** vs **12 pairs / 7 tables / 120 journal + 120 analytic items**. Both far exceed the published 30. **Neither adopted; not averaged.** Common floor: *materially wider than 30, and no date column is reliably Gregorian* |
| **Certificate/payment gap denominators** | 1,407 vs 1,405 certificates; 1,543 vs 1,488 payments — **different denominators** (`done` vs all; payments vs items). Both recorded |
| **~40–45 valuation layers** genuinely unexplained | after 245 of 296 resolved as `consu` and 1,209 as price-difference layers |
| **`S16-B-05`** | §1 — untested in the series-18 and series-19 deployments |
| **Advance→bill deduction lineage** | populations measured, lineage not; **P05 disagreement preserved unresolved** |
| Thai WHT statutory correctness | **six items routed to P07**; P01 states no position on Thai law |

**A count P01 DID resolve this run, cheaply, from open evidence:** 1,267 = `price_diff_value IS NOT NULL`
(the engine fired); 1,123 = non-zero. **1,267 − 1,123 = 144** layers where it ran and produced exactly ฿0.00.
Both correct, different predicates. **Not forced.**

---

## 5. BOSS DECISIONS — STATED AS OPTIONS, NOT RECOMMENDATIONS

1. Whether **capitalising purchase price variance into inventory** rather than expensing it is intended.
2. Whether the **GRNI suspense-and-sweep** pattern (no item reconciliation, ฿1.9bn swept manually) is acceptable.
3. Whether operating **169,143 posted entries with no period lock** is acceptable.
4. Whether **hand-entered withholding against a 0-valued rate record** is acceptable — *statutory element
   belongs to P07*.
5. Whether periodic valuation is right for any given deployment.

**P01 expresses no view on any of these.**

---

## 6. DEPENDENCIES WITH OWNERS AND EXACT NEXT ACTIONS

| ID | Item | Owner | Exact next action |
|---|---|---|---|
| `S16-B-05` | Deletion reproduces the zero-link signature | **P06 + P11** | In `551ab874` (series-18, extracts at `…/scratchpad/s18/`) and the series-19 estate: (1) is `om_data_remove` in `ir_module_module`? (2) is the FK `ON DELETE SET NULL` there — `pg_restore -s -f <out> <dump>`, **note `-f`, a redirect yields 0 bytes**; (3) id gaps in `account_move`, orphaned `account_move_line`, low minimum ids? |
| `S16-B-01` | Price differences capitalised, no P&L variance | **P08** | Decide the reporting treatment; confirm whether any P&L route exists |
| `S16-B-02` | Advance/settlement lineage; P05 disagreement | **P01 + P05** | Join 22,468 payments to 447,384 items through the two reconcile tables (all extracted) |
| `S16-B-03` | Kit price-difference correction | **P03** | See `P01_TO_P03_HANDOFF.md §2.2` |
| `S16-B-04` | No period lock on 169,143 posted entries | **P08** | — |
| `GAP-P01-07` | 41 of 651 tables extracted, no selection rule | **P01** | Declare the rule or widen the extraction |
| — | Thai WHT statutory basis | **P07** | Six routed items |
| — | Runtime execution of the seven priority edge cases | **Boss** | `HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED` |

---

## 7. P01's TERMINAL RECOMMENDATION

> **RECOMMEND HOLD.** Research scope frozen for current evidence; every open item routed to a named owner
> with an exact next action.

**This is not a Final Freeze, not PASS, not merge authority, and not design approval.** Boss may reopen P01 on
Material Delta — and `S16-B-05` returning a positive result in either the series-18 or series-19 deployment
**would itself be Material Delta**.
