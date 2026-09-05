# P01 — AUTO-RESUME STATE

Session: P01 — Procure-to-Pay (one continuing session across five prompts)
Layer: **1.** **An interruption is not a reset.**
Last updated: end of `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`

---

## 1. WHERE THE WORK IS

| | |
|---|---|
| Repository | `TH-PATTARAKRIT/AI-Collaboration-Hub` |
| Branch | `research/account-p01-procure-to-pay-2026-09-04-001` |
| Baseline this round | `2620c832b278e45d1d5f81fe95ad6ec52e12ee39` |
| Package path | `…/BOSS_GATE/PARALLEL_BUSINESS_PROCESS_PROGRAM/P01_PROCURE_TO_PAY/` |
| Expert reports | `_expert_out/`, `_expert_out2/`, `_expert_out3/`, **`_expert_out4/`** (this round, four reports + the frozen brief) |
| Terminal state | `P01 SERIES-18 DIRECT VERIFICATION — MAXIMUM AVAILABLE EVIDENCE REACHED — HOLD FOR SPECIFIC SOURCE / DATABASE / POLICY / PEER / STATUTORY / BOSS DECISION` |

---

## 2. WHAT THIS ROUND ESTABLISHED

For the first time in five rounds, a P01 source finding and a deployed record are **the same
generation**. Database `551ab874-9acb-11f1-b150-6ec7a480be3d` (`idemo18_uat`) is series 18 — proved
from the **schema**, decisively by a string comparison series 19 cannot satisfy.

- Valuation policy is **`manual_periodic`** on 126 of 126 categories, read from **both** storage
  locations. **The best-evidenced claim in five rounds of P01**; it survived four independent
  attacks.
- The 0-of-47,801 zero-link result is **EXPECTED UNDER PERIODIC POLICY**, scoped to 43,227 rows,
  and holds on a corrected runtime denominator of **541**.
- **SAME SHAPE / DIFFERENT CAUSE** against the series-19 estate — the round's central control, and
  it held.
- The GRNI account is **configured** (171 of 504 pairs; 126 of 126 in the transacting company),
  **not executed** (zero items across the whole three-account configuration), and **reachable by
  four writer routes**.
- **฿29,029,467.66** tax-exclusive received-not-invoiced, unrecognised and unaccrued.

**Findings withdrawn: 0. Findings contradicted: 0** — the one reported contradiction was this
package's own error.

---

## 3. WHAT THIS ROUND GOT WRONG, AND WHO FOUND IT

**Eleven corrections. Three found by this session, eight by the four challengers.** Two falsified
claims this run had published hours earlier: *"the bill-line override is series-19 only"* and
*"no `purchase_request` source at the deployed version"*.

Full lineage in `P01_RESEARCH_ERROR_AND_REVISION_LOG.md`, `ERR-P01-24` … `ERR-P01-40`.

---

## 4. NEXT EXACT ACTION

> **Read the located source for the deployed custom modules and the ten unenumerated database
> artefacts. Both are on this machine, and both were recorded as external dependencies until this
> round proved otherwise.**

**In order:**

1. **`~/Downloads/OCC_PR_MULTI_APPROVE_UAT_PASS_36/purchase_request`** — `18.0.1.10.0`, the deployed
   version. Content-verify it against the deployment rather than trusting the version string, then
   read `_prepare_merge_moves_distinct_fields`, `_merge_moves_fields` and `stock.picking._action_done`,
   which bound every stock-move count in this package (`ERR-P01-40`).
2. **`~/Downloads/OCC/scgl_account_coa_control`** — `18.0.1.0.1`. Its name asserts chart-of-accounts
   control, it owns four view xmlids and zero fields, and it is the sharpest candidate for a
   **method-level override** — the one gap no database artefact can close. Grep for
   `_validate_accounting_entries`, `_account_entry_move`, `AccountMove._post`, `property_valuation`,
   `_apply_price_difference`. **Until this is read, every negative in the policy proof carries an
   unbounded method-override scope across 56 modules.**
3. **`~/Downloads/BK12MAY26_2026-08-03_11-28-04.zip::dump.sql`** — 283 MB, Odoo **19.0+e**, 251
   modules. The largest database artefact on this host, invisible to every census run before this
   round, and this entire package is about the v18→v19 semantic change.
4. **`~/Library/Mobile Documents/…/Downloads/pankhamhom_2026-01-21_06-39-19.dump`** — a **series-18**
   database with a **478-module** manifest. A second same-generation deployment.
5. **`~/OCC_Odoo18_Simulation_Lab/evidence/perpetual_at_invoicing/occ_sim_pre_perpetual.dump`** — a
   local snapshot **named for the exact transition this package is about**, never cited.
6. **`mail_tracking_value` on `product.category`.** 240 tracking rows exist, **9 of them on
   `property_cost_method`** — which carries `tracking=True` while `property_valuation` does not.
   This is the only instrument that could settle **whether this deployment was ever `real_time`**,
   which no current-state read can.
7. **Measure write access to `property_valuation` in company 1** — `ir_model_access`, `ir_rule`,
   `res_groups_users_rel`. Turns a capability into an exposure, or retires it.

**Method, non-negotiable after this round:** run every enumeration at **two widths, two units and
two probe forms**, and reconcile. A bounded probe returning empty is an **unfinished measurement**,
not a negative — established three times over, including once inside this round's own verification
of someone else's correction. Declare the path set **as a set**, never as a description. *"Full-volume"*,
*"this host"* and *"everywhere"* are descriptions, and each one of them produced a published
falsehood in this programme.

---

## 5. STANDING CONSTRAINTS — UNCHANGED

- **No implementation.** No production code, no schema change, no module install, no migration, no
  deployment, no merge to `SMEsPlus`, no self-authorization.
- **Read-only runtime.** Nothing has been executed in any of five rounds. Where a write would be
  required: `HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED`.
- **Clean room.** Layer 1 carries no reference-system paths; Layer 2 is audit quarantine.
- **Statutory discipline.** Thai WHT/PND conclusions require authoritative statutory evidence.
  `HOLD — STATUTORY EVIDENCE REQUIRED`, routed to **P07**.
- **Decision authority.** P01 does not overrule P05, P06 or P07, and does not define P03, P08 or
  P11 architecture. *Peer Position ≠ Peer Decision ≠ Boss Decision.*
- **No Boss contact during execution.** FINAL GATE only.
- **No PASS wording.**
- `JIRA — AUTHORITATIVE ISSUE NOT VERIFIED`.

---

## 6. OPEN BLOCKERS

| ID | Blocker | Status |
|---|---|---|
| `DEP-P01-01` | Deployed copy identity | **OPEN, but narrowed** — 11 of 16 named custom modules now have version-matching source on this host |
| `DEP-P01-06` | Tenant residue | **PARTIALLY RESOLVED** — unchanged this round |
| `S18-B-01` | Two further series-18 identities (`4b766580`, `96548e18`) plus `pankhamhom` unread | **OPEN** |
| `S18-B-02` | Whether periodic was intended or lost in migration | **OPEN — external evidence required** |
| `S18-B-03` | The P01 source path set does not contain the deployment's custom code | **OPEN** — re-declaring it changes the evidence base of five published rounds; **raised, not done unilaterally** |
| `S18-B-04` | Estate population open — ≥ 8 identities across ≥ 27 artefacts, no total | **OPEN** |
| `S18-B-05` | Method-level override unverifiable across 56 non-core modules | **OPEN, and now closable** — see §4 items 1–2 |
| `S18-B-07` | Series-16 **core** behaviour unread | **OPEN — and no longer an external dependency.** The core is on this host (`ERR-P01-41`); the blocker changes from *unobtainable* to *unread* |
| `S18-B-06` | `om_data_remove` installed; raw-SQL deletion bounds every count | **OPEN** — flagged to **P06**, not re-derived here |
| — | Runtime execution of the seven priority edge cases | **HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED** |
| — | Thai WHT / PND statutory basis | **HOLD — STATUTORY EVIDENCE REQUIRED** → P07 |

---

## 7. EXIT POSITION

**`EC-01` … `EC-08`: 0 satisfied, 8 not satisfied. No improvement claimed.** `EC-06` deteriorates:
six population-selection defects are now recorded where round 4 recorded one.

> A round that discovers its evidence base is wronger than it thought has improved its **honesty**,
> not its exit position — and the two must not be reported as the same thing.

PMO: **`RECOMMEND HOLD`**. AAS+: no veto, dissent preserved.

---

# ROUND 6 UPDATE — SERIES-16 SAME-GENERATION DIRECT VERIFICATION

Prompt: `SMEPLUS-26-09-05-ACC-P01-P2P-S16-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Baseline: `f76e443df3b3e7c9545ca731f0d963a96d636ca0` · Expert reports: `_expert_out5/`

## R6.1 WHAT THIS ROUND ESTABLISHED

**The mechanism P01 described from source for five rounds has now been observed operating.**

Deployment `45a8e08e` (`iSMEs`, `swr.smeplus.asia`, one company — a rice miller, 183,590 journal entries):
**57,863 of 74,982 valuation layers carry a journal entry.** The series-19 estate showed 0 of 14,441; the
series-18 OCC deployment 0 of 47,801. **This is the positive control the valuation line of enquiry never had.**

It is also the first **mixed** policy population in the programme: global `manual_periodic` with **15 of 30
categories** overriding to `real_time`, so the policy claim is testable inside one database — real_time 98.2%
posts, periodic 93.0% does not, coverage control 0 of 74,982 unresolved.

The **GRNI bridge closes**: account `2900000 Goods Receipt Note`, 13,736 items, net **฿72,097,814.25**, with
**6,653 vendor-bill lines** debiting it for ฿4,516,394,611.47.

## R6.2 WHAT IS OPEN

| ID | Item | Status |
|---|---|---|
| `S16-C-14` | Inventory subledger vs GL disagree by ~10¹⁵ on 30 layers (GL itself is intact and balanced) | **OPEN** → P03, P08 |
| `S16-C-15` | 296 real_time non-zero layers unposted; 1,209 periodic layers posted; policy-change **refuted** | **OPEN** |
| `S16-C-18` | 30 posted moves dated year 2567 (BE) + 1 `invoice_date` 2568 | **OPEN** → P08 |
| `S16-B-01` | Purchase price variance account configured, **0 items in 447,384**, with the valuation gate **open** | **OPEN** |
| `S16-B-02` | Vendor-advance settlement lineage; P05 disagreement **preserved unresolved** | **OPEN** |
| `S16-B-03` | Whether `om_data_remove` (installed, 16.0.1.0.1) has ever run here | **OPEN — under challenge** |
| `S16-B-04` | No period lock of any kind, on 169,143 posted entries | **OPEN** → P08 |
| — | Thai WHT statutory correctness | **HOLD — STATUTORY EVIDENCE REQUIRED → P07** |
| — | Runtime execution of the seven priority edge cases | **HOLD — RUNTIME WRITE AUTHORIZATION REQUIRED** |

## R6.3 NEXT EXACT ACTION

> **Measure the vendor-advance / partial-payment / settlement lineage in `45a8e08e`** — the one deliverable
> this round left `PARTIAL — RESUMABLE`. Join **22,468 `account_payment` rows** against **447,384
> `account_move_line` rows** through `account_partial_reconcile` (8.49 MB) and `account_full_reconcile`
> (3.00 MB), all already extracted at
> `…/scratchpad/s16/T_*.sql`, and establish: whether advances are deducted from final bills, the
> partial-payment withholding arithmetic on the **4,941** supplier payments carrying `wt_tax_id`, and the
> residual payable after settlement.
>
> It was **not attempted** this round rather than attempted and estimated. It is the largest remaining
> executable piece in this package and it needs no new evidence — every table is already on disk.

**Second action, if the first is blocked:** enumerate every writer of `stock_valuation_layer.account_move_id`
in the series-16 core **and** in the 45 deployed custom modules, to close or explain `S16-C-15`.

## R6.4 METHOD — HARDENED AGAIN

Two widths, two units, **two probe forms** — and now also:

> **Assert every join key exists in the generation under study before joining on it.** A COPY parser that pads
> absent columns will happily let you join on a column that does not exist, return a plausible answer, and
> satisfy a positive control sitting right beside it (`ERR-P01-42`). Schema shape is generation-specific in
> exactly the way storage location is (`ERR-P01-19`).

> **A correction is not immune to the defect it corrects** (`ERR-P01-43`).
