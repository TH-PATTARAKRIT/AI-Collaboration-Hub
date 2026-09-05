# P01 — RESEARCH ERROR AND REVISION LOG

Session: `SMEPLUS-26-09-04-ACC-P01-P2P-REV2-001`
Layer: **1 — Clean-room business learning.**

Rule: **never delete an earlier incorrect conclusion.** Every entry preserves the original
finding, its original evidence, why it was wrong or insufficient, the new evidence, the
corrected finding, and the architecture impact.

---

## `ERR-P01-01` — three mis-cited line ranges in the primary evidence base

| Field | Content |
|---|---|
| **Original finding** | Four evidence items in the primary evidence base carried line references that did not resolve to the code they claimed. |
| **Original evidence** | The line numbers were taken from the surrounding region while reading, not re-derived after the reading. |
| **Why wrong** | Three of the four pointed at blank lines or unrelated statements. A reviewer following them would have found nothing and would have been entitled to treat the finding as unsupported. |
| **How found** | **By the author**, through a mechanical re-resolution step: every cited line was printed back from the file and compared to the claim before the file was committed. |
| **New evidence** | Corrected ranges re-derived by targeted search for the construct itself. |
| **Corrected finding** | The four substantive findings are unchanged; only their citations moved. Cancellation guard, receipt-entry date selection, receipt credit-account selection, and the missing-account errors. |
| **Architecture impact** | None on conclusions. Material on **evidence integrity**: it demonstrates that a citation written while reading is not yet evidence until it has been resolved back against the file. |
| **Control adopted** | Every citation in this package was mechanically re-resolved before commit. The command and its result are in the evidence manifest. |

---

## `ERR-P01-02` — an enumeration pattern that was not bounded the way it was declared

| Field | Content |
|---|---|
| **Original finding** | A probe intended to locate model declarations reported implausible counts, including 25 declarations of a single core model and 41 of another. |
| **Original evidence** | Pattern `_name\s*=\s*['"]<model>['"]`, applied over whole files. |
| **Why wrong** | The pattern had **no left anchor**, so it also matched any identifier *ending* in the same suffix — an assignment such as `model_name = "<some model>"` matched exactly as a genuine declaration would — and it matched inside transient helpers, reports and comments. The declared population ("model declarations") and the pattern actually used ("any assignment to something ending in `_name`") were different populations. This is precisely the defect the project's denominator rule names: *a deterministic enumeration is bounded by its matching pattern, not by the source.* |
| **How found** | **By the author**, because the counts were implausible on their face. It would not have been caught by a pattern that returned a plausible number. |
| **New evidence** | Pattern re-anchored to a full-line match at class-body indentation, and the model kind (persistent vs transient) recorded alongside. |
| **Corrected finding** | Counts fell to plausible values. The corrected probe was then used, and its own false-negative modes were declared in `P01_SCOPE_OWNERSHIP_MATRIX.md` §1 — including the decisive one: **the probe proves presence of company scoping, never its absence**, because a company field added by an extending module is invisible to it. |
| **Architecture impact** | None on conclusions, because no finding had yet been drawn from the faulty run. The corrected probe's absence results are therefore all recorded as class **B**, not class A. |

---

## `REV-P01-01` — constitution correction `SMEPLUS-26-09-04-ACC-REV2-CORR1` (SCOPE-AWARE)

| Field | Content |
|---|---|
| **Trigger** | Boss correction received mid-session, superseding any wording implying that tenant and company context are mandatory for every operation, and establishing PLATFORM / TENANT / COMPANY as the canonical explicit scopes. |
| **Scope assumption previously used** | The SaaS-control section of the session directive was read as a blanket requirement that every event preserve both tenant and company context, and that any cross-company financial effect is prohibited absent an explicit business transaction. |
| **Why it is over-constrained** | It conflates ownership, availability, operational scope, financial scope and reference scope. Under the corrected model, a platform-level or tenant-level object legitimately carries no company context, and a genuine intercompany transaction legitimately produces an effect in a company other than the executing one. Judging those as defects would have produced false findings. |
| **Findings materially affected** | Two, both re-stated rather than withdrawn. (1) the cross-company auto-generation trigger; (2) the placement of general-ledger accounts on catalogue objects. |
| **Correct scope analysis (1)** | The generated document is COMPANY-scoped and owned by the target company; execution is in the source company. That shape is not itself wrong. What is wrong is that **ownership of the target company's financial effect is not proven** — it is inferred from an ancestor match in the TENANT-scoped contacts hierarchy, resolved with elevated privilege, first match winning. The corrected rule states `REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`. No tenant test was found (class B). Since unrelated companies are separate tenants by default, this is a candidate tenant-boundary crossing. |
| **Correct scope analysis (2)** | Company-scoped account values held on tenant-scoped catalogue objects is a **correct** expression of `OWNERSHIP SCOPE ≠ FINANCIAL SCOPE`, and would have been mis-reported as an isolation gap. The genuine defect underneath it is narrower and sharper: **mutation authority follows the tenant-scoped object while the financial effect is company-scoped.** |
| **Updated classification (1)** | `HOLD — SCOPE EVIDENCE REQUIRED`, tolerance-zero weight retained on the tenant question. |
| **Updated classification (2)** | `CONTRA-P01-05`, SUPPORTED INTERPRETATION, with the authority question class B. |
| **Architecture impact** | A new required register, `P01_SCOPE_OWNERSHIP_MATRIX.md`, was produced. Three scope questions the source cannot settle are now explicit (`SC-01`, `SC-02`, `SC-03`), plus four routed or statutory ones. |
| **Cross-process impact** | `HO-06` is re-framed: the platform decision required is not "may companies interact" but "what proves ownership of a company-scoped financial effect". Peer processes P02–P11 inherit the same question wherever they trigger an effect in another company. |
| **Evidence required** | Record rules and access paths governing (a) the cross-company resolution and (b) mutation of company-dependent accounting values on tenant-scoped objects. |
| **What was NOT done** | No evidence discarded. No checkpoint re-run. No completed enumeration repeated. No return to L1. |

---

## `REV-P01-02` — expert briefs were issued before the correction

| Field | Content |
|---|---|
| **What happened** | The four independent expert challenges were dispatched **before** the constitution correction arrived. One brief (Database Design) instructed its expert to examine "multi-company / multi-tenant scoping" under the pre-correction reading. |
| **Attempted remedy** | Forwarding the correction to the running expert was attempted and **was not possible in this session** — the inter-agent messaging facility is disabled here. This is recorded as a fact, not as a resolved item. |
| **Consequence** | Any scope finding returned by that expert was produced under the superseded assumption and **must not be adopted verbatim**. Each was re-read against the corrected model during consolidation, and the re-reading is shown in `P01_AAS_PLUS_CONSOLIDATION.md`. |
| **Residual risk** | An expert may have suppressed a legitimate PLATFORM- or TENANT-scoped observation as "missing company scoping", or reported a correct scope split as a defect. Suppression is invisible to a re-read of what was written. **This is an unrepaired asymmetry and is carried as `DEP-P01-06`.** |
| **Architecture impact** | None directly. It bears on `EC-07`: a pass performed under a superseded constitution does not count as a clean independent pass under the corrected one. |

---

## `ERR-P01-03` — a cross-version claim asserted from a one-sided grep

| Field | Content |
|---|---|
| **Original finding** | Recorded as `EV-P01-44`: "the accounting-invoicing group has write on purchase order lines; **in the later generation** the same group additionally has write on the purchase order itself and on the bill-matching object." Presented as a `R1` → `R3` widening. |
| **Original evidence** | A grep of the later generation's access-control file that returned three grants, compared against an earlier grep of the older generation that had been filtered to the order-line rows only. |
| **Why wrong** | **The two sides were not searched with the same pattern.** The older generation was queried for the order-line model; the newer one was queried for the group. Naturally the second returned more rows. The older file in fact carries the **same three grants**. The claimed cross-version widening does not exist. |
| **How found** | **By the author**, within minutes, by running the group-level query against the older generation as well — the symmetric query that should have been run first. |
| **New evidence** | Both generations grant the accounting-invoicing group read+write, no create, no delete, on the purchase order, on purchase order lines, and on the bill-matching object; the read-only accounting group gets read only. |
| **Corrected finding** | The segregation-of-duties exposure is **real, wider than the expert stated, and identical across both generations** — it is not a regression introduced by the newer one. |
| **Architecture impact** | The finding is strengthened, not weakened: the exposure is long-standing rather than new. |
| **Rule this violated** | The project's own standing rule that **cross-version claims require a symmetric comparison** — a file-level diff or the same query on both sides — never a token checklist run differently on each side. This session wrote that rule into three of its own briefs and then broke it. |
| **Control adopted** | Every cross-version statement in this package was re-checked for query symmetry before commit. |

---

## `ERR-P01-04` — the module denominator was a direct-dependency set, not a closure

| Field | Content |
|---|---|
| **Original finding** | Population A in the evidence base was declared as "modules that declare a dependency on the purchase module", with counts 12 / 8 / 17 / 5 / 11 across the five roots. Its declared false-negative modes named two classes: manifests whose dependency list is not a literal, and modules participating without depending on the purchase module. |
| **Why insufficient** | **A third false-negative mode was not declared and not taken: transitivity.** A module that depends on a module that depends on the purchase module is in the chain and was excluded. The declared population and the intended population ("modules in the procure-to-pay dependency chain") were different sets. |
| **How found** | **By an independent expert, not by the author.** The Functional Design expert reported that three approval modules in the custom v19 set were outside the brief's module pattern, and that one of them was the highest-value unread evidence in its assignment. Checking that pointed straight at the missing closure. |
| **New evidence** | The transitive closure was computed, resolving each custom root against the base root it layers on. Direct → closure: `R1` 12 → **35**; `R2` 8 → 10; `R3` 17 → **45**; `R4` 5 → 6; `R5` 11 → **13**. |
| **What the closure added that matters** | In `R1` and `R3`: **landed costs**, **subcontracting purchase**, **subcontracting landed costs**, purchase-manufacturing, purchase-repair, requisition-stock, dropshipping, and the purchase-approval-stock module. In `R5`: `multi_level_approval_configuration`, which depends on the custom purchase-request module and carries purchase references in five files. |
| **Severity** | **Material.** Landed cost and subcontract purchase are both named explicitly in the session directive as required P01 subjects, and both were outside the declared population. `multi_level_approval_configuration` is the module on which two of the expert's approval findings depend. |
| **Corrected finding** | Population A is superseded by **Population A′ — the transitive dependency closure**, with the resolution rule (custom root resolved against its base root) and the same literal-parse false-negative mode declared. Population B (content-token sweep) is unaffected and did reach several of these modules independently, which is why the gap did not silently propagate into the findings. |
| **Architecture impact** | None of the published findings is withdrawn. The correction **widens** what remains unsearched: the closure members that were never read are now explicitly class C rather than invisible. |
| **Rule this violated** | The project's own denominator rule: *declare the pattern AND its false-negative modes.* Two modes were declared; the decisive third was not. |
| **What this demonstrates** | The programme's standing observation held again: **the author declared a population, believed it bounded, and an independent reviewer found the boundary defect.** Self-checking found three of this session's four errors; the fourth — the one that changed a denominator — came from outside. |

---

## `ERR-P01-05` — this session's own expert brief contained two wrong identifiers

| Field | Content |
|---|---|
| **Original finding** | The brief issued to the Code & UI Architect expert instructed it to examine period control via `fiscalyear_lock_date`, `tax_lock_date`, **`period_lock_date`**, `hard_lock_date`, and to look for a **`bypass_lock`-style flag**. |
| **Why wrong** | `period_lock_date` does not exist in either generation — it is a pre-v17 spelling. The actual field set is `fiscalyear_lock_date`, `tax_lock_date`, `sale_lock_date`, `purchase_lock_date`, `hard_lock_date`; the brief also **omitted** `sale_lock_date` and `purchase_lock_date`, the two that matter most to a purchase process. There is no `bypass_lock` flag; the bypass is a sentinel-object comparison. |
| **How found** | **By the expert, not by the author** — because the brief carried the instruction *"if any path in this brief is wrong, report it as a finding."* The expert recorded both as class A negatives with the alternative spellings it tried. |
| **New evidence** | `EV-P01-47`, verified independently by this session against the company model. |
| **Corrected finding** | The purchase-specific lock date exists and is named in the brief nowhere. Had the expert followed the brief literally it would have searched for a field that does not exist, found nothing, and could have reported "no period lock" — the exact class-B-presented-as-class-A failure the project's negative-claim standard was written to prevent. |
| **Architecture impact** | None on conclusions. Substantial on **method**: the "challenge the brief" instruction is the control that caught it, and it is the only control in this session that could have. |
| **Wider point** | This is the second time in the programme that an instruction written by the author of a control contained an error only an independent party found. The lesson is not "write better briefs" — it is that **the instruction to contradict the brief must be in every brief.** |

---

## `ERR-P01-06` — a probe that produced fabricated absences from empty input

| Field | Content |
|---|---|
| **Original finding** | A first pass over three database dumps reported that **every** structure probed was absent from **every** database — including structures certain to exist. |
| **Original evidence** | The extraction command omitted the required output-file argument, so it wrote nothing and failed silently into files of zero length; the probe then searched empty files and correctly reported no matches. |
| **Why wrong** | The absences were artefacts of an empty input. Published as-is they would have been **six fabricated class-A absences across three databases** — the single worst failure mode available to this package, because a class-A absence is the strongest claim the negative-claim standard permits. |
| **How found** | **By the author, immediately**, because the probe printed the DDL line count of each extracted file alongside the results and every count was `0`. The count was in the command only because the extraction was new and unfamiliar. |
| **New evidence** | Extraction re-run correctly; 150,677 / 148,090 / 106,836 DDL lines. Probes re-run. A guard was added so that any file under 100 lines prints `EXTRACTION FAILED — no claims drawn` and is skipped. |
| **Corrected finding** | `P01_DEPLOYED_SCHEMA_EVIDENCE.md` §3, §5. |
| **Architecture impact** | None — nothing was published from the faulty run. |
| **Rule this reinforces** | **Never let a probe report absence without also reporting the size of what it searched.** An empty haystack and a haystack with no needle are indistinguishable to a search, and only the search's author can tell them apart. The programme's existing rule — *an empty taxonomy cell means UNSEARCHED, never ABSENT* — has a mechanical corollary: **print the denominator next to every zero.** |
| **Related** | The Functional Design expert independently hit the same class of defect twice (a path-splitting error yielding "no model files", and a zero line count on a file lacking a trailing newline yielding "this module is dead code"). Three instances in one session, from two independent parties, of a **tooling artefact presenting as a verified absence.** |

---

# CONTINUATION `SMEPLUS-26-09-05-…-TARGETED-CROSS-PROCESS-CLOSURE-001`

## `ERR-P01-07` — a structural absence that was really an unconfigured mechanism

| Field | Content |
|---|---|
| **Original finding** | Round 2 concluded: *"The receipt-to-bill bridge has no physical structure to run on in two of the three readable deployed databases"* — the goods-received clearing account and the valuation-layer table are absent from both v19 databases. Presented as the headline finding and as a **structural** absence. |
| **Original evidence** | Deployed-schema probes: the clearing-account column is absent from the item-category table in both v19 databases, and the valuation-layer table does not exist there. Both facts are **correct and stand.** |
| **Why insufficient** | The probe asked *"is the v18 structure present?"* and correctly answered no. It never asked *"then what does v19 use instead?"* — so it read the absence of one generation's mechanism as the absence of **any** mechanism. v19 in fact has a complete receipt-valuation mechanism: the counter-account moved from the item category to the **stock location**, and the valuation record moved from a separate layer object onto the **movement itself**. Nothing structural is missing; a **configuration** is missing. |
| **How found** | **By the author**, in this continuation, by asking the question the directive demanded — *prove the actual mechanics, do not force terminology* — instead of re-running the earlier probe. |
| **New evidence** | v19 requires a valuation account on the source or destination location. In both deployed v19 databases that account is set on **0 of 525** locations, so the gate cannot pass for any movement. The v18 deployment, by contrast, shows the bridge operating: 57,863 valuation layers carry a journal-entry link. |
| **Corrected finding** | `RECEIPT → BILL BRIDGE = DEPLOYMENT / CONFIGURATION-DEPENDENT`. v18 deployment: verified present and operating. v19 deployments: verified **not operable as configured**. |
| **Architecture impact** | **Materially different, and the correction matters in both directions.** The earlier reading would have told the programme that v19 cannot support a receipt-to-bill bridge — which is false and would have misdirected the target design. The corrected reading says the capability exists and the deployments do not use it, which is a *configuration and migration* problem rather than a *capability* one. |
| **Rule this reinforces** | **An absence probe must be paired with a replacement probe.** "The structure I know is not here" and "no structure is here" are different claims, and only the first is what a targeted search can support. |

## `ERR-P01-08` — an empirical zero presented without its denominator of activity

| Field | Content |
|---|---|
| **Original finding** | Stated during this continuation: *"14,441 stock movements, 3,680 carrying a computed value, and zero linked to a journal entry"* — offered as empirical confirmation that the receipt-side accounting effect never occurs. |
| **Why insufficient** | The same database has **16 journal entries in total**, one of which is a vendor bill. It is a database with a busy warehouse and an **essentially unused ledger**. In such a database a near-zero count of receipt entries is expected on *any* configuration, so the zero does not by itself discriminate between "the bridge is unconfigured" and "the ledger is not yet in use". Presented alone, it implies a busy accounting system silently failing. That implication is not supported. |
| **How found** | **By the author**, immediately, by counting journal entries by type before drawing the conclusion — the activity denominator that the zero required. |
| **New evidence** | `D1`: 16 journal entries (15 miscellaneous, 1 vendor bill) against 14,441 movements and 31 purchase orders. `D3` (v18) by contrast: 183,590 journal entries including 36,867 posted vendor bills. |
| **Corrected finding** | The **configuration** evidence carries the finding, because it is a cause and holds regardless of activity. The empirical zero is **corroborating but not independently decisive**, and is now published with that qualification attached. |
| **Rule this reinforces** | The programme's standing rule — *print the denominator next to every zero* — has a second clause: **a zero needs the denominator of relevant activity, not only the denominator of the search.** A search that found nothing and a system that did nothing are as indistinguishable as an empty haystack and a haystack with no needle. |

---

## `ERR-P01-09` — an entire deployed database was mislabelled by generation

| Field | Content |
|---|---|
| **Original finding** | Three readable databases were labelled two **v19** and one **v18**, and the v18 one was used throughout this session as the operating counter-example: *"the v18 bridge demonstrably operates — 57,863 valuation records carry a journal-entry link."* |
| **Original evidence** | Generation was inferred from **structural markers relative to v19**: the database has the valuation-layer table and the category input-account concept, and lacks the v19 stock-variation account. Every one of those observations is true. |
| **Why wrong** | Those markers distinguish *"not v19"* from *"v19"*. They do **not** distinguish v16 from v17 from v18. The inference silently assumed the estate contained only the two generations already under study, and read every non-v19 signal as v18. **The version was never actually asked for**, although the database records it explicitly. |
| **How found** | **By an independent expert**, which read the deployed module registry's version column. Verified immediately by this session: all four core module versions in that database read `16.0.x`. |
| **New evidence** | `D3` is **generation 16.0**. `D1` and `D2` are 19.0. **There is no readable deployed v18 database in this estate.** |
| **Corrected finding** | Every "deployed v18" statement in this session is a statement about a **v16** deployment. The v16 bridge operates on 6,530 of 13,214 receipts (49.4%). |
| **Architecture impact** | **Material.** The generation the v18 source analysis targets has **no deployed representative here**, so those source findings cannot be validated against any running system in this estate. That is a significant weakening of the evidence base and it was invisible while the label was wrong. It also means the "v18 → v19" comparison this package has drawn is really a **v16 → v19** comparison at the deployed layer, spanning three major versions, not one. |
| **Rule this establishes** | **Never infer a version; read it.** A version marker inferred from the presence or absence of features is a hypothesis about which versions exist, not a measurement. The registry states the version explicitly, and it cost one query. |

## `ERR-P01-10` — an absence read as misconfiguration when it was a deliberate design change

| Field | Content |
|---|---|
| **Original finding** | Stated earlier today, and already once corrected: v19 has a receipt-side valuation mechanism whose counter-account moved to the location, and the deployments simply have not configured it — described as *"internally contradictory: perpetual valuation declared, no posting destination"* and recorded as `CONTRA-P01-12`. |
| **Why wrong** | v19's perpetual option is labelled, in the product's own configuration, **"Perpetual (at invoicing)"** — verified in three places. And on a purchase document a storable perpetual product has its **bill line account set to the stock valuation account**. **v19 deliberately moved inventory recognition from the receipt to the bill.** No receipt entry is *expected*. The "contradiction" was between the reference product's design and my assumption about where valuation belongs — not inside the deployed configuration. |
| **How found** | **By an independent expert**, tasked to disprove the claim, which located the design intent in the selection label and the bill-line rule. Both verified directly by this session. |
| **New evidence** | Verified: the configuration label, and the bill-line account rule in the v19 stock-accounting module (path and line in the Layer 2 evidence base). |
| **Corrected finding** | `RECEIPT → BILL BRIDGE = VERSION-DEPENDENT`. The clearing bridge was **removed by design**; recognition moved to the bill. **Separately**, the v19 deployments configure no valuation account anywhere, so the invoice-time route does not fire either — meaning **no inventory value reaches the ledger by any route**. That larger finding is the expert's, not this session's. |
| **`CONTRA-P01-12` disposition** | **WITHDRAWN as stated and RESTATED.** The configuration is not self-contradictory; it is incomplete against a design this session had mis-modelled. |
| **Architecture impact** | Large, and in the more useful direction. The earlier reading would have told the programme that a v19 deployment had mis-set some fields. The corrected reading says the vendor's own model **abandoned goods-received clearing entirely** in favour of invoice-time recognition — which is a first-order input to the target design, and the opposite of a configuration note. |
| **Rule this reinforces** | The rule from `ERR-P01-07` — *an absence probe must be paired with a replacement probe* — was applied, and was still not enough. The replacement probe found the new **mechanism** and stopped there; it did not ask what the product says the mechanism is **for**. **Read the vendor's own labels and defaults: they state design intent that code structure alone does not.** |

## `ERR-P01-11` — a deployment-scoped claim carried by a population of two

| Field | Content |
|---|---|
| **Original finding** | The zero journal-entry link across 14,441 movements was offered as deployment-scoped evidence that receipts produce no accounting effect. |
| **Why wrong** | An independent expert established that `D1` has **zero** done movements from a supplier-usage location: all 1,201 order-linked receipts arrive from an **inter-company transit** location, and the third-party vendor-receipt population across both v19 databases is **2 movements**. A claim about vendor receipts cannot rest on a population of two. |
| **Corrected finding** | The configuration finding stands on its own terms and is class **A within the stated configuration scope**. The **behavioural** claim about vendor receipts in the v19 deployments is **class B**, and is labelled so. |
| **Architecture impact** | None on the configuration conclusion; it removes an unsupported behavioural inference. |
| **Rule this reinforces** | This is the third distinct instance in P01 of the same defect family — `ERR-P01-06` (an empty extraction), `ERR-P01-08` (a zero without its activity denominator), and now a zero whose **relevant sub-population** was two. **A denominator must be the denominator of the claim, not of the table.** |

---

## `ERR-P01-12` — a defect claim whose mechanism could not fire

| Field | Content |
|---|---|
| **Original finding** | `CONTRA-P01-09`: *"Thai withholding **compounds** across partial vendor payments"* — the offset term subtracts `debit − credit` over prior withholding lines, which on a vendor payment is negative, so the subtraction increases the amount withheld. Worked example published: 3,000 then 6,000 = 9,000 against a 3,000 liability. Recorded as FACT VERIFIED across two rounds, and re-derived by this session in round 2. |
| **Original evidence** | The offset line itself, read directly, plus the sign of a vendor-payment withholding line. **Both are correct.** |
| **Why wrong** | The **selection** was never checked. The payment-line link is `related` to the payment's journal entry, so **every** line of that entry carries it; the withholding-tax compute stamps the tax on every such line; the filter therefore returns the **whole balanced entry**, whose `debit − credit` is **0.00**. The offset is **inert** — it neither nets nor compounds. Confirmed in deployed data: exactly zero in **4,943 of 4,945** payments. |
| **How found** | **By an independent expert explicitly tasked to disprove the claim.** Verified immediately by this session against the core field definition and the custom compute. |
| **Corrected finding** | The real defect is **repeated full withholding**: the amount is the whole bill's withholding and is never prorated, so each partial payment withholds the full amount again. Two halves of a 100,000 bill at 3% yield **6,000**, not 9,000. The error is **linear**, not geometric. The single-full-payment control case is correct. |
| **Architecture impact** | The defect is real and serious in both readings, but the **mechanism, the magnitude and the fix are all different**. A remediation aimed at the sign would have changed an inert line and left the actual over-withholding untouched. |
| **What this demonstrates** | I re-derived this finding in an earlier round and called it verified — and re-derivation confirmed only the half I had already looked at. **Re-deriving a claim from the same evidence is not independent verification; it repeats the original reading's blind spot.** Only a party told to *break* it looked at the filter. |
| **Rule this establishes** | **For any claim of the form "this term has the wrong sign/value", first prove the term is non-zero.** A control that is inert is indistinguishable from a control that is wrong, unless you evaluate what it selects. |

## `ERR-P01-13` — a finding derived from code that runs nowhere observable

| Field | Content |
|---|---|
| **Original finding** | The withholding defect was presented against the custom v18-line copy in the declared path set, and its severity was amplified in this round by the observation that the module is *"installed in all three deployments"*. |
| **Why wrong** | Installed **by name** is not installed **as that code**. The v16 deployment runs withholding version `16.0.1.0.1`, which matches **no copy in the declared path set**, and that deployed wizard — read in full — **contains no offset loop at all**. The v19-line copy has **never executed**: 0 of 7 payments in the two v19 databases carry a withholding tax. |
| **How found** | **By an independent expert**, which compared the deployed module *version* against the path set rather than the module *name*. |
| **Corrected finding** | The arithmetic is a statement about source in the declared path set. **No readable deployment is demonstrably running it.** Any deployment claim is class **B**. |
| **Architecture impact** | Substantially reduces the *live* severity of the withholding findings while leaving the source defect intact as a design lesson. |
| **Rule this establishes** | **Matching a module by name across a source tree and a deployment is not evidence that the deployment runs that source.** Compare the version, and where it matches nothing in the path set, say so — the code that is actually running has not been found. |

## `ERR-P01-14` — the PND mapping conflict is real but neither mapping governs

| Field | Content |
|---|---|
| **Original finding** | `CONTRA-P01-10`: two shipped copies map a corporate counterparty to **opposite** certificate forms, so at least one deployment misclassifies every certificate. |
| **Refined by** | An independent expert: the conflict is confirmed and the **deployed owner is identifiable**, but **both mappings are contradicted by live data**. The v16 deployment shows corporate counterparties on **both** forms — 4,437 on one and 749 on the other — because the dominant creation route is a **wizard in which the operator picks the form**, bypassing the automatic mapping entirely. Neither mapping has demonstrably executed anywhere. |
| **Corrected finding** | The code-level contradiction stands. Its **practical** consequence does not follow, because the field is set by hand on the dominant path. The classification question is therefore **an operator-behaviour question, not only a code question** — and that makes it materially harder, not easier. |
| **Architecture impact** | A target design cannot fix this by choosing the correct mapping. It must decide **who** determines the form and prevent a free-text or free-choice override of a statutory classification. |
| **Statutory position** | Unchanged: **`HOLD — STATUTORY EVIDENCE REQUIRED`, routed to P07.** P01 does not decide which form is correct. |

---

## `ERR-P01-15` — the most relevant database was excluded by a tooling assumption

| Field | Content |
|---|---|
| **Original finding** | The fourth database dump was recorded — in round 2 and again throughout this round — as *"not readable by the available tooling"* and classified **C — not searched**. Every population and installed-status statement in this package was bounded to the other three. |
| **Original evidence** | `the database restore utility -l` failed on it. True, and correctly reported. |
| **Why wrong** | The failure was a **version mismatch, not an unreadable file**: the dump is a newer archive format than the restore binary that was invoked. **A newer binary was already installed on the same machine**, in a sibling directory to the one used. The scope statement said "the available tooling" and I never checked what was available. |
| **How found** | **By an independent expert**, which tried the newer binary. Verified immediately by this session: the database opens and is a generation-19 deployment with **453 installed modules**, nearly double any other in the estate. |
| **New evidence** | Adding it moves the installed population from **18 of 65 to 37 of 65**. **Nineteen members are installed only there.** |
| **Corrected findings** | Three published claims are **false**: three-way matching, the subcontracting family and the base requisition family are each *installed* — in the database that was excluded. The "47 source-only members" count becomes 28. |
| **Architecture impact** | **Large.** Three-way match and subcontracting were both explicitly required by the session directive, and both were reported as installed nowhere. `D4` is also, per the same expert, the only database with any period lock set — so it is the single most relevant database to P01's central questions, and it was the one left out. |
| **What makes this the worst of the round** | The other errors were wrong inferences from evidence I had. This one is an **entire evidence source I declared unavailable without testing what was available.** The scope statement was honest and the scope was wrong — which is exactly the failure mode the programme's negative-claim standard exists to prevent, appearing one level up: not a claim bounded too widely, but a **boundary drawn too narrowly and then trusted**. |
| **Rule this establishes** | **"Unavailable" is a claim and needs evidence like any other.** Before recording a source as unreachable, enumerate the tools actually present, not the one that failed. The programme already had this rule for *searches* — *an empty result means unsearched, never absent*. It now has it for **instruments**. |

---

# SUPPLEMENTAL ROUND `…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001` (2026-09-05)

## `ERR-P01-16` — "the most relevant database" was half a claim

| Field | Content |
|---|---|
| **Original finding** | On discovering the fourth archive was readable, this research called it *"the single most relevant database to P01"* and *"the most relevant database in the estate"*, on the grounds that it alone had three-way matching, subcontracting and the requisition family installed, and alone had a period lock set. |
| **Why wrong** | *Relevance* was measured on one axis — **module coverage** — and reported as if unqualified. On the other axis that matters to an accounting process, **transaction evidence**, the same database holds **10 journal entries in total** and **one company**. It is the most fully-*installed* deployment and among the least *exercised*. |
| **How found** | **By the author**, in this round, by counting journal entries per database before relying on the label — the activity denominator that the claim required and did not carry. |
| **Corrected finding** | `D4` is decisive for questions of *what is installed* and near-useless for questions of *what actually happens*. Both halves are now stated wherever it is cited. |
| **Architecture impact** | Prevents a reader expecting operational evidence from `D4` that it does not contain. It does **not** weaken the three falsifications it produced, which are install-scope facts. |
| **Rule this reinforces** | The programme's *print the denominator next to every zero* rule has a mirror: **print the axis next to every superlative.** "Most relevant" is not a measurement until the dimension is named. |

## `ERR-P01-17` — two archives were counted as two deployments

| Field | Content |
|---|---|
| **Original finding** | The estate was described throughout as **four databases**, and in places as *"two v19 deployments"* whose agreement corroborated a finding. A prior expert aggregated *"across 90 company rows"*. |
| **Why wrong** | Two of the archives are **the same deployment captured eleven days apart**. Their company sets are identical on both internal identifier and partner identifier — all 44 — with the same creation-date span. |
| **How found** | **By the author**, in this round, after noticing both reported exactly 44 companies with identical earliest and latest creation dates, and then comparing the identifier sets directly rather than trusting the coincidence. |
| **New evidence** | Identical 44-row `(id, partner_id)` sets. |
| **Corrected finding** | **Three distinct deployments in four archives.** Distinct companies across the estate: **46**, not 90. |
| **Architecture impact** | **Two-fold.** Any figure aggregated "across 90 company rows" double-counts 44 of them — including the deployed-control counts this package cites. And **agreement between those two archives is not independent corroboration**, which weakens every finding that leaned on "both v19 deployments show X". |
| **Rule this establishes** | **Two archives are not two witnesses until their identity sets are compared.** Snapshot pairs of one estate are the normal case in a backup folder, not the exception. |

## `ERR-P01-18` — a severity stated without its reachability

| Field | Content |
|---|---|
| **Original finding** | This round found that the vendor-advance *"Deduct down payments"* control is inert — declared, rendered in the interface, defaulted on, and referenced in executable code zero times. The first formulation stated the consequence flatly: the same cost is recognised twice. |
| **Why insufficient** | The inert deduction sits inside one branch of the wizard, selected by the bill-creation method. **In the series-19-line copy that method is commented out of the selection**, so the branch is not reachable through the interface there — while in the series-18-line copy it is the **default**. Stated without that, the finding over-claims on one copy and under-claims on the other. |
| **How found** | **By the author**, by applying to its own new finding the reachability discipline that an expert had earlier applied to P01's findings — *a defect that cannot be reached is not the same risk as one on the default path*. |
| **Corrected finding** | The control is inert in **both** copies (`FACT VERIFIED`). The double-recognition path is **interface-reachable and default in one copy, interface-unreachable in the other**, and which copy each deployment runs is still open. |
| **Architecture impact** | None on the defect; substantial on its ranking. It moves from a flat severity to a **deployment-dependent** one. |
| **Rule this reinforces** | **Every severity claim carries a reachability qualifier.** The programme learned this from external review two rounds ago; this is the first time it was applied by the author to the author's own finding at the moment of making it. |

## `ERR-P01-19` — the right conclusion from the wrong cause: a false zero on company-dependent values

| Field | Content |
|---|---|
| **Original finding** | Published in the prior round and repeated as the package's headline: *"no valuation account resolves anywhere in the series-19 estate — category valuation account **0 of 37**, category valuation journal **0 of 37**, location account 0 of 525, account-level variation 0 of 544 — therefore **no inventory value reaches the ledger by any route.**"* |
| **Original evidence** | A structured probe over the **per-record jsonb columns** of the item-category table. The counts are correct **for that storage location**. |
| **Why wrong** | In this framework a company-dependent value resolves in **two** places: the per-record value, **and a company-level default held in a separate defaults table**. The probe read only the first. The second holds **44 rows for the valuation account — one per company, 43 carrying a real account.** **The valuation account is configured.** The published zero was a false zero, and the cause I attributed the finding to does not exist. |
| **How found** | **By an independent expert**, which warned in general terms that one extraction method cannot cover both series because company-dependent values live in different places per series. Applying that warning to my own headline immediately falsified it. |
| **New evidence** | Valuation account: **44 default rows, 43 with a value**. Valuation **journal**: 44 default rows, **every value empty**. Company-level stock journal: **set on 0 of 44** in the 44-company estate, and **set on 1 of 1** in the other series-19 deployment. |
| **Corrected finding** | **The conclusion survives; the cause is entirely different.** The entry-creation routine takes its journal from the **company's stock journal**. In the 44-company estate that journal is unset on **44 of 44**, so a valuation entry cannot be created. **It is a missing journal, not a missing account.** And in the other series-19 deployment the journal **is** configured — so there the mechanism is complete and the absence of entries is a usage fact, not a configuration one. |
| **Architecture impact** | **Large, and it inverts the remediation.** A programme acting on the published finding would have configured category accounts — which are already configured — and the system would still post nothing. The single missing setting is the company stock journal. |
| **What this demonstrates** | The zero was real, the probe was correct, the boundary was declared — and the finding was still wrong, because **the probe measured one of the two places the value can live.** This is the same defect family as the excluded archive and the mislabelled series: not a reasoning error, an **evidence-location** error. Three rounds, three instances, three different surfaces. |
| **Rule this establishes** | **Before reading a configuration value, establish every place that value can be stored in that version.** A per-record probe on a company-dependent field is a partial read by construction, and its zero means *"not set here"*, never *"not set"*. |

## `ERR-P01-20` — a path filter narrowed the very enumeration that proved an absence

| Field | Content |
|---|---|
| **Original finding** | *"12 core trees on the volume — 4 at series 19, 8 at series 18, 0 at series 16."* Used to support the `VERIFIED ABSENCE` of any series-16 core source. |
| **Why wrong** | The search required the release file to sit beneath a directory named for the application. **One series-18 tree does not, and was dropped.** The true population is **13 — 4 at series 19, 9 at series 18.** |
| **How found** | An independent expert reported 13 where I had 12. **The discrepancy was chased rather than ignored**, and the expert was right. |
| **Corrected finding** | 13 core trees. **The series-16 conclusion is unchanged** — re-run without the filter, there are still zero trees at series 14 through 17. |
| **Architecture impact** | None. The conclusion survives. |
| **Why it is logged anyway** | Because it is the **fourth** appearance in P01 of the same defect — *a pattern narrowed a population and the author did not notice* — and this time it occurred **inside the enumeration whose whole purpose was to prove a boundary properly.** The claim was right by luck of margin, not by method: had the missing tree been the series-16 one, the class-A absence would have been false. |
| **Rule this reinforces** | **Run an absence enumeration twice, with a narrower and a wider pattern, and reconcile the difference before publishing.** A single pattern's count is not a population; two patterns agreeing is evidence, and two disagreeing is a finding. |

## `ERR-P01-21` — the cross-company trigger was attributed to the wrong process

| Field | Content |
|---|---|
| **Original finding** | Stated in round 2 and repeated in round 3: *"Approving a purchase order, **or posting a vendor bill**, whose counterparty resolves to another company creates a document in that other company."* The vendor-bill half was carried into the tolerance-zero finding and into the P11 handoff. |
| **Why wrong** | The routine filters for **sale documents**, and its inverse map turns a customer invoice into a **vendor bill in the target company**. **The trigger is a customer invoice, not a vendor bill.** Verified directly by this session in both generations. |
| **How found** | **By an independent expert**, which read the filter rather than the surrounding narrative. |
| **Corrected finding** | Two distinct paths. **Path 1:** purchase-order approval creates a sales order in another company — trigger is a **P01** object; that attribution stands. **Path 2:** a **customer invoice** creates a **vendor bill** in another company — the trigger is a **P02** object and the output is a P01 object. |
| **Architecture impact** | **Ownership moves.** P01 does not own the trigger of path 2 and should not have been carrying it as a P01 surface. The *output* remains P01's concern, and the tolerance-zero risk is unchanged in substance — but the process that must control the trigger is **P02**. |
| **Routing** | Path 2 routed to **P02**; both paths remain in P11's reconciliation. |
| **Rule this reinforces** | **Read the filter, not the function name.** The routine sits in a module whose name suggests both directions; only its predicate says which documents actually enter it. |

## `ERR-P01-22` — the estate census was keyed on the wrong unit, and enumerated with too narrow a pattern

| Field | Content |
|---|---|
| **Original finding** | `ERR-P01-17`, published hours earlier: *"Two of the four archives are **the same deployment** captured eleven days apart — identical 44-company identifier sets. **Three distinct deployments in four archives.** Distinct companies: **46**, not 90."* |
| **Original evidence** | Two probes: an enumeration of `*.dump` files in the download area, and a comparison of company `(id, partner_id)` sets between two archives. **Both were executed correctly and both returned what I said they returned.** |
| **Why wrong — two independent defects** | **(1) The identity unit was the file name and the company set, not the database's own identifier.** Keyed on the database uuid, the two archives I called one deployment are **two different databases** (`66d1b52a` and `1f6338ae`). **(2) The artefact enumeration matched one extension.** Database backups also ship as **zip containers** holding a dump and a manifest; those begin `PK`, not `PGDMP`, and my `*.dump` pattern could not see them. |
| **How found** | **By peer process P04**, unprompted, reporting that its *own* census had failed in exactly these two ways and suggesting P01 check its own. P04 stated explicitly that it had not looked at P01's package. **Verified independently by this session before acceptance.** |
| **New evidence** | Five distinct database identities by uuid: `66d1b52a` (44 companies, 251 modules, two artefacts the same day) · `1f6338ae` (44 companies, 232 modules) · **`f4a44cce`** (**1** company, **179** modules, dated **2026-03-30**) · `45a8e08e` (series 16) · `a1430edc` (453 modules, several copies across the volume). |
| **Corrected finding** | **Five distinct database identities, not three deployments.** Two artefacts named `iEVING` are **different databases**; two named `BK12MAY26` are **one**. A database exists from **2026-03-30**, four months earlier than my earliest archive, and it is a **single-company, 179-module** database — not a snapshot of the 44-company one. |
| **What survives** | The **conclusion** that the two 44-company archives are not independent witnesses **survives and is better supported**: identical company identifier sets with **different database uuids** means a **clone lineage** — one is a copy of the other, or both descend from a common template — so their agreement is **inherited, not independent**. Which is ancestor is **not established**. |
| **What does not survive** | *"Three distinct deployments"*, *"the same deployment observed twice"*, and the *"46 distinct companies"* arithmetic, which was computed from the wrong identity model. |
| **Architecture impact** | Moderate and bounded. No P01 accounting finding depended on the deployment **count**; the findings are bounded by *which* database each was measured in, and those bindings are unchanged. The **date range** of P01's evidence, however, starts **four months earlier** than the package states. |
| **Rule this establishes** | **Key an identity census on the artefact's own identifier, never on its file name or on a data resemblance.** Two databases can share every company row and still be two databases; two files can carry different names and be one. And **a content-based scan is only as complete as the set of signatures it enumerates** — one magic number is a pattern, not a population. |
| **Why this one is notable** | It is the **third** time in two rounds that a correctly-executed probe produced a false conclusion because it measured the wrong *thing* rather than measuring badly — after the tool-version exclusion and the storage-location false zero. **The reasoning was never the failure.** |

## `ERR-P01-23` — the round's governing finding was false: a series-18 deployment exists

| Field | Content |
|---|---|
| **Original finding** | The governing statement of this round, published in four documents: *"There is no readable deployed series-18 database in this estate"*, *"the generation P01 analysed in source has no deployed representative"*, and — as the structural conclusion of `P01_VERSION_SENSITIVE_FINDING_REGISTER.md` §4 — *"P01's source analysis and its deployment evidence do not overlap on any application series."* |
| **Original evidence** | An enumeration of database archives **in one download directory**, keyed and version-read correctly. Every per-archive reading was right. |
| **Why wrong** | **The population was scoped by directory, not by pattern.** Run across the home directory the pattern returns **19 archives and at least nine distinct database names**. Among them is a **series-18 deployment**: 361 of 361 installed modules at `18.0.x`, **4 companies, 15,522 journal entries, 47,801 stock valuation layers**, the custom purchase-request module installed, and **the goods-received clearing account configured on 15 item categories with a valuation journal on all four companies**. |
| **How found** | **By the independent challenge layer assigned to disprove the version identification** — the layer that had not returned when this round's package was first published, and returned afterwards. Its verdict was `BROKEN`. **Verified independently by this session before acceptance.** |
| **Corrected finding** | A deployed series-18 system exists, holds real accounting history, and **has the clearing bridge configured**. P01's source analysis and its deployment evidence **do overlap**, on series 18 and 19. |
| **A second, near-miss error inside the verification** | Reading that deployment's company-level defaults, the value column silently failed to resolve and every setting reported as empty — because that dump quotes the column name. Had it been published it would have been a **false zero on five settings**, and would have wrongly made this deployment look like the series-19 one. Caught before publication, and only because an expert had warned about that exact quoting behaviour. |
| **The distinction that matters** | Both this deployment and the series-19 estate show **zero** valuation layers linked to journal entries — **for opposite reasons.** In the series-19 estate the journal is **missing**. Here the journal is **configured** and the valuation policy is **periodic**, under which a receipt correctly posts no entry. **Two identical zeros, one a defect and one a policy.** |
| **Architecture impact** | **Large, and in the useful direction.** The central claim of four rounds — that the analysed generation could not be checked against any running system — is false. It can be, from data already on this host. This displaces "obtain runtime access" as P01's highest-value next action. |
| **Why this is the worst miss of the programme** | The database was **named in this session's own context from the first turn**: the project's standing notes record runtime evidence captured against that exact database. It was not hidden. **P01 read the name and never searched for the artefact.** |
| **Rule this establishes** | **Scope an evidence population by pattern, never by directory** — and **search for every artefact your own project notes already name.** A known name that is never resolved to an artefact is a louder gap than an unknown one. |

---

# ROUND 5 — SERIES-18 SOURCE ↔ DEPLOYMENT DIRECT VERIFICATION

## `ERR-P01-24` — correcting the finding did not correct the method: the census was still directory-scoped

| Field | Content |
|---|---|
| **Original finding** | `ERR-P01-22`, and the round-4 census it produced: **five distinct database identities across ten artefacts**, re-keyed on `database.uuid` after peer P04's report. Published as the corrected census. |
| **Original evidence** | A `database.uuid` read from each of ten artefacts. Every individual reading was correct. |
| **Why wrong** | The corrected census was **still scoped by directory**. `~/OCC_BACKUP` was not swept. `idemo18_uat` carries `database.uuid = 551ab874-9acb-11f1-b150-6ec7a480be3d`, which is **not among the five**. |
| **How found** | This run, while proving the identity of the very database `ERR-P01-23` had just added. Reading its uuid and checking it against the published list took one comparison. **It was available the moment `ERR-P01-23` was written and was not done.** |
| **Corrected finding** | The estate is **at least eight identities** — six known to P01, plus `4b766580` and `96548e18` reported by peer P04 (`P04-F-101`) — across **at least 39 artefacts** (P04's completed host census, §6A.27). **No total is stated by either package.** |
| **Architecture impact** | Bounded. No accounting finding depends on the count; every finding is bound to the database it was measured in. But **every universal quantifier in the P01 package** — "installed everywhere", "across the estate", "in every deployment" — is now suspect, and one has already been narrowed by counter-example (landed cost). |
| **Why this one matters most** | `ERR-P01-23` diagnosed the defect **exactly**: population scoped by directory rather than pattern. The next census repeated it. **Diagnosing a method defect and repairing it are different acts, and writing the diagnosis feels like the repair.** |
| **Rule this establishes** | **A method defect is closed by re-running the enumeration, not by describing it.** When a correction identifies a scoping error, immediately re-run *every* population that used the same scoping — not only the one that failed. |

## `ERR-P01-25` — the source path set does not contain the code the deployment runs

| Field | Content |
|---|---|
| **Original finding** | The declared source path set (`E00_P01_PRIMARY_EVIDENCE_BASE.md §1`) names `R4` — `.../Odoo18/EXTRA MODULE/smeplus-custom/addons` — as *"the project's own addon set"* for the v18 line, and excludes `97_OCC_PROJECT*` as **CLASS C — NOT YET SEARCHED**. |
| **Why wrong** | The deployment under study **is** the OCC deployment (`web.base.url = https://occ.smeplus.cloud`; archive `…_pre_scgl_occ_website_….dump`). Intersecting the 16 installed custom modules with the volume by pattern and comparing manifest versions: **6 of 16 have a version-matching copy, and none of the six is inside `R4`.** Five are one directory level above it; one is elsewhere. `scgl_account_coa_control` exists in exactly one place on the volume — **inside the excluded `97_OCC_PROJECT` root**. |
| **How found** | This run, by intersecting the **declared** set with the **deployed** set — a test the package had never run in either direction. |
| **What survives** | Every core-module citation. `R1` (v18 core) and `R3` (v19 core) are unaffected; the deployed core modules are stock series-18 core at `18.0.x`. |
| **What does not survive** | Any implicit assumption that P01's custom-module citations describe the code this deployment runs. **10 of 16 deployed custom modules have no version-matching source on this host at all**, 7 of them no copy by name whatsoever. |
| **A correction to the correction** | Peer P04 (`P04-F-97`, relaying P07) records that **two code bodies can share one version string**. So "6 of 16 matched" is an **upper bound** on availability, not a statement of code identity. The one module whose behaviour this package reads was therefore corroborated at **schema level** — 7 of 7 stored fields and the named relation table present in the deployed database, both compute fields correctly absent. |
| **Rule this establishes** | **Intersect the declared set with the deployed set, in both directions, before citing any source as the deployment's code.** And **a stated exclusion reason is a claim requiring authority, not authority** — `97_OCC_PROJECT` was excluded with a reason, and the reason ended the enquiry. |

## `NEAR-MISS-P01-05` — a false zero from assumed column names, caught by a row count in the same line of output

| Field | Content |
|---|---|
| **What happened** | `scgl_product_category_company_rel` was queried with assumed column names `product_category_id` / `res_company_id`. The aggregate returned a clean, well-formed **zero**. |
| **The truth** | The real columns are `category_id` / `company_id`. The table holds **32 rows covering 16 categories across 4 companies**. |
| **Would-be published claim** | *"No product category carries any company scope"* — instead of the true *"110 of 126 carry none"*. **Stronger, in the same direction, and wrong.** |
| **How caught** | The row count (`rows: 32`) was printed **beside** the aggregate. Zero-by-company against 32-rows-total is a visible contradiction. |
| **Rule this establishes** | **Never publish an aggregate without the row count of the set it aggregates over, in the same output.** A key-error zero and a real zero are indistinguishable in the aggregate alone. |

## `NEAR-MISS-P01-06` — a false **positive**: an alarming statistic in the wrong unit

| Field | Content |
|---|---|
| **The candidate finding** | **1,667 of 1,879** posted vendor bills have an accounting `date` different from their `invoice_date` — median **+13 days**, maximum **+30**, and **never negative**. Read as systematic late posting and a period-cutoff risk. |
| **The discriminating test** | Re-express at the unit the *claim* is about. **0 of 1,879** cross a month boundary; **1,747 of 1,879** carry an accounting date equal to the **last day of the month**; 124 more fall on day 25. |
| **The truth** | A month-end posting convention. Every bill is recognised in the month of its own invoice date. Orthodox, and not a finding. |
| **Withdrawn** | **Before publication.** |
| **Rule this establishes** | **A difference statistic must be computed in the unit its claim is about.** The claim was about accounting periods; the statistic was in days. Aggregate direction is not evidence of the thing the aggregate is used to argue. This is the false-**positive** counterpart of the false-zero class, and it deserves the same standing control. |

## `ERR-P01-26` — one writer published where six exist, and one of the six is not valuation-gated

| Field | Content |
|---|---|
| **Original finding** | `P01_S18_PERIODIC_PERPETUAL_POLICY_PROOF.md §7`, as first published: the receipt-side accounting gate is `_validate_accounting_entries` (`R1:stock_account/models/stock_valuation_layer.py:81`), *"Under `manual_periodic` the first `continue` fires for **every** layer … `account_move_id` is never written."* And §3 of the same document: *"0 of 47,801 … **Same for `account_move_line_id`**."* |
| **Original evidence** | The mechanism, read correctly and cited correctly. |
| **Why wrong** | **It was one mechanism generalised into a completeness claim.** There are **six** writers of `stock_valuation_layer.account_move_id` in the series-18 core tree. Five are valuation-gated and the published conclusion holds for them. The sixth — `R1:purchase_stock/models/account_move_line.py:298-313` `_prepare_pdiff_svl_vals` — writes **both** link columns and is gated on **`cost_method != 'standard'`** (`…/account_invoice.py:126`), not on `valuation`. Its journal-item half is valuation-gated (`…/account_move_line.py:248`); **its valuation-layer half is not.** |
| **And the precondition is met here** | `property_cost_method` sets `average` on **18 of 126** categories for company 1. 354 posted vendor-bill journal items fall in those categories; **18** carry a `purchase_line_id`; **16 of the 18 show a real price difference** — e.g. a bill unit price of 21,400.00 against a layer unit cost of 20,000.00. |
| **Why nothing was written anyway** | Every one of those 16 layers has `remaining_qty = 0.00`, which drives `qty_to_correct` to zero. **That is a condition periodic policy does not control.** |
| **How found** | AAS-03 Expert A, under the standing disproof assignment *"disprove that periodic policy explains the zero"*. **Verified independently before adoption.** |
| **Corrected finding** | The zero on `account_move_id` is **EXPECTED UNDER PERIODIC POLICY — VERIFIED, scoped to 43,227 of 47,801 rows**; for 4,574 rows (9.57%) it is **over-determined** by three valuation-independent causes (no stock move 2,866, zero value 1,205, non-storable product 1,089). **The zero on `account_move_line_id` is not explained by periodic policy at all.** Periodic is **sufficient but not identified**. |
| **What survives, and is strengthened** | The policy proof itself — every product in all four companies resolves to `manual_periodic` — held under four independent attacks, including one test the package had not run (module attribution across 225,529 `ir_model_data` rows, positive control 718 custom field xmlids, **zero** custom xmlids on `stock.valuation.layer`). And a **new** argument the package lacked: **0 of 86 stock locations carry a valuation account**, and 46,458 of 47,801 layers sit in fully-configured categories, so a `real_time` counterfactual would have **produced entries** rather than silent nulls. That is what rules out *"it would have been zero anyway"*. |
| **Residual, open** | An `ir_model_data` xmlid records field-, model-, view- and data-level extension. **A pure Python method override leaves no database trace.** 10 of 16 installed custom modules have no version-matching source on this host, so an override of `_validate_accounting_entries`, `_account_entry_move` or `AccountMove._post` in one of them is **unverifiable here**. Every negative in the policy proof is scoped accordingly. |
| **Rule this establishes** | **Enumerate every writer of a field before attributing its null to one gate.** A mechanism that explains an observation is not the same as the only mechanism that could have produced it — *sufficient* is not *identified*. |

## `ERR-P01-27` — the discriminating set did not discriminate: `create_date` was loader-supplied

| Field | Content |
|---|---|
| **Original finding** | *"**1,812 layers are native series-18 runtime output** (created 2026-08-25..2026-08-29, all with a stock move, 946 non-zero value). **DISCRIMINATING SET: of those 1,812 native layers, 0 carry an account_move_id.** So the zero is not an artefact of migration."* |
| **Original evidence** | `create_date` after `database.create_date`, plus a description-marker classifier. The query was correct; the field was not what it was taken to be. |
| **Why wrong — two independent defects** | **(1) `create_date` on this table is loader-supplied, not insertion time.** 44,947 of 47,801 rows carry a `create_date` **earlier than the database itself was created** (2026-08-18 06:09:12), while `write_date` has a minimum of **2026-08-25 12:19:13** and **zero** rows written before the database existed. **47,218 of the 47,801 rows were written on a single day.** There is no sub-population separable by insertion time. **(2) The set was not what it was called:** 1,254 of the 1,812 are `Product Quantity Updated` inventory adjustments authored by `__system__` inside the same load window as the migration. The denominator was overstated ~3.25×. |
| **How found** | AAS-03 Expert A. **Verified independently before adoption** — `write_date` minimum, the before-database counts and the daily histogram all reproduce exactly. |
| **Corrected finding** | The defensible runtime set is **558**, reached by two classifiers with different units that converge: a **human `create_uid`** gives 559; a **non-inventory-adjustment underlying move** gives 558; they overlap on 558, separated by one human-entered adjustment. The **over-determination-free core is 541** — additionally carrying a stock move, a non-zero value, a storable product and a fully-configured category. **0 of 558 and 0 of 541 carry a journal link.** |
| **What survives** | **The conclusion, on a smaller and better-bounded set.** The zero is still not a migration artefact. |
| **What does not survive** | The number 1,812, the phrase *"native series-18 runtime output"*, and any use of `create_date` as provenance on this table. |
| **And a narrower point that matters more for P01** | Only **61 of the 558** are purchase-linked. **2,085 of the 2,146 valuation layers on purchase-linked moves are migration rows.** The `1,403 receipts / ฿22,953,527.29` figure is arithmetically exact but is a statement about the **migrated ledger**; the runtime claim rests on **61 layers**, and the package now says so. |
| **A finding in its own right** | The layer table is not internally consistent with the product master in **either** direction: **1,480** done purchase receipts on storable products with quantity > 0 carry **no** layer, while **220** receipts on non-storable products **do**, and **1,089** layers across the table sit on non-storable products. The loader did not build layers move-by-move on valuation semantics. **This bounds every behavioural inference drawn across the full 47,801 — including the periodic one.** |
| **Rule this establishes** | **A timestamp column is data until proved otherwise.** Before using any date as provenance, test it against an event whose time is independently known — here, the database's own creation. And **a discriminating set must be built from two classifiers with different units**; convergence is the evidence that the set is real. |

## `ERR-P01-28` — the headline exposure summed two tax bases

| Field | Content |
|---|---|
| **Original finding** | *"**1,580 lines received-not-invoiced, gross pre-tax ฿30,080,689.78**"*, published in six documents and handed to P08 and P11. |
| **Original evidence** | `(qty_received − qty_invoiced) × price_unit`, over a correctly bounded population. Arithmetically exact — an independent recomputation reproduces `30,080,689.7776`. |
| **Why wrong** | **`price_unit` does not carry one tax basis across the population.** 312 of the 1,580 lines carry a purchase tax with `price_include_override = 'tax_included'` (`PV7% รวม VAT`), on which `price_unit` is **VAT-inclusive**. The ratio `(product_qty × price_unit) / price_subtotal` is **exactly 1.0700 on all 312** and **exactly 1.0000 on the other 1,267** — identified, not inferred. The label *"gross pre-tax"* was true of 1,267 lines and false of 312. |
| **How found** | AAS-03 Expert A. **Verified independently before adoption**; the ratio histogram and both totals reproduce to the digit. |
| **Corrected finding** | **฿29,029,467.66 tax-exclusive** (company 1 ฿14,692,566.42, company 2 ฿14,336,901.24). **Overstatement ฿1,051,222.12 — 3.49%.** Counter-figure: invoiced-not-received **฿1,734,752.87 → ฿1,663,518.07**. |
| **The label was wrong in both directions** | For a **GRNI accrual**, tax-exclusive is correct — recoverable input VAT is not accrued to inventory. For **cash exposure to vendors**, tax-inclusive would be correct, but then all 1,580 lines must be grossed up, giving ฿30,962,543.77. **The published figure was neither.** |
| **A second error, committed inside the correction** | The receipt-backed / operator-typed split was first written by **subtracting a mixed-basis sub-total from the tax-exclusive total**, giving ฿27,489,587.35. Recomputing each sub-population on its own basis gives **฿27,490,865.80** and **฿1,538,601.86**. Caught by recomputation before publication. **Derive each figure on its own basis; never subtract across bases.** |
| **What survives** | The **direction and the substance**: goods are received, no ledger recognition occurs between receipt and bill, and no accrual exists. Currency and discount risk are nil by enumeration — `currency_id` 133 and `currency_rate` 1.0 on all 13,887 orders, discount zero on every line. |
| **Rule this establishes** | **A monetary aggregate must declare its tax basis, and the declaration must be tested, not assumed.** A single column can carry two bases in one population, and the mixture is invisible in the total. |

## `ERR-P01-29` — a received-not-invoiced aggregate that included lines with no receipt

| Field | Content |
|---|---|
| **Original finding** | 1,580 lines presented as a single *received*-not-invoiced position. |
| **Why wrong** | **169 of the 1,580 lines have `qty_received_method = manual`, and all 169 are service products.** `qty_received` there is a number an operator typed: **no picking, no stock move, no valuation layer, and no possible GRNI entry.** A three-way match has only **two** legs on those lines. They are ฿1,538,601.86 tax-exclusive — **5.30%** of the figure. A further 8 non-storable consumable lines (฿85,807.25) can likewise never produce a valuation layer. |
| **Also concealed by the aggregate** | **18 lines are over-received** (`qty_received > product_qty`), carrying **฿1,669,526.29** tax-exclusive — **5.75%** of the exposure, and a distinct control condition. |
| **How found** | AAS-03 Expert A. **Verified independently**; the split reproduces exactly. |
| **Corrected finding** | Reported as three populations, not one: receipt-backed **1,411 lines / ฿27,490,865.80**; operator-typed service quantities **169 lines / ฿1,538,601.86**; and over-received **18 lines / ฿1,669,526.29** flagged separately. |
| **Rule this establishes** | **Before summing a quantity, test whether every row was produced by the same event.** `qty_received` is one column with two provenances — a goods receipt and a keystroke — and only one of them is a receipt. |

## `ERR-P01-30` — a file name was searched where a behaviour was claimed, and a published finding was false

| Field | Content |
|---|---|
| **Original finding** | *"**In series 18 that file does not exist.** `R1:stock_account/models/` contains 15 files … and **none is `account_move_line.py`**. **CLASSIFICATION: the bill-line account override is `VERSION-DEPENDENT` — a series-19 mechanism, `NOT REACHABLE` in series 18.**"* Published in four documents and counted as this run's one **contradicted** finding. |
| **Original evidence** | A directory listing. It was accurate: no file of that name exists in the series-18 `stock_account/models/`. |
| **Why wrong** | **The search unit was a file name; the claim unit was a behaviour.** The class is in `account_move.py`. `R1:stock_account/models/account_move.py:264-279` carries `AccountMoveLine._compute_account_id`, which redirects a purchase-document line to `accounts['stock_input']` when `_eligible_for_cogs()` and `company_id.anglo_saxon_accounting` hold, with `_eligible_for_cogs` returning `is_storable and valuation == 'real_time'`. |
| **How found** | **AAS-03 Expert C**, searching for the behaviour rather than the file. Verified here before adoption by reading the source. |
| **Corrected finding** | The mechanism **exists in series 18**. It is inert in this deployment because `valuation != 'real_time'`, **not** because it is absent. **CLASSIFICATION: CONFIGURATION-DEPENDENT — REACHABLE IN PRINCIPLE, NOT EXERCISED.** |
| **What survives** | The observation: no vendor bill line posts to a valuation or clearing account. 3,375 product lines, largest accounts `510000 Cost of Revenue` in each company. |
| **What does not survive** | *"v19 only"*, *"NOT REACHABLE"*, *"file absent in v18"*, and this run's count of **one contradicted finding** — which becomes **zero**. |
| **And the corrected reading is sharper than the wrong one** | The first version implied the deployment is structurally immune to bill-line redirection. **It is not.** In company 1 `anglo_saxon_accounting` is **already true**, and `accounts['stock_input']` **already resolves to account 176 on 126 of 126 categories**. Two of three conditions are met; the third is one field value. |
| **The real generation difference, which the wrong claim obscured** | v18 redirects to the **input/clearing** account via `_eligible_for_cogs()`; v19 splits the class into its own file and redirects to the **valuation** account via an explicit `valuation == 'real_time'` test. **The target account differs.** That is material, and it is not what was published. |
| **Rule this establishes** | **Make the unit of the search the unit of the claim.** A directory is not a population (`ERR-P01-23`); a file name is not a behaviour (this one); a day is not a period (`ERR-P01-28`); a name pattern is not a membership (`ERR-P01-32`). |

## `ERR-P01-31` — "no other trigger was found" was a stopped search published as a property of the world

| Field | Content |
|---|---|
| **Original finding** | *"Reachability of the account under current configuration: **LATENT.** Would become live if valuation policy were changed to `real_time`; **no other trigger was found**."* |
| **Original evidence** | An execution test over 40,353 journal items — correct, controlled, and answering a different question. **Zero observed rows is not zero possible writers.** |
| **Why wrong** | Reachability is a property of **writers**, not of rows. Enumerating writers instead returns **four routes**, none needing a code change. |
| **How found** | AAS-03 Expert C, under the assignment *"disprove that the clearing account is materially configured and reachable"*. Verified here before adoption. |
| **Route 1 — the policy switch has no guard in company 1** | `_check_valuation_accounts` (`R1:stock_account/models/product.py:963-971`) refuses `real_time` unless input, output and valuation accounts all resolve. In company 1 all three resolve on **126 of 126** categories, so **the guard cannot refuse**. And `ProductCategory.write()` → `_svl_replenish_stock_am` (`:809-830`) posts **credit `stock_input`** in the stock journal. **One field write on one company-1 category credits account 176 in journal 40** for that category's on-hand value; company 1 holds ฿29,835,023.51 of `remaining_value`. *Unmeasured clause, stated: whether any user holds write access to that field in company 1 has not been measured. Until it is, this is a capability, not a live exposure.* |
| **Route 2 — the accrual wizard** | `account/wizard/accrued_orders.py:44-52` domains the account to `liability_current`, which **contains 176**. Deployed: `ir_act_window` 433, bound to `purchase.order` (binding resolves through `ir_model_data`), **22 users** in `account.group_account_user`, **no default** for the account, and a non-empty input set (the 1,580 received-not-invoiced lines). |
| **Route 3 — the MRP WIP wizard defaults to it** | `mrp_account/wizard/mrp_wip_accounting.py:70-78` falls through company overhead account (NULL on all four) and `property_stock_account_production_cost_id` (false/absent) to **`property_stock_account_input_categ_id`** → **176**, with the journal defaulted to **40**. `mrp` and `mrp_account` installed; **5,549 production orders**. **This route never consults `property_valuation`.** Needs one manual field for the debit side. |
| **Route 4 — an armed cron** | `account_auto_transfer` installed, `ir_cron` 24 **active**, `account_transfer_model` **exists with zero rows**. One configuration record from being a live unattended writer against any account. |
| **Routes 5–6** | `account.automatic.entry.wizard` "Change Account" (`ir.actions.server` 251) retargets journal items to **any** account; and xmlid-keyed import — `base_import` and `account_base_import` installed, with **181,540** `occ_mig` external IDs already present, **10,190 of them `account.move`**. |
| **Corrected finding** | **The account is not unreachable.** It is unused, on four live paths. |
| **What survives** | The execution test itself: 0 items on 176/62/100/138 and 0 in journals 16/24/32/40, now confirmed by three independent methods plus a synthetic injection control. |
| **Rule this establishes** | **A reachability claim must enumerate writers, not observed rows.** And *"no other trigger was found"* is a statement about a search; publishing it as a statement about the system is the negative-claim error in its purest form. |

## `ERR-P01-32` — the custom-module population was a name pattern, and the core path set was incomplete

| Field | Content |
|---|---|
| **Original finding** | *"**16 installed custom modules.**"* Used as the denominator for every custom-module claim in this run, including the scoping of the policy proof's negatives. |
| **Why wrong — two defects** | **(1) The population was selected by NAME** (`scgl_*` plus `purchase_request`), not by membership. Intersecting the 361 installed modules against the declared source roots: **66 are absent from `R1`, and 55 are absent from `R1 ∪ R2`.** **39 installed non-core modules were never enumerated.** **(2) `R1` is not the deployed core.** Eleven installed modules — `fleet`, `account_fleet`, `hr_fleet`, `documents_fleet`, `snailmail`, `construction`, `journal_entries_report` among them — live in `R2` (`addons_archive`, 962 directories). `R2` is in the declared path set but five rounds of P01 core citations were made against `R1` alone. |
| **How found** | AAS-03 Expert C, under *"find another population-selection defect"*. Verified here before adoption: 798 / 962 directory counts, 66 / 55 / 16 module counts all reproduce. |
| **What the 39 include** | **the entire Thai withholding-tax stack** (four OCA/Ecosoft modules — see `ERR-P01-33`); **`om_data_remove` 18.0.1.0.0, installed**, which peer **P06** records as deleting ledger data without authorisation — **live in this deployment too**, flagged to P06 and P11 rather than re-derived here; plus `account_payment_multi_deduction`, `hr_expense_petty_cash`, `full_summarize_bills`, `bi_print_journal_entries`, `journal_entries_report`, `print_voucher_request` and others that touch accounting objects. |
| **Architecture impact** | **High.** Every negative source claim in this package is scoped by the unread set, and the correct size of that set is **55**, not 16. `ERR-P01-30` is a direct consequence of the second defect: an absence proved against `R1` alone. |
| **A fifth surface no module census can reach** | `web_studio` 18.0.1.0 is installed with 341 xmlids, and `res_company` carries Studio fields `x_scgl_wip_control_enabled` (true on companies 3 and 4) and `x_scgl_project_wip_account_id` (accounts 705 / 706). **Studio customisations are data, not modules.** Inert today — companies 3 and 4 hold zero entries — and **not swept by this package at any pattern width.** |
| **Rule this establishes** | **Enumerate a deployed population by membership, never by a name pattern.** A name pattern encodes a guess about how things are called; membership is a measurement. And **declare which roots constitute the deployed core, then prove it** — a root can be in the path set and still never be searched. |

## `ERR-P01-33` — the withholding mechanism was attributed to the wrong module

| Field | Content |
|---|---|
| **Original finding** | *"This deployment uses `l10n_th 18.0.2.0` with `account_withholding_tax`, `withholding_tax_cert*`, `account_payment.wt_tax_id`"* — handed to **P07** in that form. |
| **Why wrong** | **`l10n_th` contains no withholding-tax code at all.** Across the 798 modules of `R1`, `withholding.tax.cert` and `account.withholding.tax` return **zero** hits. `l10n_th` is 17 files — chart of accounts, EMV QR, report layouts, bank and partner extensions. The inference ran from *"a Thai localisation module is installed and WHT tables exist"* to *"the localisation module supplies WHT"*. **Co-presence is not attribution.** |
| **How found** | AAS-03 Expert C, resolving model ownership from `ir_model_data` rather than from module names. Verified here before adoption. |
| **Corrected finding** | The mechanism belongs to **four OCA/Ecosoft modules**: `l10n_th_withholding_tax` 18.0.1.4, `l10n_th_withholding_tax_cert` 18.0.1.3, `l10n_th_withholding_tax_cert_form` 18.0.1.0.2, `l10n_th_withholding_tax_report` 18.0.1.0.1. `l10n_th_withholding_tax_multi` is **uninstalled**, so **one withholding rate per payment**. |
| **And they are readable** | **All four have version-matching source inside the declared path set `R4`.** P01 could not see them because its custom-module population was the name pattern of `ERR-P01-32`. The mechanism is not opaque; it was never looked for. |
| **What this changes for P07** | P01 handed P07 an opaque-localisation framing. The truth is a **known OCA stack with readable, version-matched source** — a materially easier statutory question. The corrected handoff is `P01_S18_WHT_DEPLOYMENT_REALITY.md`. |
| **Rule this establishes** | **Resolve model ownership from the deployment's own metadata, never from module names.** `ir_model_data` on `ir.model` says which module owns a model; a module's name says only what someone called it. |

## `ERR-P01-34` — the sentence describing the test was the negation of the test that was run

| Field | Content |
|---|---|
| **Original finding** | The discriminating test that **withdrew** a candidate cutoff finding, stated as: *"**all 1,879 are in the same month**"*, alongside *"1,747 of 1,879 carry an accounting date equal to the LAST DAY of the month"*. |
| **Original evidence** | **Every number was exact.** 1,879 posted bills · 1,667 with `date != invoice_date` · median +13 · max +30 · never negative · 1,747 on month-end · 124 on day 25 — all reproduce to the digit. |
| **Why wrong** | The **sentence** is false. The 1,879 bills span **eight** accounting months (2026-01 through 2026-08, between 132 and 377 bills each). Nothing in the data says they are "all in the same month". |
| **What the test should have said** | Whether **each bill's accounting date sits in the same month as its own `invoice_date`** — which is **1,879 of 1,879**, with **0** crossing a period boundary. |
| **How found** | AAS-03 Expert B, re-deriving every zero by field position. Both readings verified here directly. |
| **Why this one is dangerous out of proportion to its size** | It is the **load-bearing half of the only test justifying a withdrawal**. A reader auditing the withdrawal against the data would have found its stated basis contradicted and would have been **entitled to reinstate a finding this package had correctly dropped**. A wrong sentence around right numbers is harder to catch than a wrong number, because the numbers all check out. |
| **Corrected finding** | The withdrawal **stands**, on the same-month-as-its-own-invoice-date test: 1,879 of 1,879, plus 1,747 of 1,879 on month-end. Month-end posting convention, not a cutoff violation. |
| **Rule this establishes** | **Audit the prose against the query, not only the numbers against the data.** Where a sentence states what a test measured, re-read it beside the code that produced the figure. A package whose arithmetic is exact can still publish a claim that says the opposite of what it ran. |

## `ERR-P01-35` — "4 of 4 companies" counted two that have never transacted

| Field | Content |
|---|---|
| **Original finding** | *"Every product in all four companies resolves to `manual_periodic`. **126/126, 4/4**."* — and the same `4/4` framing on the clearing-account and anglo-saxon readings. |
| **Why wrong** | The figures are right; the **denominator invites a false reading**. Companies 3 and 4 hold **zero** journal entries, **zero** valuation layers, **zero** stock moves and **zero** purchase orders; company 3 has 5 users and **company 4 has none at all**; company 3 owns one product template and company 4 owns none. They are configured shells. Counting them as two of four confirmations doubles the apparent weight of the evidence. |
| **How found** | AAS-03 Expert B. Verified here. |
| **Corrected finding** | *126 of 126 categories; **measured** in the two transacting companies, **configured identically** in two that have never transacted.* |
| **And the correction is worth more than the fix** | Companies 3 and 4 are the **never-transacted negative control this evidence base already contained and was not using.** A policy that yields zero GL linkage in two live companies **and** zero rows in two dormant ones is exactly the spread that belongs beside the zero. |
| **Rule this establishes** | **State which members of a population were measured and which were merely configured.** A never-transacted member is not a confirmation — it is a control, and it is more useful as one. |

## `ERR-P01-36` — this package adopted an expert claim that the expert then withdrew

| Field | Content |
|---|---|
| **What happened** | `P01_S18_DEPLOYMENT_IDENTITY_PROOF.md §4.2` was rewritten mid-run to rest on the **schema** rather than on `latest_version`, adopting AAS-03 Expert B's discriminator table — which offered `account_move.origin_payment_id` and `product_template.lot_valuated` as **series-18** markers. |
| **Why wrong** | **Both exist in series 19 as well.** Verified here directly: `R3:account/models/account_move.py:206` carries `origin_payment_id`. They discriminate against series ≤ 17; they do **not** discriminate against 19. |
| **How found** | **By the expert itself.** It sent its own version attributions for verification against the source trees rather than asserting them from memory, and withdrew two on the result. This package had already adopted the pre-withdrawal version. |
| **Corrected finding** | The decisive series-19 exclusion is a **direct string comparison**, not an attribution: `ir_model_fields_selection` for `product.category.property_valuation` holds **`manual_periodic`**, and `R3:stock_account/models/product.py:666-670` shows series 19 renamed that key to **`periodic`**. **A series-19 database cannot physically contain the string `manual_periodic`** — and this deployment contains it on the very field the valuation-policy proof turns on. Corroborated by the absence of `res_groups_privilege` from all 1,122 tables, with a ten-table positive control. |
| **Rule this establishes** | **Verify a reviewer's disproofs against source before adopting them.** Independent review is the discovery engine of this programme and it commits its own bounded errors; adopting a correction unverified imports them. Here the expert caught itself first — the correction is recorded anyway, because the package had already published the withdrawn version and would not otherwise show it. |

## `ERR-P01-37` — "full-volume" named a storage device, and the absence it proved was false

| Field | Content |
|---|---|
| **Original finding** | *"**16 copies** found … **No copy at `18.0.1.10.0`.** The deployed purchase-request module has **no matching source on this host**. **CLASSIFICATION: VERIFIED ABSENCE (class A) within the stated population.**"* Published this run, with its population, pattern and unit all declared. |
| **Original evidence** | `find /Volumes/iMacSys -type d -name "purchase_request"` plus a manifest-version read. Every step executed correctly. |
| **Why wrong** | **The path set was `/Volumes/iMacSys` and the claim said "this host".** The module is at **`/Users/admin/Downloads/OCC_PR_MULTI_APPROVE_UAT_PASS_36/purchase_request`**, `"version": "18.0.1.10.0"` — verified here by reading the manifest — and again inside the sibling `.zip`. A second unit failure compounds it: `find -type d` cannot see a module shipped **inside an archive**, and at the ZIP-member unit there are 87 further hits. |
| **How found** | AAS-03 Expert D, under *"find another population-selection defect"*. |
| **Corrected finding** | Version-matching source exists for **11 of 16** name-matched custom modules, not 6. **Three** have no copy anywhere, not seven — `scgl_delivery_cost`, `scgl_signature`, `scgl_signature_hr_expense` — with a negative control (`scgl_signature`'s 6 name matches are all a different module's file) and a positive control (`scgl_uom_archive` → 1). `purchase_request` has **53** copies, **2** at the deployed version. |
| **What this changes** | A gap this package recorded as an **external dependency** — *"closable only by obtaining the module from the deployment owner"* — is a **file on this machine**. |
| **Why it is the sharpest instance of the class** | It was written **in the same run, in the same document, as a section correcting exactly this error in someone else's work.** The phrase *"full-volume"* reads as exhaustive; it names a **storage device**, not a boundary over the artefacts. `ERR-P01-23` was a directory standing in for a population; `ERR-P01-25` a declared root that excluded the deployment's own code; this is a volume standing in for a host. **Three instances, one package, two of them found by someone else.** |
| **Rule this establishes** | **A path set is a set, and it must be written as one.** "Full-volume", "the host", "everywhere" are descriptions; `$HOME` + `/Volumes/*` + the cloud-document mounts, minus a named exclusion, is a boundary. And **enumerate at two units** — a module is a directory *and* an archive member. |

## `ERR-P01-38` — the artefact census is bound by format and by path set; ten artefacts are invisible to it

| Field | Content |
|---|---|
| **Original finding** | The estate census, corrected twice already (`ERR-P01-22`, `ERR-P01-24`), and published this run as *"at least six identities"*, then raised to eight on peer P04's completed sweep. |
| **Why still wrong** | Enumerated by **content classification across a corrected path set**, the host holds **27 artefacts**, not 17 — and **8 distinct `database.uuid` values are directly readable from the PGDMP artefacts alone**, across **at least 10 database names**. |
| **What is invisible** | **The largest database artefact on this host** — a **283 MB `dump.sql`** inside `BK12MAY26_2026-08-03_11-28-04.zip`, an Odoo **19.0+e** database with a 251-module manifest, whose `.dump` sibling *taken 5h40m earlier the same day* **was** enumerated. **An entire database, `pankhamhom`** — two artefacts, **series 18**, a **478-module** manifest — in iCloud Drive. Plus `T805efaplus` (series 18) and two `iMSCG` snapshots (series 16). |
| **The instructive part** | **The extension test and the content test agreed exactly — 17 = 17 — inside the old path set.** Zero false positives, zero false negatives. A reviewer re-running only that test at a second width would have concluded the census was sound. **Width agreement on one rung is not evidence about another rung.** |
| **And the exclusion reason again exceeded its authority** | `~/Library` is pruned for a real reason — a macOS permission-prompt storm across ~855 application-data directories. That reason governs **application data**. It has no authority over `~/Library/Mobile Documents` (iCloud Drive) or `~/Library/CloudStorage` (Google Drive), which are **user document stores** mounted under `Library` by Apple and Google. Both were swept with no prompt storm. |
| **One thing it newly supports** | `web.base.url = https://occ.smeplus.cloud` is the basis for identifying this as the OCC deployment, and Odoo **rewrites that key on login unless frozen**. It is frozen: `web.base.url.freeze = True`. The identification holds — but it had been asserted from a **mutable** key without checking. |
| **Rule this establishes** | **Enumerate artefacts by content, across a declared path set that includes cloud-document mounts** — and re-run every inherited census against the corrected set rather than adopting its count. |

## `ERR-P01-39` — a labelled source tree accepted without content proof, in a table that said this had not happened

| Field | Content |
|---|---|
| **Original finding** | `P01_POPULATION_SELECTION_METHOD_AUDIT.md §5`, published this run: *"**M4** — version accepted from a label: **Not found in this run.**"* |
| **Why wrong** | It was there, in this package's own foundations. `R1` is cited throughout five rounds as *"the v18 core"*. **Manifest versions cannot discriminate**: v18 core ships `'version': '1.3'` for `account` and the series is prefixed at install, so `R1`'s `1.3` matches the deployment's `18.0.1.3` — **as do at least eleven other trees on this host**. |
| **Content does discriminate** | **6 distinct contents of `stock_account/models/account_move.py` exist across the 15 series-18 `stock_account` trees on this host.** Two concrete hazards: `/Volumes/iMacSys/CLAUDE AI/MIGRATION/ODOO18/enterprise/addons/stock_account` is **labelled ODOO18 and is v19 content** (it carries `account_move_line.py` and `product_value.py`); and two different trees both named `odoo-18.0.post20260605` carry `account/__manifest__.py` at **1.4** and **1.3**. **A build string does not identify code.** |
| **What survives, and why the citations still stand** | The predicate the valuation proof turns on is **build-invariant**: of the 15 series-18 trees, **14 carry a byte-identical `_eligible_for_cogs` body** and the fifteenth has no `account_move.py` at all. The generation split is clean in both directions — **15 of 15 series-18 trees lack `account_move_line.py`; 8 of 8 series-19 trees carry it**, no counterexample. The conclusions do not depend on which tree was read; **the method that selected it was still unsound.** |
| **Coverage, stated as coverage** | 44 of the 72 `stock_account` directories on this host could not be series-resolved — almost all `.Encrypted` Google-Drive mirrors whose files are non-materialised cloud stubs. |
| **Rule this establishes** | **Identify a source tree by content, not by its label, its path or its manifest version** — and **never record a failure mode as "not found" without running the test that would find it.** Writing "not found in this run" in an audit table is a claim, and this one was false. |

## `ERR-P01-40` — two installed modules bound what every count in this package can mean

| Field | Content |
|---|---|
| **What was missing** | The package counted 47,801 valuation layers, 3,158 purchase-linked stock moves and a single global `ir_default` row for `property_valuation`, and treated each as the state of the system. **Two installed modules bound what those counts can support**, and neither was named. |
| **`om_data_remove` 18.0.1.0.0 — installed** | The only source copy located is version **19.0.1.1**, so its content is **not evidence about the deployed module**. That copy deletes by raw SQL (`sql = "delete from %s" % t_name`), names **`stock.valuation.layer`** among its targets, and separately deletes from **`ir_default`** — the exact table the valuation-policy proof reads. Peer **P06** records this module deleting ledger data without authorisation in another deployment. |
| **Why this disproves nothing, and bounds everything** | A raw `DELETE` leaves **no trace**, so the absence of evidence of a purge is expected under both hypotheses. **The claims are unchanged in substance and are now correctly framed**: 47,801 layers and one `ir_default` row are the **post-hoc state of tables a resident, installed module can silently empty.** |
| **`purchase_request` 18.0.1.10.0 — installed** | Overrides `stock.move._prepare_merge_moves_distinct_fields`, `_merge_moves_fields`, `_prepare_merge_move_sort_method` and `stock.picking._action_done`. Every move count here is taken over a table whose **merge semantics an installed module changes**. The figures are what the data says; **their reading as a one-to-one receipt population is not established.** |
| **How found** | AAS-03 Expert D. |
| **Rule this establishes** | **Before reading a table as the state of a system, enumerate the installed modules that can rewrite or erase it.** A count is a count of what remains, and saying so is not a hedge — it is the claim. |

## `ERR-P01-41` — the series-16 core was never absent; the search was

| Field | Content |
|---|---|
| **Original finding** | Published across **six** documents: *"the series-16 **core** is a `VERIFIED ABSENCE` — 13 core trees on the volume, 9 at series 18, 4 at series 19, **0 at series 14–17**"*, and in its strongest form *"the only series-16 artifact of any kind is the custom addon directory"*. It carried a remediation: *"requires a series-16 core tree **obtained from outside**"*. |
| **Original evidence** | An enumeration of `odoo/release.py` across `/Volumes/iMacSys`, correctly executed, correctly counted, and already corrected once (`ERR-P01-20`, 12 → 13 after a path filter was removed). |
| **Why wrong** | **The path set was the volume; the claim said *anywhere*.** Estate-wide there are **31 core trees across five series** — 14.0 ×1, **16.0 ×3**, 17.0 ×2, 18.0 ×15, 19.0 ×10 — and **19 of the 31 are under `/Users/admin`**, including **every series-14, -16 and -17 tree**. The volume count was right. The word attached to it was not. |
| **How found** | The **late-returning version-identity challenge layer**, reporting it **against its own work as well as P01's** — its manifest population covered volume *and* home while its core enumeration covered the volume only, and it attached the "anywhere" claim to the narrower one. **Verified here independently before adoption**, by four probe forms. |
| **Verified by reading, not listing** | `odoo-16.0+e.20230401`: `version_info = (16, 0, 0, FINAL, 0, '')`, **955 addons**, `account/models/account_move.py` **4,200 lines**, `stock_account/models/product.py` **873 lines**, `purchase/models/purchase.py` **1,447 lines**, `purchase_stock` and `l10n_th` both present. |
| **Corrected finding** | The series-16 core is **present and readable**. *"The series-16 core remains unread"* is **literally true and materially misleading** — a **search** gap, not a **source** gap. **P01's source and deployment evidence overlap on series 16, 18 and 19**, not only 18 and 19. The remediation changes from *obtain a tree from outside* to **read the one that is here**. |
| **One inference upgraded to FACT VERIFIED** | The series-16 `adapt_version` (`odoo/modules/module.py:488-492`) is an **unconditional prefix with no part-count guard and no validating regex**, so a manifest declaring `14.0.1.0.0` on a series-16 engine is stored as **`16.0.14.0.1.0.0`** — exactly what the series-16 deployment holds for `l10n_th_withholding_tax_cert`, and a string neither the 18.0 nor the 19.0 code could emit. **The certificate module in the only deployment with real accounting history is a series-14 body on a series-16 engine.** Previously inferred from 18/19; now read in the series-16 core itself. |
| **Architecture impact** | Bounded but real. No accounting finding is withdrawn — none rested on the series-16 core being absent. What changes is a **published negative about the evidence base**, a **remediation that pointed outside the estate**, and the overlap statement in the version-sensitive register. |
| **Why this one lands hardest** | It is `ERR-P01-37` again — `/Volumes` standing in for the host — **in a second population, found hours later, against a different author.** The programme has now established twice, independently, that **in this estate `/Users/admin` holds evidence `/Volumes/iMacSys` does not.** |
| **And a third instance, committed inside the verification** | My own first check was `find /Users/admin -maxdepth 6 -type d -name "odoo-16.0*"` → **empty**. The trees sit **ten or more levels deep** in Google Drive. **Had I stopped at one probe form I would have contradicted a correct report and left a falsehood standing in six documents.** Three further forms all returned it. **A bounded probe returning empty is not a negative result; it is an unfinished measurement.** |
| **A near-miss the challenger caught in itself** | Its first probe for the series-16 purchase model asked for **`purchase_order.py`** and returned ABSENT. In series 16 the file is **`purchase.py`** — confirmed here (1,447 lines; `purchase_order.py` genuinely does not exist there). Stopping at the first form would have published a **Class-A absence built on one guessed filename** — the shape of `ERR-P01-30`. |
| **Rule this establishes** | **Run a negative at two probe *forms* as well as two widths**, and treat the first empty return as unfinished. A filename, a depth bound and a storage device are each a guess about where a thing lives; none of them is a population. |

---

# ROUND 6 — SERIES-16 SAME-GENERATION DIRECT VERIFICATION

## `ERR-P01-42` — a discriminating test joined on a column that does not exist in the generation under study

| Field | Content |
|---|---|
| **Original finding** | The first run of this round's central test returned: *"`manual_periodic` UNLINKED 17,119 · `manual_periodic` linked 57,863 · **unlinked DESPITE real_time: 0**"* — i.e. every one of the 74,982 valuation layers classified as periodic, and the 15 `real_time` categories appeared to hold no layers at all. |
| **Original evidence** | A join from `stock_valuation_layer.categ_id` to the `ir_property` policy rows. The query executed, returned rows, and its totals reconciled to the table. |
| **Why wrong** | **`stock_valuation_layer` has no `categ_id` column in series 16.** The table has 19 columns and that is not one of them; it belongs to a later generation. The COPY parser pads absent columns with `None`, so `r.get('categ_id')` was `None` for all 74,982 rows and every row fell to the `else` branch — periodic. |
| **Why the control did not catch it** | A **57,863-row positive control sat directly beside the result** and was satisfied: rows were parsed, the join ran, the totals added up. The failure was not in whether rows were read but in **whether the predicate could see its input**. A well-formed, plausible, internally consistent answer. |
| **How found** | The result was *too* clean — zero layers in fifteen categories that between them hold the deployment's real-time inventory. Checking the actual COPY header took one command. |
| **Corrected finding** | Joined `product_id` → `product_product.product_tmpl_id` → `product_template.categ_id`, **with an explicit coverage control: 0 of 74,982 unresolvable.** Result: real_time 56,654 linked / 1,044 not; manual_periodic 1,209 linked / 16,075 not. |
| **Architecture impact** | None on any published finding — the defect was caught inside the round. But the corrected result is the round's central claim, and it would have been **exactly inverted**: "the policy has no effect" instead of "the policy explains 98.2% and 93.0%". |
| **Rule this establishes** | **Schema shape is generation-specific, and a parser that pads missing columns will let you join on a column that is not there.** Before any cross-generation query: read the COPY header of the table in *this* generation and assert every join key exists. Carrying a column set forward from the generation you last worked in is the same class as carrying a storage location forward (`ERR-P01-19`). |

## `ERR-P01-43` — a correction to `ERR-P01-41` that was itself made from the wrong directory

| Field | Content |
|---|---|
| **Original finding** | Ranking the three series-16 core trees, I counted `odoo/addons` and got **955 / 31 / 32**, and was about to record that only one was a complete core and that `ERR-P01-41`'s count of three overstated the estate. |
| **Why wrong** | Two of the three use the **standard split layout**: `odoo/addons/` holds only `base` and the `test_*` modules, and the business modules live in **`<root>/addons/`** — **461** and **464** of them, including `purchase`, `stock_account` and `l10n_th`. |
| **How found** | Checked the second addons location before publishing, specifically because this is the defect class the package has been repeatedly caught by. |
| **Corrected finding** | **All three are complete series-16 cores. `ERR-P01-41`'s count of 3 stands.** |
| **Why it matters** | `ERR-P01-41` was itself a correction *about reading the wrong location*, and its follow-up was nearly published from reading the wrong location. **A correction is not immune to the defect it corrects.** |
| **Rule this establishes** | When a project's layout admits two conventional locations for the same content, **enumerate both before counting** — and treat a count that would revise a recent correction as requiring more evidence, not less. |

## `ERR-P01-44` — a version predicate that ignored the framework's own default

| Field | Content |
|---|---|
| **Original finding** | The first source-tree ranking reported 23 version "mismatches" in the best tree, e.g. `account_asset` deployed at `16.0.1.0` against a source manifest with no version at all. |
| **Why wrong** | Odoo core manifests routinely omit `version`. `odoo/modules/module.py:56` sets `'version': '1.0'` in the manifest defaults and `:393` applies `adapt_version`, so an omitted version resolves to **`16.0.1.0`** — a match, not a mismatch. My predicate treated absent as unmatched. |
| **How found** | The "mismatches" were implausibly concentrated in core modules. The rule was then **read from the source** rather than assumed. |
| **Corrected finding** | **144 of 144 present modules version-match in the ranked tree; zero mismatches in any of the three trees.** |
| **Rule this establishes** | **Read the framework's own defaulting rule before comparing against a stored value.** A comparison against a field the framework fills in for you is a comparison against your assumption about it. |

## `NEAR-MISS-P01-07` — a normaliser that assumed the answer it was testing for

| Field | Content |
|---|---|
| **What happened** | To resolve deployed modules against the whole-host index, version strings were normalised by prefixing `16.0.` when absent. Pointed at the host-wide index this prefixes **every** tree's versions, so a **series-18** tree's `stock_landed_costs 1.1` normalised to `16.0.1.1` and **false-matched the series-16 deployment**. The instrument reported "48 exact-version copies" whose top hits were odoo-18 and odoo-19 trees. |
| **How caught** | The reported paths were read rather than counted. `~/Downloads/odoo-18.0.post…` is not a series-16 source. |
| **Consequence avoided** | A source-availability claim built on cross-generation false matches. |
| **Rule adopted** | **Exact-version matching across a multi-generation index is valid only where the containing tree's series is separately confirmed.** Normalise using the tree's own series, never the series you are looking for. Core citations in this round therefore come only from the tree whose `release.py` was read. |

## `NEAR-MISS-P01-08` — "quadrillions posted to the general ledger", checked before publishing

| Field | Content |
|---|---|
| **The candidate** | 30 valuation layers carry values to **±1.5 × 10²¹ THB** with per-unit costs of **744,082,316,162.43** for milled rice, and **25 of them carry POSTED journal entries**. The obvious headline wrote itself. |
| **The check** | Read the 50 journal items on those 25 entries. **They balance exactly: debits = credits = ฿31,622,699.37**, with net effects by account in the millions. |
| **The truth** | The **general ledger is intact**. The divergence is between the **inventory subledger and the ledger** — ~15 orders of magnitude on 30 rows — which is a serious reconciliation break and a different claim from the one nearly published. |
| **Rule this reinforces** | **A finding and its consequence clause are two claims.** "Absurd values exist in the subledger" was evidenced; "absurd values were posted to the GL" was assumed from the presence of a link, and was false. Measure the consequence, never inherit it from the finding. |
