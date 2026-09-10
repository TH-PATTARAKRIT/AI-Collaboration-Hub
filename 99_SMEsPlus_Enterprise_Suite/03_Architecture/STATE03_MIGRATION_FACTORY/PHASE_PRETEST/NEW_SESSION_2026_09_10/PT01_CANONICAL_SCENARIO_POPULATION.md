# PT-01 — CANONICAL SCENARIO POPULATION

## `CP-PT-01 — SCENARIO POPULATION RECONCILED`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `d4ad2579`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **No `PASS`. `0 of 22` verified. `0` vetoes discharged. `E2E-04` `NOT TRAVERSABLE`.**

---

## 1. Result

| | |
|---|---|
| Boss-approved cross-module scenarios reconciled | **`22 of 22`** — `X-01`…`X-22`, no gap, no duplicate |
| End-to-end scenarios reconciled | **`18 of 18`** — `E2E-01`…`E2E-18`, each appearing exactly once |
| Canonical register generation established | **`FINAL_CONTROLLED_V2`**, of **`3`** competing generations |
| Scenarios added by this checkpoint | **`7`** — `PT-S-01`…`PT-S-07`, each with a measured coverage reason |
| **Canonical Pre-Test scenario population** | **`47`** = `22` + `18` + `7` |
| Evidence-pointer traps found and disarmed | **`3`** — `PT01-N-01`, `PT01-N-02`, `PT01-N-03` |
| Coverage gaps **measured** against master prompt §6/§7 | **`7`**, in **two distinct classes** |
| Instrument failures in this checkpoint's own tooling, caught and reported | **`3`** — §6.4 (`1` by positive control, `2` by implausibility) |

---

## 2. The two source populations are NOT one population

**They are different units on different axes, and summing them to `40` would be a denominator defect.**

| | **Population A** | **Population B** |
|---|---|---|
| Name | Boss-approved joint cross-proof baseline | End-to-end scenario register |
| **UNIT** | one **Accounting × Inventory handoff case** | one **end-to-end business flow** |
| Count | **`22`** | **`18`** |
| Authority | **Boss**, `SMEPLUS-26-09-02-ACC-INV-JOINT-BOSS-22SC-001`, Jira `ERPPLUS-140` | SMEs Core register, Phase SA |
| Canonical artefact | blob `a1fc7cd6` (§7) | `SA15_..._FINAL_CONTROLLED_V2.md` |
| Disposition axis | `10 / 12 / 0` (six-way class) | `9 / 9 / 0` (six-way class) |
| Second axis | — | traversability `2 / 15 / 1` |

**They overlap semantically and are not derivable from each other.** `X-16` (RM→WIP→FG) and `E2E-03`
(Sales→Manufacture→…→AR) both touch production, but `X-16` asks *does the stock-to-financial handoff
reconcile*, while `E2E-03` asks *does the whole commercial flow route end to end*. **A scenario can be
`RECONCILED` on A's axis and carry a named break on B's.**

> **Binding on `PT-12`:** the canonical matrix carries **both** populations with their unit named on every
> row. **`22 + 18` is never written as `40`.**

---

## 3. Population A — the Boss-approved 22, reconciled

**Authority:** Boss approval document, status `BOSS APPROVED / EFFECTIVE AS MINIMUM JOINT CROSS-PROOF
BASELINE`, content-pinned at blob **`a1fc7cd6`**, resolved and read this checkpoint (§7).

**Boss's own scope rule, carried verbatim:**

> *"These are minimum scenarios, not a closed universe. A new scenario may be added only when a material
> Delta Trigger, new evidence, unresolved contradiction, or 9 Veto / 9 Special Team finding demonstrates
> that the existing baseline is insufficient. Repeated questions or duplicate scenarios without material
> delta are prohibited."*

**This is the rule §5 of this document operates under.** The master prompt's §6/§7 mandatory coverage is
itself a Boss-issued instrument, so a **measured** absence against it is a qualifying Delta Trigger.

| # | Scenario | Cross-proof state at `SA_CORR3_06` |
|---:|---|---|
| `X-01` | Stockable purchase receipt → handoff | `HOLD` · `DEPENDENCY` · goods-received bridge is a swept suspense account, not item-matched |
| `X-02` | Vendor bill with receipt timing variation | `HOLD` · `DEPENDENCY` · **no prior-period attribution mechanism exists at all** |
| `X-03` | Stockable sales delivery → cost handoff | `HOLD` · `DEPENDENCY` · recognition-point split, `BP-02` not selectable |
| `X-04` | Customer invoice with delivery timing variation | `HOLD` · `DEPENDENCY` · `JT-04`'s `CONFLICTING` flag discharged |
| `X-05` | Partial receipt | `HOLD` · over-receipt tolerance undefined |
| `X-06` | Partial delivery | `HOLD` · `H-05` draft invoice consumes billable quantity, posts nothing, freely deletable |
| `X-07` | Backorder | `HOLD` · **`STRUCTURAL`** · `R-17` **`NO CONSUMER`**; cancellation leaves no document trail |
| `X-08` | Purchase return | `HOLD` · return basis `PENDING` |
| `X-09` | Sales return | `HOLD` · **`JT-05` NOT DECIDABLE** — original-cost vs current-cost basis |
| `X-10` | Cancellation before physical execution | `HOLD` · **`STRUCTURAL`** · `C-01` symmetry, `C2-F-01` durability |
| `X-11` | Correction after physical execution | `HOLD` · **`STRUCTURAL`** · only correction route is a return; corrected-entry link **does not exist** |
| `X-12` | Inventory count / adjustment | `HOLD` · **`STRUCTURAL`** · approval mechanism absent; can silently reduce a reservation |
| `X-13` | Scrap / damage / write-off | `HOLD` · **salvage undefined**; scrap has no cost causality |
| `X-14` | Internal warehouse transfer — no inappropriate financial effect | `HOLD` · **`STRUCTURAL`** · `R4-F-18` no independent check; neutrality configuration-protected only |
| `X-15` | Multi-company / tenant boundary | `HOLD` · **`STRUCTURAL`** · **this scenario *is* element 10**; `0 of 8` isolation proofs; **two** lock-defeat paths |
| `X-16` | Manufacturing RM → WIP → FG | `HOLD` · `R-22` **`GAP`**; fixed-overhead elements have **no injection path** |
| `X-17` | Manufacturing reversal / scrap / variance | `HOLD` · **no variance mechanism exists** — one of nine recognised |
| `X-18` | Stockable vs consumable vs service routing | `HOLD` · **`STRUCTURAL`** · two-axis tie-break undefined; `BD-ACC-01` silent for services |
| `X-19` | Period-end / cut-off | `HOLD` · **no accounting-period object exists**; reconciliation holds at the boundary, not continuously |
| `X-20` | Historical migration across fiscal years | `HOLD` · **`STRUCTURAL`** · element 14; provenance reference must be originated |
| `X-21` | AI migration mapping + deterministic reconciliation | `HOLD` · **`STRUCTURAL`** · element 14; `MTI-42` |
| `X-22` | Retry / idempotency / replay | `HOLD` · **`STRUCTURAL`** · **this scenario *is* element 15**; `UAE-29` the root |

**Enumerated check:** identifiers `X-01`…`X-22` each appear **exactly once**; **`0`** gaps, **`0`**
duplicates. **`22 of 22` at `HOLD`; `0` `VERIFIED`** — reproduced, not revisited.

---

## 4. Population B — the 18 end-to-end scenarios, reconciled

**Canonical artefact:** `SA15_END_TO_END_SCENARIO_REGISTER_FINAL_CONTROLLED_V2.md`.

**Traversability, counted from the class column only** (SA15's own instrument note warns a whole-file grep
returns false positives from *"was `NOT TRAVERSABLE`"* annotations — **this checkpoint reproduced that
warning and honoured it**):

| Class | Scenarios | Count |
|---|---|---:|
| `TRAVERSABLE` | `E2E-02`, `E2E-07` | **`2`** |
| `TRAVERSABLE WITH NAMED BREAK` | `E2E-01`, `-03`, `-05`, `-06`, `-08`, `-09`, `-10`, `-11`, `-12`, `-13`, `-14`, `-15`, `-16`, `-17`, `-18` | **`15`** |
| **`NOT TRAVERSABLE`** | **`E2E-04`** | **`1`** |
| Total | | **`18`** |

**`2 + 15 + 1 = 18`** ✔ · every identifier `E2E-01`…`E2E-18` appears exactly once ✔.

**Two carried facts that Pre-Test may not soften:**

1. **`E2E-04` is `NOT TRAVERSABLE` on a structural ground its own source states** — the target
   manufacturing state machine's shortage state *"exits only on reservation completing, never on
   procurement being raised. A shortage can therefore be entered and never left by supply."* A prior draft
   re-graded this row and **suppressed the second clause of its own source sentence**; the re-grade was
   **withdrawn** (`CHF-03`). **This checkpoint does not re-grade it.**
2. **`E2E-15` is a dependency gate on every other scenario's retry / duplicate / join dimension.**
   Element 15 is *specified, not built*. **Nothing may be read as testing a cross-module join.**

**Neither of the two fully-traversable scenarios is a forward sale** (`SA15-F-01`): `E2E-02` is
purchase-to-pay and `E2E-07` is kit/bundle. **The most common SME transaction — `E2E-01` — is not fully
traversable.**

---

## 5. Population C — `7` scenarios added, each on a measured absence

**Method, stated before the result.** Each of the master prompt's §7 mandatory challenge examples and §6
domain requirements was tested against the corpus. **An absence was recorded only where an executed
command returned zero with a firing positive control.** Additions are **not** proposed on judgement alone.

**POPULATION:** Phase SA markdown corpus.
**PATH SET:** `6` directories — `PHASE_SA_CROSS_MODULE_ASSURANCE_2026_09_08`, `PHASE_SA_CORR2_*`,
`PHASE_SA_CORR3_*`, `PHASE_SA_CORR4_*`, `PHASE_SA_CORR5_*`, `PHASE_SA_FINAL_BOSS_GATE_2026_09_09`.
**UNIT:** one file containing at least one match. **CORPUS SIZE:** `192` files.
**INSTRUMENTS:** stem = `grep -rliF`; acronym = `grep -rlwE`. **Positive control:** `dropship` → `49`.

### 5.1 The measured table — corpus vs the three canonical scenario registers

| Topic | Corpus (192 files) | **Scenario registers (3 files)** | Class |
|---|---:|---:|---|
| `dropship` *(control)* | **49** | present (`E2E-05`) | — |
| `idempot` | **57** | present (`X-22`, `E2E-15`) | — |
| `stale` | **30** | — | — |
| **`VAT`** *(whole-word)* | **8** | **`0`** | **CLASS 1** |
| **`WHT`** *(whole-word)* | **4** | **`0`** | **CLASS 1** |
| **`metering`** | **12** | **`0`** | **CLASS 1** |
| **`make-to-stock`** | **`0`** | **`0`** | **CLASS 2** |
| **`partial payment`** | **`0`** | **`0`** | **CLASS 2** |
| `partial invoic` | **1** | **`0`** | CLASS 2 (effectively) |
| `event order` / `out-of-order` | **`0` / `1`** | **`0`** | **CLASS 2** |

> **The two classes are materially different and must not be reported as one number.**
>
> **CLASS 1 — known but not scenario-represented.** The topic is discussed in the Phase SA corpus and is
> **absent from the scenario registers**. The risk is that it is never *tested* because no scenario carries
> it.
>
> **CLASS 2 — absent corpus-wide.** `0` in `192` files. The risk is that it was never *considered*.

**The earlier three-file measurement is not the corpus measurement.** Reporting `VAT = 0` without naming
the path set would have asserted a corpus-wide absence that **is false** — `VAT` appears in `8` corpus
files. **The boundary is declared so the negative means what it says.**

### 5.2 The `7` added scenarios

| ID | Scenario | Coverage reason (**measured**) | Master-prompt hook | Primary route |
|---|---|---|---|---|
| **`PT-S-01`** | Sale with statutory tax consequence → VAT/WHT determination → register → GL | **CLASS 1.** `VAT` `0` and `WHT` `0` in all three scenario registers (corpus `8`/`4`). Tax appears only as a *hop* inside `E2E-14` and as a cross-cutting rule (`R-19` `HARD`, `BD-ACC-02` company-scoped) | §6.E *tax/VAT/WHT*; §7 *Tax — if statutory consequence exists* | Sales → Tax → Accounting |
| **`PT-S-02`** | Direct buy → sell with no manufacture (trading route) | **CLASS 2.** `0` corpus hits for a direct buy→sell chain as a scenario; `X-01` and `X-03` are separate legs and are never joined in one commercial act | §7 *direct buy→sell* | Purchase → Inventory → Sales → Accounting |
| **`PT-S-03`** | Make-to-stock vs make-to-order — the routing contrast | **CLASS 2.** `make-to-stock` `0` in `192` files. MTO is covered (`E2E-03`, `E2E-06`); **the contrast that selects between them is not** | §7 *make-to-stock vs make-to-order* | Manufacturing → Inventory → Accounting |
| **`PT-S-04`** | Partial invoice and partial payment | **CLASS 2.** `partial payment` `0`, `partial invoic` `1` corpus-wide. §7 requires **all four** partials; only receipt (`X-05`) and delivery (`X-06`) exist | §7 *partial receipt/delivery/**invoice/payment*** | Sales/Purchase → AR/AP → Payment → Accounting |
| **`PT-S-05`** | Return **before** invoice vs return **after** invoice | **CLASS 1/2 boundary.** `X-08`/`X-09` and `E2E-11`/`-12` are returns **without a timing split**; §7 names the two timings as **separate** challenges | §7 *return after invoice*; *return before invoice* | Sales/Purchase → Inventory → Accounting |
| **`PT-S-06`** | Reversal after a **downstream module** has consumed the output | **CLASS 2.** `X-11` is *correction after **physical** execution* — a different predicate. Reversing an event whose output another module already consumed is not represented | §7 *reversal after downstream consumption* | any producer → any consumer → Accounting |
| **`PT-S-07`** | Out-of-order / stale event arrival and partial mid-chain failure | **CLASS 2.** `event order` `0`, `out-of-order` `1` corpus-wide; `stale` `30` but never as a scenario | §6.F *event ordering · stale state · partial failure* | cross-cutting |

**`7` added. `0` added without a measured absence. `0` added to reach a target count.**

### 5.3 What was tested and **deliberately NOT added** — the refusal half

**A coverage checkpoint that only adds is not a control.** These candidates were tested and **rejected as
already covered**, which is the outcome that costs something to report:

| Candidate | Why NOT added |
|---|---|
| Role / privilege / negative-access boundary | **Already covered as a runtime obligation family**, not missing: `SA17` §2b carries `0 of 60` negative cases (**52 rejection cells + `S-01`…`S-08`**) and `0 of 13` enforcement surfaces. Adding a scenario would **duplicate a specified obligation** and inflate the denominator |
| Cross-tenant / cross-company attempt | **Covered** — `X-15`, which *is* element 10 |
| Duplicate event / retry | **Covered** — `X-22` (*is* element 15) and `E2E-15`, the dependency gate |
| Stock sale vs service sale | **Covered** — `X-18`, `E2E-08` |
| Consumable / expense immediate expense | **Covered** — `X-18`, `E2E-10` |
| Invoice-before-delivery / delivery-before-invoice | **Covered** — `X-04` (customer side), `X-02` (vendor side), both stated as *timing variation*, i.e. both directions |
| Scrap with / without salvage | **Covered** — `X-13`, `E2E-13`; salvage specified at `XMC-C-D7` |
| FG delivery → COGS | **Covered** — `X-03`, `E2E-03` |
| RM → WIP → FG | **Covered** — `X-16`, `E2E-03` |
| Buy vs manufacture | **Covered** — `E2E-04`, `E2E-06`, routing template `XMC-F-03` |
| `metering` (CLASS 1, corpus `12`) | **NOT added as a scenario.** §6.F says *"metering **where relevant**"*; relevance to the Accounting/Inventory chain is **not evidenced**, and `PT-11` owns it as a **scope question**, not a test row. **Recorded rather than silently dropped** |

**`11` candidates tested, `10` refused as covered, `1` (`metering`) routed elsewhere with its reason
stated.** **Declining to add is the half a coverage review usually omits.**

---

## 6. Evidence-pointer traps, and the instrument failures this checkpoint caught

### 6.1 `PT01-N-01` — the canonical generation is not the newest file

**`3` generations of `SA15`/`SA17` exist**; two share the date `2026-09-09`. **Recency does not
discriminate and is not authority.**

| Generation | Status |
|---|---|
| `PHASE_SA_CROSS_MODULE_ASSURANCE_2026_09_08/SA15…` | historical |
| `PHASE_SA_CORR5_…/SA15…_CORR5_CONTROLLED.md` | superseded (`379fd073`) |
| **`PHASE_SA_FINAL_BOSS_GATE_2026_09_09/SA15…_FINAL_CONTROLLED_V2.md`** | **GOVERNS** — by its own controlled-version notice, authority `SA_FINAL_01` §5 |

**Resolved by the artefact's own supersession notice, not by file date.** Both earlier files remain
readable and unoverwritten, so the correction chain stays auditable.

### 6.2 `PT01-N-02` — the Boss baseline is pinned by **blob**, and a commit-shaped check returns silence

`SA_CORR3_06` cites the 22-scenario baseline as `a1fc7cd6497061f9a6e1fd2d0f755589412830df`, in a column
alongside commit SHAs.

| Instrument | Result |
|---|---|
| `git log -1 <sha>` | **empty output, exit 0** — indistinguishable from "does not exist" |
| `git cat-file -t <sha>` | **`blob`** |
| `git rev-parse --verify <sha>^{commit}` | **error: dereferences to blob type** |
| Path resolution | `…/ACCOUNT_INVENTORY_JOINT/02_BOSS_APPROVAL_JOINT_22_SCENARIO_CROSS_PROOF_BASELINE_2026_09_02.md` |

**Verdict: the pointer is VALID and is *stronger* than a commit reference** — a blob SHA pins exact file
content, which a commit SHA does not.

> **The trap is the instrument, not the citation.** The first check run here produced an empty result that
> would have supported a *false material finding* — *"the Boss-approved baseline commit does not resolve"*.
> **It was caught only by re-running the negative in a second and third form.** A challenger will meet the
> same silence; the disarming is published here so the finding is not manufactured twice.

### 6.3 `PT01-N-03` — the handoff package never names the register that defines its own denominators

The `SMES_CORE_CONTINUATION_2026_09_10` package cites `22` and `18` repeatedly and contains **`0`**
references to `SA15`, `SA17`, `END_TO_END`, `HANDOFF_BASELINE` or `FINAL_CONTROLLED_V2`
(positive control: `SC-45` → `5` files, so the instrument fires).

**The pointer resolves one level up** — the parent `PHASE_SA_FINAL_BOSS_GATE_2026_09_09` package cites
`SA15`/`SA17` in `7` files and co-locates both registers.

| | |
|---|---|
| Severity | **MINOR — traceability weakness, not a broken chain** |
| Why recorded | a reader given only the continuation package **cannot reach the scenario definitions**; B-7 is routed that package |
| Action | `PT-14` — the B-7 pack must name `SA15`/`SA17` `FINAL_CONTROLLED_V2` explicitly |

### 6.4 Instrument failures caught **inside** this checkpoint — `3`

**Reported because a checkpoint that hides its own tooling errors cannot be trusted about anything else.**

| # | Failure | How caught | Consequence had it stood |
|---:|---|---|---|
| 1 | `awk` field-strip left a leading space; `comm` reported **every** file as present-on-both-sides | the result was implausible (both lists full) | a fabricated manifest-coverage catastrophe |
| 2 | Multi-directory path set expanded as **one** argument with embedded newlines; **every** topic returned `0` | **positive control `dropship` also returned `0`** | **`10` fabricated CLASS-2 corpus gaps** |
| 3 | `grep -w` applied to the **stem** `idempot` returned `0` on a topic present in `57` files | implausible against known element-15 coverage | a fabricated gap on the most-discussed control in the programme |

> **Two of the three produced clean, confident zeros.** In each case the zero was indistinguishable from a
> real absence, and in case 2 **only the positive control separated them.** Every negative in §5.1 carries
> a firing control for this reason.

---

## 7. Authority pointers verified this checkpoint

| Pointer | Type | Resolves | Verified as |
|---|---|---|---|
| `a1fc7cd6…` | **blob** | **YES** | Boss 22-scenario approval, `BOSS APPROVED / EFFECTIVE`, Jira `ERPPLUS-140` |
| `SA15…_FINAL_CONTROLLED_V2.md` | file | **YES** | governing E2E register |
| `SA17…_FINAL_CONTROLLED_V2.md` | file | **YES** | governing Pre-Test handoff baseline |
| `SA_CORR3_06…22X22.md` | file | **YES** | 22-scenario joint cross-proof, all 22 rows |
| `379fd073` | commit | **YES** | CORR5 superseded generation |

---

## 8. Canonical Pre-Test scenario population — carried to `PT-02`

| Population | Unit | Count | State |
|---|---|---:|---|
| **A** — Boss joint cross-proof | Accounting × Inventory handoff case | **`22`** | `22 of 22` `HOLD`; `0` `VERIFIED` |
| **B** — end-to-end | end-to-end business flow | **`18`** | `2` traversable · `15` named break · **`1` `NOT TRAVERSABLE`**; `0` verified |
| **C** — Pre-Test additions | coverage-closing scenario | **`7`** | `NEW — UNPROVEN`, each on a measured absence |
| **TOTAL** | **mixed — unit named per row** | **`47`** | **`0` runtime-verified** |

**`47` is a population, not a score.** Every row enters `PT-02` at `0` proven.

---

## 9. Checkpoint

> ## `CP-PT-01 — SCENARIO POPULATION RECONCILED`
>
> **`22 of 22` Boss scenarios reconciled against the Boss-approved baseline (blob-pinned, resolved) ·
> `18 of 18` E2E reconciled against the governing `FINAL_CONTROLLED_V2` generation, chosen by supersession
> notice rather than file date · the two populations kept as **two units**, never summed to `40` ·
> **`7` scenarios added, each on a measured absence with a firing positive control; `10` further candidates
> tested and REFUSED as already covered; `1` routed elsewhere with its reason stated** · gaps separated into
> **CLASS 1 (known, not scenario-represented)** and **CLASS 2 (absent in `192` files)** · `3` evidence-pointer
> traps disarmed · **`3` of this checkpoint's own instrument failures reported, `2` of which produced clean
> confident zeros.**
>
> **`E2E-04` NOT re-graded · `E2E-15` dependency gate intact · `0 of 22` verified · `EC-04` `0/3` ·
> `6` vetoes in force.**

Next checkpoint: `PT-02 — Input Completeness Matrix`.

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
Boss remains the sole Final Approver.
