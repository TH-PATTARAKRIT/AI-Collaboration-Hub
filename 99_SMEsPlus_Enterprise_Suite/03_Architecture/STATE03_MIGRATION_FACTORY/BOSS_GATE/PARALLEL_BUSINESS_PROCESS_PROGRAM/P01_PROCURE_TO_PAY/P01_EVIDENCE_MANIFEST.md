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
ad6adc14f9080ca7460b34ab48db8d9f480906bb3abef5d0c0d875c10025b7b0  00_README_P01_PACKAGE_INDEX.md
dd4908cb18540a689f67d52be5a6f28971b7d74f24aad8dacdf01492692e7fc1  LAYER2_EVIDENCE_QUARANTINE/E00_P01_PRIMARY_EVIDENCE_BASE.md
ae95e4a9b322957588bf9efde6cb9913be5aa1a5b190b8497eadd46884e00959  P01_AAS03_EXPERT_CHALLENGE.md
405a656912a5d65a090feb8ffb503a00351082a7e8fd1e5fd0e945030037ebb8  P01_AAS03_SUPPLEMENTAL_CHALLENGE.md
db1f6bbd22ba4448349b350a0a87bd347f4d9d3aeb5a95c268a3680de719351e  P01_AAS03_TARGETED_CHALLENGE.md
74e52d8a399f129f7730bc555dadc353589421c949b64a58c1932a31b76dab5e  P01_AAS_PLUS_CONSOLIDATION.md
089e4722e66a4558ecef51c07aaa229f315cd5870ada546ee8f265599e759062  P01_AAS_PLUS_SUPPLEMENTAL_CONSOLIDATION.md
39318d1aa6895e26ef0f3f46f6925222d9065092124d8a0edf2f913ab19b74e6  P01_AAS_PLUS_TARGETED_CONSOLIDATION.md
0f7e9c1c9151fd2bf311af6202b8d7339cae0aca4f4e6cea239b86db68a75dba  P01_ACCOUNTING_EVENT_REGISTER.md
1946b58bdefc5baf7c518a46fd36281ceaa5ad422b91127c33b92c0d30af8495  P01_ACCOUNTING_LINEAGE_SEMANTIC_INTEGRITY.md
dbf27456e3833ebfc37b215692675a79f7f42a745b08a7fa5ae61ed783092a9e  P01_AUTO_RESUME_STATE.md
9c654f2f116e901955e52fbfdcc178d76b22f3e3f1dc863143260745a9c79a89  P01_BUSINESS_EVENT_REGISTER.md
07896239007ee497926efab6a2c42e2333c66062ab9aabd05b8986e13fb8a163  P01_CHECKPOINT_REGISTER.md
608765ea6b1695d44b57f28609db1fba150a3ac47ec59cd0b01e70f7bb63b4d4  P01_CONTRADICTION_REGISTER.md
a4be7a742a1b8f9252ad39427b6196daef70b93d59b0678fe6c1bef3ab2ac80f  P01_CONTRADICTION_REGISTER_V2.md
46a5c759f4e374e33bdb75e38ec91ce1d6819e08c1711564dd26c0779fb6d27c  P01_CORE_RECON_HANDOFF_PACK.md
615eef2495db54d924e38357c660c8a58b00a9fb87fd4fb374a4ceeb0abd02de  P01_CROSS_PERIOD_EDGE_CASE_MATRIX.md
4ef632c92b6b19abeee423fb3dc303f7aaf83809baedcd88889fb6121445e5da  P01_CROSS_PROCESS_OWNERSHIP.md
ba2cc4243b1673f919334130b4d8d19d94cb232037b2120e7b2a16c61fc64973  P01_CROSS_PROCESS_OWNERSHIP_REGISTER.md
943ffcb362c7dcc64743b5d8f038f8c82f8d5ef4bad18ad6bf8771f510790251  P01_CURRENT_STATE_EVIDENCE_VERSION_REPAIR.md
05baf982ea0f27d61166b92217847bd2e3d92e71958fee424cc136e63ab6eb72  P01_CURRENT_STATE_RECONCILIATION.md
c8f2055038ea302a21930a5b0dcb006948e011b78d4176b25dc337c9ca4e5477  P01_DATABASE_FALSIFICATION_REGISTER.md
7251e8793a8d6141ce9d82a044ecdc0fcfce25b59c2d9ef68bc03e533ec28557  P01_DATABASE_IDENTITY_REPAIR.md
e88a0b3909107aa4917bf9dbfcd6051f0ce5180a493cc461ba482be85064be98  P01_DEPENDENCY_REGISTER.md
46c36e77913bd5cb27bb7b3c52d60c1ed91bb72eb7467f5f202e1935f43bfacb  P01_DEPLOYED_SCHEMA_EVIDENCE.md
1ba785ee79df28bd03cbdbdba711d7916f568aceb29a5c2d4ef7238dad094c06  P01_DEP_P01_06_EXPERT_CORR1_RECHECK.md
ff3b8b93362dd482dd886019b033c55c556ca1f9a38cdbdade66406d9bb2532f  P01_DEP_P01_06_RESIDUAL_CLOSURE.md
1c25c926fd5a47f969c341e59e7706dd69c229ec71d21c9830f15eb72c2f23f8  P01_EC06_DETERIORATION_FORENSIC.md
d7bf915843c616eca9ee039b56e216bc455942d1ac4bfc7107d07473ae9ba393  P01_EDGE_CASE_TEST_MATRIX.md
886744671128aa89f6f4a342fbd44069dbda1f5740b5e337ea4b4f67650bbb01  P01_EVENT_TO_GL_MATRIX.md
64d883bfdf966dd2436e8166b60fed37c0a84f6a132cddb664940a3c3171d2ac  P01_EXIT_CRITERIA_V2.md
a6b0cf264ef39c57eecf1efe4bdfd96419f8e7e2437f277d6b9d5362ac3ca3e1  P01_FINANCIAL_COMPANY_OWNERSHIP_V2.md
f542b7d1e0405d995b36083cda5cf1fad4413bdd44a98426acc65013b6fd6e78  P01_FINANCIAL_OWNERSHIP_PROOF_MATRIX.md
fa983ef50028871cd60ff3b361184a16b07c54fda915ab71761b7e8e5bde2795  P01_FUNCTION_COVERAGE_REGISTER.md
7888b4c093d9ade4679b81bdfe9f27f1331b2364508e983f74133dd88c7fd5c3  P01_LANDED_COST_44_COMPANY_REALITY.md
a08ea743a4180261b81dc3f444477067d763d979d3ae09d489e6f31d263f60ab  P01_LANDED_COST_ACCOUNTING_TRACE.md
a20c4bba56583dec29666082f9f7ffc27bd4d2dc66ad9a696ed0dd802a16bdfa  P01_MODEL_FIELD_RELATIONSHIP.md
4c14e5d1310d636f7c50fd7bcd5e9ef3db18a58baf462f2f26372b94fe817b29  P01_P03_CORRECTION_HANDOFF.md
f21281606d4d37e3fd4fd128b4303effca7487a82c4ddd0957401967205d05b9  P01_P04_CENSUS_RESPONSE.md
90bc88a452e9b4f2fda7939f4c373be84ec2a6447b9cc1200a051b9e9d7931ff  P01_P05_VENDOR_ADVANCE_RECONCILIATION.md
ce09af035dc0829e9532d38a7354200493a01393a97145c78ccca62d329f3881  P01_P05_WHT_CROSS_PROCESS_CONTRADICTION.md
7818dc308c7075319c88d34ab580cad8deb6a67c76b8135acce18d2947c3e002  P01_P05_WHT_RECONCILIATION_V2.md
b3ffe2540b786c56d37553808559578e2056700d9ce996ffabef9c636d513e35  P01_P06_SUPERSESSION_RECONCILIATION.md
dad95ee824a73bffb46d057b4b4a484a051fbe283842d5cc6c39c76514c5b111  P01_P11_EVIDENCE_VERSION_DEPLOYMENT_SUPPLEMENT.md
80ea336aab4ec4085c40b202c036dc849fe9e31c173853f5c7cd8d1a0308f124  P01_PEER_EVIDENCE_RECONCILIATION.md
3fbeb6d0f0f221e98187c5c74855edaf3df5e9b87c1d0dfdd4df287f163bde64  P01_PERIOD_LOCK_CUTOFF_FORENSIC.md
53e6d8029ea5963ea9d995d1d152d0dd1134847e9f6873f1e12f606a9d52162b  P01_PERIOD_LOCK_PATH_MATRIX_V2.md
5317835e606d1d411770a11b421679e13722bcf762b50d93ceb374c73b4226dc  P01_PMO_REVIEW.md
4ff43ab6b49bd1fbca5a056a83c0584f3c0da0dcaa030d1dd2e807a051ae832d  P01_PMO_SUPPLEMENTAL_REVIEW.md
323ce5388602bcaf24f08e19af92fdca72fab81f0d572eabd1c505af4315f4dd  P01_PMO_TARGETED_EXIT_REVIEW.md
e634c22c80e66e964c961dc6d1340ed4c880094024fde3396a665eaa3f08de18  P01_PND_MAPPING_CONTRADICTION.md
864c9b9e5c96c8292668cc729863e3fe8399dffd62d75ef71d97191194919e6a  P01_PND_MAPPING_DEPLOYMENT_OWNER.md
db34d2af6b9c1665f432b121ec5c71054a706b9ef559bead8b5716caf34ac137  P01_POSTED_BILL_CORRECTION_V2.md
28c190975c885db7568e0544aa94d41a36f33fade96d1c0a325013b5cd3e8e3e  P01_PROCESS_MAP.md
4ce44adc8fbdd9633fd159459e6c4c118ab1df49eab12823b17e194ad24690bd  P01_PURCHASE_ACCOUNTING_TRUTH_MODEL.md
bd6c3db5145e6c5a08a06c249880ae8c15eb6c75ea6dcacf812ac881c8b84a67  P01_RECEIPT_LIABILITY_CUTOFF_MODEL.md
2483a9ec4762d1c27ac23c267d361870ffc29cf4c62dc677ea7ea87897a73a6f  P01_RECEIPT_TO_BILL_BRIDGE_FORENSIC.md
4ff222f4898cacd8b47dc28af7445bc517c77be24c3c16c647a3cce0f5e1ec72  P01_RECEIPT_VALUATION_MATRIX.md
db3df9bbb77e980e4c489fffe9596867a003fdef88870bdf5a18e1c000b5f492  P01_RESEARCH_ERROR_AND_REVISION_LOG.md
4a65fa96d855776ca03e078b48e225739d038b6d74ad3e1940e57da0349af5c4  P01_RETURN_REFUND_REVERSAL_MATRIX.md
d3ef56fb1683d2b86305ed6c06f2f34aba0c59e37fbb5847dd6eb91c9ab1bb00  P01_SCOPE_OWNERSHIP_MATRIX.md
fcf1579e892db5ee13c26075e914493110d8cc4f6118156c9f4e270089b9c1c9  P01_SERIES18_DEPLOYMENT_DISCOVERY.md
f0358e3b757271c6c6193f8ac28521c31c71f606afa74e4def66cacc5eaae872  P01_SOURCE_LINK_REGISTER.md
19704118bc4a3ca9513ed914a5737f58ebaea034857e5e559d2117eb3de90bc9  P01_SOURCE_TO_AP_TRACE.md
989033a05d5cfd9e7c77bf5190173b27743cd445310e0f3d96b26b99e618f7a2  P01_SUBCONTRACT_DEPLOYMENT_REALITY.md
7c07c2f8e67cd91c054974e50c8b39f6e49a8b18256764518e694870214ead68  P01_SUBCONTRACT_PURCHASE_HANDOFF.md
7fb4ecfbd1cff12b67a7b40a6157296f510aa10047893c1d5a214fe7c9de578e  P01_THAI_WHT_PARTIAL_PAYMENT_ARITHMETIC.md
11b5ef99208e31eaf9eee925b8d8ee05cfadc6bd33806c9faeb5d7540e5f83f5  P01_THREE_WAY_MATCH_MATRIX.md
f21ea252122b938c5aa2671e5e49f5d3b9798926ce8a43d7dcdf56b428270c40  P01_TRANSIENT_PERMISSION_BLOCKER_REGISTER.md
704d4842f8215361fd058e877fb8c3426c37d1d90473abeee7176c66b7a9ff3e  P01_TRANSITIVE_MODULE_POPULATION.md
d5661e8b88ce80b2d453cd0647fb329b6f5824784195858097a957b169d6c660  P01_UNRESOLVED_EVIDENCE_REGISTER.md
abc6af1e76b361c82728ada65bc763e807980b0d319c86365cf4c0564f590b21  P01_VENDOR_ADVANCE_OWNERSHIP_CLOSURE.md
e737e1ceef1ebd7554698ec1f8c75e8637335b603cc63d3193adcd089e103080  P01_VENDOR_BILL_CORRECTION_INTEGRITY.md
4c8315698eddeca79f9bcee3977c098a086d549fb1dcb1bed75a1f862f9755bf  P01_VERSION_DEPLOYMENT_RECEIPT_BILL_MATRIX.md
d0659c3c153f8dcb2b5686f153be052a20c076b6d1d75e140cc40a1baf542729  P01_VERSION_IDENTITY_MATRIX.md
0269c8f85e03b598d42e16342bcaf6eeba80e9c1ca57086c0d9d48082818a39d  P01_VERSION_SENSITIVE_FINDING_REGISTER.md
ce1db4d577d0d9cf3930017c48a7303cdf46f5895659246b2e38f1d23a132d5b  P01_WHT_MECHANISM_REACHABILITY.md
48cca08ea1b0cb65460e238b0bb2e4899e3e9c9580562d617df31d7f5121e1c9  P01_WHT_PARTIAL_PAYMENT_V2.md
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

---

## ADDENDUM 2 — REGISTER-TEXT PROPAGATION AUDIT

A standing programme lesson holds that **a revision log is not a correction**: accepted findings
have previously been logged and never edited into the registers themselves.

That audit was run over this package as a separate, named step. It found **eight residual stale
claims** — four in the module-population change table, two disposition rows still marked *under
challenge* after their challenges had landed, and two that were legitimate before/after quotes.

All six genuine residuals were corrected. Final state: **zero** stale "installed nowhere"
claims and **zero** unresolved challenge markers outside the revision log.

**Every correction in the revision log is now reflected in the register text.**


---

## ADDENDUM 3 — ROUND 4 SCAN RESULTS (2026-09-05)

| Scan | Result |
|---|---|
| Prohibited verdict wording | **clean** |
| Clean-room vendor tokens in Layer 1 | leaks found and scrubbed, including tool names; **re-scan over a broadened token list returns zero** |
| **Register-text propagation audit** | Run as a named step. **Six genuinely stale assertions found** that the correction banners had not fixed — table rows and summary sentences still asserting the superseded cause. All six corrected in the text. Re-audit returns **zero** |
| Negative-claim audit | The round's own absence proof was **re-run with a wider pattern** and corrected from 12 to 13 (`ERR-P01-20`); the conclusion held |
| Evidence-base audit | **Nine defects found**, eight by independent challenge |

**Files hashed: 76** (the manifest excludes itself).


---

## ADDENDUM 4 — PEER-PROMPTED CENSUS RE-KEY (`ERR-P01-22`)

Peer **P04** reported two defects in its **own** database census and suggested P01 test for them.
Both were present here, and both were verified independently before acceptance:

| Defect | Effect on P01 |
|---|---|
| Artefact enumeration matched one file extension | **Zip-container backups were invisible.** Ten artefacts exist, not four |
| Identity keyed on file name and a data resemblance | **Five distinct database identities**, not three deployments. Two artefacts named alike are different databases; two named differently are one |

**Survives:** the two 44-company archives are not independent witnesses — now better supported,
since identical company sets with different database identifiers indicate a **clone lineage**.
**Withdrawn:** the deployment count and the 46-company arithmetic.
**Also corrected:** P01's evidence range begins **2026-03-30**, four months earlier than stated.

**Files hashed: 76.**


---

## ADDENDUM 5 — LATE DISPROOF: THE ROUND'S GOVERNING FINDING WAS FALSE (`ERR-P01-23`)

The challenge layer assigned to disprove the version identification returned **after** this
package was first published, with verdict **BROKEN**.

**A series-18 deployment exists on this host** — 4 companies, 15,522 journal entries, 47,801
valuation layers, and the **goods-received clearing account configured**. P01 had enumerated one
download directory; the pattern run across the home directory returns **19 archives and at least
nine distinct database names**.

**Consequences:** `EC-01` falls back to **NOT SATISFIED**; **7 of 8 not satisfied — no
improvement over the prior round**; the PMO claim that the round improved in substance is
**withdrawn**. **No accounting finding is withdrawn.**

**Files hashed: 78.**
