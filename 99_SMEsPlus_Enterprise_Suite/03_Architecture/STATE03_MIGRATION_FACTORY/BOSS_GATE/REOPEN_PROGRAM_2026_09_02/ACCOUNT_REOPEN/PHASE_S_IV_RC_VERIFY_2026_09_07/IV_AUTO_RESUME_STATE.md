# IV AUTO-RESUME STATE

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001]`
**Branch** `audit/account-phase-s-iv-rc-verify-2026-09-07-001`
**Terminal state:** `IV-CLOSEOUT-C — REQUIRED EVIDENCE UNAVAILABLE`

## 1. NEXT EXACT ACTION

**Boss dispatches the verifier prompt
`NEXT_PROMPT_CHATGPT_PHASE_S_INDEPENDENT_RC_VERIFICATION_2026_09_07.md` @ `0941161` to
ChatGPT GPT-5.6 Sol** — the party appointed by `Q-BOSS-03` §1 — **or rules otherwise per `11_` §2.**

**This is a dispatch, not a decision, if Path A is taken.** No owner action is required first.

## 2. State carried forward

| | |
|---|---|
| §1 precondition | **SATISFIED** — do not re-run it. `0941161` |
| Prior `IV-PRECONDITION-HOLD` @ `9d8ad70` | **SUPERSEDED WITH LINEAGE.** Do not consume it as current |
| Frozen refs | **6 of 6 current** at the SHAs in `04_RC01_RC06_VERIFIER_HANDOFF_MATRIX.md` |
| `RC-05` evidence | **complete and hash-verified** — 4 dumps, both `pg_restore` versions. **Do not re-route to P08 for evidence** |
| `RC-01` inputs | root exists, 13,515 `.py`; source `k1_population.json` **in-repo**, not from the peer clone |
| `RC-06` | blocked on **two** independent grounds — independence **and** `RC-05` not certified. Lifting one does not clear it |
| `RC-07` | **NOT REQUIRED** — pointer-only |
| Vetoes | **0 dischargeable, 0 discharged.** Denominator is `IV-R-05` — **do not restate "17"** |
| Boss decisions | 51 open, 0 answered. **1 new item raised** (`11_` §2) |
| Closure criteria | 1, 2, 6 **FALSE**; 3 **RE-OPENED** by `IV-R-04`/`IV-R-05` |

## 3. Warnings for whoever runs the RCs

1. **The matrix's "controls published" column is owner-selected.** `AASP-P11-C3-VETO-04` forbids a
   control set drawn by the party it controls. **Draw your own**, especially for `RC-02`.
2. **The declared surfaces are narrower than the changed sets** in 4 of 5 lanes (`IV-R-01`).
   **Bound to the changed set**, or `RC-04` leaves 6 of 8 files untested and `RC-02` leaves 6 of 10.
3. **Do not trust a manifest's coverage assertion** — two of the three checked are false as stated
   (`IV-R-04`). Re-run the declared command.
4. **`q1.py` reads a path outside the repository.** Re-point it in-repo before executing `RC-01`.
5. **This session ran three defective instruments** (`07_` §5). All three were caught only by
   re-running in a **different command shape**, never by inspecting the first result — including one
   that returned a *favourable* answer about someone else's package.

## 4. Not done, and not to be inferred as done

**0 of 6 repairs tested.** No `RC-PASS`, no veto discharge, no `CP-SC-14`, no Phase S closure.
`PHASE S = NOT CLOSED.` Boss is the sole Final Approver.
