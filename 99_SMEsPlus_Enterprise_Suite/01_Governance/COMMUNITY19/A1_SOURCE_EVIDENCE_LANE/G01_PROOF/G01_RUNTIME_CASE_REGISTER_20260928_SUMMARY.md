# G01 RUNTIME Case Register — Summary (2026-09-28)

Companion summary to `G01_RUNTIME_CASE_REGISTER_20260928.tsv`. This is a **register-reconciliation artifact only** (Step R1). No case was executed by this pass. Only RUNTIME-layer cases are counted; SOURCE/CONFIG-layer cases (already fully executed and A3-reviewed per the static VDR pipeline) are out of scope here.

## 0. Method and lineage note

The register was built by reading, in full, every sealed Proof file and addendum/delta variant under `G01_PROOF/` (36 files), every `*_RUNTIME_EXECUTED_20260927.md` companion (32 files, per MD-13), and the 2 `*_RUNTIME_EXECUTED_SUBSTITUTE_*_20260928.md` pilot records (per MD-15/MD-16). Every distinct predeclared RUNTIME case_id found in any sealed file's own runtime-cases table is a row, including case_ids that a later addendum superseded — those are kept as separate `SUPERSEDED` rows (not deleted), and their replacement case_id is a separate row of its own, per the MASTER Decision Log's "superseded, not deleted" rule (MD-01, MD-03, MD-10, etc.).

## 1. Total case count

**TOTAL_CASES = 323**, not exactly MASTER_DECISION_LOG's stated 313 (MD-13). Reconciliation of the difference:

- Summing the "Runtime totals: N cases" line stated explicitly inside each of the 32 sealed files that has a `*_RUNTIME_EXECUTED_20260927.md` companion gives **322**, not 313 — this is an internally reproducible, auditable count (every file's own declared total was re-added by hand and cross-checked twice against a full per-case enumeration; the two methods agree exactly at 322). This 322 legitimately includes every superseded original case_id as its own row alongside its replacement (e.g. `PC-BAUT-12` and `PC-BAUT-12R1` are both counted; `PC-BAUT-64` → `PC-BAUT-64R1` → `PC-BAUT-64R2` are all three counted) — MD-13's 313 figure appears to undercount by not fully reconciling every addendum's lineage additions (base_automation alone carries 3 nested supersessions across 2 addenda authored on the same day before the runtime attempt).
- **+1 additional case**, `PR-PHON-12` (module `phone_validation`), predeclared in `G01_R2D_PROOF_ADDENDUM_20260927.md` (§5). This file has **no** `*_RUNTIME_EXECUTED_20260927.md` companion at all — it was not covered by the 32-file runtime-attempt pass that produced MD-13, even though it predates that pass's timestamp (R2D predeclared 16:33Z; the runtime attempt ran from 18:21Z). This is flagged in the register as a coverage gap for the next execution cycle, not as this pass's error.
- Total: 322 + 1 = **323**.

No case's own class or execution status was fabricated or guessed beyond what its own sealed text states; the one exception (`PC-UTM-17`) is explicitly marked `UNKNOWN`/unsatisfiable-as-written per the sealed file's own text (its own precondition — an archive/active flag on `utm.source` — does not exist in the model at all), not treated as a silent failure.

## 2. Execution-state breakdown

| execution_state | Count | Notes |
|---|---|---|
| NOT_EXECUTED | 292 | All carry `result = BLOCKED` (runtime device unreachable; no substitute-environment pilot has touched them) |
| SUPERSEDED | 29 | Original case_id superseded by a later addendum's replacement case_id; kept in history, not double-counted as open work; `retest_required = NO` (retest targets the replacement id instead) |
| EXECUTED | 2 | The 2 substitute-environment pilot cases (see §3) |

## 3. Result breakdown (of the 2 EXECUTED cases; all NOT_EXECUTED carry BLOCKED)

| Result | Count | Case(s) |
|---|---|---|
| PASS | 1 | `PC-HBLD-02` (html_builder) — substitute-env (iTest19C) pilot, non-access-control case, PASS per MD-15 disclosure rules |
| INCONCLUSIVE | 1 | `PC-BASE-02` (base) — substitute-env pilot; RPC-only methodology insufficient for this access-control (ir.rule) case per MD-16; the substitute file's record supersedes the original companion file's BLOCKED row for this case_id, which is retained in history per the task's supersession rule |
| BLOCKED | 292 | All remaining NOT_EXECUTED cases |
| FAIL | 0 | — |

- **EXECUTED_PASS = 1, EXECUTED_FAIL = 0, EXECUTED_INCONCLUSIVE = 1, BLOCKED (not-yet-executed) = 292.**

## 4. Classification by precondition class

| Class | Count | Meaning |
|---|---|---|
| CLASS_A_RPC | 121 | Plain data/CRUD/computed-field/config-read/cron-with-manageable-clock checks — executable via authenticated RPC; superuser is fine |
| CLASS_B_SESSION | 110 | Tests ir.rule / ACL / company isolation / portal-vs-internal / role visibility / delegated authorization — superuser RPC is invalid evidence (MD-16); needs a real non-superuser user with correct group/company/ACL setup |
| CLASS_C_DISPOSABLE | 91 | Needs destructive/reversible state control, exact source-commit match, controlled clock, a real mail-capture sink, multi-worker/multi-DB concurrency, a sandboxed capture listener/stub, or a browser/cross-site test |
| CLASS_UNKNOWN | 1 | `PC-UTM-17` — its own sealed text states the precondition (archiving a `utm.source`) cannot be met because that model has no archive/active field at all; cannot be classified against any of A/B/C as written |

**121 + 110 + 91 + 1 = 323.** Note: several cases carry precondition language that touches more than one class (e.g. `PC-BASE-01` needs both an ir.rule/company check *and* 2 HTTP workers). Where a case's own text names an infra-level hard precondition (multi-worker, clock, mail sink, sandbox listener) on top of an access-control test, it was classed CLASS_C, since that is the harder blocking requirement for execution planning; this is noted in the `notes` column of the affected rows.

## 5. Per-module case count (all 23 G01 modules)

| Module | Total | CLASS_A | CLASS_B | CLASS_C | UNKNOWN |
|---|---|---|---|---|---|
| auth_signup | 15 | 8 | 2 | 5 | 0 |
| base | 21 | 1 | 12 | 8 | 0 |
| base_automation | 37 | 20 | 7 | 10 | 0 |
| base_setup | 13 | 5 | 7 | 1 | 0 |
| base_sparse_field | 10 | 6 | 1 | 3 | 0 |
| bus | 16 | 4 | 4 | 8 | 0 |
| digest | 14 | 1 | 8 | 5 | 0 |
| google_recaptcha | 15 | 7 | 1 | 7 | 0 |
| html_builder | 2 | 2 | 0 | 0 | 0 |
| html_editor | 12 | 1 | 3 | 8 | 0 |
| http_routing | 11 | 11 | 0 | 0 | 0 |
| mail | 30 | 2 | 21 | 7 | 0 |
| onboarding | 9 | 5 | 3 | 1 | 0 |
| phone_validation | 12 | 8 | 4 | 0 | 0 |
| portal | 11 | 1 | 10 | 0 | 0 |
| privacy_lookup | 10 | 6 | 1 | 3 | 0 |
| resource | 23 | 10 | 8 | 5 | 0 |
| resource_mail | 4 | 1 | 2 | 1 | 0 |
| utm | 14 | 10 | 3 | 0 | 1 |
| web | 18 | 4 | 6 | 8 | 0 |
| web_hierarchy | 7 | 3 | 3 | 1 | 0 |
| web_tour | 4 | 2 | 1 | 1 | 0 |
| web_unsplash | 15 | 3 | 3 | 9 | 0 |
| **TOTAL** | **323** | **121** | **110** | **91** | **1** |

All 23 G01_PLATFORM_BASE modules are represented; none silently dropped to zero.

## 6. What this register is, and is not

- This is **register-building only**. No case in this file was executed, re-executed, or given a new result by this pass.
- No sealed Proof file, no existing `*_RUNTIME_EXECUTED_20260927.md` companion, and no `*_SUBSTITUTE_*` file was modified. Only these two new files were created:
  - `G01_RUNTIME_CASE_REGISTER_20260928.tsv`
  - `G01_RUNTIME_CASE_REGISTER_20260928_SUMMARY.md` (this file)
- The register is the intended input to the **next** execution stage (per MD-15/MD-16): CLASS_A cases are the best near-term candidates for RPC-based substitute-environment execution; CLASS_B cases require full ACL/group/rule provisioning of named non-superuser test users (or UI-driven execution) before they can produce a real PASS/FAIL rather than a superuser-invalid PASS; CLASS_C cases require a disposable/purpose-built environment, controllable clock, mail-capture sink, sandbox listener/stub, multi-worker/multi-DB setup, or reverse-proxy/browser testing beyond plain RPC.
- `PC-UTM-17` (CLASS_UNKNOWN) cannot be executed as written under any environment and should be formally retired in favour of its already-predeclared amended variant `PC-UTM-17a` in the next execution-planning pass, rather than re-attempted.
- `PR-PHON-12` (phone_validation, from `G01_R2D_PROOF_ADDENDUM_20260927.md`) was never covered by the 32-file runtime-attempt pass and should be picked up explicitly in the next runtime cycle.
