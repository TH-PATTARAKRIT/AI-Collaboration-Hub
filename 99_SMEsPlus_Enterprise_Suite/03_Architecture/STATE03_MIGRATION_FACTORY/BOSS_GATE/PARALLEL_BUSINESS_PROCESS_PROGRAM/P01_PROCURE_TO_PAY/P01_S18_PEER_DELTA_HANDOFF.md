# P01 — SERIES-18 CROSS-PROCESS PEER DELTA

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-12`
Rule applied: **delta only.** Unchanged peer packages were not re-read.

---

## 1. PEER HEADS AT THIS RUN

| Peer | Branch head | Last consumed by P01 | Changed? |
|---|---|---|---|
| P02 order-to-cash | `ff8be512` | — | not consumed this run (no P2P delta sought) |
| P03 manufacture-to-cost | `7fca09ae` | — | **not re-read** — no material delta identified for this run's scope |
| **P04 acquire-to-retire** | **`9e377e30`** | **`985840e`** | **YES — 20+ commits. Consumed in full, §2** |
| P05 expense-to-pay | `808b30e5` | — | not re-read |
| P06 bank-to-reconcile | `9e5d7297` | — | not re-read |
| P07 Thailand tax | `cc9891fe` | — | not re-read; **statutory questions routed to it**, §4 |
| P08 record-to-report | `838134f4` | — | not re-read; **notified**, §4 |
| P09 plan-to-analyze | `d7deb650` | — | not re-read |
| P10 time-based recognition | `284ea665` | — | not re-read |
| P11 core reconciliation | `78e5f58a` (`research/account-core-reconciliation-2026-09-04-001`) | `78e5f58` | unchanged since last consumption |

---

## 2. P04 — CONSUMED, AND IT CORRECTS THIS PACKAGE TWICE

P04 independently reached the same database. **Verified before adoption**, not inherited.

### 2.1 Agreement on identity — independently reached

P04-F-90 records `~/OCC_BACKUP/idemo18_uat_pre_scgl_occ_website_20260830_085432.dump`, internal
`dbname: idemo18_uat`, `database.uuid` **`551ab874-9acb-11f1-b150-6ec7a480be3d`**, `base` **`18.0.1.3`**.
Every one of those matches this package's independent reading in
`P01_S18_DEPLOYMENT_IDENTITY_PROOF.md §2–§4`.

**Two processes reached the same identity from the same artefact by separate routes.** That is
corroboration, and it is recorded as such rather than as one package citing the other.

P04 also records its own version of the same population-selection failure: the database sat
*"one directory away from a path set I chose and never declared"* (P04-F-88). **The identical
defect, found independently, on the same artefact, by two processes.** That is not coincidence —
it is a programme-level method defect, and it is the strongest available evidence for the standing
rule in `P01_POPULATION_SELECTION_METHOD_AUDIT.md §6`.

### 2.2 CORRECTION 1 — there are **three** series-18 identities, not one

**P04-F-101.** Three v18 identities are known:

| uuid | Modules | Character |
|---|---|---|
| `551ab874` | 361 | **the deployment this package analysed**; 388 real assets |
| `4b766580` | 478 | 7 real assets |
| `96548e18` (`T805efaplus`) | 123 | `base 18.0.1.3`; **no `account_asset` table, 0 move lines — a never-transacted v18 install** |

P04 records that `96548e18` was missed by **both** of its own sweeps — it is a `.zip`, so a
`PGDMP` signature scan does not see it, and it is dated **2025**-12-27, so a `*_2026-*` name
pattern does not see it either. **A second independent bound inside the very sweep written to
reconcile the first.**

**Effect on this package.** Everywhere this package says *"the series-18 deployment"*, the correct
reading is *"the series-18 deployment `551ab874`"*. Nothing in this package is a claim about
`4b766580` or `96548e18`. The valuation-policy proof, the GRNI proof and the ฿30.08M
received-not-invoiced figure are all bounded to `551ab874` @ 2026-08-30.

**This does not weaken any finding.** It corrects an article: *the* becomes *this*. But it removes
any licence to speak of "the series-18 generation as deployed" from a single artefact.

**Accepted. Verified:** the `551ab874` reading is this package's own, made before P04's report was
read. The existence of the other two is P04's measurement, adopted with attribution and **not**
re-derived here — reading two further archives was not reachable in this run and is recorded as an
open action, not as an agreed fact.

### 2.3 CORRECTION 2 — a matching version does not prove code identity

P04 (P04-F-97, relaying P07) records that **two code bodies can share one version string** —
17–179 changed lines across seven files in P07's case — and that a display name and version can
span two technical identities. *"Neither name nor version identifies deployed code."*

**Effect on this package.** `P01_POPULATION_SELECTION_METHOD_AUDIT.md §4` reports that 6 of 16
deployed custom modules have a **version-matching** source copy. That statement is accurate as
written and **must not be read as "the source on this host is the code that runs"**. A version
match is **necessary, not sufficient**.

**Where this package relied on a version match, it has been strengthened rather than caveated.**
The one custom module whose *behaviour* this package reads —
`scgl_product_category_company 18.0.1.5.0`, in
`P01_S18_RECEIPT_VALUATION_ACCOUNTING_TRACE.md §6` — was re-verified at **schema level**:

| Source declares on `product.category` | Present in the deployed table? |
|---|---|
| `company_ids` Many2many, `relation="scgl_product_category_company_rel"` | **yes** — table exists, columns `category_id` / `company_id`, 32 rows |
| `show_on_product` Boolean | **yes** |
| `usage_type` Selection | **yes** |
| `scgl_allow_sale` Boolean | **yes** |
| `scgl_allow_purchase` Boolean | **yes** |
| `scgl_allow_expense` Boolean | **yes** |
| `active` Boolean | **yes** |
| `scgl_available_for_current_companies` (compute) | correctly **absent** — not stored |
| `scgl_company_scope_summary` (compute) | correctly **absent** — not stored |

**Seven of seven stored fields correspond, the named relation table matches, and both compute
fields are correctly absent.** That is structural correspondence, not a version string.

*Residual doubt, stated:* schema correspondence proves the deployed module declares the same
model; it does **not** prove the deployed method bodies are identical. The guard's *existence and
reachability* are `FACT VERIFIED`; its *exact code* is `SUPPORTED INTERPRETATION`. A competing
module, `product_category_filter` in `smeplus-custom/addons`, declares an overlapping field set
and is **not installed** — precisely the "two technical names, one behaviour" hazard P07 named.

### 2.4 P04's completed host census — adopted as a bound

P04-F-123 and §6A.27: **39 artefacts** under a declared path set (`/Volumes` + `$HOME`), size
bound ≥ 1 MB (justified: the smallest Odoo dump on this host is 3.37 MB), and **two** signatures —
`PGDMP` magic **and** a zip central directory containing `dump.sql`. **8 identities keyed; the
population is explicitly left OPEN.**

**Effect on this package.** `P01_POPULATION_SELECTION_METHOD_AUDIT.md §3` published six identities
as a **floor**. P04's completed census raises the floor to **eight**, and P04 declines to state a
total. **P01 adopts eight as the floor and likewise states no total.**

A partial independent sweep run here (home directory, depth 4, `~/Library` and `~/.Trash` pruned,
size > 1 MB, four extensions) returned artefacts consistent with P04's — including
`iSMEs_2026-07-11`, `iEVING_2026-07-23`, `iEVING_2026-03-30.zip`, `iTEST02_2026-07-14`,
`BK12MAY26_2026-08-03` in both `.dump` and `.zip` form, and the OCC archive. It was **not** run at
P04's rigour (no content-signature scan, no volume sweep) and is recorded as **corroborating, not
replicating**.

---

## 3. WHAT P01 HANDS TO PEERS

| To | Item | Why it is theirs |
|---|---|---|
| **P08** record-to-report | **฿29,029,467.66 tax-exclusive** received-not-invoiced across 1,580 PO lines — ฿27,490,865.80 of it receipt-backed on 1,411 lines, the balance operator-typed service quantities — **unrecognised and unaccrued**, with **0 accrual entries** in 15,522 journal entries | A completeness question for liabilities and inventory at a reporting date. P01 measures it; P08 owns the reporting judgement |
| **P08**, **P11** | **10 vendor bills whose balancing line sits outside the payables subledger** (9 on `218001`, 1 on `221002`; ฿12,969.27) | A subledger-to-ledger reconciliation difference |
| **P11** core reconciliation | The **series-18 vs series-19 same-shape / different-cause** result, and the fact that five "not reachable" P01 findings collapse to **one** configuration setting | Prevents P11 double-counting five findings that are one decision |
| **P11** | `stock_move.created_purchase_request_line_id` — requisition identity survives into the goods movement in this deployment | Lineage P11 needs; offered as an observation, **not** a design position |
| **P07** Thailand tax | **`P01_S18_WHT_DEPLOYMENT_REALITY.md`** — and it corrects a P01 attribution (`ERR-P01-33`): **`l10n_th` supplies no withholding code at all**. Four **OCA/Ecosoft** modules do, all with **version-matching source in `R4`**; the *multi*-rate module is uninstalled, so one rate per payment. Reachability measured: **0 of 3,508 payments carry `wt_tax_id`**; the certificate register (332 rows) was **bulk-loaded** under `__system__` with migration xmlids; withholding reaches the GL by a **different route** — 358 items on generic `232000` accounts, 330 raised in bank journals — while the **PND-keyed accounts `214001/2/3` hold zero items in all four companies**; register and ledger differ by **฿935.96 (0.59%)** | Statutory correctness is P07's. Three questions routed, `HOLD — STATUTORY EVIDENCE REQUIRED`. P01 answers none of them |
| **P03** manufacture-to-cost | Valuation is `manual_periodic` and cost method `standard` globally, with `average` on 18 categories in company 1 only; `stock_landed_costs` **not installed** | Cost-flow assumptions P03 may have taken from another deployment |
| **P04** | Acknowledgement of P04-F-90 / F-101 / F-97, and the schema-level corroboration in §2.3 which P04 may reuse for its own custom-module identity claims | Reciprocal |

---

## 4. DECISION-AUTHORITY BOUNDARY

Restated because this run consumed a peer package that corrects it twice:

- **A peer position is not a peer decision, and a peer decision is not a Boss decision.**
- P01 has **adopted two P04 corrections** (§2.2, §2.3) because they are measurements P01 verified
  or bounded, not because a peer asserted them.
- P01 has **not** adopted P04's identity total, because P04 does not state one.
- P01 does **not** overrule P05, P06 or P07, and does **not** define P03, P08 or P11 architecture.
- Nothing in §3 is a decision. Each item is measurement plus routing.
- Whether periodic valuation is right for this business, and whether the unaccrued GRNI position
  is acceptable, are **Boss decisions**. They are stated in
  `P01_P11_S18_DIRECT_VERIFICATION_SUPPLEMENT.md` as options, never as recommendations.
