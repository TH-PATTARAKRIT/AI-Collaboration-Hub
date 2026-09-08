# ACCOUNT_ONE_PROMPT_EVIDENCE_MANIFEST_SHA256.md

**Prompt:** `[SMEPLUS-26-09-08-ACC-ONE-PROMPT-FINAL-CLOSURE-001]` · deliverable **11 of 12**
**Branch:** `audit/account-one-prompt-final-closure-2026-09-08-001`
**Classification:** LAYER 2 — AUDIT QUARANTINE

---

## 1. The population, declared — including its self-exclusion

| Clause | Declaration |
|---|---|
| **POPULATION** | every file under `…/PHASE_S_CLOSURE/ACCOUNT_ONE_PROMPT_FINAL_CLOSURE_2026_09_08/`, **EXCEPT `ACCOUNT_ONE_PROMPT_EVIDENCE_MANIFEST_SHA256.md` itself** |
| **PATTERN** | `find . -type f` — **not** `*.md`, so a non-markdown artefact could not hide from it |
| **PATH SET** | that one directory, non-recursive in effect because it has no subdirectories at this commit |
| **UNIT** | **one file** |

> **The self-exclusion is by definition, not by omission.** **A manifest cannot carry its own digest**: writing the hash changes the bytes that produced it. **An unstated exclusion and a missing file are indistinguishable to anyone recounting the directory**, which is why this clause is written rather than left to be inferred.

## 2. Coverage assertion — both halves measured in this run

| Measure | Value |
|---|---|
| files `find` returned (whole directory, manifest included) | **14** |
| files in the substantive population (excluding this manifest) | **13** |
| files this manifest **processed** | **13** |
| **substantive == processed?** | **YES** |
| manifest regenerated **after** it existed on disk, so the directory count includes it | **YES — the first generation reported 13/13/13 because the manifest was not yet written, and 13 was then the directory count. It is 14 now. A manifest that measures the directory before adding itself to it reports a figure that is true only for an instant.** |

**Both figures are produced by this regeneration. Neither is carried forward from an earlier manifest** — a carried-forward coverage assertion is how a previous manifest in this programme came to assert `86 = 86` falsely.

**Positive control:** the two Boss control files (`CLAUDE_DESKTOP_ONE_PROMPT_…`, `BOSS_RULING_NO_QUALITY_…`) and all twelve deliverables **must** appear in §4. They are not this session's work, and their presence proves the pattern reaches beyond what this session wrote.

## 3. Package roll-up digest

SHA-256 over the sorted list of per-file SHA-256 values, so one value fixes the whole surface:

```
07c5cc40f491f6033caf447da07fb43b221b15b74e5c1a62008f6dfdc5361e35
```

## 4. Per-file SHA-256 — 13 files

```
bf867e066f5e3b90f08c0832e5d3d1388dc89c8f4975f01fe442a599dfd86129  ACCOUNT_FINAL_BOSS_DECISION_MATRIX.md
41d01f77b717db2bcd6b03e1aee4fc4ce5222464c9e646543a3a7cd416994f18  ACCOUNT_FINAL_CROSS_PACKAGE_DELTA_RECONCILIATION.md
63e4dad9b55065bf8857598105084bdaaf7782bb2a073368b462f2e05a60cef7  ACCOUNT_FINAL_OWNER_SHA_REGISTER.md
96712a4e429e294836b7c22c895ea104b723ac44f9197b8cae16185e9724cda5  ACCOUNT_FINAL_VETO_RECOMMENDATION.md
4341c80ab810e954e2c0a4b69fe6aeeb963084c8e77549e245ddfdd8222da3fe  ACCOUNT_ONE_PROMPT_AUTO_RESUME_STATE.md
fceaa6b678098b78acd170e1885460235db94480d6e0d8f360cabb17ce3e3e8a  ACCOUNT_ONE_PROMPT_EXECUTION_REGISTER.md
f160a9d818a9a4aacfe4325fc8cf4b860a9b4b0c7c723a7fc443a7d9ce034080  ACCOUNT_PHASE_SA_INPUT_OUTPUT_READINESS_PACK.md
34419fc9bb4b89fff35dc61192938ecd2643468e2917d6a4d7cbe4ef259d2304  BOSS_RULING_NO_QUALITY_SCOPE_EVIDENCE_DEGRADATION_2026_09_08.md
99e5f1fe992cd97efeae78e5f4733665b20405da228395e4cb07a79bdc406915  CLAUDE_DESKTOP_ONE_PROMPT_ACCOUNT_FINAL_CLOSURE_TO_PHASE_SA_2026_09_08.md
70917beb8cc654723841f405826732e49b26cce07081a091c0012d0104d2c7fc  P06_FINAL_DELTA_EVIDENCE.md
d5c0e497bffd2e931dac5ad0ba8d2dc7b5cb28e1c1b2bd969bf81331891c6485  P08_FINAL_DELTA_EVIDENCE.md
1bfb03f316af3128aa6d261409808a72944a9c0baffa3d0db345f08e06a09530  P09_FINAL_DELTA_EVIDENCE.md
144a9b3835678a3b8240141777f7cad1752e54bfe56a5968d4e966e01e07e3a3  P11_FINAL_DELTA_EVIDENCE.md
```

## 5. The owner surfaces this package cites — outside this manifest's population

**Deliberately excluded and named, because they live on other branches and their integrity is Git's, not this manifest's:**

| Owner | SHA |
|---|---|
| P06 | `a533fe92d6f6855e0b362179403476520cc9aafa` |
| P08 | `ca577be42e6ba9535e1911dc0bad1dfab74a8aa8` |
| P09 | `ab8c0131c46e8154ad7efae18de2a54af2f17362` |
| P11 | `79e1369156ca052ad77c8f589842f5e99b25f800` |
| P07 | `ee2be30ebf155e241510b3c7133c69419eb060a0` **READ-ONLY** |
| P08 prediction commit | `78f537876852ea6f20047524555fd89e90ee4c78` |

**A commit SHA already is a content digest over its whole tree.** Re-hashing those files here would add nothing and would create a second, divergeable record of the same fact.
