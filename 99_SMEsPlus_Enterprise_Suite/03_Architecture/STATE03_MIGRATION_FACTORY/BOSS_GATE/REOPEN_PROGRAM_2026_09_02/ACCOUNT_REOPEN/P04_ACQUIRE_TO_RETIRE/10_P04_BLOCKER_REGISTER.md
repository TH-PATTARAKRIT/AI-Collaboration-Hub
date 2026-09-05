# 10 — P04 BLOCKER REGISTER

Layer: **2 — audit quarantine**.

Inherited blockers are carried at their prior state and **not re-derived**.
New blockers are numbered `P04-B-nn`. Every row states **what closes it**.

---

## 1. Inherited — open (4)

| ID | Statement | Status | Closes on |
|----|-----------|--------|-----------|
| **BLK-01** | Which day convention the live asset population actually uses — **MATERIALLY ADVANCED, NOT CLOSED.** A second population is now measured: in `iSMEs`, **683 of 685** assets use daily computation — while **every asset template across the v19 line is on `constant_periods` — 96 of 96 per identity and 144 of 144 over six snapshots, spanning **four** v19 database identities and four months**, the product default and the convention production does *not* use (`P04-F-81`). Since the two conventions agree annually within 0.05 %, an annual reconciliation cannot detect the mismatch. **ANSWERED IN THE DATABASE IT NAMES — NOT CLOSED.** `idemo18_uat` **was on this host all along**, at `~/OCC_BACKUP/`, outside a path set this package chose and never declared; the exclusion that kept this blocker open is withdrawn (`P04-F-88` withdrawn, `P04-F-90`). Read: **375 of 388 real assets on `daily_computation`** and **16 of 16 templates on `constant_periods`** — the split measured **inside one v18 database** (`P04-F-91`) | **ANSWERED — NOT CLOSED**; the close condition names *"the 280 records"* and this archive holds **404** (388 real + 16 templates), so the runtime figure and the archive figure do not agree and this package cannot say which moment either describes | The grouped count is **executed and published**. What remains is reconciling 280 against 404, which is a **Boss/runtime question**, not a research one |
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
| **P04-B-25** | **Thai tax treatment of gain on disposal.** Left on hold in P1, then dropped | P1 | **RE-OPENED, and now with a named owner gap.** P07 **declines it explicitly and correctly**: its statutory register holds **no corporate income tax authority at all** — it is VAT, withholding and tax-document authority by design — and answering from those sources would be inference across statutes, the exact defect this programme has spent the week correcting. P07 carries it as `U-25` with an explicit evidence requirement so it stops being dropped for a fourth package. **It needs its own corporate-income-tax retrieval, and no process currently owns that scope.** That ownership gap is itself the blocker |
| **P04-B-29** | **Seven preserved expert disagreements from P2** never closed and never carried. Two are advanced by this session's evidence (see `12` §3) | P2 | **RE-OPENED.** Closes on adjudication at the Final Gate or by targeted research |

## 4. New — acquire end (11)

| ID | Statement | Class | Closes on |
|----|-----------|-------|-----------|
| **P04-B-01** | The upstream link to the purchase order exists **only on the journal item**; the two-hop join is nowhere stored, so the mandatory *"trace to initiating business event"* is not satisfiable from stored asset data. **Strengthened from a design gap to a measured one:** in the one asset population this session could measure, **the first hop does not exist for 96.7 % of records**, so no traversal can reach a purchase order however it is written (`P04-F-82`) | FACT VERIFIED (design) · **FACT VERIFIED (measured, `iSMEs`)** | A design decision to materialise the source-document reference on the asset |
| **P04-B-02** | The **origin mechanism** of the 280 live assets is not established. The runtime capture that appeared to show migration origin was **identifier-bounded** | UNRESOLVED | One unbounded count of assets grouped by presence and namespace of an external identifier |
| **P04-B-03** | Whether any live asset carries a link to a source vendor bill — **ANSWERED for one population, OPEN for the one it names.** Executed against database `iSMEs` @ 2026-07-11: of **669** non-template assets, **22** carry any source-line link — **647, or 96.7 %, carry none** (`01` §6A.3, `P04-F-82`). **ANSWERED for `idemo18_uat`** — the archive was found after the path set was declared (`P04-F-90`): `asset_move_line_rel` **exists and holds no rows**, so **0 of 388 real assets** carry a source-line link, against 22 of 669 in `iSMEs`. Positive control in the same command (`account_asset` → 404 rows) proves the empty result is absence, not extraction failure (`P04-F-92`) | **FACT VERIFIED** for `iSMEs`; UNRESOLVED for `idemo18_uat` | One equivalent count against `idemo18_uat` |
| **P04-B-47** | **Were the missing asset journal entries never created, or created and removed?** In `551ab874`, **285 of 350** assets in entry-generating states carry no journal entry at all, including **30 of 30 disposed** (`P04-F-96`). `P04-B-40` — the pending-entry clearing routine whose draft branch has no date test — turns on exactly this distinction | **NOT DECIDABLE FROM THIS EVIDENCE.** A single snapshot cannot separate never-created from created-and-deleted. Recorded rather than resolved; the disposal-specific reading is **not** confirmed by this database because the absence is general, not disposal-specific | Either a second snapshot of the same identity at a different date, or the deployment's own audit/mail-message trail. Both are **runtime requests** |
| **P04-B-46** | **The declared source scope is not the deployed source scope.** Against the v18 deployment `551ab874`: **27 of 361 installed modules are in neither declared root**, and **37 of the 65 declared custom directories are not installed there** (`P04-F-93`). Source for **`equipment_fleet`** and **`journal_entries_report`** does not exist anywhere under `/Volumes` or `$HOME` (`P04-F-94`) | **UNRESOLVED — SOURCE SCOPE UNDECLARED.** Every source-derived finding in this package is bounded to a scope now known not to be the deployed one. No finding withdrawn; effect unassessed because none of the 27 has been read | Read the 25 modules whose source is on the host, starting with `scgl_account_coa_control` (the capitalization designation lives on the chart-of-accounts account) and `scgl_date_range_auto_period` (period assignment — the silent re-dating finding). The remaining two need the deployment's own addons path, which is a **runtime request**, not research |
| **P04-B-04** | **Hire purchase / instalment acquisition** has no host. The VAT treatment is prescribed (tax invoice per instalment due date) | Estate FACT VERIFIED; treatment DESIGN CANDIDATE | Accounting-Tax track ruling, then design |
| **P04-B-05** | **Borrowing-cost capitalization** (TAS 23): no write of loan interest into asset cost was found; interest goes to expense | Estate FACT VERIFIED (scoped); standard UNRESOLVED | Retrieve TAS 23 and decide applicability, then design. **Ownership corrected after P07 declined it:** this is an **accounting-standard** question, not a tax one, and P07's register is VAT, withholding and tax-document authority by design. It returns to the **accounting track / P04**, and is not routed to P07 |
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
| **P04-B-19** | **Re-classified from UNRESOLVED to FACT VERIFIED after independent challenge.** Re-opening a disposed asset is **not** blocked by its own draft disposal entry. Where the operation date does not precede that entry, no guard fires and the clearing routine — whose draft branch carries **no date test** — **silently deletes it**. See `P04-B-40` | **FACT VERIFIED** | Closed as a question; carried as `P04-B-40` as a defect |
| **P04-B-20** | **No derecognition trigger for "no future economic benefit expected"** — TAS 16's second criterion. No idle state, no benefit test, no impairment concept | FACT VERIFIED | Design |
| **P04-B-21** | **Donation as a disposal form** is expressible only as a no-proceeds disposal, losing its tax and VAT character | FACT VERIFIED | Design plus an Accounting-Tax ruling |
| **P04-B-22** | The **disposal date** is a free-text field defaulting to today, with no link to a control-transfer event. TAS 16 requires the date the recipient obtains control | FACT VERIFIED | Design |
| **P04-B-24** | **Widened after P07 challenge, and its route corrected.** An unevidenced destruction of a fixed asset has **two** tax consequences, not one. **Limb A — income tax:** whether the 30-day advance-notice regime extends to fixed assets; the instruction's own scope names goods and scrap, and a single ruling is persuasive on its facts, not general. **Limb B — value-added tax:** whether the destruction is a **deemed sale** carrying output tax independently of deductibility. P04 originally scoped only Limb A. **Route corrected:** for a fixed asset the deemed-sale limb runs through sub-paragraph **(ง)**, not (จ) — (จ) is anchored to the s.87(3) goods-and-raw-materials report, which is required only of goods-selling registrants and in which a fixed asset is not an entry (`07` §5.2.1, `P04-F-67`) | **HOLD / EVIDENCE REQUIRED**, both limbs | Limb A: a Revenue Department confirmation — open. Limb B: **partly advanced.** The retrieval P04 predicted would serve both blockers did (`P04-LAW-H`): the safe harbour covers **use, not transfer**, so a destruction is outside it. Residual on limb B is the unresolved services-versus-goods limb and the exemption list. **The (จ) question remains formally open**: P07 attempted the prescribed contents of the s.87(3) report **and did not locate it** — recorded as *attempted-and-not-located*, not as absent — so `P04-F-67` stays **SUPPORTED INTERPRETATION**. Owner **P07** |

## 6. New — ledger, period and control (5)

| ID | Statement | Class | Closes on |
|----|-----------|-------|-----------|
| **P04-B-17** | **No sub-ledger to general-ledger reconciliation exists**, and **six** verified mechanisms can break the agreement, with nothing that would detect any of them | FACT VERIFIED | Design. Must be originated, not adapted |
| **P04-B-31** | **A depreciation entry aimed at a locked period is silently re-dated, not rejected.** The estate's own board-computation test `test_post_moves_after_lock_date` sets a fiscal-year lock of 30 June 2021 and asserts a 31 December 2020 charge of 12 000 posting as **31 July 2021** — seven months later, in the following fiscal year, at full value. The hard lock is covered too. **The behaviour lives in the accounting core's generic posting routine, not in the asset module**, so it applies to every programmatically posted entry in the product | FACT VERIFIED — **and re-framed after P11 widened `T0-13`: this is a PRESENT DEFECT, not a prospective risk.** It is reachable today inside a single company, so it **does not wait on the Boss's tenant ruling (`D-12`)** and stands whatever that ruling is | **Close condition restated after the P11 exchange.** Not "refuse rather than re-date" — that is only half. P11's new tolerance-zero boundary `T0-13` separates the two questions correctly: whether a boundary is crossed, and whether the crossing is **detectable**. Applied here: the defect is that the mutation happens with **no refusal and no trace**, so the close condition is **refuse, or record an attributable trace of the re-dating**. **Refined by P11 and adopted:** the two are alternatives **only where a rule is being broken**. For the second re-dating path (`P04-B-45`) **no lock is configured, so there is no violation to detect and refusal is not an available control** — a design could implement refusal, satisfy the boundary as written, and leave that path live. **Where a mutation path has no violation to detect, an attributable trace is MANDATORY, not alternative.** **Owner P08** (core, not asset). See §8 and `20` §4.2.2 |
| **P04-B-32** | **Confirmation posts an asset's entire life in one action with no lock-date check** | PRIOR EVIDENCE re-confirmed | Design |
| **P04-B-33** | Writing to an asset rewrites accounts on **already-posted** entries **by line ordinal**, including on the disposal entry, whose lines are not a two-line depreciation pair | FACT VERIFIED | Design |
| **P04-B-34** | Every disposal **silently rewrites the company's gain and loss account defaults**, with elevated privilege | FACT VERIFIED | Design |

## 7. New — scope, evidence and governance (6)

| ID | Statement | Class | Closes on |
|----|-----------|-------|-----------|
| **P04-B-26** | **Evidence-root integrity — narrowed after independent challenge.** The stray artefact is a **zero-byte** temporary file dated months before this session: a writability probe, not a mutation of module content. Separately, **one directory of 791 carries no manifest and no content** — a web-integration module reduced to an empty translation folder. Neither undermines any finding; both mean *"primary source complete for the declared path set"* needs the qualifier that one module in the tree is empty | FACT VERIFIED, **severity reduced** | Stated. No further action unless the empty module is material to another process |
| **P04-B-27** | The **third `BLK-07` option** requires a reliable expected-total-output estimate per asset, reviewed annually. Nothing holds one | DESIGN CANDIDATE | `P04-BD-05` |
| **P04-B-28** | **CLOSED — the source decides it, and this package over-claimed uncertainty.** *(P11 registered the general rule behind this caveat as `SCP-08`: the semantics of an absent scope value must be defined, and "unset" may never mean "all". An operator whose behaviour on null is undecidable is itself the defect.)* The parent-of operator drops falsy identifiers and expands to a membership test over ancestor identifiers, so a null company can never match; and the asset security rules **omit** the explicit null-company alternative that the framework's own company helper adds. **A company-less asset group is visible to no one.** Runtime query `Q-13` is withdrawn as unnecessary and repurposed to count such groups, which would otherwise be invisible and undeleted | **FACT VERIFIED** | Closed. The residual is a data question, not a behaviour question |
| **P04-B-30** | **TAS 16 standard text** not retrieved. All TAS 16 findings in this package rest on TFAC's explanatory manual, which states on every page that it is **not part of the standards**. This also affects the acquisition-cost composition paragraphs | **HOLD / EVIDENCE REQUIRED** | Retrieve the gazetted standard text. Continues prior `HOLD-03` |
| **P04-B-35** | **Work-centre company-optionality** is a scope violation on the corrected constitution's own terms: it creates a financial effect and cannot answer which company owns it | FACT VERIFIED (estate) / SUPPORTED INTERPRETATION (scope) | **PEER DEPENDENCY — P03**, plus one runtime count |
| **P04-B-36** | **Handover residue control.** At least ten registered items ceased to appear across three packages without being closed, while each package's lineage statement was true as written | FACT VERIFIED | A carry-forward rule that tracks **open items**, not only conclusions |

## 6A. New — raised by independent challenge (3)

Both were found by the independent adversarial review and **verified directly**
by this session before being registered. See `16` §3.

| ID | Statement | Class | Closes on |
|----|-----------|-------|-----------|
| **P04-B-40** | **The draft derecognition entry is silently DELETED by ordinary later activity.** The routine that clears pending entries before any asset operation filters *draft* **or** *(posted and dated after the operation date)* — and **the draft branch carries no date test**. Every pending entry on the asset is removed whatever its date. Re-opening, pausing or re-valuing a closed asset therefore destroys its derecognition entry with no warning and no trace. Compounds `P04-F-13` from "never posted" to "never posted, and destroyable" | **FACT VERIFIED** | Design: the derecognition entry must post as part of the retirement, or be protected from the clearing routine |
| **P04-B-42** | **Repeated re-evaluation of an asset that already carries gross-increase children.** The modify wizard writes method and period to the children unconditionally and re-posts their schedules. The interaction with an existing child's own schedule is **untested in the estate** and untraced here | UNRESOLVED | One runtime test |
| **P04-B-41** | **A custom module injects a general-ledger account into every company that installs it.** Its data file — listed under the manifest's `data` key, with the `demo` key commented out, so it loads on **every** install — creates a hard-coded account (code `555555`, expense type, reconcilable) plus a product pointing at it, and **explicitly sets that account's capitalization automation flag from the data file**. A chart of accounts is company legal-accounting truth; a module writing into it on install makes a company-scoped accounting decision from platform-scoped packaging. It is also live proof of `01` §3.1 `UC-02`/`UC-04`: the designation is written by a non-interface path | **FACT VERIFIED** | Deployment decision plus a scope ruling on what an installable module may write into a chart of accounts |

## 6B. New — from the P11 scope intake (3)

| ID | Statement | Class | Closes on |
|----|-----------|-------|-----------|
| **P04-B-45** | **A second re-dating path that involves no lock.** P11's accounting-event register records, besides the on-posting re-dating this package found, an entry re-dated **on a document-date change** on any non-sale document — *"fires with no lock configured"*, and reachable by an upstream clerical edit with no accounting justification. `P04-B-31` and `T0-13` are both framed around the lock path; this one is outside it | **FACT VERIFIED** — read at P11 commit `2e284ef` | A control on the **document-date change** path, not only on posting. Owner **P08 / P11** |
| **P04-B-43** | **The lock date cascades across the company hierarchy, irreversibly, through a deliberately privileged traversal.** Verified from primary source: the effective hard lock is the **maximum over the whole parent chain**, computed with elevated privilege and including archived companies; the soft locks traverse the same way; the code carries an explicit comment that elevated privilege is needed *because the user might not have access to a parent company*; and the hard lock **cannot be removed or moved earlier**. Compounded with `P04-B-31` — which establishes that the lock **re-dates rather than refuses** — a hierarchy edge crossing a tenant boundary would produce **silently mis-periodised entries in another tenant's books**, not a visible failure | **FACT VERIFIED** | The lift condition stated by P11 and adopted at `20` §4.2.1: an invariant admitting no exception that every company's tenant assignment is stored and non-null and that **no hierarchy edge may join two companies with different tenant assignments**, plus a continuous conformance control. Owner **P11 / P08** |
| **P04-B-44** | **The machine register's TENANT scope expires.** It is TENANT-scoped with no financial effect **only because the absorption path is absent**. TAS 2 ¶12 makes absorption **required**, so the first mechanism SMEsPlus is obliged to build makes the machine the carrier of a company financial effect and forces **COMPANY**. Adopted from P11 `P11-F-05` | **SUPPORTED INTERPRETATION** (the scope consequence) on **FACT VERIFIED** premises | A scope re-test triggered by the absorption design, not by a date. Owner **P04 / P03** |

## 7A. New — asset master data, recognition timing and indirect tax (6)

Registered here after an internal consistency check found these five referenced
elsewhere in the package but absent from this register. The check, and this
correction, are recorded in `18_P04_REVISION_LOG.md` as `P04-REV-10`.

| ID | Statement | Class | Closes on |
|----|-----------|-------|-----------|
| **P04-B-14** | **No asset numbering, tagging, barcode or physical-verification capability.** Not covered by any prior package and not found in the estate. A fixed-asset register that cannot be counted cannot be audited | FACT VERIFIED (scoped negative) | Design |
| **P04-B-15** | **No component depreciation.** The TAS 16 explanatory manual requires a component whose cost is significant relative to the whole to be depreciated separately, illustrating it with a production machine. The estate has no component concept and a single-valued asset-to-machine link | Estate FACT VERIFIED; requirement ACCOUNTING STANDARD INTERPRETATION | Design, plus a decision on how components aggregate into one machine cost pool |
| **P04-B-23** | **No path for third-party compensation** for an impaired, lost or retired asset. TAS 16 requires it to be recognised in profit or loss when the entity becomes entitled to it, as an event **separate** from the derecognition | Estate FACT VERIFIED (scoped negative); requirement ACCOUNTING STANDARD INTERPRETATION | Design |
| **P04-B-37** | **Received-not-billed / in-service date.** Recognition is driven by the supplier invoice, and the acquisition date is derived from the **invoice date**. An asset received and in service but not yet billed is not recognised, and there is no accrual path. For Thai tax, pro-ration runs from acquisition — so the estate's pro-ration start is **later than the statutory basis** whenever receipt and billing fall in different months | Estate FACT VERIFIED; statutory consequence SUPPORTED INTERPRETATION | Design decision on the recognition trigger, plus an Accounting-Tax ruling on the pro-ration start date. Raised at `15` Level 1; **`D-P04-01` is open on whether it is in P04 scope** |
| **P04-B-38** | **VAT on the sale of a fixed asset.** Raised at `15` Level 3 as unresearched; **researched and narrowed the same session** (`07` §5.5). A fixed asset is "goods" and its sale is a "sale" — output tax arises and a tax invoice is required. **Narrowed to:** the disposal entry and the customer invoice's tax treatment exist independently and **nothing reconciles them** | Statute FACT VERIFIED; the reconciliation gap FACT VERIFIED | Design: a check that the disposal entry and the tax document agree |
| **P04-B-39** | **The no-proceeds disposal path produces no tax invoice**, while the VAT definition of "sale" **does not require consideration** and separately deems several acts — non-business use, goods missing from the record, goods remaining on cessation — to be sales. A **donation**, a scrapping or a write-off recorded through that path is, on the face of the definitions, an **unrecorded output-tax event** | Estate FACT VERIFIED; tax outcome SUPPORTED INTERPRETATION | **NARROWED, not closed.** P07 retrieved the self-supply safe-harbour announcement (`P04-LAW-H`). Two things now hold on either reading of an ambiguity P07 carries open: the harbour is conditioned on use **in a VAT-liable business**, so it does not reach an exempt one; and it covers **use, not transfer**, so **donation and scrapping fall outside it entirely**. The exposure therefore **survives the retrieval that might have closed it**. Residual: the announcement is cited to the **services** limb while its text names services *or goods*, and no separate announcement under (8)(ง) was found — unresolved, and not resolved by inference by either session. Still needs the s.81 exemption list. Owner **P07**. **Second independent reason for `P04-BD-07`** |

## 8. Ranking — what actually stops progress

| Rank | Blocker | Why it ranks here |
|------|---------|-------------------|
| **1** | **BLK-07** + the single-mechanism proof | The AAS+ veto. No costing implementation may begin. The second limb is **wider** after this session — nine paths (`06` §2) |
| **2** | **P04-B-31** — silent re-dating into an unlocked period | It is not a design gap; it is **live behaviour that misstates a fiscal year**, asserted by the estate's own test. Any migration or parallel-run that posts a back-dated depreciation entry is exposed today. **Confirmed as a present defect, not a prospective one:** it needs no tenant boundary and no company hierarchy (`P04-F-68`), so the standing boundary against it (`T0-13`, widened to any scope) is **not contingent** on the Boss's tenant ruling |
| **3** | **P04-B-17** — no sub-ledger reconciliation, six ways to break it, none detected | It is the control that would catch most of the others |
| **4** | **P04-F-13 + P04-B-40** — the derecognition entry is never posted by the retirement, **and is silently deleted by ordinary later activity** | An asset reads "Closed" while its cost and accumulated depreciation stay in the ledger — and the only record that a retirement was computed can disappear without trace. Raised from its original rank on the independent review's evidence |
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
| **Q-13** | Asset groups with no company — **repurposed**. `P04-B-28` is closed from source: such a group is visible to no one. The query now counts groups that exist but cannot be seen or deleted by any user | data hygiene, not behaviour |
| **Q-14** | Work centres and equipment records with no company | `P04-B-35` |

The prior package's priority-1 query — the **installed-module list of the running
system** — retains its priority. It caps **every** negative finding in this
package as well as in the previous two.
