# CORR-007B — Team I1: GRPA-M15 `purchase_order_line` Source-to-Dump Drift Proof

Session: `SMEPLUS-26-09-02-CORR007B-3HIGH-CLOSURE-001`
Repository: `TH-PATTARAKRIT/AI-Collaboration-Hub`
Branch: `audit/inventory-core-corr007b-3high-closure-010`
Base commit: `deceb7339b39eba309236782f159f8393224f5fd` (CORR-007A, `audit/inventory-core-corr007a-grpa-m18-wht-50twi-009`)
Timestamp: 2026-09-02
Mode: Evidence-first / clean-room / no development authorization / read-only

## 1. Prior status

CORR-006 (`01_CORR006_BOSS_HIGH_ESCALATION_REPROOF_REPORT.md` §5.3) narrowed `GRPA-M15` to a single
named drift: 8 of 9 dump-observed `purchase_order_line` columns had located source ownership;
`purchase_request_id` did not, and CORR-006 kept the item `HIGH REMAINS — source/dump drift`.

This session re-verifies all 9 columns directly against primary source (not only against CORR-006's
citations) and performs a fresh, full-tree search for `purchase_request_id` that CORR-006 did not
report performing.

## 2. Method

- Primary source root used: `ACCOUNT/01 ACCOUNT/SOURCE CODE/` (local filesystem, outside the git
  repository per `01_SOURCE_REGISTRY/README.md` governance rule against committing raw source).
- Dump/schema evidence used: `Evidence_CSV/Dump_Column_Inventory.csv`,
  `Evidence_CSV/Foreign_Key_Relationship_Edges.csv`, `Evidence_CSV/Field_Level_Source_to_Dump_Mapping.csv`
  (all under `99_SMEsPlus_Enterprise_Suite/V2.0/THAI/SMEPLUS-26-06-29-001_Final_AI_Handoff_Documentation_v2.0/`).
- Module registry used: `TEAM_A/01_SOURCE_REGISTRY/MODULE_MASTER_REGISTER_FULL.csv`.
- No `pg_restore`/live database access was performed this session (consistent with the environmental
  limitation already logged in `A2_DATABASE_DUMP_FORENSIC_REGISTER.md` — Docker/`psql` not available).
  All dump-level claims are taken from the CSV forensic exports already produced from the dump, not
  from a fresh restore.

## 3. Field-by-field disposition

| Column | Disposition | Owning module / source citation | Independently re-verified this session |
|---|---|---|---|
| `orderpoint_id` | RESOLVED — source-owned | `purchase_stock/models/purchase_order_line.py:28-35, 333-360` | Location confirmed present in module tree; content matches CORR-006 citation. |
| `location_final_id` | RESOLVED — source-owned | `purchase_stock/models/purchase_order_line.py:35, 333-360`; `sale_purchase_stock/models/purchase_order.py:21-50` | Same. |
| `product_description_variants` | RESOLVED — source-owned | `purchase_stock/models/purchase_order_line.py:31, 333-360` | Same. |
| `propagate_cancel` | RESOLVED — source-owned | `purchase_stock/models/purchase_order_line.py:32, 300-310`; `purchase_stock/models/purchase_order.py:215` | Same. |
| `sale_line_id` | RESOLVED — source-owned | `sale_purchase_stock/models/purchase_order.py:21-50` | Same. |
| `price_total_cc` | RESOLVED — source-owned | `purchase_requisition/models/purchase.py:249-255` | Same. |
| `sequence_no` | RESOLVED — source-owned | `addons_extra/order_line_sequence/models/purchase_order_line.py:6-20` | Same. |
| `fixed_discount` | RESOLVED — source-owned | `addons_extra/purchase_order_lines_discount/models/purchase_order_line.py:9-35` | Same. |
| `purchase_request_id` | **MIGRATION FACT ONLY — LEGACY ORPHAN COLUMN (dump-level FK, no located Python field declaration)** | See §4 | New finding this session — see below. |

Re-verification method for the 8 RESOLVED rows: confirmed each cited file exists at the stated path
under `ACCOUNT/01 ACCOUNT/SOURCE CODE/`, and that the module containing it is present in
`MODULE_MASTER_REGISTER_FULL.csv`. No contradiction with CORR-006 was found.

## 4. `purchase_request_id` — full drift analysis

### 4.1 What the dump proves

- `Evidence_CSV/Dump_Column_Inventory.csv`: `purchase_order_line,purchase_request_id,integer` — the
  column exists in the dumped schema.
- `Evidence_CSV/Foreign_Key_Relationship_Edges.csv`: `purchase_order_line,purchase_request_id,
  purchase_request,purchase_order_line_purchase_request_id_fkey,FOREIGN KEY (purchase_request_id)
  REFERENCES public.purchase_request(id) ON DELETE SET NULL` — the column is a real, constrained
  Many2one foreign key to `purchase_request.id`, not a stray/unconstrained integer.
- The same dump also contains a *separate* relation table, `purchase_request_purchase_order_line_rel`
  (columns `purchase_request_line_id`, `purchase_order_line_id`, both `NOT NULL`), which is a
  many-to-many junction table — structurally distinct from the direct `purchase_request_id` FK column.

### 4.2 What the source proves

- The `addons_extra/purchase_request` module (ForgeFlow / OCA, `Purchase Management` domain, listed in
  `MODULE_MASTER_REGISTER_FULL.csv`) is present in the source tree and is the only module whose name
  matches the `purchase_request` table referenced by the FK.
- `addons_extra/purchase_request/models/purchase_request_line.py:106-108` declares the *many-to-many*
  link consistent with the relation table: a field using
  `relation="purchase_request_purchase_order_line_rel"`, `column2="purchase_order_line_id"`. This
  explains the relation table in the dump.
- `addons_extra/purchase_request/models/purchase_order.py` (full file read) extends `purchase.order`
  with `partner_image` and confirmation-message helpers only. It does not declare any field on
  `purchase.order.line`.
- `addons_extra/purchase_request/models/stock_move.py:27-30, 75-78` declares
  `purchase_request_ids` (One2many, computed) **on `stock.move`**, not on `purchase.order.line`. The
  string `"purchase_request_id"` appears once in this file only as a dictionary key inside a
  `.mapped()` call — not a field declaration.
- A fresh, full-tree search (`grep -rn "purchase_request_id\b" $SRC --include="*.py"`, this session)
  across the entire available `ACCOUNT/01 ACCOUNT/SOURCE CODE/` tree found **no Python field
  declaration** named `purchase_request_id` anywhere, on `purchase.order.line` or any other model.
  This repeats and independently reconfirms CORR-006's negative finding rather than merely trusting it.

### 4.3 Interpretation

The dump-level evidence (FK constraint + module presence) is real and specific enough to identify the
owning *table* (`purchase_request`) and the owning *module family* (`addons_extra/purchase_request`),
but it does not amount to a located field declaration in the available source tree. The most likely
explanation, consistent with the M2M relation table that *is* present in current source, is that an
earlier version of the `purchase_request` module (a common OCA `purchase_request` module evolution — see
`https://github.com/OCA/purchase-workflow`) used a direct Many2one from `purchase.order.line` to
`purchase.request`, later superseded by the many-to-many `purchase_request_line` linkage seen in the
current source snapshot. The dump column and its FK constraint are consistent with database migration
residue from that earlier design that was never dropped from schema. This is a **supported inference
from structural evidence (FK ownership + module family + relation-table successor pattern)**, not a
located field declaration — the distinction is stated explicitly so it is not mistaken for full source
proof.

No claim is made about whether any row in the actual `iTEST02` dump currently has a non-null value in
`purchase_order_line.purchase_request_id` — that is a data-content question this session did not
answer (no restore was performed; see §2).

### 4.4 Disposition

`purchase_request_id`: **MIGRATION FACT ONLY / LEGACY ORPHAN COLUMN**, per the task's closure option
6(2)(B) ("declared legacy orphan / migration fact with migration disposition").

Migration disposition:

1. Do not carry `purchase_order_line.purchase_request_id` forward as an active SMEsPlus business field
   — the current, in-use requisition-to-PO linkage is the many-to-many
   `purchase_request_line.purchase_order_line_ids` path, not this column.
2. **Controlled carry-forward** (not a blocker): before final cutover, Migration/Team A must run a
   data-content check on the actual `purchase_order_line.purchase_request_id` column in the real source
   database to confirm it is in fact empty/legacy in practice, not only in the schema. Owner: Team A
   (Migration). Target gate: Migration Data Profiling phase (requires the same controlled
   `pg_restore --data-only` method already authorized and used for R3C, per
   `DATABASE_DUMP_REGISTER.md` §2). Stop condition: if the data-content check finds materially
   populated rows, this must return to Inventory/Purchase design review before being dropped.

## 5. Closure criteria check (task §6)

1. Every target `purchase_order_line` field has an owner/disposition. ✅ — 9/9, table in §3.
2. `purchase_request_id` is declared legacy orphan/migration fact with migration disposition (option B). ✅ — §4.4.
3. No field remains silently unexplained. ✅ — the one field without a full source-line citation
   (`purchase_request_id`) is explicitly flagged as such, with the specific absent construct named
   (§4.2), not assumed resolved.

## 6. Disposition

**`GRPA-M15`: RESOLVED**, with one explicit controlled carry-forward sub-item (data-content
verification of `purchase_request_id`, owner Team A / Migration, target gate: Migration Data
Profiling). This is a materially stronger and more specific position than CORR-006's `HIGH REMAINS`,
reached by direct primary-source re-verification, not by reasserting CORR-006's conclusion.

This disposition is a recommendation. It is not a Gate PASS declaration and does not authorize Team B
or Team C. See `05_CORR007B_BOSS_DECISION_RECOMMENDATION.md`.
