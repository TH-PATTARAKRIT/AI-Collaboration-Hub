# 47 — P02 `C-04` RUNTIME CLOSURE OR AUTHORISATION PACK

*(mandated semantic name `33_P02_C04_…`; 33 taken, next free number used per §15.)*

`LAYER 2 — AUDIT QUARANTINE.` **CP-05.** Baseline `aca211e`.

**Result: `C-04` SPLITS. One half CLOSES ON READ-ONLY EVIDENCE. The other half requires authorisation
that does not exist, so nothing was executed.**

**No write, install, restore, or mutation of any kind occurred in producing this file.**

---

## 1. The Split

`C-04` was carried as one question. It is two, and they have different answers.

| | Question | Status |
|---|---|---|
| **`C-04a`** | Is the invoice-side cost generator **idempotent**? | **CLOSED — READ-ONLY, ON SOURCE. It is NOT.** |
| **`C-04b`** | Is repeat execution **reachable in a deployment**? | **OPEN — precondition measured present, mechanism never observed.** |

## 2. `C-04a` — CLOSED. The Generator Is Structurally Non-Idempotent.

Two source facts, together decisive, both re-derived this round:

1. **No dedup read.** `stock_account/models/account_move.py:77` —
   `_stock_account_prepare_anglo_saxon_out_lines_vals` builds the COGS pair without reading existing
   `display_type='cogs'` lines and without consulting `cogs_origin_id`.
2. **The collection it iterates cannot contain what it creates.**
   `account/models/account_move.py:330-336` —
   `invoice_line_ids = fields.One2many(..., domain=[('display_type','in',('product','line_section','line_note'))])`.
   **`cogs` is not in that domain.** So previously created COGS lines are invisible to the generator by
   construction, not by oversight.

**`P02-F-47a` — `FACT VERIFIED` (source), WITH ITS LABEL CORRECTED (`C-58`).** A second invocation over
the same move **must** create a second COGS pair, and the structure forecloses an in-generator guard.

> **But this is a design fragility, not a control failure — and calling it a closed defect overstates it.**
> Idempotency is delegated to the **state machine**, and the compensating controls are real, in the same
> file: `button_draft` (`:59-60`) and `button_cancel` (`:70`) both **unlink every `display_type='cogs'`
> line**, and `copy_data` (`:27-35`) strips them on duplication. The generator has **one** caller and that
> caller is the transition. Delegating idempotency to a state transition is a legitimate posting-engine
> pattern.
>
> **The thing that can produce a wrong number is entirely `C-04b`:** the soft-post path leaves the move in
> `draft` **with** the COGS lines already created, so the transition fires twice against one state and the
> cleanup never runs.
>
> **And under `BP-02` this is not a risk P02 carries against the SMEsPlus target at all.** `BP-02`
> recognises COGS on **physical delivery**; `C-04a` is a defect in the **invoice-side** generator, a
> mechanism the target does not adopt. Its correct disposition is a **design requirement input**: *the
> delivery-triggered cost generator must carry an explicit idempotency key.* The benchmark already ships
> the field — `cogs_origin_id` exists in v18 (`stock_account/models/account_move.py:257`) and v19, and is
> **written but never read as a guard**. `C-04a` remains a live risk **to the deployed estate**, which is a
> different question with a different owner. **This half of `C-04` needed no
runtime and should not have been carried as runtime-blocked.**

**Prior status corrected:** `03` §6 labelled exploitability `UNRESOLVED`; `33` §5.9 proposed a run to
determine it. **Expert 4 (`C-42`) was right that the outcome is determined** — this file closes it on
source rather than spending authorisation to confirm it.

## 3. `C-04b` — Reachability. Measured, Not Assumed.

The reachable mechanism (`03` §6) needs a **soft-mode** poster: an invoice posted via a bare `_post()`
rather than `action_post`, which can leave a draft carrying COGS lines that the autopost cron later posts
again. Expert 4 identified `point_of_sale` and `sale_subscription` as soft-mode callers **inside the
declared root**.

**Measured against the installed-module list of all 11 material deployments:**

| deployment | gen | marker-capable? | soft-mode poster installed |
|---|---|---|---|
| `4b766580` pankhamhom | 18.0 | yes | **`point_of_sale`** |
| `66d1b52a` BK12MAY26 | 19.0 | yes | **`point_of_sale`** |
| `1f6338ae` iEVING | 19.0 | yes | **`point_of_sale`** |
| `a1cdeab8` | 16.0 | yes | **`sale_subscription`** |
| `5d5164c4` odoo_cff | 14.0 | **no** (`C-43`) | `point_of_sale` + `sale_subscription` |
| the other six | — | mixed | none |

*Control: `account` is installed in 11 of 11, so the extraction fires.*

**`P02-F-47b`** *(corrected `C-57`)*. The precondition is present in **three marker-capable LINEAGES** — the four uuids include `66d1b52a` and `1f6338ae`, which `45` §5 confirms are **one lineage**. The original "four" over-counted by 25%. It is therefore not theoretical. **But `display_type='cogs'` is zero in every one of
them** — the generator has never executed **once**, so no deployment can evidence it executing **twice**.

**`P02-F-47c` — why read-only exhaustion is now proved rather than asserted.** All **nine** live
databases across **both** containers were re-queried this round: **0 journal lines and 0 posted moves in
every one.** The archived estate contains **zero** instances of the mechanism firing. `C-04b` is
unanswerable from the estate **by construction, not by insufficient searching.**

---

## 4. Authorisation Status

**Searched: this session's user instructions. No explicit Boss authorisation for bounded sandbox
execution exists.** Per §9.2 of the governing prompt: **DO NOT EXECUTE.** Nothing was executed.

## 5. `P02_C04_BOSS_AUTHORISATION_PACK`

**Requested only for `C-04b`. `C-04a` no longer needs a run.**

| Field | Value |
|---|---|
| **Exact sandbox** | container `occ-odoo18-db` (postgres:16), app container `occ-odoo18-webtest` (odoo:18.0) |
| **Exact database** | **`occ_anglo_test`** — 0 journal lines, 0 posted moves, perpetual stack already installed (`account 18.0.1.3`, `stock 18.0.1.1`, `stock_account 18.0.1.1`, `sale_stock 18.0.1.0`, `l10n_th 18.0.2.0`). **No customer or production database.** |
| **Exact company** | **`id=1` (`My Company`)** — not a real-entity record. Companies 2–5 carry live OCC entity names and must not be used. |
| **Exact script** | `~/OCC_Odoo18_Simulation_Lab/scripts/anglo_gross_profit_test.py`, **plus** the soft-mode variant in §5.1 |
| **Exact command** | `docker exec -i occ-odoo18-webtest odoo shell -d occ_anglo_test --no-http < <script>` |
| **Modules to install** | **NONE.** The stack is already installed. |
| **Expected writes** | `res_company(1).anglo_saxon_accounting=True`; create 1 account (`130100`), 1 product category, 1 warehouse, 1 product, 2 partners, 1 PO + receipt + bill, 1 SO + delivery + **future-dated** invoice; `env.cr.commit()` |
| **Pre-state** | **MANDATORY, not optional:** `docker exec occ-odoo18-db pg_dump -U odoo -Fc occ_anglo_test > occ_anglo_test_pre_c04.dump` |
| **Rollback** | `dropdb --if-exists occ_anglo_test` → `createdb occ_anglo_test` → `pg_restore` the pre-state dump. **Do not run `reset_to_baseline.sh` — it targets `occ_sim`, a different database.** |
| **Restoration proof** | post-rollback `SELECT count(*) FROM account_move_line` must return **0** |
| **Duration / side effects** | single run, one database, bounded to the writes above; no network egress; no other database touched |
| **Stop conditions** | any error before `commit()`; any write attempted outside `occ_anglo_test`; any prompt for a customer credential |

### 5.1 The run must reproduce the reachable mechanism, not the determined one

Per `C-42`, a manual re-invocation of the generator proves only `C-04a`, which is already closed.
The run must instead reproduce `03` §6:

1. post a **future-dated** customer invoice for the storable, real-time product through a **soft-mode**
   caller (bare `_post()`);
2. assert **one** COGS pair exists on a move still in `draft`;
3. let the autopost path post it;
4. **count `display_type='cogs'` lines before and after.**

### 5.2 Evidence to capture
`SNAP` at all five stages including `AFTER_DELIVERY_BEFORE_INVOICE`; the `GROSS_PROFIT / REVENUE / COGS /
INTERIM` block; the `display_type` distribution before and after the second post; `stock_valuation_layer`
count and `account_move_id` linkage; full session log; pre- and post-rollback line counts.

### 5.3 What the run will close
**`C-04b` only** — whether the non-idempotency proved in §2 is reachable through the autopost path.
Secondarily it would be the **first observation anywhere in this package of the split cost path
executing at all**, which **no** deployed history in the estate contains. *(Corrected `C-56`: this sentence originally read "17 lineages", reinstating the withdrawn uuid count under the withdrawn label — precisely the conflation `44` §1.3 forbids.)*

### 5.4 What it will NOT close

**`BP-02` DISCLAIMER (`C-59`, mandatory).** The pack's expected writes set
`res_company(1).anglo_saxon_accounting = True`, which configures the sandbox to the **invoice-triggered**
cost model — **the model `BP-02` declines**. **This run exercises the invoice-triggered path only. It
supplies no evidence about `BP-02`'s delivery trigger and must not be cited toward it.** Reporting a
completed run as *"the split cost path executes correctly"* would present evidence about the rejected
trigger as P02 assurance — the `P02-F-38b` error `38` exists to prevent.
Nothing about the deployed estate: it runs standard v18 with **none** of the 189 unreadable custom
modules. It says nothing about 19.0, whose mechanism differs and whose guard is absent (`P02-F-05c` as
corrected by `C-39`). A v19 counterpart target now exists (`bhpro_tracking_test_20260901`, 19.0,
`anglo_saxon_accounting = true`, 0 transactions) and should be authorised **separately** if a v19 answer
is wanted.

### 5.5 Maximum scope requested
> Authority to execute **one** scripted run against the single disposable database `occ_anglo_test`,
> company `id=1`, in the local `occ-odoo18-db` container, with a mandatory pre-state dump, no module
> install, no other database touched, and the stated rollback with proof.

---

## 6. Disposition

| | |
|---|---|
| `C-04a` | **CLOSED — VERIFIED (source).** Non-idempotent by construction. |
| `C-04b` | **BLOCKED — BOSS AUTHORISATION.** Precondition present in 4 marker-capable deployments; mechanism never observed anywhere; estate exhausted by proof. |

**No work elsewhere in this round was left waiting on it.**
