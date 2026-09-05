# 14 — P05 EVIDENCE MANIFEST

`LAYER 2 — AUDIT QUARANTINE`

## 1. Commit Lineage

| Item | Value |
|---|---|
| Repository | `https://github.com/TH-PATTARAKRIT/AI-Collaboration-Hub.git` |
| Canonical branch | `SMEsPlus` — **not modified by this session** |
| Working branch | `research/account-p05-expense-to-pay-2026-09-04-001` |
| Base commit | `88f52cd7ba6dc40b8951c4bfc4e0016af7cbb7ad` |
| Commit 1 | `64b10cd` — traces, registers, scope-aware correction (interim, before the challenges returned) |
| Commit 2 | `1172f79` — challenge consolidation, corrections, final registers |
| Commit 3 | `40166d0`, `9b1006b` — commit lineage, peer-table correction |
| **Evidence-base repair** | `120e1bd` exhaustive search + v18 DB · `8b4edbc` Challenge D corrections · final commit in `19 §10` |
| **Targeted closure** | `f0037b8` U-01/U-02 evidence · `61e158a` two published findings corrected · `068c71c` TX-01 measured · `d8d8f6f` all four experts' corrections · final commit in `19 §10` |
| Merge status | **Never merged.** Boss decides. |

## 2. Evidence Classes Used

| Class | Meaning | Count in package |
|---|---|---|
| `FACT VERIFIED` | Re-derived from source; citation re-openable | majority |
| `SUPPORTED INTERPRETATION` | Follows from source but not executed; closure needs runtime (`20 U-02`) | ~12 |
| `DESIGN CANDIDATE` | A proposed SMEsPlus position, not a reference fact | `17 §6` |
| `BOSS CONTROLLED DECISION` | Framed, deliberately unanswered | `BD-01`..`BD-08` |
| `CONTRADICTED` | Disproved, retained with its disproof | 6 negatives + 12 finding corrections |
| `UNRESOLVED` | Registered with a disposition | `20`, 11 entries |

## 3. Reproducible Verification — `C-01`

The package's most-cited single fact is that a declared immutability guard does not contain the fields
it names. It is reproducible in isolation, without reading the surrounding module:

```bash
cd "/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/hr_expense"
python3 - <<'PY'
import ast
t = ast.parse(open('models/account_payment.py').read())
for node in ast.walk(t):
    if isinstance(node, ast.Assign) and getattr(node.targets[0], 'id', None) == 'trigger_fields':
        vals = sorted(ast.literal_eval(node.value))
        print("members:", len(vals))
        print("'journal_id'    in set:", 'journal_id' in vals)
        print("'ref'           in set:", 'ref' in vals)
        print("'journal_idref' in set:", 'journal_idref' in vals)
PY
```

Expected output:
```
members: 12
'journal_id'    in set: False
'ref'           in set: False
'journal_idref' in set: True
```

Independently re-run by AAS-03 Expert 1 with the same result (`16 §4.1`).

## 4. Enumeration Commands

Every population claim in this package states its command, path set, pattern and unit.
The consolidated set is at `21 §1-§2`; the module denominator is at `01 §1.1`.
Two enumerations were **re-run independently by a reviewer with different patterns** (Expert 2,
`16 §4.2`), which is how the residual boundary defect `21 NC-E-05` was found.

## 5. Package Integrity — SHA-256

Computed over the files as committed. Regenerate with:

```bash
shasum -a 256 *.md
```

| File | Bytes | SHA-256 |
|---|---:|---|
| `00_README_PACKAGE_INDEX.md` | 7985 | `9fb9aa5f974c527f2415b8192564f20ccac2f659266aad5e893dbccf8eb17537` |
| `01_P05_PROCESS_MAP.md` | 18649 | `cf9482306f9228c3f06a704a2b0df019b7b25359dc1da93222310e0cfaff4914` |
| `02_P05_EXPENSE_CLASSIFICATION_MATRIX.md` | 13228 | `da49426ffd061a6a543a8d87bce0114a37edf08f2250f9c2b10aa7d2f7b4ea52` |
| `03_P05_EXPENSE_RECOGNITION_MATRIX.md` | 9402 | `7e552026f3160bebad07c83b8dba6014c415bd1ed561aa3f8036b9249b2b335e` |
| `04_P05_EMPLOYEE_VENDOR_PAYABLE_MATRIX.md` | 9444 | `72591664dbad2310de50f00a1746bac8703f4ad90ab011acebdc379bd63820af` |
| `05_P05_EVENT_TO_GL_MATRIX.md` | 15468 | `da675b96a690b7be456a7dbfe5561832c4ff4b320ff7f2f9102a8faa97462cbb` |
| `06_P05_ANALYTIC_HANDOFF.md` | 4227 | `9cf95f4b4ae4afca14015ff7512285f59b6aa21c761b49be7df19a883d25a5f6` |
| `07_P05_TAX_WHT_MATRIX.md` | 25470 | `efdf6ca90a9d64e582e5ddaef69898219d158c514f578e78b6c3b9b2be1c80dc` |
| `08_P05_SETTLEMENT_RECONCILIATION.md` | 9400 | `44f6d4e7b27414ab67f7d5cdcc41f3a7f373fee830da35b6c4bf2a4c78f62592` |
| `09_P05_CROSS_PROCESS_OWNERSHIP.md` | 6531 | `16a7b3c4a34eadf634464471e1f954dbf3c1df94660e401036faad6d420a2d12` |
| `10_P05_EDGE_CASE_MATRIX.md` | 30014 | `f594572bd91b506046e8d72424e22f9deb3374c899eb90c9bc31e08afc1363b8` |
| `11_P05_CONTRADICTION_REGISTER.md` | 13703 | `51936ff89a63cff93b8828be30370b4f89dc52461811fa0de7847863fe2a405e` |
| `12_P05_DEPENDENCY_REGISTER.md` | 6292 | `d94c95a1ca1f04500040dc856082c117aa4005a8bbfb169efa47c3506fd7768b` |
| `13_P05_SOURCE_LINK_REGISTER.md` | 7961 | `1156148d7dedeb8e6daab5b09fff7bc1f57193737f0118f170be8aa2e5ed1b98` |
| `15_P05_REVISION_LOG.md` | 7583 | `e485167a512d14f9c2e6e185b1b8753d25aa4c278334d87a37d80bf9dfc9666d` |
| `16_P05_AAS03_CHALLENGE.md` | 16487 | `bca451badc1b2fec452bb754b39fa2f8e13ed20399986be10eae202425e99cf9` |
| `17_P05_AAS_PLUS.md` | 12876 | `1ccc4f26798646ea3116bcf3468f46d5fc4bc7f366cb686688137b87d2f49bf4` |
| `18_P05_PMO.md` | 10443 | `b6ef5d02eaa9a6459ab83403790b5fbe32200ee9ad8c1dda5898afe633714569` |
| `19_P05_CORE_RECON_HANDOFF_PACK.md` | 10723 | `326dc26213fd2ed8ebfd2996ffa9d83af86189dd707e05eb10a8c0af2bac5e04` |
| `20_P05_UNRESOLVED_REGISTER.md` | 4662 | `737e0706225a2e484440c93c1f46b6154aaddb85a4f173a5102c845765853138` |
| `21_P05_NEGATIVE_CLAIM_REGISTER.md` | 13694 | `c995ff8e46ea3c83b85e0a9375d3b2532aecbc7367de66b2a067806a759196d3` |
| `22_P05_SCOPE_OWNERSHIP_MATRIX.md` | 16389 | `bedffefd862c278cf7282d7e88ecf8168fa8c1dfe135eac9db2bde12daf37ab6` |
| `23_P05_CURRENT_STATE_RECONCILIATION.md` | 4597 | `4228075b246a7e74fb15cae9e66f7ff85c8a1498a712a90fd6165c9de48afc33` |
| `24_P05_DEPLOYED_MODULE_EVIDENCE_U01.md` | 11016 | `d91bfca12f097d8ee89adc885590383cf63e48362d8c19924a0f7c78e6c62d4a` |
| `25_P05_RUNTIME_TRACE_U02.md` | 15912 | `287cbf77b630513000ac2e4443216ad4916e9115c5d7086932804b1381d832af` |
| `26_P05_TOLERANCE_ZERO_BOUNDARY_REGISTER.md` | 11025 | `280920e23c9251bc8ebe33d619e18d1960c1825353da250b678e0335143491ac` |
| `27_P05_EXIT_CRITERIA_REGISTER.md` | 8054 | `07eff04c827a912e8ac955a1819f60fad55457b5374bc4d031e15032046ebbe0` |
| `28_P05_HANDOFF_COMPLETENESS_REGISTER.md` | 5814 | `597f8b7b0195abcdd76f4f5b7307ea6b68881a261fb31587c0b46ff483b21a0c` |
| `29_P05_EC07_EVIDENCE.md` | 4782 | `99738f3ab8845290f248bdb93b98e2f1aa08e007e5b890852916361d4dd175b1` |
| `30_P05_PEER_HANDOFF_MATRIX.md` | 14875 | `77e626e6da8748d33ee9f52d2ac47fda8f95f4644f2be628d53d7d311fd3eed2` |
| `31_P05_SCOPE_REVALIDATION_CORR1.md` | 6963 | `0a077f22bb5a2d1d5d90c357e5e184e7bfc12adc9df24a0f67cef04f470b5d33` |
| `32_P05_BUSINESS_EVENT_REGISTER.md` | 4789 | `34289b973bb33e4bd8bd4df7f1e3e34883bb5ede5c1d3e91d3b7f7398bbc763a` |
| `33_P05_ACCOUNTING_EVENT_REGISTER.md` | 5049 | `be30110671040c05b9107d9c2815cb79f92a4d9a2c83e27990a3bbc1807b3e6f` |
| `34_P05_CROSS_PROCESS_OWNERSHIP_REGISTER.md` | 6837 | `97fef81258df8446f8205cc1ba769a8cdfe81aaa3d9ba4e6666cbcb9397fa7ab` |
| `35_P05_UNRESOLVED_EVIDENCE_REGISTER.md` | 6417 | `cd6c78565e524870626c10b687cca072b7ba98920a03681a8981e8c22ca78ebe` |
| `36_P05_AAS03_TARGETED_CLOSURE_CHALLENGE.md` | 17228 | `40b310848c974ea33560d872872498ad898a30f087ef0b0e71422534767b4cd2` |
| `37_P05_AAS_PLUS_TARGETED_CONSOLIDATION.md` | 8393 | `5359b2dbf38e3153b8d75c71918dfa4835496654a8d112fb1bde1329c65c5182` |
| `38_P05_PMO_EXIT_REVIEW.md` | 8909 | `fcf593be495f1c7ff88eaac688460f80816fa901ac18f6eac8f60353dfc30aef` |
| `39_P05_RESEARCH_ERROR_AND_REVISION_LOG.md` | 18586 | `768ee83a5cfb2365ce908b502ee6ae9664d937b30848d28d070df6a269c400bd` |
| `40_P05_CHECKPOINT_REGISTER.md` | 5438 | `7eb6e5808f4f7e0e7f209fb2a8a6566c5f61d2bdcba03131273c083cf3e94c2c` |
| `41_P05_EVIDENCE_BASE_RECONSTRUCTION.md` | 6849 | `f250be37b9468faa1ef4e4b5b5bfe8f84a372b0d49a4c030e66ab65ee9804337` |
| `42_P05_MULTI_DATABASE_POPULATION_PROOF.md` | 2807 | `ede3adb7bb4c7f6c012da21b3b372a125043d799163a1515814c1870afe16dea` |
| `43_P05_DEPLOYED_MODULE_REGISTRY_MATRIX.md` | 5822 | `f84c1d71a3e134c61ce3701879c4c3f31bdfd3163bb0e2f194ba445c0467deab` |
| `44_P05_LIVE_LATENT_FINDING_REGISTER.md` | 6343 | `a5a315f34caaa10131d7f7c86f6348cd93f17e9c4d8668d3d6f0cadfbfe4bb83` |
| `45_P05_PETTY_CASH_DEPLOYMENT_RECLASSIFICATION.md` | 8797 | `f399d22c0d9083fdf5c4c2ada5a75229cc621bb441864eda8812f4a09f7ebbd9` |
| `46_P05_EMPLOYEE_ADVANCE_DEPLOYMENT_RECLASSIFICATION.md` | 3130 | `b8c8ec0b1599d240cd3697858d6991074b66337728eba3fdd58c6e17f33a4d45` |
| `47_P05_PURCHASE_ADVANCE_DEPLOYMENT_FORENSIC.md` | 4016 | `ce4e85e1a2ec53217f483f0874bf9fcd0f69555eeae66a71bc0e3fed9993dba6` |
| `48_P05_VENDOR_BILL_SUDO_AUTHORIZATION_FORENSIC.md` | 2654 | `8c479816e61d7b87a21c8bbbcc855f12b797ea5c225bd966af122dd22c4dfd22` |
| `49_P05_P01_VENDOR_ADVANCE_HANDOFF.md` | 4106 | `4a468626f2f20843092aaa2e60ccc0928ec8982ea8ddb5e70bd65e30739b25fa` |
| `50_P05_TX01_SCREEN_CSV_DIVERGENCE.md` | 5216 | `fd012f8d7d0a73aac2f8477447dbcdf246cea797c6e59fa62a90b40fa6c4ff25` |
| `51_P05_P07_TX01_STATUTORY_HANDOFF.md` | 2568 | `a3b1174f0301c859885dadf96ab724e3dd86668f52ac543814d87a6edfd23269` |
| `52_P05_CERTIFICATE_FINDING_REVISION.md` | 3458 | `c72b21b354cac7e76237f9f37ce88a61c596b038ae506ec7db3cae98988373e7` |
| `53_P05_R01_CORR1_REINSTATEMENT_FORENSIC.md` | 3585 | `cd1ab84b5df8d9ad797d2647ad1bceac8ba8865bc3bf9cb98b72a9f605ef7a5a` |
| `54_P05_RESEARCH_ERROR_RE07_RE23_RECONCILIATION.md` | 8617 | `78f92e032a909512c1b166d510ac6ab2815a833abbb597477a6f6c7fd7eeb0f2` |
| `55_P05_RESEARCH_METHOD_FAILURE_ANALYSIS.md` | 5548 | `4d081745b7b4bc31b99253c940f9c673347829ad43502e4d59e97599fb8ee2c1` |
| `56_P05_EXIT_CRITERIA_V2.md` | 3319 | `a69b7c36e30f143de8b933aaae56e1d3edab613c672436fb81c4e440234e1344` |
| `57_P05_HANDOFF_COMPLETENESS_V2.md` | 3310 | `27d39c630360f42adee2af576e19cbf8285dfac40c8c8819da52106b34cce4d0` |
| `58_P05_TOLERANCE_ZERO_V2.md` | 3925 | `17cb8d851ef45be8d48281e6bff4aa15eb419659d8bd7f74d48b7f620abbe54d` |
| `59_P05_EC07_CLEAN_PASS_REGISTER.md` | 2675 | `f8594d34deab254689a1256cf3b908ab43f2cf9ca6c5fe8826fb687e42e915fa` |
| `60_P05_DUMP_READONLY_EVIDENCE_BOUNDARY.md` | 2519 | `7add08cd9c35df1de7f3efadddcfa22a8af95efa0dd7ce213918925052dbc220` |
| `61_P05_PEER_RECONCILIATION_REFRESH.md` | 2565 | `d0a098e57348904e44d679fe205bd8ef5e092154d77ee6a1e477cc7b6130a6b0` |
| `62_P05_AAS03_EVIDENCE_BASE_CHALLENGE.md` | 8461 | `6b3033565b6eb1dfc7261309435a51fc13917f9f8a1828792edf00c14ac5d9ee` |
| `63_P05_AAS_PLUS_SUPPLEMENTAL_VETO_RECHECK.md` | 3725 | `1340dc69b3d9878e205a80592fa2bc0ba27d36ecc1d620c86390bed313293b78` |
| `64_P05_PMO_SUPPLEMENTAL_REVIEW.md` | 6574 | `46b25a37c9c541f8ca9a16bf5ad5d908edf22ef938e26361799b58b41276b782` |
| `65_P05_P11_EVIDENCE_BASE_AND_LIVE_RISK_SUPPLEMENT.md` | 5386 | `d24c7b80eb000958d2ddbaec97cc84ba3da8857506b75bf229525497a7c3c927` |
| `66_P05_AUTO_RESUME_STATE.md` | 3815 | `ab211d657249140859c2ed920790ce8a91c9aab026f2e37a91d4007736ec2616` |

> **`14_P05_EVIDENCE_MANIFEST.md` is deliberately excluded from its own table** — a file cannot
> contain its own hash. All 66 other files are listed. Verify them with `shasum -a 256 *.md`, and
> verify this file against the commit SHA in §1.

## 6. Layer Boundary Attestation

| Section | Layer | Scan result |
|---|---|---|
| `17 §6`, `19 §1-§6` | **1 — clean room** | 0 vendor-token occurrences, word-bounded patterns (`18 §6`) |
| All other files and sections | **2 — audit quarantine** | contain reference-ERP `file:line` citations by design; **must not** be transcribed into any Team B reference package |

## 7. Evidence Not Held

| Missing evidence | Consequence | Registered as |
|---|---|---|
| Deployed module list | Every custom-module finding is conditional | `20 U-01` (gating) |
| P05 runtime / database trace | Every `SUPPORTED INTERPRETATION` stays unclosable | `20 U-02` (gating) |
| Thai statutory source | Seven statutory items held | `20 U-09`, `21 §5` |
| Two of the three custom addon copies | Findings bounded to the copy that was read | `13 §3` caveat |
| `addons_archive` sweep for compensating guards | Eight negative claims are class **C** as whole-installation statements | `20 U-11` |
