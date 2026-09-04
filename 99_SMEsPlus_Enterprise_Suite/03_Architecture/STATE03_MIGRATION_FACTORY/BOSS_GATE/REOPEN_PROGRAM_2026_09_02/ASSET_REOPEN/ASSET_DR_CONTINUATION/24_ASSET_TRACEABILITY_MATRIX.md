# 24 — TRACEABILITY MATRIX

**LAYER 2 — AUDIT QUARANTINE.**

Three traces: requirement → evidence → design; evidence → conclusion → gate impact; and
Boss decision → consequence.

---

## 1. Requirement → evidence → design → blocker

| Requirement | Source | Evidence | Design | Blocker |
|---|---|---|---|---|
| A job carries only the machines it actually used | `BD-03` | `E-C-01`, `E-C-02` — no machine on the operation; N:1 equipment to work centre | `19` §3 — machine on the operation; work centre demoted to resource group | `BLK-02` |
| Internal usage accumulates without cap | `BD-01` | `E-C-05` — the off-balance firewall; `E-L-03` — no statutory presentation | `19` §6; `10` | Closed |
| Internal usage must not alter statutory figures | `BD-01` | `E-C-05`, `E-L-03` | `10` §10 — four independent grounds | Closed |
| Every period 100% attributed | `BD-02` | `E-L-01` ¶13 — unallocated expensed in period | `09` §3 identity | `BLK-07` |
| Non-productive classified by cause | `BD-02` | `E-C-04` — the downtime taxonomy; `E-C-03` — the preventive/corrective axis | `09` §4; `19` §4 | `BLK-08` |
| One allocation method per context | `BD-04` | `E-L-01` ¶13 — different bases for fixed and variable | `11` §4 — declared departure | Boss confirmation |
| Depreciation may enter inventory | Design premise | `E-L-01` ¶12 — **required** | `12` §3 | Closed — `BLK-03` |
| No cross-tenant access | Prompt §16 | `E-C-11` — company-optional master data; `parent_of` on assets | `19` §8 | AAS+ **FAIL** on current state |
| No cross-company cost leakage | Prompt §16 | `E-C-11` | `14` §5 rules 1–8 | `Q-05` |
| Daily, not monthly, basis | `BD` / baseline | `E-C-10`, `E-D-01` — 30/360 default, 8% February | `19` §2 rule 4 | `BLK-01` |
| Full auditability | Prompt §7 | `E-C-07` — a snapshot nothing reads; `E-C-13` — silent inert code | `19` §7 — dated records, reversal not deletion | — |

## 2. Evidence → conclusion → gate impact

| Evidence | Conclusion | Gate impact |
|---|---|---|
| `E-L-01` ¶12 | Absorption of production-equipment depreciation into inventory is **required** by Thai accounting standards | **Closes `BLK-03`.** The costing proposition's statutory precondition is satisfied |
| `E-L-01` ¶13 | The fixed-overhead denominator must be normal capacity; unallocated is expensed in period | **Closes `BLK-06` by corroboration; raises `BLK-07` and `BLK-08`** |
| `E-L-03` | Off-balance amounts have no statutory presentation surface | **Closes `BLK-04`** |
| `E-C-05` | The platform refuses any entry mixing off-balance and on-balance accounts | Makes `BD-01`'s isolation structural; answers the baseline's `UNR-17` |
| `E-C-09` | No normal-capacity or variance mechanism exists in 797 modules | Adds build step 3 in `19` §10; the reference product cannot be configured into compliance |
| `E-C-01`, `E-C-02` | Machine identity is absent from the whole measurement chain | Confirms `BD-03` structurally; sets build steps 1–2 |
| `E-C-04`, `E-C-03` | A reusable downtime taxonomy and a planned/unplanned axis already exist | Reduces build scope; supplies `BLK-08`'s data |
| `E-C-07` | Valuation and the ledger read the live rate, not the snapshot | Corrects the baseline; sets the `13` §3 rule |
| `E-C-08` | Absorption is conditional on costing method and valuation mode; the labour entry is dated at posting | `CTR-C-07`, `CTR-C-09`; `13` `T-02` |
| `E-C-11` | Company-optional master data and an upward-traversing asset rule | AAS+ **FAIL** on SaaS integrity |
| `E-C-13`, `E-C-14` | Three of four custom link behaviours are inert; the claim is a one-way ratchet | Build step 1; `CTR-02`, `CTR-04` |
| `E-D-01` | The baseline's day-convention figures reproduce exactly | The 8% February exposure is confirmed, not inherited |

## 3. Boss decision → consequence

| Decision | Direct consequence | Second-order consequence | Where |
|---|---|---|---|
| `BD-01` no cap | Unbounded off-balance accumulator | Needs a rate base (`UNR-C-02`), a disposal close, and a re-entry rule — none supplied by the decision | `10` §3, §6, §7 |
| `BD-02` 100% attribution | The productive/non-productive identity | **Two readings; one breaches the standard** | `09` §2–3 → `BLK-07` |
| `BD-02` cause-based classification | Eight causes rather than seven | Planned and unplanned maintenance take **opposite** treatments | `09` §6 → `BLK-08` |
| `BD-03` work-centre principle | Work centre demoted to resource group | Machine dimension on the operation; assignment becomes a dated record | `19` §3 |
| `BD-04` one driver | Two drivers, one per cost class | Declared departure; per-context choice retained inside the variable class | `11` §4 |

## 4. Deliverable → level → checkpoint

| Deliverable | Level | Checkpoint |
|---|---|---|
| `01` Session control | — | All |
| `02` Prior research lineage | 7 | CP-01 |
| `03` Blocker reconciliation | 7 (§3 mandatory first action) | CP-01 |
| `04` Boss decision incorporation | 7 | CP-01 |
| `05` Asset accounting forensic | 8 | CP-02 |
| `06` Equipment / maintenance forensic | 9 | CP-03 |
| `07` Work centre / operation / routing forensic | 10 | CP-03 |
| `08` Depreciation → manufacturing trace | 11 | CP-04 |
| `09` Productive / non-productive model | 11 | CP-04 |
| `10` Post-depreciation internal usage | 12 | CP-05 |
| `11` Allocation driver matrix | 13 | CP-05 |
| `12` Cost classification matrix | 14 | CP-06 |
| `13` Period close model | 15 | CP-06 |
| `14` Multi-company / SaaS control | 16 | CP-06 |
| `15` Edge case matrix | 17 | CP-06 |
| `16` Source / database learning | 18 | CP-07 |
| `17` Contradiction register | 19 | CP-07 |
| `18` Thai statutory register | 20 | CP-07 |
| `19` Clean-room synthesis | 21 | CP-08 |
| `20` AAS+ audit | 22 | CP-09 |
| `21` PMO gate review | 23 | CP-10 |
| `22` Final blocker register | 24 | CP-11 |
| `23` Evidence index | 7, 18 | CP-01, CP-07 |
| `24` Traceability matrix | — | CP-11 |
| `25` Boss Final Gate Pack | Final | CP-FINAL |

## 5. Coverage check

| Prompt requirement | Where satisfied |
|---|---|
| §3 blocker reconciliation as the first action | `03` — executed before any new research |
| §4 objectives A–S | A–F `05`; G–H `09`; I–J `10`; K–L `08`, `13`; M `19` §5, §7; N `05` §7, `12`; O `10`; P `08`, `19`; Q `14`; R `13`; S `13` §7, `15`, `19` §7 |
| §5 all levels | `21` §1 |
| §6 all 25 deliverables | This matrix §4 |
| §7 evidence standard | `23` |
| §8 UAT rule — read-only, no fabricated result | `01` §6, `22` §4 |
| §9 implementation prohibition | `21` §10 |
| §10 GitHub governance | `01` §1; `25` §26 |
| §11 Jira governance | `25` §25 |
| §12 checkpoints | `01` §7 |
| §13 stop conditions | `01` §6 — the access constraint was declared as soft and all unaffected work completed |
| §14 terminal state | `01` §8, `25` |
