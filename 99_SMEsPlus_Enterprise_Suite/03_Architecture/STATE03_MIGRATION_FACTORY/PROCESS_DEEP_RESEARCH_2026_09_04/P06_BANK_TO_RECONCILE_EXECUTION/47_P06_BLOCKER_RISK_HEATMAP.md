# P06_BLOCKER_RISK_HEATMAP.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S02)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Companion to:** `46_` (severity by impact). This file plots **impact against reachability**, because the two orderings disagree and the disagreement is the point.

---

## 1. Reachability scale — stated before use

| Level | Meaning |
|---|---|
| **R1 — routine** | occurs in ordinary correct operation; no privilege beyond a normal user's job |
| **R2 — ordinary privilege** | needs a role an accounting team normally holds |
| **R3 — administrative** | needs an administrator, or a specific configuration choice |
| **R4 — conditional** | needs an uncommon configuration, module install, or company topology |
| **R5 — unverified** | source-reachable, runtime unverified, or deployment-dependent |

---

## 2. The heatmap

Rows are impact. Columns are reachability. **Read top-left first.**

| | **R1 routine** | **R2 ordinary privilege** | **R3 administrative** | **R4 conditional** | **R5 unverified** |
|---|---|---|---|---|---|
| **CRITICAL** | **B-10** duplicate ingestion | **A6/B-46** un-reconcile past close · **B-13** identity mutable | — | **B-26** unowned bank account | **B-50** unauthorised ledger deletion |
| **CRITICAL (always-on)** | **B-06** no bank-confirmation fact — present in every operation, not "reached" at all | | | | |
| **HIGH** | **B-11** completeness self-satisfies · **B-14** silent drops | **B-04** four payment doors · **B-07** two writers · **B-22** write-off uncontrolled · **B-29** identity scope | **B-12** deletability toggle · **B-37** re-dating module · **B-52** write-off ACL | **B-25** net settlement · **B-30** webhook window · **B-38** auto-posting · **B-45** lock inheritance | **B-17** no fee owner · **B-44** generation gap · **B-55** filtered build |
| **MEDIUM** | **B-18** no ageing · **B-23** silent `False` · **B-32** inverted tolerance | **B-05** · **B-15** · **B-16** · **B-19** · **B-24** · **B-49** | **B-36** · **B-43** · **B-47** · **B-48** | **B-20** · **B-33** · **B-34** · **B-35** · **B-28** | **B-21** · **B-31** |
| **LOW** | — | — | **B-51** | **B-39** · **B-53** | — |
| **INFORMATIONAL** | — | — | — | — | B-01 · B-02 · B-03 · B-40 · B-41 · B-42 · B-54 |
| **UNRANKED** | — | — | — | — | B-08 · B-09 |

---

## 3. The top-left cell is the finding

**HM-F-01 — `B-10` sits alone in CRITICAL × R1, and it is the most mundane item in the package.**
Its precondition is *"import a bank statement file twice"*. No privilege. No unusual configuration. No hostile actor. For a CSV or QIF file the system creates a complete second set of statement lines **and posted journal entries**, silently, because a null identity is treated as "not a duplicate" at all three enforcement points.

**Ranked by impact, `B-50` leads. Ranked by reachability, `B-10` leads.** Both are in the same severity band, and they demand different responses:
- `B-50` is a **removal** decision — take the module off the addons path, or prove it is not there.
- `B-10` is a **design** decision — bank-event identity must be mandatory and schema-enforced.

**A single ordered list would have concealed one of these. That is why the prior rounds' absence of a severity model was a real defect and not a formatting gap.**

---

## 4. `B-06` is off the grid on purpose

**HM-F-02 — "No field means the bank confirmed this" has no reachability, because it is not reached — it is the permanent state of the system.**
Every reconciliation, every settlement assertion and every payment state in the package rests on its absence. Placing it in an R-column would imply a precondition it does not have. It is recorded in its own row and it is the **single most consequential item for the target design**, because it cannot be fixed by a control — only by creating the fact.

---

## 5. Concentration

| Reachability band | CRITICAL | HIGH | Total C+H |
|---|---|---|---|
| R1 routine | 1 (+1 always-on) | 2 | **4** |
| R2 ordinary privilege | 2 | 4 | **6** |
| R3 administrative | 0 | 3 | **3** |
| R4 conditional | 1 | 4 | **5** |
| R5 unverified | 1 | 3 | **4** |

**HM-F-03 — Ten of the twenty-three CRITICAL/HIGH blockers are reachable at R1 or R2 — that is, by an ordinary accounting user doing ordinary work.** The risk in P06 is not concentrated in exotic paths. It is concentrated in the daily ones: importing a statement, matching a line, un-matching a line, registering a payment.

**HM-F-04 — Four of the twenty-three sit at R5, and three of those four are evidence-boundary items** (`B-44` generation gap, `B-55` filtered build, `B-17` bounded negative). **A quarter of the high-severity population is uncertain because of what this programme does not know about its own target, not because of what the system does.** One module-registry export moves most of that column.

---

## 6. What the heatmap says about sequencing

Not a plan — the Boss sequences work. But the grid supports three observations:

1. **The R5 column is the cheapest to collapse.** One `ir.module.module` export from the target resolves `B-44`, materially bounds `B-50`, and improves `B-31` and `B-19`. Nothing else in the package moves four items at once.
2. **The R1/R2 cells cannot be closed by evidence at all.** They are design decisions — identity, confirmation, close discipline. More research will not change them.
3. **The R3/R4 cells are configuration questions** and mostly resolve to "what is actually switched on", which is the same export as (1).

---

## 7. Honest limits of this heatmap

- **Reachability is assessed from source, not from observed use.** No system was exercised.
- **Impact is assessed against the criteria in `46_` §2**, which are this session's criteria, published before assignment so they can be argued with.
- **No likelihood is assigned.** Likelihood needs a deployment and a user population; this session has neither. Reachability is a proxy for precondition difficulty, not a probability.
- **`B-53` is ranked LOW *to P06*** because P05 owns it. Its severity in P05's own register is P05's to set, and the two may legitimately differ.
