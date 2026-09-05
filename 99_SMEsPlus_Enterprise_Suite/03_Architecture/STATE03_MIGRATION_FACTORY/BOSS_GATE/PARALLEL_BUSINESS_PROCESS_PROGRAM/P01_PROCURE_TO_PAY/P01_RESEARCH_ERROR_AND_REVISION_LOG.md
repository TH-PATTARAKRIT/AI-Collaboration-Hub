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
| **Original evidence** | `pg_restore -l` failed on it. True, and correctly reported. |
| **Why wrong** | The failure was a **version mismatch, not an unreadable file**: the dump is a newer archive format than the restore binary that was invoked. **A newer binary was already installed on the same machine**, in a sibling directory to the one used. The scope statement said "the available tooling" and I never checked what was available. |
| **How found** | **By an independent expert**, which tried the newer binary. Verified immediately by this session: the database opens and is a generation-19 deployment with **453 installed modules**, nearly double any other in the estate. |
| **New evidence** | Adding it moves the installed population from **18 of 65 to 37 of 65**. **Nineteen members are installed only there.** |
| **Corrected findings** | Three published claims are **false**: three-way matching, the subcontracting family and the base requisition family are each *installed* — in the database that was excluded. The "47 source-only members" count becomes 28. |
| **Architecture impact** | **Large.** Three-way match and subcontracting were both explicitly required by the session directive, and both were reported as installed nowhere. `D4` is also, per the same expert, the only database with any period lock set — so it is the single most relevant database to P01's central questions, and it was the one left out. |
| **What makes this the worst of the round** | The other errors were wrong inferences from evidence I had. This one is an **entire evidence source I declared unavailable without testing what was available.** The scope statement was honest and the scope was wrong — which is exactly the failure mode the programme's negative-claim standard exists to prevent, appearing one level up: not a claim bounded too widely, but a **boundary drawn too narrowly and then trusted**. |
| **Rule this establishes** | **"Unavailable" is a claim and needs evidence like any other.** Before recording a source as unreachable, enumerate the tools actually present, not the one that failed. The programme already had this rule for *searches* — *an empty result means unsearched, never absent*. It now has it for **instruments**. |
