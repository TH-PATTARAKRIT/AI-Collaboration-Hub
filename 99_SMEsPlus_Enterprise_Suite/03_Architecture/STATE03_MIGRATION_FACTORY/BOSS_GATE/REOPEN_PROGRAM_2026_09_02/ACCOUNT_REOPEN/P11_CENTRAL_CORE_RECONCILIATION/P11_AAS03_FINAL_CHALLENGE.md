# P11 — AAS-03 FOUR-EXPERT FINAL CHALLENGE

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · CP-09 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. How the challenge was run, and its independence limitation

Four AAS-03 expert panels were commissioned against the committed pre-challenge package
(`8a7a994`), each with a distinct lens, each instructed to **attack rather than endorse**, each
bound by four method rules: cite correction sections rather than headline tables; declare a search
boundary proportional to any negative claim; re-derive every count challenged; and use only the
five permitted verdicts — `SUPPORTED` / `SUPPORTED WITH CORRECTION` / `CONTRADICTED` /
`NOT DECIDABLE` / `EVIDENCE REQUIRED`. `PASS`, `APPROVED` and `CONDITIONAL PASS` were prohibited
as verdicts.

> **Independence limitation, stated first because it qualifies everything below.** The four panels
> are separate reasoning contexts commissioned by the session that produced the work. They read the
> package and the upstream evidence independently and were not shown each other's findings. They are
> **not** a human review and **not** an organisationally independent audit. A reader should weight
> their verdicts accordingly. This limitation is stated in the same terms the Asset package used of
> its own AAS+ audit, and for the same reason.

---

## 2. Expert 3 — Lead, Integration & Localization (Thailand)

**Verdict: `SUPPORTED WITH CORRECTION`.** *"the reconciliation's structure, its blocker discipline
and three of its five revalidations hold under attack, but the package may not be published until
`X3-F06`, `X3-F04` and `X3-F01`/`X3-F02`/`X3-F03` are corrected at source."*

### 2.1 Findings

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X3-F01` | **HIGH** | **Statutory class upgrade.** `P11_TAX_ARCHITECTURE.md` §1 heads three positions *"Statutory"*. The source reserves `THAI STATUTORY REQUIREMENT` for Revenue Code s.65 bis (2) and Royal Decree 145 alone; it classifies TAS 2 ¶12/¶13 as **`ACCOUNTING STANDARD REQUIREMENT (TFRS)`** and the DBD finding as **`THAI REGULATORY FACT`**. P11 collapsed three classes into one word | **ACCEPTED — CORRECTED.** Also self-caught as `P11-E-08` |
| `X3-F02` | **HIGH** | **TAS 2 ¶13 under-stated — two of four requirements dropped.** Missing #1 (normal capacity *"taking into account capacity lost to planned maintenance"*; the actual level may be used **if close to normal capacity**) and #4 (in abnormally high production the per-unit fixed amount is **reduced** so inventory is **not carried above cost**). Consequence: `CVP-01` mandates absorption **with no upper bound** — the half of ¶13 that protects the balance sheet | **ACCEPTED — CORRECTED.** Also self-caught as `F-E`. `CVP-01` gains an absorption cap |
| `X3-F03` | **HIGH** | **`CVP-02` over-claims its statutory ground and P11 contradicts itself on `BLK-07`.** ¶13 req 1 **permits** the actual level where it approximates normal capacity, so *"breaches TAS 2 ¶13"* is too strong. And the tax file lists the actual-hours rejection as a **consequence of a closed statutory position** while two other files keep `BLK-07` at `HOLD — DESIGN DECISION REQUIRED, owner Boss`. The upstream is itself split between its `§3` and `§6`, and P11 imported only the `§6` half | **ACCEPTED — CORRECTED** |
| `X3-F04` | **HIGH** | **A Boss-approved element was rewritten inside the column that records it.** The scope restatement of element 10 was placed in the **`BC-02` wording** column. Under it a producer declaring `PLATFORM` scope would be compliant carrying no context — which the Boss contract's §4 disqualifier forbids unconditionally | **ACCEPTED — CORRECTED.** Boss wording restored; restatement moved to the `P11 generalisation` column and marked `DESIGN CANDIDATE` |
| `X3-F05` | **HIGH** | **The compliance line contradicts two sources P11 itself registers.** Element 10 is *"specified, not built, not verified"*, not unchanged-failing; element 14 applies to *"the migration, replay and recovery handoffs, **not all ten**"* (`REV-F-02`); and **elements 4 and 7 are held under the COGS Gap on 8 of 10** and were omitted while `1–9` was marked *"unchanged"* | **ACCEPTED — CORRECTED.** This is the headline-over-corrections defect occurring in P11 |
| `X3-F06` | **HIGH** | **A Boss ruling inverted, and the inversion attributed to that ruling.** `MTI-D-01` is **Option B — Company-owned Product Master**; P11 recorded *"`TENANT` (per Boss ruling `D-01`)"*. P11's own table defines `TENANT` as *company context not required* — licensing exactly the shared cross-company product the ruling refuses. The ruling's stated reason is two companies performing a same-looking service under **different withholding-tax conditions** | **ACCEPTED — CORRECTED.** Also self-caught as `P11-E-05`. Product master → `COMPANY`; a separate `TENANT`-scoped mapping-layer object added per rule 5 |
| `X3-F07` | **MED-HIGH** | **`SCP-04` is violated by P11's own matrix in three rows** — numbering control, control/deletion evidence, and migration/replay batch all carry a financial effect yet are scoped `TENANT`; and element 14 then hard-codes `TENANT` identity for an object with a company-level effect. `P11_TIME_BASED_RECOGNITION_ARCHITECTURE.md` applies `SCP-04` correctly, so the rule is applied inconsistently inside one package | **ACCEPTED — CORRECTED** by qualifying `SCP-04`: the *effect* is `COMPANY`-scoped even where the *object* is wider, stated on all three rows |
| `X3-F08` | **HIGH** (Thai) | **The tax rate is `SCP-03`'s fourth instance and was not split.** The published rate is reference data, but **which** rate applies — WHT category by payee status and service type, VAT vs zero-rated vs exempt — is a company-level determination with a financial effect, exactly the shape already split for FX | **ACCEPTED — CORRECTED** |
| `X3-F09` | **MED-HIGH** (Thai) | **A `HOLD` that P11's own rule resolves.** Tax configuration is held `SCOPE EVIDENCE REQUIRED` while `SCP-04` determines it, and tax obligations attach per juristic person | **ACCEPTED — CORRECTED.** Tax configuration → `COMPANY`; `P11-B-08` reduced to three objects |
| `X3-F10` | **MED** (Thai) | **Consolidation placed at `TENANT` scope with its condition dropped.** Consolidation is a **parent company's** obligation; the tenant has no legal standing. The permission relied on is `XCR-02`, `SPECIFIED — CONDITIONAL`, carrying *"no valuation content while the COGS Gap stands"* — and a consolidated statement is entirely valuation content | **ACCEPTED — CORRECTED** |
| `X3-F11` | **MED** | **`RV-04` narrows three findings on an unenforced default.** *"Unrelated independent companies = separate tenants by default"* is a provisioning default, not an enforced invariant, and no tenant-assignment rule exists that would make it binding | **ACCEPTED — CORRECTED.** The narrowing becomes **conditional**; `SC-09` severity restored and `DC-13`/`PC-05` un-narrowed until the invariant exists |
| `X3-F12` | **MED** | **`RV-01` replaces a bright line with a self-declaration and supplies no declaration authority.** Nothing says who may declare an object `PLATFORM`, nor forbids declaring `PLATFORM` for an object with a financial effect | **ACCEPTED — CORRECTED.** New position: scope declaration is a controlled act with a named approver, and **no object with a financial effect may be declared `PLATFORM`** |
| `X3-F13` | **MED** (Thai) | **`TXP-02` adopts an answer to a question P11 holds.** `TX-H05` holds the Thai period-attribution consequence; denial suppresses a tax fact whose statutory recognition point may be the settlement date. P11 showed a two-way choice where a third exists — date at the statutory recognition point | **ACCEPTED — CORRECTED.** `TXP-02` → `DESIGN CANDIDATE — conditional on TX-H05`, third option added |
| `X3-F14` | **MED** | **Four cross-process handoffs missing entirely.** (a) **Payroll → ledger has no existence** — payroll is not among `P01`–`P10`, has no business event, no owner, no contract, so `P11-B-05`'s *"nine producing processes"* counts over an incomplete population. (b) **Statutory document issuance is not an owned event** — the WHT certificate has no document object, no per-company sequencing, no owner; the tax invoice/receipt does not appear at all. (c) **The tax point is never determined**, which is the unnamed cause of `DC-07`. (d) **No statutory filing, submission or retention object** | **ACCEPTED — CORRECTED.** Registered as `P11-F-03`; the four are added to the dependency register rather than left silently absent |
| `X3-F15` | **LOW-MED** | **Product category has no matrix row and collides with `MTI-D-03`.** `MTI-D-03` lists Product Category among what a **tenant** may configure, yet `CV-01` makes it carry a `COMPANY`-scoped costing method with a financial effect — an unregistered `SCP-03` instance and a direct ruling conflict | **ACCEPTED — CORRECTED** |
| `X3-F16` | **LOW** | **Citation hygiene** — the ¶13 row carries no ประกาศ citation, and the TAS-16M corroboration was carried without its qualifier that the TAS 16 standard text could not be retrieved | **ACCEPTED — CORRECTED** |

### 2.2 Claims Expert 3 attacked and could not break

Recorded because a challenge report listing only successes is not falsifiable.

- **`BC-02` binds Inventory → Accounting only.** Attacked via the contract's own *"for every material handoff"* wording; defeated by the approval record's title. `P11-F-02` **`SUPPORTED`**.
- **`RV-03` (`T0-07`).** Attacked as a quiet downgrade of a tolerance-zero boundary; defeated — it remains `UNRESOLVED`, tolerance-zero, with `CONDITIONAL PASS` unavailable by rule.
- **`RV-02` (`MCU-04`).** Attacked as relieving the defect via "platform data is correctly company-less"; defeated — disposition stays `CLOSED — VERIFIED DEFECT`, sharpened not softened.
- **`RV-05`'s arithmetic.** Attacked as relaxing the 10-of-10 failure; defeated. The defect found was what the subledger file *did* with the restatement, not `RV-05` itself.
- **`BLK-04` / DBD แบบ 2.** Attacked for converting a presentation fact into bookkeeping authorisation; defeated — the Accounting Act question is carried as held.
- **`SC-04` fiscal year = `COMPANY`.** Attacked as a Thai boundary error; defeated — supported by the required company field and the constraint refusing a fiscal year on a child company.
- **`CVP-04`, `CVP-05`, `CVP-06`.** Attacked against the `HOLD` on the day as pro-ration unit; defeated — P11 nowhere claims the day is statutory, and `CVP-06` mandates *recording* the convention rather than asserting one.

### 2.3 Score

| Measure | Count |
|---|---|
| Findings raised | **16** — 6 HIGH, 1 MED-HIGH + 1 HIGH(Thai) + 1 MED-HIGH(Thai), 5 MED, 2 LOW/LOW-MED |
| Accepted by P11 | **16 of 16** |
| Disputed by P11 | **0** |
| Independently reproduced a P11 self-caught error | **2** — `X3-F01`≡`P11-E-08`, `X3-F06`≡`P11-E-05` |
| P11 claims attacked and **not** broken | **7** |

---

## 3. Expert 2 — Leadership, Database Design

**Verdict: `SUPPORTED WITH CORRECTION`.** *"the core structural position (no accounting-event
object, one root behind seven recorded symptoms) survives attack, but `F8` is a schema column
mislabelled as a fact, the subledger test's stated rule is not the rule applied and collapses three
'of record' verdicts when applied as written, the 'six problems closed by one identity' is at most
three, and four load-bearing absence claims are stated at strengths their own governing CORR1 and R4
correction sections deny."*

### 3.1 The critical finding

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X2-F06` | **CRITICAL** | **The stated decision rule is not the rule applied.** `P11_SUBLEDGER_ARCHITECTURE.md` §1 declares *"a structure failing `S3` **or** `S4` is a derived view, not a subledger, and no reconciliation may be claimed against it."* §2 then awards *"of record"* to four rows that fail `S3` or `S4` — Asset (`S4` ✘), Tax (`S3` ✘), Settlement (`S4` ✘), Inventory (`S2` ✘). **Only Analytic, the one row failing both, was rejected.** The applied rule is *"fails both"*; the stated rule is *"fails either"*. Under the stated rule the register reads **3 of record, 5 derived views, 2 unknown** — and every reconciliation claim against Asset, Tax and Settlement falls with it, including semantic-model §5 Q7 and Q9 | **ACCEPTED.** A logic error, not a citation error, and the most serious finding of the round |

### 3.2 Findings — the fact model

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X2-F01` | HIGH | **`F8` is the table's own column promoted to a row.** §2 already carries a populated **Scope** column for `F1`–`F7`; `F8`'s own Scope cell reads *"itself"*, which is not a member of `{PLATFORM, TENANT, COMPANY}` — the domain `SCP-01` declares mandatory and non-null. **The model's own type rule is violated by its newest row** | **ACCEPTED.** `F8` withdrawn; the seven facts stand and scope returns to being an attribute, as `SCP-01` already says |
| `X2-F02` | HIGH | **`F8` "may it change? never" is falsified by P11's own actions** — `SCP-03` splits objects, `RV-01` restates `TI-01`'s reach, and a Boss ruling re-scoped the product master, all in one session | **ACCEPTED** — subsumed by `X2-F01` |
| `X2-F03` | HIGH | **`F2`/`F3` is not a coherent schema separation.** Amount and classification are carried at **both** levels with no stated cardinality, no aggregate invariant binding the event total to the sum of its items, and no key — the same unenforced-aggregate shape `T0-01`/`T0-12` document as the reference model's worst defect | **ACCEPTED.** The event carries no amounts; `F3` is sole carrier; event→entry cardinality stated |
| `X2-F04` | HIGH | **`F2`'s owner was silently changed and the change is undisclosed.** Wave A `06` §1 sets `F2` owner = *"the ledger"*; P11 set it to *"the owning process"* with nothing in the revision log. It also contradicts P11's own finding that three events are ledger-owned — which is why `OWN-01` had to be invented beside the model to patch it | **ACCEPTED.** Logged; `F2`'s owner becomes *"the owning process, or the ledger where the ledger emits"*, putting `OWN-01` inside the model |
| `X2-F05` | MED | **The eight-fact model has fewer attributes than the seven-fact model it extends** — Wave A's **Lifetime** column was dropped without notice | **ACCEPTED.** Restored |
| `X2-F12` | HIGH | **Scope was made a fact but the event's own key uniqueness is never declared** — identity and idempotency key, one key or two; unique per company, per tenant, or table-global | **ACCEPTED.** Key set stated explicitly |
| `X2-F13` | MED | **`DEP-01` assigns the accounting event to the wrong scope** — recorded *"platform → all ten"* while the matrix makes it `COMPANY`-owned with financial effect, which `SCP-04` mandates | **ACCEPTED.** Restated as a `COMPANY`-scoped object whose *specification* is programme-wide |

### 3.3 Findings — the subledger test, re-derived

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X2-F07` | HIGH | **AR/AP fail `S3` and `S4` on the same evidence P11 uses to fail Settlement.** The residual is `DERIVED FACT`, *"stored, therefore capable of drift"*; and entry substance while posted is *"no — application guard, **seven production bypass sites**"*, entry existence *"no — configuration, default off"*, matching records *"deleted by an entry-level operation"*. **The headline "3 unqualified" becomes 0** | **ACCEPTED** |
| `X2-F08` | HIGH | **The Asset row cites the wrong criterion and misstates its source.** `CTR-06` says the opposite in structure — *"a model constraint enforcing precisely that"*, evaluated on ORM write, **not** on a direct data load. The defect is application-only enforcement plus an unmeasured migrated population — an `S2` question, not `S4` — and P11 discarded the storage-vs-application distinction the source states in terms | **ACCEPTED** |
| `X2-F09` | MED | **The Tax row fails `S3` on a control that does not test `S3`.** Hash coverage is tamper-**evidence**, not immutability; and CORR1 `C04` governs: *"'not detected' was written where 'not **hash**-detected' was meant. Tax fields and the due date carry field-level change tracking"* | **ACCEPTED** |
| `X2-F18` | HIGH | **Element 7 fails 10 of 10 and elements 1–9 were presented as unproblematic.** Re-derived by counting R4 `16` §3's own rows: element **7 (basis)** appears in **all ten**; element **4 (when financial)** in **six**. R4 §3.1's summary names only 10/14/15 — **P11 inherited the summary rather than the table beneath it, which is the failure mode this programme's method rule exists to prevent** | **ACCEPTED.** Independently confirms `X3-F05`. *Basis unsuppliable on every handoff is a valuation-model finding, not a footnote* |

### 3.4 Findings — the "one identity closes six problems" claim

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X2-F10` | HIGH | **The six does not survive at its strongest.** (a) **Double-counted** — ownership is a *separate* attribute, element 17, which P11 itself says does not exist as a requirement. (b) **Not closed** — period re-attribution is caused by a layer-4 numbering store with *"no dimension at all"*; an event carrying an intended date does not constrain the entry's date, which is why `OWN-03` and `PCP-05` had to be asserted separately. (c) **Not exclusive** — a **genuine database constraint** `unique (unique_import_id)` was verified by CORR1 Reviewer B `N1`; an idempotency key is an attribute and exists today with no accounting-event object | **ACCEPTED.** Restated to **three** — duplicate detection, correction semantics, the audit question. `P11-B-02`'s *"the root"* framing and `DEP-01`'s status line are re-derived accordingly |
| `X2-F14` | HIGH | **"9 of 23 dependencies sit downstream" is asserted twice and enumerated nowhere** — an unenumerated count, against P11's own POPULATION/PATTERN rule. And `DEP-01`'s *"nothing downstream is closable without it"* is contradicted by the same file's §3 (*"six of them cost hours"*) | **ACCEPTED.** Figure withdrawn; the sentence deleted |

### 3.5 Findings — integrity, storage level vs application guard

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X2-F11` | HIGH | **The `F7` absence is stated at a strength the governing correction denies.** P11 wrote *"`F7` is not implemented at all"* and *"element 15 does not exist today"*. CORR1 `C04`/`C11` govern: **`PARTIALLY VERIFIED`** — *"a real database constraint exists, but only with an optional module installed, and it is **table-global rather than tenant-scoped**. `N1` re-scoped, not withdrawn."* The surviving claim is *"no **general, mandatory** carrier was found in `addons/account`"*. **This is P11's own stated method rule violated at its most load-bearing claim** | **ACCEPTED.** All three restated to the `N1` form — **and the scope mismatch registered**: the one idempotency constraint that exists is **table-global with no tenant scoping**, a new `SC-` row |
| `X2-F19` | HIGH | **`F6`/close is mischaracterised and the file contradicts itself in adjacent sentences.** Wave A `12` §2: *"no artefact — only a **tracked field change on the company record**"*; CORR1 `N11`: *"**lock-date changes are tracked and lock exceptions are first-class records.** The governance conclusion is unchanged."* And the hard lock's forward-only movement is **one of exactly two unconditional immutabilities in the reference core ledger**, by a monotonic write guard — an enforcement fact *"a bare date with no object behind it"* erases | **ACCEPTED** |
| `X2-F20` | MED | **The storage/application distinction is made in one file and dropped everywhere else.** Four storage-level facts never carried: entry-number uniqueness is a **partial** unique index so duplicate numbers are **reachable while draft**; **four per-item rules are genuine DB CHECK constraints while the balance invariant is not**; the rate table carries real constraints `unique(name,currency_id,company_id)` + `CHECK(rate>0)`; the reconciliation model declares **zero** DB constraints | **ACCEPTED.** An *"enforced at"* column (storage / application / configuration / none) added to the fact model and the subledger register. *Without it the SMEsPlus design will re-derive its constraints from application-level statements* |
| `X2-F21` | MED | **`RC-05` as written is contradicted by the evidence base.** *"Reversal → original: **yes**, a stored link, plus messages on both."* What does not exist is the **corrected-entry → entry-it-corrects** link; and `BW-35` is *"no **constraint** on the link"* | **ACCEPTED.** Restated; `RCP-03` survives, the `DC-01` bridge weakens and is re-argued |
| `X2-F22` | MED | **The scope matrix asserts integrity properties the same package denies** — the hash chain row is unmarked while `SC-07` and `COR-06` record that it omits the transaction-currency amount and *"the write guard also fails open on the canonical amount field"* — `CONTRA-01b`, *"the true integrity hole"* | **ACCEPTED** |
| `X2-F23` | MED | **"Journal entry / item … immutable once posted" is stated as present-tense fact** in a table that flags other rows as target-state, while the evidence records **seven production bypass sites** and an audit-trail ratchet that *"locks the protection off at first posting"* by default | **ACCEPTED** |

### 3.6 Findings — counts, denominators, register hygiene

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X2-F15` | HIGH | **Undetected count error.** *"The remaining **26** rows pass `C2`–`C4`"* — 44 − 13 failing rows = **31**, and §5 enumerates exactly 31 ids. `P11-E-01` re-derived the `C2` headline in that same file and left this second count untouched | **ACCEPTED.** 26 → 31 |
| `X2-F16` | HIGH | **Two incompatible "no determined owner" sets across three files.** The business-event register names **8**; the ownership register names **9**; the sets share five members and differ on seven. `P11-E-01` logged the 8→9 **number** and missed the **membership** divergence, which is the more serious half | **ACCEPTED.** Reconciled to one set with one definition |
| `X2-F17` | MED | **Two mutually inconsistent "six of fifteen"** — the table names **seven** rows, and the semantic model claims a *different* six including `JT-08`, which has no matrix row at all | **ACCEPTED.** Corrected to seven; the two files aligned |
| `X2-F24` | MED | **The claim the non-convergence argument rests on is contradicted by its own table.** *"Not one of the twenty-one carries a terminal state stronger than `HOLD`"* — yet `SL-21` is the canonical baseline, terminal state **"Canonical"**, and `BC-01`…`BC-03` are `BOSS APPROVED / EFFECTIVE`, which P11's own class table ranks *"Yes, and it governs"* | **ACCEPTED.** Restated over the **twenty research packages**. *The conclusion survives; the arithmetic as written does not* |
| `X2-F25` | LOW | **`COR-07` attributed to the wrong tolerance-zero id** — it belongs to `T0-01`, with `T0-11`/`T0-12` recorded as attacks on the same invariant from different directions | **ACCEPTED** |
| `X2-F26` | LOW | **`DC` class arithmetic** — §6 reports 17 while §3 tabulates 12 rows; `DC-03b` was run and dispositioned but excluded from both the denominator and the *"0 of 17"* headline | **ACCEPTED.** Also self-caught as `P11-E-07` |

### 3.7 Claims Expert 2 attacked and could not break

- **`0 of 10 peer processes have published anything.`** Population, pattern, path set and unit declared before the count; the `P0[1-9]`/`P10` glob defect self-logged; the snapshot time-stamped and described as a reading at an instant. *"I could not find an author-chosen boundary. This is the cleanest denominator declaration I have seen in this programme."*
- **The negative-claim boundary in the double-counting register.** Attacked by looking for a row written as class `A`; the closest carries its own stated search scope. *"The boundary holds — which is precisely why `X2-F11` is a defect against P11's own standard rather than a defensible inheritance."*
- **`RV-05` did not relax.** Attacked expecting the correction to have quietly relieved a failing count; the reasoning and the supporting evidence hold, and the direction of every revalidation is recorded rather than assumed.
- **`DC-09`.** Attacked by searching the Asset and Inventory packages for a relief mechanism, and for a package with both halves in view. *"I found neither… `DC-09` as NEW at P11 stands."*
- **`P11-C-01`.** The two commit timestamps and file inventories check out; the finding that `AASR`'s own `V-SYS-2` now applies to `AASR` is sound and is dispositioned as a contradiction rather than used to discount `AASR`.
- **`SR-04`/`DC-07` restraint.** Attacked by looking for a later escalation of the unknown to a defect; there is none.
- **`SRP-01`/`SR-01`.** *"The one place P11 gets the storage-vs-application distinction fully right, and it is exactly where it matters most."*

### 3.8 Score

| Measure | Count |
|---|---|
| Findings raised | **26** — 1 CRITICAL, 12 HIGH, 10 MED, 3 LOW |
| Accepted by P11 | **26 of 26** |
| Disputed | **0** |
| Independently reproduced a P11 self-caught error | **1** — `X2-F26`≡`P11-E-07` |
| Independently reproduced Expert 3's finding | **1** — `X2-F18`≡`X3-F05` (elements 4 and 7) |
| P11 claims attacked and **not** broken | **7** |

---

## 4. Expert 1 — Leader, Functional Design

**Verdict: `SUPPORTED WITH CORRECTION`.** *"P11's method, its refusal to fabricate the event-to-GL
matrix, and its cross-domain findings are sound and are the package's real contribution — but the
business-event register is not the enumeration it presents itself as: it publishes four wrong or
mutually contradictory counts, under-extracts three of its own declared sources including a
Boss-approved control, contradicts Boss ruling `MTI-D-01` while citing it, and lists an undecided
decision package among the controls that govern it."*

### 4.1 Findings — authority and control integrity

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X1-F01` | **HIGH** | **An ownership assertion contradicts the Boss ruling it cites as its authority.** `D-01` rules `OPTION B — Company-owned Product Master`, and its §4 records the ruling *"supersedes the earlier AAS+ recommendation that preferred tenant-level product master with company-level attachment."* **P11 reinstated the superseded position and attributed it to the ruling that killed it** | **ACCEPTED — CORRECTED.** Third independent detection (`X3-F06`, `P11-E-05`) |
| `X1-F02` | **HIGH** | **A control listed as `BOSS-APPROVED` and governing is an undecided decision package.** `BC-04` sits in the table headed *"Boss-approved controls that **govern** this reconciliation"*, while the GB-08 artefact reads **`BOSS DECISION REQUIRED — GB-08` / "This file does not select an option"** — and P11's own `DEP-14` says *"packaged, not decided"*. **§1's declared POPULATION (*"named in a `BOSS-APPROVED` control"*) is contaminated until this is fixed** | **ACCEPTED — CORRECTED.** `BC-04` reclassified out of §3 into §4 as `PEER-PUBLISHED`, pending decision |
| `X1-F03` | **HIGH** | **Five Boss-approved `BC-01` scenarios name business events absent from the register, and 13 of 22 scenarios are never cited.** Missing: **10** cancellation before physical execution, **11** correction after physical execution, **12** inventory count / adjustment, **14** internal warehouse transfer, **18** stockable vs consumable vs service routing. Re-derived: 9 of 22 scenarios cited anywhere; **no `BC-01`→`UBE` coverage map exists** | **ACCEPTED — CORRECTED.** *"`P11-B-10` counts the 22 for proof; it does not discharge extraction"* |

### 4.2 Findings — counts and the enumeration itself

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X1-F04` | **HIGH** | *"The remaining **26** rows pass `C2`–`C4`"*; §5 lists **31**. *"This is `GB-06`'s shape, uncaught, in the file whose §5 lectures the reader about `GB-06`"* | **ACCEPTED.** Independently confirms `X2-F15` |
| `X1-F05` | **HIGH** | **The `C2` correction was applied and the identical defect in `C3` and `C4` was not.** Re-derived: `C3` FAIL = 11 rows but **9 business facts**; `C4` FAIL = 3 rows but **1 business fact** — both published *"of 44"*, a business-event denominator. The semantic model propagates it | **ACCEPTED — CORRECTED** |
| `X1-F06` | **HIGH** | **Two uncorrected instances of the very figure `P11-E-01` says was corrected.** *"The correction is a note beneath, not an edit. A reader who takes the headline — which is what the programme's own adversarial-section rule warns against — gets 8"* | **ACCEPTED — CORRECTED in place**, note retained as lineage |
| `X1-F07` | **HIGH** | **Three mutually inconsistent published counts of "events with no determined owner"**: the register's prose says 8; the register's own table says **4** rows read `NOT DETERMINED`; the ownership register says 9 with a different membership | **ACCEPTED — CORRECTED.** With `X2-F16` |
| `X1-F08` | **HIGH** | **A declared PATTERN adopts an author list as a denominator — the programme's named recurring defect.** P11 declared *"9 `INV-OWNED`"*; R4 `16` §2 declares **`INV-OWNED` = 14**. The 9 is the row count of a narrative section. **Five `INV-OWNED` handoffs are silently outside P11's declared extraction surface** | **ACCEPTED — CORRECTED.** The single most serious method finding against P11: it is the exact defect P11's own source-link register exists to prevent |
| `X1-F14` | **MED** | **The "denominator `UNBOUNDED`" disclaimer is honest as to the *business* and a shield as to the *published evidence*.** The published extraction surface **is** bounded and enumerable, and P11 under-extracted it four ways — none of it blocked on `P01`–`P10`. *"The blocker register's own closing line applies to P11's own enumeration and is not applied to it"* | **ACCEPTED — CORRECTED.** The disclaimer is split in two, with a per-source extraction-coverage table |

### 4.3 Findings — events missing from the register

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X1-F09` | **HIGH** | **Six events named in artefacts P11's own PATTERN cites, absent from the register**: vendor credit/debit note; budget line consumed; shared account used by a second company; `HO-11` adjustment fact; `HO-21` internal warehouse transfer; `HO-22` inter-company transfer as a paired sale and purchase. *"P11 asserting a dependency (`DEP-20`) on an event it never registered is not coherent"* | **ACCEPTED — CORRECTED** |
| `X1-F10` | **HIGH** | **Six Asset events absent, one mis-presented as settled.** `UBE-29` cites `BD-01` as settling internal usage; the source states *"a fully depreciated asset can be made depreciable again by a capital improvement. **`BD-01` is silent**"* and warns *"running both would count the same machine twice"* — **a double-count with no `DC` class**. Also absent: equipment transferred between sites; cost revaluation; repair vs capital improvement; useful-life/residual review at year end; impairment; reclassification/transfer/split/merge | **ACCEPTED — CORRECTED.** The re-entry double-count is registered as a new `DC` class |
| `X1-F15` | **MED** | **Missing period-governance events in the process P11 assigns period attribution to.** `AE-16` period reopened (*"no distinct authority required"*) and `AE-17` finality overridden are not registered, **while P11 asserts `OWN-03`, `PCP-03` and `PCP-04` about exactly those acts** | **ACCEPTED — CORRECTED** |
| `X1-F16` | **MED** | **One of the three "ledger-owned business events" is not one of the 44** — the reversal half of correction has no `UBE`, yet is counted against a denominator of 44 | **ACCEPTED — CORRECTED** |
| `X1-F21` | **LOW-MED** | **No service or non-stockable revenue path exists anywhere in the package.** `P02` has no *"service rendered / performance obligation satisfied"* event, so revenue is tied to invoice issuance or goods delivery only. **For a Thai SME suite this is a material coverage hole**, and Boss ruling `D-01`'s own worked example is a **transport service** | **ACCEPTED — CORRECTED** |
| `X1-F22` | **LOW-MED** | **Non-sale stock reductions collapsed into one production event.** R4 distinguishes **scrap, shrinkage, write-down and adjustment** as four things that must be separately identified and records `L5-09` as the *semantic collapse* defect. **P11 restates the fix as `CVP-07` and leaves the register in the collapsed shape the fix exists to prevent** — and files warehouse scrap under a manufacturing process | **ACCEPTED — CORRECTED** |

### 4.4 Findings — internal coherence

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X1-F11` | **HIGH** | **Unqualified negative existence claims in registers other than the one that declares the boundary.** *"No variance mechanism exists in 797 modules"* and *"`ABSENT` in 797 modules"* are published without the source's own cap: *"**every 'does not exist' in both research packages is bounded by the source trees in this workspace. That qualifier cannot be dropped until the running system's installed modules are known**"* (`Q-04`, priority 1) | **ACCEPTED — CORRECTED.** The double-counting register's §1 boundary is applied package-wide |
| `X1-F12` | **HIGH** | **The register states a one-owner rule, breaks it in six rows, and the ownership test scores those rows as passing `C2`.** And `UBE-03`/`UBE-12` inherit their predecessor's semantics but not its `C3` FAIL | **ACCEPTED — CORRECTED** |
| `X1-F13` | **HIGH** | **The owner population is never declared.** Owners asserted include `Inventory` (7 rows), *"the ledger"*, *"governance"* and *"contested"*; the close file tabulates **eleven** processes. **This is the exact `DENOMINATOR COMPLETENESS` element (POPULATION) P11 enforces on itself for events and never applies to owners** | **ACCEPTED — CORRECTED.** Owner population declared before any `C2` verdict |
| `X1-F17` | **MED** | **A mandatory statutory treatment rendered as optional.** `UBE-26` says *"expense **or** conversion cost"*; the closure states *"**absorption is required, not merely permitted**"*. *"A functional designer reading only the event register would treat absorption as a configuration choice"* | **ACCEPTED — CORRECTED** |
| `X1-F18` | **MED** | **A design position placed inside a table of closed statutory positions** — the actual-hours rejection is faithfully sourced but `BLK-07` is `HOLD` with an AAS+ veto | **ACCEPTED — CORRECTED.** With `X3-F03` |
| `X1-F19` | **MED** | **`P09`'s risk routed to a class that does not cover it** — `DC-09` is double cost absorption and has no `P09` content; no class covers *"a read-only consumer emits a posting"* | **ACCEPTED — CORRECTED.** Re-pointed to `C4-01`/`DC-16` |
| `X1-F20` | **LOW-MED** | **Process naming vs process content.** All three payment events filed to `P06` leaves `P01` **Procure-to-Pay** with no pay step, `P02` **Order-to-Cash** with no cash step and `P05` **Expense-to-Pay** with no pay step. The filing is sourced, but *"a Thai SME reader will look for AP payment in `P01` and not find it"* | **ACCEPTED — CORRECTED.** The boundary is stated explicitly |

### 4.5 Claims Expert 1 attacked and could not break

1. **The 44-event register is internally complete as a list** — extracted by regex: 44 rows, no gaps, no duplicates, subtotals 9+8+7+6+3+3+4+4 = 44. *"The membership is attackable; the arithmetic is not."*
2. **The 32-accounting-event arithmetic and "27 of 32"** — all re-derived and correct.
3. **"15 rows, 30 withheld cells"** — counted independently from Wave A `08` Part 2; `UAE-24` correctly excluded. Exact.
4. **The refusal to fill the event-to-GL matrix** — *"I looked for any cell filled from convention or from a peer WIP file. There are none… §1 is the strongest passage in the package and it does what it says."*
5. **`RV-05`** — tried to construct a scope argument relaxing element 10 for any of the ten; all ten create a financial effect, so `SCP-04` forces `COMPANY`. Holds.
6. **`CVP-02`'s `REJECTED — INVALID ASSUMPTION`** — survives at source in those exact words; only its *placement* is defective.
7. **`UBE-19`'s two-basis divergence** — carried accurately, including the correction that supersedes the Asset baseline's own `C-01`/`C-02`.
8. **`DC-09` as new at P11** — searched both packages for any relief-entry or absorption-offset concept; *"nothing describes one… the reasoning is sound and is genuinely only visible cross-domain."*
9. **The `P09` read-only conclusion** — the upstream `INFERENCE` label was not upgraded, and P11's extension is labelled `P11-DERIVED, SUPPORTED INTERPRETATION`. *"Correctly handled."*
10. **`P01`–`P10` published nothing** — *"Not testable from my position… I did not attack it and I do not endorse it; it is `NOT DECIDABLE` from this review."* **Recorded as stated: this reviewer declined to endorse the package's central premise rather than assume it.**

### 4.6 Score

| Measure | Count |
|---|---|
| Findings raised | **22** — 13 HIGH, 5 MED, 4 LOW-MED |
| Accepted by P11 | **22 of 22** |
| Disputed | **0** |
| Independently reproduced another expert's finding | **2** — `X1-F01`≡`X3-F06`, `X1-F04`≡`X2-F15` |
| Independently reproduced a P11 self-caught error | **1** — `X1-F01`≡`P11-E-05` |
| P11 claims attacked and **not** broken | **9**, plus 1 declined as `NOT DECIDABLE` |

---

## 5. Expert 4 — Lead, Code & UI Architect

**Verdict: `SUPPORTED WITH CORRECTION`.** *"the package's terminal `HOLD`, its 21 verified SHAs and
its refusal to fabricate the 30 withheld cells all stand, but its single load-bearing peer claim is
now contradicted by two published peer branches, its own intake script's section C is provably
inert, and seven headline counts disagree with the tables beneath them."*

**Declared negative-claim boundary of this review:** git checks bounded by `origin` at 136 heads,
fetched during the review; document checks bounded by the 26 package files and the upstream trees.
*"I read no reference-ERP source. 'Not found' below never means 'does not exist'."*

### 5.1 The two critical findings

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X4-F01` | **CRITICAL** | **`0 of 10 peers published` is CONTRADICTED at review time.** Two peer branches now exist, both carrying a handoff pack addressed to P11, and `P03` carrying its own event-to-GL matrix. §5's table **has no snapshot stamp** — unlike the WIP snapshot — so it reads as a standing state | **ACCEPTED.** Independently found by P11 in parallel; the count reached **6** before the session closed. See `P11_PEER_INTAKE_DELTA_01.md` and §5.4 below |
| `X4-F02` | **CRITICAL** | **`peer_intake.sh` section C is inert and always has been.** `set -e` plus a piped `for` loop kills the subshell at the first ref with no match — `origin/SMEsPlus`, enumerated first — so declared PATTERN (b) **could never return a hit**. Proven: the identical loop with `set -e` returns 0 lines; without it, **46** matching paths today. *"The published `(end C)` was accidentally correct at publication… but the check cannot detect what it declares to search"* | **ACCEPTED — CORRECTED.** Script rewritten as v2 with `set -e` removed from C, `|| true` per ref, and a **positive control** so an empty C is evidence rather than an artefact. Re-run: control returns **86** matching paths. **P11's own evidence script was broken, and only an executed independent re-run found it** |

`X4-F02` is the most important finding of the whole round. It is `P11-E-03`'s defect — a pattern that
cannot cover its declared population — recurring in the very artefact written to prevent it, and it
was invisible to every reading of the script.

### 5.2 Count integrity — Expert 4's re-derivation

Twenty-seven headline figures were independently re-derived. **Seven disagree.**

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X4-F03` | HIGH | *"the remaining **26** rows pass"* → **31** | ACCEPTED (third detection) |
| `X4-F04` | HIGH | **`C3` and `C4` mix denominators** — 2 of 11 `C3` FAILs and 2 of 3 `C4` FAILs are not members of the 44. Business-fact figures are `C3` **9 of 44**, `C4` **1 of 44**. *"The identical defect P11 self-caught as `P11-E-01` for `C2` and did not re-run for `C3`/`C4`; the §2 headline still reads 8 of 44 uncorrected"* | ACCEPTED (with `X1-F05`/`X1-F06`) |
| `X4-F05` | HIGH | **§4's three `C4` failures are not the §3 table's three** — `C4-03` has no §3 row; `UAE-05`'s `C4` FAIL has no §4 narrative | ACCEPTED |
| `X4-F06` | HIGH | Two different "no determined owner" sets, both published; **only 4 rows actually carry `NOT DETERMINED`**. §3.1 conflates *owner undetermined* with *timing/basis undetermined* | ACCEPTED (with `X1-F07`, `X2-F16`) |
| `X4-F07` | HIGH | **The 44 does not cover its own declared PATTERN** — zero occurrences of "adjust", "transfer", "cancel"; and **`UBE-01` and `UBE-10` cite `BC-01` scenarios that name different events**, so 2 of 44 are author-supplied against a population defined as *"named in the evidence"*. *"`DC-13` cross-company leakage currently has no business event behind it"* | ACCEPTED (with `X1-F03`) |
| `X4-F08` | HIGH | **"`DEP-23` blocks 15 of the 30 withheld cells" is arithmetically impossible** — cells are paired per row, so any peer-blocked subset is **even**. Re-derived: **16** | ACCEPTED |
| `X4-F09` | MED | *"Six of the fifteen rows"* — the table lists **seven** | ACCEPTED (with `X2-F17`) |
| `X4-F10` | MED | **`27 of 32` is true over the wrong denominator** — the 32 includes 7 Class-C events that *do not exist* and cannot have a posting pattern; over extant events it is **20 of 25**. And `M-01`…`M-05` are not `UAE` ids, so no reader can map the 5 into the 32 | ACCEPTED — both ratios published, `M-` ids mapped |
| `X4-F11` | MED | *"Four `HOLD — SCOPE EVIDENCE REQUIRED`"* — only **3** rows carry `HOLD`; budget's row reads `tenant-owned` | ACCEPTED |
| `X4-F12` | MED | *"15 lanes. 2 reach a statement line without an unresolved break."* By the ✘ test **3** lanes carry no ✘; by the unresolved-break test **0** do — *"the same sentence concedes both named lanes end on an open tolerance-zero / contract failure"* | ACCEPTED (self-caught in parallel as `P11-E-06`) |
| `X4-F13` | MED | *"Three of eight facts absent or degenerate"* **excludes `F2`** — the accounting event, whose absence is the package's own root blocker | ACCEPTED — 3 → 4, `F2` made the headline degeneracy |
| `X4-F19` | LOW | `CONTRA-03` counted among the 14 with an **empty** description; `FC-F5` described only by cross-reference. 2 of 14 unverifiable as published | ACCEPTED |
| `X4-F21` | LOW | `peer_wip_snapshot.sh` declares POPULATION `ACCOUNT_P??_*` but its PATTERN is `P0[1-9]` + `P10`; and it counts **untracked only**, so a peer that commits locally reads as empty | ACCEPTED — pattern aligned, both measures reported |
| `X4-F22` | LOW | **Prohibited-wording grep is clean** — no `PASS`/`APPROVED`/`FROZEN`/`MERGED`/`IMPLEMENTATION AUTHORIZED` used as a verdict. Residual: lowercase `pass` as a cell value and the heading *"Events passing `C2`, `C3` and `C4`"* | ACCEPTED — changed to `SATISFIED` / `NOT SATISFIED` |

### 5.3 Method and enforceability

| id | Sev | Finding | P11 disposition |
|---|---|---|---|
| `X4-F14` | MED | **The blanket class-`C` demotion is over-broad and internally inconsistent.** *"Not one of those packages has declared which of 22 roots it searched"* is contradicted by `SL-13` (797 modules re-counted, exhaustive, *FACT VERIFIED (negative, workspace-bounded)*) and by `SL-01`'s GB-08 trace (*"searched all 22 roots… the two tests agree on all 22 roots"*). **`MCU-21` is *which root SMEsPlus targets*, not *which scope was searched*** — and P11 simultaneously **relies on** the 797-module negatives as fact | **ACCEPTED.** A logical error: P11 conflated **applicability** with **verification**. Split into *search boundary declared* vs *target root undeclared, so applicability unknown* |
| `X4-F15` | MED | **`MCU-01…MCU-20 \| 17 standing gating unknowns` carries the parent's headline over its §7 correction** — the set is recorded as **17 → 11 → 18 → 17, "oscillating, not converging"**; and the range omits `MCU-21`/`MCU-22`, both cited elsewhere in P11 | **ACCEPTED.** The adversarial-section rule violated by P11 itself |
| `X4-F16` | MED | **No position is enforceable as written.** *"1,972 lines contain no storage, runtime, API or UI vocabulary — no enforcement point, mechanism, detection test or failure action for any of the 49 positions"* | **ACCEPTED.** Four columns added to every position table |
| `X4-F17` | MED | **Runtime/UI reality gap.** `RCP-01` and `OWN-03` remove the two operations users actually use to fix errors, and the correction architecture is **ledger-side only** — the source-document cancel/amend path is never addressed. *"In a real ERP the users will delete and re-key the source document instead, reproducing `DC-01` one layer up, unlinked"* | **ACCEPTED.** A genuinely new defect class, found by asking what operators will actually do |
| `X4-F18` | LOW | `CVP-02` pre-decides a reserved decision under a standing veto | ACCEPTED (with `X3-F03`, `X1-F18`) |
| `X4-F20` | LOW | **P11's own branch is not on `origin`.** *"By §6's own standard the package cannot be verified by a reviewer — the test it applies to the peers"* | **ACCEPTED.** Pushed before the gate; both evidence outputs stamped |

**Expert 4's enforceability triage — carried into the Boss pack verbatim.** Enforceable at storage or
one runtime choke point: `OWN-01`, `OWN-03`, `OWN-04`, `SCP-01`, `SCP-02`, `SCP-04`, `SCP-06`,
`CVP-03`…`CVP-07`, `SRP-02`…`SRP-06`, `TXP-01`…`TXP-04`, `ANP-01`, `ANP-02`, `PCP-01`…`PCP-04`,
`PCP-06`, `PCP-07`, `RCP-01`, `RCP-02`, `RCP-03`, `RCP-05`, `RCP-07`. *"`ANP-05` ('P09 emits no
posting. Ever.') and `SRP-03` ('the balance assertion is not suppressible') are the two strongest and
cheapest in the package — one is a revoked grant, the other a deferred constraint trigger plus a CI
grep for bypass tokens."*

**Not enforceable as written** — `OWN-05` (a sequencing instruction, not a system rule); `OWN-06` /
`ANP-03` (*"must prove they agree"* with no tolerance, timing or action — unfalsifiable);
`ANP-04` (forbids both branches, no predicate); `SCP-03` (design-time/CI only); `SCP-05` (the points
of effect are never enumerated, so the deny cannot be sited); `SRP-01` (names no mechanism, and
*"in a Node/ORM stack this becomes an application guard by default"*); `CVP-01` (no pairing key or
granularity); `RCP-04`/`PCP-05` (enforceable only after `UAE-32` exists); `RCP-06` (*"business
identity" is nowhere defined*); `TXP-05` (a governance rule, not a system position).

### 5.4 Claims Expert 4 could not break

- **All 21 `SL` SHAs and branch names verify exactly** — *"the most disciplined source register I have reviewed in this programme."*
- **`P11-C-01`** re-derived independently to the second and the file count.
- **`SL-18` is a governance container only**; **`0 of 10` handoffs and `BC-01`'s 22**; **797 modules**; **the 48-token bucket** — all reproduce verbatim.
- **The refusal to fill the 30 cells** — *"the correct call, argued correctly; `X4-F01` changes who is blocking, not whether the cells may be filled from convention."*
- **`DC-09` and `DC-07`** — *"genuinely new, correctly classed… I could not find either stated in the upstream packages."*
- **`P11-E-01`** — *"a real self-catch of the `GB-06` shape, logged honestly — the correction is just incomplete."*

### 5.5 Score

| Measure | Count |
|---|---|
| Findings raised | **22** — 2 CRITICAL, 6 HIGH, 9 MED, 5 LOW |
| Accepted by P11 | **22 of 22** · Disputed **0** |
| Headline counts re-derived | **27**, of which **7 disagree** |
| P11 claims attacked and not broken | **8** |

---

## 6. Round score

| Measure | X1 | X2 | X3 | X4 | **Total** |
|---|---|---|---|---|---|
| Findings raised | 22 | 26 | 16 | 22 | **86** |
| Accepted by P11 | 22 | 26 | 16 | 22 | **86** |
| **Disputed by P11** | 0 | 0 | 0 | 0 | **0** |
| CRITICAL | 0 | 1 | 0 | 2 | **3** |
| HIGH | 13 | 12 | 7 | 6 | **38** |
| Claims attacked and not broken | 9 (+1 declined) | 7 | 7 | 8 | **31** |

**Cross-confirmations — the same defect found independently by more than one panel:**
`X1-F01` ≡ `X3-F06` ≡ `P11-E-05` (Boss ruling `D-01` inverted, **three** detections);
`X1-F04` ≡ `X2-F15` ≡ `X4-F03` (26 → 31, **three**);
`X2-F18` ≡ `X3-F05` (handoff elements 4 and 7);
`X1-F05`/`X1-F06` ≡ `X4-F04` (`C3`/`C4` denominators);
`X1-F07` ≡ `X2-F16` ≡ `X4-F06` (owner-set membership, **three**);
`X2-F17` ≡ `X4-F09` (six vs seven);
`X1-F18` ≡ `X3-F03` ≡ `X4-F18` (`CVP-02` pre-decides `BLK-07`, **three**).

> **Six defects were found independently by two or more panels. Three were found three times.**
> That is not redundancy — it is the measurement that matters: **a defect found once by one reviewer
> could be that reviewer's error; a defect found three times by three lenses is the package's.**
>
> **0 findings were disputed by P11.** That figure is reported as a warning, not a credential. A
> synthesis that concedes every point either had many real defects or is not defending its
> positions. On the evidence of §4.5, §5.4 and the 31 claims that survived attack, the first is the
> case — but the second cannot be excluded by the party conceding.
