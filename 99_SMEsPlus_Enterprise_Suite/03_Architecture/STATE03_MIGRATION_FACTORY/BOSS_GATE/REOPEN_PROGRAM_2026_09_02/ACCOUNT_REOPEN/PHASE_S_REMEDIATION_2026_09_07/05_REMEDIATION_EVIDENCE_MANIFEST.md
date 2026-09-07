# 05 — REMEDIATION EVIDENCE MANIFEST

**POPULATION:** every file under `PHASE_S_REMEDIATION_2026_09_07/` · **PATTERN:** `find . -type f` · **UNIT:** one file.

| Files | Roll-up SHA-256 |
|---|---|
| **7** | `83dc2e66d7384eafcfd9b9146ce5f0e8fcee15c38ff14febc8adc9fe3d48bec0` |

> **Coverage assertion:** `find` returned **7**, manifest processed **7** — **both re-measured in this commit, after the last edit to any listed file** (`P11-G-15`).

## Cross-branch evidence this session produced

| Branch | SHA |
|---|---|
| `corr/p11-phase-s-remediation-2026-09-07-001` | `9d4ecdc` |
| `corr/p08-phase-s-rc05-prep-2026-09-07-001` | `e368d11` |

## Frozen primary inputs (outside the repository, hashed)

| Label | SHA-256 |
|---|---|
| `DB-SM` | `ca77818b6daa1184199018add4e695cb75112e25608b0a664bfbf3ada5118ae2` |
| `DB-BK` | `1a67347491a056d1e86675568a68473aa239c96396988d21493b805970e151a3` |
| `DB-EV` | `eade5512bbab1bd06f4f3a521c9468eadc08facaeb7e551631ae51be3a85cb0f` |
| `DB-T2` | `84a75479e432be21bc23e4986821f0307e4035e97d6398985ee5de52adb837a4` |

```
0af87edcfc7b383e6dfa6bb71c6e3365804e39e3ec0c260340127e1a1f6370f6  00_PHASE_S_REMEDIATION_PRE_FREEZE.md
1c6329541ff87aa73173e70e2a0b0d8e0416a6734564328cb8f429390555776f  01_P11_CO_F_01_PIN_INSTRUMENT_REPAIR.md
959b7577572826b0fc8a870a559cc98bc2cc0751fdc2cf49825b16bc708dad95  02_P11_CO_F_02_STALE_INBOUND_REPAIR.md
5af291ab4ad0702e79bcc580c9e01bc82cd04b529990e0c147bf93034bd6efa3  03_P08_RC05_REPRODUCIBILITY_PACKAGE.md
9896bdafcede02c7473ae407cd3c31ef0d7eacf81967b6de2d346c78165ba6ee  04_RC01_RC06_VERIFIER_HANDOFF_MATRIX.md
8ff4226f43c5d926304cb717c044f6f06b56405271c0c58800f68064563f3e69  06_REMEDIATION_CHECKPOINT_REGISTER.md
b41837d42dfc16731f33b6bcf2601dde109132752b31811b623027dc962b65ab  PHASE_S_REMEDIATION_AUTO_RESUME.md
```
