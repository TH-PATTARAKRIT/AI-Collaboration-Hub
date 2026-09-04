# P01 — CONTRADICTION REGISTER

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

Per `EC-05`, every material contradiction records the competing claims, the evidence for each,
the scope of each evidence source, the kind of contradiction, a disposition and the downstream
impact. Nothing here is settled by averaging or by counting opinions.

---

## `CONTRA-P01-01` — correction by deletion

| | |
|---|---|
| **Claim A** | A posted accounting fact is immutable; corrections are made by reversal so that history is preserved. This is the project's own rule (`§2.13`). |
| **Claim B** | Resetting a posted vendor bill to draft, or cancelling it, **deletes** the interim and price-difference journal items. Duplicating an entry strips them. Resetting also deletes still-draft assets created from the bill. |
| **Evidence A** | Session directive `§2.13`. |
| **Evidence B** | `EV-P01-11`, `EV-P01-12`, `EV-P01-19`. Scope: `R1`, the reset and cancel paths of the entry model as extended by the valuation module, and the asset module's extension of the same paths. |
| **Kind** | **Semantic.** Not a version artefact, not data-specific. |
| **Disposition** | **CONTRADICTED — the reference behaviour is rejected as a transfer candidate.** It is recorded as learning about what the benchmark does, never as a requirement. |
| **Downstream impact** | A clean-room design must make the reversal path the only correction path, with no privileged deletion of derived journal items. Reviewers of any future P01 design should treat the presence of a delete-on-draft path as an automatic finding. |

---

## `CONTRA-P01-02` — two owners for the received-not-billed obligation

| | |
|---|---|
| **Claim A** | The obligation for goods received but not yet billed is represented by the balance on the goods-received clearing account, raised at receipt and discharged at the bill. |
| **Claim B** | The obligation is represented by an accrual entry raised **from the order**, sized from received-not-billed quantity, and automatically reversed. |
| **Evidence A** | `EV-P01-07`, `EV-P01-09`, `EV-P01-10`. Scope `R1`. |
| **Evidence B** | `EV-P01-16`. Scope `R1`. |
| **Kind** | **Control-specific.** Both mechanisms exist and are reachable. Path A is automatic and applies only to storable, continuously-valued items; path B is manual and applies to any item. |
| **Additional finding** | Nothing observed prevents both from being live for the same quantity at the same date, and path B **leaves no record on the order** (`EV-P01-17`), so the overlap is not visible from the source document. **The simultaneity was not runtime-confirmed** — the claim that both *paths exist* is FACT VERIFIED; the claim that they *can overlap* is SUPPORTED INTERPRETATION. |
| **Disposition** | **DESIGN DECISION REQUIRED AT FINAL GATE.** `§2.7` permits one canonical event owner. |
| **Downstream impact** | `DEP-P01-05`. Whichever is chosen, the other must be demoted to a reporting view with no ledger effect. |

---

## `CONTRA-P01-03` — the two reference generations disagree about the process itself

| | |
|---|---|
| **Claim A** | Purchases bridge from receipt to bill through a goods-received clearing account, with a price-difference engine reconciling layers. (`R1`) |
| **Claim B** | There is no clearing account. Valuation resolves to a valuation account and a variation account, and the price-difference engine does not exist in the corresponding place. (`R3`) |
| **Evidence A** | `EV-P01-07`, `EV-P01-09`, `EV-P01-13`. Scope `R1`. |
| **Evidence B** | `EV-P01-24` — whole-root search of `R3`, all file types: the clearing-account resolution keys have **no runtime definition or use**; the 19 residual occurrences of the category field name are 16 stale translation catalogues and 3 test files. The replacement key appears in 127 `R3` files and 0 `R1` files. `EV-P01-25` — file-level line counts and definition-list comparison. |
| **Kind** | **Version-specific, and structural.** This is not a refactor of one algorithm; the account model of the receipt-to-bill bridge is different. |
| **Disposition** | **UNRESOLVED — `DEP-P01-01` — BOSS DECISION REQUIRED.** P01 cannot choose the benchmark generation. |
| **Downstream impact** | Severe and wide. Any design that inherits the clearing-account model inherits a pattern the benchmark's own later generation abandoned. **This independently reproduces, in the liability bridge, the instability the COGS track already recorded in the valuation pattern** — two independent areas, same failure mode. It raises the question whether the reference system is a stable benchmark for *this process* at all. |

---

## `CONTRA-P01-04` — asset classification and inventory clearing write the same field

| | |
|---|---|
| **Claim A** | The capital-asset decision is made at bill posting, from the asset flag on the bill line's ledger account. |
| **Claim B** | The bill line's ledger account is silently replaced by the goods-received clearing account whenever the item is storable, continuously valued, and the company runs the clearing model. |
| **Evidence A** | `EV-P01-18`. Scope `R1`. |
| **Evidence B** | `EV-P01-09`. Scope `R1`. |
| **Kind** | **Implementation-specific composition.** Each mechanism is verified; their interaction is inferred. |
| **Disposition** | **UNRESOLVED — RUNTIME EVIDENCE REQUIRED.** The composition has **not** been executed or observed. Recording it as a defect without that evidence would be exactly the over-reach the negative-claim standard forbids. |
| **Downstream impact** | If confirmed: a storable item bought as a capital asset cannot reach its asset account through the ordinary path, and conversely a clearing account carrying the asset flag would generate assets from clearing lines. Either way the classification decision does not belong on a field another mechanism overwrites. |

---

## `CONTRA-P01-05` — mutation authority and financial-effect scope diverge

| | |
|---|---|
| **Claim A** | Company-scoped accounting values held on tenant-scoped catalogue objects correctly express `OWNERSHIP SCOPE ≠ FINANCIAL SCOPE`. |
| **Claim B** | The right to mutate follows the tenant-scoped object, so a tenant-scope actor can change which accounts a specific company's purchases post to. |
| **Evidence A and B** | The same field declarations: every account role P01 uses is a company-dependent value on an object with no company field of its own. Scope `R1`, field declarations only. See `P01_SCOPE_OWNERSHIP_MATRIX.md` §3. |
| **Kind** | **Scope-semantic.** A guard constraining the chosen account to the correct company is declared on those fields; **whether it executes is not established here** — class **B**, scope: the declarations, not the access rules. |
| **Disposition** | **SUPPORTED INTERPRETATION**, authority question open. Raised by the corrected constitution; under the superseded reading it would have been mis-reported as an isolation gap (`REV-P01-01`). |
| **Downstream impact** | A clean-room design must decide **which scope may mutate a company-scoped accounting value**, independently of which scope owns the object carrying it. |

---

## `CONTRA-P01-06` — a financial outcome that depends on a non-accounting record

| | |
|---|---|
| **Claim A** | Which receipt a bill line settles is determined by the accounting documents. |
| **Claim B** | It is determined by replaying history in the order recorded by **the audit-log tracking rows of each entry's status field**, falling back to the record's creation timestamp. |
| **Evidence B** | `EV-P01-13`. Scope `R1`. |
| **Kind** | **Semantic, and migration-critical.** |
| **Disposition** | **CONTRADICTED — rejected as a transfer candidate.** |
| **Downstream impact** | Three consequences, each independently sufficient to reject the pattern: the outcome depends on data no accounting control protects and that is routinely purged; migrated documents carry none of it and therefore all fall to the fallback branch; and two systems holding identical documents can compute different results. **A migration that reproduces the documents faithfully can still fail to reproduce the valuation.** |

---

## Summary of dispositions

| Disposition | Count | IDs |
|---|---|---|
| CONTRADICTED — rejected as transfer candidate | 2 | `CONTRA-P01-01`, `CONTRA-P01-06` |
| DESIGN DECISION REQUIRED AT FINAL GATE | 1 | `CONTRA-P01-02` |
| UNRESOLVED — BOSS DECISION REQUIRED | 1 | `CONTRA-P01-03` |
| UNRESOLVED — RUNTIME EVIDENCE REQUIRED | 1 | `CONTRA-P01-04` |
| SUPPORTED INTERPRETATION, authority question open | 1 | `CONTRA-P01-05` |

**Zero contradictions are closed by this session.** That is the honest count.

---

# ADDENDUM — CONTRADICTIONS ADDED AFTER THE EXPERT CHALLENGE AND THE DEPLOYED-SCHEMA EVIDENCE

## `CONTRA-P01-07` — the deployed schema disagrees with the source this package analysed

| | |
|---|---|
| **Claim A** | Procure-to-pay bridges receipt to bill through a goods-received clearing account, with valuation layers corrected by a price-difference engine. Traced in full from the v18 source. |
| **Claim B** | The two readable **deployed v19 databases have no clearing-account column on the item category and no valuation-layer table at all.** |
| **Evidence B** | `P01_DEPLOYED_SCHEMA_EVIDENCE.md` §3. Class **A within those two databases**, licensed because the sibling account properties on the same table *are* present, so a column probe is the right instrument. |
| **Kind** | **Version-specific and structural, now confirmed at the deployed level** — no longer only a source-tree divergence. |
| **Disposition** | **UNRESOLVED — `DEP-P01-01` — BOSS DECISION REQUIRED**, and materially escalated: this is no longer "two source trees differ" but "the mechanism analysed has no physical structure to run on in two of the three readable live databases". |
| **Downstream impact** | Supersedes `CONTRA-P01-03` in severity while leaving it standing. Any P01 design built on the clearing-account bridge would be modelled on something the deployed v19 line does not have. |

## `CONTRA-P01-08` — a period lock that relocates instead of refusing

| | |
|---|---|
| **Claim A** | A period lock prevents posting into a closed period. |
| **Claim B** | On a lock violation the posting routine **rewrites the entry's date** to a permitted date and posts it. |
| **Evidence B** | `EV-P01-48`, re-derived by this session. |
| **Kind** | **Semantic.** Present in the searched generation. |
| **Disposition** | **CONTRADICTED — rejected as a transfer candidate.** |
| **Downstream impact** | Cut-off testing on the entry's own date is self-confirming: the date inspected is the date the system chose to make the test pass. Any P01 or period-close control that relies on entry dates alone is measuring an artefact. A clean-room design must refuse, not relocate. |

## `CONTRA-P01-09` — a control that compounds the amount it is meant to net

| | |
|---|---|
| **Claim A** | Withholding already taken on earlier partial payments is netted off the amount to withhold on the next one. |
| **Claim B** | The netting term is computed as *debit − credit*. On a vendor payment the withholding write-off is a credit, so the term is negative and the subtraction **increases** the amount withheld on each subsequent payment. |
| **Evidence B** | `EV-P01-52`, re-derived by this session; the arithmetic is as the expert stated, and the defect is confined to the purchase side. |
| **Kind** | **Implementation.** In the project's own custom layer, not in the base capability. |
| **Disposition** | **CONTRADICTED — the custom implementation does not do what its own comment says it does.** |
| **Downstream impact** | Over-withholding grows with the number of partial payments. Whether the resulting amounts are lawful is `HOLD — STATUTORY EVIDENCE REQUIRED`; that the code does not match its stated intent is settled. |

## `CONTRA-P01-10` — two shipped copies classify the same fact onto opposite statutory forms

| | |
|---|---|
| **Claim A** | A corporate counterparty maps to one withholding certificate form. |
| **Claim B** | A corporate counterparty maps to the **other** form. |
| **Evidence** | Both, from **the same file at the same two lines in two shipped copies of the same module**. `EV-P01-53`, read directly in both by this session. |
| **Kind** | **Data-specific and deployment-specific.** Mutually exclusive; both cannot be right. |
| **Disposition** | **UNRESOLVED on two axes.** Which copy is deployed is `DEP-P01-01`. Which mapping is correct is `DEP-P01-04` — `HOLD — STATUTORY EVIDENCE REQUIRED`. |
| **Downstream impact** | **At least one shipped copy misclassifies every certificate it produces.** This is the clearest single demonstration in the session of why "which copy is deployed" is a gating question and not an administrative one. |

## `CONTRA-P01-11` — deleting a commitment line silently erases both its downstream traces

| | |
|---|---|
| **Claim A** | The chain from order to receipt to bill is referentially protected. |
| **Claim B** | In the deployed schemas of **both** generations, the bill-line→order-line and receipt-movement→order-line foreign keys are `ON DELETE SET NULL`. |
| **Evidence B** | `P01_DEPLOYED_SCHEMA_EVIDENCE.md` §5, read from the extracted schemas. |
| **Kind** | **Physical.** Not version-specific. |
| **Disposition** | **CONTRADICTED — Claim A is false.** |
| **Downstream impact** | Deleting one order line erases the bill's origin and the receipt's purpose in a single operation, leaving both documents present and internally valid. This is the physical counterpart of the traceability gap recorded in `P01_SOURCE_TO_AP_TRACE.md` §6. |

---

## Revised summary of dispositions

| Disposition | Count | IDs |
|---|---|---|
| CONTRADICTED — rejected as transfer candidate | 4 | `CONTRA-P01-01`, `-06`, `-08`, `-11` |
| CONTRADICTED — implementation does not match stated intent | 1 | `CONTRA-P01-09` |
| DESIGN DECISION REQUIRED AT FINAL GATE | 1 | `CONTRA-P01-02` |
| UNRESOLVED — BOSS DECISION REQUIRED | 2 | `CONTRA-P01-03`, `CONTRA-P01-07` |
| UNRESOLVED — RUNTIME EVIDENCE REQUIRED | 1 | `CONTRA-P01-04` |
| UNRESOLVED — statutory **and** deployment axes | 1 | `CONTRA-P01-10` |
| SUPPORTED INTERPRETATION, authority question open | 1 | `CONTRA-P01-05` |

**Eleven contradictions. Zero closed by this session.** The count rose during the session; it
did not converge.
