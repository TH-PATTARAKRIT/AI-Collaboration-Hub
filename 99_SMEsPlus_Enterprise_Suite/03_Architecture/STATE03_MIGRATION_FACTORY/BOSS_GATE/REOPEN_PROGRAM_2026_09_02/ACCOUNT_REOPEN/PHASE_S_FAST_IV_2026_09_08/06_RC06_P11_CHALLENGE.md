# 06 — `RC-06` P11 DEPENDENCY CHALLENGE

**Frozen surface** `corr/p11-phase-s-remediation-2026-09-07-001` @ `9d4ecdc744fbbb0e502a0b907f59c301bdf7812c`
**Lane** C — dependency release
**Dependency** `RC-05`
**Result** `RC-HOLD — REQUIRED EVIDENCE OR INDEPENDENCE UNAVAILABLE`

## 1. Exact scope restated before testing (prompt §10)

Run **only after** `RC-05` establishes the P08 premise. Verify P11 `Q-P11-04`, the `F-02`
withdrawal/re-statement, method-rule withdrawal consistency, and that **no live bounded carrier still
treats the superseded P08 premise as current authority**.

## 2. Dependency state — exact, per prompt §4 Lane C

Prompt §4: *"If `RC-05` reaches FAIL or HOLD, keep `RC-06` blocked with exact dependency evidence."*

`RC-05` terminal result this session = `RC-HOLD — REQUIRED EVIDENCE OR INDEPENDENCE UNAVAILABLE`
(`05_` §6). **`RC-06` is therefore blocked, and the block is recorded with its cause rather than
inherited.**

**The dependency is unchanged but its character has changed.** At `9a5699e` `RC-06` was blocked
because `RC-05` was thought unrunnable for want of host evidence. `05_` §3–§5 establishes that the
host evidence is present and integrity-verified. **`RC-06` is now blocked solely by executor
eligibility, one link up the chain** — not by any missing artefact.

## 3. Not run

`RC-06` was **NOT RUN**. `Q-P11-04` was not tested, the `F-02` withdrawal was not certified or
refused, method-rule withdrawal consistency was not checked, and **no sweep for live carriers of the
superseded P08 premise was executed**. That last one matters: `[[smeplus-peer-status-field-rule]]`
records P10 promoting an UNRESOLVED blocker to an adopted rule, and
`[[smeplus-narrow-negatives-survive]]` records that the widest-scoped negatives rot first. **A carrier
sweep that was never run must not be read as a sweep that found nothing.**
