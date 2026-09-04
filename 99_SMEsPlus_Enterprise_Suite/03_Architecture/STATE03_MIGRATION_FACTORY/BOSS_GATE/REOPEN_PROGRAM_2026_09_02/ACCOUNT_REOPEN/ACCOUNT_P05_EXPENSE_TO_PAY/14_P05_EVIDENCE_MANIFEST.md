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
| Commit 2 | `1172f79` — challenge consolidation, corrections, final registers, terminal HOLD |
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
| `00_README_PACKAGE_INDEX.md` | 3294 | `28270339fafd9f9de06bd17ad5182b20f3d30275e6e8bc7f05c4ad340ff04ab6` |
| `01_P05_PROCESS_MAP.md` | 18649 | `cf9482306f9228c3f06a704a2b0df019b7b25359dc1da93222310e0cfaff4914` |
| `02_P05_EXPENSE_CLASSIFICATION_MATRIX.md` | 13228 | `da49426ffd061a6a543a8d87bce0114a37edf08f2250f9c2b10aa7d2f7b4ea52` |
| `03_P05_EXPENSE_RECOGNITION_MATRIX.md` | 9402 | `7e552026f3160bebad07c83b8dba6014c415bd1ed561aa3f8036b9249b2b335e` |
| `04_P05_EMPLOYEE_VENDOR_PAYABLE_MATRIX.md` | 8872 | `ad64ea45db3dd21ddd5fc3980211fd00ca6d73fc91def3506b0fe12d80a286ca` |
| `05_P05_EVENT_TO_GL_MATRIX.md` | 15468 | `da675b96a690b7be456a7dbfe5561832c4ff4b320ff7f2f9102a8faa97462cbb` |
| `06_P05_ANALYTIC_HANDOFF.md` | 4227 | `9cf95f4b4ae4afca14015ff7512285f59b6aa21c761b49be7df19a883d25a5f6` |
| `07_P05_TAX_WHT_MATRIX.md` | 23156 | `bb3f266435cb3633525bf1e499aa8ea0f0df79871efd98fc96b7ab2bca379804` |
| `08_P05_SETTLEMENT_RECONCILIATION.md` | 7756 | `6c95cbc2a3fb2f7bf82878cf36fde240d494393cd2d31b468c1630c14783c3c0` |
| `09_P05_CROSS_PROCESS_OWNERSHIP.md` | 6531 | `16a7b3c4a34eadf634464471e1f954dbf3c1df94660e401036faad6d420a2d12` |
| `10_P05_EDGE_CASE_MATRIX.md` | 30014 | `f594572bd91b506046e8d72424e22f9deb3374c899eb90c9bc31e08afc1363b8` |
| `11_P05_CONTRADICTION_REGISTER.md` | 13703 | `51936ff89a63cff93b8828be30370b4f89dc52461811fa0de7847863fe2a405e` |
| `12_P05_DEPENDENCY_REGISTER.md` | 6292 | `d94c95a1ca1f04500040dc856082c117aa4005a8bbfb169efa47c3506fd7768b` |
| `13_P05_SOURCE_LINK_REGISTER.md` | 7961 | `1156148d7dedeb8e6daab5b09fff7bc1f57193737f0118f170be8aa2e5ed1b98` |
| `15_P05_REVISION_LOG.md` | 7583 | `e485167a512d14f9c2e6e185b1b8753d25aa4c278334d87a37d80bf9dfc9666d` |
| `16_P05_AAS03_CHALLENGE.md` | 16487 | `bca451badc1b2fec452bb754b39fa2f8e13ed20399986be10eae202425e99cf9` |
| `17_P05_AAS_PLUS.md` | 12876 | `1ccc4f26798646ea3116bcf3468f46d5fc4bc7f366cb686688137b87d2f49bf4` |
| `18_P05_PMO.md` | 10443 | `b6ef5d02eaa9a6459ab83403790b5fbe32200ee9ad8c1dda5898afe633714569` |
| `19_P05_CORE_RECON_HANDOFF_PACK.md` | 8988 | `b1d64ed6dffa45c0d30eb3dd9892c7b0268110353dafebea5e75427f4073e5ec` |
| `20_P05_UNRESOLVED_REGISTER.md` | 4662 | `737e0706225a2e484440c93c1f46b6154aaddb85a4f173a5102c845765853138` |
| `21_P05_NEGATIVE_CLAIM_REGISTER.md` | 13694 | `c995ff8e46ea3c83b85e0a9375d3b2532aecbc7367de66b2a067806a759196d3` |
| `22_P05_SCOPE_OWNERSHIP_MATRIX.md` | 14168 | `18374ef1e2bac977e4c109581b9a800d94da1e4e3aad4a24ea87cd558165faa4` |

> **`14_P05_EVIDENCE_MANIFEST.md` is deliberately excluded from its own table** — a file cannot
> contain its own hash. All 22 other files are listed. Verify them with `shasum -a 256 *.md`, and
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
