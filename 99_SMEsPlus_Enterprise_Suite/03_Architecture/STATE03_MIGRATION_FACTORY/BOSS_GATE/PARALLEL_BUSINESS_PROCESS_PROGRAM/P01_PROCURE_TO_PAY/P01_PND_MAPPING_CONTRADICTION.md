# P01 — PND FORM MAPPING CONTRADICTION

Session: `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`
Layer: **1.**
**P01 makes no statutory determination. Which form is correct is P07's, and is held.**

---

## 1. THE CONFLICT — CONFIRMED

| | Implementation A | Implementation B |
|---|---|---|
| Where | the v18-line custom copy | the v19-line custom copy |
| Rule | a **corporate** counterparty maps to one form, an individual to the other | **the reverse** |
| Location | the same file, the same two lines, in both copies | |
| Switch between them | **none** — one code hunk, two literals, no configuration | |

Classification: **FACT VERIFIED** — read directly in both copies by this session and
independently by an expert.

**Deployed owner:** Implementation **B**, present in both v19 databases and retained by a newer
module body. The certificate module is installed in all three readable databases.

---

## 2. THE REFINEMENT THAT CHANGES WHAT THIS MEANS

> **Neither mapping demonstrably governs, because the dominant creation route lets the operator
> choose the form by hand.**

In the v16 deployment, corporate counterparties appear on **both** forms — 4,437 on one and
749 on the other. That distribution cannot be produced by either automatic mapping. The
explanation found by the independent expert is that certificates are predominantly created
through a **wizard in which the operator picks the form**, bypassing the automatic rule
entirely.

In the two v19 databases the automatic rule has no observable effect either: one certificate
exists in total and its form is unset; the other database has none.

Classification: **FACT VERIFIED** for the distribution; **SUPPORTED INTERPRETATION** for the
attribution to the wizard route.

This is recorded as `ERR-P01-14`: the code-level contradiction stands, but the inference *"at
least one deployment misclassifies every certificate"* **does not follow** and is withdrawn.

---

## 3. WHY THIS IS HARDER THAN A CODE FIX

| If the problem were | The fix would be |
|---|---|
| Two implementations disagree | choose the correct one |
| **What is actually the case** | **decide who is entitled to determine a statutory classification, and stop a free choice from overriding it** |

Three independent places currently decide the form: the automatic rule (two contradictory
versions), the operator's choice in the wizard, and — reported by the expert and **not
re-derived here** — free-text withholding-tax names that also carry a form.

---

## 4. THE INPUT IS ALSO CONTESTED

Peer **P07** records that vendor legal personality **must be a typed attribute**, and that the
boolean "is a company" flag is the wrong instrument — it is `BLOCKING for P07`.

Both implementations key their mapping off exactly that boolean.

So the two copies disagree about a mapping whose **input** a peer process has already ruled
inadequate. **P01 accepts P07's position on the input and does not contest it.**

---

## 5. DISPOSITION

| Axis | Status |
|---|---|
| Code-level contradiction | **CONFIRMED — FACT VERIFIED** |
| Which copy is deployed | **Implementation B** in the v19 line; `DEP-P01-01` for the rest |
| Which mapping is correct | **`HOLD — STATUTORY EVIDENCE REQUIRED` — P07 owns it** |
| Whether either mapping governs in practice | **CONTRADICTED by live data** — the operator route dominates |
| Who *should* determine the form | **BOSS / target-design decision.** P01 states the evidence only |

---

## 6. WHAT P01 HANDS P07

1. Two contradictory automatic mappings, with the deployed one identified.
2. Evidence that the automatic mapping is bypassed on the dominant route, with counts.
3. The observation that the classification input is a boolean flag P07 has already rejected.
4. A third and fourth decision surface — the wizard, and free-text names — reported by an
   expert and **flagged as not re-derived by P01**.
5. **No statutory opinion whatsoever.**
