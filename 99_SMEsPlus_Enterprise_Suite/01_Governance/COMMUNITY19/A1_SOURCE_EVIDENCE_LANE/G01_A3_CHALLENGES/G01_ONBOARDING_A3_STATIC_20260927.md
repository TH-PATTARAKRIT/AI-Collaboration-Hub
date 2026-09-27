# G01 PLATFORM_BASE — Module `onboarding` — RED TEAM A3 Independent Challenge (STATIC, CLAIM-LEVEL)

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A3, an independent adversarial challenger. It did not author Lane A, A1, A2, REC or PROOF |
| Module | G01 PLATFORM_BASE / `onboarding` |
| Date | 2026-09-27 (intake 2026-09-27T15:21:45Z) |
| Scope | STATIC, CLAIM-LEVEL only. Runtime is NOT-EXECUTED, which means it neither passed nor failed. MVQ QID lineage is **NOT A3-ELIGIBLE** (W1-B09 HOLD). Standard 55 was sampled |
| Source anchor | `raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/onboarding/` (A3 re-fetched it independently; 11 module files, all blobs MATCH the Lane A pointers) |
| **Disposition** | **A3 STATIC PASS WITH DEFECTS (route to REC; PROOF)** — the source-level substance holds; process rules 1–4 and one PROOF predicate change are defective |

### Intake (sha256, `scratchpad/a3_ui4/intake.sha256`)

| Input | sha256 |
|---|---|
| Lane A | `c2f11c68f411264a84864064bec52d54dedfa63e1d694a6c54e91952eaf3f651` |
| A1 | `50b0f4d675880e20dd64319ba8d904fbe31ac6f60e0e4cfdc0df2959c12271a9` |
| A2 | `8f1ab5f7313f49ab16e77725a79dd02c75f4cd24d4a57a46d260cbb899386089` |
| REC | `fdd2d41b3b3cfdc7d5612820ff46c6c226da92d95d27012adbbd384308b91889` |
| PROOF | `841e394aebc53078b519d655d0783326c106d6271b5394fbc4f26d525da5c219` |

Lane A, A1 and A2 match the values recorded downstream. REC has no downstream recorded value, because PROOF does not record it (see rule 4).

## 2. Challenge log

| # | Challenge | A3 re-check (A3's own fetch) | Disposition |
|---|---|---|---|
| A3-ONBD-01 | REC-ONBD-11 CONTRADICTION: per-company scope is recalculated and reverts to global when no company tracker exists | `models/onboarding_onboarding.py`@9ed728d6 L22–24: the per-company flag is a non-stored compute. L45–54: true iff any tracker carries a company OR any linked step is per-company. The code comment (L47–49) states the intent that the flag is "sticky". Only a company-bearing tracker makes it sticky, and that tracker is created by the refresh routine (L92–102). With no company tracker, removing the last per-company step gives false, so the flag is not one-way. The A1 wording "can only move from global to per-company" is negated. Classifying it CONTRADICTION rather than GAP is defensible, because A2 PARTIAL cites source that directly negates an A1 sentence. | **UPHELD** (runtime effect NOT-EXECUTED, PC-ONBD-08) |
| A3-ONBD-02 | Propagation of the C11 negation | A1 BR-5 ("Scope is sticky. Once per-company, a panel stays per-company") and the A1 state line "Panel scope: global → per-company (one way)" repeat the negated position. REC did not reconcile BR or state items, so these lines would reach MASTER without the CONTRADICTION flag. | **CHALLENGE-SUSTAINED (REC)** |
| A3-ONBD-03 | `/onboarding/<route_name>` owner not found in 27 probes (PC-ONBD-15 INCONCLUSIVE) | A3 widened the search (log `scratchpad/a3_ui4/xmod_a3.txt` sha256 `7ed4be49ff299fda64fd3c05bcc57d629274e4f4c987f35ecaa16ed6b1e220f5`). It fetched the manifest and controllers package init for 15 modules (account, sale, account_payment, payment, website_sale, sale_management, stock, point_of_sale, web, base_setup, website, mass_mailing, hr, project, crm), plus `account/models/__init__.py`, `payment/models/__init__.py` and `account/data/onboarding_data.xml`. Findings: only `account` and `payment` declare a manifest dependency on `onboarding`. `account` ships a panel with a route key and a step-model extension. Neither module's controllers package imports an onboarding controller, and 0 controller inits in the set mention "onboarding". No owner was found. This is more consistent with stale documentation than before, but it is still not proof, because there is no listing API and other dependents cannot be enumerated. | **INCONCLUSIVE** (upstream INCONCLUSIVE classification UPHELD) |
| A3-ONBD-04 | Render-time just_done consumption across panels and companies (REC-ONBD-06/08/20) | `models/onboarding_progress.py`@26dacc18 L53–78: the render routine consolidates every just_done step progress it finds (L66–72) before the closed branch (L74). Step progress is keyed by (step, company-or-none) (`onboarding_progress_step.py`@311a0fef L21), not by panel. The current step progress resolves company in {none, current} (`onboarding_onboarding_step.py`@26218646 L47–63). So a render of panel A consumes the celebration of any panel that shares the step. For global steps (no company) it also consumes it for every company. Per-company steps are isolated per company. | **UPHELD** (runtime NOT-EXECUTED, PC-ONBD-02/04) |
| A3-ONBD-05 | PC-ONBD-05 excludes superuser use in tests | Re-scan: `models/*.py`, `__init__.py`, `models/__init__.py` contain 0 elevation constructs. `tests/test_onboarding_concurrency.py`@801def35 builds superuser environments (L25, L37, L49, L72), and `tests/test_onboarding.py`@32649804 L236 switches user, which lowers rights rather than raising them. Substance: the exclusion is sound, because test-harness code is not loaded in normal runtime. Process: the predeclared predicate said "scan all module .py … zero elevation calls in module code; FAIL: any elevation call". Narrowing it to "module runtime code" after execution, without a `POST-DECLARATION` tag, breaks rule 2. Under the literal predeclared predicate the case meets its fail condition. The PROOF disclosed the scope note, but should have recorded FAIL (lineage/predicate), or a tagged post-declaration re-scope. | **CHALLENGE-SUSTAINED (PROOF)**: substance UPHELD, predicate handling defective |
| A3-ONBD-06 | GAP items without a PR (REC-ONBD-21, 23–26) | Spot-checked REC-ONBD-25 (the scope-change rebuild unlinks trackers, so the closed flag is lost: `onboarding_onboarding.py` L98–102; `onboarding_onboarding_step.py` L85–87) and REC-ONBD-26 (closing with no tracker acts on an empty set: L79–81, L104–105). Both hold on source. | **UPHELD** |
| A3-ONBD-07 | C15 / ACL | `security/ir.model.access.csv`@f99bf429: only `base.group_system` rows are non-zero. The "all" and internal-user rows are all zero. | **UPHELD** |

### Static PASS re-execution (A3 independent fetch, blob-verified)

| PC | A3 re-execution | Citation check | Weakness flagged |
|---|---|---|---|
| PC-ONBD-01 | PASS reproduced | L53–78, L72, L74 exact | None |
| PC-ONBD-07 | PASS reproduced | L22–24, L45–54, L47–49 exact | Predicate checks structure only. Whether the compute is re-triggered after a tracker is deleted is framework behaviour (runtime) |
| PC-ONBD-13 | PASS reproduced | L56–69, L60–61 exact | The expected "singleton-type error" when both trackers co-exist is inference (assigning several records to a single-record field) and stays runtime |
| PC-ONBD-16 | PASS reproduced | L125–135; progress L60 exact | None |
| PC-ONBD-05 | Substance reproduced; see A3-ONBD-05 | ACL L2–13 exact | Predicate re-scoped after declaration (untagged) |
## 3. Process-rule compliance (MASTER C1B systemic findings 1–5)

Source of the rules: `01_Governance/COMMUNITY19/MASTER_CONTROLLED_HANDOFF_STATE_20260927_C1B.md` section "Systemic process findings". Evidence below is from the inputs, the upstream scratch folder `scratchpad/rec_ui4` (read only) and read-only `git log`/`git show`.

| # | Rule | Result for this batch (onboarding, html_builder, web_hierarchy, web_unsplash) | Evidence |
|---|---|---|---|
| 1 | Preserve the A2 `MISSING_REQUIRED_RUNTIME_PROOF` (MRRP) label; do not collapse it into `UNCORROBORATED` | **NOT MET** | None of the four RECs uses the MRRP label in any row. The label is kept only indirectly, where the REC class is UNKNOWN_PENDING_PROOF (whose definition cites MRRP). Where A2 classed a claim MRRP but REC gave it another class, only `UNCORROBORATED` remains: onboarding C11 (CONTRADICTION) and C17 (GAP); web_hierarchy C10 (GAP); web_unsplash C12 (GAP). html_builder has one MRRP claim (C06); it is UNKNOWN_PENDING_PROOF, so it is preserved indirectly only. |
| 2 | Tag any Expected/predicate text added after predeclaration `POST-DECLARATION` | **NOT MET** | 0 `POST-DECLARATION` tags in the four PROOF files. Untagged changes against `predeclared_proof_cases.tsv`: PC-ONBD-05 scope narrowed from "all module .py / any elevation call" to "module runtime code" (tests excluded); PC-UNSP-08 and PC-UNSP-26 steps gained "(mock-resolved)", and PC-UNSP-10 gained "(mock)". Most other rows are wording changes with the same meaning. |
| 3 | REC scans all A1 item classes (BR / states / exceptions / handoffs / gaps / CRQ) | **NOT MET** | The four REC tables reconcile only the claims (Cnn) and A2 omissions (OM). GAP and CRQ items are carried forward in prose. No BR-, state, exception or handoff item is reconciled (0 `BR-` mentions in the four RECs). Effect: onboarding BR-5 and the state line "Panel scope: global → per-company (one way)" still state the negated C11 position; web_unsplash state lines and BR-5 are not updated for REC-UNSP-12/21 and CONTRADICTION-UNSP-1. |
| 4 | REC frozen (sha256 recorded) before PROOF; PROOF header records the REC sha256 it consumed | **NOT MET** | None of the four PROOF headers records a REC sha256 (they give path + item count only). The REC files cite `laneb_search.txt` (sha256 `21b8a78d…0ce7f`), and that file's mtime is 15:13:14Z, after PROOF source fetch began (first `src/` file 15:11:03Z; `blobcheck.txt` 15:11:12Z). REC files were first committed at 15:14:38Z (onboarding), 15:15:22Z (html_builder), 15:16:10Z (web_hierarchy) and 15:17:15Z (web_unsplash), all after PROOF execution started. The html_builder REC was edited again between commits `b31a0e8` and `37823e6` (a one-line correction to a freeze-hash abbreviation; nothing recorded the change), and REC-HBLD-08 cites a PROOF case (PC-HBLD-07). |
| 5 | Cases-file sha256 + UTC timestamp written before first source fetch | **MET (with note)** | `predeclared_proof_cases.tsv` recomputed sha256 = `2203bab7a4d6ebdd38a61dccda74340a5c02c66774a6c5644e48441a2b22f307` (MATCH); `predeclared_sha256.txt` and `predeclared_time.txt` = 2026-09-27T15:10:27Z; first source file 15:11:03Z; 67 case IDs present (19 + 8 + 14 + 26). Note: `tree_probe.json` (15:09:19Z, before predeclaration) records a GitHub API tree-listing attempt that returned 403 with no source content. The timestamp evidence still rests on self-written files and mtimes in scratch, not on a committed record. |

## 4. Lineage

| Artifact | Commits (`git log --follow`, read-only) | Content check |
|---|---|---|
| Lane A | `07cca3c` 14:51:32Z | = intake sha256 |
| A1 | `a4373e7` 14:55:23Z, then `63318b8` 14:57:33Z | The earlier version differs (`4f2145ce…`). The final version = `50b0f4d6…` = the value recorded by A2. A2 consumed the final version |
| A2 | `5ffea26` 15:03:59Z | = value recorded by REC |
| REC | `f510676` 15:14:38Z | Committed after PROOF source fetch began (15:11:03Z). No frozen hash was recorded before PROOF (rule 4) |
| PROOF | `6d55fdb` 15:18:45Z | = intake sha256 |

Commit subjects are ignored, because MASTER checkpoint commits carry subjects that name other modules and stages; only content and hashes are judged. Predeclaration verified: `2203bab7…f307` at 15:10:27Z. Standard 55 bank sha256 `f6726f11…540d` = REC intake. Standard-55 sample: REC-ONBD-11 → STD-Q27 (company scope) and Q49 (shared-data ownership) fit topically; REC-ONBD-20 → Q28 (cross-boundary visibility) fits. No QID is answered. MVQ lineage: NOT A3-ELIGIBLE (W1-B09 HOLD).

Overclaim, Lane B and clean-room scan: no runtime outcome is claimed as proven; there are no percentages and no Formal Coverage. No Lane B exists, and none was misused: every Lane B column reads UNCORROBORATED or NOT_APPLICABLE, and nothing is FAIL for lack of Lane B. Clean room: 0 code blocks or code fragments across the five inputs, and identifiers are used as pointers only.

## 5. Defects routed

| ID | Owner stage | Severity | Defect | Required action |
|---|---|---|---|---|
| D-ONBD-A3-1 | REC | MED | BR-5 and the A1 state line repeat the C11 position that A2 negated. REC did not reconcile BR, state, exception or handoff items (rule 3) | Add REC items for A1 §2–§5 and flag BR-5 and the scope state line as CONTRADICTION (linked to REC-ONBD-11). Similarly align BR-1 with the C17 GAP |
| D-ONBD-A3-2 | REC | LOW | The MRRP label is lost for C11 (CONTRADICTION) and C17 (GAP); the Lane B column shows only UNCORROBORATED (rule 1) | Add the A2 MRRP label to REC-ONBD-11 and REC-ONBD-17 |
| D-ONBD-A3-3 | REC / PROOF | MED | REC was not frozen before PROOF, and the PROOF header records no REC sha256 (rule 4) | Freeze the REC (record its sha256), then re-issue the PROOF header with the consumed REC sha256. Results need not change if the REC content is unchanged |
| D-ONBD-A3-4 | PROOF | LOW | PC-ONBD-05 predicate re-scoped after declaration without a `POST-DECLARATION` tag (rule 2) | Record PC-ONBD-05 as FAIL against the literal predicate, noting that the fail is due to test-harness code only. Or add a tagged post-declaration case limited to runtime code |

## 6. Runtime / gate-blocked items

- RUNTIME NOT-EXECUTED (neither passed nor failed): PC-ONBD-02, 04, 06, 08, 10, 12, 14, 17, 19. The device is OFFLINE, and there is no Lane B.
- REC-ONBD-11 must not be resolved without PC-ONBD-08.
- MASTER handoff is pending the runtime results and the gate: MVQ W1-B09 HOLD-LOCAL; Formal Coverage is not authorized.
- GAP-1 (route owner) remains open (INCONCLUSIVE).

## 7. Limitations

- One anchor commit. Framework internals (constraint triggering on inverse links, singleton behaviour, re-triggering of the non-stored compute) and client JS were not read.
- The cross-module search is bounded: 15 extra modules (manifests and controller inits) plus 3 account/payment files. There is no listing API.
- No runtime executed, no results invented, and no external service contacted beyond `raw.githubusercontent.com`. Git was used read-only. Inputs were not edited. Scratch: `scratchpad/a3_ui4` (`intake.sha256`, `fetch1.txt` sha256 `d680485f…587c3c`, `xmod_a3.txt`).
- No percentages; no Formal Coverage; no QID answered.
