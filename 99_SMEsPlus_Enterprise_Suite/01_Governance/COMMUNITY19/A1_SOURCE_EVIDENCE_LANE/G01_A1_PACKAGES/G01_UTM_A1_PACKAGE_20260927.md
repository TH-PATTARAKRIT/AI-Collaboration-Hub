# G01 PLATFORM_BASE — RED TEAM A1 PACKAGE — Module `utm`

| Field | Value |
|---|---|
| Role | RED TEAM A1 (source-backed research synthesizer) |
| Group / Module | G01 PLATFORM_BASE / `utm` |
| Lane A input | `A1_SOURCE_EVIDENCE_LANE/G01_LANE_A_PASS1/G01_UTM_LANE_A_PASS1_20260927.md` |
| Lane A sha256 | `8b7a3df858acdb0fb5ed063c1337910708aef851bb43cc37974b1d018ffaac6c` |
| Anchor commit | `odoo/odoo` 19.0 @ `8d05257d83f9128953f580a066db67c48fcdb96f` (`addons/utm/`) |
| Topic lens (not answered) | `GMVQ/G01_PLATFORM_BASE/G01_UTM_GMVQ_MVQ_40_V1.00_DRAFT.md` (sha256 `af28ded258ac26abbd3962e019dc41754e5c0b46b3c3b8f5d0834e942f756ecd`) |
| Freeze batch / hash | W1-B03 / `1247c218ba4e2e6a57e259427030f4350881da56a5a28c59901a20f8b2d3a5d3` (ELIGIBLE) |
| Lane B dependency | None. A1 does not wait for Lane B. |
| Date | 2026-09-27 |
| Status | **A1 PACKAGE COMPLETE — HANDOFF TO A2** |
| Clean-room | Neutral WHAT/WHY/RISK only. No code, schema, ORM or workflow is reproduced or recommended for reuse. Identifiers are pointers only. |

## 1. Claims

Layer for every claim: SOURCE-STATIC. Evidence paths are relative to `addons/utm/`. Blob = git SHA-1. `[SC]` = re-verified in the spot-check (Section 10).

| Claim ID | Claim (WHAT / WHY / RISK) | Evidence (path @ blob) | Conf. |
|---|---|---|---|
| A1-G01-UTM-C01 | WHAT: when a new tracker name collides case-insensitively with an existing one, a unique-name generator appends a numeric counter suffix and fills gaps, instead of rejecting the name. Records being updated can be excluded so they do not collide with themselves. WHY: user input is never refused. RISK: near-duplicate trackers ("X", "X [2]") split attribution silently. | `models/utm_mixin.py` @ 0c8be65a [SC] | HIGH |
| A1-G01-UTM-C02 | WHAT: creating a medium or source always runs the generator. A campaign runs its identifier (falling back to its title) through it, and the identifier is recomputed from the title. RISK: renaming a title changes the identifier, which can affect attribution by label (G5). | `models/utm_medium.py` @ 539b4dc7 [SC]; `models/utm_source.py` @ 636587e9 [SC]; `models/utm_campaign.py` @ a9b07365 | MED |
| A1-G01-UTM-C03 | WHAT: find-or-create from free text trims the name, matches it case-insensitively (including archived records) and otherwise creates a new record. Campaigns created this way are flagged as auto-generated. RISK: an archived tracker is silently reused instead of blocking new use. | `models/utm_mixin.py` @ 0c8be65a [SC] | HIGH |
| A1-G01-UTM-C04 | WHAT: in the free-text find-or-create helper, when the name is blank after trimming, the lookup result variable is never assigned before it is tested. Statically this is an unassigned-variable failure path, not a clean validation error. The cookie-default caller filters empty strings but not whitespace-only values. RISK: an unhandled error on record creation (runtime reachability unproven). | `models/utm_mixin.py` @ 0c8be65a [SC] | MED (static-confirmed; reachability LOW) |
| A1-G01-UTM-C05 | WHAT: the public find-or-create wrapper accepts a model name. For tracker models it uses find-or-create. For any other model it performs a plain create with the given name and relies on standard ACLs. RISK: a generic creation entry point whose safety rests entirely on the ACLs of the target model. | `models/utm_mixin.py` @ 0c8be65a [SC] | HIGH |
| A1-G01-UTM-C06 | WHAT: after each HTTP request, the `utm_campaign`, `utm_source` and `utm_medium` URL parameters are written to optional cookies scoped to the request host. The cookies last 31 days and are refreshed only when the value changes. The lifetime is fixed in code. | `models/ir_http.py` @ 8a6e6e4f [SC] | HIGH |
| A1-G01-UTM-C07 | WHAT: when any record that inherits the tracking mixin is created, the defaults read those cookies and resolve free text through find-or-create. WHY: automatic attribution. RISK: an external visitor-supplied URL value can cause new tracker records to be created in the tenant, with no normalisation beyond trimming and no length limit visible in this module. | `models/utm_mixin.py` @ 0c8be65a [SC]; `models/ir_http.py` @ 8a6e6e4f [SC] | HIGH |
| A1-G01-UTM-C08 | WHAT: the cookie defaults are skipped for members of the `sales_team` salesman group unless the code runs as superuser, but `sales_team` is not a declared dependency (only `base` and `web` are). RISK: an undeclared cross-module coupling. Behaviour when that group does not exist is not proven here (G6). | `models/utm_mixin.py` @ 0c8be65a [SC]; `__manifest__.py` @ 94c25dc9 [SC] | HIGH (presence); LOW (effect) |
| A1-G01-UTM-C09 | WHAT: six seeded mediums (Email, Direct, Website, X, Facebook, LinkedIn) cannot be deleted (user error). The seeded Referral source cannot be deleted (validation error). Both guards are skipped during uninstall. | `models/utm_medium.py` @ 539b4dc7 [SC]; `models/utm_source.py` @ 636587e9 [SC] | HIGH |
| A1-G01-UTM-C10 | WHAT: ten mediums are seeded. Four of them (Phone, Banner, Television, Google Adwords) have no deletion guard. RISK: protection of seeded vocabulary is not uniform, and the intent is unknown. | `data/utm_medium_data.xml` @ d719225f [SC]; `models/utm_medium.py` @ 539b4dc7 [SC] | HIGH |
| A1-G01-UTM-C11 | WHAT: medium fetch-or-create by normalised key creates the medium and its external id with elevated rights when the key is missing. WHY: downstream modules can register required mediums. RISK: this is creation that bypasses ACL for the medium vocabulary. | `models/utm_medium.py` @ 539b4dc7 [SC] | HIGH |
| A1-G01-UTM-C12 | WHAT: the ACL gives internal users read, write and create on campaigns, mediums and sources (no delete), and read-only access to stages and tags. Settings administrators have full rights. There are no groups and no record rules. | `security/ir.model.access.csv` @ 3f7f7241 [SC] | HIGH |
| A1-G01-UTM-C13 | WHAT: no tracker model has a company field, so trackers are a single vocabulary shared across all companies. RISK: labels leak across companies and cannot be separated per company. | `models/utm_campaign.py` @ a9b07365; `models/utm_medium.py` @ 539b4dc7 [SC]; `models/utm_source.py` @ 636587e9 [SC] | MED-HIGH |
| A1-G01-UTM-C14 | WHAT: the campaign lifecycle is stage-only, with no status guards. A default stage ships as mandatory data. Deleting a stage that is in use is restricted, and the kanban reads all stages with elevated rights. | `models/utm_campaign.py` @ a9b07365; `data/utm_stage_data.xml` @ 87e7e7c0 | MED |
| A1-G01-UTM-C15 | WHAT: content records that own a source get an auto-generated source name (flattened, truncated, with the model description and date appended). A multi-record rename is refused, and duplication yields an incremented counter name. The source cannot be deleted while it is in use. | `models/utm_source.py` @ 636587e9 [SC] | MED |
| A1-G01-UTM-C16 | WHAT: the tracker menus are visible only in debug mode, and there are no HTTP routes, controllers, wizards or crons. | `views/utm_menus.xml` @ 7743723c; `__manifest__.py` @ 94c25dc9 [SC] | MED |

## 2. Business rules
- BR1: Tracker names are unique case-insensitively. A collision produces a suffixed variant rather than a rejection (C01, C02).
- BR2: Free-text attribution resolves to an existing tracker, archived ones included, or creates a new one (C03).
- BR3: Attribution context comes from URL parameters, persists for 31 days in host-scoped cookies and is applied when attributable records are created (C06, C07).
- BR4: Salespeople do not receive cookie-based attribution defaults unless the code runs as superuser (C08).
- BR5: Core seeded mediums and the Referral source cannot be deleted outside uninstall (C09).
- BR6: Every content record owns exactly one source, and that source cannot be deleted while it is in use (C15).

## 3. States / transitions
- Tracker: absent → created (manual, find-or-create, cookie default or keyed fetch-or-create). Medium: active ↔ archived. Source: no archive state. Deletion is blocked for protected or in-use records.
- Campaign: moves between user-defined stages freely, starting from the default stage. There are no guarded transitions.
- Attribution cookie: absent → set or replaced (a URL parameter differs) → expires after 31 days.

## 4. Exceptions / failure modes
- Deleting a protected medium raises a user error, and deleting the Referral source raises a validation error (C09).
- A multi-record source rename is refused (C15). Deleting an in-use stage or source is restricted by the relation (C14, C15).
- A name that is blank after trimming leads to an unassigned-variable failure path (C04), which is not a designed validation error.
- Database-level uniqueness violations are pre-empted by suffixing (C01). A concurrent-creation race is not addressed in this module (G7).

## 5. Cross-module handoffs
- `base` / `web`: ACL groups, campaign owner (a user) and the HTTP post-dispatch hook.
- `sales_team` (undeclared): the salesman group check in the defaults (C08).
- Downstream: any module that inherits the attribution mixin or the content-source mixin, or that registers mediums through the keyed fetch-or-create path. The cookie-domain hook and the tracking-field list are extension points.
- Frontend link tooling (a website links module) uses the public wrapper, according to its docstring. This is not verified (Lane A X4).

## 6. Evidence gaps (carried from Lane A, plus A1 additions)
- G1 (Lane A): runtime reachability of the blank-name path. The path is now statically confirmed (C04); runtime is still unknown.
- G2 (Lane A): whether leaving four seeded mediums unguarded is intentional (C10).
- G3 (Lane A): demo file contents and JS assets were not analysed.
- G4 (Lane A): downstream mixin consumers were not enumerated.
- G5 (A1): the effect of a campaign title or identifier rename on historical attribution reporting.
- G6 (A1): how the defaults behave when the `sales_team` group reference is absent.
- G7 (A1): concurrent find-or-create of the same name (duplicate or suffix race).
- G8 (A1): consent handling for the optional cookies is outside this module and unverified.

## 7. CRQ candidates
- CRQ-UTM-01: Should a colliding tracker name be rejected, or offered as a merge, instead of being suffixed silently? (C01)
- CRQ-UTM-02: Should attribution vocabulary be scoped per tenant or company? (C13)
- CRQ-UTM-03: Should externally supplied tracking values be validated, length-bounded and rate-limited before they create tracker records? (C07)
- CRQ-UTM-04: Should blank or whitespace-only tracking input fail with a defined validation outcome? (C04)
- CRQ-UTM-05: Should the protected-vocabulary policy be explicit and uniform across seeded values? (C09, C10)
- CRQ-UTM-06: Should the attribution-context lifetime and consent be configurable policy instead of fixed in code? (C06)
- CRQ-UTM-07: Should role-based attribution exclusions depend only on declared dependencies? (C08)
- CRQ-UTM-08: Should a generic "create by name" entry point be restricted to tracker vocabularies? (C05)
- CRQ-UTM-09: Should archived trackers be blocked from reuse through free-text matching? (C03)

## 8. Contradictions
- None were found between Lane A and the source. Every spot-checked claim matched.
- Lane A G1 (blank-name path) is CONFIRMED-FROM-SOURCE at the static level (C04). Runtime reachability remains CANDIDATE.
- CANDIDATE tension with the GMVQ lens topics "archiving prevents new use" versus C03 (archived records are matched and reused), and "tracking data scoped per company" versus C13.

## 9. Provenance
- Input: Lane A PASS-1 packet (sha256 above), 23 blobs at the anchor commit.
- Spot-check source: `https://raw.githubusercontent.com/odoo/odoo/8d05257d83f9128953f580a066db67c48fcdb96f/addons/utm/<path>`, fetched on 2026-09-27 into the session scratchpad and not committed.
- The GMVQ bank was used only as a topic lens. No QID is answered and the bank was not edited.

## 10. Spot-check log (7 files; `git hash-object` vs the Lane A blob)

| # | File | Recorded blob | Recomputed | Claim content checked | Result |
|---|---|---|---|---|---|
| 1 | `models/utm_mixin.py` | 0c8be65a139fda06c873cec9d491090fdf33c655 | identical | suffix generator with skip-ids; case-insensitive match including archived; blank-name unassigned path; salesman skip; public wrapper creates in any model | MATCH |
| 2 | `models/utm_medium.py` | 539b4dc75565ce2e15a6df3c69ba8de42ed176ba | identical | 6 protected mediums, user error, skipped at uninstall; elevated keyed create | MATCH |
| 3 | `models/utm_source.py` | 636587e93760986da6b5db071174c16956c7ee6a | identical | Referral guard (validation error), skipped at uninstall; required restricted source on content | MATCH |
| 4 | `models/ir_http.py` | 8a6e6e4f25c7eea231b5d62284038c200d6b013e | identical | 3 params into optional cookies, 31-day max-age, host domain hook | MATCH |
| 5 | `security/ir.model.access.csv` | 3f7f7241d5ff8085f40f32850124c0b83035d89f | identical | 10 rows: internal users with no delete, read-only stage/tag; admin full | MATCH |
| 6 | `__manifest__.py` | 94c25dc98ad015df4c6d9278e415a4fe5fdc31a7 | identical | depends on only `base` and `web` (no `sales_team`) | MATCH |
| 7 | `data/utm_medium_data.xml` | d719225fe7ca2e8ec444da96f2621b8beea9a60a | identical | 10 seeded mediums; Phone/Banner/Television/Google Adwords unguarded | MATCH |

## 11. Limitations
- SOURCE-STATIC only. Source presence does not prove runtime reachability, and statements of absence cover only this module's files.
- There is no Formal Coverage claim and no percentages. A2 verification, Lane B corroboration and Proof are still pending.
- Claims that were not spot-checked (C14, C16 in part) rely on Lane A blob pointers.
