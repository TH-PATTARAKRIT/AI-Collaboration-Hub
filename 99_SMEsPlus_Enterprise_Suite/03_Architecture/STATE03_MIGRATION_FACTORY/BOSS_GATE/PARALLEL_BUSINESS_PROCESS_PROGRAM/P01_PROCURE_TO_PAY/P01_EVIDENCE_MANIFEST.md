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
9a9c9a7f6788fcb1af5ef9e5fc30b5834a13a9811ef00d54cb1443d8187dddf5  00_README_P01_PACKAGE_INDEX.md
dd4908cb18540a689f67d52be5a6f28971b7d74f24aad8dacdf01492692e7fc1  LAYER2_EVIDENCE_QUARANTINE/E00_P01_PRIMARY_EVIDENCE_BASE.md
ae95e4a9b322957588bf9efde6cb9913be5aa1a5b190b8497eadd46884e00959  P01_AAS03_EXPERT_CHALLENGE.md
db1f6bbd22ba4448349b350a0a87bd347f4d9d3aeb5a95c268a3680de719351e  P01_AAS03_TARGETED_CHALLENGE.md
74e52d8a399f129f7730bc555dadc353589421c949b64a58c1932a31b76dab5e  P01_AAS_PLUS_CONSOLIDATION.md
4856fc0dc97052d7b800a19ff533ecf94adc8cec947a7d4895d6f58a5438bb6a  P01_AAS_PLUS_TARGETED_CONSOLIDATION.md
0f7e9c1c9151fd2bf311af6202b8d7339cae0aca4f4e6cea239b86db68a75dba  P01_ACCOUNTING_EVENT_REGISTER.md
9c654f2f116e901955e52fbfdcc178d76b22f3e3f1dc863143260745a9c79a89  P01_BUSINESS_EVENT_REGISTER.md
e878f1ab7cf6a308b0c0490781c22ad61de99958487e4776154674d92564188a  P01_CONTRADICTION_REGISTER.md
905c40b20bded74ce78b1f526ee0f4a2ff4e2aab12677380f2700d8fc61444e3  P01_CORE_RECON_HANDOFF_PACK.md
615eef2495db54d924e38357c660c8a58b00a9fb87fd4fb374a4ceeb0abd02de  P01_CROSS_PERIOD_EDGE_CASE_MATRIX.md
4ef632c92b6b19abeee423fb3dc303f7aaf83809baedcd88889fb6121445e5da  P01_CROSS_PROCESS_OWNERSHIP.md
b579318903228b63f0511efaf3e73a2a2ce8ef09ff910d39dff4dd2f1a9d3ede  P01_CROSS_PROCESS_OWNERSHIP_REGISTER.md
034a6df199cb9a826d92028289078b4666bf11d84234120f9b25decc70635bad  P01_CURRENT_STATE_RECONCILIATION.md
e88a0b3909107aa4917bf9dbfcd6051f0ce5180a493cc461ba482be85064be98  P01_DEPENDENCY_REGISTER.md
46c36e77913bd5cb27bb7b3c52d60c1ed91bb72eb7467f5f202e1935f43bfacb  P01_DEPLOYED_SCHEMA_EVIDENCE.md
1ba785ee79df28bd03cbdbdba711d7916f568aceb29a5c2d4ef7238dad094c06  P01_DEP_P01_06_EXPERT_CORR1_RECHECK.md
d7bf915843c616eca9ee039b56e216bc455942d1ac4bfc7107d07473ae9ba393  P01_EDGE_CASE_TEST_MATRIX.md
ab97d7bd8a3754b41f84db1491dbe613f70ac12da53cb151a7cff36c5f1f1948  P01_EVENT_TO_GL_MATRIX.md
f542b7d1e0405d995b36083cda5cf1fad4413bdd44a98426acc65013b6fd6e78  P01_FINANCIAL_OWNERSHIP_PROOF_MATRIX.md
fa983ef50028871cd60ff3b361184a16b07c54fda915ab71761b7e8e5bde2795  P01_FUNCTION_COVERAGE_REGISTER.md
a08ea743a4180261b81dc3f444477067d763d979d3ae09d489e6f31d263f60ab  P01_LANDED_COST_ACCOUNTING_TRACE.md
a20c4bba56583dec29666082f9f7ffc27bd4d2dc66ad9a696ed0dd802a16bdfa  P01_MODEL_FIELD_RELATIONSHIP.md
90bc88a452e9b4f2fda7939f4c373be84ec2a6447b9cc1200a051b9e9d7931ff  P01_P05_VENDOR_ADVANCE_RECONCILIATION.md
ce09af035dc0829e9532d38a7354200493a01393a97145c78ccca62d329f3881  P01_P05_WHT_CROSS_PROCESS_CONTRADICTION.md
80ea336aab4ec4085c40b202c036dc849fe9e31c173853f5c7cd8d1a0308f124  P01_PEER_EVIDENCE_RECONCILIATION.md
3fbeb6d0f0f221e98187c5c74855edaf3df5e9b87c1d0dfdd4df287f163bde64  P01_PERIOD_LOCK_CUTOFF_FORENSIC.md
5317835e606d1d411770a11b421679e13722bcf762b50d93ceb374c73b4226dc  P01_PMO_REVIEW.md
323ce5388602bcaf24f08e19af92fdca72fab81f0d572eabd1c505af4315f4dd  P01_PMO_TARGETED_EXIT_REVIEW.md
e634c22c80e66e964c961dc6d1340ed4c880094024fde3396a665eaa3f08de18  P01_PND_MAPPING_CONTRADICTION.md
28c190975c885db7568e0544aa94d41a36f33fade96d1c0a325013b5cd3e8e3e  P01_PROCESS_MAP.md
4ce44adc8fbdd9633fd159459e6c4c118ab1df49eab12823b17e194ad24690bd  P01_PURCHASE_ACCOUNTING_TRUTH_MODEL.md
02ff1e1b0aa6111b3db3e02e89b9f3f5d1b4353a688277ebfa13e2c39543cc99  P01_RECEIPT_LIABILITY_CUTOFF_MODEL.md
73d4749c2bb6920d6ade3424e844ab49f6891ae7d70b84bbe68647744d585ca8  P01_RECEIPT_TO_BILL_BRIDGE_FORENSIC.md
4ff222f4898cacd8b47dc28af7445bc517c77be24c3c16c647a3cce0f5e1ec72  P01_RECEIPT_VALUATION_MATRIX.md
1eeaf16dc9a278d058282a5ddd7655226d22b86627d460f7e0b42844a47ccba8  P01_RESEARCH_ERROR_AND_REVISION_LOG.md
4a65fa96d855776ca03e078b48e225739d038b6d74ad3e1940e57da0349af5c4  P01_RETURN_REFUND_REVERSAL_MATRIX.md
d3ef56fb1683d2b86305ed6c06f2f34aba0c59e37fbb5847dd6eb91c9ab1bb00  P01_SCOPE_OWNERSHIP_MATRIX.md
a893992b825d6963258474c47800a09be07ee036f82a8368f52d602efb467b27  P01_SOURCE_LINK_REGISTER.md
19704118bc4a3ca9513ed914a5737f58ebaea034857e5e559d2117eb3de90bc9  P01_SOURCE_TO_AP_TRACE.md
7c07c2f8e67cd91c054974e50c8b39f6e49a8b18256764518e694870214ead68  P01_SUBCONTRACT_PURCHASE_HANDOFF.md
7fb4ecfbd1cff12b67a7b40a6157296f510aa10047893c1d5a214fe7c9de578e  P01_THAI_WHT_PARTIAL_PAYMENT_ARITHMETIC.md
11b5ef99208e31eaf9eee925b8d8ee05cfadc6bd33806c9faeb5d7540e5f83f5  P01_THREE_WAY_MATCH_MATRIX.md
e5a19b336d3c442313b8cfdb39a01517aef0155a8c998fdba321b7f4078161e0  P01_TRANSITIVE_MODULE_POPULATION.md
d5661e8b88ce80b2d453cd0647fb329b6f5824784195858097a957b169d6c660  P01_UNRESOLVED_EVIDENCE_REGISTER.md
e737e1ceef1ebd7554698ec1f8c75e8637335b603cc63d3193adcd089e103080  P01_VENDOR_BILL_CORRECTION_INTEGRITY.md
381d654519c9639773bbcbfebb1ea6bc6e361acc0c1766d0880b8b0e62a9d922  P01_VERSION_DEPLOYMENT_RECEIPT_BILL_MATRIX.md
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


---

# ADDENDUM — ROUND 3 SCAN RESULTS (2026-09-05)

| Scan | Result |
|---|---|
| Prohibited verdict wording | **1 hit, retained**: the directive's own mandated disclaimer that the terminal state is not PASS/APPROVED/FROZEN/MERGED. No verdict uses PASS/FAIL wording |
| Clean-room vendor tokens in Layer 1 | **9 leaks found across 6 files, all scrubbed.** Re-scan over a broadened token list returns **zero** Layer 1 hits |
| Negative-claim audit | **Three published claims found FALSE** and corrected (`ERR-P01-15`); every class-A claim re-checked for an explicit scope |
| Evidence-base audit | **Two structural defects found by experts**: a database wrongly recorded unreadable, and a database mislabelled by three major versions. Both corrected throughout |
| Citation resolution | Cross-checked; two expert citations corrected by this session |

**Files hashed: 47** (the manifest excludes itself).
