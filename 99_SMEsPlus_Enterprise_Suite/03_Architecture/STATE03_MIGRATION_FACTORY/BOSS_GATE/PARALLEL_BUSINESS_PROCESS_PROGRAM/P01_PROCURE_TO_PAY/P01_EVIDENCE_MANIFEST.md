# P01 — EVIDENCE MANIFEST

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Branch: `research/account-p01-procure-to-pay-2026-09-04-001`

---

## 1. PRE-COMMIT SCAN RESULTS

| Scan | Method | Result |
|---|---|---|
| **Prohibited verdict wording** | Recursive search for bare `PASS` / `FAIL` / `PASS WITH …` across all package files | **2 hits, both benign and retained**: one is the rule statement "no PASS wording" in an expert-brief summary; one is the English phrase "FAIL SILENTLY" in a section heading. No verdict in this package uses PASS/FAIL wording. The PMO recommendation uses the permitted enum value `RECOMMEND HOLD`. |
| **Clean-room vendor tokens** | Recursive search of **Layer 1 files only** for reference-system identifiers and file-extension tokens | **2 leaks found and scrubbed**: a search command quoting a source file extension, and a reference model name used as an illustration in the revision log. Re-scan over a broadened token list returns **zero** Layer 1 hits. |
| **Negative-claim audit** | Deliberately over-inclusive scan for absolute words, then manual review of each material behavioural negative | 176 occurrences of absolute words, the large majority ordinary prose, method statements, or the project rule text itself. **Five material behavioural negatives were qualified** with an explicit class letter and scope. Every `class A` assertion in the package was then listed and checked: **all carry an explicit scope.** |
| **Citation resolution** | Every cited line re-printed from its source file and compared with the claim | **3 mis-cited ranges found and corrected** before commit (`ERR-P01-01`) |
| **Cross-version symmetry** | Every cross-version statement re-checked for a symmetric query on both sides | **1 asymmetric claim found and corrected** (`ERR-P01-03`) |
| **Probe-size guard** | Every structural probe reports the size of what it searched | **6 fabricated class-A absences caught before publication** (`ERR-P01-06`) |

## 2. WHAT THE EVIDENCE BASE RESTS ON

| Class | Obtained | Used for |
|---|---|---|
| Deployed database schema | **Yes** — 3 of 4 dumps restorable | The decisive finding; referential integrity |
| Reference source code | **Yes** — 5 declared roots | `EV-P01-01` … `EV-P01-53` |
| Independent expert reading | **Yes** — 4 disjoint assignments | Admitted only after re-derivation |
| Runtime behaviour | **No** | — |
| Authoritative statutory sources | **No** | — |

## 3. SHA-256 MANIFEST

The manifest excludes itself, since a file cannot contain its own hash.
**24 files.** Regenerate with `find . -name '*.md' ! -name 'P01_EVIDENCE_MANIFEST.md' | sort | xargs -I{} shasum -a 256 {}`.

```
8495d54e70f29543abd07e95553260138d7eed845fb2a72ec81b869186a85894  00_README_P01_PACKAGE_INDEX.md
dd4908cb18540a689f67d52be5a6f28971b7d74f24aad8dacdf01492692e7fc1  LAYER2_EVIDENCE_QUARANTINE/E00_P01_PRIMARY_EVIDENCE_BASE.md
ae95e4a9b322957588bf9efde6cb9913be5aa1a5b190b8497eadd46884e00959  P01_AAS03_EXPERT_CHALLENGE.md
74e52d8a399f129f7730bc555dadc353589421c949b64a58c1932a31b76dab5e  P01_AAS_PLUS_CONSOLIDATION.md
bdde1124d1ed0ccceca5928f4aa4550c5566153c1770a2b4b06b137e96d08b8f  P01_ACCOUNTING_EVENT_REGISTER.md
ca2160584d201201a9cfe732f64917f7dcb901d784cd98711b6b2f8666db8ce8  P01_BUSINESS_EVENT_REGISTER.md
246988d3dbb6e6edb0de4c516d6c17876b420b93f7a27d15680b26a27bff0c66  P01_CONTRADICTION_REGISTER.md
76b31f639e89be83a0c65ffa46b591e541658f572c67326275e831fd9726cbbb  P01_CORE_RECON_HANDOFF_PACK.md
dc68459cea9a5bba84a913f1f4459f6c7d58963d2f7a500b7b28e9c32435e602  P01_CROSS_PROCESS_OWNERSHIP.md
e88a0b3909107aa4917bf9dbfcd6051f0ce5180a493cc461ba482be85064be98  P01_DEPENDENCY_REGISTER.md
5bb0ba2231ab75a403e4a9621bab4fbf5c23d78e86dc6943dd816747abb925ad  P01_DEPLOYED_SCHEMA_EVIDENCE.md
d7bf915843c616eca9ee039b56e216bc455942d1ac4bfc7107d07473ae9ba393  P01_EDGE_CASE_TEST_MATRIX.md
107fc0d340cfdda85c61863546eef161e9d72b4a301dd13818dd2bb02a1414cd  P01_EVENT_TO_GL_MATRIX.md
fa983ef50028871cd60ff3b361184a16b07c54fda915ab71761b7e8e5bde2795  P01_FUNCTION_COVERAGE_REGISTER.md
a20c4bba56583dec29666082f9f7ffc27bd4d2dc66ad9a696ed0dd802a16bdfa  P01_MODEL_FIELD_RELATIONSHIP.md
5317835e606d1d411770a11b421679e13722bcf762b50d93ceb374c73b4226dc  P01_PMO_REVIEW.md
28c190975c885db7568e0544aa94d41a36f33fade96d1c0a325013b5cd3e8e3e  P01_PROCESS_MAP.md
4ff222f4898cacd8b47dc28af7445bc517c77be24c3c16c647a3cce0f5e1ec72  P01_RECEIPT_VALUATION_MATRIX.md
5aa5d37dcbf6a9c46ff414e07c1c713d83fb58256934673a1a7e460652ae487c  P01_RESEARCH_ERROR_AND_REVISION_LOG.md
4a65fa96d855776ca03e078b48e225739d038b6d74ad3e1940e57da0349af5c4  P01_RETURN_REFUND_REVERSAL_MATRIX.md
58387a1dfc3b0a128b976c4bd0c7489e8ca543baa9b18fe38cb41d5075c55009  P01_SCOPE_OWNERSHIP_MATRIX.md
aed70aa1fb79d2d2b87cedb75b85938430602b062529ddae8e8c3b52b6d2acea  P01_SOURCE_LINK_REGISTER.md
19704118bc4a3ca9513ed914a5737f58ebaea034857e5e559d2117eb3de90bc9  P01_SOURCE_TO_AP_TRACE.md
11b5ef99208e31eaf9eee925b8d8ee05cfadc6bd33806c9faeb5d7540e5f83f5  P01_THREE_WAY_MATCH_MATRIX.md
```

## 4. LAYER 2 QUARANTINE

`LAYER2_EVIDENCE_QUARANTINE/E00_P01_PRIMARY_EVIDENCE_BASE.md` is **AUDIT QUARANTINE — Boss /
PMO / AI-Audit only.** It holds every reference-system path, identifier and line number, the
declared path set, all population denominators with their patterns and false-negative modes,
the preserved enumeration scripts, and evidence items `EV-P01-01` … `EV-P01-53`.

It must not be transcribed into any Layer 1 deliverable, any downstream package, or any
implementation artefact.

## 5. WORKING MATERIAL NOT COMMITTED

The four independent expert reports live in `_expert_out/` in the session working directory.
They carry dense reference-system citations and are Layer 2 working material. They are cited by
this package but are not part of the committed Layer 1 deliverable set.
