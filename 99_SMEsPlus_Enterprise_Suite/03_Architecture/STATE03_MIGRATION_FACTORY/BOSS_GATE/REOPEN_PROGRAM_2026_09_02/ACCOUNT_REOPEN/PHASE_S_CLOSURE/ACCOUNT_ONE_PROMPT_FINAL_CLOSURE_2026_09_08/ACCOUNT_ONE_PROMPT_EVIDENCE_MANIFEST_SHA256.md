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

### Regeneration 2 — 2026-09-08, after the closing clean-room sweep

**This manifest was regenerated because five of its own listed files changed after the first generation.** The closing sweep moved P11's SHA (`79e1369` → `490ccdd`), which is cited in five deliverables.

> **A manifest that is not regenerated after its population changes is worse than no manifest**: every digest still looks authoritative and five of them are wrong. **The first generation's roll-up is superseded and is not retained**, because a superseded digest has no lineage value — it is not evidence of anything except the moment it was taken.

## 3. Package roll-up digest

SHA-256 over the sorted list of per-file SHA-256 values, so one value fixes the whole surface:

```
a6c8a862362d49419171f3a848400001f6cc85a905d76528058fdfa1e76399d3
```

## 4. Per-file SHA-256 — 13 files

```
bf867e066f5e3b90f08c0832e5d3d1388dc89c8f4975f01fe442a599dfd86129  ACCOUNT_FINAL_BOSS_DECISION_MATRIX.md
41d01f77b717db2bcd6b03e1aee4fc4ce5222464c9e646543a3a7cd416994f18  ACCOUNT_FINAL_CROSS_PACKAGE_DELTA_RECONCILIATION.md
7b139407b5fc7bfe270d88296af664d32a1f882f6ae3ef322ac7cd7c49e2a427  ACCOUNT_FINAL_OWNER_SHA_REGISTER.md
96712a4e429e294836b7c22c895ea104b723ac44f9197b8cae16185e9724cda5  ACCOUNT_FINAL_VETO_RECOMMENDATION.md
7dbaff93f089d8e080d26f03e2380b5a409d260e77bdaadc5beb1d6f2cf602b5  ACCOUNT_ONE_PROMPT_AUTO_RESUME_STATE.md
4e082e5a8f84d88de1cd4eda41256b03834fbb18d24a9b30efa7cc0615bc8e3c  ACCOUNT_ONE_PROMPT_EXECUTION_REGISTER.md
f160a9d818a9a4aacfe4325fc8cf4b860a9b4b0c7c723a7fc443a7d9ce034080  ACCOUNT_PHASE_SA_INPUT_OUTPUT_READINESS_PACK.md
34419fc9bb4b89fff35dc61192938ecd2643468e2917d6a4d7cbe4ef259d2304  BOSS_RULING_NO_QUALITY_SCOPE_EVIDENCE_DEGRADATION_2026_09_08.md
99e5f1fe992cd97efeae78e5f4733665b20405da228395e4cb07a79bdc406915  CLAUDE_DESKTOP_ONE_PROMPT_ACCOUNT_FINAL_CLOSURE_TO_PHASE_SA_2026_09_08.md
70917beb8cc654723841f405826732e49b26cce07081a091c0012d0104d2c7fc  P06_FINAL_DELTA_EVIDENCE.md
d5c0e497bffd2e931dac5ad0ba8d2dc7b5cb28e1c1b2bd969bf81331891c6485  P08_FINAL_DELTA_EVIDENCE.md
1bfb03f316af3128aa6d261409808a72944a9c0baffa3d0db345f08e06a09530  P09_FINAL_DELTA_EVIDENCE.md
b116db768855acbbd43528d610353d0757e9e1201aede426f681ffbdc994bb19  P11_FINAL_DELTA_EVIDENCE.md
```

## 5. The owner surfaces this package cites — outside this manifest's population

**Deliberately excluded and named, because they live on other branches and their integrity is Git's, not this manifest's:**

| Owner | SHA |
|---|---|
| P06 | `a533fe92d6f6855e0b362179403476520cc9aafa` |
| P08 | `ca577be42e6ba9535e1911dc0bad1dfab74a8aa8` |
| P09 | `ab8c0131c46e8154ad7efae18de2a54af2f17362` |
| P11 | `490ccdd81a4fed79d36b7b9d3bbc25deedd597b4` |
| P07 | `ee2be30ebf155e241510b3c7133c69419eb060a0` **READ-ONLY** |
| P08 prediction commit | `78f537876852ea6f20047524555fd89e90ee4c78` |

**A commit SHA already is a content digest over its whole tree.** Re-hashing those files here would add nothing and would create a second, divergeable record of the same fact.
