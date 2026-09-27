# G01 PLATFORM_BASE — Module `onboarding` — RED TEAM A2 Review

## 1. Header

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A2 (functional/semantic verifier of A1 conclusions); independent of A1 |
| Governed group / module | G01 PLATFORM_BASE / `onboarding` |
| A1 package under review | `A1_SOURCE_EVIDENCE_LANE/G01_A1_PACKAGES/G01_ONBOARDING_A1_PACKAGE_20260927.md` |
| A1 package sha256 | `50b0f4d675880e20dd64319ba8d904fbe31ac6f60e0e4cfdc0df2959c12271a9` |
| Upstream Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_ONBOARDING_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `c2f11c68f411264a84864064bec52d54dedfa63e1d694a6c54e91952eaf3f651` (equals the value recorded in the A1 header) |
| Question Gate | Batch W1-B09 = **HOLD-LOCAL** (freeze hash not reproducible). A2 verifies claims only. QID-level lineage for this module is **NOT A3-eligible** until GMVQ re-freezes W1-B09. This is a gate condition, not an A1 defect. |
| Source anchor (independent re-check) | `odoo/odoo` @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/onboarding/`, fetched from raw.githubusercontent; blobs computed with `git hash-object` in scratchpad only |
| Date | 2026-09-27 |
| Lane B | None exists for this module (section 6) |
| **Disposition** | **A2 PASS WITH FINDINGS** |

Disposition reasons:
1. All 18 A1 claims are grounded in source; no claim is contradicted on its WHAT. 16 VERIFIED, 2 PARTIAL, 0 NOT_VERIFIED, 0 OUT_OF_SCOPE.
2. PARTIALs are scope overstatements: per-company stickiness (C11) is conditional on a company-bearing tracker existing, and the open-callback rule (C17) is only checked when the step-side panel link is written.
3. CONTRADICTION-ONBD-1 (documented `/onboarding/<route_name>` controller absent from module) is independently confirmed.
4. Material omissions (section 5) are additive and routable to Reconciliation/Proof. None requires A1 rework before REC. Handoff: Reconciliation, carrying 10 proof requirements.

## 2. Test plan (predeclared before verification)

Plan file sha256 `a13915d2464adcef5dc515bbe18512cda075e328507a6058d59720f3a34df3a6` (scratchpad, written before source re-read).

| TP | Test | Pass condition | Result |
|---|---|---|---|
| TP-1 | Lineage: sha256 of A1 package and Lane A packet; A1-recorded Lane A hash | Recorded equals recomputed | PASS |
| TP-2 | Re-fetch all 20 Lane A pointer files; probe controllers absence | All blobs equal pointer table; controllers 404 | PASS (20 of 20 match; `controllers/__init__.py` and `controllers/main.py` both 404) |
| TP-3 | Semantic re-read of every HIGH claim and every CRQ/contradiction item: render mutation incl. closed panel (C06, C08); per-company stickiness (C11); system-only ACL (C15); missing controller (C16); scope-change reset (C12); co-existence (C13) | Claim meaning matches source behaviour, not just file identity | Done, section 3 |
| TP-4 | Business framing: setup-guidance tracking in multi-company SaaS | No overclaim / no material omission of company, privilege or state risk | SF-O01..SF-O05 |
| TP-5 | Omission scan: 4 model files, ACL, templates, views/menus, tests | Material behaviour absent from A1 recorded | OM-O01..OM-O09 |
| TP-6 | Lane B classification | NOT_APPLICABLE / UNCORROBORATED / MISSING_REQUIRED_RUNTIME_PROOF; never FAIL | Section 6 |
| TP-7 | Proof requirements for inherently runtime claims | Falsifiable, expected + fail condition | Section 7 (10 items) |
| TP-8 | Gate note | W1-B09 HOLD-LOCAL recorded; no QID answered | Header |

## 3. Claim verdict table

| Claim | A1 conf. | A2 verdict | A2 basis (independent re-read) |
|---|---|---|---|
| A1-G01-ONBD-C01 | HIGH | VERIFIED | Manifest: hidden category, depends on `web` only, data = 3 view files + ACL, no seed/panel data. |
| A1-G01-ONBD-C02 | HIGH | VERIFIED | Four models; route key required with DB uniqueness; ordered many-to-many panel↔step; step links back to many panels. Note: "one-word" is a label only, not enforced (OM-O08). |
| A1-G01-ONBD-C03 | HIGH | VERIFIED | Both trackers carry a functional unique index treating empty company as a value. Concurrency test (tagged non-standard, post-install) expects exactly one winner and one uniqueness violation; model code has no catch. |
| A1-G01-ONBD-C04 | HIGH | VERIFIED | Step validation filters to not_done and sets just_done; already-validated steps return empty. Missing step-progress records are created for the context company (or empty company for global steps), linked only to panel trackers of the context company or none. |
| A1-G01-ONBD-C05 | HIGH/LOW | VERIFIED | External-reference resolution is generic (no type check); three outcome strings returned. Non-step reference failing is a correct LOW inference. |
| A1-G01-ONBD-C06 | HIGH | VERIFIED | Render-state routine collects every just_done step of the panel for the current context and moves them to done before returning; docstring states the once-only intent and that only "the onboarding controller" should call it. Refinement: see OM-O02 (consumption crosses panels and companies). |
| A1-G01-ONBD-C07 | HIGH | VERIFIED | Stored state computed as done only when the count of done-like step trackers equals the panel's step count. Rendered panel value: `closed` if closed flag; else `just_done`/`done` only when stored state is done. Refinement: a not-done, not-closed panel has **no** panel-state key in the render output (absence, not a `not_done` value); the container template only reacts to `just_done`. |
| A1-G01-ONBD-C08 | HIGH | VERIFIED | Consolidation call precedes the closed-flag branch; a closed panel's render still converts just_done to done. Nothing restores it on reopen. |
| A1-G01-ONBD-C09 | HIGH | VERIFIED | Panel write recomputes tracker step links when the step set changes; test shows stored state returns to not_done after adding a step to a closed completed panel. Refinement: the closed flag is untouched, so the rendered state stays `closed` while the stored state is not_done. See OM-O04 for the cross-company side of the recompute. |
| A1-G01-ONBD-C10 | HIGH | VERIFIED | Close sets flag, toggle flips, model entry point resolves reference and quietly no-ops if missing; per-company test shows closed flag differs between companies. Refinement: close on a panel with no tracker is also a silent no-op (OM-O09). |
| A1-G01-ONBD-C11 | HIGH | PARTIAL | Compute and design comment verified; step default per-company verified. Overclaim: stickiness holds only while at least one tracker with a company exists. If the panel never had a company tracker, or all company trackers are removed (company deletion cascade, admin deletion), removing the last per-company step reverts the panel to global. "Scope can only move from global to per-company" is not guaranteed by source. |
| A1-G01-ONBD-C12 | HIGH | VERIFIED | Step write deletes all progress of steps whose per-company flag changed (all companies); linked panels that are per-company with only global trackers have those trackers deleted and recreated for the writer's current company only. Refinements: the panel refresh runs on every step write, not only on flag change; tracker deletion also discards the closed flag (OM-O07). |
| A1-G01-ONBD-C13 | HIGH/LOW | VERIFIED | Current tracker = company is context company or empty; no record rule; ACL file only. Refinement to LOW co-existence part: if a global and a company tracker co-exist, the filter yields two records and the subsequent single-record reads would most likely raise a singleton error rather than choose one (inference; PR-ONBD-07). |
| A1-G01-ONBD-C14 | HIGH | VERIFIED | Shared-steps test: completing the common step completes panel 2 once its other step is done. |
| A1-G01-ONBD-C15 | HIGH/MED | VERIFIED | 12 ACL rows; only system group has full CRUD; "all" and internal-user rows are all-zero. No elevation calls in model code. A module test comment states the ERP-manager group has no access to onboarding, supporting the MED implication. |
| A1-G01-ONBD-C16 | HIGH | VERIFIED | Package imports models only; both controller paths 404; field comment and docstring reference a route and controller. CONTRADICTION-ONBD-1 confirmed. Tests explicitly "simulate role of controller" by creating trackers before rendering. |
| A1-G01-ONBD-C17 | HIGH | PARTIAL | Render values carry close model/method; step template carries step model and open-method names for client dispatch. Constraint verified only in its narrow form: it is declared on the step's panel link and fires when that link is written from the step side (test does exactly this). Clearing the open-callback name on an already linked step is not re-checked, and whether linking from the panel side triggers the check is not established from module source (PR-ONBD-06). |
| A1-G01-ONBD-C18 | HIGH | VERIFIED | Two menus under the base technical "User Interface" parent; list header and form header both carry the toggle button; no cron/config/settings; company cascade on both trackers; company-deletion test is skipped. |

Totals: VERIFIED 16 · PARTIAL 2 · NOT_VERIFIED 0 · OUT_OF_SCOPE 0.

Contradiction/CRQ items: CONTRADICTION-ONBD-1 confirmed (within-module). CRQ-ONBD-1..7 are well-founded. CRQ-ONBD-1 should be widened per OM-O02 (celebration consumed across panels and companies). CRQ-ONBD-2 should add the closed-flag loss (OM-O07). CRQ-ONBD-6 should add OM-O04.

## 4. Semantic / business findings

- SF-O01 (read-mutates-state, C06/C08): Framing correct. Business consequence: the "just completed" acknowledgement is a shared, stored fact, not a per-viewer one. For a per-company panel, the first person in that company who renders consumes it for every colleague; for a global step, the first render in any company consumes it everywhere.
- SF-O02 (scope, C11/C12): The per-company property is derived, not declared. It is inferred from step flags and tracker history, so the same panel can have different scope depending on data history. Downstream design must not treat panel scope as configuration.
- SF-O03 (privilege, C15/C16): Because only the system group has model rights and the render entry point is outside the module, the effective privilege of every normal-user interaction is decided by an unidentified consumer. A1's framing (gap, not assertion) is correct.
- SF-O04 (company isolation, C13): Company separation is a context filter only. With no record rule, any system-group user sees all companies' trackers in the technical menus, which is expected for a technical admin surface.
- SF-O05 (panel completion, C07): Completion is a count comparison. It does not check that the done-like trackers belong to the panel's current steps; correctness relies on the recompute on step-set changes (see OM-O04).

## 5. Omissions (material, not in A1)

- OM-O01 Render prerequisite: the rendering-values routine requires an existing current tracker (single-record assertion). Without prior tracker creation (a consumer responsibility, as the tests simulate), rendering fails. A1 does not state this ordering dependency.
- OM-O02 Cross-panel and cross-company consumption: consolidation acts on step trackers, and step trackers are shared by every panel containing the step and, for global steps, by every company. Rendering panel A consumes the just_done state that panel B (or another company) would have shown.
- OM-O03 Empty panel: a panel with zero steps satisfies the count comparison and is stored as done as soon as a tracker exists.
- OM-O04 Cross-company recompute (inference): the tracker step-link recompute resolves step progress in the current company context but is applied to all trackers of the panel, including other companies' trackers. A step-set change made from company A may re-link company B's tracker to company A's step progress.
- OM-O05 Open-callback rule scope (see C17 PARTIAL).
- OM-O06 Step images are served through the generic image URL of the step model; with system-only ACL, non-system viewers depend on framework placeholder/access behaviour (unverified).
- OM-O07 Scope-change rebuild also discards the closed/hidden flag, so a hidden panel reappears.
- OM-O08 Route key "one word" is not enforced; only required + unique.
- OM-O09 Close/hide before any tracker exists is silently lost.

## 6. Lane B classification

No Lane B evidence exists in the repository for `onboarding`. Absence is not a failure.

| Claim | Classification |
|---|---|
| C01, C02, C16, C18 | NOT_APPLICABLE (static declaration / structure / absence) |
| C04, C05, C07, C09, C10, C12, C14 | UNCORROBORATED (runtime-observable, behaviour fully determined by source) |
| C03, C06, C08, C11, C13, C15, C17 | MISSING_REQUIRED_RUNTIME_PROOF (concurrency, access-control, and edge-state conclusions that source alone cannot settle) |

## 7. Proof requirements

All in an authorized, isolated test instance with a synthetic consumer panel; no production systems.

| PR | Claim(s) | Procedure | Expected (source prediction) | Fail condition |
|---|---|---|---|---|
| PR-ONBD-01 | C06, C08 | Validate a step, close the panel, render once, reopen, render again | First render returns closed; second render shows step as done, no just_done | Step still just_done after the closed render |
| PR-ONBD-02 | OM-O02, SF-O01 | Step shared by panels A and B; validate; render A; render B | B shows the step as done (celebration consumed by A) | B shows just_done |
| PR-ONBD-03 | C15, SF-O03 | As an internal non-system user without elevation, call render and step validation | Access error | Operation succeeds without elevation |
| PR-ONBD-04 | C11 | Panel with one per-company step and no trackers; switch step to global; read scope. Repeat after deleting all company trackers | Scope reverts to global in both cases | Scope stays per-company |
| PR-ONBD-05 | OM-O04 | Per-company panel with trackers for companies A and B, B's steps partly done; from A add a step to the panel; inspect B's tracker links and state | B's tracker linked to A's step progress (contamination) | B's links remain B-scoped |
| PR-ONBD-06 | C17, OM-O05 | (a) Link a step without open callback from the panel side. (b) Clear the callback of an already-linked step | Record whether a validation error is raised in each case; source predicts (b) passes | (b) raises → constraint scope wider than source reading |
| PR-ONBD-07 | C13 | Force co-existence of a global and a company tracker for one panel; read current state | Singleton-type error | A single tracker is silently chosen |
| PR-ONBD-08 | C16 | Cross-module source search at the anchor for the owner of the `/onboarding/<route_name>` route and its privilege mode | Owner identified, with elevation mode recorded | No owner found → record as dead documentation |
| PR-ONBD-09 | OM-O01 | Render a panel before any tracker exists | Single-record assertion error | Render succeeds |
| PR-ONBD-10 | C03 | Execute the non-standard concurrency test | Exactly one tracker, one uniqueness violation | Two trackers or no violation |

## 8. Limitations

- Static source at a single anchor commit. JS client (hide/close dispatch, reload on close) and framework internals (constraint triggering on inverse links, image serving, singleton errors) were not read.
- Nothing here is runtime proof; section 7 defines what would be.
- No QID answered; W1-B09 HOLD-LOCAL means QID-level lineage is not A3-eligible until re-freeze. No Formal Coverage claim; no percentages.
- Clean room: neutral WHAT/WHY/RISK; identifiers are evidence pointers; no code reproduced.
- A1 package and Lane A packet were not modified. No git operations performed.
