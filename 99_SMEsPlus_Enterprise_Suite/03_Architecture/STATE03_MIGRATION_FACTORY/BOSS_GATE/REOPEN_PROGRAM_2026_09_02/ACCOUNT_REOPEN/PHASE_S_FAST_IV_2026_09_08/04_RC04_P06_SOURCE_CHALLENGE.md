# 04 — `RC-04` P06 SOURCE CHALLENGE

**Frozen surface** `corr/p06-source-phase-s-final-2026-09-07-001` @ `b5f5a211763568a4212d08954c835412f7728a0a`
**Lane** A — repository-only
**Result** `RC-HOLD — REQUIRED EVIDENCE OR INDEPENDENCE UNAVAILABLE`
**Cause** independence only. **The lane is executable today.**

## 1. Exact scope restated before testing (prompt §8)

Test `Q-P06-03`, `Q-P06-04` and the **re-issued** `Q-P06-02`. Verify count families, `P06-B-58`
scaling, and the archive-negative pattern **with a positive control**. Explicitly reconcile the known
**`:45` versus `:54`** contradiction. If material, **FAIL the exact bounded surface only** and route a
bounded correction; do not reopen unrelated P06 work.

## 2. Not run

`RC-04` was **NOT RUN**. No count family was re-derived, `P06-B-58` scaling was not tested, the
archive-negative pattern was not fired against a positive control, and the `:45`/`:54` contradiction
was **not** reconciled. The handoff states *"the `:45` row is unrepaired at this SHA by design and
contradicts `:54`"* — that is a declared, deliberate contradiction awaiting adjudication, **not a
defect this session found and not one it has cleared**.

## 3. Input-locality determination (executor-neutral)

`git grep -nE "/Users/|/Volumes/" b5f5a21 -- '*.py'` returns **no matches**. The surface is
`G02_OWNER_CORRECTION_2026_09_07/` including `P06_TO_P11_COUNT_CORRECTION_NOTICE.md`.
**No host-local input is required.**

## 4. Standing hazard carried to the eligible verifier

The archive-negative pattern is the exact shape `[[smeplus-executed-not-quoted-rule]]` and
`[[smeplus-synthetic-injection-control]]` were written for: **a pattern that cannot fire yields a
silence indistinguishable from absence.** The prompt's demand for a positive control on that pattern
is not a formality — in this programme an archive negative has been wrong twice
(`[[smeplus-archive-denominator-key]]`), on **format-versus-extension** and on **keying by
`database.uuid`**, the second time with the memory already written.
