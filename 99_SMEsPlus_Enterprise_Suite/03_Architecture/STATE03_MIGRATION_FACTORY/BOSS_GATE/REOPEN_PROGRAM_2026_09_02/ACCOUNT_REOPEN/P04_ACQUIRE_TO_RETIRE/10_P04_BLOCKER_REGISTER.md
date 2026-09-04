# 10 — P04 BLOCKER REGISTER

Layer: **2 — audit quarantine**.

Inherited blockers are carried at their prior state and **not re-derived**.
New blockers are numbered `P04-B-nn`. Every row states **what closes it**.

---

## 1. Inherited — open (4)

| ID | Statement | Status | Closes on |
|----|-----------|--------|-----------|
| **BLK-01** | Which day convention the live asset population actually uses | HOLD — RUNTIME REQUIRED | One grouped count over all 280 records, plus the provenance of the model export. Blocks **migration**, not design |
| **BLK-02** | Whether several assets share one machine record | HOLD — RUNTIME REQUIRED | Two counts: assets with the link populated; machine records referenced by more than one asset. Blocks **per-machine costing**. A duplicated machine's cost pool doubles silently |
| **BLK-07** | The allocation denominator — normal capacity or actual hours | HOLD — BOSS DECISION | A Boss ruling. **The AAS+ veto's first limb.** Now with a **third option** — see `09` §3, `P04-BD-05` |
| **BLK-08** | Does maintenance split into planned and unplanned | HOLD — BOSS DECISION | A Boss ruling |

## 2. Inherited — closed, carried for lineage (4)

`BLK-03` absorption permitted → **closed, and exceeded**: TAS 2 ¶12 makes it
required. `BLK-04` off-balance presentation → **closed**: no such line exists in
the prescribed statutory forms. `BLK-05` unbounded internal usage → **closed by
`BD-01`**. `BLK-06` where unabsorbed depreciation goes → **closed by `BD-02`**,
reinforced by TAS 2 ¶13.

## 3. Re-registered — items that fell out of prior registers (3)

Per `08` §5. These were never closed; they stopped appearing.

| ID | Statement | Origin | Status |
|----|-----------|--------|--------|
| **P04-B-13** | **No tax book / no tax written-down value.** Named in P2 as the largest single functional gap for a Thai deployment, with six tax scenarios shown impossible against statutory rates that are ceilings. Not carried into P3 as a blocker at all | P2 | **RE-OPENED.** Owner **P08**. Closes on a Boss scoping decision plus a design |
| **P04-B-25** | **Thai tax treatment of gain on disposal.** Left on hold in P1, then dropped | P1 | **RE-OPENED unchanged.** Not researched by this session. Routed to the Accounting-Tax track |
| **P04-B-29** | **Seven preserved expert disagreements from P2** never closed and never carried. Two are advanced by this session's evidence (see `12` §3) | P2 | **RE-OPENED.** Closes on adjudication at the Final Gate or by targeted research |

## 4. New — acquire end (9)

| ID | Statement | Class | Closes on |
|----|-----------|-------|-----------|
| **P04-B-01** | The upstream link to the purchase order exists **only on the journal item**. Reaching it from an asset needs a two-hop join that is nowhere stored. The mandatory *"trace to initiating business event"* is **not satisfiable from stored asset data** | FACT VERIFIED | A design decision to materialise the source-document reference on the asset |
| **P04-B-02** | The **origin mechanism** of the 280 live assets is not established. The runtime capture that appeared to show migration origin was **identifier-bounded** | UNRESOLVED | One unbounded count of assets grouped by presence and namespace of an external identifier |
| **P04-B-03** | Whether any live asset carries a link to a source vendor bill is **not observable** — the capture's 12-field list omits the link | UNRESOLVED | One count of assets with a non-empty source-line link |
| **P04-B-04** | **Hire purchase / instalment acquisition** has no host. The VAT treatment is prescribed (tax invoice per instalment due date) | Estate FACT VERIFIED; treatment DESIGN CANDIDATE | Accounting-Tax track ruling, then design |
| **P04-B-05** | **Borrowing-cost capitalization** (TAS 23): no write of loan interest into asset cost was found; interest goes to expense | Estate FACT VERIFIED (scoped); statute UNRESOLVED | Research TAS 23 applicability, then design |
| **P04-B-06** | **No capitalization-versus-expense decision point exists.** Nothing distinguishes a repair from an improvement | FACT VERIFIED | `P04-BD-08` plus a design |
| **P04-B-07** | **No assets-under-construction / capitalization stage.** No state exists between "does not exist" and "draft asset with a full cost" | FACT VERIFIED | Design |
| **P04-B-08** | **No acquisition-cost composition.** Cost is the bill line balance; nothing assembles a cost from several documents (freight, installation, duty, non-recoverable input tax, testing, dismantling provision) | FACT VERIFIED | Design, informed by TAS 16 ¶16–17 (not yet retrieved — see `P04-B-30`) |
| **P04-B-16** | Whether a **vendor credit note** reliably satisfies the positive-total eligibility test. Intent is asserted by the field's own help text; the code path was not traced | UNRESOLVED | A trace of the tax engine's sign behaviour, or one runtime test |

## 5. New — retire end (10)

| ID | Statement | Class | Closes on |
|----|-----------|-------|-----------|
| **P04-B-09** | **No transfer capability at all.** Not found under the asset module using case-insensitive `transfer` | FACT VERIFIED (scoped) | Design. Note the standing ruling that a cross-company move is a **disposal and an acquisition**, reinforced by the scope-aware constitution |
| **P04-B-10** | **No impairment concept.** The nearest behaviour records an impairment as **accelerated depreciation**, labelled in the ledger as ordinary depreciation | FACT VERIFIED | Design against TAS 36, which no package has yet researched |
| **P04-B-11** | **No revaluation surplus / equity component.** A downward revaluation posts to depreciation expense; on derecognition TAS 16 requires the surplus to go **directly to retained earnings** | FACT VERIFIED | Design |
| **P04-B-12** | **Scrap is not an asset event.** One action cannot carry the two different Thai evidence regimes | FACT VERIFIED | `P04-BD-07` plus design |
| **P04-B-18** | A child asset already closed with zero residual passes the sale guard **yet is still fed the parent's customer-invoice lines** | UNRESOLVED — no test exercises it | One runtime test |
| **P04-B-19** | Whether **re-opening a disposed asset** works at all: the path refuses when a draft entry predates the operation date, and the draft disposal entry is exactly such an entry | UNRESOLVED — no test covers it | One runtime test |
| **P04-B-20** | **No derecognition trigger for "no future economic benefit expected"** — TAS 16's second criterion. No idle state, no benefit test, no impairment concept | FACT VERIFIED | Design |
| **P04-B-21** | **Donation as a disposal form** is expressible only as a no-proceeds disposal, losing its tax and VAT character | FACT VERIFIED | Design plus an Accounting-Tax ruling |
| **P04-B-22** | The **disposal date** is a free-text field defaulting to today, with no link to a control-transfer event. TAS 16 requires the date the recipient obtains control | FACT VERIFIED | Design |
| **P04-B-24** | Whether the **30-day advance-notice** destruction regime extends to fixed assets. The instruction's own scope names goods and scrap; a single ruling points a taxpayer toward it | **HOLD / EVIDENCE REQUIRED** | An Accounting-Tax track ruling or a Revenue Department confirmation |

## 6. New — ledger, period and control (5)

| ID | Statement | Class | Closes on |
|----|-----------|-------|-----------|
| **P04-B-17** | **No sub-ledger to general-ledger reconciliation exists**, and **six** verified mechanisms can break the agreement, with nothing that would detect any of them | FACT VERIFIED | Design. Must be originated, not adapted |
| **P04-B-31** | **A depreciation entry aimed at a locked period is silently re-dated, not rejected.** The estate's own test asserts a charge for one fiscal year posting into the next, carrying its full value with it. The behaviour applies to the hard lock as well | FACT VERIFIED | Design decision: refuse rather than re-date. **Owner P08.** See §8 |
| **P04-B-32** | **Confirmation posts an asset's entire life in one action with no lock-date check** | PRIOR EVIDENCE re-confirmed | Design |
| **P04-B-33** | Writing to an asset rewrites accounts on **already-posted** entries **by line ordinal**, including on the disposal entry, whose lines are not a two-line depreciation pair | FACT VERIFIED | Design |
| **P04-B-34** | Every disposal **silently rewrites the company's gain and loss account defaults**, with elevated privilege | FACT VERIFIED | Design |

## 7. New — scope, evidence and governance (6)

| ID | Statement | Class | Closes on |
|----|-----------|-------|-----------|
| **P04-B-26** | **Evidence-root integrity.** A stray temporary write artefact was found in the reference source tree. Something has written into an evidence root | FACT VERIFIED | Confirm the artefact's origin; re-verify the tree's integrity if it cannot be explained |
| **P04-B-27** | The **third `BLK-07` option** requires a reliable expected-total-output estimate per asset, reviewed annually. Nothing holds one | DESIGN CANDIDATE | `P04-BD-05` |
| **P04-B-28** | A **company-less asset group's** visibility under the parent-of rule is not decidable from source — it may be visible to none or to all | UNRESOLVED | One runtime check |
| **P04-B-30** | **TAS 16 standard text** not retrieved. All TAS 16 findings in this package rest on TFAC's explanatory manual, which states on every page that it is **not part of the standards**. This also affects the acquisition-cost composition paragraphs | **HOLD / EVIDENCE REQUIRED** | Retrieve the gazetted standard text. Continues prior `HOLD-03` |
| **P04-B-35** | **Work-centre company-optionality** is a scope violation on the corrected constitution's own terms: it creates a financial effect and cannot answer which company owns it | FACT VERIFIED (estate) / SUPPORTED INTERPRETATION (scope) | **PEER DEPENDENCY — P03**, plus one runtime count |
| **P04-B-36** | **Handover residue control.** At least ten registered items ceased to appear across three packages without being closed, while each package's lineage statement was true as written | FACT VERIFIED | A carry-forward rule that tracks **open items**, not only conclusions |

## 7A. New — asset master data, recognition timing and indirect tax (5)

Registered here after an internal consistency check found these five referenced
elsewhere in the package but absent from this register. The check, and this
correction, are recorded in `18_P04_REVISION_LOG.md` as `P04-REV-10`.

| ID | Statement | Class | Closes on |
|----|-----------|-------|-----------|
| **P04-B-14** | **No asset numbering, tagging, barcode or physical-verification capability.** Not covered by any prior package and not found in the estate. A fixed-asset register that cannot be counted cannot be audited | FACT VERIFIED (scoped negative) | Design |
| **P04-B-15** | **No component depreciation.** The TAS 16 explanatory manual requires a component whose cost is significant relative to the whole to be depreciated separately, illustrating it with a production machine. The estate has no component concept and a single-valued asset-to-machine link | Estate FACT VERIFIED; requirement ACCOUNTING STANDARD INTERPRETATION | Design, plus a decision on how components aggregate into one machine cost pool |
| **P04-B-23** | **No path for third-party compensation** for an impaired, lost or retired asset. TAS 16 requires it to be recognised in profit or loss when the entity becomes entitled to it, as an event **separate** from the derecognition | Estate FACT VERIFIED (scoped negative); requirement ACCOUNTING STANDARD INTERPRETATION | Design |
| **P04-B-37** | **Received-not-billed / in-service date.** Recognition is driven by the supplier invoice, and the acquisition date is derived from the **invoice date**. An asset received and in service but not yet billed is not recognised, and there is no accrual path. For Thai tax, pro-ration runs from acquisition — so the estate's pro-ration start is **later than the statutory basis** whenever receipt and billing fall in different months | Estate FACT VERIFIED; statutory consequence SUPPORTED INTERPRETATION | Design decision on the recognition trigger, plus an Accounting-Tax ruling on the pro-ration start date. Raised at `15` Level 1; **`D-P04-01` is open on whether it is in P04 scope** |
| **P04-B-38** | **VAT on the sale of a fixed asset is not addressed anywhere** in this or any prior package. The disposal path derives proceeds from a customer invoice carrying its own tax treatment, and nothing checks that the disposal entry and the VAT treatment agree | UNRESOLVED — not researched | Accounting-Tax track research. Raised at `15` Level 3 |

## 8. Ranking — what actually stops progress

| Rank | Blocker | Why it ranks here |
|------|---------|-------------------|
| **1** | **BLK-07** + the single-mechanism proof | The AAS+ veto. No costing implementation may begin. The second limb is **wider** after this session — nine paths (`06` §2) |
| **2** | **P04-B-31** — silent re-dating into an unlocked period | It is not a design gap; it is **live behaviour that misstates a fiscal year**, asserted by the estate's own test. Any migration or parallel-run that posts a back-dated depreciation entry is exposed today |
| **3** | **P04-B-17** — no sub-ledger reconciliation, six ways to break it, none detected | It is the control that would catch most of the others |
| **4** | **P04-F-13 / P04-B-06** — the derecognition entry is never posted by the system | An asset reads "Closed" while its cost and accumulated depreciation stay in the ledger |
| **5** | **P04-B-02 / B-03** — the live population's origin and upstream linkage are unknown | Two queries. They gate every migration statement |
| **6** | **P04-B-35** — work-centre company-optionality | The narrowed, sharper form of the prior SaaS finding |

Everything below rank 6 is real and none of it blocks the **research**; it
blocks **design closure** at specific points named in each row.

## 9. Runtime evidence set

The prior package's nine read-only queries are carried unchanged. This session
adds five, all read-only and all one execution each:

| ID | Query | Closes |
|----|-------|--------|
| **Q-10** | Assets grouped by presence and namespace of an external identifier — **unbounded** | `P04-B-02` |
| **Q-11** | Count of assets with a non-empty source-journal-item link | `P04-B-03`, `P04-B-01` |
| **Q-12** | Accounts carrying an automation mode other than "no", with their attached model count and account type | `01` §UC-02, UC-03 |
| **Q-13** | Asset groups with no company, and their visibility | `P04-B-28` |
| **Q-14** | Work centres and equipment records with no company | `P04-B-35` |

The prior package's priority-1 query — the **installed-module list of the running
system** — retains its priority. It caps **every** negative finding in this
package as well as in the previous two.
