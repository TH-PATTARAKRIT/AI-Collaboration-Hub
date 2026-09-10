# VDR_EXCLUSION_REGISTER.md
# Every cell removed from a denominator, with authority

Session `[SMEPLUS-26-09-10-VDR-PREP-003]` · Layer: **LAYER 1 — CLEAN-ROOM.** Register version **R2**.

This register exists because round R1 did not have one. 180 cells were removed from two denominators
without a register, without a reviewer and without a status, and the two percentages concerned rose to
100.00% as a direct result (`CH-01`). **All 180 have been restored.**

---

## 1. Rule

A cell leaves a denominator by exactly one of two routes:

| Route | Requires |
|-------|----------|
| **`NA` by class** | an entry in the applicability rule table, fixed before measurement, applying to **every** item of that class without exception |
| **Exclusion** | a row in this register: Learning ID set · reason · **evidence** · reviewer · status |

**A per-row `NA` that is not in this register is a defect, not an exclusion.** *Unknown* is neither.

## 2. Exclusions in force

| # | Items | Reason | Evidence | Reviewer | Status |
|---|-------|--------|----------|----------|--------|
| — | **none** | — | — | — | — |

**The register is deliberately empty.** Every cell that R1 removed has been returned to its denominator
and graded against the evidence, including the grade `NOT_DETERMINED`, which R1 did not possess.

## 3. What was restored, and what each cell now says

| Set | n | R1 disposition | R2 disposition |
|-----|--:|----------------|----------------|
| Buttons that are framework discard controls | **48** | `NA` — *"the process belongs to another domain"* — **false against source** (`CH-02`) | **applicable · DETERMINED · not research-verified.** Condition corrected to: *framework discard control declared in a domain module; no method executes in this or any domain* |
| Buttons genuinely invoking a method outside the boundary | **4** | `NA`, same reason | **applicable · NOT_DETERMINED** — the reason is true for these four, and a true reason is still not an exclusion |
| Extension menus whose action is owned outside the domain census | **38** | `NA` | **applicable · NOT_DETERMINED** — a scope statement, never verified |
| Handoff elements' runtime cell | **90** | `NA` — *"that domain's measurement, not this one's"* | **applicable · NOT_DETERMINED** — their own reachability field reads `UNMEASURED`, which is the honest value |
| **Total restored** | **180** | | |

## 4. `NA` by class — the corrected rule table

Two cells of the R1 table were wrong against the code that ran, and are corrected here:

| Class | R1 published | R2, matching the executed register |
|-------|-------------|-----------------------------------|
| `HANDOFF` | SOURCE · **RUNTIME** · CROSS_MODULE | SOURCE · **RUNTIME** · CROSS_MODULE — *unchanged; it was the register that was wrong, and the register is now corrected to match* |
| `BUTTON` · `MENUX` | PROCESS applicable to the whole class | PROCESS applicable to the whole class — *unchanged, and now true of every row* |

**The rule table did not move. The register moved to obey it.** That direction matters: when a published
rule and a published measurement disagree, correcting the rule to fit the measurement is how a
denominator quietly becomes whatever the result needs.

## 5. The three grouping containers — a class correction, not an exclusion

`LI-INV-MENU-0028`, `-0034`, `-0042` carry `kind: CONTAINER` in their own detail field and invoke
nothing. Five dimensions are now `NA` on them **by the container rule**, which applies to every node of
that kind (the register holds 17 such nodes; 14 were already correct). This is a rule-table application
that R1 failed to make, not a bespoke removal — and it is recorded here because a reader is entitled to
see every cell that left a denominator, whatever route it took.

Effect: applicable cells **30,921 → 30,906**.

## 6. Denominator lineage

| Version | Applicable cells | Why it changed |
|---------|-----------------:|----------------|
| V3 as published (R1) | 30,741 | — |
| V3 under its own published rule table | 30,921 | the 180 were never authorised to leave |
| **V4 (R2, current)** | **30,906** | 180 restored, 15 removed by the container rule |

Prior calculations are preserved, not overwritten. **No denominator in this programme may change again
without an entry in this register.**
