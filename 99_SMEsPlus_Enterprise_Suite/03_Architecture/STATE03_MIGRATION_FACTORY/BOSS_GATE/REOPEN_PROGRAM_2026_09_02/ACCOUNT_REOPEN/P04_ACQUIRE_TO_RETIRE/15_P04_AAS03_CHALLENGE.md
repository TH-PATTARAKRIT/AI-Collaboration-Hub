# 15 — P04 AAS-03 FOUR-EXPERT CHALLENGE

Layer: **2 — audit quarantine**.

All four experts challenge every material level. **Disagreement is preserved.**

- **E1 — Accounting standards** (TFRS / TAS)
- **E2 — Thai statutory and tax**
- **E3 — ERP systems and data architecture**
- **E4 — Audit, control and evidence**

---

## Level 1 — The upstream capitalization finding (`01`)

**Claim challenged:** the capitalization source of truth is the posted vendor
bill or a manually selected posted journal item; never the purchase order,
never the receipt, never the product.

| Expert | Position |
|--------|----------|
| **E1** | **Accept, and note it is defensible.** Recognition under TAS 16 depends on cost being reliably measurable and on control passing — the bill is closer to both than the order is. The **weakness is the reverse**: an asset received and in use but **not yet billed** is not recognised, and the estate has no accrual path to recognise it. Raise as a finding |
| **E2** | **Accept with a Thai qualification.** For tax, the acquisition date drives pro-ration under `LAW-01` / `LAW-02`. The estate derives it from the **invoice date**, not the in-service date. Where a machine is received in one month and billed in the next, **the estate's pro-ration start is later than the statute's basis**. This is not addressed anywhere in the package |
| **E3** | **Accept the finding; challenge its completeness.** The negative for purchase and receipt rests on a model-name grep. A hook injected under a different name would not be caught. The mitigation applied — checking callers of the creation method directly — closes it for that method, not for hypothetical unrelated hooks. The residual risk is small and **is not zero** |
| **E4** | **Accept, and escalate `UC-02`/`UC-03`/`UC-04`.** Three of four values that determine every future depreciation entry are enforced by the interface only. From a control standpoint that is the **single most important sentence in the package**, because every migration, integration and scripted correction bypasses all three — and the live population was created by exactly such a path |

**Disagreement recorded — `D-P04-01`.** E1 and E2 both identify a **received-not-billed / in-service-date** gap; E3 considers it out of P04's declared scope
(it is a recognition-timing question, not a mechanism question). **Not resolved.**
Registered as **P04-B-37**.

## Level 2 — The event and general-ledger findings (`03`, `04`)

**Claim challenged:** the derecognition entry is created in draft and the system
never posts it.

| Expert | Position |
|--------|----------|
| **E1** | **Material.** Under TAS 16 derecognition occurs when the criteria are met; the accounting must follow. An asset in a "closed" state whose cost and accumulated depreciation remain in the ledger is **not derecognised**. The state field is telling the user something the ledger does not say |
| **E2** | **Material for tax too.** The deductible loss on write-off arises in the period of the event. If the entry is posted late — or in a different period after a lock-date re-dating — **the deduction lands in the wrong year** |
| **E3** | **Accept the mechanism; challenge the framing.** Leaving it in draft may be deliberate: the entry frequently needs a human to attach proceeds or correct an account. The defect is not that it is draft — it is that **nothing surfaces the outstanding draft**, and the asset's state has already moved |
| **E4** | **Accept E3's framing and sharpen it.** The compound in `03` §3 is what matters: a disposal can misconfigure the company, produce an **unbalanced** draft entry because of that misconfiguration, and leave the asset reading "Closed" — **with no error at any step**. Three independent defects that only fail together, which is precisely the profile that survives testing |

**Consensus:** the finding stands. **Disagreement recorded — `D-P04-02`:** E3
holds that draft-by-design is defensible; E1, E2 and E4 hold that the state
transition preceding the posting is not. **Not resolved.**

## Level 3 — The retire end and TAS 16 (`07`)

**Claim challenged:** of seven TAS 16 derecognition requirements, one is met, two
partly, four have no host.

| Expert | Position |
|--------|----------|
| **E1** | **Accept the count; challenge one row.** The disposal-date requirement is scored NOT MET because the date is a free field. In practice a competent user enters the control-transfer date. The defect is that **nothing enforces or evidences it** — that is a control finding, not a standards gap. **Recommend re-scoring as PARTLY MET** |
| **E2** | **Accept, and add the item the package does not have.** VAT on the sale of a fixed asset is not addressed anywhere. A sale of business assets is a "sale" for VAT purposes and the estate's disposal path derives proceeds from a customer invoice that carries its own tax treatment — but **no one has checked that the disposal entry and the VAT treatment agree**. Raise it |
| **E3** | **Accept.** And note the structural point: four requirements having "no host" means new models, not configuration. That is a **scope statement for the build**, and it belongs in the handoff pack |
| **E4** | **Accept, with a warning about the source.** Every TAS 16 row rests on TFAC's **explanatory manual**, which says on every page that it is not part of the standards. The package classifies this correctly. **It must not be quietly upgraded later.** The gazetted text is one retrieval away and has now been on hold across two packages |

**Disagreement recorded — `D-P04-03`.** E1 would re-score the disposal-date row
as PARTLY MET; E3 and E4 hold that a requirement with no enforcement and no
evidence trail is not partly met by user diligence. **Not resolved.**
E2's VAT item is registered as **P04-B-38**.

## Level 4 — The cost handoff and the veto (`06`)

**Claim challenged:** nine monetisation paths; the analytic route nets to zero;
the veto's second limb is wider.

| Expert | Position |
|--------|----------|
| **E3** | **Accept the enumeration; challenge the unit.** Nine is correct **under the declared unit** — own rate field, own driver, or own destination ledger. A different unit gives a different number. The package declares its unit, which is what the rule requires, but a reader comparing "nine" against the prior "two" is comparing **two different units**. Say so explicitly |
| **E1** | **Accept, and rank the standard-costing mismatch highest.** It is a **live general-ledger misstatement** under a supported configuration, not a design gap. It also answers a prior open item about how a standard-costed product complies with TAS 2 — **badly, and with no variance account** |
| **E4** | **Accept the netting finding; it is the most consequential correction in the package.** A control everybody believed existed does not. Also note the complementary case is worse than the first: with no distribution, the two lines get **different** distributions and produce meaningless non-zero residue |
| **E2** | **No Thai-specific position on the mechanism count.** But if the third `BLK-07` option is adopted, the depreciation **charge** changes, and that has direct tax consequences under `LAW-01` / `LAW-02` that are **unresearched**. The option must not be presented to the Boss without that caveat attached |

**Consensus:** the veto is not dischargeable by this session, and its second limb
is wider. **E3's unit caveat is adopted** and is stated in `06` §2.1 and in the
handoff pack. **E2's caveat is adopted** and appears in `09` §3 and `06` §7.

## Level 5 — Scope (`20`)

**Claim challenged:** the prior company-optional finding narrows to one object
class.

| Expert | Position |
|--------|----------|
| **E3** | **Accept and endorse.** Ownership scope ≠ operational scope was exactly the conflation. A machine register spanning a tenant's companies is normal and correct |
| **E1** | **Accept for the machine register; press harder on the work centre.** Its rate lands in **inventory valuation**. An object that changes the carrying amount of inventory and cannot say which legal entity owns that effect is not a scope preference — it is **unauditable** |
| **E4** | **Accept, and record the method risk.** Narrowing a High-severity finding on a constitutional correction is the moment when a real defect quietly disappears. The package narrows it **visibly**, in two places, and keeps the residue at High for the one class that deserves it. **That is the right handling**; it must be checked at the Final Gate that no one later cites the narrowing as a clearance |
| **E2** | **One addition.** Company = legal/accounting boundary means **tax filings** follow the company. Any object feeding a figure into a Thai statutory return is company-scoped by necessity, whatever its operational convenience |

**Consensus:** the narrowing stands, with E4's warning attached to the handoff.

## Level 6 — Governance (`08` §5)

**Claim challenged:** at least ten registered items ceased to appear across three
packages without being closed.

| Expert | Position |
|--------|----------|
| **E4** | **Accept, and call it the most transferable finding here.** Each package's lineage statement was **true as written** and the residue happened anyway, because a statement about **conclusions** does not protect **open items**. That is a reusable control lesson, not an Asset-domain fact |
| **E3** | **Accept.** And note this session reproduced the same class of defect internally within one session — three enumerations, three denominators, one false negative. It is not a between-sessions problem; it is an enumeration-discipline problem |
| **E1** | **Accept, and note which items matter.** The tax book is not a minor omission. It was called the largest single functional gap for a Thai deployment and then vanished from every register |
| **E2** | **Agree, emphatically, on the tax book.** Thai statutory rates are **ceilings**. Book and tax depreciation therefore diverge by design. **A deployment with no tax book cannot compute its own tax position.** This should rank higher than it does |

**Disagreement recorded — `D-P04-04`.** E2 would rank the tax book above rank 6
in `10` §8; the ranking as written places it outside the top six because it is a
P08-owned gap that does not block P04 research. **Not resolved — E2's position is
preserved and visible.**

## Summary of preserved disagreements

| ID | Between | Subject | Status |
|----|---------|---------|--------|
| `D-P04-01` | E1, E2 vs E3 | Whether the received-not-billed / in-service-date gap is in P04 scope | **OPEN.** `P04-B-37` |
| `D-P04-02` | E3 vs E1, E2, E4 | Whether a draft derecognition entry is defensible by design | **OPEN** |
| `D-P04-03` | E1 vs E3, E4 | Whether the disposal-date requirement is NOT MET or PARTLY MET | **OPEN** |
| `D-P04-04` | E2 vs the ranking | Whether the tax book ranks in the top six blockers | **OPEN** |

Plus the **seven** inherited disagreements re-opened in `12` §3, which this
session re-registers rather than adjudicates — two of them advanced by evidence.
