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
