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

### `AR-04` — scope authorization to enumerate the unread installed code *(new, opened by `MD-03`)*

| | |
|---|---|
| **What is requested** | Authorization to read the **167 installed modules** that `81 §2` shows lie outside this package's declared path set and were **not** examined. |
| **Why it is not already done** | It is a **widening**, and this phase forbids widening. `MD-03` went as deep as the rule allows: it read the `_inherit` declarations of the **three** modules that inherit the P05 core models and stopped. The remaining 167 are `C — NOT SEARCHED`. |
| **Why it matters** | Every negative claim this package makes of the form *"no X exists in the reference"* is bounded to a path set now measured at **52.9% of the installed deployment**. Those negatives are not withdrawn — they are **correctly scoped and narrower than they read**. |
| **Exactly what would be done** | Intersect the installed list with the newly named third addons root; read only modules whose `_inherit` touches a P05 model; re-audit every existing P05 negative against the result. |
| **Constraint** | **Read-only.** No restore, no install, no mutation. |
| **Owner** | Boss |
| **Affected CQ** | `CQ-P05-13` **RE-OPENED**, and the boundary of every negative in `21` / `55`. |

> **`AR-04` is not a request to redo P05.** The positive findings — the counts, the version basis,
> `TX-01`, the state model, the funding partition — rest on code and data that **were** read and do
> not move. What moves is the **reach of the negatives**, and only those.

## 4. Disposition

| | |
|---|---|
| CQs blocked by an authorization item | **2** — `CQ-P05-11`, and `CQ-P05-13` via `AR-04` |
| CQs closed on currently obtainable evidence | **11 of 13** |
| Estate enumeration performed | **NONE** |
| Mutation performed | **NONE** |
| Live database accessed | **NONE** |
| Authorization items open | **3** (`AR-01`, `AR-02`, `AR-04`) · **1 satisfied** (`AR-03`) |

**No CQ was left waiting idle.** Every question that could be closed without authorization was closed,
and the one that could not be **honestly** left closed was re-opened.
