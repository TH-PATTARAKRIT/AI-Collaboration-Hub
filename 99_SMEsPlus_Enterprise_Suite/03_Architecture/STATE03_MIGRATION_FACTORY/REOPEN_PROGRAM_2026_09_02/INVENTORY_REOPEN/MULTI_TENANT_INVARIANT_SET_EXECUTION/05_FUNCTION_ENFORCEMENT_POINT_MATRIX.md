# [SMEPLUS-26-09-04-INV-MT-INVARIANT-SET-001]
# 05 — Function Enforcement Point Matrix

Control Level: `/L9999.9999`
Scope: `41 controlled Inventory functions (INV-F-01 .. INV-F-41) across 29 menus`
Status: `41 OF 41 FUNCTIONS GIVEN ENFORCEMENT POINTS — DESIGN / SPECIFICATION ONLY — NOT DEVELOPMENT FINAL GATE`

---

## 1. Why A Function Matrix Is Required

An invariant that is not attached to a function boundary is a wish. `RISK-U03` records that the invariant set does not exist; it does not follow that stating fifty invariants discharges it. The set is only usable if every place where the property could be broken is named.

The 41 functions and 29 menus are carried unchanged from `04_L3_FUNCTION_FORENSIC_REGISTER.md` and `14_MENU_COVERAGE_REGISTER_29_OF_29.md`. No function is renumbered and none is added.

---

## 2. Enforcement Point Classes

| Class | Name | What Must Happen | Governing Invariants |
|---|---|---|---|
| `EP-R` | **Resolve** | `CTX` is resolved at function entry from the declared anchor. If it cannot be resolved, the function fails and the failure is recorded. Never defaulted, never inferred | `MTI-01`, `MTI-04`, `MTI-05`, `MTI-20` |
| `EP-W` | **Write barrier** | The persistence boundary rejects any record whose `CTX` is absent, inconsistent with its anchor, or references another context outside the `MTI-22` register | `MTI-04`, `MTI-17`, `MTI-03` |
| `EP-Q` | **Query scope** | Every read is scoped to the caller's `AUTH` set **before** evaluation. Absence is indistinguishable from non-existence | `MTI-21`, `MTI-26`, `MTI-27` |
| `EP-A` | **Aggregate barrier** | No computation combines records from more than one `CTX` unless a Cross-Context Report Grant is in force and logged | `MTI-23`, `MTI-24`, `MTI-25` |
| `EP-X` | **Execution binding** | The run binds exactly one `CTX` and carries the authority it was scheduled under; a lapsed authority prevents execution | `MTI-29`, `MTI-30`, `MTI-31` |
| `EP-E` | **Event emission** | The act emits an immutable event carrying full `CTX`, actor, authority, physical date, entry date and evidence reference | `MTI-38`, `MTI-39`, `MTI-50` |
| `EP-H` | **Handoff carriage** | The emitted fact carries `CTX` **and** the attestation naming what guaranteed it | `MTI-43`, `MTI-45` |
| `EP-G` | **Governance gate** | A change to a context anchor is an approved, evidenced act with before and after values | `MTI-06`, `MTI-37`, `MTI-40` |

`EP-W` is the class that distinguishes this specification from prior rounds. Prior evidence records enforcement at the application layer with **no database-layer backstop**; `EP-W` is the requirement that the barrier exists beneath application code, so that a path nobody enumerated cannot bypass it.

---

## 3. Operations Functions (`INV-M01` .. `INV-M06`)

| Function | Menu | Enforcement Points | Principal Failure Mode If Absent |
|---|---|---|---|
| `INV-F-01` Compute replenishment shortfall | `M01`, `M06` | `EP-R` `EP-Q` `EP-A` `EP-X` | A shortfall computed over a location hierarchy spanning companies raises supply in the wrong company. The hierarchy walk is the leak surface |
| `INV-F-02` Convert a proposal into a supply action | `M01` | `EP-R` `EP-W` `EP-E` `EP-H` | A purchase raised in company A against company B's shortfall |
| `INV-F-03` Record a physical count | `M02` | `EP-R` `EP-Q` `EP-W` `EP-E` | A count sheet listing another company's locations; a counted quantity written to a foreign balance |
| `INV-F-04` Approve and apply an adjustment | `M02` | `EP-R` `EP-W` `EP-E` `EP-G` | Approval by an actor with no authority in the record's context. Compounded by the absence of any approval state at all (`R4-F-02`) |
| `INV-F-05` Create a stock operation | `M03` | `EP-R` `EP-W` `EP-E` | An operation whose source and destination resolve to different companies |
| `INV-F-06` Reserve stock against an operation | `M03` | `EP-R` `EP-W` | A reservation taken against another company's availability. Reservation is held on the balance, so the balance's context is the only protection |
| `INV-F-07` Validate a stock operation | `M03` | `EP-R` `EP-W` `EP-E` `EP-H` | **The single most consequential point in the module.** This is where a movement fact becomes done and where element 10 is either supplied with a guarantee or is not |
| `INV-F-08` Handle a shortfall — backorder or close | `M03` | `EP-R` `EP-W` `EP-E` | A backorder created in a context other than the original demand's |
| `INV-F-09` Handle over-delivery or over-receipt | `M03` | `EP-R` `EP-W` `EP-E` | An excess absorbed into a location outside the operation's company |
| `INV-F-10` Cancel before execution | `M03` | `EP-R` `EP-E` `EP-G` | A cancellation cascading across a context boundary. `C-01` symmetry is an unarbitrated conflict and is not resolved here |
| `INV-F-11` Return goods after execution | `M03` | `EP-R` `EP-W` `EP-E` `EP-H` | A return resolving to a different company from the original movement, breaking reversal-to-original linkage |
| `INV-F-12` Scrap goods | `M04` | `EP-R` `EP-W` `EP-E` `EP-G` | A write-off authorised by an actor outside the context. No approval state exists in the reference pattern (`R4-F-04`) |
| `INV-F-13` Recover salvage value | `M04` | `EP-R` `EP-W` `EP-E` | The concept has **no object at all** (`R4-F-03`). Enforcement points are stated for when it is originated; the value treatment is held |
| `INV-F-14` Allocate a landed cost | `M05` | `EP-R` `EP-W` `EP-A` `EP-H` | Allocation spreading cost across target lines in more than one company |
| `INV-F-15` Run the planning engine on demand | `M06` | `EP-R` `EP-X` `EP-A` | A manual run overlapping a scheduled run, and a run spanning contexts. `L6-10` records that nothing prevents overlap today |

---

## 4. Product And Master-Data Functions (`INV-M07` .. `INV-M09`, `INV-M25`)

| Function | Menu | Enforcement Points | Principal Failure Mode If Absent |
|---|---|---|---|
| `INV-F-16` Create or amend a product | `M07` | `EP-R` `EP-W` `EP-G` | Under `MTI-11` this writes tenant-level definitional data and company-level attachment in one act. The two halves need different barriers, and conflating them is the risk |
| `INV-F-17` Change stock-control classification while stock exists | `M07` | `EP-R` `EP-G` `EP-E` | A destructive, one-directional change applied tenant-wide while only one company's stock was considered |
| `INV-F-18` Generate or amend variants | `M08`, `M25` | `EP-R` `EP-W` `EP-G` | Attribute change after variants hold stock, in one company, affecting all. `GAP-FS-03` unresolved |
| `INV-F-19` Create a batch or serial identity | `M09` | `EP-R` `EP-W` `EP-Q` | **The `R4-F-06` point.** A company-less identity is created here, or a uniqueness message discloses another company's identity (`MTI-27`) |
| `INV-F-20` Amend or merge a batch identity | `M09` | `EP-R` `EP-W` `EP-E` `EP-G` | A merge spanning companies rewrites two companies' traceability chains in one act |

---

## 5. Reporting Functions (`INV-M10` .. `INV-M15`)

Every reporting function carries `EP-Q` and `EP-A` without exception. This is the `R4-F-22` requirement expressed at the function boundary.

| Function | Menu | Enforcement Points | Principal Failure Mode If Absent |
|---|---|---|---|
| `INV-F-21` Derive the current stock position | `M10`, `M11` | `EP-R` `EP-Q` `EP-A` | A derived on-hand summing rows from more than one company while every row is individually correct. Display clamping (`R4-F-07`) can mask the resulting discrepancy |
| `INV-F-22` Produce movement history | `M12` | `EP-Q` `EP-A` | A stock card containing another company's movements. The stock card is the document a Thai auditor asks for |
| `INV-F-23` Produce the valuation position | `M14` | `EP-Q` `EP-A` | Cross-company value aggregation. **All conclusions `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`** |
| `INV-F-24` Produce warehouse analytics | `M15` | `EP-Q` `EP-A` | Analytic measures crossing a boundary invisibly, since an analytic surface rarely shows its own scope |
| `INV-F-25` Export a report | `M12`, `M14`, `M15` | `EP-Q` `EP-A` `EP-E` | **An export is the highest-consequence leak surface**: it leaves the system, it is not re-scoped on arrival, and it is routinely shared. The export must carry its `CTX` scope and the export act must be evented |

---

## 6. Configuration Functions (`INV-M16` .. `INV-M29`)

Configuration functions are where a context anchor changes, so `EP-G` is near-universal here.

| Function | Menu | Enforcement Points | Principal Failure Mode If Absent |
|---|---|---|---|
| `INV-F-26` Change a capability switch | `M16` | `EP-R` `EP-G` `EP-E` | A switch changed at platform scope taking effect across tenants, or retroactively |
| `INV-F-27` Create or restructure a warehouse | `M17` | `EP-R` `EP-W` `EP-G` `EP-E` | **The `SAAS-04` regeneration point.** Re-derivation of operation types, locations and routes is where company-less derived records are produced in bulk. `MTI-35` and `MTI-04` are the defences |
| `INV-F-28` Create or change a location, including its kind | `M18` | `EP-R` `EP-W` `EP-G` `EP-E` | **The `R4-F-09` point.** A location created without a company, or re-parented under a warehouse in another company, or its kind changed so completed movements are re-interpreted |
| `INV-F-29` Change a supply route or rule | `M19`, `M20` | `EP-R` `EP-W` `EP-G` | A rule attached to a route in another company. The reference pattern already rejects this and it is adopted as `MTI-10` |
| `INV-F-30` Change an operation type, including numbering | `M21` | `EP-R` `EP-W` `EP-G` `EP-E` | Numbering continuity broken, or a sequence shared across companies. `TH-HOLD-09` held |
| `INV-F-31` Define storage constraints | `M22` | `EP-R` `EP-W` `EP-G` | Constraints referencing locations in another company |
| `INV-F-32` Suggest and override a put-away destination | `M23` | `EP-R` `EP-Q` `EP-W` `EP-E` | A suggested or manually overridden destination outside the source's company. The override must be an evented act |
| `INV-F-33` Assign or change a product category | `M24` | `EP-R` `EP-G` `EP-E` | The category owns a costing facet that is company-scoped and a structural facet that may be tenant-scoped (`R4-F-10`). A single act changing both across companies is the exposure |
| `INV-F-34` Define a packaging | `M26` | `EP-R` `EP-W` `EP-G` | A contained-quantity change re-interpreting history; and a handling unit spanning companies (`MTI-13`) |
| `INV-F-35` Set or maintain a reordering rule | `M27` | `EP-R` `EP-W` `EP-G` | A rule acting on a location in another company. **Within-company nested overlap (`R4-F-11`) is not addressed by any enforcement point here** and remains open |
| `INV-F-36` Define barcode interpretation | `M28` | `EP-R` `EP-Q` `EP-G` | A scan resolving an identity outside the caller's context, which turns a shared nomenclature into a cross-context lookup |
| `INV-F-37` Define or change a unit conversion | `M29` | `EP-R` `EP-G` `EP-E` | A tenant-level factor change altering historical quantity in every company at once |

---

## 7. Cross-Cutting Functions

These four apply to every menu and carry the heaviest obligations.

| Function | Scope | Enforcement Points | Treatment |
|---|---|---|---|
| `INV-F-38` Enforce the period guard | All operational menus | `EP-R` `EP-G` `EP-E` | The lock date is supplied per company by the Accounting side, so the guard is inherently context-scoped. The **exception grant** must carry `CTX` as well as grantor, reason and expiry. The global unscoped bypass recorded at `G-2` is rejected, consistent with the settled v1.0 position and with `MTI-18` |
| `INV-F-39` Emit a fact to Accounting | All value-bearing functions | `EP-R` `EP-H` `EP-E` | **This is where handoff element 10 is supplied or is not.** The fact carries `CTX` plus the `MTI-43` attestation. Elements 4 and 7 remain `HOLD - ACCOUNTING COGS GAP EVIDENCE REQUIRED`; elements 14 and 15 remain unsuppliable pending ranks 3 and 2 |
| `INV-F-40` Correct a completed fact | All operational menus | `EP-R` `EP-W` `EP-E` `EP-H` | A correction resolves to the **same `CTX`** as the original and links to it. A correction that changes context is prohibited outright — it is a migration act, not a correction (`MTI-06`) |
| `INV-F-41` Establish opening balances at cutover | `M02`, migration | `EP-R` `EP-W` `EP-G` `EP-E` | **The highest-risk point in the matrix.** Bulk creation with `CTX` assigned explicitly and evidenced, never inferred (`MTI-42`). Prior evidence names the opening balance the highest fabrication-risk point in the whole Inventory scope. Quantity half is Inventory-owned; value half is held; provenance is `GAP-FS-08`, rank 3 |

---

## 8. Enforcement Point Coverage Result

| Measure | Result |
|---|---:|
| Controlled functions in scope | 41 |
| Functions given enforcement points | **41** |
| Functions carrying `EP-R` | 37 — the four pure-reporting functions carry `EP-Q` instead, since a query resolves the **caller's** authorized scope rather than a record's anchor |
| Functions carrying `EP-W` | 26 |
| Functions carrying `EP-Q` | 10 |
| Functions carrying `EP-A` | 8 |
| Functions carrying `EP-X` | 2 |
| Functions carrying `EP-E` | 25 |
| Functions carrying `EP-H` | 6 |
| Functions carrying `EP-G` | 20 |
| Functions where a named prior finding lands directly | 9 — `INV-F-04`, `-07`, `-12`, `-15`, `-19`, `-27`, `-28`, `-35`, `-41` |
| Functions where an enforcement point is specified but **not exercisable** without rank 2 or rank 3 | 6 — `INV-F-07`, `-11`, `-15`, `-39`, `-40`, `-41` |
| Functions closed by this matrix | **0** |

---

## 9. What This Matrix Does Not Do

| Not done | Why |
|---|---|
| It does not say **how** any enforcement point is implemented | Implementation is out of scope. `EP-W` names an obligation, not a mechanism |
| It does not enumerate privileged paths | The bypass-path audit was started and never completed (`L9-01`). Until it is, `EP-W` coverage cannot be asserted as complete |
| It does not resolve the within-company reordering overlap | `R4-F-11` is a hierarchy-uniqueness item, Lane A, outside this authorization |
| It does not supply the idempotency identity that six functions need | `RISK-C02`, rank 2, not in this authorization |
| It does not verify that any function currently satisfies any point | There is nothing to verify against. Verification requires an implementation |

---

## 10. Non-Authorization Lock

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
