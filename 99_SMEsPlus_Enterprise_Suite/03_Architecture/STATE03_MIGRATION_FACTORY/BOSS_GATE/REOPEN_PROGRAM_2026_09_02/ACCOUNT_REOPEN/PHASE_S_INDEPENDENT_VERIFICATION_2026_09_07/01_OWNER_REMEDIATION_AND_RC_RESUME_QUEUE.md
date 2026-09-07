# Phase S Independent Verification — Owner Remediation and RC Resume Queue

Session: `[SMEPLUS-26-09-07-ACC-PHASE-S-IV-001]`
Authority: `PHASE-S/Q-BOSS-02` @ `2930723fbd45d8c4dada26197963ad6285d6c502`
Independent verification branch: `audit/account-phase-s-independent-verification-2026-09-07-001`

## 1. Control Objective

Contain the owner-publication boundary breach, complete the missing P06 repairs, freeze compliant correction surfaces, and resume `RC-01`…`RC-06` without resetting research or rewriting history.

**Do not force-reset any moved branch. Do not delete any owner correction commit. Preserve all current commits as audit lineage.**

## 2. Required Owner Publication Containment

Each owner must create a NEW correction branch. The branch must preserve a direct immutable mapping to:
- original frozen owner SHA;
- current correction commit already published in-place;
- exact correction artefacts carried forward;
- explicit statement that prior in-place publication is preserved as control-failure lineage and is not erased.

Recommended branch family (owner may use a compliant equivalent while preserving exact mapping):

| Owner track | New correction branch basis |
|---|---|
| P06 IEV | frozen `b423eff` + published repair `692ea27` |
| P06 source | frozen `1b018c1`; execute remaining source repairs there |
| P08 source | frozen `00ccd66` + published repair `c7cfd8a` |
| P08 IEV | frozen `bd95d1d` + published repair `d685176` |
| P09 | substantive frozen `4778792` + owner correction `2079a25` |
| P11 | frozen `dc4cc4a` + owner correction `ce0cc2b` |

The independent verifier does not create these owner branches and does not mutate owner evidence.

## 3. P06 Mandatory Remediation Before RC-03 / RC-04

### `P06-RQ-01` — queue target correction
Re-issue `Q-P06-02` against the actual source-track location:
`G02_RECOVERY_2026_09_06/P06_VERIFICATION_TOOL_DEFECT_REGISTER.md`:45,
not the IEV file named by the original queue.

### `P06-RQ-02` — 25 vs 26 adjudication
The mandatory enumeration found `IEV-D-01…IEV-D-26` = **26**, while the queue adopted 25.
Do not silently substitute. Publish a bounded disposition explaining whether `IEV-D-26` belongs to the material-defect denominator and update every dependent total only after that disposition.

### `P06-RQ-03` — execute source count corrections
Execute `Q-P06-03` on the compliant source correction branch, including the blocker/open-item/veto/author-error families and `P06-B-58` re-scaling.

### `P06-RQ-04` — execute archive-pattern correction
Execute `Q-P06-04`: use a proved-to-fire pattern, publish grep mode + command + output + positive control, and re-state or withdraw the 1,752-directory generalisation.

Only after `P06-RQ-01…04` publish immutable SHAs may `RC-03` and `RC-04` start.

## 4. P08 Resume Condition for RC-05

Republish the existing source and IEV corrections on compliant correction branches.
Provide independently executable evidence for the exact-arithmetic balance measurement:
- instrument/script or exact executable method;
- frozen input/extract location;
- population identity for DB-SM / DB-BK / DB-EV;
- exact / 1e-7 / 1e-4 / 0.005 outputs for computed and stored balance;
- discriminating positive control.

The P08 → P11 written notification is already published and must be carried forward by immutable reference.

## 5. P09 Resume Condition for RC-01

Republish `Q-P09-01` and `Q-P09-02` on a compliant NEW correction branch.
Freeze the exact six-correction surface and provide a repository-wide search method sufficient for the independent verifier to test questions A–I in `Q_P09_02_CHALLENGE_SCOPE_PREPARED_NOT_RUN.md`.

`AAS+-VETO-04` remains standing until `RC-01` completes and findings are dispositioned.

## 6. P11 Resume Condition for RC-02 / RC-06

Republish `Q-P11-01…04` on a compliant NEW correction branch.
Before freezing the challenge surface:
- re-resolve P09 after `2079a25` and state the post-P11 delta explicitly;
- acknowledge the already-published P08 `Q-P08-01` written notification as received evidence, without editing P08;
- preserve `F-02` and the derived method-rule withdrawal exactly as lineage;
- publish occurrence enumerations in a verifier-reproducible form.

`RC-06` remains dependent on independent establishment of the P08 numerical premise under `RC-05`.

## 7. Independent Verification Order

The verifier will resume in this order when compliant frozen surfaces exist:

1. `RC-01` — P09 six-correction surface.
2. `RC-05` — P08 exact-arithmetic correction and notification.
3. `RC-02` — P11 re-pin / HO / B-38 surface.
4. `RC-06` — P11 F-02 and method-rule withdrawal, after RC-05 premise verification.
5. `RC-03` — P06 IEV totals, after 25-vs-26 disposition.
6. `RC-04` — P06 source corrections and archive negative, after the source surface exists.

Order may run in parallel where dependencies permit; no RC may be self-run by its owner.

## 8. Gate Preservation

No Veto discharge.
No Phase S PASS.
No Functional Design.
No merge/release.
No peer-owner mutation.
No Boss decision inferred from silence.

No Evidence = No Progress.
Never Skip Gate.
Boss is the sole Final Approver.
