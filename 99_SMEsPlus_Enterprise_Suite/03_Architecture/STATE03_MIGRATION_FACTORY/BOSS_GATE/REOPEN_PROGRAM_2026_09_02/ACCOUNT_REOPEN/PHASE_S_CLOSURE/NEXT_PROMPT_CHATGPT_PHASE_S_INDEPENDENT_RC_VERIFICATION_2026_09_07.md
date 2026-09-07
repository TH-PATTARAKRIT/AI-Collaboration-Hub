# [SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001]
# CHATGPT NEW SESSION — STRUCTURALLY INDEPENDENT RC-01…RC-06 VERIFICATION
# /L99999.99999

## 0. APPOINTMENT AND ROLE

Project: SMEsPlus ENTERPRISE SUITE
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Verifier: **ChatGPT GPT-5.6 Sol**
Boss: Sole Final Approver
Mode: NEW ISOLATED VERIFICATION SESSION / READ-ONLY OWNER EVIDENCE / EVIDENCE-FIRST

Boss appointment and governing ruling:
`BOSS_DECISION_Q_BOSS_03_AND_INDEPENDENT_VERIFIER_APPOINTMENT_2026_09_07.md`

This session is verifier/challenger only.
It must not author or execute the repair under review.
It must not mutate owner branches.
It must not self-discharge a Veto.
It must not declare Phase S closed.

No Evidence = No Progress.
Never Skip Gate.

## 1. HARD PRECONDITION — DO NOT START RC WORK EARLY

Before any `RC-*` execution, verify that the Claude remediation session has published:
`REMEDIATION-A — ALL RC SURFACES FROZEN AND READY FOR INDEPENDENT VERIFIER`

Required handoff artefact:
`04_RC01_RC06_VERIFIER_HANDOFF_MATRIX.md`

For every RC row require:
- owner;
- immutable correction SHA;
- exact bounded surface/files;
- accessible frozen inputs;
- control definitions;
- expected challenge action;
- dependencies;
- evidence path.

If remediation is not at `REMEDIATION-A`, STOP:
`IV-PRECONDITION-HOLD — VERIFIER HANDOFF NOT COMPLETE`.

Do not infer readiness from moving branch heads.

## 2. STRUCTURAL INDEPENDENCE CONTROLS

For each RC separately record:
1. verifier did not author/execute the repair;
2. owner did not select the control set where prohibited;
3. frozen SHA read directly;
4. owner evidence treated read-only;
5. result independently reproduced where the RC requires reproduction;
6. verifier's own instruments have positive, negative and failure/discriminating controls;
7. every material finding is re-read against source evidence before adoption;
8. disagreements preserved;
9. verifier publishes independent evidence on a separate audit branch;
10. no PASS/Veto discharge inferred from absence of findings.

If any independence control fails for an RC, classify that RC:
`HOLD — STRUCTURAL INDEPENDENCE NOT PROVEN`.

## 3. RC EXECUTION ORDER

Execute in dependency-safe order unless the handoff matrix proves a different required order:

### `RC-01` — P09 corrected surface
Bounded to the six corrections / exact corrected surface defined by XRECON and the current handoff.
Do not re-challenge the whole P09 package.
Attempt to falsify truth-at-location, superseded lineage, single authoritative disposition, no new contradiction, no peer mutation.

### `RC-05` — P08 exact-arithmetic / corrected reconciliation handoff
Boss ruling `Q-BOSS-03`: documentary inspection alone is insufficient.
Must independently execute the P08-provided instrument/procedure against frozen inputs.
Reproduce the in-scope balance/tolerance results and controls.
If frozen executable inputs are absent or inaccessible:
`RC-05 = HOLD — MISSING REPRODUCIBLE EVIDENCE`.

### `RC-02` — P11 post-correction package
Run only after the latest P11 remediation SHA includes `CO-F-01` and `CO-F-02` corrections where they affect the RC-02 surface.
Test peer-currentness/pin behaviour from the actual repaired instrument, not from prose.
Prove the instrument consumes immutable pins and can fail when a pin/control is changed.

### `RC-06` — P11 `F-02` / derived-rule correction
Run after RC-05 because P11 consumes P08's corrected evidence.
Verify that the stale falsification is withdrawn/re-stated consistently and that no live carrier still treats the no-referent figure as current authority.
Do not adjudicate broader method-rule truth beyond the evidence.

### `RC-03` — P06 IEV revised population/totals surface
Verify the current authoritative denominator and enumeration, including the proven 26-vs-25 correction, using independent count forms and controls.
Challenge revised totals at the actual frozen IEV surface.

### `RC-04` — P06 source corrections / archive-negative surface
Verify corrected count families, P06-B-58 scaling and the archive-negative instrument with a pattern proven to fire plus positive control.
Do not reopen unrelated P06 findings.

## 4. CHALLENGE METHOD

For every RC:
A. Restate exact scope before testing.
B. Attempt falsification before confirmation.
C. Run at least two independently shaped checks for material counts where feasible.
D. Every zero/negative requires a positive control inside the same population.
E. Any control selected by the property it tests is invalid.
F. Compare member identity when population identity matters; equal cardinality is insufficient.
G. Never rely on a moving `origin/<branch>` when the evidence contract requires immutable SHA.
H. Record verifier errors and reruns; do not erase them.

Allowed finding dispositions:
- `SUPPORTED`
- `CONTRADICTED`
- `NARROWED`
- `MISSING EVIDENCE`
- `ROUTED — OUTSIDE RC SCOPE`

Each finding must state materiality and exact file/claim/evidence.

## 5. RC RESULT STATES

Each RC receives exactly one result:
- `RC-PASS — BOUNDED SURFACE SURVIVES INDEPENDENT CHALLENGE`
- `RC-PASS-WITH-NONMATERIAL-FINDINGS`
- `RC-FAIL — MATERIAL DEFECT FOUND`
- `RC-HOLD — REQUIRED EVIDENCE OR INDEPENDENCE UNAVAILABLE`

`RC-PASS` is not Phase S PASS and does not itself discharge any Veto.

If `RC-FAIL` requires a repair:
1. freeze verifier finding;
2. route exact bounded correction to the owner;
3. owner repairs on a new correction ref;
4. freeze again;
5. re-run only the changed RC surface.
Never let the verifier author the repair it will re-verify.

## 6. POST-RC CROSS-PACKAGE VERIFICATION

After all six RCs have terminal results, perform independent cross-package sweeps for:
- withdrawn/superseded claims still consumed as current;
- stale SHA/currentness references;
- handoff sent vs handoff received;
- duplicate root defects vs manifestations;
- contradiction propagation;
- producer-qualified namespaces;
- P07 read-only closure impact;
- Veto lifting dependencies;
- Boss-only decision dependencies.

Use controls for every sweep. Record any verifier instrument defect and re-run after correction before accepting results.

## 7. VETO DISPOSITION PREPARATION

For all standing Phase S Vetoes, prepare evidence-backed recommendations only:
- `DISCHARGEABLE BY VERIFIED EVIDENCE`
- `PARTIALLY SATISFIED — REMAINS OPEN`
- `UPHELD`
- `SUPERSEDED WITH LINEAGE`
- `ROUTED`
- `BOSS DECISION REQUIRED`

The verifier does NOT perform the final discharge if authority is reserved elsewhere.

## 8. PHASE S CLOSURE TEST

After RC and cross-package work, independently test every Phase S closure criterion from the canonical closure prompt.
No criterion may be marked TRUE from documentary assertion alone where its own rule requires independent reproduction/challenge.

If all criteria are proven or defensibly dispositioned under the governing closure test, publish:
`CP-SC-14 — READY FOR BOSS PHASE S FINAL DECISION`.

If not, publish one of:
- `IV-CLOSEOUT-B — BOUNDED MATERIAL BLOCKER REMAINS`, exact item named;
- `IV-CLOSEOUT-C — REQUIRED EVIDENCE UNAVAILABLE`, exact evidence named.

## 9. REQUIRED OUTPUTS

Publish on a NEW independent audit branch:
- `00_IV_APPOINTMENT_AND_PRECONDITION.md`
- `01_RC01_P09_CHALLENGE.md`
- `02_RC05_P08_CHALLENGE.md`
- `03_RC02_P11_CHALLENGE.md`
- `04_RC06_P11_CHALLENGE.md`
- `05_RC03_P06_IEV_CHALLENGE.md`
- `06_RC04_P06_SOURCE_CHALLENGE.md`
- `07_RC_RESULT_REGISTER.md`
- `08_POST_RC_CROSS_PACKAGE_VERIFICATION.md`
- `09_VETO_DISPOSITION_RECOMMENDATION.md`
- `10_PHASE_S_CLOSURE_CRITERIA_INDEPENDENT_TEST.md`
- `11_PHASE_S_FINAL_BOSS_DECISION_EVIDENCE_PACK.md`
- `IV_CHECKPOINT_REGISTER.md`
- `IV_AUTO_RESUME_STATE.md`
- `IV_EVIDENCE_MANIFEST_SHA256.md`

Every material claim must carry exact Branch + Commit SHA + Artifact Path + verifier status.

## 10. FINAL STOP

If and only if the evidence supports it, stop at:
`READY FOR BOSS PHASE S FINAL DECISION`.

Do not start Phase SA.
Do not close Phase S on behalf of Boss.
Boss is the sole Final Approver.
