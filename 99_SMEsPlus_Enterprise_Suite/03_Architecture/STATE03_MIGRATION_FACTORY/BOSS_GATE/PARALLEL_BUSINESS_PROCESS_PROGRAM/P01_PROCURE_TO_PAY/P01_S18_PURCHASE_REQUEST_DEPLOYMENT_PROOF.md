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

## 2. THE SOURCE EXISTS — MY OWN ABSENCE CLAIM WAS FALSE — `ERR-P01-37`

> **The first published version of this section stated:**
> *"**16 copies** found … **No copy at `18.0.1.10.0`.** The deployed purchase-request module has
> **no matching source on this host**. **CLASSIFICATION: VERIFIED ABSENCE (class A).**"*
>
> **It is at `/Users/admin/Downloads/OCC_PR_MULTI_APPROVE_UAT_PASS_36/purchase_request`,
> `"version": "18.0.1.10.0"`** — plus the same tree inside the sibling `.zip`.
> Found by AAS-03 Expert D; **verified here directly** by reading the manifest.

### 2.1 How the claim was made, and why it failed

| Rung | Declared | Actually executed |
|---|---|---|
| **PATTERN** | `find -type d -name "purchase_request"` | correct — but blind to a module shipped **inside an archive** |
| **PATH SET** | *"full-volume"* | **`/Volumes/iMacSys` only.** The file is in **`$HOME/Downloads`** |
| **UNIT** | one module directory | a module can also be a **ZIP member**; at that unit there are 87 more hits |

**"Full-volume" named a storage device, not a boundary over the artefacts.** It reads as
exhaustive and is a *scope stated as a description* — the same failure that produced `ERR-P01-23`
(a directory standing in for a population) and `ERR-P01-25` (a declared root that excluded the
deployment's own code). **This is the third instance in one package, and the second found by
someone else.**

### 2.2 The corrected enumeration

**POPULATION:** the 16 name-matched installed custom modules. **UNIT:** a directory *or a ZIP member
path* containing `__manifest__.py`. **PATH SET:** `$HOME` (less `~/.Trash`) **+ both volumes +
`~/Library/Mobile Documents` (iCloud Drive) + `~/Library/CloudStorage` (Google Drive)**.

| | As first published | Corrected |
|---|---|---|
| Version-matching source exists | 6 of 16 | **11 of 16** |
| No copy by name **anywhere** | 7 | **3** |
| Copies only at other versions | 3 | 2 |
| `purchase_request` copies | 16 | **53** |
| **`purchase_request` at `18.0.1.10.0`** | **0 — "no copy"** | **2** |

**Four modules the first version placed in the "zero copies anywhere" bucket do have
version-matching source**, among them `scgl_account_coa_control 18.0.1.0.1` and
`scgl_multi_approve_purchase_request 18.0.1.0.0`.

The residual absence, with its negative control, is **three** modules — `scgl_delivery_cost`,
`scgl_signature`, `scgl_signature_hr_expense`. (`scgl_signature` returns 6 name matches, all of
which are `scgl_jasper_api/models/scgl_signature_image.py`, a different module.)
*Positive control, same finder:* `scgl_uom_archive` → 1.

### 2.3 Why `~/Library` was not a defensible exclusion

This session's standing note prunes `~/Library` from home-directory sweeps for a real reason: it
triggers a macOS permission-prompt storm across roughly 855 application-data directories.

**That reason has authority over application data. It has none over
`~/Library/Mobile Documents` (iCloud Drive) or `~/Library/CloudStorage` (Google Drive)** — those are
*user document stores* that Apple and Google happen to mount under `Library`. Both were swept by
Expert D with no prompt storm. **A stated exclusion reason stopped the audit at a boundary the
reason did not cover** — the same shape as `97_OCC_PROJECT` being excluded as CLASS C in
`ERR-P01-25`.

### 2.4 What survives

`purchase_request 18.0.1.10.0` is installed, is exercised (§3), and **its source is now readable**.
Prior P01 purchase-request findings were read from `18.0.1.8` copies and remain bound to that
version — but the gap between analysed and deployed code **is now closable**, and closing it is a
concrete action rather than an external dependency.

**And a caution that survives with it.** A matching version string is **necessary, not sufficient**:
peer P04 (relaying P07) records two code bodies sharing one version string across 17–179 changed
lines. The located tree should be **content-verified** against the deployment before any behaviour
is attributed to it.

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

**That gap is no longer an external dependency.** `purchase_request 18.0.1.10.0` is on this host
(§2). Reading it — and content-verifying it against the deployment rather than trusting the version
string — is a concrete next action, recorded in `P01_AUTO_RESUME_STATE.md`.

---

## 7. CLASSIFICATION SUMMARY

| Item | Classification |
|---|---|
| `purchase_request 18.0.1.10.0` installed | **FACT VERIFIED** |
| Multi-approve companions installed | **FACT VERIFIED** |
| Module is exercised (1,043 requests, 866 approved, 1,504 lines to PO) | **FACT VERIFIED** |
| Requisition identity carried to the stock move | **FACT VERIFIED** |
| No direct financial effect | **FACT VERIFIED** within the stated population |
| Source copy at the deployed version exists on this host | **PRESENT — my own absence claim was FALSE (`ERR-P01-37`).** `~/Downloads/OCC_PR_MULTI_APPROVE_UAT_PASS_36/purchase_request` at `18.0.1.10.0`; 53 copies exist, 2 at the deployed version |
| Prior P01 purchase-request source findings, against this deployment | **VERSION-DEPENDENT — REACHABILITY UNKNOWN**, and **now closable**: the deployed version's source is readable |
| Migrated vs natively-created request rows | **UNRESOLVED — not separated**; bounded gap, did not affect the conclusion |
