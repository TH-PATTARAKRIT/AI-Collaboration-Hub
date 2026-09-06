# 76 — P05 OPEN EVIDENCE AND AUTHORIZATION REGISTER V3

`LAYER 2 — AUDIT QUARANTINE` · `CQ-P05-11` · `CP-P05C-03`

## 1. Rule Applied

> Read only evidence **directly relevant to a declared CQ**. Do **not** re-enumerate the estate to
> prove files still exist. If read-only live access needs authorization, produce an exact request and
> **HOLD only the affected CQ**. Continue every unaffected CQ.

**Two bounded reads were performed** (`MD-01`, `MD-02`, `68 §1`). **No estate enumeration was run.**

## 2. Previously-Named Gaps — reconciled against relevance

| Gap | Relevant to a declared CQ? | Action taken | Disposition |
|---|---|---|---|
| `U-15` `scgl_signature_hr_expense` unanalysed | **YES** — `CQ-P05-03`, `CQ-P05-09` (approval/signature is intrinsic expense control) | **`MD-01` executed**, bounded to the module directory in the three declared source roots | **AUTHORIZATION / LOCATOR REQUIRED** — see `AR-01` |
| `U-16` deployed code ≠ analysed source | **YES** — `CQ-P05-13` | **`MD-02` executed** | **NARROWED** — version basis confirmed for 5 of 5; code identity remains class **D** |
| `U-18` three unread readable archives (`iSMEs182`, `iErpOCC`, `iSCErP`) | **NO** — they would extend the *population census*, not answer any CQ-P05-01..12 | **deliberately NOT read** | **OUT OF BOUNDED SCOPE — closure may become deeper, not wider.** Recorded, not pursued. |
| `U-19` v18 certificate population unanalysed | **PARTIAL** — `CQ-P05-06` is closed on the P05 *interface*, which does not depend on it | not read | **NOT REQUIRED FOR P05 CLOSURE**; would serve P07 |
| `U-20` 12 Docker DBs, 2 live | **YES** — `CQ-P05-03` (live posting behaviour), `CQ-P05-13` (`U-16`) | **not accessed** | **AUTHORIZATION REQUIRED** — see `AR-02` |
| `U-17` cause of the unlinked-sheets population | **YES** — `CQ-P05-09` | not resolvable without live posting | folded into `AR-02` |
| `U-02b` runtime execution evidence | **YES** — `CQ-P05-03`, `CQ-P05-09` | not obtainable read-only from files | folded into `AR-02` |
| `U-09` Thai statutory basis | **NO** — `EXTERNAL DOMAIN BOUNDARY` | not researched | **OUT OF P05 SCOPE — P07 owns it** |

## 3. Authorization / Evidence Request Pack

### `AR-01` — source locator for an installed module
| | |
|---|---|
| **What** | The source of `scgl_signature_hr_expense`, deployed at `18.0.1.0.0` on `idemo18_uat` |
| **Why** | It is an **installed** module extending the expense/approval surface; approval and signature semantics are **P05-owned** (`CQ-P05-03`, `CQ-P05-09`) |
| **Bounded evidence needed** | The module directory, or its `addons_path` location on the deployment host |
| **What was already done** | Checked all three **already-declared** source roots — **absent from all three** (class **B**). No wider search performed, per the no-widening rule. |
| **Owner** | Boss / Infrastructure |
| **Affected CQ** | `CQ-P05-03`, `CQ-P05-09` — **both closed on other evidence**; this would strengthen, not unblock |

### `AR-02` — read-only access to the live Odoo 18 instance
| | |
|---|---|
| **What** | Read-only observation of the running `occ-odoo18-webtest` / `occ-odoo18-db` pair |
| **Why** | It is the **only** route to evidence of the application **posting** an expense. Every P05 accounting-artefact population examined is migration output — no live posting exists in any file-based evidence. |
| **Exactly what would be observed** | Create-provenance of accounting artefacts produced by an authorisation act; whether the float account is credited by a live claim; whether a correction publishes anything; the deployed module source |
| **Constraint** | **Read-only. No mutation, no restore, no configuration change, no transaction creation.** |
| **Owner** | Boss |
| **Affected CQ** | `CQ-P05-11` **HOLD**. `CQ-P05-03` and `CQ-P05-09` are **closed on source + state evidence**; this would upgrade specific sub-claims from `SUPPORTED INTERPRETATION` to `FACT VERIFIED`. |

### `AR-03` — deployed module list for the target platform *(satisfied)*
Closed by `43`: two Odoo 18 registries obtained. **No further request.**

## 4. Disposition

| | |
|---|---|
| CQs blocked by an authorization item | **1** — `CQ-P05-11` only |
| CQs closed on currently obtainable evidence | **12 of 13** |
| Estate enumeration performed | **NONE** |
| Mutation performed | **NONE** |
| Live database accessed | **NONE** |

**No CQ was left waiting idle.** Every unaffected question was closed.
