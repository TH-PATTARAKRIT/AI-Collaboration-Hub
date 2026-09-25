# SMEsPlus Community19 G01-G04 RED TEAM Checkpoint R14

Date: 2026-09-25
Mode: A1 Source Evidence + QUESTION GATE independent integrity replay + roster recovery
Formal Coverage: NOT AUTHORIZED / NOT CALCULATED

## Control boundary
- Pipeline: A1 Source Evidence -> QUESTION GATE -> A2 Blind Runtime -> Reconciliation -> A3 Independent Adversarial Verification -> MASTER.
- A2/A3/MASTER are prohibited for any exact module/batch unless its governed question document/question bank is present, verified, frozen, and independently eligible.
- No Evidence = No Progress.
- Source Presence != Runtime Reachability.
- Canonical Function-ID denominator is not Boss-frozen; Formal Coverage is prohibited.

## Runtime state
Authorized Community19 device `THPATTARAKRIT-SOLUTION-SERVICE-2.local` is OFFLINE.
Last seen: `2026-09-24T12:53:18.011+00:00`.
Therefore A2 Blind Runtime was NOT EXECUTED. Reconciliation, A3, and MASTER do not advance.

## Roster recovery / question-authoring control
- Governed counts remain G01=23, G02=11, G03=11, G04=9.
- Controlled row-level roster pointer remains `GROUP_STRUCTURE_V2_CORE.tsv` SHA-256 `203ff43e7844a734de5e9aaebb91529e46dd7998423d4d5772999ed0db9ff5bf`.
- Exact-name, related-name, and exact-hash Google Drive searches returned no accessible roster artifact.
- Current GitHub state still exposes references to the roster but not its row-level bytes.
- New governed artifact `OVQDT_G02_G16_ROSTER_HOLD_20260925_1521.md` (Git blob `2d3adba808f3c114711fe853577743bf3f9b0156`) explicitly places G02, G03, and G04 in `EVIDENCE POINTER NOT VERIFIED / HOLD` for question authoring and forbids converting category/prefix/dependency/count-matching candidates into governed membership.
- No candidate module name is promoted to canonical G02-G04 membership.

## G01 PLATFORM_BASE — A1 source delta
Upstream source anchor: `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`.

New verified source blobs:
- `odoo/addons/base/models/ir_attachment.py` = `905ae118b8c8e5050fdc33eb1631c88e3926b888`
- `odoo/addons/base/models/ir_sequence.py` = `920e0b2347f850b60c1bf8b392f82a2c7f964272`
- `odoo/addons/base/models/res_currency.py` = `015ca78353c734949545d4364f500d4d57f32d9f`
- `odoo/addons/base/models/res_lang.py` = `563b4eff214fbd9940661b9f76ee3a3aa571c76c`

Static findings:
1. `ir.attachment` has admin-only storage migration; sanitized filestore paths and collision checks; GC uses an explicit table lock; XML-like uploads can be forced to `text/plain` for users without view-write authority; URL-served binary attachment writes are restricted to serving groups; attachment access is conditioned by public state or access to the referenced model/record/field/creator path.
2. `ir.sequence` disables sudo commands, rejects zero increments, distinguishes standard versus `no_gap`, scopes sequences by company/date-range, and uses row locking for `no_gap` progression.
3. `res.currency` enforces unique currency code and positive rounding, automatically toggles multi-currency group behavior, blocks deactivation of a currency used by a company, and resolves rates from global or root-company records.
4. `res.lang` disables sudo commands, enforces unique name/code/url-code, requires at least one active language, and rejects disallowed date/time format directives.

Disposition: A1 ACTIVE / VERIFIED STATIC DELTA / BASE NOT COMPLETE. None of the above is runtime proof.

## G01 QUESTION GATE — new independent defect
### W1-B06 / html_builder
Re-check confirms the previous defect persists.
- Module bank SHA-256 actual = manifest declared = `893a84d23035083c95d1da81dc12ce1559acba09093325b47f64ff8c2410ba56`.
- Standard-55 SHA-256 actual = manifest declared = `f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d`.
- Module bank contains 40 unique `QID:` values.
- `FREEZE_W1-B06.json` SHA-256 = `ed6079aff9fa4464dc9e750a0b63b8934c8cbae8e48e7c25754c6c87ce518851`.
- Manifest-declared freeze hash = `58e86d15836770a20a79c18d8d776db57c6da09a9cea0de5114485184049fa94`.
- Canonical `freeze_batch.py` replay = `a01a5d7236cee621e4e1833a55d0423f90d23c268c4c587b7bfca562dac77035`.
- Result: MISMATCH.

Disposition: `W1-B06 = HOLD / FREEZE-INTEGRITY MISMATCH / NOT A2-ELIGIBLE`.

### W1-B07 / html_editor — NEW
The question programme added W1-B07 and marks it as rolling-frozen, but independent replay finds the same class of freeze-integrity defect.
- `G01_HTML_EDITOR_GMVQ_MVQ_40_V1.00_DRAFT.md` SHA-256 actual = manifest declared = `a421e3177abd55333a3647ead363f5e29389223581755b76273cdb84106ba619`.
- Module bank contains 40 unique `QID:` values (`Q001` through `Q040`).
- Standard-55 SHA-256 actual = manifest declared = `f6726f111932aecce4432daf3e412d0c9de3291fa45fa8908e9e89ee79cb540d` and has 55 unique STD-Q identifiers.
- `FREEZE_W1-B07.json` SHA-256 = `c2bef1c1599818e881b429fa163e5a221e6de2f957e2b898dc50010b1f826416`.
- Manifest/sidecar declared batch hash = `ea24b270cf375fc108735ca6e15d68500dd9b5cfb69e849bd2eb673a232d332e`.
- Canonical `freeze_batch.py` replay = `6533318143afe5a19d0483cddc4b5b84bf5f19e9e98478ffb21cd5001650774d`.
- Result: MISMATCH.

Disposition: `W1-B07 = HOLD / FREEZE-INTEGRITY MISMATCH / NOT A2-ELIGIBLE`.

The OVQDT rolling-freeze status is therefore not accepted by RED TEAM as A2 eligibility for B06 or B07. No question was edited or invented. Governed re-freeze/re-authorization is required.

## G02 IDENTITY_ACCESS — candidate source deepening only
Exact governed 11-row roster remains unrecovered; the following are source-presence evidence for already-recorded candidate modules only and receive NO CANONICAL MEMBERSHIP CREDIT.

New verified blobs:
- `addons/auth_password_policy/models/res_users.py` = `c4e9fd0e61fedbea26ced9201fdeb1a3283bb804`
- `addons/auth_password_policy/models/res_config_settings.py` = `1583bb0f0dc0c37c889109caec17d420d5710ab9`
- `addons/auth_oauth/models/res_users.py` = `091c72b98d383c8e8a6617cea9d845cf89e43fdc`
- `addons/auth_oauth/models/auth_oauth.py` = `f5879ef555a2c46aef763ddf3db3aa68b58b4a24`

Static findings:
1. Password policy reads minimum length from a governed config parameter and checks it before setting passwords; zero disables the minimum-length rule.
2. OAuth user identity is unique per provider+UID; stored access token is hidden with `NO_ACCESS`; token removal is restricted to ERP manager or self; provider endpoints and enabled state are explicit configuration.

Question Gate: G02 remains governed HOLD / WAIT QUESTION because exact roster evidence and a frozen module-specific question package are absent.

## G03 MASTER_DATA — verified anchor deepening
The full 11-row roster remains unrecovered. Evidence below is within already-established `product` / `analytic` anchors; it does not infer the remaining roster.

New verified blobs:
- `addons/product/models/product_product.py` = `6519834b4ab045a1b0f0db496279ccc51528b0de`
- `addons/analytic/models/analytic_distribution_model.py` = `a9083cf1a447f69552caf03d98b190d6647dc8ea`

Static findings:
1. Product variants inherit from product templates, apply parent-of company-domain checking, carry separate variant barcode/reference identity, restrict variant attribute-value deletion, and keep `standard_price` company-dependent.
2. Analytic distribution models enforce automatic company checking and reject company-specific analytic accounts inside a shared or different-company distribution model; distribution merge behavior is plan-aware.

Question Gate: no exact governed/frozen G03 package; `WAIT QUESTION`.

## G04 ACCOUNT_BASE — account-boundary deepening
The exact nine-row roster remains unrecovered. `account` source presence does not establish ACCOUNT_BASE versus ACCOUNT_PROCESS ownership.

New verified blobs:
- `addons/account/models/account_code_mapping.py` = `6fdb13ce3caf234a5411771a7c3c7eef99a589a2`
- `addons/account/models/account_account_tag.py` = `b494875f8d4b16b864e831d75cd9949520a8623a`

Static findings:
1. Account code mapping is a non-persistent UI projection designed for Chart-of-Accounts access only; direct search without account IDs is rejected, and expanded company mappings are limited to the current user's allowed companies.
2. Account tags enforce uniqueness by name/applicability/country and carry country-sensitive tax-tag semantics; this is metadata/accounting-boundary evidence only.

Question Gate: no exact governed/frozen G04 package; `WAIT QUESTION`.

## Downstream disposition
- G01: A1 ACTIVE. Exact frozen/eligible batches through the previously verified set remain eligible in principle, but runtime is unavailable. W1-B06 and W1-B07 are independently rejected at the Question Gate.
- G02: A1 ACTIVE / ROSTER RECOVERY OPEN / WAIT QUESTION.
- G03: A1 ACTIVE / ROSTER RECOVERY OPEN / WAIT QUESTION.
- G04: A1 ACTIVE / ROSTER RECOVERY OPEN / WAIT QUESTION.
- A2: NOT EXECUTED.
- Reconciliation: NOT STARTED.
- A3: NOT STARTED.
- MASTER: NOT STARTED.
- Formal Coverage: NOT AUTHORIZED / NOT CALCULATED.
