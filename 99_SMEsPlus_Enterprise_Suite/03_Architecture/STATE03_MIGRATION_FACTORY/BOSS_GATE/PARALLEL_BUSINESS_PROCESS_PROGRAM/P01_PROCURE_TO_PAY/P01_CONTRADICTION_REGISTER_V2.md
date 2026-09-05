# P01 — CONTRADICTION REGISTER v2

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.** The v1 register is preserved unchanged as lineage. This is the **re-ranked** view.

**Closure is not forced.** Sixteen were carried in; this round adds two and closes **one**.

---

## 1. RANKED REGISTER

| ID | Subject | Version | Deployment | Scope | Peer owner | Decision owner | Evidence can resolve? | Rank |
|---|---|---|---|---|---|---|---|---|
| `CONTRA-P01-15` | The analysed series has **no deployed representative**; the deployment with history has no source | all | estate-wide | — | — | **Boss** | **No** — a fact about the estate | **CRITICAL** |
| **`CONTRA-P01-16`** *(new)* | **Source analysis and deployment evidence do not overlap on any series** | all | estate-wide | — | P11 | **Boss** | Partly — a series-16 core root would help | **CRITICAL** |
| `CONTRA-P01-12R` | Perpetual valuation declared; **no valuation account resolves by any route** | 19 | `E-1` | COMPANY | Inventory | Boss | **Yes** — runtime | **CRITICAL** |
| Financial company ownership | COMPANY-scoped effect raised where ownership is **inferred, not proven**; the guard **cannot execute** | 19 | `E-1`, `E-3` | **TENANT + COMPANY** | SaaS / Platform | **Boss** | Partly | **CRITICAL — tolerance-zero** |
| `CONTRA-P01-08` | Period lock **re-dates rather than refuses** | 16/18/19 | all | COMPANY | **P08** | P08 → Boss | **Yes** — runtime | **HIGH** |
| `CONTRA-P01-01` / `-06` | Correction **deletes** derived items; strong form contradicted — an audit record survives but is weak, and **absent in the series-16 deployment** | 16/18/19 | all | COMPANY | P08 | P08 → Boss | **Yes** — runtime | **HIGH** |
| `CONTRA-P01-03` / `-07` | The two generations implement **different accounting models** | 18 vs 19 | — | — | P11 | **Boss** | No — a design fact | **HIGH** |
| `CONTRA-P01-09R` | **Repeated full-base withholding**, linear — **now verified in deployed source** | 16 | `E-2` | COMPANY | **P07** | P07 → Boss | **Yes** — runtime | **HIGH** |
| `CONTRA-P01-10` | Two shipped copies map to **opposite statutory forms**; neither observed governing | 16 vs 19 | all | COMPANY | **P07** | **P07 statutory** | Partly | **HIGH** |
| `CONTRA-P01-02` | Received-not-billed obligation has **two owners** — P10 reached the same boundary | 18 | — | COMPANY | **P10** | Boss | No — a design decision | **HIGH** |
| `CONTRA-P01-11` | Order-line links are `ON DELETE SET NULL` in **both** deployed series | 16 + 19 | all | COMPANY | P08 | Boss | Verified — needs a **design** answer | **HIGH** |
| **`CONTRA-P01-17`** *(new)* | The vendor-advance **deduction control is inert** — visible, defaulted on, referenced only in commented-out code | 16/19 custom | all | COMPANY | P05 boundary | Boss | **Yes** — runtime | **HIGH** |
| `CONTRA-P01-13` | v19 turned a **blocking refusal into silence** on missing valuation accounts | 18 → 19 | — | — | — | Boss | No — a design fact | **MEDIUM** |
| `CONTRA-P01-04` | Asset classification and clearing **compete for one field**; P04 confirms nobody owns the decision | 18 | — | COMPANY | **P04** | Boss | **Yes** — runtime | **MEDIUM** |
| `CONTRA-P01-05` | **Mutation authority** and financial-effect scope diverge | all | all | **TENANT vs COMPANY** | P11 | Boss | Partly | **MEDIUM** |
| `CONTRA-P01-14` | One capability, **two installed copies, different behaviour** | 16/19 custom | all | — | — | Boss | **Yes** — identify the deployed copy | **MEDIUM** |
| ~~`CONTRA-P01-12`~~ | *withdrawn and restated as `-12R`* | — | — | — | — | — | — | **CLOSED — withdrawn** |
| ~~*"no deployment runs the withholding code"*~~ | **CLOSED this round** — the source root was found and matches the deployment exactly | 16 | `E-2` | — | — | — | **resolved by evidence** | **CLOSED** |

---

## 2. COUNT

| | Count |
|---|---|
| Carried in | 16 |
| Added this round | **2** (`-16`, `-17`) |
| **Closed this round** | **1** — the withholding source-location gap, closed by locating the previously unsearched source root |
| Withdrawn-and-restated | 1 (`-12` → `-12R`), already counted |
| **Open** | **17** |

**This is the first round of P01 to close a contradiction with evidence.** It closed because a
**boundary was repaired**, not because a finding was reinterpreted.

---

## 3. BY RANK

| Rank | Count | Character |
|---|---|---|
| **CRITICAL** | **4** | Three are facts about the estate or the design that no further analysis here can resolve; one is tolerance-zero |
| **HIGH** | **8** | Five resolvable by runtime; two need a design decision; one is statutory |
| **MEDIUM** | **5** | |
| LOW / UNRANKED | 0 | |

---

## 4. WHAT COULD ACTUALLY BE CLOSED, AND BY WHOM

| Resolvable by | Count | Items |
|---|---|---|
| **Runtime execution** — none has ever been performed in P01 | **7** | valuation route, period lock, correction, withholding, advance deduction, asset-field collision, deployed-copy identification |
| **Boss / design decision** | 5 | the two accounting models; the received-not-billed owner; referential integrity; the estate's version gap |
| **P07 statutory** | 2 | withholding lawfulness; the certificate form |
| **Platform / P11** | 2 | ownership proof; mutation-authority scope |
| **Further evidence available here** | **1** | a series-16 **core** source root, if one exists — not yet searched |

> **Seven of seventeen would fall to a single runtime session.** That is the highest-leverage
> action available to the programme, and it has not been performed in any P01 round.

---

# ADDENDUM — `CONTRA-P01-12R` RESTATED AGAIN (`ERR-P01-19`)

| | |
|---|---|
| **As stated (round 3, repeated this round)** | Perpetual valuation declared while **no valuation account resolves by any route** |
| **Corrected** | **The valuation account resolves.** It is configured as a company-level default on 43 of 44 companies. What is missing is the **company stock journal**, unset on **44 of 44** — and the entry-creation path takes its journal from exactly there |
| **Status of the contradiction** | **STANDS**, and is now correctly caused: perpetual valuation is declared and cannot post **for want of a journal** |
| **New sub-finding** | In the *other* series-19 deployment the journal **is** configured — so the contradiction is **specific to one estate**, not a property of the series |
| **Rank** | **CRITICAL**, unchanged |
| **Resolvable by** | one configuration reading in the live system, or one runtime test |

**This is the second restatement of this contradiction. Both restatements preserved its
conclusion and both corrected its cause** — first from "structural absence" to "unconfigured",
now from "no account" to "no journal". The conclusion has been stable; the explanation has been
wrong twice.

---

# G01 CLOSURE ADDENDUM — `SMEPLUS-26-09-05-G01-P01-P2P-CONTROLLED-SCOPE-FREEZE-HANDOFF-001`

## Contradictions closed at freeze

| ID | Contradiction | Resolution | Closed by |
|---|---|---|---|
| **1,123 vs 1,267** | Two counts of the same price-difference engine | **CLOSED — not forced.** 1,267 = `price_diff_value IS NOT NULL` (the engine fired); 1,123 = non-zero. **Difference = 144** layers where it ran and produced exactly ฿0.00. Both correct, different predicates | this run, from already-open evidence |
| **Account 1173 mechanism** | Expert 2 (product-level overrides) vs Expert 1 (correct-by-construction) | **CLOSED on evidence** in Expert 1's favour, verified: `purchase_price_diff` gate is `cost_method == 'standard'`, the only configured category is `fifo`, and `anglo_saxon_accounting` is FALSE. Two sufficient gates. Expert 2's 6 `product.template` rows exist but are not the cause | round 6 + Expert 4 addendum |

## Contradictions carried OPEN into the freeze

| ID | Contradiction | Why not closed |
|---|---|---|
| `S16-C-14` | Subledger/ledger divergence; and the ledger is not clean either | Root cause identified (`purchase_stock/_get_price_unit`); **remediation is not P01's to make** |
| `S16-C-15` | ~40–45 layers unexplained after 245 `consu` + 1,209 price-difference resolved | Residual rows not yet characterised |
| `S16-C-18` | **Buddhist-era extent disputed between two experts** — 484 values / 14 columns / 11 tables vs 12 pairs / 7 tables | Two methods, two answers; **neither adopted, not averaged.** Common floor recorded |
| **Certificate/payment denominators** | 1,407 vs 1,405 certs; 1,543 vs 1,488 payments | **Different denominators** (`done` vs all; payments vs items). Both recorded |
| `S16-B-05` | Deletion reproduces the zero-link signature published for series 18 and 19 | **Untested in those deployments.** Highest-ranked open item |

**Standing rule reaffirmed at freeze: a preserved disagreement is a result, not a failure.** Three of the five
open items above are disagreements between competent parties that P01 declines to resolve by preference.
