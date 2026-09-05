# P01 — SERIES-18 PURCHASE-REQUEST MODULE DEPLOYMENT PROOF

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-S18-SOURCE-DEPLOYMENT-DIRECT-VERIFY-001`
Checkpoint: `CP-P01S18-06`

Governing rule for this document: **presence of a custom module does not imply exercised behaviour.**
Installed, configured, reachable and exercised are established separately.


> ### PEER DELTA APPLIED — BOUND TO ONE IDENTITY
>
> Peer **P04** (`9e377e30`, `P04-F-101`) records **three** series-18 database identities on this
> host, not one: `551ab874` (361 modules — the one analysed here), `4b766580` (478 modules), and
> `96548e18` (`T805efaplus`, 123 modules, never transacted). **Everything in this document is
> bounded to `551ab874` @ 2026-08-30** and is not a claim about the series-18 generation as
> deployed elsewhere. See `P01_S18_PEER_DELTA_HANDOFF.md §2.2`.

---

## 1. MODULE IDENTITY

| Property | Value |
|---|---|
| Technical name | `purchase_request` |
| `state` | **installed** |
| `latest_version` | **18.0.1.10.0** |
| Companion | `scgl_multi_approve_purchase_request` 18.0.1.0.0, **installed** |
| Companion core | `scgl_multi_approve_core` 18.0.0.3.1, **installed** |

Tables present in the archive: `purchase_request`, `purchase_request_line`,
`purchase_request_allocation`, `purchase_request_line_make_purchase_order`,
`purchase_request_line_make_purchase_order_item`, `purchase_request_purchase_order_line_rel`,
`purchase_request_rejected`, and the custom `scgl_multi_approve_purchase_request_event`.

---

## 2. INSTALLED ≠ AVAILABLE IN SOURCE — AND HERE IT IS NOT

**POPULATION:** every directory named `purchase_request` on `/Volumes/iMacSys`, at full depth.
**PATTERN:** `find /Volumes/iMacSys -type d -name "purchase_request"`.
**UNIT:** one module directory. **MEASURE:** the `version` string in its `__manifest__.py`.

**16 copies** found. Versions:

| Version | Copies |
|---|---|
| 19.0.2.4 | 4 |
| 19.0.1.0 | 3 |
| **18.0.1.8** | **4** |
| 14.0.1.3.8 | 2 |
| 19.0.1.1 | 1 |
| 19.0.1.0.0 | 1 |
| 1.0 | 1 |

**No copy at `18.0.1.10.0`.** The deployed purchase-request module has **no matching source on
this host**.

**CLASSIFICATION: VERIFIED ABSENCE (class A) within the stated population** — the population being
this volume, this pattern, this unit. It is not a claim about any other host or about the module's
behaviour. `NO SOURCE COPY FOUND` is not `THE MODULE DOES NOT WORK`.

The nearest copies are four at `18.0.1.8`, including one inside the declared source path set `R4`.
**A near version is not the version.** `ERR-P01-13` was caused precisely by reasoning from source
that no deployment runs; the same mistake is available here and is refused. Nothing in this package
attributes behaviour to `purchase_request` from reading `18.0.1.8`.

---

## 3. DEPLOYED POPULATION — THE MODULE IS EXERCISED

| Measure | Value |
|---|---|
| `purchase_request` rows | **1,043** |
| — `approved` | **866** |
| — `to_approve` | 96 |
| — `draft` | 74 |
| — `rejected` | 7 |
| By company | company 1: 652; company 2: 391 |
| `date_start` range | 2022-08-31 → 2026-08-29 |
| `purchase_request_line` rows | **3,398** |
| — carrying a `purchase_state` (i.e. reaching a purchase order) | **1,504** (`purchase` 1,462, `done` 42) |
| — no purchase state | 1,894 |

**44.3% of request lines reach a purchase order.** The rejection path is exercised too (7 rejected
requests) — a control that is used, not merely present.

**CLASSIFICATION: INSTALLED · CONFIGURED · REACHABLE · EXERCISED.**

Note on the date range: `date_start` values reach back to 2022-08-31, well before
`database.create_date` (2026-08-18). These are **migrated** request records. The distinction
between migrated and natively-created rows, which mattered decisively for the valuation layers,
is **not** separated here — it was not needed for the conclusion (exercise is established either
way) and is recorded as a bounded gap rather than left implicit.

---

## 4. HANDOFF INTO THE PURCHASE ORDER

| Link | Evidence |
|---|---|
| `purchase_request_line.purchase_state` | 1,504 lines carry one |
| `purchase_request_purchase_order_line_rel` | relation table present |
| `stock_move.created_purchase_request_line_id` | column present on `stock_move` — the request identity is carried all the way to the **stock move**, not only to the order |

That last link is worth stating plainly: in this deployment the requisition identity survives into
the goods movement. That is more lineage than the reference chain provides on its own, and it is
the kind of link P11 needs for reconciliation. It is offered to P11 as an **observation**, not as a
design position.

---

## 5. FINANCIAL EFFECT — NONE DIRECTLY

**POPULATION:** the 1,122 TABLE definitions in the archive TOC, and the 40,353 rows of
`account_move_line`.

No `account_move` or `account_move_line` in this deployment references a purchase request. The
module's accounting effect is **indirect**: it governs which purchase orders come into existence,
and the purchase order's own accounting effects are traced in
`P01_S18_RECEIPT_VALUATION_ACCOUNTING_TRACE.md`.

**CLASSIFICATION: no direct financial effect — FACT VERIFIED** within that population.

---

## 6. ARE PRIOR P01 PURCHASE-REQUEST FINDINGS REACHABLE HERE?

Prior P01 rounds analysed purchase-request behaviour from source copies in the declared path set,
which are at `18.0.1.8`. The deployment runs `18.0.1.10.0`.

**Every prior purchase-request source finding is therefore classified
`VERSION-DEPENDENT — REACHABILITY UNKNOWN` against this deployment.** Not withdrawn — findings stay
bound to the population in which they were measured — but they may not be asserted of this
deployment, and this package asserts none of them.

The gap is closable only by obtaining `purchase_request 18.0.1.10.0` itself, from the deployment
owner or the build that produced it. That is recorded as the concrete evidence request in
`P01_AUTO_RESUME_STATE.md`.

---

## 7. CLASSIFICATION SUMMARY

| Item | Classification |
|---|---|
| `purchase_request 18.0.1.10.0` installed | **FACT VERIFIED** |
| Multi-approve companions installed | **FACT VERIFIED** |
| Module is exercised (1,043 requests, 866 approved, 1,504 lines to PO) | **FACT VERIFIED** |
| Requisition identity carried to the stock move | **FACT VERIFIED** |
| No direct financial effect | **FACT VERIFIED** within the stated population |
| Source copy at the deployed version exists on this host | **VERIFIED ABSENCE** — 16 copies, none at `18.0.1.10.0` |
| Prior P01 purchase-request source findings, against this deployment | **VERSION-DEPENDENT — REACHABILITY UNKNOWN** |
| Migrated vs natively-created request rows | **UNRESOLVED — not separated**; bounded gap, did not affect the conclusion |
