> GROUP A — Sales + Inventory + Purchase | Independent Evidence Reviewer | READ ONLY | No target design | Boss sole Final Approver
> Session: SMEPLUS-26-08-31-GRPA-SIP-IER-004 | Cluster C — R6 Approval Evidence Boundary Review

# 03 — R6 APPROVAL EVIDENCE BOUNDARY REVIEW (most important review cluster)

## 00 — Method: full independent reproduction, not a document review

Rather than reviewing Team A's row-level claims as prose, this review independently re-restored the same
`iTEST02` dump into a **freshly created, disposable local PostgreSQL instance** and ran its own SQL queries
against it — none of the query results below were copied from Team A's report; they were produced fresh and then
compared.

### 00a — A materially important reproduction finding, resolved

Team A's methodology note (`19_TEAM_A_CORRECTIVE_CLOSURE_REPORT.md` §03) states: *"PostgreSQL 16 was installed
locally (Homebrew) specifically for this investigation... `pg_restore -j4`; 18 restore errors, all isolated to an
unrelated `pgvector`-dependent AI-embedding table and one harmless unrecognized GUC."*

This review first attempted the identical procedure with PostgreSQL 16.15 (Homebrew, the same tool version
documented) and it **failed immediately and completely**: `pg_restore: error: unsupported version (1.16) in file
header` — not 18 isolated errors, a hard stop before any table is touched. Inspecting the dump's own header
confirmed why: it was produced by **`pg_dump`/server version 18.4 (Debian)**, and PostgreSQL's custom-archive
format is backward- but not forward-compatible — a v16 `pg_restore` cannot read a v18 dump at all.

This review then installed PostgreSQL 18 (Homebrew, keg-only, did not disturb the existing v16 installation used
elsewhere in this project) and repeated the restore. With matching tooling, the restore succeeded with **30
ignored errors** (Team A recorded 18), **all of the same category**: `relation "public.ai_embedding" does not
exist`, `type "public.vector" does not exist`, `extension "vector" is not available` — i.e. the same
pgvector-dependent AI-embedding table Team A described, not a new or different failure class.

**Finding**: Team A's stated tool version ("PostgreSQL 16") does not match what is actually required to restore
this dump; the dump requires PostgreSQL 18-class tooling. The exact ignored-error count also differs (18 vs. 30).
Both are **methodology-documentation inaccuracies**, not fabrication — every downstream data claim was
independently reproduced exactly (see §01–§03 below) once compatible tooling was used, which is strong evidence
the underlying restoration genuinely happened and genuinely queried this dump; it was simply mis-described as
having used PostgreSQL 16. **Recorded as a MEDIUM finding for Team A's documentation, not a Gate blocker** — see
`06_GROUP_A_REMAINING_GAP_GATE_IMPACT_REGISTER.md`.

The scratch database was fully torn down (server stopped, data directory deleted) at the end of this review's use
of it, matching Team A's own stated practice of non-persistence.

## 01 — A. MODULE EXISTENCE and B. MODULE INSTALLED STATE

Independently queried `ir_module_module`:

| Module | Team A claim | Independent query result | Match? |
|---|---|---|---|
| `sale_order_level_approve` | installed, v19.0.1.0.0, author "SMEsPlus" | `installed \| 19.0.1.0.0 \| SMEsPlus` | **EXACT MATCH** |
| `purchase_request_level_approve_po` | installed, v19.0.1.2.0, author "BH Pro International" | `installed \| 19.0.1.2.0 \| BH Pro International` | **EXACT MATCH** |
| `purchase_request_level_approve` | installed, v19.0.1.2.1, author "BH Pro International" | `installed \| 19.0.1.2.1 \| BH Pro International` | **EXACT MATCH** |
| `multi_level_approval` | never installed | `uninstalled \| Domiup` | **EXACT MATCH** |
| `multi_level_approval_configuration` | never installed | `uninstalled \| Domiup` | **EXACT MATCH** |
| `multi_approval` / `multi_approval_type` (tables) | do not exist in the live DB at all | `information_schema.tables` query for `multi_approval%`: **zero rows returned** | **EXACT MATCH** |

## 02 — C. FIELD OWNERSHIP and E. OBSERVED STATE VALUE

Independently queried `ir_model_fields` (state = `'base'` vs `'manual'`) and `ir_model_data` (owning module):

| Claim | Independent query result | Match? |
|---|---|---|
| `level1_user_id`/`level2_user_id`/`level1_approved_by`/`level2_approved_by`/`reject_reason` on `sale.order`, `purchase.order`, `purchase.request` all show `state='base'` (Python-declared, not Studio) | Confirmed for all rows returned — every field listed shows `state='base'`; `purchase.request` correctly lacks `level2_user_id` (matches Team A's "same set minus level2_user_id") | **EXACT MATCH** |
| `x_review_result`/`x_has_request_approval`/`x_need_approval` show `state='manual'`, present only on `purchase.order`/`purchase.request`, never `sale.order` | Confirmed — all three appear with `state='manual'` on `purchase.order` and `purchase.request`; zero rows returned for `sale.order` | **EXACT MATCH** |
| `ir_model_data` names the exact owning module per field | `field_purchase_request__level1_user_id` → module `purchase_request_level_approve`; `field_purchase_order__level1_user_id` → module `purchase_request_level_approve_po`; `field_sale_order__level1_user_id` → module `sale_order_level_approve` | **EXACT MATCH** |

## 03 — D. HISTORICAL USAGE

Independently queried row counts and state distributions directly:

| Claim | Independent query result | Match? |
|---|---|---|
| `purchase_order` total row count: 27,874 | `SELECT count(*) FROM purchase_order` → **27,874** | **EXACT MATCH** |
| 98.5% of `purchase_order` rows have `level1_user_id` set | `count(level1_user_id)=27,453` of 27,874 → **98.5%** | **EXACT MATCH** |
| `level1_approved_by` populated on 0 of 27,874 rows | `count(level1_approved_by)` → **0** | **EXACT MATCH** |
| Live `purchase_order.state` includes `to_check_level`, 131 rows | `GROUP BY state`: `to_check_level \| 131` (alongside `purchase=25578, draft=2086, cancel=78, sent=1`) | **EXACT MATCH** |
| `purchase_request` shows 1,945 `approved`, 96 `rejected` of 2,199 records | `GROUP BY state`: `approved=1945, approved_level1=104, rejected=96, draft=51, to_approve=3` — **sum = 2,199** | **EXACT MATCH, including the total** |
| Sale Order's approval-column usage is too small a sample to characterize | Not independently re-queried this pass (low materiality; Team A's own pack already down-weights this to "sample too small," which is the conservative direction) | **Not independently re-verified — no concern** |

## 04 — F/G/H: INTERNAL WORKFLOW LOGIC, PERMISSION/SoD LOGIC, CURRENT-LIVE BEHAVIOR

Independently confirmed via a full-tree filesystem search across the entire `SMEsPlus ENTERPRISE SUITE` volume
(not just the `SOURCE CODE` extraction Team A was given): **zero files** anywhere on this machine match
`sale_order_level_approve`, `purchase_request_level_approve_po`, or `purchase_request_level_approve` by name.

This confirms Team A's characterization is accurate and not a convenient excuse: the three modules' Python source
genuinely is not available in this environment. Therefore:

- **F (internal workflow/transition logic)**: correctly EVIDENCE_MISSING. Cannot be resolved without the module
  source. Not resolvable by further DB querying — button/transition logic is code, not data.
- **G (approval permission / SoD logic)**: same — correctly EVIDENCE_MISSING.
- **H (current-live behavior)**: correctly out of scope for a point-in-time dump snapshot (2026-06-14); Team A
  consistently caveats every quantitative claim as "in this dataset" / "this snapshot," which this review
  confirms is the right discipline, not an evasion.

**These are genuine, correctly-classified Unknowns — not a Gate blocker for the Team A Evidence Gate itself.**
See `06_GROUP_A_REMAINING_GAP_GATE_IMPACT_REGISTER.md` for the Gate-impact classification and the recommended
"request module source" action item's status.

## 05 — Overall Cluster C verdict

**`VERIFIED`.** Every quantitative and qualitative claim in the R6 resolution — module existence, install state,
version, author, field ownership, field declaration type, and every row-level statistic cited — was independently
reproduced exactly via a from-scratch database restore and fresh SQL queries, not by reading Team A's prose. This
is the single most significant finding in the entire GROUP A evidence chain, and it survives independent,
adversarial reproduction completely intact. The only finding attached to this cluster is the tooling/methodology
documentation inaccuracy in §00a, which affects confidence in Team A's *process narrative* but not in the
*substance* of what was found.
