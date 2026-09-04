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
