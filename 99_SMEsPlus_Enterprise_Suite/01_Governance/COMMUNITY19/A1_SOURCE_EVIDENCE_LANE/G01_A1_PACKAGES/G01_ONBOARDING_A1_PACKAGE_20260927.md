# G01 PLATFORM_BASE — RED TEAM A1 Package — `onboarding`

| Item | Value |
|---|---|
| Role | SMEsPlus RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `onboarding` |
| Lane A packet | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_ONBOARDING_LANE_A_PASS1_20260927.md` |
| Lane A packet sha256 | `c2f11c68f411264a84864064bec52d54dedfa63e1d694a6c54e91952eaf3f651` |
| Source anchor | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f`, `addons/onboarding/` |
| Gate status (header only) | Question batch W1-B09 = **HOLD-LOCAL** (freeze not reproducible). No QID answered, no bank edited. The Question Gate controls A2+ QID lineage. It does not control A1 synthesis. |
| Lane B dependency | None. A1 does not wait for Lane B, and no runtime evidence was consumed. |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |

Clean-room note: claims are neutral WHAT / WHY / RISK statements. Identifiers are evidence pointers only. No vendor code is reproduced, and no reuse of vendor schema, ORM, workflow, UI or naming is recommended.

Evidence key (blob SHA-1 from Lane A; "V" = re-verified by an A1 spot-check, see §9): E1 `__manifest__.py` eaa50cca…; E2 `__init__.py` dc5e6b69… V; E4 `models/onboarding_onboarding.py` 9ed728d6… V; E5 `models/onboarding_onboarding_step.py` 26218646… V; E6 `models/onboarding_progress.py` 26dacc18… V; E7 `models/onboarding_progress_step.py` 311a0fef… V; E8 `security/ir.model.access.csv` f99bf429… V; E9 `views/onboarding_views.xml` 7688f73d…; E10 `views/onboarding_menus.xml` f036c700…; E11 `views/onboarding_templates.xml` 58cd0c2d…; E12 `tests/test_onboarding.py` 32649804…; E13 `tests/test_onboarding_concurrency.py` 801def35…

## 1. Claims

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence | Conf. | Layer |
|---|---|---|---|---|
| A1-G01-ONBD-C01 | WHAT: A hidden, reusable engine for setup-guidance panels and their completion tracking. It depends only on `web` and ships no panel content or seed data. WHY: consumer apps declare their own panels and steps and reuse the tracking. RISK: no panel behaviour is visible without a consumer module. | E1 | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C02 | WHAT: There are four persisted entities: panel definition, step definition, panel-progress tracker and step-progress tracker. A panel has a globally unique one-word route key (DB constraint) and an ordered many-to-many link to steps. A step can be shared by several panels. | E4 V; E5 V; Lane A §2.2 | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C03 | WHAT: Each panel has at most one progress tracker per (panel, company-or-none), and each step at most one per (step, company-or-none). A functional unique index treats "no company" as a value. RISK: concurrent first-time creation is settled by a DB uniqueness violation that model code does not catch (the concurrency test shows exactly one winner). | E6 V; E7 V (uniqueness); E13 | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C04 | WHAT: States are not_done, just_done and done. A step moves only from not_done to just_done when validated. Steps already validated are skipped, so validation is idempotent and returns an empty set. Missing step-progress records are created lazily for the current company context at validation time. | E7 V; E5 V | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C05 | WHAT: Validation by external reference returns one of three outcomes: not found, just done or was already done. A missing reference is a quiet outcome, not an error. RISK: the reference is resolved generically and its type is not checked before the step-validation call. A reference to a record that is not a step would fail at runtime (inference). | E5 V | HIGH (outcomes) / LOW (non-step ref) | SOURCE-STATIC |
| A1-G01-ONBD-C06 | WHAT: A read changes stored state. The routine that fetches a panel's state for rendering also moves every just_done step of the current context to done. The docstring says this is so the celebration renders only once. RISK: the read path writes, so a duplicate, concurrent or prefetch render can use up the one-shot state before the user sees it. | E6 V (render-state routine, docstring); E7 V (consolidation) | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C07 | WHAT: The stored panel-tracker state is computed from its step trackers and only ever holds not_done or done. just_done and done both count as complete, and the panel is done when the number of complete step trackers equals the number of steps on the panel. The panel-level just_done and closed values exist only in the rendering output: just_done appears when the panel is done and consolidation happened on this render, and closed overrides everything else. | E6 V | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C08 | WHAT: Consolidation (just_done to done) runs before the closed check. RISK: rendering a closed panel still uses up pending just_done step states. If the panel is later reopened, the one-time completion feedback is gone. | E6 V | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C09 | WHAT: Linking a new step to a panel recomputes its trackers. Adding a step to a completed panel, even a closed one, makes it not done again. | E4 V (write); E12 | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C10 | WHAT: Close sets a closed flag on the current tracker, and toggle flips it. A model-level entry point closes a panel by external reference and does nothing if the reference is missing. The closed flag belongs to the tracker, so per-company panels are closed per company. | E4 V; E6 V; E12 | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C11 | WHAT: A panel becomes per-company once any linked step is per-company or any tracker has a company. This flag is sticky: removing the last per-company step does not revert it. A code comment says this avoids merging progress. Steps default to per-company. WHY: prevents loss or merging of per-company progress. RISK: panel scope can only move from global to per-company. | E4 V (compute + comment); E5 V (default) | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C12 | WHAT: When a step's per-company flag changes, all of that step's progress records (across companies) are deleted. Linked panels that are now per-company but still have a global tracker have those trackers deleted and recreated for the current company only. RISK: completion history is thrown away when scope changes, and the rebuild targets only the company of the user making the change. | E5 V (write); E4 V (refresh); E12 | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C13 | WHAT: The current progress is the tracker whose company is the context company or empty. Company isolation comes only from this filter logic. No record rule exists. RISK: the lookup assumes at most one matching tracker. A global tracker and a company tracker existing together is not handled explicitly (see CRQ-3). | E4 V; E5 V; E8 V | HIGH (filter) / LOW (co-existence) | SOURCE-STATIC |
| A1-G01-ONBD-C14 | WHAT: Completing a step shared by two panels counts toward both. | E12; E5 V | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C15 | WHAT: The ACL grants full CRUD on all four models to the system group only. Rows for "all" and for internal users exist but grant no permission. The module defines no groups and no record rules. RISK: the module's own code never elevates rights (no elevated-access calls), so rendering or validating as an ordinary internal user fails the access check unless a consumer module elevates rights. Any such elevation is outside this module. | E8 V; E4/E5/E6/E7 V (no elevation calls) | HIGH (ACL) / MED (implication) | SOURCE-STATIC |
| A1-G01-ONBD-C16 | WHAT: The module declares no HTTP routes. The package imports only models, and a controllers package does not exist at the anchor (404). The panel's route-key field comment and the render-state docstring both refer to an `/onboarding/<route_name>` route and an "onboarding controller". RISK: the documented entry point lives outside the module, so the render/consolidation trigger and its privilege context cannot be traced here. | E2 V; E4 V; E6 V; S7 (404) | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C17 | WHAT: The render values pass the close callback's model and method name to the client, together with the steps, the computed state and the completion text. Step buttons carry open-callback method names that the client dispatches. A step cannot be linked to a panel unless its open-callback name is set (validation error). RISK: server-side methods are chosen by name through client dispatch. The available methods are limited by the definitions, which only the system group can author. | E4 V; E5 V (constraint); E11 | HIGH | SOURCE-STATIC |
| A1-G01-ONBD-C18 | WHAT: The backend offers two technical menus under a `base` technical parent. Each has list and form views, and the list has a "toggle visibility" action. There are no crons, config parameters or settings. Company deletion cascades to trackers. The related test is skipped. | E9; E10; E1; E12 | HIGH | SOURCE-STATIC |

## 2. Business rules
- BR-1: A step can be linked to a panel only if it has an open callback (C17).
- BR-2: A panel is complete when every step on it is complete. The just_done state counts as complete (C07).
- BR-3: Validation is one-way and idempotent: not_done to just_done only (C04, C05).
- BR-4: just_done is shown once and then turned into done by the render read (C06, C08).
- BR-5: Scope is sticky. Once per-company, a panel stays per-company. A scope change deletes progress (C11, C12).
- BR-6: Adding a step re-opens completion (C09). Close/hide is per tracker (C10).
- BR-7: Only the system group has model access (C15).

## 3. States / transitions
- Step (per step, per company or global): not_done → just_done (validate) → done (consolidated on render read). There is no reverse transition. Deleting progress on a scope change effectively resets it to not_done (C04, C06, C12).
- Stored panel state: not_done ↔ done, recomputed from steps. Adding a step brings back not_done (C07, C09).
- Rendered panel state: not_done | just_done (only on the render where consolidation happened) | done | closed (the closed flag overrides) (C07, C08).
- Panel visibility: open ↔ closed (close/toggle), per tracker (C10).
- Panel scope: global → per-company (one way) (C11).

## 4. Exceptions / failure modes
- Linking a step without an open callback raises a validation error (C17).
- Concurrent first creation of a tracker raises an uncaught uniqueness violation for the losing transaction (C03).
- Validating or closing a missing external reference is a quiet no-op or returns a "not found" outcome (C05, C10).
- An ordinary internal user without elevation gets an access error on every model operation (C15).
- A render can use up just_done states on a closed panel or on a duplicate render (C06, C08).

## 5. Cross-module handoffs
- `web`: backend assets and the generic RPC dispatch that client callbacks use (C17).
- `base`: technical menu parent, placeholder image and confetti image, and `res.company` (cascade) (C18).
- Consumer apps (not identified in this module): panel and step definitions, open and close callback implementations, the `/onboarding/<route_name>` render route and any privilege elevation (C01, C15, C16).
- `mail`: used only by tests (a helper import). It is not a manifest dependency (Lane A §3).

## 6. Evidence gaps (Lane A carried forward + A1)
- GAP-1 (G-ONB-1): the owner of the `/onboarding/<route_name>` route and controller has not been found (C16).
- GAP-2 (G-ONB-2): JS inventory and client behaviour (hide, close dispatch, reload on close) are not enumerated.
- GAP-3 (G-ONB-3): whether consumer render or validate paths elevate privileges, and how far (C15).
- GAP-4 (A1): behaviour when a global tracker and a company tracker exist together for one panel (C13).
- GAP-5 (A1): the transaction and isolation behaviour of the consolidation write inside a render read (C06). This needs runtime evidence.

## 7. CRQ candidates
- CRQ-ONBD-1: Should displaying progress ever change progress state? Or should the "celebrate once" acknowledgement be an explicit, idempotent per-viewer event? (C06, C08)
- CRQ-ONBD-2: When a step's scope changes between global and per-company, should completion history be kept or migrated instead of deleted? And should the rebuild cover all companies, not only the one making the change? (C12)
- CRQ-ONBD-3: What is the defined resolution when both a global and a company-specific progress record exist? (C13)
- CRQ-ONBD-4: What least-privilege model lets ordinary users view and advance their own guidance without system-level model rights or unrestricted elevation? (C15)
- CRQ-ONBD-5: Should concurrent first creation of progress be idempotent, for example get-or-create with retry, instead of surfacing a uniqueness failure? (C03)
- CRQ-ONBD-6: Should company-scoped progress be isolated by an enforced rule rather than by filter logic only? (C13, C15)
- CRQ-ONBD-7: Should callback actions dispatched by name be restricted to an explicit allow-list? (C17)

## 8. Contradictions
- CONTRADICTION-ONBD-1 — **CONFIRMED** (within-module scope): the panel's route-key field comment and the render-state docstring both refer to an `/onboarding/<route_name>` route and an "onboarding controller". The module has no controllers: the package imports only models, and the controllers package returns 404 at the anchor. Verified by S1, S2, S4 and S7. Whether a controller exists in some other module is not established. That part stays open as GAP-1.
- No contradiction was found between the Lane A findings and the re-fetched source. A1 adds C08 and C12 ("rebuild uses the current company only") as refinements. Neither contradicts Lane A.

## 9. Spot-check log (A1 re-fetch from raw.githubusercontent.com at anchor commit; `git hash-object` compared)
| # | Path | Recorded blob | Recomputed blob | Result | Claim(s) checked |
|---|---|---|---|---|---|
| S1 | addons/onboarding/models/onboarding_progress.py | 26dacc18…6474595 | 26dacc185dcd6533fc7212cf72021f5f06474595 | MATCH | C06–C08: render routine consolidates just_done→done; stored compute yields only not_done/done; closed override after consolidation; docstring references controller |
| S2 | addons/onboarding/models/onboarding_onboarding.py | 9ed728d6…2de0cb | 9ed728d6cbc8b6f45b090222c8b6f54a3f2de0cb | MATCH | C11–C13, C16: sticky per-company compute + comment; refresh deletes/recreates for current company; current = company or none; route comment |
| S3 | addons/onboarding/security/ir.model.access.csv | f99bf429…b351cc | f99bf429ceb2f8b24b2d247afc4e3c3cf5b351cc | MATCH | C15: 12 rows; only `base.group_system` has 1,1,1,1; all/user rows 0,0,0,0 |
| S4 | addons/onboarding/__init__.py | dc5e6b69…26b7b2 | dc5e6b693d19dcacd224b7ab27b26f75e66cb7b2 | MATCH | C16: imports models only |
| S5 | addons/onboarding/models/onboarding_onboarding_step.py | 26218646…3cac3623 | 262186464fc868d9c5623f131e9832433cac3623 | MATCH | C04, C05, C11 (default per-company), C12 (progress unlink on flag change), C17 (constraint) |
| S6 | addons/onboarding/models/onboarding_progress_step.py | 311a0fef…5813d1bce | 311a0fef450dfadbe4f835e3fa4085b5813d1bce | MATCH | C04, C06: only not_done→just_done; consolidate just_done→done |
| S7 | addons/onboarding/controllers/__init__.py | (absence) | HTTP 404 | ABSENCE CONFIRMED | C16, CONTRADICTION-ONBD-1 |

Result: 6 of 6 re-fetched blobs match (HTTP 200), and 1 absence was confirmed (HTTP 404).

## 10. Provenance
- Input: only the Lane A packet named in the header, pinned by sha256. Spot-check files were re-fetched from `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/onboarding/<path>` and hashed with `git hash-object` into scratch storage outside the repository.
- No Lane B, question bank, runtime or other-module material was used. No git operations were run on the repository.

## 11. Limitations
- Static source only: code being present does not prove it is reachable at runtime. No runtime proof and no Formal Coverage claim. No percentages.
- Where a claim depends on consumer modules (the privilege context, the render route), it is marked as an implication or a gap.
- Claims based on test files marked E12/E13 carry Lane A's blob record and were not re-hashed by A1.
