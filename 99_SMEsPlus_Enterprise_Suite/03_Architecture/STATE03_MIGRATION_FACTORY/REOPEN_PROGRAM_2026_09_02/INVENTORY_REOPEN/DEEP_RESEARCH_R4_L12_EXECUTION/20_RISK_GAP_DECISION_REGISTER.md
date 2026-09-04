# [SMEPLUS-26-09-04-INV-DEEP-RESEARCH-R4-L12-001]
# 20 — Risk / Gap / Decision Register

Control Level: `/L9999.9999`
Status: `OPEN-ITEM REGISTER — NOTHING BELOW IS CLOSED BY THIS SESSION`

---

## 1. Register Rules

- **Nothing in this register is closed by R4.** Naming an owner is not authorization. Recording new evidence against an item is not closure.
- Prior identifiers are carried **unchanged**. R4 adds its own items under new prefixes so that lineage stays unambiguous: `R4-F-*` for findings, `R4-D-*` for corrections and disclosures, `R4-Q-*` for questions raised for Thai business input, `R4-N-*` for naming conflicts.
- Severity vocabulary carried from prior rounds: `BLOCKING`, `MATERIAL`, `CARRIED`, `WATCH`, `HOLD / EVIDENCE REQUIRED`.
- Lane vocabulary carried from the v2.0 decision matrix: **A** proceeds now, unaffected · **B** proceeds now, valuation-adjacent but not gated · **C** waits for Accounting COGS Gap evidence · **D** waits for a Boss-only ruling independent of COGS evidence.

---

## 2. Carried Register — Prior Items

R4 re-read the full prior register and confirms its state. **60 items entering, 60 items still open, 0 closed by R4.**

| Category | Count entering | State after R4 |
|---|---:|---|
| Clean-room and provenance risks (`RISK-C05`, `RISK-C05B`, `RISK-CR-01`, `RISK-U07`, `RISK-CR-02`) | 5 | All open. `RISK-CR-02` (single-session synthesis, no independent verification) applies to R4 itself and is re-raised by AAS+ Tracks 01 and 08. |
| Carried conflicts and unknowns (`RISK-C01`, `-C02`, `-C03`, `RISK-U01`, `-U02`, `-U03`, `RISK-G1G2G3`, `RISK-G5`, `RISK-G7`, `RISK-N-A12-01`) | 10 | All open. R4 adds new evidence to `RISK-C02` and `RISK-U03`; arbitrates neither. |
| Joint decisions `JT-01` .. `JT-12` | 12 | All open. Three (`JT-01`, `JT-04`, `JT-05`) now formally **NOT DECIDABLE**. |
| Design gaps `GAP-FS-01` .. `GAP-FS-23` | 23 | All open. Six have their **evidence basis materially improved** by R4 — see §3. |
| Thai statutory holds `TH-HOLD-01` .. `TH-HOLD-09` | 9 | All `HOLD / EVIDENCE REQUIRED`, routed to the Accounting-Tax track. R4 makes no Thai statutory claim. |
| New in v2.0 (`RISK-COGS-01`) | 1 | **Factually superseded** — see `R4-D-01`. Remains formally open pending Boss acknowledgement of the correction. |
| Menu Deep Challenge gaps `GAP-MD-01` .. `GAP-MD-31` | 31 | All open. Six upgraded from *no evidence* to *first-hand structural evidence* — see §3. |
| Carried unknowns `U-01` .. `U-07` and conflicts `C-01` .. `C-05` | as above | All open. |

**Total prior open items: 60 (v2.0 roll-up basis). Closed by R4: 0.**

---

## 3. Items Whose Evidence Basis R4 Materially Improved

These are **not closures.** Each item remains open. What changed is the quality of evidence beneath it, which is what a Deep Research round is for.

| Item | Was | Now | Basis |
|---|---|---|---|
| `GAP-FS-20` / `GAP-MD-08` | Variants and attributes: no evidence in any round | First-hand field, configuration and variant-creation-mode evidence | `INV-M08`, `INV-M25` |
| `GAP-MD-16` | Storage categories: never studied | First-hand capacity and mixing-constraint structure | `INV-M22` |
| `GAP-MD-17` | Put-away rules: never studied | First-hand structure; category dual-ownership coupling **confirmed** | `INV-M23` |
| `GAP-MD-18` | Packaging: no packaging model found in the source examined | **Corrected** — a packaging structure with a contained base quantity does exist in the target generation | `INV-M26`, `R4-D-02` |
| `GAP-MD-19` | Barcode formats: never studied | First-hand structure; plain and structured-standard nomenclatures both exist | `INV-M28` |
| `GAP-FS-02` | Is product category acceptable as owner of both valuation policy and put-away | Coupling **confirmed real** in the reference pattern; root cause identified as triple ownership | `R4-F-10` |
| `RISK-C02` / `IV-06` | Idempotency: contested severity | Now **contract-blocking** under a Boss-approved contract that did not exist when it was last argued | `R4-F-16` |
| `RISK-U03` | Multi-tenant invariant set does not exist | Two **specific structural mechanisms** identified by which isolation can fail | `R4-F-06`, `R4-F-09` |
| `GAP-MD-25` / `GAP-FS-13` | Warehouse analysis measure set unevidenced | **Unchanged** — this remains the one genuinely evidence-thin menu | `INV-M15` |

---

## 4. New R4 Findings — `R4-F-01` .. `R4-F-25`

| ID | Finding | Severity | Lane | Owner |
|---|---|---|---|---|
| `R4-F-01` | Shortfall computation uses the greater of minimum and maximum; an inverted min/max entry is silently accepted | MATERIAL | A | Inventory |
| `R4-F-02` | Reference pattern treats the count as an attribute of the balance, not a document with a lifecycle and approval state | MATERIAL | A | Inventory |
| `R4-F-03` | Scrap carries no salvage-value concept at all; salvage is original design work | MATERIAL | A scope / C value | Inventory + Joint |
| `R4-F-04` | Scrap has two states with no approval or rejection path; the mandated scrap approval control has no reference pattern | MATERIAL | A | Inventory |
| `R4-F-05` | Weight- and volume-based landed cost allocation silently distorts when those product attributes are unmaintained | MATERIAL | C | Inventory + Joint |
| `R4-F-06` | Traceable identity uniqueness is scoped to (identifier, product, company) with company-less identities possible | **BLOCKING** for multi-company | A | Inventory + SaaS Foundation |
| `R4-F-07` | Available quantity is display-clamped at zero while true on-hand can be negative | MATERIAL | A | Inventory |
| `R4-F-08` | Running balance differs by entry-sequence versus effective-date ordering; backdating is routine | MATERIAL | A | Inventory |
| `R4-F-09` | A location's company assignment is optional — the structural mechanism for cross-company visibility | **BLOCKING** for multi-company | A | Inventory + SaaS Foundation |
| `R4-F-10` | Product category simultaneously owns reporting, put-away and costing — root of `GAP-FS-02` / `JT-01` | MATERIAL | C | Joint |
| `R4-F-11` | Rule uniqueness is per (product, location, company) only; overlapping rules on nested locations each raise supply | MATERIAL | A | Inventory |
| `R4-F-12` | A misparsed structured barcode yields a plausible but wrong quantity silently | MATERIAL | A | Inventory |
| `R4-F-13` | Default unit-conversion rounding is upward; repeated conversion inflates quantity monotonically and silently | MATERIAL | A | Inventory |
| `R4-F-14` | Planning runs read a forecast that already includes in-progress supply, so a run is not reproducible without its own input snapshot | MATERIAL | A | Inventory |
| `R4-F-15` | The reference ERP supplies almost no approval infrastructure for the changes that most affect stock integrity; internal control is predominantly original design work | MATERIAL, trending BLOCKING for build | A | Inventory + Boss scope |
| `R4-F-16` | **Three of the sixteen Boss-mandated handoff elements are unsuppliable by Inventory, none for COGS reasons. No material handoff and no Boss-approved cross-proof scenario can be declared verified.** | **BLOCKING** | A | **Boss** |
| `R4-F-17` | On-hand, reserved and incoming all depend on one missing capability — movement identity — expressed three times | **BLOCKING** | A | **Boss** |
| `R4-F-18` | Financial neutrality of internal movement is protected only by configuration; no independent check exists | MATERIAL | A mechanism / C value | Inventory |
| `R4-F-19` | Every semantic reaches the user as an unvalidated Thai label | **BLOCKING** for user-facing design | A | **Boss to commission** |
| `R4-F-20` | Retroactive cost compensation is sequenced by record creation order, not effective date | MATERIAL | C | Joint — `L13-01` |
| `R4-F-21` | A Thai micro-SME may have two staff; a segregation model that cannot degrade gracefully will be bypassed | MATERIAL | A | Inventory + Thai validation |
| `R4-F-22` | Isolation must be proven on **derived** surfaces, not only stored records, because the most-used numbers are derived by design | MATERIAL | A | SaaS Foundation |
| `R4-F-23` | Migrating legacy batch identities without resolving company scope imports the collision surface in bulk | MATERIAL | A | Migration |
| `R4-F-24` | Assigning location kinds by name-matching at migration silently mis-states the financial meaning of historical movements | MATERIAL | A | Migration |
| `R4-F-25` | Quantity-side cutover reconciliation is achievable independently of the value side — **opportunity, not defect** | MATERIAL | A | Inventory |

**25 new findings. 19 of 25 are Lane A — not COGS-gated.**

---

## 5. R4 Corrections And Disclosures — `R4-D-01` .. `R4-D-05`

| ID | Item | Content |
|---|---|---|
| `R4-D-01` | **Correction to `RISK-COGS-01`** | The v2.0 register recorded the COGS Deep Research as not executed, with no commit, branch or archived record existing. That is factually superseded: the package exists at commit `a959327938cc1168c93e1e4a89bd1dcf846871c5` with 37 deliverables. The dependency is **not** lifted — the executed package closes none of the twelve Joint decisions and its own terminal state is a `HOLD`. What changes is the reason Inventory is blocked, and therefore the remedy. Commissioning the research again would achieve nothing. |
| `R4-D-02` | **Correction to the packaging finding** | An earlier round recorded that no packaging model existed in the source it examined. A packaging structure carrying a contained base quantity **does exist** in the target generation. `GAP-MD-18` remains open but its premise is corrected. |
| `R4-D-03` | **Disclosure — branch base** | R4 branched from the prompt branch rather than the canonical branch, because the mandatory sources live there. Two binding Boss controls found only on the canonical branch — the 16-element handoff contract (`d9e845e`) and the 22-scenario baseline (`296b495`) — were read by direct commit citation. No merge was performed. Raised by AAS+ Track 01 and recorded here rather than left implicit. |
| `R4-D-04` | **Disclosure — charter conditionality** | This session's L12 challenge follows the canonical 9 Veto Council roster. `RISK-U07` / `U-07` records two competing definitions, both claiming approval. If Boss rules the other governs, the L12 challenge must be re-run. |
| `R4-D-05` | **Disclosure — two reachable leads not followed** | Primary-source access was available and was used for thirteen findings, but two specific named leads were not closed: `C-04` / `N-CONC-01` reservation locking sufficiency, and `N-A13-01` the unread manual-override path onto the derived available quantity. R4 prioritised breadth across 29 menus and 12 levels. AAS+ Track 07 raises this as a fair criticism and R4 accepts it without qualification. |

---

## 6. Questions And Naming Conflicts Raised By R4

| ID | Item | Routed to |
|---|---|---|
| `R4-Q-01` | What reason taxonomy should adjustments and scrap use — this is what keeps non-sale reductions distinguishable from sales, so it is not cosmetic | Thai business validation |
| `R4-Q-02` | Are `INV-M12` and `INV-M13` comprehensible as two menus, or should they be one view with a state filter | Thai business validation |
| `R4-Q-03` | Which structured barcode formats are actually in use by Thai suppliers | Thai field validation |
| `R4-N-6` | Thai candidate strings diverge between three prior registers for five menus; the naming register is the designated authority but the divergence is unsettled | Thai naming panel |

---

## 7. Register Roll-Up

| Category | Count |
|---|---:|
| Prior open items entering R4 | 60 |
| Prior items closed by R4 | **0** |
| Prior items with materially improved evidence basis | 9 |
| Prior items factually corrected | 2 (`R4-D-01`, `R4-D-02`) |
| New R4 findings | 25 |
| New R4 disclosures | 3 |
| New R4 questions for Thai input | 3 |
| New R4 naming conflicts | 1 |
| L13+ escalated items | 6 |
| **Total open items after R4** | **92** |
| `BLOCKING` after R4 | 25 (21 carried + 4 new: `R4-F-06`, `R4-F-09`, `R4-F-16`, `R4-F-17`, `R4-F-19` — `R4-F-19` counted once) |
| Items in Lane A — actionable without any COGS decision | **19 of the 25 new findings, plus 4 of 6 escalations** |

The register grew. That is the expected outcome of a Deep Research round that had primary-source access for the first time, and it is not presented as progress in itself. The useful measure is the lane distribution: **the majority of what R4 found is not waiting on Accounting.**

---

## 8. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
