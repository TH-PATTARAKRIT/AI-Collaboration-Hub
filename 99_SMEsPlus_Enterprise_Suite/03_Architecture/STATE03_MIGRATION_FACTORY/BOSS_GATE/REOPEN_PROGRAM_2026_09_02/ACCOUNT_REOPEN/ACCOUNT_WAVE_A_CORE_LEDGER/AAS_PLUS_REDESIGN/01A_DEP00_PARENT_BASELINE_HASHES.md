# 01A — `DEP-00` PARENT BASELINE HASHES (CONSUMPTION-TIME SNAPSHOT)

**`PROVISIONAL / NON-AUTHORITATIVE`** · governed by `01`

> The parent Method Convergence Closure package was **untracked in git and unpushed** when this
> session consumed it (`AASR-F-01`). These SHA-256 hashes fix **exactly what was read**, so that when
> the parent publishes its final package, delta revalidation has a byte-level baseline to diff
> against rather than a recollection.
>
> **This is a preservation record, not an adoption record.** These files are not authoritative and do
> not supersede whatever the parent finally publishes. `MCC_J`, the MCC gate report and the MCC
> evidence manifest are **absent from this list because they do not exist**.

Snapshot taken 2026-09-04 · source: `ACCOUNT_WAVE_A_MCC_2026_09_04_EXECUTION` working tree
Files: **20** · Parent git HEAD at snapshot: `33cdc6fa009c4eafcca543c253ccad19e97fd0dc` (the **MC** round's commit)

| SHA-256 | Path |
|---|---|
| `24fc1989a35c676c66d188ca10b8715f0c1835ba7c77845d577f351ecec6b96d` | `METHOD_CONVERGENCE_CLOSURE/ACCOUNT_WAVE_A_MCC_MASTER_RECONCILIATION.md` |
| `e1c8c0b8ef9e6bc4f48e088dff1789a7f3fd589b46dacb135e61d1541d2b2115` | `METHOD_CONVERGENCE_CLOSURE/LAYER2_MCC_EVIDENCE/MCC_E00_FX_RATE_PRIMARY_EVIDENCE.md` |
| `54a98c1e14b3353138250995666623e49fdc4d757f57b274121c9d8045a942d4` | `METHOD_CONVERGENCE_CLOSURE/LAYER2_MCC_EVIDENCE/MCC_E01_CONVERGENCE_PASS_CONTRADICTIONS.md` |
| `b42682f452400245ab1757f2d9f537ff20a54b957e0acbd0fa839b737eee204c` | `METHOD_CONVERGENCE_CLOSURE/LAYER2_MCC_EVIDENCE/mcc_scripts/README.md` |
| `c138479da9a16aaff0ea7ac69a92e2be575cd8e2e953497c6363b25740645725` | `METHOD_CONVERGENCE_CLOSURE/LAYER2_MCC_EVIDENCE/mcc_scripts/compliance.sh` |
| `e453f8b89ac64b23ba6d05895f9ce3ca09947d3959c96691cb9c8cb3ac86ff98` | `METHOD_CONVERGENCE_CLOSURE/LAYER2_MCC_EVIDENCE/mcc_scripts/mkmanifest.sh` |
| `afc0da4689cf22ba14a44a5cfbb602da8283d9ed5beba8e6e39423ed4a5a4a79` | `METHOD_CONVERGENCE_CLOSURE/LAYER2_MCC_EVIDENCE/mcc_scripts/ncscan.sh` |
| `b63ed11ce453ce57a0aabf51a778bdbcf940174ed67d728f14301241b889b88e` | `METHOD_CONVERGENCE_CLOSURE/LAYER2_MCC_EVIDENCE/mcc_scripts/recount.sh` |
| `9b93594d90502f8d5a5a15c96d982941406cb9aee91ea67b5dec87f4705c42a7` | `METHOD_CONVERGENCE_CLOSURE/LAYER2_MCC_EVIDENCE/mcc_scripts/v3.sh` |
| `00902c8deb54b6e24bbb125179fd5e9aa0cb9c1a522bd33726434978abe7b8bf` | `METHOD_CONVERGENCE_CLOSURE/LAYER2_MCC_EVIDENCE/mcc_scripts/xver.sh` |
| `fd479965d84ea5c7ded006862167b72c7723cd6371811a974aa99bf2aa995582` | `METHOD_CONVERGENCE_CLOSURE/MCC_A_CANONICAL_BASELINE_RECONCILIATION.md` |
| `a4c85968a3f166503252d435b2964369034ad29d5edc0d9926005f8da33f62d2` | `METHOD_CONVERGENCE_CLOSURE/MCC_B_GB03_ROOT_CLOSURE.md` |
| `971c12a9dcfd9a934a8cf38a80672b948283bf83a7b0ab3b6cf849bfd5a9ce32` | `METHOD_CONVERGENCE_CLOSURE/MCC_C_FX08_MCU13_FORENSIC_REVERIFICATION.md` |
| `949e7fd331e0bb540de76f51a48f52d83ec5bc557984e5436eb414fcc02a434c` | `METHOD_CONVERGENCE_CLOSURE/MCC_D_GATING_UNKNOWN_EXHAUSTION_REGISTER.md` |
| `4fb101287753941fdc8756b51140379594c2b0a47ffb3be208ac3279ca1ce5df` | `METHOD_CONVERGENCE_CLOSURE/MCC_E_DENOMINATOR_RECONCILIATION.md` |
| `b00d1d41550612d185617dda32df91030be197c4897683710cd80c169469ca65` | `METHOD_CONVERGENCE_CLOSURE/MCC_F_NEGATIVE_CLAIM_EXHAUSTION.md` |
| `746834e7755bcee61ba5f4f14caa11e57088bd72815b18d50e9f822aad97484f` | `METHOD_CONVERGENCE_CLOSURE/MCC_G_BALANCED_BUT_WRONG_FIXED_POINT_PROOF.md` |
| `09fc710e9d1584fbf15cb602d5bd4a85eb245449b0eab65bdbedc47b03d5efa0` | `METHOD_CONVERGENCE_CLOSURE/MCC_H_FIXED_POINT_CONVERGENCE_PROOF.md` |
| `d04c841ad0e401392f5911e2bf5afa8bdae24635ec4b2a256844d7fde0e2e251` | `METHOD_CONVERGENCE_CLOSURE/MCC_I_MC01_MC10_TARGETED_RERUN.md` |
| `80707554d2427d778c74b3003efc2ab12cbd097a2cd4b2bfa98f5144bc91378e` | `METHOD_CONVERGENCE_CLOSURE/MCC_K_REUSABLE_METHOD_DELTA.md` |

## Delta revalidation use

1. Re-hash the parent's final published package.
2. Any path whose hash differs from this table changed after consumption → **every `01` row citing it
   is re-tested**.
3. Any path present there and absent here is **new evidence this synthesis never saw** — including
   `MCC_J`, which has never been read by anyone.
4. Any path present here and absent there was **withdrawn** → designs citing it move to `INVALIDATED`.
