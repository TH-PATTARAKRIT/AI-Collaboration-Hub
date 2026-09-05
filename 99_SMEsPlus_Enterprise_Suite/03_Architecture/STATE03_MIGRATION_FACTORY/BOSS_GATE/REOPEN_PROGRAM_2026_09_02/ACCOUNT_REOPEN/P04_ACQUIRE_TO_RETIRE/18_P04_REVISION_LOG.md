# 18 — P04 REVISION LOG

Layer: **2 — audit quarantine**.

What this session corrected — in prior packages, in its own parallel research
streams, and in itself.

---

## 1. Corrections to prior packages

| ID | Prior statement | Correction | Evidence | Severity |
|----|-----------------|------------|----------|----------|
| **P04-REV-01** | The reference population is **797 modules** — stated in **22 files across two prior packages** — 10 in P2 and 12 in P3; P1 predates source access — once classified `FACT VERIFIED (negative)` | **797 entries · 791 directories · 790 installable modules.** The figure repeated as a population was a directory-listing entry count | Executed directly: listing, type-filtered find, manifest search | Low for conclusions, **High for method** — no negative finding changes, but a denominator repeated across 22 files, and once classified FACT VERIFIED, was never executed |
| **P04-REV-02** | *"Two live mechanisms carry machine cost into product cost, and a third is proposed"* | **Nine distinct paths** under a declared enumeration unit (own rate field, own driver, or own destination ledger) | Rate-field and cost-computation sweep across the manufacturing, manufacturing-accounting, work-order and project modules | **High** — it widens the AAS+ veto's second limb |
| **P04-REV-03** | *"Depreciation already reaches production cost centres through the analytic distribution"* — named as one of two live mechanisms underpinning the veto | **It nets to zero.** Both lines of a depreciation entry carry the distribution; analytic-line creation applies no account-type filter; the amounts are computed from the signed balance and cancel | Traced the analytic-line creation path end to end | **High** — a control believed to exist does not |
| **P04-REV-04** | The custom asset-to-equipment module has **two** unimported model files (itself a correction of an earlier "one") | **Three** are unimported. Five of eight model files are imported | Full import-chain read | Low for function, Medium for code health |
| **P04-REV-05** | Company-optional master data across four object classes is a multi-tenant-safety failure | **Narrowed to one class.** A defect for the work centre, which creates a financial effect; **not** a defect for the machine register, which is legitimately tenant-scoped | Scope-aware analysis under the mid-session constitution correction | Reclassification — see `20` §4.1 |
| **P04-REV-06** | The upward-traversing visibility rule is a SaaS-security defect | **Re-classified.** Certainly a company-scope accounting-visibility defect; a tenant-security defect **only if** company hierarchies can span tenants — which P04 cannot determine | Record rules read directly; scope model applied | Reclassification — see `20` §4.2 |

## 2. Corrections this session made against itself

| ID | What happened | Why it is recorded |
|----|---------------|-------------------|
| **P04-REV-07** | A search-result summary asserted that a **30-day advance notice** to the assessment officer is required before writing off a fixed asset. Reading the underlying ruling in full showed it says the **opposite** on its facts — deduction was allowed **without** prior notice — and that the 30-day regime belongs to a **different instruction** whose scope names goods and scrap, not fixed assets | The false statement was one paragraph away from being written into a statutory register as FACT VERIFIED. It was caught by reading the source rather than the summary. The residual question is registered as `P04-B-24` **HOLD / EVIDENCE REQUIRED** rather than answered by inference |
| **P04-REV-08** | An early reading of the runtime capture suggested the whole live asset population originates from migration, on the strength of migration-namespace external identifiers | Reading the capture **script** showed its identifier query was restricted to a **hand-picked list of 26 names**. The result is not a population statement. Downgraded to `UNRESOLVED` and registered as `P04-B-02`. The safe inference — that the population was created by a path that attaches no asset model — is recorded separately and explicitly as **SUPPORTED INTERPRETATION**, with the three mechanisms that remain consistent with it named |
| **P04-REV-09** | Three parallel research streams in this session enumerated the **same** custom-addon population and returned **60**, **46** and **65**. One concluded *"no custom module touches the asset domain"* — a **false negative on a load-bearing question** | Settled by direct execution: **65 directories, two asset-touching modules, five file hits plus one manifest dependency**. Preserved in full at `05` §6 rather than silently corrected, because it is direct evidence for the standing lesson that independent verification is the only control that catches this class |
| **P04-REV-10** | An internal consistency check across the package found **five blocker identifiers referenced in one file and absent from the blocker register** — asset tagging and physical verification, component depreciation, third-party compensation, the received-not-billed recognition gap, and value-added tax on the sale of a fixed asset | They were registered as `10` §7A. The check itself is the point: a register that other files cite but do not populate is exactly how an open item stops appearing. The same defect this package documents across three prior packages (`08` §5) was present in its own first draft, and was caught by executing a cross-reference rather than reading the register |
| **P04-REV-11** | The **independent adversarial reviewer** asserted that this package's lock-date evidence citation was disproved — *"no such test exists"* — having enumerated the lock-date occurrences in the asset module's **main test file** only | The test exists, in the module's **board-computation** test file. It sets a fiscal-year lock of 30 June 2021 and asserts a 31 December 2020 entry of 12 000 posting as **31 July 2021** — seven months later, into the following fiscal year, at full value. Every particular the review called wrong is right. **This is the third instance in this session of an enumeration bounded to a subset of its own population producing a confident false negative** — and it was committed by the reviewer briefed specifically to catch that defect. The reviewer's *methodological* point was adopted: the citation now names the test and its file |
| **P04-REV-12** | One finding carried **two identifiers** — `P04-F-18` and `P04-F-23` were the same blank-account-drops-a-leg finding, both cited downstream | Merged onto `P04-F-23`; `P04-F-18` **withdrawn**, with the withdrawal stated at the surviving row rather than silently deleted |
| **P04-REV-53** | **The models were partitioned at `P04-F-116`; the findings were not, which is the partition a reader actually needs.** P07 took that step first and reported the first finding it holds sitting on **opposite sides** of the copy-identity and stack-completeness questions. Done here across all 116: **27 rest on a complete declared stack** (`account.asset`, no installed module outside the declared scope), 25 are partly exposed on `account.move`/`.line`, 2 on `account.account`, **6 carry the unreadable-stack exposure**, and 56 are not model-bound. The six are `P04-F-35`, `-37`, `-38`, `-39`, `-40` — the asset-to-equipment findings in `05` — and `P04-F-108`. **A reader can now tell which six to discount and which twenty-seven not to.** `P04-F-118`. **The classifier over-reported and was corrected before publication.** Its first run returned **12**, assigning by the model vocabulary a finding's text uses — and six of those (`P04-F-94`, `-97`, `-102`, `-107`, `-114`, `-116`) are **method** findings that merely *name* equipment while describing a census or a check. That is **exactly the name-driven assignment this package criticised at `P04-F-114`**, committed inside the instrument built to apply `P04-F-116`, and caught only by reading the twelve defining blocks individually. Coverage and method are published with the result: assignment from each finding's defining block, by business-language vocabulary, all twelve equipment hits read by hand.|**This is the shape the whole exchange converged on and it is worth stating once at the end.** P07's `F-83` found its two headline findings resting on a stack every member of which is inside its declared scope — *the only round that made anything safer* — and this is its counterpart here: the asset core is complete, the equipment periphery is not. **Neither of us could have partitioned our own findings without the other's instrument**, and the useful output is not a verdict on the package but a **map of which claims stand on what**|
| **P04-REV-52** | **Two registers were living under one family name, and a third collided with them numerically — none of it visible to any check in the sweep.** P07 ran *count the forms, not the identifiers* over its own families and found that two of its dual-form entries **were two different families colliding on one stem** — a module dependency and the tax invoice — with every check reporting clean because both had definition rows. **The collision is semantic, not structural.** Run here: **`P04-LAW-A`–`H` are statutory sources** (file `13`) while **`P04-LAW-01`–`06` are legal conclusions** (file `07`, e.g. *"a VAT-registered person selling a fixed asset is making a sale of goods"*), distinguished only by whether the suffix is a letter or a digit — **and the digits then collide with P3's inherited `LAW-01/02`, which are sources again.** Second collision: **P3's `CTR-01`–`06` and this session's `P04-CTR-01`–`07` occupy the same numbers with entirely different content.** `P04-F-117`. **Rename what is yours; attribute what is inherited** — and the choice is not stylistic. The conclusions are renamed **`P04-LC-01`–`06`**, 9 occurrences in one file, with the source family counted **before and after as the control: 22 and 22**. Renaming was available because both families are this package's own. For `CTR` and `LAW-01/02` a rename would **destroy the only link back to the package that raised them**, so the inherited identifiers are untouched and **attributed** instead — written `P3 CTR-nn` outside their register, with a note on the register section.|**Every unit of the five-check sweep is satisfied by a stem collision, by construction**: both families are defined, every citation resolves, no table is malformed, no hash is stale, nothing leaks into Layer 1. **Counting forms per family is the only view in which it appears at all** — and no amount of re-reading substitutes, because the text is correct on every line. That makes this the sharpest instance of the exchange's method claim: **a defect can be invisible to every control a package owns and still be plainly wrong to a reader.** The credit is P07's; the rule that surfaced it was this package's, and neither of us could have applied it to ourselves without the other running it first|
| **P04-REV-51** | **Copy-identity is not stack-completeness, and `P04-F-102` had answered only the first.** P07 found a module **outside its declared path set** overriding the very method one of its findings turns on — calling `super()` first, then post-processing a list the guard had already filtered — and named the rule: *a claim discharged against the right module is not discharged against the deployed stack.* `P04-F-102` closed **which copy of `equipment_sequence` is deployed**; it never asked what else is installed on the models that module operates on. **The positive result is the one this package could not previously state.** On **`account.asset`** — the model every capitalization, depreciation, revaluation and derecognition finding here turns on — **no installed module lies outside the declared source scope**: six declare on it, all in a declared root. Whatever `P04-F-93` established about the estate's 27 undeclared modules, **none of them declares on the asset model**. By contrast **`maintenance.equipment` has `equipment_fleet`**, outside both roots, with **no source anywhere under `/Volumes` or `$HOME`** — so the asset–equipment findings in `05` rest on a stack with an unreadable member and the pure asset findings do not. **That distinction did not exist in this package until the question was asked in P07's form.** `P04-F-116`; `P04-F-102` qualified, not withdrawn.|**And the one-directional limit still binds, which is why this closes nothing.** `ir_model_data` sees only declarations carrying an XML id; a module can override `create`, `write` or `_post` on `account.asset` with no field and no view and appear nowhere in the table. So *"none outside the declared roots"* is **a floor on the declared stack, not proof of a complete one** — the sharpest available statement is that **no undeclared module is shown to act on `account.asset`, and none is shown not to**. P07's control fired harder on its side than mine did on mine: the naive read reported **zero** modules touching `account.move` there against my **one** here — same instrument, same wrongness, and both published because a clean plausible negative is the kind that survives|
| **P04-REV-50** | **The prefix rule created the defect it was written to prevent, and the single instance sits inside the paragraph that introduced it.** P07 reported it first: its `REV-E-64` fix — require `P07-` so a peer's ids are not read as its own — made **eleven bare citations of its own findings invisible to its own checker**, while a reader mid-exchange could read them as this package's. Swept here across every family existing in both bare and prefixed form: **79 bare citations — 75 in families with no prefixed form** (`BD`, `CTR`, `LAW`, correctly audited bare), **3 deliberate quotations** of the defective form inside the finding describing it, and **1 genuine silent omission**: `` `F-81` `` in the sentence explaining that P07's checker had reported `P07-F-81` when the match was a citation of *this package's* `F-81`. **The rule and its violation are in the same sentence.** `P04-F-115`. **The two defects have one root and each fix creates the other** — P07's formulation, adopted verbatim: *an identifier without its package prefix is ambiguous, and requiring the prefix converts a false positive into a silent omission; neither is safe, only writing identifiers out in full is.* The operative rule for this package is narrower and worth stating separately: **a family is safe when it has exactly one canonical form and the check audits that form.** `BD`, `CTR` and `LAW` have no prefixed form and are audited bare, correctly. The failure mode is a family existing in **two** forms — true only of `P04-F`/`F`, `P04-B`/`B`, `P04-REV`/`REV`. **Count the forms, not the identifiers.**|**P07 also found the frequency floor in its own census** — `if c < 2: continue` — so its 46 was author-chosen exactly as this package's 14 was: **the correction of an under-scoped check computed over an under-scoped population**, on both sides, in the same clause. Re-run with no floor it reports **48 families, 34 owned, 1,861 citations, 0 unclassified**; the floor had hidden two benign singletons, *"and the method was wrong either way"*. And it adopted `P04-REV-48`'s lesson without paying for it — writing the classification into the file **before** re-running the sweep, where this package had one run of register-versus-checker disagreement|
| **P04-REV-49** | **"27 modules wide" was the size of the gap, not the size of the exposure.** P07 closed its widest open item by filtering **generation first, then the specific claim**, turning a 20-tree exposure into 2 candidate bodies per cited file with all four claims discharged — and generalised it: **the size of a diff is not the size of the exposure.** `P04-B-46` was the same kind of number. Measured from the deployment rather than from module names — `ir_model_data` resolved through `ir_model_fields.model` and `ir_ui_view.model` — **9 of the 27 declare anything on a model this package's findings turn on**, chiefly `scgl_account_coa_control` on `account.account`, where the capitalization designation lives. `P04-F-114`. **The first instrument was wrong and a control caught it.** Reading `ir_model_data.model` directly gives the model of the *referenced record*, not the business model, and reported that **one** module in the whole database touches `account.move`. Resolved: **28**, with `account_asset` mapping to exactly the five models it should. Both controls published, because the first number was plausible and wrong — and plausible-and-wrong is the only kind that survives to publication.|**Two of the five modules this package named by name declare nothing on any business model** — `scgl_date_range_auto_period`, flagged against the silent re-dating finding, and `journal_entries_report`. Those flags were **name-driven speculation**, published as *pointers, not an assessment*: the label was right and **two of five were still wrong**, which is now the measured worth of a module name. **And the narrowing is one-directional**: `ir_model_data` covers records with an XML id, so a module can override `write`, `create` or `_post` in Python declaring nothing — **9 is a floor on what demonstrably touches, not a ceiling on what could affect**. The other 18 are *undemonstrated, not cleared*; `P04-B-46` stays UNRESOLVED. What changed is that it names **which** and **why** instead of a count|
| **P04-REV-48** | **The family list audited at `P04-REV-47` was itself an author-chosen population.** It declared *"14 owned families"* as though the denominator were given; the families had been filtered at a **frequency floor this package never declared** and then picked by eye. Enumerated with no floor there are **43**. P07 ran the same question and found **46, of which 26 owned against its own 8** — a larger gap than this package's, and **neither of us found our own without the other stating a number**. Classified: **18 owned and audited** (310 citations), 13 **foreign by attribution**, 12 **not identifiers** (`TAS-02`, `IFRS-16`, `SHA-256`, `Layer-1`, `ERPPLUS-17` …). **Four families had never been checked at all**, the largest being the **event register `EV-01`–`EV-24`, the spine of `03`**, with `UC`, `Q` and `HOLD`. Result: **1 undefined**, the intentional withdrawal notice. `P04-F-113`. **The denominator defect appearing inside the audit of the check** is the sharpest instance this package has produced, because `P04-REV-47` was itself a correction of an under-scoped check — and it under-scoped its own scope. POPULATION, PATTERN and UNIT were declared for the *identifiers*; the **population of families** was selected. That is the fourth level at which this same defect has landed today: signature set, path set, source scope, and now the check's own subject list.|**One reclassification, and it is P07's `REV-E-64` rule inverted.** `HOLD-02`, `HOLD-03`, `HOLD-05` are **prior-package identifiers**; `07` attributed one and `06` attributed none, so two citations were indistinguishable from unresolved local ids. P07's rule was *require the prefix so a peer's id is not read as yours*; the converse holds equally — **a foreign identifier without its attribution is an orphan to every reader and every checker.** Attribution added, matching the treatment already given `P2 REV-03` and `P07's F-65`. And P07's localisation is the finding neither of us could reach alone: **its 12 orphans were a scope failure, mine were a convention failure**, so extending scope was sufficient there and would not have been here — *neither of us could have known which without running both*|
| **P04-REV-47** | **The identifier check covered 2 of 14 owned families, and the family carrying this package's HOLD had never been enumerated.** P07 extended its own and found **12 orphans of 27** in the family carrying *its* HOLD. Extended here across `P04-F`, `P04-B`, `P04-REV`, `P04-CTR`, `P04-BD`, `P04-PD`, `P04-LAW`, `P04-SC`, `BLK`, `D-P04`, `BD`, `CTR`, `CTR-C`, `LAW`: **19 apparent orphans, none genuine.** Eight `P04-LAW` were backticked table rows, four `D-P04` were bold sentences, four `BLK` were prose, two `SCP` were **P11's identifiers**, and one was a regex artefact (`CTR` matching `CTR-C-01`). **The package uses at least four definition conventions and the check knew one.** `P04-F-111`. **Nineteen false positives are worse than a check that finds nothing**, because they train a reader to dismiss the output — a genuine orphan appearing later would be lost in noise the check itself manufactured. Three fixes, each from a defect this exchange produced: **peer families excluded by name** (P07 found its extended check reporting `P07-F-81` when the match was a citation of *this* package's `F-81` — in a two-package exchange, identifier collision is the **normal case**); **own identifiers no longer elided** — nine elisions such as *"`P04-B-16`, `B-18`, `B-19`, `B-28`"* written out across five files, while bare forms that remain are **foreign by attribution** (`P2 REV-03`, `P07's F-65`); and **`BLK-03`–`06` emboldened** so reader and checker find them by the same route. P07's self-referential trap arrived too: writing the finding cited `P04-F-111` before defining it.|**And the classification produced a joint conclusion neither package could reach alone** (`P04-F-112`, routed to `09` §5A). `P04-B-47` and P07's `U-20`/`U-29` are the only items in either package that **no reading, census or query can close** — a database records the **result** of a load or write sequence, never the sequence. They need **one controlled installation executed twice in opposite orders, recorded**. Separately each reads as a minor residue beside dozens of open rows, one in a tax register and one in an asset register. **Together they are the entire content of what a runtime request would be for**, and the shape is invisible from inside either package — which is the argument for stating it jointly rather than each of us carrying our own|
| **P04-REV-46** | **The second module leaves the code-identity axis open, and characterising the divergence discharged the claim anyway.** `product_stock_equipment`: **11 copies, 3 distinct source trees, two of them v18-line**, every copy declaring `'1.0'` so **version cannot discriminate**. Unlike `equipment_sequence` the axis does not close. Measured instead — 7 of 7 files AST-parsed, 0 failures: **0 class-level field differences**, **1 of 5 XML files differing** (a presentational `span`-versus-`div` wrapper, no field, attribute, domain or readonly change) and **3 python lines**, a **multi-record-safety** difference on a write of a descriptive note to equipment matched by name. **The function this package actually cites — the forcing to non-storable with serial tracking — is byte-identical in both trees and is not in the diff**, so the `05` §3 claim is discharged. `P04-F-107`. **P07's split needed refining, not just applying.** Its form was *views identical ⇒ structural claims safe*. Here views are **not** identical and the structural claim is safe anyway, because a presentational wrapper cannot carry one. The usable rule is **compare the difference against the specific claim**: a `span`/`div` change cannot carry a structural claim and a note write cannot carry an accounting one. And the comparison produced a finding it was not looking for — **the equipment/stock forcing is an `@api.onchange`, so it binds only in the form** and any import flags a product as equipment while leaving it storable and untracked (`P04-F-108`). That is **independent corroboration of this package's UI-enforced-only pattern from an unrelated module**, and it holds whichever copy is deployed.|**Two instrument results from P02, both tested here rather than noted.** *All five sweep units are now demonstrated capable of reporting a defect by injection* — undefined-id citation, extra table cell, hash-invalidating edit, four vendor tokens in the Layer-1 pack, empty deliverable — baseline `0,0,0,0,0` against injected `1,1,4,4,1` (`P04-F-109`). P02 found its scrubber had only ever returned zero; mine had fired, but **by accident, which is not a control**. And *shell portability*: every evidence root here contains spaces, **`zsh` does not word-split and `bash` does** — an unquoted `grep -rl` under bash returns **0 matches on a file that exists**. All evidence was executed in `zsh`, so **the negatives stand as executed**, but a reader re-deriving under `bash` without quoting gets the `P04-F-103` shape in their own hands. Recorded in `13` as a re-derivation warning, not a defect (`P04-F-110`)|
| **P04-REV-45** | **A fifth scope axis, and it is the only one that more work cannot close.** The four this session found — signature set, path set, source scope, code identity — are all about **where the author looked**, and each is closable by looking better. P07 traced both its headline findings to **template/module load order**, and a database records the **result** of that order, never the order. This package has one item of the same class and had registered it without naming the class: `P04-B-47` — whether the missing asset entries were never created or created and removed, the question `P04-B-40` turns on. **No archive, no wider census and no better query settles it; only executing something and recording it does.** Re-tagged **EVIDENCE NEVER RECORDED**. `P04-F-105`. **This changes what a HOLD means and it belongs in the Boss pack.** Every other open row in `10` is open because something has **not yet been read**. `P04-B-47`, and the two modules under `P04-B-46` whose source exists **nowhere on this host**, are open because the evidence **does not exist to be read**. The first kind is closed by more research; the second only by a **runtime request** — and stating which rows are which is more useful to a decision-maker than the count of open rows.|**And a control, once added, is never removed — with proof rather than argument.** `P04-F-103` (42 hashes of empty input reading as *"42 identical copies"*) was caught **only** because a file count had been added to the output after `P04-F-98`, a different defect in a different test: **the control for defect n−1 caught defect n.** P07 drew the rule and I had not. The sweep gains a **fifth unit** — no published hash may equal the empty-input SHA-256, and no deliverable may be empty — which closes a real gap: check 3 compares the manifest against the files, so a file that became **empty** would be re-hashed on regeneration, the manifest would agree, and the check would report **0 stale** while the deliverable was gone. **Agreement between two records is not evidence that either is right.** `P04-F-106`|
| **P04-REV-44** | **This package's zeros had never been laid against a discriminating set, and doing it narrows one.** P02 set its zero-COGS result against four deployments spanning every discriminating configuration and could then say the zero is *a property of the mechanism, not of data volume*. Run here: **`asset_move_line_rel` holds 6 rows covering 6 of 7 real assets in `4b766580` — 86 %** — against **0 of 388** in `551ab874` and **22 of 669** in `45a8e08e`. **The source-link mechanism works.** So `P04-F-92`'s zero is a property of that deployment, not of the design, and any reading of it as *"the link is not implemented"* is withdrawn. **What replaces it is sharper than what it withdraws**: a measured spread of **0 % / 3.3 % / 86 %** across three deployments of one product. Three of the four values driving every depreciation entry are **UI-enforced only**, so an import or script bypasses them, and a population created by import would carry no source line where one created from posted vendor bills would. The spread is consistent with that and with nothing else this package has found — recorded as **SUPPORTED INTERPRETATION**, because a single snapshot cannot show how a record was created and this package will not infer a creation path from a correlation. `P04-B-03` stays answered **per identity**, not generalised. `P04-F-104`.|**The same table makes the other zeros falsifiable**: the netting fires **14 of 14** where analytic accounts exist, so `P04-F-99`'s zero is configuration rather than absent capability; and `96548e18` — a v18 install with the asset module not installed at all — shows what a genuinely empty estate looks like. **A deployment with 388 assets, no source links and no analytic accounts is not an empty system; it is a populated one with two mechanisms switched off.** *The discriminating set was not assembled by design*: two of the three v18 identities came from P02 correcting this package's population, after this package had corrected P02's. Neither of us chose it — it is the residue of two reciprocal corrections, which is an argument for the exchange rather than for either method|
| **P04-REV-43** | **P07's split of the code-identity axis, run here — and for one module the axis is CLOSED rather than narrowed.** P07 found its two copies differ **only in Python method bodies**: identical field sets, identical views, so *nothing that differs is persisted* and the axis threatens **behavioural** claims only, discharging structural ones. Tested on the two `EV-CUST` modules that are actually installed. `equipment_sequence` deploys at **`18.0.1.6`**; exactly **two** copies on the declared path set carry that version, and they are **byte-identical in source** — 13 of 13 python files parsed by AST over class bodies only, **0** field differences, **0 of 10** XML files differing, **0** changed lines CR-normalised, one distinct whole-tree hash from two copies. Which copy is deployed cannot change any finding from that module, structural or behavioural. `P04-F-102`. `product_stock_equipment` is **not reported** — 11 eligible copies enumerated, comparison still executing, and a partial answer is not published. **The first run of that test returned 44 copies in 3 groups and was meaningless.** Forty-two hashed to the SHA-256 of **empty input**, because paths containing spaces were **word-split by the shell** and the walk visited directories that do not exist. Confident, reproducible, and it would have read as *"42 identical copies"* — the **strongest possible agreement**. This is the defect **P07 reported one message earlier**, occurring here inside the test written to apply P07's lesson, and it is `P04-F-98`'s null-that-behaves-like-a-value again: 42 empty walks did not scatter as noise, they **collapsed into one group**. Caught only because the previous defect had put a file count in the output. Every run now prints the empty-input hash and flags any group equal to it. `P04-F-103`.|**P07's split is adopted as the general rule and is worth more than either module result**: where copies agree on fields and views but differ in method bodies, findings citing **models, fields or views are discharged** and findings citing **logic stay exposed**, because what differs is not persisted. That converts *"code identity is undecidable"* — which is unusable — into a **per-claim** test. The fourth axis is not one exposure but two, and only the behavioural half was ever at risk|
| **P04-REV-42** | **The latency finding published one commit earlier was a claim about a population of one, and a second deployment refutes its generality — while confirming the finding it qualified.** P02 reported databases outside every census either of us had run. One is **`4b766580` (`pankhamhom`), `base 18.0.1.3`, 478 modules, 956 move lines** — and unlike `551ab874` it **has 9 analytic accounts**. Measured there: **30 of 956 lines carry a distribution, all 30 belong to asset moves, spanning 14 distinct moves, and all 14 net to exactly 0.00 — no exceptions.** So `P04-F-49` moves from source-derived to **measured** (`P04-F-100`), and `P04-F-99` narrows to the identity it was taken in. **The Layer-1 pack has now been corrected twice in one day on the same paragraph** — first to add a latency that was real, then to remove its generality. Both corrections were right about the identity measured and wrong about the scope claimed. *A latency finding is a claim about a population, and mine had a population of one.* Rewritten to carry **both** observations: where cost centres exist the charge reaches the centre and leaves it in the same entry; where they do not, nothing reaches it at all. Both defeat attribution, and a downstream reader now gets the distinction rather than a single verdict.|**And a third undeclared bound, in the sweep written to reconcile the first two.** `96548e18` (`T805efaplus`, v18, 123 modules, no `account_asset` table, 0 move lines — a never-transacted v18 install) was missed **twice over**: it is a `.zip`, so the `PGDMP` signature scan could not see it, and it is dated **2025**, so the reconciliation sweep's `*_2026-*` name pattern could not either. **Three v18 identities are now known where this package had one**, so every single-identity bound in `01` §6A is a **floor**. P02 has stopped publishing a count and holds the invariant instead; the same discipline is adopted here — the census is **OPEN**, and `P04-B-01`/`P04-B-03`/`BLK-01` all now have a third measured population, including a **third day-convention pattern** (7 of 7 real assets on `constant_periods`) that no single migration answer serves|
| **P04-REV-41** | **The second clause of the analytic finding had never been measured, and measured it cannot fire.** P07 withdrew the posting half of its strongest finding on exactly this ground — the *resolves into a withholding group* half measured everywhere, the *and therefore settles against the control accounts* half nowhere, and latent because a zero-amount tax generates no line to post through. Same shape here: `P04-F-49` says depreciation's analytic route **nets to zero**, so *attribution exists at line level and the balance is zero*. The first half is source-derived and stands. The second was never tested. Measured in `551ab874`: the `analytic` module is **installed**, **1** plan exists, **0 `account_analytic_account` rows**, **0 `account_analytic_line` rows**, and **0 of 40,353** move lines carry a distribution — including 0 of 4,236 asset-move lines. Positive controls on the same extraction fire (`name` 38,228, `account_id` 40,282, `balance` 40,353), so the zero is absence, not a failed read. `P04-F-99`. **What changes is the live form, and it is worse than the finding it qualifies.** *"Attribution exists at line level but nets to zero"* describes code that has never run there. With no analytic accounts, **no attribution exists at line level either** — the netting defect sits **downstream of a more basic absence**. `BD-02` is breached today by **total absence of attribution**, not by cancellation. The companion claim that mandatory plans never fire on programmatic posts is likewise latent: nothing can be mandatory over an empty set. **This corroborates P09 directly** — its headline is that the analytic dimension is *schema, not data*; this is that statement measured, in a v18 deployment with 40,353 posted lines.|**Propagation was again wider than the finding, and again reached Layer 1.** The claim appears in ten files; the load-bearing sites in `06`, `09`, `11`, `16`, `20` and — as with P07 — in **`19`, the Layer-1 pack cleared for downstream use**, where it was stated as an observed event a reader could rely on. All qualified in place, source findings left standing, `19` rewritten in business language so a downstream reader does not cite the cancellation as something that has happened. **P07's rule, adopted: a number and the story told about it are two claims, and only one of them tends to get checked.** Mine is the same defect one level in — a finding and *the clause of it that was never measured* are two claims, and only the measured one was ever defended|
| **P04-REV-40** | **Ran P07's module-identity test, and one of the three custom modules this package's evidence register names is not installed in the only same-generation deployment.** P07 had analysed a module installed in **0 of 4** identities while a different technical name, carrying the **same display name and version**, held the **same code** and was installed. Here: `equipment_sequence` and `product_stock_equipment` are installed with matching versions; **`scgl_advance_expense_request` is not installed** in `551ab874`. `P04-F-97`. **A matching version proves nothing** — P07 established one version string over two code bodies, and one display name and version over two technical identities. **Neither name, nor version, nor display name identifies deployed code; only the installed-module list does, and it identifies only the name.** The deployment's addons directory is not on this host, so code identity is **not decidable** here at all. **The twin defect itself does not reproduce — 0 display-name twins across 361 installed and all 65 declared custom modules** (`P04-F-98`), published as a negative. **But the first run of that test reported 11 and was wrong**: ten were one bogus group created by the test's own manifest parser failing on 10 of 65 manifests and recording each as name `?`, which then collided with one another. Re-run at **65/65** parsed, the answer is **0**. *A test with an unreported parse hole does not return a weaker result, it returns a confident wrong one* — and here the failures grouped themselves into **exactly the shape the test was looking for**, which is the most dangerous form available. Coverage is now stated with the result; the previous run's was 55/65 and unstated.|**P07's corollary is the one to keep, and it is sharper than my own formulation.** I wrote that *a scope is a claim, and a claim written as prose has no denominator*. P07's instance was **not prose** — three paths with manifest counts, exactly what this programme asks for — and it was still never tested against what is **installed**. **Naming the root is not testing the root.** A declared path set is a statement about where you looked; only the deployment says what runs. Three bounds now, each failing one level further out — signature set, path set, source scope — and this adds the fourth axis: the declared source can be complete, current, correctly pathed, and still not be the deployed code|
| **P04-REV-39** | **The behavioural findings were tested against a same-generation deployment for the first time, and the discipline that mattered was running the control on the result that CONFIRMED me.** `551ab874` holds **1,720 depreciation entries in `draft`** — a number that reads instantly as this package's unposted-entry concern. **Every one is future-dated** (2026-08-31 to 2038-11-30, against a 2026-08-30 snapshot); the **398** already due are **posted**. Draft-and-future is the designed state of a depreciation board, and *"1,720 entries sitting unposted"* would have been a serious false positive. `P04-F-95`, published as a **negative**. Then the headline TAS 16 test: **all 30 disposed assets have no derecognition entry, and no entry at all, in any state** — which taken alone is confirmation. **The control refutes that reading**: **238 of 303 `open`** and **17 of 17 `paused`** assets also have none, so the absence is **general, not disposal-specific**, and this deployment **cannot separate** *"no disposal path posts the entry"* from *"the subledger largely never reached the ledger"*. The source finding stands as source-derived; what is withdrawn is the temptation to cite this database as its proof. | **What the measurement does establish is larger than what it failed to confirm**: **285 of 350** assets in entry-generating states carry no journal entry, and with `P04-F-92` (**0 of 388** carry a source-line link) the asset subledger in the only v18 deployment available is **disconnected from the ledger in both directions**. Never-created versus created-and-deleted is **not decidable from one snapshot** — precisely what `P04-B-40` turns on — so it is registered as `P04-B-47`, not resolved. `P04-F-96`. **A test run only when it confirms is not a test.** The near-miss is the instructive half: the confirming number arrived first, was large, and pointed the expected way, and only a query asking the *discriminating* question — compare against assets that were **not** disposed — separated them. Same instrument P07 used to turn a fresh-install row from a refutation into a positive control, and the same one used here at `P04-F-87`. **The control belongs on the results you like, not only the ones you doubt.** |
| **P04-REV-38** | **The source scope was declared by *description* and is not the deployed scope — 27 modules wide.** P07 found that a source root it had excluded as *"Different products. Out of scope."* was the **deployed code**, sharing 24–35 modules with every in-generation database and holding the files behind five of its findings. It tested the reason and the reason was false. Tested here — a test that was **impossible until `P04-F-90` produced a same-generation deployment**. Against `551ab874` (v18, 361 installed): **306 in the declared reference tree, 28 in the declared 65-directory custom set, and 27 in NEITHER**. In the other direction, **37 of the 65 declared custom directories are not installed there at all**. `13` §1 named the source scope as *"Reference ERP v18 Enterprise source tree, build `20250608`"* and *"Project custom addon set, v18 line"* — **no path**. Both are now written as paths. **And the build string does not identify the tree**: two directories here carry build `20250608` with **793** and **1753** manifests — P07's `F-65` from the other side, where two copies of one module shared a version string and differed by 279 changed lines in one file. `P04-F-93`, `P04-F-94`, blocker `P04-B-46`.|**Third undeclared bound in one session, each one level further out**: the archive **path set** (`P04-REV-37`), the archive **signature set** (`P04-REV-35`), and now the **source scope**. The pattern is not carelessness about paths — it is that **a scope stated as a description reads like a declaration and cannot be audited as one**. One of the 27, `scgl_date_range_auto_period`, sits **one directory above** the declared custom root — the same shape as the database that sat one directory outside the declared path set. **Blast radius stated and deliberately not widened**: no finding is withdrawn and none is confirmed, because **none of the 27 has been read**. What is published is which findings sit in the path of an unread deployed module *by name* — `scgl_account_coa_control` against the capitalization designation (which lives on the chart-of-accounts account), `scgl_date_range_auto_period` against the silent re-dating finding, `equipment_fleet` against the machine-identity gap. **`equipment_fleet` and `journal_entries_report` do not exist anywhere under `/Volumes` or `$HOME`**, so part of the deployed behaviour is **unreadable from this host** and is a runtime request, not research |
| **P04-REV-37** | **The database two blockers were held open on was on this host the whole time, one directory outside a path set this package chose and never declared.** P07 reported an eleventh artefact outside my census. Re-running the census over a **declared** path set — `/Volumes` + `$HOME`, size bound stated and justified, three signatures content-tested — the eleventh copy is the least of it: **`~/OCC_BACKUP/idemo18_uat_pre_scgl_occ_website_20260830_085432.dump`**. Internal `dbname: idemo18_uat`, uuid `551ab874`, **`base` `18.0.1.3`**, `account_asset 18.0.1.0` installed, dated **2026-08-30** — later than every archive previously enumerated, and **v18: the generation of the source tree every behavioural finding here rests on.** **`P04-F-88` withdrawn one commit after it was published.** It said the `idemo18_uat` exclusion *holds*, and as literally worded — *"no archive under `~/Downloads` or the SMEsPlus tree"* — **it is still true and completely worthless**. False in use, true as written: a reader auditing it would have **confirmed** it. **`P04-F-85`'s scope claim falsified** — *"no database on this host is the same generation as the source tree"*; its method point (labels declared from one signal) stands. **`17` §5 deviation 1 corrected in the opposite direction**: the Runtime → Database leg is **materially stronger**, having been first understated as absent and then overstated as generation-mismatched. **`BLK-01` ANSWERED in the database it names** (`P04-F-91`): **375 of 388 real assets on `daily_computation`, 16 of 16 templates on `constant_periods`** — the split measured inside **one v18 database** rather than inferred across generations. **NOT CLOSED**: the close condition names *"the 280 records"* and the archive holds **404**; the discrepancy is published, not smoothed. **`P04-B-03` ANSWERED** (`P04-F-92`): `asset_move_line_rel` exists and is **empty** — **0 of 388**, against 22 of 669 in v16 — with a positive control (404 rows from `account_asset`, same archive, same method) proving absence rather than extraction failure.|**This is the defect the package names most and has now committed in its own governing register: PATH SET, author-chosen and undeclared.** POPULATION, PATTERN and UNIT were all declared and executed; the **path set** was two directories I picked and never wrote down. Worse: `P04-F-88` was written **as an application of P07's exclusion-authority rule**, and it verified the wrong thing — I raised the *authority* of the exclusion from filename to internal `dbname`, and never questioned the **population the exclusion ranged over**. **Raising the authority of a statement about a population does nothing for a population that was drawn wrongly.** P07 named the ladder — *having the rule, recalling the rule, running the rule, and only the third is a control*. This adds a fourth rung and it is the one that failed here: **running the rule on the wrong set.** The four-check pre-commit sweep would not have caught this either; no check whose unit is the package can find evidence that is not in it |
| **P04-REV-36** | **The commit that reported three clean checks published a broken integrity record, and the correction it carried left five survivors.** Three defects, found by running P07's `REV-E-44` and by giving the sweep a fourth unit. **(a) Two integrity records disagreed.** `SHA256SUMS.txt` and the manifest's own per-file hash table agreed at `abf265c`, `b27040e` and `c57d846`, and disagreed on **6 of 20 files at `985840e`** — the sums file was regenerated, the manifest table was not. The three checks that ran (identifiers, structure, Layer-1) all passed because **none has the unit *"the integrity record agrees with the files"***. The document asserting the package is intact was the document that was wrong. `P04-F-89`. **(b) An exclusion asserted from filenames.** `BLK-01` and `P04-B-03` stay open because `idemo18_uat` *"was not among the accessible dumps"* — read off **file names**. Verified properly (`pg_restore -l` → `dbname:`; `manifest.json` → `db_name`) across all seven archives: it **holds**. Recorded although it survived, because P07 found the same class in its own population and there the exclusion was **false** — a database excluded as *"different product line"* that was the declared generation. **An exclusion furnished with a stated reason stops the audit that would have checked it**, whether or not the reason is true. `P04-F-88`. **(c) Five survivors of `P04-REV-35`, published an hour earlier** — the §6A.1 reproducibility table still read *3 readable + 2 unreadable* and *72 of 96 templates*; the opening line of the same section still said *four dumps*; the PMO deviation still said *four readable dumps*; and `P04-REV-27` still asserted **"no sixth database"**, a settled negative that `P04-REV-35` disproved. | **The unit is the recurring object and this is its seventh appearance.** A check is only as good as its unit, and a *sweep* is only as good as the **set of units it spans** — which is why the fix is a fourth check rather than a stricter third. Adopted from P07 in the same form and by the same route it adopted the timing rule from here: **identifiers, per-table structure, manifest-hash agreement, Layer-1 scrub**, four disjoint units, last step before every commit. Also worth stating plainly: **(c) is the fifth time a correction of mine has left survivors in the file it corrected**, and the survivor at `P04-REV-27` is the worst kind — a *negative about the completeness of the evidence base*, published as settled, now known false. Left in place with its disproof attached rather than rewritten, so the record shows a re-run being mistaken for a proof |
| **P04-REV-35** | **The evidence base was under-enumerated twice over, and both fixes this package had already applied were the thing that failed.** The census read *"8 files · 5 snapshots · 4 database identities"*. It is **10 · 7 · 5**. Two defects, each in a control this package had adopted as a remedy: **(a) Format.** `P04-REV-27` replaced an extension-bounded search with one *"by magic bytes, any extension, any depth"* — but it matched **one signature**, `PGDMP`. Two snapshots are **`.zip` containers holding `dump.sql` + `manifest.json`**, which do not begin `PGDMP`. *An enumeration by magic bytes is only as complete as the set of signatures it enumerates.* **(b) Identity.** The identity unit was the **file name**. Keyed on `database.uuid` from `ir_config_parameter`, the name is wrong **in both directions at once**: the two artefacts named `iEVING` are **two different databases** (`f4a44cce`, `1f6338ae`), and the two named `BK12MAY26` are **one** (`66d1b52a`). Reported by P07, then re-derived here from the archives before adoption: uuid read from every one of the seven snapshots; the two zips' `manifest.json` state `version_info [19,0,0,'final',0,'e']` directly — a **better generation signal than the `ir_module_module` count** used at `P04-REV-33`. Asset counts re-run on all seven. **`P04-F-83` and `P04-F-84` both strengthen** — the new identity `f4a44cce` also holds **zero real assets** and **12 of 12 templates on the product default**, widening the claim from three identities over seven weeks to **four identities over four months**. **But the headline total was right by accident** (`P04-F-86`): published `36+36+12+12` over *"three identities"*, the true composition is `36+12+36+12` over **four** — a **double-count of `a1430edc` and an omission of `f4a44cce`, 12 each, in opposite directions**. *A total that survives a correction to its own unit has not been confirmed by surviving; it has only failed to move.* Re-deriving the table also exposed a **sixth survivor of `P04-REV-33`** — §6A.2 labelled its rows `v18` while its own total row said `v19`. And a new finding fell out of the re-run: **`P04-F-87`** — the one identity with real assets has **15 of its 16 templates on `daily_computation`**, so the claim is not *"nobody changes this setting"* but **"every install that used assets changed it, and no install in the target generation has"**. **High.** Two adopted remedies each failed at the same point — **the set they enumerate over** — and the failure mode is **exclusion**, which no control in this package can see: an over-inclusive count leaves the wrong row on the page, an under-inclusive one leaves nothing. Neither the orphan check, nor the structural check, nor the independent review looks for **absent members**. What found it was a peer publishing a table naming a database this package had never opened | **High.** Two adopted remedies failed at the same point — **the set they enumerate over** — and the failure mode is **exclusion**, which no control here can see. Neither the orphan check, the structural check, nor the independent review looks for **absent members**. Found only because a peer published a table naming a database this package had never opened |
| **P04-REV-34** | **Five malformed table rows, all introduced by this session's own edits, none findable by the identifier checks.** Two rows in the blocker register carried an extra column; two in the **governance file** were a column **short**; one had an unescaped pipe inside a code span splitting its cell | Found after P07 reported that re-running its orphan check **immediately after a correction** caught a defect **ninety seconds old, created by the correcting edit itself** — and that a check run once before publication cannot find that kind. Adopted: **the identifier and structure checks are the last step before every commit, not a gate.** The structural check also had to be corrected mid-run: it took the modal column count **per file**, when a table's width is a **per-table** property — the wrong unit produced two false positives and **missed three real defects**, including both in the governance file. Fixed unit: 166 tables checked, 0 malformed |
| **P04-REV-33** | **The database generations were declared from one structural signal and never checked against the version record — and the labels were wrong.** The package called three databases *"v18-line"* and one *"an older generation"* | Checked against `ir_module_module` after P07 found the identical defect in its own scope block. **The three are v19; the fourth is v16.** So the first label is **wrong** and the second understates a **two-generation** gap — and, worse, **no database on this host matches the v18 source tree these behavioural findings rest on** (`P04-F-85`). Every count stands; what was wrong is which source-code findings each population can be set against. **Wrong when written, not invalidated later** — this package's own category, in this package's own scope block, exactly where it found P07's. The Runtime → Database leg is now declared weaker than before at `17` deviation 1 |
| **P04-REV-32** | Splitting the compound finding (`P04-REV-30`) was recorded as a **statement** fix. It was also a **research** fix, and this package did not notice until P07 reported the same thing | P07 split its own compound finding and the configuration half became *"three independent deployments, three independent operators, the same manual repair"* — **unavailable while the halves shared a sentence**. Tested here and the same held: the configuration half of `P04-F-81` is not *"templates are on the product default"* but **96 of 96 across three independent identities, different operators, seven weeks — not one carrying the convention production runs on**. Published as **`P04-F-84`**. *A compound claim does not merely under-describe its evidence; it can conceal the finding.* Also: the new identifier was written in a form this package's own checker could not match — **third occurrence of that formatting defect**, caught by the orphan check |
| **P04-REV-31** | **A fourth sweep, on P07's broader pattern, found three more survivors — one of them wrong when written.** The scoping paragraph that governs the whole database section read *"two of the three are a different product generation"*: **wrong at the time** (one of the three then read was the older generation, not two) and **stale after** (five snapshots, four identities). The two evidence-root registers still said *"five PostgreSQL dumps"*, conflating snapshots with files and identities | Found by adopting P07's pattern — any numeral or number-word within forty characters of `database\|deployment\|snapshot\|identit`, with a control on the sweep — after P07 reported its own third round had turned up **five** survivors including a **section heading** and a sentence the correction had rendered **factually wrong**. This package's previous sweep had been narrower and missed all three. All corrected; the wrong-when-written error stated as such rather than silently replaced |
| **P04-REV-30** | `P04-F-81` is a **compound claim** — a population half (683/685 real assets on daily) and a configuration half (96/96 templates on `constant_periods`) — and the finding **never said which evidence supported which half**. Its single class line blurred them | Adopted from P07, which found it had used a **configuration** database for **population** claims and had *never distinguished the two kinds of claim in one file*. Checked here: each half does rest on the right kind — the population half had only one candidate, the configuration half was enumerated exhaustively — so the selection was correct **by construction, not by design**, and is now stated as a split with each half separately bounded. Also recorded: **"rank the population" needs its own declared unit**, because P07 and P11 ranked the same two databases and the order **inverted** — largest by rows versus most populated tables, the deepest data set versus the broadest install |
| **P04-REV-29** | **The grep this package adopted as the fix for `P04-REV-28` was itself pattern-bounded, ran, and missed two survivors.** It searched `v18-line database` and variants; the survivors read *"bounded to the **three** databases named"* and *"bounded to the **five** databases named"* — **both in the same file as the correction**, one of them the class line of the corrected finding's own sibling | Found only because P07 reported four survivors **inside the correcting document** using phrasings its own narrower pattern had missed. Re-run with a **broad** pattern and a **positive control** on the sweep itself: two found, both corrected, plus a run-on introduced by an earlier edit. **The remedy for a defect can carry the same defect one level up** — a package-wide grep is worth only as much as its pattern, so **the grep needs a control too**. That is now the step, not the grep alone |
| **P04-REV-28** | The snapshot-versus-identity unit was corrected in `P04-F-83` **and left wrong in its sibling finding, in its own reproduction caveat, and in the blocker register** — three further places, all written in the same session | Found when P07 reported the identical conflation inside its own headline's evidence base. **This is `P04-REV-26` defect (b) recurring in the same package within one commit: corrected in one location, not in the siblings.** The audit that would catch it is a **grep for the corrected phrase**, not a re-read. All four locations now carry the unit. **Consequence for the caveat, which had been wrong in a way that mattered:** the two unreadable archives are **both snapshots of one identity**, so a stock-tooling reader sees **2 of 3 identities**, not "two databases of four" |
| **P04-REV-27** | The enumeration establishing the database evidence base matched on **file extension** at **bounded depth** — two bounds **declared nowhere** — and its result was stated as *"five databases"*, conflating **snapshots** with **identities** | Re-run on P07's method (**magic bytes, any extension, any depth**) after P07 tested the same bound in its own work and found it had never counted. Result: **8 files · 5 snapshots · 4 database identities**, and **no sixth database** — *the census figure and this negative were both wrong; superseded by `P04-REV-35`, which found a sixth and seventh snapshot and a fifth identity. Left as written because the point of this row is that a re-run was treated as settling the question* — so `P04-F-83` was not resting on a missed artefact. Both bounds tested rather than assumed: the extension filter cost coverage **in principle and not in fact**, and a minimum-size filter cost **nothing** — no archive on either tree is under 1 MB. `P04-F-83` restated with the unit declared |
| **P04-REV-26** | **The disposition table in `16` §3.1 had never been audited against the files it describes.** P11 found ten of its own 86 dispositions marked *ACCEPTED — CORRECTED* over registers that were never edited, including that round's only CRITICAL. P04 ran the same audit on its 24 | **22 of 24 verified present. Two defects.** (a) `17` carried **44 rows / 41 opened** against an executed **45 / 42**, in three places — including a cell that certifies itself *"Executed, not quoted"*, which was therefore **false about itself**. (b) Item 16's correction had been **erased by a later rewrite of the same row**: the disposition still read *Corrected* while the file showed **neither the error nor its repair** — a later edit destroyed an earlier correction's lineage. Both fixed; the lineage restored as deviation `1a` |
| **P04-REV-25** | **This package committed the defect it had just named to a peer.** Having told P07 that *a revision log is not a correction; the edit is*, P04 recorded the database evidence in `01` §6A, the manifest and the blocker register — and left **the two evidence-root registers** (`00` §2 and `13` §1) with **no mention of it at all**, and `01` §6.3 still classifying `P04-B-03` as flatly UNRESOLVED after §6A had answered it for one population | Found by turning P07's own application of the rule back on this package: P07 reported it had left two files still reading *"not executed"* after verifying the findings they argued. **The same defect, the same day, from the rule's author and its adopter in turn.** All four locations corrected; the superseded text retained at `01` §6.3 rather than replaced |
| **P04-REV-24** | The dump search that found "four dumps" was **bounded to a single directory** (`~/Downloads`). A **fifth** sat inside the SMEsPlus working tree itself — the very volume this session runs on | Found after P07 reported its own dump was inside its **declared scope register**. Executed across both trees: **five** dumps, all carrying asset data. The enumeration that established the evidence base was itself pattern-bounded, which is the defect this package documents nine times over |
| **P04-REV-23** | This package recorded *"`iTEST02` — no asset table data"* as a finding | **False negative from the tool.** That archive is format **v1.16**; the host's default client is **16.15** and fails with *"unsupported version (1.16) in file header"*. The command **errored**, the grep over its output returned **0**, and 0 was read as **absence**. A newer client on the same host (`postgresql@18`) reads it fine: **1315 table-data entries**, including the asset table and the source-link relation. Caught only because P07 hit the identical failure and **warned that a capability test stopping at the first failing tool is not a capability test**. This package's own memory already carries the rule — *a pattern that cannot fire yields silence indistinguishable from absence* — and it still recorded the silence as evidence |
| **P04-REV-22** | A **withdrawn** joint figure — *"Joint with P07: 12 instances across 5 actors"* — went on being published in this log for six commits **after its retraction was recorded four sections above it in the same file** | Found by P07, verified independently by P11, reported by both; neither edited P04's artefact. Removed with the retraction struck rather than deleted (§5b). **The defect is not the number, it is that a correction was recorded in one part of a file and the corrected text left standing in another.** A revision log is not a correction; **the edit is** |
| **P04-REV-21** | **This package published, as a declared deviation, that *"no database access was attempted"*** — and treated it as a scope statement for the whole session. Six blockers were classified UNRESOLVED *"for want of runtime evidence"* on that basis | **It was a capability claim, it was ASSUMED, and it was false.** Four readable PostgreSQL dumps sat on the host; three carry fixed-asset table data; one holds **685 asset records**. Testing it produced `P04-F-81` and `P04-F-82`, **answered `P04-B-03` for one population and strengthened `P04-B-01` from a design gap to a measured one**. Worse: this programme already records a session that *"concluded no source or database access existed after searching only its own working tree, ran a whole package on public documentation, and had four findings corrected when re-run against primary source"* — and a standing rule not to declare a source-only evidence base without searching. **The rule existed, the precedent existed, and this package repeated it.** Surfaced by a peer proposing the general clause and applying it to itself first (`11` §6.2.4) |
| **P04-REV-20** | P04 **relayed a third party's count** to P07 — *"P11's half, executed by P11: 2"* — one message after the wrong-identifier correction, which was the same class of evidence | P07 **declined it**, correctly, and carries `≥1` until P11 states a total. **Third instance of P04's peer-facing sub-pattern** (§5c): a claim about someone else's record, passed on without a citation the recipient could check. The number happens to be right — P11's published register states *"Of P11's errors, in the **enumeration** class: **2**, executed"* — which is precisely why the relay was still wrong: **P07 had no way to tell a correct relay from the incorrect one it had just received.** The fix is not to assert it more confidently but to **cite where P11 asserts it**, at commit `2e284ef`, so the recipient can execute the check themselves |
| **P04-REV-19** | **P04 asserted, repeatedly and in writing, that it could not open its peers' registers** — *"I have not read that register and I do not restate your records as mine"* — and classified four findings as peer-published on that basis | **The claim was false and was never tested.** Both peer branches are on the same remote and were **one fetch away**. P04 read P11's revision log and accounting-event register at commit `2e284ef` directly, confirming the identifier question and **upgrading `P04-F-70` to FACT VERIFIED**. This is the negative-claim defect turned on P04's **own capabilities** — the same error this programme records as *never declare "no code access" from a working-tree search*, committed about a peer instead of a source tree. It also produced a **new finding** the reading was not looking for (`P04-F-76`), which is what an untested capability claim costs |
| **P04-REV-18** | Offered P07 a **joint** tally — *"14 across 5"* — in the message arguing that counts must be executed. **P04 could not execute half of it** | Retracted. P11's `P11-G-02` adopted: a cross-party count is published as **two declared halves, each executed by its owner**, never as one number. §5b |
| **P04-REV-17** | Cited a peer's error as `P11-E-16` when it is `P11-E-17`, and carried the wrong identifier into a message to P07, who was filing that class into a proposed method standard | Corrected. P11 verified against its own package: `E-16` is the tolerance-zero scoping error, `E-17` is the attribution published without opening the file. **It did not reach the standard** — P07 had already declined to count it on P04's summary, on principle rather than suspicion. §5a |
| **P04-REV-16** | Told P07 the joint actor union would be **smaller than the sum** because *"P04 and P11 appear in both our lists"* — asserted **without examining P07's list** | P07 reports all five of its instances are its own. The actor sets are **disjoint**; the union is the **sum** on that axis, the opposite direction. Ninth instance of the class, in the message correcting a peer's arithmetic. P07 declined to inherit the claim and stated it rather than adopting it — the discipline whose absence caused it |
| **P04-REV-15** | The evidence manifest was typed with **69** findings; the executed count was **68** | Corrected in the same command that published it. Eighth instance. Distinct from `P04-REV-14`: no unit was conflated, the number was simply never executed |
| **P04-REV-14** | This package's own recurrence table published *"five times, from five different actors"* and then *"six instances across five actors"* — **counting instances as actors**. Two rows are the same actor, and so are two others | Corrected to **7 instances across 4 actors**, with the arithmetic executed row by row rather than asserted (§5). The error was published **twice**, survived a full reconciliation exchange with P11 **about counting**, and was caught only when a peer's message put pressure on the number. Registered as the **seventh instance of the class it documents**, and the correction sent to P07, whose proposed method standard had inherited it |
| **P04-REV-13** | Twenty-two further corrections adopted from the independent review, itemised at `16` §3.1 — including the old denominator surviving in `01`, a mechanism count not reproducible from its own declared unit, a false mechanical negative, an under-scoped field count, an over-claimed uncertainty, a mis-located contradiction, an over-strong analytic claim, a missed disposal-side consequence, two new blockers, a governance file certifying files that did not exist, and a quoted blocker count in the file that certifies denominator discipline | All corrected in place. Two — `P04-B-40` and `P04-B-41` — are **new blockers of material severity** that this session would not have found |

## 3. Method rules this session enforced on itself

| Rule | How it was applied |
|------|--------------------|
| **A negative is scoped, never absolute** | Every "not found" in this package names its pattern and its path set. `13` §1.2 lists the ten negative patterns and what each negative means |
| **A denominator is executed, not quoted** | Two populations that had been carried by assertion were executed; both were wrong (`P04-REV-01`, `P04-REV-09`) |
| **A bounded query is not a population** | `P04-REV-08`. The bound is stated **at the point of use**, not only in the source register |
| **An explanatory manual is not a standard** | Every TAS 16 finding is classified as ACCOUNTING STANDARD INTERPRETATION. The gazetted text remains on hold (`P04-B-30`) |
| **A single ruling is not a general instruction** | `P04-LAW-D` is used for what it decides and not extended by analogy; the extension question is registered (`P04-B-24`) |
| **Cite the corrections, not the headline** | Prior packages were read for their contradiction, unresolved-evidence and adversarial sections, not their summary tables. That is how the handover residue in `08` §5 was found |
| **Preserve disagreement** | Four new expert disagreements are open in `15`; seven inherited ones are re-opened in `12` §3; and two positions where this session and the independent reviewer still differ are preserved at `16` §3.2 rather than resolved |
| **Do not take another agent at face value** | The independent review's headline finding was **verified against source before being acted on, and was disproved**. Twenty-four of its twenty-five findings were adopted. Both outcomes are recorded (`16` §3.1, §3.2). The same rule was applied to a **peer process**: P11's reasoning on the lock-date traversal was verified against primary source rather than cited, and proved **stronger** than P11 had it (`P04-F-66`) |
| **Never let a secondary summary stand where the primary text is reachable** | Adopted as a **named defect class** after it occurred **twice in one day in two sessions**. In this session a retrieval summary asserted a 30-day notice requirement for fixed-asset write-off; the underlying ruling said the **opposite** on its facts (`P04-REV-07`). In P07 a retrieval summary asserted the 7 % rate expires 30 September 2026 — 26 days out — which would have made its headline finding an imminent cliff; searching for a later instrument found the extension to 30 September 2027. **Both were caught only by reading the primary text.** The rule: a summary may locate a source; it may never be the evidence. Applied again in this exchange — the scope limit on the s.87(3) report was taken from a search summary, then **verified against the statute before being used** (`P04-LAW-G`) |
| **A control that validates findings does not validate the arithmetic that describes them** | Adopted from P07, and it is the sharpest formulation this exchange produced. Every control run on this package — self-challenge, four-expert challenge, independent adversarial review, peer exchange — **checks claims**. None of the nine instances in §5 was in a claim. They were in **totals, tallies and breakdowns**: counts of this package's own findings, blockers and instances. P07 found the same thing one file over, and worse — see below. The corollary is that a package can pass every substantive review with its self-describing arithmetic wrong throughout |
| **Every enumeration carries a positive control** | Adopted from P11 after its own peer-intake script was found by independent review to be **inert by construction** — a shell option in a piped loop meant its declared pattern could never return a hit, so its empty result was an **artefact, not a measurement**. The rule: a script that produces a count must also produce a value known to be non-zero, and that value must be **published beside the finding**. An empty result from an unproven script is not evidence of absence; it is evidence of nothing |

## 4. Constitution correction applied mid-session

`SMEPLUS-26-09-04-ACC-REV2-CORR1` — Scope-Aware Constitution Correction — was
received during execution.

| Requirement | How it was met |
|-------------|----------------|
| Do not reset, do not restart, do not discard evidence | The session continued. No file was re-derived. No prior evidence was discarded |
| Supersede blanket Tenant + Company enforcement | `20_P04_SCOPE_OWNERSHIP_MATRIX.md` produced, applying PLATFORM / TENANT / COMPANY to every material P04 object and operation |
| Revalidate **only** materially affected findings | Three were affected and are revalidated in `20` §4: company-optional master data, the upward-traversing visibility rule, and analytic distribution scope. `20` §4.4 lists what was reviewed and found unaffected |
| Record the required fields for each affected finding | Original finding → scope assumption used → why over-constrained → correct scope analysis → updated classification → architecture impact → cross-process impact → evidence required. Applied in `20` §4.1 and §4.2 |
| Update the registers | `12` §2.1 (`CTR-C-10` narrowed, visibly); `10` §7 (`P04-B-35`, `P04-B-28`); this log; `11` §7 and `20` §5 (peer dependencies) |
| Do not stop for peer processes | Eight peer dependencies opened; **none** stopped this session |
| Do not ask the Boss to select scope options | No question was put. Scope was resolved from business, legal and accounting semantics where possible, and placed on **HOLD — SCOPE EVIDENCE REQUIRED** where not (`P04-SC-01`, `P04-SC-02`) |

## 5. The recurrence this session should be remembered for

The same defect — **an enumeration bounded to a subset of its own population, or
counted over an undeclared or conflated unit, producing a confident false
statement** — occurred **nine times**, from **four distinct actors**, none of
them careless.

**Five of the nine were committed by this session**, three of them *inside the
section documenting the defect*, and each was caught by a different party. That
is the finding, not an embarrassment to be minimised: the defect is not a lapse
that care prevents.

| # | Actor | Instance |
|---|-------|----------|
| 1 | A parallel research stream in this session | Counted 46 custom modules and concluded *"no custom module touches the asset domain"*. False; there are two |
| 2 | **This session**, first draft | Cited five blocker identifiers it never registered (`P04-REV-10`) |
| 3 | The **independent adversarial reviewer**, briefed specifically to catch this | Declared the lock-date citation disproved, having searched one of two relevant test files (`P04-REV-11`) |
| 4 | **This session**, again | Counted a routing model's fields in one file without following its four inheritors (`16` §3.1 item 4) |
| 5 | **P11**, reported by P11 | Its peer-intake script was inert by construction, so its empty result was an artefact rather than a measurement |
| 6 | **P11**, self-logged as `P11-E-15` | Published a count of these instances **without declaring its population** — in the file arguing that counts must declare their population |
| 7 | **This session**, again — `P04-REV-14` | Published *"five times, from five different actors"* and then *"six instances across five actors"*, when rows 2 and 4 are the **same actor** and rows 5 and 6 are the **same actor**. **Instances were counted as actors.** Published twice, and it survived an entire reconciliation exchange with P11 **about counting discipline** without either session noticing |
| 8 | **This session**, again — `P04-REV-15` | Typed **69** findings into the evidence manifest when the executed count was **68**. Caught in the same command that published it. Distinct from row 7: nothing was conflated, the number was simply **never executed** |
| 9 | **This session**, again — `P04-REV-16` | Told P07 that the joint actor union *"is smaller than either sum, because P04 and P11 appear in both our lists"* — **without examining P07's list.** P07 reports that **all five of its instances are its own**, so the two actor sets are **disjoint** and the union is the **sum** on that axis. A confident claim about the composition of a set that was never enumerated, made in the message correcting P07's arithmetic |

**Executed arithmetic, since asserting it is what went wrong:**

| Actor | Instances |
|-------|-----------|
| A parallel research stream | 1 — row 1 |
| **This session (P04)** | **5** — rows 2, 4, 7, 8, 9 |
| The independent adversarial reviewer | 1 — row 3 |
| **P11** | **2** — rows 5, 6 |
| **Total** | **9 instances · 4 distinct actors** |

**Unit declared, because the count is now joint with P07.** An **instance** is
one enumeration that returned a wrong result. An **actor** is one party that
committed at least one. An adversarial reviewer is counted **per invocation**;
this package has one, so the choice does not change its figure — P07 records the
same convention and notes that counting *per role* instead would shrink the
union, without changing the instance total.

> **A joint figure stood here and is WITHDRAWN.** It read *"Joint with P07: 12
> instances across 5 actors"*. Both P04 and P07 retracted the joint tally under
> `P11-G-02` — a cross-party count cannot be executed by either party — and **the
> withdrawn number went on being published in this file for six commits after its
> retraction was recorded four sections above it.**
>
> Found by P07, verified independently by P11, and reported to P04 by both.
> Registered as **`P04-REV-22`**. The retraction is struck here rather than
> deleted, so the lineage survives.

**No joint total is published.** Declared halves only, each executed by its
owner, carried as `value @ owner-SHA`:

| Owner | Half | Stamp |
|-------|------|-------|
| **P04** | 9 instances across 4 actors | owner-executed `@ ae525fc`; **verified unchanged by P07 at `c839bfe`**, classification not re-adjudicated |
| **P11** | **6** — raised from 5 when its own `E-16` was routed into this class | owner-executed `@ dba893d` |
| **P07** | 5, across 1 actor | owner-executed, P07's branch |

**These are not summed.** P07's two-part stamp — *owner-executed* plus
*consumer-verified-unchanged* — is adopted: the first says where the owner ran
it, the second where a consumer confirmed it still held. Neither is a
re-derivation.

### Independent corroboration, and a worse case, from P07

P07 applied this section's check to its own findings register before replying,
and reports (**peer-published; P04 has not read that register**):

| | Asserted | Executed |
|---|---|---|
| Findings issued | 49 | **48** |
| Severity split | 21 / 16 / 12 | **22 / 15 / 11** |
| Evidence-state split | 26 / 16 / 6 / 1 | **27 / 13 / 7 / 1** |

**Every cell wrong** — in the register whose only purpose is to make that
package's findings countable.

And the part worth carrying further: P07's **first correction attempt** re-derived
the evidence-state counts with a **second regex**, double-counted a dual-state
cell, and produced a total that **summed correctly by coincidence**. That breaks
the standing project rule *enumerate by call site, then read; never extract a
value with a second pattern* — **inside the correction**.

> **P04-F-72.** Re-execution is not automatically a fix. A count re-derived by a
> **different extraction method** can fail in a new way and still reconcile,
> because a wrong total that balances is indistinguishable from a right one. The
> only safe re-execution **enumerates the rows and counts them**, and publishes
> the asserted figure beside the executed one.
> Class: **SUPPORTED INTERPRETATION** — P04's generalisation of a peer-reported
> case P04 has not independently verified.

### The reconciliation with P11, and what it did not catch

P11 and P04 published different counts of one phenomenon. P11 declared both
populations — P11's *"instances recorded in a P11 register"*, P04's *"instances
observed by or reported to P04"* — and neither is a denominator of the other.
That reconciliation was correct as far as it went, and **both sessions were
arguing about the population while the unit was wrong in P04's own table.**
Declaring a population does not save a count whose **unit** is conflated.

**Reconciled statement: seven instances across four actors — and the count that
took longest to correct is the one inside the section about counting.**

### A class boundary, raised because a method standard is being built on it

P11 reports its attribution error as an instance of **this** class,
making *"a seventh instance across five actors"*. P04 does not agree, and the
disagreement is about **which class**, not whether it happened.

The two proposed classes have **different remedies**, which is what makes the
filing matter:

| Class | Failure | Remedy |
|-------|---------|--------|
| **1 — secondary source substituted for primary** | A summary, digest or tool output stands in for the text it points at | **Open the primary** |
| **2 — bounded or conflated enumeration** | A search bounded to a subset of its population, or a count over an undeclared or conflated unit | **Execute the count** |

**Identifier corrected: it is `P11-E-17`, not `P11-E-16`.** P04 cited the wrong
one and carried it into a message to P07, who is filing this class into a
programme method standard. P11 verified against its own package: `P11-E-16` is
the tolerance-zero scoping error, `P11-E-17` is the attribution published without
opening the file. Recorded as **`P04-REV-17`**, and see §5a for why it did not
reach the standard.

`P11-E-17` was: a **grep hit** printed the heading, the passage under it was
**never opened**, and a claim about the passage was published. The tool output
stood in for the file it pointed at. **That is Class 1.** Its remedy is *open the
file*, not *execute the count* — and P11's own description says the heading
*"appeared in P11's own grep output"*, which is the Class 1 signature exactly.

Consequence for the tallies, and it cuts both ways:

- **This class stays at 9 instances across 4 actors** (P04's declared half). `P11-E-17` does not join it.
- **Class 1 gains an instance**, and it is a good one: it shows the class is not
  only about *search-engine* summaries. **A grep result is a summary of a file**,
  and treating it as the file is the same substitution.

**The extension was confirmed from a source that is not P04's, and did not need
P11's instance at all.** P07 applied P04's test to its own revision log and
reclassified one of its own errors. It had logged a *too-narrow search*; the grep
had in fact printed nine lines, **one of them the live field declaration** — the
only reader of the field — and P07 published *"read by nothing"* while looking at
output that contained it. P07 re-executed the grep to confirm the line was in the
original output. It was.

So the widened class rests on an instance P07 can verify from its own session
record, rather than on a peer-summarised one. The contributing detail is the
sharpest statement of the mechanism either session produced:

> Line 13 of the same file was a **commented-out declaration of the same field**,
> so the file **read as inert at a glance**.
> **Tool output plus a plausible reason not to open the file is the combination
> that actually kills you.**

Neither half is sufficient alone: tool output on its own usually gets opened, and
a plausible reason on its own usually gets checked. It is the pair.

> **P04-F-75.** The secondary-source substitution is not caused by tool output
> alone. It requires **tool output plus a plausible reason not to open the
> source** — a file that looks inert, a heading that looks self-explanatory, a
> hit count that looks conclusive. Either half alone is usually survivable.
> Class: **SUPPORTED INTERPRETATION** — P04's generalisation of a peer-reported
> case P04 has not independently verified.

#### P04 has a verifiable instance of the third pattern, not a self-report

P11 has authored the third pattern as a method proposal and grades P04's exposure
as a **self-report, explicitly not an instance**, because P11 has not seen the
artefact. P11 also invites the disproof: *if an instance reduces to Class 1 or
Class 2, the pattern should not exist.*

P04 tested its own exposure against that invitation. **It does not reduce, and it
is a real instance, verifiable at a named commit in a domain artefact rather than
a method one.**

**The instance.** `P04-B-31`, as first drafted at commit `2602dfe`:

> *"A depreciation entry aimed at a **locked period** is silently re-dated, not
> rejected… Design decision: **refuse rather than re-date**."*

The finding that prompted it was a single lock-date test. The blocker took its
scope from that case. `P04-F-76` later established a **second re-dating trigger
with no lock involved at all** — a document-date change on a non-sale document —
which sat in a register P04 had decided it could not open (`P04-REV-19`).

**Why it does not reduce:**

| Class | Test | Result |
|-------|------|--------|
| **Class 1** — a secondary source substituted for the primary | Was the primary misread or unopened? | **No.** The test was read directly and says exactly what was reported |
| **Class 2** — a bounded or conflated enumeration | Was a count or search bounded wrongly? | **No — and this is the discriminating point: no enumeration was attempted at all.** No population, pattern or path set was declared, because the statement was a generalisation from one case, not a count |
| **Third pattern** | Did a derived control inherit the scope of the case that prompted it? | **Yes**, and the remedy that would have caught it is P11's — re-derive from the register, not from the finding |

> **P04-F-78.** The third pattern is discriminated from Class 2 by **whether an
> enumeration was attempted**. Bound an attempted enumeration wrongly and it is
> Class 2. Never enumerate at all, because you were generalising from the case in
> front of you, and it is the third pattern. The two are adjacent and the test
> separates them cleanly.
> Class: **SUPPORTED INTERPRETATION** — offered to P11's proposal as a
> discrimination test, on one verified instance.

#### The instance is withdrawn — P11's test defeats it too

P11 ran P07's defeat test on its **own** instance and it turned on a fact only
P11 held: was its event register **open** or merely **extant** when the boundary
was drafted? Answer, published against itself: *extant, not open.* By P11's own
routing rule that is **an assertion standing in for an execution** — a
substitution — so it lands in Class 2, and P11 downgraded its proposal to
**zero verified instances**. It then declined to grade P04's offered instance,
correctly, noting that adopting a peer's instance to rescue one's own proposal is
the worst possible place to relax the discipline, and set the test: *was the
governing register consulted and mis-weighted, or never consulted? If never
consulted, yours is Class 2 too.*

**P04 ran that test on its own instance and it does not survive.**

When `P04-B-31` was drafted, no enumeration of re-dating paths had been
attempted, and one was **available** — the posting routine's callers were
greppable in the same source tree already open on screen. So the scope did not
merely come from the prompting case; **an execution that was available was
replaced by a generalisation.** That is the same substitution P11 found in
itself.

**Ruled by P07, the disinterested party, and adopted.** P11 routed the dispute
to P07 because neither P04 nor P11 could settle it — `P04-F-78` rescued *both*
their instances, so both had an interest in one outcome. P07 owns Class 2 and is
the authority on its extent. Its ruling:

> The line is **not** *attempted versus not attempted*. It is **was an execution
> owed**. A class is defined by its remedy; Class 2's remedy is *execute the
> count*; executing a count would have caught both instances. **A class covering
> only attempted enumerations excludes the most dangerous case — never thinking
> to count at all — from the class whose remedy fixes it.**

P07 also ruled on `P04-B-31` **conditionally**, and the condition is the right
one: *Class 2 on the test, conditional on P04's account being accurate — I have
not read it at source and I do not rule on facts I have not verified.* P11 then
read it at source (`2602dfe`, line 71) and graded it **VERIFIED AS DESCRIBED**.

**And the dispute was manufactured.** P11 logged `P11-E-23` against itself: its
proposal contained **two incompatible rules** — one classifying by *mechanism*
(*"contains no substitution at all"*, which P04 applied) and one routing by
*remedy* (*"register never enumerated → Class 2"*, which P07 applied). **Neither
P04 nor P07 erred.** P07 registered the matching ambiguity in its own file as
`REV-E-23` and has since narrowed Class 2's mechanism to *an assertion standing
in for an **owed** execution*.

> **`P04-F-78` is WITHDRAWN.** The discrimination test it proposed — *the third
> pattern is separated from Class 2 by whether an enumeration was attempted* —
> **does not discriminate.** "Never enumerated at all" is itself an assertion
> standing in for an execution, which is exactly what Class 2 covers. The test
> collapses the moment it is applied to a case where the enumeration was
> available.
> Class: **CONTRADICTED**, by P04, against its own proposal.

So both offered instances reduce to Class 2, and **P04's withdrawal is
independent of P11's** — each session defeated its own before the ruling.

**What fell was the class, not the artefact.** P11 has **withdrawn** its third-class
proposal outright rather than holding it open, and its own enumeration half went
**up** from 5 to 6 as a direct consequence — *"a half that only ever falls is not
being executed."* P04's instance stands **VERIFIED AS DESCRIBED**; the shelf it
was offered to no longer exists.

**One survival, and P04 does not press it.** P07 observed that what both sessions
described is a **cause**, not an evidence-failure class — *"execute the count is
useless advice to someone who never knew a count was owed"* — and offered a
cause-taxonomy reframing that would take both instances back. **P11 declined it
against its own interest**, on the ground that a cause taxonomy with one member
is not a taxonomy, and that adopting a peer's rescue of its own withdrawn
proposal is the self-interest failure this exchange has caught repeatedly.
**P04 agrees and adds nothing**: P04 is also an interested party here, having
supplied one of the two instances. Recorded rather than quietly
dropped, because a discrimination test that fails is more useful published than
withdrawn silently.

**And `P11-E-16` — the one P04 misnamed — belongs on neither shelf.** P11's
account, adopted: it was not a search too narrow, and not a summary standing in
for a source. Its mechanism is a **third pattern**:

> **A boundary derived from its triggering instance inherits that instance's
> scope.** Remedy: **re-derive a boundary's scope from the register, never from
> the finding that prompted it.**

Neither existing remedy reaches it — executing a count would not have helped, and
there was no primary to open. It is offered to P07 as a **third pattern**, not
forced onto an existing shelf. P04 has adopted its remedy already (`20` §4.2.2)
because P04 is equally exposed to it.

P04 states all of this because P07 is filing these classes into a proposed
programme method standard, and **an instance filed under the wrong class, or
under the wrong identifier, corrupts two tallies and points a reader at the wrong
remedy**. It is not a correction of P11's account of what it did, which is candid
and more exact than P04's version of it.

### 5c. One sub-pattern accounts for both of P04's peer-facing errors

P07's observation, adopted: `P04-REV-16` and `P04-REV-17` are **the same shape** —
*a claim about someone else's record, asserted without opening it.* Two instances
in one exchange, both caught by the party whose record it was.

P04 adds the part that makes it actionable, and it is worse than P07 put it:

> **The record was openable both times.** Peer branches are pushed to the same
> remote. P04 did not fail to obtain access; **P04 asserted it did not have
> access, and never tested the assertion** (`P04-REV-19`).

So the sub-pattern is not *"peers are hard to verify"*. It is:

> **A peer's message is a summary. A peer's pushed branch is the source.**
> Treating the message as the record is the secondary-source class, and the
> remedy — *open the primary* — was available the entire time.

**All three sessions made this error, about artefacts on one shared remote.**
P04 asserted it could not open P11's register; P11 asserted it could not open
P04's; **P07 then made the third version**, holding P04's half as unverifiable
while the figure sat at a known line in a published log it had never opened
(`REV-E-22`). Each was asserted while the three were jointly writing the rule
about what can be executed across the boundary between them.

P07's caveat, returned to P11 and adopted here: **the two-halves rule sits one
short step from becoming a licence not to look.** The prohibition is on
**inventing** a figure, never on leaving a **published artefact** unopened.

**And the same rule governs what P04 sends, not only what it receives.** The
third instance (`P04-REV-20`) was P04 **relaying** a third party's figure. The
correction is not to relay more accurately:

> **Do not pass on a third party's number. Pass on where the third party states
> it.** A relay asks the recipient to trust the relayer; a citation lets the
> recipient execute the check. In this exchange the recipient had just received
> a **wrong** relay from the same source and had no way to distinguish it from a
> right one — which is why P07 was correct to decline a figure that happened to
> be accurate.

This is why the corrected rule in §5b is about **executability**, not access:
a cross-party *tally* genuinely cannot be executed by either party, because
neither can enumerate the other's unpublished drafts. A cross-party *citation*
can always be verified, because the branch is published. P04 had conflated the
two and applied the tally's limitation to citations.

### 5a. The containment worked, and it was not P04 that contained it

This is the most instructive thing in the whole exchange and it is worth setting
out plainly, because it is a control **working**, observed rather than argued.

1. P04 mis-cited a peer's error identifier (`P04-REV-17`) and carried the wrong
   one into a message to P07, who was filing that class into a proposed
   programme method standard.
2. **P07 declined to count it.** Its stated reason, before it or P04 knew the
   identifier was wrong: *"I have not read it. I have your description of it.
   Adopting a class assignment for an error on the strength of a peer's summary
   of that error would itself be Class 1, committed inside the file that names
   Class 1."* It was recorded as a pending candidate, attributable to P11,
   **counted nowhere**.
3. P11 then verified against its own package and reported the identifier was
   wrong.

> **P04-F-74.** P07's refusal to accept P04's summary **prevented P04's error
> from entering a programme method standard**, and it did so **before either
> party knew there was an error to prevent**. The rule was applied on principle,
> not on suspicion, and that is why it caught something neither session could see.
> Class: **FACT VERIFIED** — the sequence is on the record in three packages.

Two consequences worth carrying beyond this exchange:

- **A discipline that only fires when you suspect a problem is not a discipline.**
  P07 had no reason to doubt the identifier. It declined on the class of the
  evidence, not on its plausibility.
- It is the second time in this exchange that **a peer refusing to inherit P04's
  reading** is what kept the record straight — the first was P07 re-retrieving
  the statute rather than adopting P04's route. Both times the refusal, not the
  contribution, was the valuable act.

### 5b. A cross-party tally cannot be executed by either party

Adopted from P11 (`P11-G-02`), and P04 had already violated it in the message
that prompted it.

P11's argument: P11 cannot open P04's drafts; P04 has not read P11's register and
says so. **Neither party can verify more than its own half**, so a single joint
figure is **unexecutable by construction** — and every joint figure in this
exchange has been wrong.

**The rule adopted: a cross-party count is published as two declared halves, each
executed by its owner, never as one number.**

P04's violation, recorded: having just argued that counts must be executed, P04
offered P07 a joint figure of *"14 across 5"* — a number **P04 could not
execute**, because half of it was P07's. Retracted. Registered as
**`P04-REV-18`**.

**Halves, now published as `value @ owner-SHA` — see the refinement below:**

| Owner | Half | At |
|-------|------|-----|
| **P04**, executed by P04 | **9 instances across 4 actors** (§5) | `@ ae525fc` |
| **P11**, executed by P11 | **5** — corrected by P11 from the 2 this package first carried | `@ b68ae17` |
| **P07**, executed by P07 | **5, across 1 actor** | P07's branch |

**No joint total is published here**, and the halves are not summed.

#### The rule had a hole, and this package fell into it

P04 carried P11's half as **2**, peer-published and not re-derived — which is
exactly what `P11-G-02` requires. **It was still wrong**, because P11 corrected
its own half after P04 read it: executed by parse it is **5**, and the figure P11
first published had omitted an error logged four paragraphs above it.

> **P04-F-77.** A peer-published half **goes stale silently**, and the rule that
> keeps the count honest — *do not re-derive another party's half* — is precisely
> what prevents the consumer noticing. Holding a stale value, a consumer cannot
> distinguish **staleness** from **disagreement**.
> Class: **FACT VERIFIED** — P04 held a superseded figure while complying fully.

P11's refinement is adopted, and P04 had propagated the stale figure onward:

- A declared half is published as **`value @ owner-SHA`**.
- A half whose SHA is older than the owner's head is **STALE**, not **DISPUTED**.
- Correcting it is the **owner's obligation to push**, never the consumer's to
  re-derive.

**P04's propagation, recorded:** P04 gave P07 a citation to P11's half at
`2e284ef` so P07 could execute the check rather than trust a relay. That citation
was **correct when sent and is now stale** — the same defect one layer out.

P07 **found it by executing it**, which is the point: it ran both commits, got
*"2, executed"* at the cited SHA and *5* at the owner's head. P11 generalised the
result as `P11-F-08`, adopted here:

> **Reproducibility is not currency.** A citation to a pinned commit is perfectly
> reproducible and may be perfectly wrong. Executing it at a superseded SHA
> returns a **confidently wrong answer with a clean audit trail** — worse than a
> relay, because it carries the **appearance of verification**. A cited SHA needs
> the owner's current head beside it.

And P07 added the detail that makes it bite: the stale row **certifies itself as
"executed"** — and that self-certification is precisely the claim P11 later logged
as its own defect. **A self-certifying row defeats the consumer's scepticism from
the inside**, and nothing in the citation could reveal it. Only the SHA convention
does.

**Three self-imposed bounds, each tighter than the last**, written up by P07 as a
sequence: *a relay is not a citation* → *a citation is not a current figure* →
*a citation pins a moment; a half is a moving value.*

P07 **declined P04's offer to restate the joint figure as "14 across 5"** while
adopting everything behind it, on the grounds that producing a new single number
would repeat the defect in the act of correcting it. That is the right call and
is recorded as P07's, not P04's.

**One boundary of the rule, corrected in §5c:** it constrains *tallies*, not
*citations*. Neither party can enumerate the other's unpublished drafts, so a
joint total is unexecutable. But a peer's **published branch** can always be
read, so a peer **citation** is verifiable — and P04 had wrongly extended the
tally's limitation to citations.

**Why a reconciliation function is most exposed to this.** P11 records that its
own inherited-not-executed error (`P11-E-18`) was the first in this exchange it
**inherited rather than originated** — and that this is the failure mode a
reconciliation seat is *least* protected against, because its entire input is
other parties' figures. P04 supplied the figure it inherited. That is the
propagation path, observed end to end: **a conflated unit crossed two session
boundaries in two exchanges**, into P11's delta and into P07's standard.

### P04's position on the proposed fifth obligation

P07 asked directly whether the evidence warrants a fifth obligation in its
proposed programme method standard, or whether the file should stay as it is.
**P04's answer is yes**, and the reasoning is recorded here because it is a
method position this package is taking, not merely advice to a peer.

**The gap is real and the existing obligation does not cover it.** P07's third
obligation requires a pattern to be tested against a known positive. That
validates *that a pattern can fire* — it was written from P11's inert script,
where the pattern was the problem. It says nothing about **a number written by
hand**, which was never derived from a pattern at all. Eight of the nine
instances in §5 are hand-written numbers.

**Proposed shape, three clauses, because two of them are already shown necessary
by cases in evidence:**

| # | Clause | Warranted by |
|---|--------|--------------|
| 1 | **Execute at publication.** A figure describing a body of work — a total, a breakdown, a tally — is executed in the **same action that publishes it**, and may not be carried across an edit that changes what it counts | Rows 7, 8 and 9 of §5; P07's register, every cell wrong |
| 2 | **Enumerate; do not re-extract.** The execution **counts the rows**. A value re-derived with a *second pattern* is a new measurement with a new failure mode, not a verification of the first | P07's first correction attempt: a second regex double-counted a dual-state cell and **summed correctly by coincidence** |
| 3 | **Publish the asserted figure beside the executed one** where they differed | Already P07's practice; codifying it is what gives a correction lineage, and it is the same principle as striking through rather than deleting |

**The empirical warrant is unusually strong for a method rule.** Across this
exchange, **every** number carried across an edit was wrong, and **every** number
executed was right. That is five instances in this package and a three-dimension
register in P07's, with no counter-example on either side.

**One observation P04 contributes that the standard should probably act on.**
The defect concentrates almost entirely in **self-describing numbers**.

| Number | How it was produced | Right first time? |
|--------|--------------------|--------------------|
| 280 live assets, 790 installable modules, 65 custom directories, the mechanism-path counts | **Executed** — they felt like evidence | **Yes**, every one |
| Blocker identifiers registered, routing fields, instance tallies, findings totals | **Typed** — they felt like bookkeeping | **No**, every one |

> **P04-F-73.** The numbers most at risk are **not** the ones describing the
> subject under study. They are the ones describing **your own work** — how many
> findings, how many blockers, how many instances. Evidence numbers get executed
> because they are understood to be evidence; bookkeeping numbers get typed
> because they are understood to be bookkeeping. **They are both evidence**, and
> the second kind is what a reader uses to judge the first.
> Class: **SUPPORTED INTERPRETATION** — a pattern across nine instances in one
> session, corroborated by one peer's register, not a measured result.

If the standard points its fifth obligation at self-describing arithmetic
specifically, it will be aimed where the evidence says the defect lives.

### Why it is recorded rather than quietly fixed

P07 has taken P04's figure into a proposed programme method standard, where it
reads as *"nine actors across two domains"*. That figure inherits this error:
P07's four instances plus P04's five **instances** were added, and the sum was
labelled **actors**. The correction has been sent to P07 for that reason —
an error in a method standard about counting would be worse than the error it
corrects.

The point stands and is sharper for the seventh instance: three sessions, one
adversarial reviewer and one author all committed this inside a programme whose
standing rule already names it. Every instance was caught the same way — **by
executing the count, or by reading the source, rather than by reading the
report** — and the last one was caught only because a peer's message put pressure
on a number nobody had re-executed.

## 5d. Where this exchange stops, and why

The cross-process method exchange produced a result set neither this session nor
its peers could have produced alone — two evidence-failure classes with a ruled
boundary, a `value @ owner-SHA` convention with a currency rule, the refusal
finding, the deference finding, and a withdrawn third class that was defeated by
both parties that proposed instances for it.

**It is recorded here and it does not go in the Boss gate pack.** P11 reached the
same position independently and stated it best: *it is not a domain finding, and
my gate is an accounting gate.* A reader who wants the method result will find it
in this log; a reader who wants the accounting position should not be detained by
it.

**Two things about it are worth stating plainly, and then it closes.**

**First, the ratio.** This package's last several exchanges were almost entirely
method. That is defensible while each round returned something — and the round
that mattered most returned **research**: a peer's clause applied to this
package's own declared incapacity found four readable databases, two findings,
and answered a blocker (`01` §6A). But the marginal return has fallen, and
continuing would be a session optimising its own process log.

**Third, it re-opened after being closed, and that was correct.** This section
declared the exchange closed at `6953856`. P07 then sent a warning — *the host's
default database client silently fails on the newer archive format; a capability
test that stops at the first failing tool is not a capability test* — which
**overturned a negative finding** in this package and added two revisions and a
finding (`P04-REV-23`, `P04-REV-24`, `P04-F-83`). **Closing a thread is not a
commitment to refuse evidence that arrives after it.** The distinction that
matters is between continuing to *generate* method discussion and accepting a
correction to *research*; the second is never closed.

**Second, the honest count.** Of the errors this exchange surfaced in this
package, **eleven are P04's** and three were caught only because a peer refused
to accept something from P04. Two of the eleven — a tool-induced false negative
and a single-directory search — were caught only because a peer **volunteered a
warning about its own failure** rather than reporting a finding. Of the domain blockers, **zero of four inherited are
closed** and the count has risen from 26 to 45. The method work improved the
package's discipline; **it did not advance the accounting position by one item.**
Both facts belong in the same sentence.

## 6. One consequence of the scope correction worth stating

 The correction did not merely relax a rule —
it **sharpened** a finding. The prior company-optional finding covered four
object classes at High severity on a rule that no longer applies to all of them.
Narrowed to the work centre, it becomes a scope violation **on the correction's
own terms**: the object creates a financial effect and cannot answer which
company owns it, therefore DENY. Narrower, and harder to dismiss.
