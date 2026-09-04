# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 11 — Open Items And Dependency Register

Control Level: `/L9999.9999`
Status: `14 NEW ITEMS RAISED — 0 PRIOR ITEMS CLOSED — ALL CARRIED IDENTIFIERS PRESERVED UNCHANGED`

---

## 1. Lane Vocabulary In Force

**This register uses the authorization's lane vocabulary**, which is the same vocabulary the AAS+ / PMO review used and translated to. R4's own registers use different meanings for the same letters, and `REV-F-03` records that collision as `MATERIAL` and unresolved.

| Letter | Meaning here |
|---|---|
| **A** | Inventory-owned architecture / control / data identity |
| **B** | Accounting COGS / valuation / period-close dependency |
| **C** | Business SME / Thai user / statutory validation |
| **D** | Clean-room / governance / audit veto / Boss ruling |
| **E** | Cross-module joint decision |
| **F** | Duplicate / superseded / no-action |

`REV-F-03` remains open. Until Boss ratifies one vocabulary programme-wide, every cross-document lane reference stays ambiguous and the review's mapping at `05` §2 remains the only published translation. **This session adds a second document using the authorization's vocabulary; it does not resolve the collision.**

---

## 2. New Findings Raised By This Session

| ID | Finding | Lane | Severity | Owner | Evidence Need / Next Action | Blocks v2.0 | Blocks DFG |
|---|---|---|---|---|---|---|---|
| `MTI-F-01` | A traceable identity's **bare value is not its identity**. Identical batch or serial values across companies are legitimate; presenting, exporting or handing off the bare value is not | **A** | MATERIAL | Inventory | Adopt the resolved tuple as the presented and transmitted identity everywhere. No further evidence needed to specify; verification needs an implementation | No | Yes |
| `MTI-F-02` | The **owner dimension is orthogonal to company** and must never be conflated with it. Conflation fails in both directions — consignment stock and goods on approval | **A** design / **B** value | MATERIAL | Inventory + Joint | Separation is specifiable now (`HF-CTX-09`). What may be valued as whose asset is `GAP-MD-09`, open | **Yes** | Yes |
| `MTI-F-03` | **Absence must not leak existence.** Per-company uniqueness creates a disclosure channel through uniqueness feedback, autocomplete, barcode resolution and error text | **A** | MATERIAL | SaaS Foundation | Specify the non-disclosure response contract. Created by `MTI-12`; must be designed with it, not after | No | Yes |
| `MTI-F-04` | Element 10 requires **carriage plus attestation**. A context value without evidence of how it was determined does not satisfy contract §3 or survive §4 | **A** | MATERIAL | Inventory + SaaS Foundation | `HF-CTX-05`, `HF-CTX-06` specified. Requires the `MTI-19` control to exist before the attestation means anything | **Yes** | **Yes** |
| `MTI-F-05` | **Approval routing may not cross a company boundary**, so segregation of duties must degrade to a compensating control rather than be satisfied by crossing one | **A** design / **C** content | MATERIAL | Inventory + Thai panel | The compensating-control design needs Thai user input. Compounds `R4-F-21` and `L7-09` | No | Yes |
| `MTI-F-06` | **Context conservation across handoffs is not checked by any existing reconciliation.** Both domains can balance internally while a fact crossed a boundary | **A** count / **B** value | MATERIAL | Inventory + Accounting | New identity `RC-11`. Count comparison specifiable now; value comparison held | **Yes** | Yes |

---

## 3. New Decision Blockers Raised By This Session

Each requires a decision that this session is not empowered to take. None is an investigation.

| ID | Decision Required | Lane | Owner | Why It Cannot Be Taken Here | Consequence If Deferred |
|---|---|---|---|---|---|
| `MTI-D-01` | **Product master scope** — tenant-level definitional identity with company-level attachment (option A, the position taken), or a company-owned master (option B) | **D** then **A** | **Boss** | It is a product-scope decision with a real trade-off in both directions, set out at `03` §4.2. An executor may state the options and a recommendation; it may not choose | `MTI-11`, matrix rows 5, 6, 7, `XCR-03`, `L10-04` and `MTA-17` all stay conditional. The invariant set cannot be finalised |
| `MTI-D-02` | **Authorization granularity** — company-only, warehouse-level, or location- and operation-class-level | **D** then **A** | **Boss** | Carried from `RISK-U01` / `U-01`, recorded as *"not merely undesigned — unevidenced either way"*. A scope ruling, not research | `L9-03` stays unprovable; segregation of duties stays undesignable (`L7-09`); `MTP-15` cannot be scored |
| `MTI-D-03` | **Shared-template versus tenant-owned boundary content** — what a tenant may change | **D** then **A** | **Boss / product scope** | Carried from `GAP-MD-14` / `SAAS-04`. The mechanism is specified (`MTI-35`); the boundary is a product decision | `L9-04` stays `PARTIALLY DEFINABLE`; `MTP-19` cannot be run; `XCR-04` stays conditional |
| `MTI-D-04` | **Cross-company visibility policy** — whether a group owner may hold a consolidated read across companies, and under what governance | **D** | **Boss** | A real Thai SME group need, and a deliberate hole in an isolation boundary. Only Boss may authorise a door | `MTI-25` and `XCR-02` stay conditional. Without a ruling the need will be met informally by exports, which is worse |
| `MTI-D-05` | **PDPA and tenant erasure scope** for Inventory documents and records | **D** then legal | **Boss + Legal + Account track** | `GAP-MD-29` is recorded as having **zero coverage anywhere in the evidence chain**. No AI may supply a legal scope | `MTI-49` stays shape-only; `MTA-24` stays `BLOCKING`; tenant offboarding has no defined boundary |
| `MTI-D-06` | **Physical consolidation across companies** — whether a handling unit may ever carry two companies' goods, and if not, what concept replaces the practice | **C** then **A** | **Thai panel then Inventory** | A logistics reality question. No AI may answer it | `MTI-13` may prohibit an operational practice the target market depends on (`MTA-20`) |

---

## 4. Evidence Notes

| ID | Note | Lane | Severity | Owner | Action |
|---|---|---|---|---|---|
| `EVIDENCE-NOTE-01` | Three of the eleven mandatory sources are named in the authorization by filenames that do not exist. Functional equivalents identified and verified at `01` §2 | **D** | WATCH | PMO | Correct the source names in any successor prompt. No evidence was unavailable |
| `EVIDENCE-NOTE-02` | Both governing Boss controls exist only on the canonical branch and not in the prompt or execution branch working tree. Read by commit citation; both resolve | **D** | WATCH | PMO / Boss | Same condition as `R4-D-03`, independently reproduced. Consider carrying the controls onto prompt branches so a working-tree reader does not conclude they are missing |

---

## 5. Dependencies This Session Inherits And Does Not Discharge

Nothing in this table is affected by the work in this package. Each is listed because the invariant set cannot be completed, implemented or verified while it stands.

| ID | Dependency | Lane | Severity | Owner | What It Blocks Here |
|---|---|---|---|---|---|
| `RISK-C02` / `IV-06` | Deterministic movement attempt identity — rank 2 | **A** build / **D** severity | **BLOCKING** | **Boss** | `MTI-15`, `MTI-31`, `MTI-41`; `MTA-12`; six enforcement points; handoff element 15 |
| `GAP-FS-08` / `CN-36` | Migration and replay provenance reference — rank 3 | **A** | **BLOCKING** | Migration + Inventory | `MTI-06`, `MTI-42`; `MTA-04`, `MTA-21`; handoff element 14; `L10-01`, `L10-09`, `L10-10` |
| Privileged-bypass path audit | Started and never completed (`L9-01`) | **A** | **BLOCKING** for `L9-01` | Inventory + SaaS Foundation | `MTI-18` is unverifiable until the path set is enumerated. `MTP-03` cannot be scored for completeness |
| `RISK-U01` / `U-01` | Warehouse- and operation-level authorization scope | **D** then **A** | **BLOCKING** for `L9-03` | **Boss** | `MTI-D-02`; the `AUTH` shape at `04` §7 |
| `GAP-MD-14` / `SAAS-04` | Provisioning-template regeneration, switch-off guards, versioning | **D** then **A** | MATERIAL | Boss / product | `MTI-D-03`; `MTI-37`; `L9-04` boundary half |
| `JT-01` | Which concept owns valuation policy — **NOT DECIDABLE** | **E** | **BLOCKING** | Joint | `MTI-16`, `MTI-11` category facet; `L9-06` value half; `MTA-18`; `L8-15` policy version |
| `JT-10` | Inter-company transfer treatment | **E** | **BLOCKING** for `XCR-01` | Joint | The principal `MTI-22` register entry; `MTI-44`; `MTP-28`; `MTA-22` |
| `GAP-FS-07` | Cross-company transfer path **never traced end to end** | **B** | **BLOCKING** | Joint / Inventory | Same as `JT-10`; `L9-06` |
| `GAP-MD-09` | Consignment and ownership policy | **B** | MATERIAL | Joint | `MTI-16`, `HF-CTX-09`, `MTI-F-02`, `MTA-23` |
| `GAP-MD-29` | PDPA scope for Inventory documents — **zero coverage anywhere** | **D** | MATERIAL, trending BLOCKING | Boss + Legal | `MTI-D-05`; `MTI-49`; `MTA-24` |
| `GAP-FS-11` / `GAP-MD-30` | Thai user validation — 0 of 78 validated | **C** | **BLOCKING** for user-facing design | **Boss to commission** | `L9-07`, `L9-08`; `MTI-D-06`; `MTI-F-05` compensating control; every label in this package is unvalidated |
| `TH-HOLD-01` .. `TH-HOLD-09` | Thai statutory holds, including `TH-HOLD-06` branch-versus-warehouse | **C** statutory | `HOLD / EVIDENCE REQUIRED` | **Accounting-Tax track** | `MTI-07`; `L9-07`; the branch dimension at `04` §7. **No statutory claim is made by this session** |
| `C-05` / `RISK-C05` | Clean-room containment — exposure confirmed live by the review | **D** | **BLOCKING** for downstream reliance | **Boss only** | Reliance on this package inherits the same lock. See `12` §2 |
| `U-07` / `RISK-U07` | Two competing 9 Veto Council charters | **D** | **BLOCKING** for challenge finality | **Boss only** | This session's `12` verdict inherits the same conditionality |
| `R4-F-06`, `R4-F-09`, `R4-F-22` | The three structural findings this design responds to | **A** | **BLOCKING** | Inventory + SaaS Foundation | **All three remain open.** Design responds to them; only implementation and verification can close them |
| `R4-F-11` | Nested reordering rule overlap within a company | **A** | MATERIAL | Inventory | Explicitly **not** addressed by `MTI-14`. `MTA-14` |
| `R4-F-07` | Available quantity display-clamped at zero | **A** | MATERIAL | Inventory | `MTA-07` — the display contract decision is outside this authorization |
| `R4-F-24` (kind half) | Location kind assigned by name-matching at migration | **A** | MATERIAL | Migration | `MTI-42` covers context, **not** the financial-meaning attribute |
| `C-04` / `N-CONC-01`, `N-A13-01` | Two reachable leads, unfollowed | **A** | CONFLICTING | Team A / Track 07 | `REV-F-01`. Not read by this session either |
| `REV-F-03`, `REV-F-04` | Lane vocabulary collision; open-item roll-up not reconstructable | **D** | MATERIAL | Boss / PMO | Register hygiene; unchanged |

---

## 6. Roll-Up

| Measure | Result |
|---|---:|
| New findings raised | **6** — `MTI-F-01` .. `MTI-F-06` |
| New decision blockers raised | **6** — `MTI-D-01` .. `MTI-D-06` |
| Evidence notes raised | **2** |
| **Total new items** | **14** |
| New items by lane | A 5 · A/B 2 · A/C 1 · D 5 · C-then-A 1 |
| Inherited dependencies listed | 20 |
| Inherited dependencies **discharged** | **0** |
| Prior items closed | **0** |
| Carried identifiers renumbered or retired | **0** |

**No open-item roll-up total is asserted by this session.** `REV-F-04` records that the 92 figure is not independently reconstructable and that no open-item crosswalk exists. Adding fourteen items to a total that cannot be reconstructed would produce a number that looks precise and is not. The fourteen new items are enumerated exactly; the roll-up awaits the crosswalk PMO has been asked to publish.

---

## 7. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
