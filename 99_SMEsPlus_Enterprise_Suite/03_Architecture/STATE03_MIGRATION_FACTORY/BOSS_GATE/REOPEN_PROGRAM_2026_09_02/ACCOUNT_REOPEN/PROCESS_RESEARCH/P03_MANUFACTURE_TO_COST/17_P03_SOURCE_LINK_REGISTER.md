# 17 — P03 SOURCE LINK REGISTER

**LAYER 2 — AUDIT QUARANTINE.** Citations in this file must not be transcribed into any
Layer 1 or reference package.

---

## 1. Declared source root

| Field | Value |
|---|---|
| **Primary source root** | `/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo/addons/` |
| Generation | v18 Enterprise, build 20250608 — the target-generation tree |
| Module count | 797 |
| Selection reason | `smeplus-primary-source-evidence-locations` designates this as the target-generation Enterprise source. The 2026-09-03 Asset session's error — searching only the session working tree and concluding no code access existed — is explicitly not repeated |
| **Not used** | The v14 legacy tree, the v19 trees, and the several near-identical custom addon copies. Which copy is deployed is unknown and is `DEP-04` |

**Every negative claim in this package is bounded by this root.** No claim is made about
the running system's configuration.

## 2. Cited artefacts, with SHA-256

Format: `SHA-256  path relative to the source root`.

```
e8fa1b9cdb3d722b6c8a4270da5f271b913d66cbd21d0611c2366d0a5900d23a  mrp/models/mrp_production.py
549f6d4ac785da73438ea7f8a5285cd3594b25bca9e54891de0e0142b2e5466e  mrp/models/mrp_workorder.py
a958c4109d17bc6b778a82c37230aa59daa7c82f7aeafacbb6424f3626030bc7  mrp/models/mrp_workcenter.py
3a760c5f84084d38cd0704497e76c546c4e49673b4a408fde204be1eb3d164cf  mrp/models/mrp_bom.py
8d0bbb1a40a2f8484e8521e285b95a994e4acf95bc965f57781e7fe9c6922c53  mrp/models/mrp_unbuild.py
fb41531d0e7cbe70d1a5c1896f8221a33260b13079985ebb72ba767914a3c7a4  mrp/models/stock_scrap.py
1de171c469e8b86810178bcce48a132f793324dc6ff57a043014adfd4c4e8a92  mrp_account/models/mrp_production.py
0e2b28803f671665cb5e04d86496c6f43d520970163763906fa063ff32d1148b  mrp_account/models/mrp_workorder.py
9898ae78c1ea671b274fd312a274c48914b65cc5dd96d209a9a8cd7e81d7fc2e  mrp_account/models/mrp_routing.py
ab415775b15a085181bc3b2ecaa7f6719e7c49ddde4b9c594d16955faabfde7b  mrp_account/models/product.py
fc742019fc564572dbf138ce4c5795888e2b20dd4bf01e55d00a9ecb707ff147  mrp_account/models/stock_move.py
8d432714d438a449a038911de114de6d1a19b15586f81814d2c1124e20f8938a  mrp_account/wizard/mrp_wip_accounting.py
c92058f3fa4934236e311671ff4effa5dc8dae13c191d0d579e123173b4f78b0  mrp_workorder/models/mrp_workorder.py
290834bae96fa77fc05c367d645017bcd8d5dba0258c80bb6624f7ec761b156e  mrp_workorder/models/mrp_workcenter.py
e132d2c7bdda0f4868897e1b91f96246ebadf65db3ed3e50ae5eeeb2280a7c83  mrp_workorder_hr_account/models/mrp_routing.py
4608442d0c69ec824472ed52bc7d1c352ccc44654606d28b70bf378e20f0b391  mrp_workorder_hr_account/models/mrp_workorder.py
df3873481ea3b1e69cf1cc7f4da5f25fa1f74bea5dec2f65c7f2e04a274c746e  mrp_workorder_hr_account/report/mrp_cost_structure.py
45fd4b02ee6ed67bf1e104361ca00a8d8e4b6b4d251d7553555995eea3a28b94  mrp_subcontracting_account/models/stock_move.py
a584dfc6600c952c71a264c45447bfe54b4c964f1ae5543068eb065505b68f7a  mrp_subcontracting_account/models/mrp_production.py
252b1fcfd6d073f35448d695ee65fc64ceac1997495d7890576a23c783e97e5a  project_mrp_workorder_account/models/mrp_workcenter_productivity.py
b31b1141f49d55f469c962c626b1dcf78fb07fabf3aaeb7117755438fb21cc55  stock_account/models/res_company.py
```

## 3. Function-level citation index

| Finding | Citation |
|---|---|
| `DC-01` | `mrp/models/mrp_workorder.py:576-588 — MrpWorkorder._cal_cost`; `mrp/models/mrp_workorder.py:321-329 — _compute_duration`; `mrp_workorder/models/mrp_workorder.py:757-767 — _compute_duration`, `:811 — _intervals_duration`, `:828-836 — get_duration` |
| `DC-02` | `mrp_workorder/models/mrp_workcenter.py:61-73 — MrpWorkcenterProductivity._compute_employee_cost/_compute_total_cost`; `mrp_workorder/models/mrp_workorder.py:854-858 — _cal_cost` |
| `DC-03` | `mrp_account/models/mrp_production.py:13, 53-54, 69, 82-84`; `mrp_subcontracting_account/models/stock_move.py:31` |
| `DC-04` | `mrp_account/models/mrp_production.py:63-64` vs `:74` |
| `DC-05` | `mrp_account/models/mrp_workorder.py:41-54 — _create_or_update_analytic_entry` |
| `DC-06` | `mrp/models/mrp_workorder.py:587, 906, 909-912`; `mrp_workorder_hr_account/report/mrp_cost_structure.py:61` |
| `DC-07` | `mrp_account/models/mrp_production.py:81, 90-91`; `mrp_account/models/mrp_workcenter.py:12-13` |
| `DC-08` | `mrp/models/mrp_production.py — _post_inventory`, the work-order duration loop |
| `DC-09` | `mrp_account/models/mrp_production.py:94` |
| `DC-10` | `mrp_workorder_hr_account/models/mrp_workorder.py:18, 25`; `project_mrp_workorder_account/models/mrp_workcenter_productivity.py:40` |
| `DC-11` | `mrp_account/models/mrp_production.py:74` vs `:77`; `mrp_account/models/product.py:124-128` |
| `DC-12` | `mrp_workorder_hr_account/report/mrp_cost_structure.py:43-44, 47` |
| `DC-13` | `mrp_account/models/stock_move.py:44-67 — _get_out_svl_vals` |
| WIP account families | `mrp_account/wizard/mrp_wip_accounting.py:70-107, 124-150`; `stock_account/models/res_company.py:8-9` |
| By-product constraints | `mrp/models/mrp_bom.py:199-202`; `mrp/models/mrp_production.py:872-874` |
| Scrap | `mrp/models/stock_scrap.py:10-15, 23-49, 83-90` |
| Unbuild known limitation | `mrp/models/mrp_unbuild.py:31` (source comment, verified in place) |
| Discarded hypothesis | `mrp_account/models/stock_move.py:23-24`; falsified at `stock_account/models/stock_move.py:573` |

## 4. Repository evidence — prior SMEsPlus lineage

| Reference | Branch |
|---|---|
| Asset DR Continuation `07`, `12`, `22` | `origin/research/asset-deep-continuation-2026-09-04-001` |
| Asset Deep L1–L6 | `origin/research/asset-deep-l1-l6-2026-09-04-001` |
| COGS targeted resolution | `origin/research/cogs-targeted-resolution-2026-09-03-001` |
| Inventory MTI rulings `D-01`/`D-02`/`D-03` | `origin/ruling/inventory-mti-d0{1,2,3}-…-2026-09-04-001` |
| Account Wave A GB-08 ruling | `origin/SMEsPlus` @ `8004a81` |
| Session base | `origin/SMEsPlus` @ `88f52cd` |

## 5. Governance evidence

| Document | Path |
|---|---|
| `PROJECT_CONSTITUTION.md` v1.4 | `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/` |
| Understand-Transfer-Preserve addendum | same directory, `…_2026_09_02_UNDERSTAND_TRANSFER_PRESERVE.md` |
| `SYSTEM_RESEARCH_MASTER_INDEX.md` | `…/STATE03_MIGRATION_FACTORY/TEAM_A/` |
| `END_TO_END_BUSINESS_PROCESS_MATRIX.md` | `99_SMEsPlus_Enterprise_Suite/` |

## 6. Not consulted

| Source | Why |
|---|---|
| Running UAT database | No access in this session. `DEP-04` |
| P01 and P02 peer outputs | Peers running concurrently; duplication and answer-key contamination both forbidden |
| Public vendor documentation | Primary source was available. Documentation was not used as a substitute for code, per the correction recorded in `smeplus-primary-source-evidence-locations` |


## 7. Runtime / database evidence — added round 3

**All read-only.** No database server was started. `pg_restore` streamed table data to
stdout; no restore into a live database was performed, and nothing was written anywhere.

| Database | File | Readable | Role |
|---|---|---|---|
| `iSMEs` | `~/Downloads/iSMEs_2026-07-11_05-03-27.dump` | Yes | **The only deployment where manufacturing has executed** |
| `BK12MAY26` | `~/Downloads/BK12MAY26_2026-08-03_05-48-30.dump` | Yes | 44 companies; manufacturing installed, unused |
| `iEVING` | `~/Downloads/iEVING_2026-07-23_10-31-06.dump` | Yes | manufacturing unused |
| `iTEST02` | `~/Downloads/iTEST02_2026-07-14_16-34-51.dump` | **No** — `pg_restore: unsupported version (1.16) in file header` | `UNR-P03-07` |

**Reproduction.** `evidence/P03T_db_rowcounts.py` regenerates the row-count table;
`evidence/P03T_EXECUTED_OUTPUT.txt` records every executed command and its output,
including the positive controls.

| Claim | Executed evidence |
|---|---|
| Installed-module lists | `ir_module_module` where `state='installed'` — 251 (`BK12MAY26`), 190 (`iSMEs`) |
| Conversion cost is zero | `mrp_workcenter`/`mrp_workorder`/`mrp_routing_workcenter`/`mrp_workcenter_productivity` = **0** in all three |
| `extra_cost` unused | 10,344 null + 420 zero + **0 non-zero** = 10,764 |
| Live mechanisms | `stock_move.cost_share` non-zero **8,176**; `stock_scrap` **2,286**; `mrp_unbuild` **987**; `stock_landed_cost` **0** |
| Positive controls | `account_asset` 36/685; `res_company` 44/1; `stock_move` 103,949; `account_move_line` 447,384 |
| Custom addons carry no cost override | 3 roots, 1,325 `.py` files, **378** matching the control pattern, **0** matching any cost identifier |

**Bound.** Every runtime claim is about **these three dump files**. None is a claim about a
running system, and `UNR-P03-10` records that no readable database is established as the
migration target.
