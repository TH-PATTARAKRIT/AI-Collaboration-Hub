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
| `00_README_PACKAGE_INDEX.md` | 5594 | `ae791e7cc72e461303a64380fb57e719aa82d07c3a3c99c8e96126ec5021eaca` |
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
| `19_P05_CORE_RECON_HANDOFF_PACK.md` | 10580 | `6930ad2866433cd04eb72a9be5ccb14931962c8f83e2b545ff316cf8d10a1389` |
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
| `34_P05_CROSS_PROCESS_OWNERSHIP_REGISTER.md` | 6580 | `bd709f5528c7a7885830199806682223bf396e92b04c9cd8d4055cefb9490e07` |
| `35_P05_UNRESOLVED_EVIDENCE_REGISTER.md` | 6417 | `cd6c78565e524870626c10b687cca072b7ba98920a03681a8981e8c22ca78ebe` |
| `36_P05_AAS03_TARGETED_CLOSURE_CHALLENGE.md` | 17228 | `40b310848c974ea33560d872872498ad898a30f087ef0b0e71422534767b4cd2` |
| `37_P05_AAS_PLUS_TARGETED_CONSOLIDATION.md` | 8393 | `5359b2dbf38e3153b8d75c71918dfa4835496654a8d112fb1bde1329c65c5182` |
| `38_P05_PMO_EXIT_REVIEW.md` | 8909 | `fcf593be495f1c7ff88eaac688460f80816fa901ac18f6eac8f60353dfc30aef` |
| `39_P05_RESEARCH_ERROR_AND_REVISION_LOG.md` | 18586 | `768ee83a5cfb2365ce908b502ee6ae9664d937b30848d28d070df6a269c400bd` |

> **`14_P05_EVIDENCE_MANIFEST.md` is deliberately excluded from its own table** — a file cannot
> contain its own hash. All 39 other files are listed. Verify them with `shasum -a 256 *.md`, and
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
