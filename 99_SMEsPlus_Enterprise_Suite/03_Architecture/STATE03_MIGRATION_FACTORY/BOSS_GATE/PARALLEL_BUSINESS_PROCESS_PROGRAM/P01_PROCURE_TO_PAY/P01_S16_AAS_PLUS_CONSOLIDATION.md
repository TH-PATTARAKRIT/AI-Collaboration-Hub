# P01 — SERIES-16 AAS+ CONSOLIDATION

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S16-12`
AAS+ may recommend HOLD or VETO. **AAS+ may not decide Boss-only architecture policy, and does not here.**

---

## 1. WHAT THE ROUND ESTABLISHED THAT SURVIVES CHALLENGE

| Established | Status after four challenges |
|---|---|
| The receipt → valuation → GL path **executes** in this generation — 57,863 of 74,982 layers post | **SURVIVES.** Reproduced by all four experts |
| The policy population is genuinely **mixed** — 15 of 30 categories `real_time` | **SURVIVES**, both `ir_property` scopes read |
| The policy **explains** the linkage split | **SURVIVES AND STRENGTHENS** — the residuals that appeared to contradict it are now largely explained *by other mechanisms*, not by policy failure |
| Correction is **immutable reversal** — 5,115 pairs, 0 unresolvable originals | **SURVIVES** |
| **No period lock of any kind** on 169,143 posted entries | **SURVIVES** |
| Series-16 source exists locally and is version-ranked to the deployment | **SURVIVES**, and Expert 4 improved it: the custom source is **one directory**, 45 of 46 modules |
| Thai WHT is heavily exercised — 5,201 certificates | **SURVIVES**, and is far more serious than reported (§3) |

**The round's central purpose — establishing that the mechanism P01 described from source for five rounds is
real and operable — holds.** That is not diminished by anything below.

---

## 2. WHAT DID NOT SURVIVE

| Withdrawn / corrected | Consequence |
|---|---|
| GRN net **฿72,097,814.25** | All-states. Posted-only **−฿7,048,692.08**, opposite sign |
| *"The price-difference engine has never fired"* | **฿2,246,313,274.64** across 1,123 layers |
| Residual B as 1,209 policy violations | Bill-created price-difference layers |
| *"Policy change refuted"* | The change **happened**; my test could not see reverted rows |
| *"The general ledger is intact and sane"* | **8 posted items above ฿1bn**; ฿39.2m misallocated |
| Cost explosion owned by **P03** | Owned by **P01** — `purchase_stock/_get_price_unit` |
| BE leakage = 30 rows | Materially wider; extent disputed between experts |

**Seven published statements from this round were corrected inside the same round.** Six were found by
challengers; none was found by the author after publication.

---

## 3. THE FOUR ITEMS AAS+ RANKS AS MATERIAL

### 3.1 `S16-B-05` — the deletion hypothesis, and it is programme-wide
`stock_valuation_layer.account_move_id` is **`ON DELETE SET NULL`** (verified from schema, with controls), and
`om_data_remove` — installed here — performs raw `DELETE` with `commit()`, no ORM, no lock check, no log.
**A journal-entry deletion reproduces the "0 of N linked" signature P01 published for series 18 and series 19.**
Those findings had independent positive explanations and are not overturned; **the alternative was never
excluded.** **Highest-ranked item in this consolidation.**

### 3.2 The price-unit defect is live and is P01's own
`purchase_stock/models/stock_move.py::_get_price_unit` — no zero-guard on `remaining_qty`, unsigned
`invoice_lines` summation, no cancelled-bill filter — all three contradicting `_compute_qty_invoiced` in the
same module. Entry condition `qty_invoiced > qty_received`. **Conditions still live.**

### 3.3 Withholding amounts are hand-entered
A rate record **named `WHT3%` valued `0`**, used by 2,038 payments, with **฿21,556,228.06** posted after it
was zeroed. The computed path yields 0.00; the operator types the figure. **Statutory implications belong to
P07 and are not drawn here.**

### 3.4 The clearing account is a swept suspense account
Account 39 has `reconcile = 'f'`; **no receipt is ever matched to its bill**; 39 manual `MISC` items sweep
฿1.9bn out of it, driving it to exactly ฿0.00 five times. **"The bridge closes" is true of totals and false of
items** — a materially weaker statement than published.

---

## 4. DENOMINATOR AND SCOPE DEFECTS THIS ROUND EXHIBITED

| Defect | Instance |
|---|---|
| Aggregate published without its **state basis** | GRNI, and every total in that section |
| Conclusion about a **mechanism** from one **account's** count | price-difference engine |
| Population chosen **from the side you already searched** | "GL is intact", tested from the subledger |
| A **negative tested only against surviving rows** | policy-change refutation |
| A ratio published **without its unit** | 6:1 bills-to-POs — 73.1% by count, 89.8% by value |
| **Extraction denominator never declared** | 41 of 651 tables (6.3%) |
| A **freeze declared and not enforced** | 15 files added during review |

**Every one is a boundary defect. None is a reasoning defect.** That is now the settled pattern of this
programme and it is not improving.

---

## 5. CROSS-PROCESS CONFLICTS

| Peer | Item | Position |
|---|---|---|
| **P03** | Cost explosion | **P01 withdraws its routing to P03 as owner.** P03 is a **propagation** route |
| **P05** | Vendor advance, dead `deduct_down_payments`, now with **฿14,429,800.46** attached | **Disagreement preserved.** P01 does not overrule P05 |
| **P06** | `om_data_remove` | P06's finding is **corroborated** and extended by the `ON DELETE SET NULL` consequence |
| **P07** | All withholding statutory questions | **Routed. P01 states no statutory position** |
| **P08** | Cut-off, BE dates, GRN suspense behaviour, AP state basis | Routed with measurements |
| **P11** | `S16-B-05`, event identity, the state-basis question | Routed |
| **P04** | Its warning that a version match is not code identity | **Confirmed in fact**, and superseded by the registry method |

---

## 6. AAS+ POSITION

> **RECOMMEND HOLD.**

**Grounds.** The round's central finding is sound and important. But **seven of its published statements were
corrected within the same round**, one headline inverted in sign, and one — `S16-B-05` — raises a competing
explanation for conclusions published in **two earlier rounds** that has not been excluded.

**AAS+ does not veto.** Nothing here is unsafe to hold; nothing here authorises implementation. The
appropriate state is HOLD pending: (a) the `S16-B-05` test in the series-18 and series-19 deployments;
(b) a re-derivation of every monetary total in the P01 package on a declared state basis; (c) resolution or
formal preservation of the two expert disagreements in §4 of the challenge document.

**Boss-only items are untouched**: whether periodic valuation is right for any deployment, whether the
unaccrued or swept clearing positions are acceptable, and whether the Thai withholding practice is compliant
all remain Boss and P07 decisions. **AAS+ expresses no view on any of them.**
