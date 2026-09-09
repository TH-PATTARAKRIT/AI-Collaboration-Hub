# SA_CORR3_13 — TVDR-06 PRICE AND CREDIT DETERMINATION — PROOF

`PHASE SA · CORR3 · TARGETED VERY DEEP RESEARCH — EXECUTED, NOT CARRIED`
Finding prefix `TV6-`. Frame: `CORR3-FRAME` (declared in the shared execution brief; not re-declared here).
Authority boundary: this artefact designs and proves. It does not approve, merge, release, or open the
Pre-Test Matrix. Boss remains sole Final Approver.

---


> **Orchestrator intake note.** Same-model executor; `INTERNAL ADVERSARIAL SELF-CHALLENGE`; **not adopted
> on its word.** This artefact **executes** an item CORR2 answered *"Can research close it? **Yes**"* and
> then did not run — discharging the second of the three actions CORR2's own resume state named as
> highest-value.
>
> **Cross-corroboration worth recording.** `TV6-F-01` finds the inherited zeros are **vocabulary
> artefacts**, and `TV6-K-01` measures that **removing vendor field names from a published pattern as a
> clean-room scrub moved the control figure.** A **second, independent executor** working on an unrelated
> subject (`SA_CORR3_14`, the Quality object) reached the **same root cause by a different route**: a
> clean-room scrub silently converted a positive into a negative, and the pattern's blind spot and the
> object's evidence base were the same set. **Two instruments, two subjects, one defect class — this is
> the strongest form of corroboration available inside a single round, and it is still not independence.**


## 1. What this item is, and why it existed

`SA16` scoped `TVDR-06` on the strength of a count — *"pricing 18 blobs, credit control 16 blobs"* — and
set the closing question: **what is the core price and credit determination that extensions extend, and
what may an extension not change?** (blob `1e51af9d` §2, lines 78–88).

`SA02` converted that count into an input status: *"Price determination inputs … `INPUT-EVIDENCE-INSUFFICIENT`
… SA-D21 thin (18 blobs). What determines price is not evidenced"* (blob `5bfa85ee` line 34), while
recording the customer credit limit as *`INPUT-COMPLETE` **as a negative*** — *"advisory only, never a gate"*
(same blob, line 29).

`SA15` carried the consequence into the end-to-end register: `E2E-01` is `TRAVERSABLE WITH NAMED BREAK`
because *"commercial entry (SA-D21) unevidenced"* (blob `29416e10` line 31).

CORR2 re-measured the domain at **195 blobs / 187 paths, a 7.8× discounted ratio** against the 18/16 figure
(blob `1f1efe47` §2.2) and reclassified `SA-D21` from `THIN` to `THIN — NARROWED` (§3.5), leaving `TVDR-06`
`OPEN — bounded`, then answered *"Can research close it?"* with **"Yes"** in its Boss pack (blob `7753e217`
§3 row 3) and did not execute it.

This artefact executes it.

---

## 2. Instrument — declared, executed, and controlled

### 2.1 Frame
`POPULATION`, `PATH SET`, `UNIT` and `COVERAGE` are `CORR3-FRAME` verbatim: 184 branch heads UNION the
mainline tree; `U1` = 3,900 unique text blobs; `U2` = 3,579 unique text paths; 3900 requested / 3900 written
/ 0 missing / 0 zero-byte. This artefact adds **no** author-chosen boundary to that frame.

### 2.2 This item's own patterns — published in full and executed as written

```text
TV6-PRICE   price ?list|pricing (rule|policy|method|engine)|price (rule|determination|derivation|
            precedence|round)|unit price|discount|price break|quantity break
TV6-CREDIT  credit (limit|control|hold|block|exposure|policy)|customer (hold|blocked)|payment term|
            credit warning
```

Both patterns contain **generic commercial vocabulary only**. No reference-system object name appears in
either, deliberately — `K2-15` (blob `1f1efe47` §2.2.1) recorded that publishing a vendor object name inside
a published pattern is itself a clean-room leak, and that the scrub moved a control figure. This item
therefore never had those tokens to remove.

### 2.3 Result under three command shapes

| Measure | shape 1 `grep -rlE` → blobs | shape 2 `grep -rohE \| wc -l` → occurrences | shape 3 blob→path join → paths |
|---|---|---|---|
| `TV6-PRICE` | **178** (U1) | **1,699** | **171** (U2) |
| `TV6-CREDIT` | **97** (U1) | **223** | **81** (U2) |
| positive control `BD-ACC-01` | **55** | — | — |
| negative control `qxvz7481_no_such_token` | **0** | **0** | — |

Positive control reproduces `CORR3-FRAME`'s declared 55. Negative control is 0 on both shapes.

### 2.4 What the patterns actually matched, printed before being counted

`TV6-PRICE`: price-rule-set 881 · discount 721 · unit price 44 · price rule 33 · price list 12 ·
price determination 4 · pricing engine 2 · pricing rule 1 · price derivation 1.
`TV6-CREDIT`: payment term 128 · credit exposure 26 · credit control 26 · credit limit 24 · credit policy 10 ·
credit hold 5 · credit warning 3 · customer hold 1.

### 2.5 Injection control on **these** patterns, not on the corpus generally

A synthetic blob containing exactly `quantity break` and `credit exposure` was written into the corpus and
removed. `TV6-PRICE` 178 → **179** → 178. `TV6-CREDIT` 97 → **98** → 97. The injected blob was identified by
name in the match list. Corpus re-counted at **3,900** after removal.

Per the programme's own standard, extraction working is not the same as the predicate being able to fire.
This control proves the predicate fires.

### 2.6 `TV6-M-01` — the discriminating spread, zeros published beside non-zeros

| Sub-term (U1, case-insensitive) | blobs | second shape (occ) |
|---|---|---|
| `discount` | 123 | — |
| `payment term` | 57 | — |
| `price ?list` | 43 | — |
| `unit price` | 40 | — |
| `release.{0,20}(hold\|block)` | 34 | — |
| `tax.inclusive\|price.include\|inclusive of tax` | 25 | — |
| `price rule` | 17 | — |
| `credit limit` | 16 | — |
| `credit exposure` | 13 | — |
| `credit hold` | 5 | — |
| `price determination` | 4 | — |
| `margin (floor\|cap\|clamp\|min\|max)` | 1 | — |
| `credit.{0,20}audit` | 1 | 2 |
| `price round\|rounding…price\|price…rounding` | 1 | 1 |
| **`price precedence`** | **0** | **0** |
| **`quantity break\|price break\|volume break`** | **0** | **0** |
| **`price override`** | **0** | **0** |
| **`credit block`** | **0** | **0** |

### 2.7 `TV6-F-01` — **the four zeros are vocabulary artefacts, and this is the root cause of the original 18-blob figure**

Every zero above was re-searched as a **fact** rather than as a **phrase**:

| Phrase searched | U1 | The same fact searched as a fact — **clean pattern** | U1 |
|---|---|---|---|
| `quantity break` | **0** | `minimum quantity\|quantity threshold\|min(imum)? qty` | **1** |
| `price precedence` | **0** | `most specific rule wins\|rule scope hierarchy\|resolution order\|scope hierarchy` | **12** |
| `price override` | **0** | `unit price\|locked…price\|freeze…price\|named-field freeze` | **47** |
| `credit block` | **0** | `never raises\|advisory only\|advisory, non-blocking\|non-blocking` | **186** |

#### 2.7.1 `TV6-K-01` — vendor field names were removed from these published patterns, and the effect is measured, not asserted

The first version of the four fact-patterns above carried **reference-system field names**. Publishing a
pattern is required for reproducibility; publishing a vendor object or field name on a Layer 1 surface is a
clean-room leak — the precedent is `K2-15` (blob `1f1efe47` §2.2.1). All were removed and the effect measured:

| Row | With the vendor tokens | Clean | Δ |
|---|---|---|---|
| quantity break | **7** | **1** | **−6** |
| price precedence | 14 | **12** | −2 |
| price override | 50 | **47** | −3 |
| credit block | 186 | **186** | 0 |

**The table above reports the clean figures, and the quantity-break row is now 0 against 1, not 0 against 7.**
That delta is published because it is **large, load-bearing, and works against this artefact's own headline**:
on the clean pattern, the contrast for that one row is nearly gone.

**What survives, and what does not.** The *conclusion* of the quantity-break row survives, because it does not
rest on the frequency: a minimum-quantity gate is evidenced in **primary text** (`PRC-10`, blob `ce002d94`
line 287 — quantity gate evaluated before scope match) and as a **stored column in the deployed schema**
(blob `26ed9c8e` line 9466). The *corpus-frequency argument* for that row does **not** survive and is
withdrawn. `TV6-F-01` therefore rests on **three** frequency contrasts, not four, plus primary text for the
fourth. Stated here rather than in the residual section because a reader must not have to reach §10 to learn
that one row of a headline table was weakened by this artefact's own sweep.

**`TV6-F-01`. `SA02`'s `INPUT-EVIDENCE-INSUFFICIENT` on price is `EVIDENCE-REJECTED`.** Its stated authority
was a count — 18 blobs — and that count measured the programme's *vocabulary*, not its *evidence*. Four of
the six sub-questions `SA16` raised return zero on the word and 1–186 blobs on the thing, three of them
by an order of magnitude or more (see the scrub note at §2.7.1). CORR2 corrected the
count's magnitude (18 → 195) but not its *kind*; the defect was never that the number was small, it was that
a phrase-frequency measure was used as an evidence measure. The programme's own `Denominator completeness`
rule requires `POPULATION + PATTERN + PATH SET + UNIT`, none author-chosen — it does not yet require that the
**pattern be a predicate over the fact rather than over the words**, and that is the gap this item found.

**Scope of `TV6-F-01`.** It falsifies the *authority* for the negative. It does not by itself establish what
price determination is. §4 does that from primary text.

### 2.8 Pre-publication sweeps, and the one that returned a false positive

Seven checks with **deliberately disjoint units** were run as the last act before publication, because three
clean checks sharing one unit have shipped a broken record in this programme before.

| # | Unit | Result |
|---|---|---|
| 1 | vendor-token **occurrence** (declared set) | **0** |
| 2 | vendor **field name** occurrence (the `K2-15` class, wider than the declared set) | 7 found → scrubbed → **0**, delta published at §2.7.1 |
| 3 | prohibited-approval **line** | 1 hit, and it is the checkpoint's own disclaimer that completion is *not* Boss approval |
| 4 | **identifier** — every cited `TV6-` id is defined | cited 54 / defined 54 / **orphans 0** |
| 5 | **status string** — every disposition is from the CORR3 vocabulary | 5 distinct strings, all in vocabulary |
| 6 | **statutory claim** | 0 — the only tax words in this artefact are a verbatim quotation of `BD-ACC-02`'s own subject list |
| 7 | **citation resolution** — every cited blob prefix resolves to exactly one blob | 29 cited, 29 resolve, **after one correction** |

**Two defects were caught by these sweeps and both are recorded rather than silently fixed.**

**`TV6-K-02`.** Sweep 7 found a **cited blob prefix that resolved to zero blobs** — a transcription error in
the citation for the peer artefact discussed at `TV6-F-05`. Corrected. A citation that does not resolve is
indistinguishable from a fabricated one, which is why this check exists and why the correction is disclosed.

**`TV6-K-03`.** Sweep 4, on its first run, reported **six orphan identifiers**. All six were false positives:
the check's definition-regex matched register rows and bare bold labels but **not headings of the form
`### 7.1 \`TV6-D-01\` — …`**, which is how the design and method findings are defined. The *document* was
clean; the *check* had the wrong unit. Recorded because the programme's `Check unit must match the defect`
lesson predicts exactly this, and because a checker that cannot see one of its subject's two legitimate
definition forms will report clean on a document that is not, in the mirror-image case.

---

## 3. `TV6-F-02` — verdict on CORR2 Boss-pack blocker 3

> CORR2 (blob `7753e217` §3, row 3): *"**Price and credit determination are undefined.** Price: no rule,
> `INPUT-EVIDENCE-INSUFFICIENT`. Credit: a verified non-control that self-erases at confirmation.
> **Every sale begins here**."*

**Disposition: UPHELD IN ONE CLAUSE, CORRECTED IN THREE.**

| Clause | Verdict | Basis |
|---|---|---|
| *"Price: no rule"* | **`EVIDENCE-REJECTED`** | A **25-fact, line-cited price-determination register** exists on the remote (`PRC-01`…`PRC-25`, blob `ce002d94` lines 278–306), and SMEsPlus has already named **Sales Price Rule** as a canonical Shared Master concept with a stated owner, consumer, and boundary (blob `52ea2b07` §03 line 63 and §09 summary table line 190) |
| *"Price … `INPUT-EVIDENCE-INSUFFICIENT`"* | **`EVIDENCE-REJECTED`** | §2.7; the negative's authority was a vocabulary count |
| *"Credit: a verified non-control"* | **`EVIDENCE-PROVEN` — and narrower than stated** | Verified for two source generations by its owner's own five-form negative and by a reference-system self-test (blob `da0afa53` §2 S-02; blob `9f46094f` SO-32/33/36). **It does not transfer to the oldest deployed generation** — `P02-F-35a`, blob `dfe7e9e9` §2 |
| *"… that self-erases at confirmation"* | **`EVIDENCE-PROVEN` for the banner; INCOMPLETE as a statement of the defect** | The banner is guarded on pre-commitment status, so it is absent at the transition. But the exposure figure and the warning text are **both non-stored** — the control never existed as a record at any instant, not merely at confirmation. See `TV6-F-09` |
| *"determination … undefined"* (credit half) | **`EVIDENCE-REJECTED`** | SMEsPlus's credit-gate design **already exists and is complete in shape**: decision `APR-003`, blob `9ec4c968` §04 — an explicit, configurable Confirmation Gate Policy per gate type, each settable to block / warn-and-allow / allow-silently, with the **default value** deliberately deferred to Boss. It is registered as Fit-Gap candidate #14 (blob `3fe429ea` §04 line 45) and referenced by the current Sales canonical design (blob `e78a2bbe` lines 19–27) |
| *"Every sale begins here"* | **UPHELD** | `SA15` `E2E-01` and `SA16`'s block list (BN-01/02/03/06) both stand |

**`TV6-F-02`. Blocker 3 is not a research gap. It is one open research question (what exposure *is*), one
open design question this artefact closes (§4/§5), and one genuine Boss policy election that was already
correctly identified and correctly deferred five packages ago and has been re-reported three times since as
though it were unknown.** Three registers described a *decided design with a deferred default* as
*"undefined"*, because each read a status line rather than the design record it points at.

---

## 4. Per-element register

Status vocabulary is the CORR3 set. `Owner` names who must act, not who wrote the evidence.

### 4.1 Part A — price determination

| # | Element / question | Evidence | Status | Owner |
|---|---|---|---|---|
| `TV6-A-01` | What determines the unit price of a sell line | A rule-set is resolved for the party, a rule is matched inside it, and the line price is taken **from the matched rule object, not from the rule-set header** — `PRC-21`, blob `ce002d94` line 303 | `EVIDENCE-PROVEN` | — |
| `TV6-A-02` | Rule precedence order | Rules are ordered **scope → quantity-break descending → classification descending → identity descending**; most specific wins — `PRC-07`, blob `ce002d94` line 284. Scope hierarchy is a four-level ladder: global → classification → product → variant (`PRC-08`, line 285) | `EVIDENCE-PROVEN` | — |
| `TV6-A-03` | Computation precedence *inside* a matched rule | Literal order: **fixed → percentage → formula, then rounding, then surcharge, then margin clamps** (`PRC-11`, line 288). A margin floor and a margin ceiling both exist (deployed columns, blob `26ed9c8e` line 9472 and the adjacent 9473) | `EVIDENCE-PROVEN` | — |
| `TV6-A-04` | Quantity break | A minimum-quantity gate is evaluated **before** scope match (`PRC-10`, line 287); the deployed column exists (blob `26ed9c8e` line 9466). The buy side carries a structurally parallel but **separate** vendor break list (`PRC-24`, line 306) | `EVIDENCE-PROVEN` | — |
| `TV6-A-05` | Date validity | Applicable-rule filtering is by scope **AND** a start/end validity window (`PRC-06`, line 283); both deployed columns exist (blob `26ed9c8e` lines 9474–9475) | `EVIDENCE-PROVEN` | — |
| `TV6-A-06` | Basis and chaining | Base is **another rule-set (recursive), or the product cost, or the product list price**, with cross-currency conversion when needed (`PRC-12`, line 289), guarded against self-chaining by a depth-first cycle check (`PRC-13`, line 290) | `EVIDENCE-PROVEN` | — |
| `TV6-A-07` | Customer → rule-set resolution | Order is **party-specific → country-group → generic fallback → first available** (`PRC-15`, line 292), defaulted onto the commitment from a party property (`PRC-17`, line 299) | `EVIDENCE-PROVEN` | — |
| `TV6-A-08` | Unit of measure | Quantity is converted into the product's default unit **before** rule matching (`PRC-05`, line 282). Its own author flags this as a coupling not to copy (blob `ce002d94` line 322 (a)) | `EVIDENCE-PROVEN` | — |
| `TV6-A-09` | Currency: which, at what date, from what source | The **rule-set's currency silently becomes the transaction currency** (`PRC-18`/`CUR-14`, lines 300/474). The rate is **frozen at order date, not looked up live** (`CUR-15`, line 475) and is a stored column on the commitment header (blob `26ed9c8e` line 11695). Rate rows are **one per currency per company per day** (`CUR-11`, line 466) and creatable **only for root companies** (`CUR-12`, line 467). Missing rate resolves to **parity, silently, rather than raising** (`CUR-04`, line 459; the same defect class this programme has recorded as the silent 1:1 FX fallback) | `EVIDENCE-PROVEN` | — |
| `TV6-A-10` | FX revaluation of the resulting receivable | Owned elsewhere and heavily worked — `AAS_PLUS_REDESIGN/10_ACCOUNT_WAVE_A_FX_REDESIGN`, `ACCOUNT_P08.../10_P08_CURRENCY_FX_MODEL`, `GB-08`. Period-end unrealised revaluation is present in both studied generations and **licence-gated in both**, so a community-equivalent deployment has never had it (blob `47782c74` §15.4) | `NOT APPLICABLE — EVIDENCE-BACKED` (peer-owned; do not duplicate) | Account FX owners |
| `TV6-A-11` | Tax-inclusive vs tax-exclusive boundary | The boundary sits **on the tax master, defaulted from the company** (`TAX-04`, blob `ce002d94` line ~300 of §07). The company-level default is a stored, NOT-NULL column (blob `26ed9c8e` line 3724); the company also owns the tax rounding method (line 3721). The sell line stores **both** a tax-excluded and a tax-included reduced price (lines 10118–10119 region) | `EVIDENCE-PROVEN` | — |
| `TV6-A-12` | Discount — line vs document vs cascading | **Three structurally different facts share one word.** See `TV6-F-03` | `EVIDENCE-PROVEN` | — |
| `TV6-A-13` | Is discount a price component or a separate accounting fact | **Line discount is a price component** (a percentage column on the line and on the resulting entry line — blob `26ed9c8e` lines 10111 and 831 — with no discount account anywhere). **Document discount is an accounting fact** — it resolves onto a designated discount *product*, and the company carries three such product pointers plus two allocation accounts (blob `26ed9c8e` lines 3769 and the two adjacent allocation columns). **Early-payment discount is a third, settlement-time accounting fact** with its own gain and loss accounts (line 3692) | `EVIDENCE-PROVEN` | — |
| `TV6-A-14` | Price override — who may, within what bound, with what audit consequence | Partly proven, partly a hard gap. See `TV6-F-04` | `MATERIAL HOLD — EXACT UNRESOLVED PROOF GAP` | SMEs Core (design) + evidence acquisition |
| `TV6-A-15` | Rounding — at what step, to what precision, who owns the residual | Three distinct rounding owners are proven: **(i)** a per-rule rounding step applied after the formula and before surcharge (`PRC-11`; deployed column blob `26ed9c8e` line 9469); **(ii)** the currency's own rounding precision, through which every value-rounding call routes (`CUR-07`, blob `ce002d94` line 462); **(iii)** the payment-term installment builder, where **the last line absorbs the residual** (`PAY-05`, line 404), with a hard invariant that percentage lines sum to exactly 100% (`PAY-04`, line 403). Company-level tax rounding method is a fourth (blob `26ed9c8e` line 3721) | `EVIDENCE-PROVEN` | — |
| `TV6-A-16` | Does a price difference become a posting | **Yes, and the surface is three-tier — but it is a buy-side/valuation fact, not a sell-side price-determination fact.** See `TV6-F-05` | `EVIDENCE-PROVEN` | — |
| `TV6-A-17` | Price provenance durability | **The matched rule is cached on the line in the model and has no column in the deployed schema.** See `TV6-F-06` | `EVIDENCE-PROVEN` | — |
| `TV6-A-18` | Tenant / Company boundary on price | **The sell price is the one commercial quantity in the set that is not company-scoped.** See `TV6-F-07` | `EVIDENCE-PROVEN` | — |
| `TV6-A-19` | What may an extension **not** change (`SA16`'s closing question, price half) | Answered by design in §5.1 | `TARGETED RESEARCH COMPLETE — PROOF ESTABLISHED` | SMEs Core |

### 4.2 Part B — credit determination

| # | Element / question | Evidence | Status | Owner |
|---|---|---|---|---|
| `TV6-B-01` | What the credit control actually is | *"The entire enforcement surface is one comparison inside a string builder that returns a translated message or an empty string. It never raises."* Five distinct negative forms run separately against each of two full roots, zero relevant rows in both (blob `da0afa53` §2 S-02). Independently corroborated: the confirmation gate is **state plus product-presence only — no credit check** (`SO-13/14`, blob `9f46094f` line 49) | `EVIDENCE-PROVEN` | — |
| `TV6-B-02` | Where it is evaluated | Two sites, sharing one builder: the commercial commitment and the receivable document (`SO-32/33`, blob `9f46094f` line 59) | `EVIDENCE-PROVEN` | — |
| `TV6-B-03` | Against what exposure figure, and what is included | Exposure is **two components**: the party's open receivable, plus a **to-be-invoiced** component that the sell-side module *extends* onto the party (the same compute name is declared **twice**, once by the accounting module and once by the sales module — blob `3d290bcc`, partner rows). See `TV6-F-08` | `EVIDENCE-PROVEN` in composition · `MATERIAL HOLD — EXACT UNRESOLVED PROOF GAP` in coverage | Research (bounded, §7) |
| `TV6-B-04` | Verify *"self-erases at confirmation"* at primary evidence | Primary text located and read: *"the warning is guarded on draft/sent status, so it self-erases at the moment of confirmation or posting — absent precisely at the transition a gate would have to intercept"* (blob `da0afa53` lines 50–51). **Upheld.** Corroborated structurally: pre-commitment and "sent" states are treated identically by the confirmation-error builder, and "sent" has **no behavioural difference** from draft (blob `9f46094f` synthesis) | `EVIDENCE-PROVEN` | — |
| `TV6-B-05` | Is the non-control LATENT or LIVE | **Both, in different deployments.** See `TV6-F-10` | `EVIDENCE-PROVEN` | — |
| `TV6-B-06` | Blocking vs warning vs informational | Informational only in the reference behaviour, **test-confirmed by the reference system's own test**: an order at exactly the party's limit confirms with no exception (`SO-36`, blob `9f46094f` line 60). SMEsPlus has already decided the *shape* is a three-valued configurable policy (`APR-003`, blob `9ec4c968` §04) | `EVIDENCE-PROVEN` | — |
| `TV6-B-07` | Who may release a hold, and with what audit trail | **No release concept exists to audit.** See `TV6-F-11` | `MATERIAL HOLD — EXACT UNRESOLVED PROOF GAP` (evidence) / closed by design in §5.2 | SMEs Core (design) |
| `TV6-B-08` | The four-site company-context defect | Reported by its owner as *"each compute opens with a company-context call whose return value is discarded … the limit actually read is the one resolved against the acting company, not the document's"* with deployed consequence `UNRESOLVED — EVIDENCE REQUIRED` (blob `da0afa53` lines 53–57). **This artefact supplies the missing mechanism proof from a disjoint instrument**: the limit column is physically stored as a **company-keyed JSON document** (blob `26ed9c8e` line 4178). A company-dependent read with a discarded company context therefore necessarily resolves against the acting company. The mechanism is no longer an inference | `EVIDENCE-PROVEN` (mechanism) · deployed consequence `MATERIAL HOLD — EXACT UNRESOLVED PROOF GAP` | P02 / Research |
| `TV6-B-09` | Tenant / Company boundary, and does `BD-ACC-02` bind it | See `TV6-F-12`. `BD-ACC-02` does **not** literally bind credit exposure; its structure nevertheless answers the question | `EVIDENCE-PROVEN` (boundary) · `TARGETED RESEARCH COMPLETE — PROOF ESTABLISHED` (design) | SMEs Core |
| `TV6-B-10` | Relationship to `XD-01` invoice durability | They touch at exactly one point and this artefact defers. See `TV6-F-13` | `NOT APPLICABLE — EVIDENCE-BACKED` (deferred, not duplicated) | Boss (`XD-01`) |
| `TV6-B-11` | A second exposure granularity in the deployed estate | A **party-group-level credit limit** exists in the deployed schema, on an excluded-source legacy structure. See `TV6-F-14` | `EVIDENCE-PROVEN` (existence) · **learning excluded by Boss ruling** | Migration / TBRAC carry-forward |
| `TV6-B-12` | Feature switches that determine whether any of this runs | A per-company boolean governs whether the credit-limit surface is used at all (blob `26ed9c8e` line 3739); a per-party opt-in and a display flag exist **only as non-stored computes** (blob `f4b359f6`, partner rows). Line-level discount is itself behind a per-database settings flag (blob `26ed9c8e`, the settings-table row governing per-line discount) | `EVIDENCE-PROVEN` | — |
| `TV6-B-13` | What may an extension **not** change (`SA16`'s closing question, credit half) | Answered by design in §5.2 | `TARGETED RESEARCH COMPLETE — PROOF ESTABLISHED` | SMEs Core |

---

## 5. Part A — price determination: the findings

### `TV6-F-03` — one word, three facts, two of them accounting facts

The deployed schema carries, simultaneously:

1. **Line trade discount** — a percentage on the commercial line and on the resulting entry line
   (blob `26ed9c8e` lines 10111, 831). It reduces the line subtotal. **There is no discount account for it
   anywhere in the schema.** It is a *price component*.
2. **Document trade discount** — a separate record per document on each of the sell and buy sides, carrying a
   type, an amount and a percentage (blob `26ed9c8e`, the sell-side and buy-side document-discount tables and
   the entry-side one). It resolves onto a **designated discount product**, of which the company holds three
   pointers, plus **two dedicated allocation accounts** (blob `26ed9c8e` line 3769 and adjacent). It **is** an
   accounting fact, and its account is resolved from a product, not from a discount policy.
3. **Early-payment (settlement) discount** — a payment-term construct (deployed columns: discount days,
   percentage, and a computation-basis selector) landing on the entry line as a discount date, a discount
   balance and a discount amount in currency (blob `26ed9c8e` lines 817, 832–833), with **its own gain and
   loss accounts on the company** (line 3692). Its basis is configurable as total or total-minus-tax
   (`PAY-06`, blob `ce002d94` line 405).

**The collision is physical, not merely conceptual**: facts (1) and (3) occupy columns with the *same name
stem* on the *same entry-line table*, at different grain and with different accounting consequence.

**Why it matters for `SA16`'s question.** `02_BOSS_DECISION_CORE_EXTENSION_BOUNDARY` names discount strategy
as a *more extensible* area. An extension point over a concept that silently names three facts is not an
extension point; it is a defect generator. The core must separate them **before** anything extends it.

### `TV6-F-04` — price override: the authority surface exists, its application to price is not established, and the field-level freeze that does exist is post-commitment only

Three separate things were tested.

**(a) What is provably frozen, and when.** On a locked commitment, line writes are refused for a
**named set of exactly eight fields**, which includes the unit price, the discount, the quantity, the unit of
measure and the tax set (`SO-26/27`, blob `9f46094f` line 56). This is a **field-level freeze, not a blanket
block**, and locking is an **independent boolean, orthogonal to lifecycle state** — a just-confirmed
commitment defaults to *unlocked* (blob `9f46094f` synthesis; adopted as a SMEsPlus mechanism shape at blob
`e78a2bbe` lines 28–31). Separately, the **rule-set itself** cannot be changed once the commitment is
confirmed, and this is *the only* header write-restriction tied to state (`SO-28`/`PRC-19`, blob `9f46094f`
line 57; blob `ce002d94` line 301).

**Consequence, stated plainly: between confirmation and locking there is a window in which the unit price of
a committed line can be rewritten, and locking is off by default.** The price is protected against a *rule-set
swap* from the instant of confirmation and against a *direct edit* only from the instant of locking.

**(b) Whether a field-level permission surface exists at all.** First reading of the deployed schema found
row-level rules and model-level access only, and would have reported *no field-level permission surface*.
**That would have been a false negative.** A second command shape over the same artefact found a
**field-to-group relation table** (blob `26ed9c8e`, the field-group relation table). A field-level
restriction surface **does** exist. Recorded because the programme's `Counting-command validation rule`
predicts exactly this, and it fired.

**(c) Whether it is applied to the price fields.** **Not established.** The evidence base at hand is a
*column inventory* — it enumerates schema, not rows. Which fields carry a group restriction is a **row**
question about that relation table, and no artefact in `CORR3-FRAME` contains those rows.

`TV6-A-14` proof gap, exactly: **enumerate the rows of the field-to-group relation table for the unit-price
and discount fields in at least two deployments of different generations.** That is one query per deployment
against evidence the programme has repeatedly established is on the host but outside the session clone
(`primary source evidence locations`). It is not closable from source and is not a Boss decision.

### `TV6-F-05` — the price-difference account is real, three-tier, and on the wrong side of the sale

The Boss-approved product-level accounting override surface includes a **Price Difference Account**. The
brief asked what creates it. Tested:

The account exists at **three** levels in the deployed schema — a company default (blob `26ed9c8e` line 3715),
a **classification-level company-dependent property** (line 9327), and a **product-level company-dependent
property** (line 9654). Its evidence trail across the corpus is dense and lands, without exception, on the
**buy and manufacture** sides: receipt-versus-bill cost flow, landed cost, late cost, standard-cost variance,
manufacturing valuation explosion.

**No artefact in `CORR3-FRAME` places a price difference on the sell side.** Searched as a fact, not a
phrase; the sell-side packages that discuss price difference discuss it as a *scope boundary they route away*
(`P02` blob `931a7271`), not as an event they emit.

**`TV6-F-05`. The Price Difference Account is a procurement-and-valuation artefact, not an output of sell-side
price determination.** It arises where a *committed cost* and a *billed cost* disagree under a costing regime
that has already fixed a value. A sell-side price difference has no equivalent, because a sell-side price is
not a valuation — nothing was previously recorded at a different price for it to differ from.

**A by-product this item can close for a peer.** `CGS-U03` (blob `73ebba9d`) is `HOLD — EVIDENCE REQUIRED` on
whether the Price Difference Account and a newer "Variation Account" are *the same concept renamed, two
coexisting concepts, or version drift*. It could not resolve this because it had only **documentation
sources** and no live instance — the programme's own `Secondary-source defect class`. **Primary deployed
schema settles the structural half**: a stock-variation account pointer exists **on the chart-of-accounts
record itself** (blob `26ed9c8e` line 21), while the price-difference pointers sit on company, classification
and product. They are **two distinct fields at two distinct levels, coexisting in one deployed schema** —
therefore not a renaming. Which costing methods each *applies to* remains open and remains `CGS-U03`'s.
Offered to that owner as `TV6-F-05a`; this artefact does not amend a peer's register.

### `TV6-F-06` — price provenance is computed and never stored

The matched price rule **is** cached onto the line in the model layer (`PRC-20`, blob `ce002d94` line 302).
It has **no column in the deployed schema**.

Proven under three command shapes against the same artefact, with two positive controls that fire and a
declared denominator:

| Test | Result |
|---|---|
| exact-field match on the sell-line table for any price-rule column | **0** |
| anchored pattern match, different command | **0** |
| loose match within the table's rows | **0** |
| positive control — a column that *does* exist on that table (unit price) | **1** |
| positive control — the same concept *does* exist on the header | **1** |
| total columns enumerated for that table | **58** |
| disjoint second instrument (model-to-schema mapping, blob `f4b359f6`) | agrees — declared in the model, **mapping status: not found in the deployed schema** |

**Consequence.** After a commitment is confirmed, the system holds a price and no record of **why** that price
was that price. The rule that produced it, its validity window, its quantity break and its basis are all
recoverable only by *re-running determination against today's master data* — which is not the same
computation, because the rule may have been edited, expired, or deleted.

This is a **price-side instance of the identity defect `BD-ACC-01` rules against on the accounting side**:
a fact exists and nothing durable joins it to the act that produced it.

### `TV6-F-07` — the sell price is the only commercial quantity in its own set that is not company-scoped

Read directly off the deployed schema (blob `26ed9c8e`, line numbers given):

| Commercial fact | Physical storage | Scope |
|---|---|---|
| Product **base sell price** | plain numeric column on the product record (line 9627) | **NOT company-scoped** |
| Product **cost** | company-keyed JSON document (line 9486) | Company |
| Party **credit limit** | company-keyed JSON document (line 4178) | Company |
| Party **assigned price rule-set** | company-keyed JSON document (line 4172) | Company |
| Party **payment term** | company-keyed JSON document (line 4182) | Company |
| Party **trust / reliability** | company-keyed JSON document (line 4184) | Company |
| Product **revenue account** | company-keyed JSON document (product record) | Company |
| Company **tax-inclusive default** | NOT-NULL column on the company (line 3724) | Company |
| Company **tax rounding method** | column on the company (line 3721) | Company |
| Company **credit-limit switch** | column on the company (line 3739) | Company |
| **Price rule-set** | company reference is **nullable** (line 9442) — a tenant-global rule-set is permitted (`PRC-03`, blob `ce002d94` line 280) | Company **or** Tenant |
| Payment term | company reference nullable — a global term is permitted (blob `ce002d94` §08 synthesis) | Company **or** Tenant |
| Currency | genuinely global; **scoping enters only at the rate**, and rates are root-company-only (`CUR-12`) | Tenant / root |

**`TV6-F-07`. Every input that *consumes* the sell price is company-scoped. The sell price itself is not.**
A product shared across two companies in one tenant carries **one** base price for both, while carrying two
costs, two revenue accounts, two credit limits on its customers, two tax-inclusive conventions and two
rounding methods. The rule-set that can override the base price *may* be company-bound — and may equally be
tenant-global.

This is not a defect to normalize away. It is the correct question to put to design, and §5.1 answers it.

---

## 6. Part B — credit determination: the findings

### `TV6-F-08` — the exposure figure, and the coverage question that is genuinely open

**Composition, proven.** Exposure is the sum of a **posted open-receivable** component and a
**to-be-invoiced** component. The to-be-invoiced compute is declared **twice** — once by the accounting
module on the party record, and once by the sell-side module on the same party record (blob `3d290bcc`,
partner rows for both modules). The sell side therefore *extends* the accounting exposure to reach commercial
commitments that have not yet become receivables. There is also a company-level **default limit**, but it is
a settings compute with **no column on the company record** (verified: an anchored search for a default-limit
column on the company table returns nothing, while the *switch* column on the same table returns a hit).

**What is genuinely open — coverage.** The brief asks whether exposure includes delivered-not-invoiced. The
programme has **measured** that position and found it large and cross-generational: **3,593 lines across five
databases**, and in one measurement understated **24×** — 1,145 lines (23.4%) rather than 47 (1.0%), a
correction that **reversed the direction of its own parent finding** (`P02-F-34a`, blob `ca4ecb54` §§ 27–28,
67). Whether the to-be-invoiced compute's predicate actually reaches those lines is **not** answerable from a
column inventory or from the compute's *name*.

`TV6-B-03` proof gap, exactly: **for one deployment, compute the to-be-invoiced component for a party that
has delivered-not-invoiced lines, and compare it against those lines' value.** The `Discriminating set for
zeros` rule applies: include at least one party with delivered-not-invoiced lines and one never-transacted
party. Owner: Research, bounded, one query. It is not a Boss decision.

**Why it matters more than it looks.** If delivered-not-invoiced is outside exposure, then the single largest
measured un-billed position in the sell-side estate is invisible to the only commercial control that exists.

### `TV6-F-09` — the control is not merely un-enforcing; **nothing about it is ever recorded**

CORR2 said the control *self-erases at confirmation*. Verified (`TV6-B-04`). But the primary evidence
supports a **stronger and structurally different** statement, which CORR2 did not make.

Proven from the model-to-schema mapping (blob `f4b359f6`) and confirmed by direct enumeration of the deployed
schema (blob `26ed9c8e`):

| Element of a credit decision | Stored? |
|---|---|
| the party's **limit** | **stored** (company-keyed JSON, line 4178) |
| the party's **open-receivable exposure** | **not stored** — computed at read |
| the party's **to-be-invoiced exposure** | **not stored** — computed at read |
| the **warning text** on the commitment | **not stored** |
| the **warning text** on the receivable document | **not stored** |
| the per-party **opt-in** to the limit | **not stored** |
| the per-party **display** flag | **not stored** |

**`TV6-F-09`. Only the *threshold* is durable. Everything that would constitute a credit *decision* —
the exposure it was measured against, the comparison, the warning, and whether the check even applied to that
party — is transient.** "Self-erases at confirmation" describes *when* the banner disappears. The deeper fact
is that **there was never a record to erase**: no instant exists at which the system held a durable statement
of what a party's exposure was, or that anyone was told about it.

This makes `TV6-B-07` (release authority and audit trail) unanswerable from the reference behaviour **not
because the answer is hidden, but because the object the audit trail would attach to does not exist**.

### `TV6-F-10` — LATENT and LIVE, in different deployments; and the negative does not travel

| Deployment generation | Parties | Limits configured | Enforcement | Disposition |
|---|---|---|---|---|
| oldest generation, one deployment | 5,732 | **1,204 (21.0%)** | **unknown — its overriding sell-side code is unreadable** | **LIVE surface, enforcement `EVIDENCE REQUIRED`** |
| oldest generation, second deployment | 16,306 | 0 | — | LATENT |
| middle generation, four deployments | 10,399 | 0 | — | LATENT |
| newest generation, three deployments | 34,787 | 0 | — | LATENT |
| one generation, two deployments | — | **the column does not exist in that generation** | not representable | **NOT APPLICABLE** |

*(blob `dfe7e9e9` §2, `P02-F-35a`)*

**`TV6-F-10`. The verified non-control is LATENT in 9 of 11 material deployments by configuration, absent by
schema in 2 of them, and its LIVE instance is precisely the one deployment whose code cannot be read.** The
five-form negative that established "advisory only" was run against two source generations; its owner
explicitly refused to transfer it to the oldest generation, and said why: *"Asserting the v18/v19 finding
there would be exactly the source-versus-deployed conflation this round exists to prevent"* (blob `dfe7e9e9`
line 52).

**CORR2's blocker 3 cited the earlier artefact and not the later one that narrows it.** `24` (blob `da0afa53`)
is the source of "verified non-control that self-erases"; `35` (blob `dfe7e9e9`), `37` (blob `1c727e5e`, row
`B-4`), `38` (blob `260778a5`, row `U-6`) and `43` (blob `5ce7631d`, dependency 2) all carry the narrowing as
an open, owned dependency. Four artefacts in the same package say the claim is bounded; the Boss pack states
it unbounded. This is the `Supersession binds at claim level` defect, in its exact published shape.

### `TV6-F-11` — there is no release concept, and the one release-shaped surface on the sell side has been mis-reported twice

**No hold exists, therefore no release exists.** `credit block` returns 0 on two command shapes; the fact
search returns 186 blobs all saying *advisory / non-blocking / never raises*. There is nothing to release.

**But a release-shaped control does exist on the sell side**, and its history is instructive:

- The sell-side commitment carries a **two-level approval schema** — two approver references, two
  approved-by references, two approval dates and a rejection reason (blob `26ed9c8e` line 11737 and the
  following rows).
- The sell-side capability model recorded these as **orphans with zero source anywhere**, calling it *"the
  single largest open governance question in GROUP A research"* (blob `9f46094f`, database-evidence section
  and `SO-43`).
- That was **wrong, and was corrected** by a full data-plus-schema restore and direct queries against the
  deployed metadata: the owning module is named, is **first-party (author "SMEsPlus")**, and is **installed**.
  Their absence from three independent source greps is an **extraction-completeness gap, not a schema
  mystery** (blob `0db2be19` §03a, resolved under `CORR-003`). Live usage on the sell side: **two rows** —
  the artefact itself says the sample is too small to characterize.
- A *separate*, generically-named approval framework also exists and was **verified by exhaustive grep to
  have zero references to the sell-side commitment** (`SO-43`, blob `9f46094f`).

**`TV6-F-11`. A first-party, installed, sell-side multi-level approval control exists and is essentially
unused; a generic approval framework exists and is not wired to the sell side; and the capability model that
is still the most-cited sell-side artefact reports the first as an unexplained orphan.** The correction lives
in a different file and never propagated — the programme's `A revision log is not a correction` and
`Narrowed-finding propagation` defects, both present here at once.

For `TVDR-06` this matters because it is the **only** candidate carrier for a credit-release or
price-override authority on the sell side, and its internal gating logic is a `Controlled Carry-Forward
Unknown` in the current design (blob `e78a2bbe` lines 98–106; blob `9ec4c968` §03).

### `TV6-F-12` — the Tenant/Company boundary for credit exposure, and what `BD-ACC-02` does and does not decide

**What `BD-ACC-02` says** (blob `1db097c7` lines 22–30): VAT, withholding, tax registers, statutory tax
reporting, tax ownership and filing are **Company-scoped**; multi-company **informational views may be
provided**; such views **must not create cross-company tax posting, offsetting, settlement, statutory
aggregation, or filing authority**; multi-company support does not weaken Company accounting/tax boundaries.

**Does it bind credit exposure?** Tested against its own enumerated subjects. Credit exposure is not VAT,
not withholding, not a tax register, not statutory reporting, not tax ownership and not filing.
**`BD-ACC-02` does not literally bind credit exposure.** Saying otherwise would be the programme's
`Unresolved peer decision is not a boundary` defect in reverse — treating a *settled* ruling as wider than
its own text.

**But its structure answers the question anyway**, in three steps, each independently evidenced:

1. The **limit** is physically company-scoped (`TV6-F-07`).
2. The **receivable** the exposure measures is a Company accounting fact — `BD-ACC-01`'s closing clause:
   *"Every accounting event is bounded by Tenant + Company context"* (blob `1db097c7`).
3. `BD-ACC-02` **expressly permits** multi-company informational views and expressly forbids only
   cross-company *authority*.

**`TV6-F-12`. Credit exposure is a Company-scoped measurement that may be *viewed* at Tenant level and must
not be *decided* at Tenant level.** A tenant-wide exposure roll-up is a permitted informational view. A
tenant-wide **block** would be an authority exercised across a Company boundary over a set of Company-scoped
receivables — the exact shape `BD-ACC-02` forbids for tax, for reasons that apply identically here.
Design consequence in §5.2.

### `TV6-F-13` — where credit touches `XD-01`, and the deferral

`XD-01` is the **sell-side cancellation gate**, decomposed by CORR2 into two Boss decisions plus one delivery,
with a **durability precondition** raised as `C2-F-01`, and reframed as *"not 'which state blocks' but 'which
state SMEsPlus will make durable enough to block with'"* (blob `3d5bb1fc` §3.5–3.6). Its status is
**`OPEN — BOSS AUTHORITY REQUIRED`**.

**They touch at exactly one point.** `XD-01`'s Q2 asks whether a **posted receivable constitutes blocking
exposure**. That is the same predicate `TV6-B-03` asks about the exposure figure's composition.

**The deferral, stated.** `TVDR-06` supplies `XD-01` with the *measurement* answer (exposure is
posted-receivable **plus** to-be-invoiced — `TV6-F-08`) and with the *durability* answer for its own half
(nothing about a credit decision is durable today — `TV6-F-09`). `TVDR-06` **does not** decide which state
carries blocking weight. That is `XD-01`'s Q1/Q2 and it is Boss's. Anything this artefact said about it would
be the `Unresolved peer decision is not a boundary` defect.

### `TV6-F-14` — a second exposure granularity exists in deployed data, and Boss has excluded it from learning

The deployed schema carries a **party-group / head-office structure** with its own **credit limit**, its own
payment term, its own currency, and a total-sales accumulator (blob `26ed9c8e` line 2271 and the surrounding
rows; confirmed under three command shapes; independently listed as financially sensitive in blob
`b5fd181d`). Unlike the party limit, it is a **plain numeric, not company-keyed** — but the group record
itself is bound to exactly one company by a NOT-NULL reference, so this is a **party-group limit *within* a
company**, not a cross-company aggregation.

**Governance handling, applied.** A Boss ruling dated 2026-09-01 (blob `b6802cd4` §1.1) places this module
family **`EXCLUDED / OUT-OF-SCOPE FOR SMEsPlus SOURCE LEARNING`**, reason: *incomplete / analytically
unreliable*, and states: *"The project may record that a legacy table/field/module exists, but must not
derive target business logic, workflow, schema design, architecture, validation behavior, or canonical
semantics from excluded source."* Its Mandatory Downstream Handling item 4 requires valid migration
carry-forwards to be **explicitly recorded rather than silently deleted**.

**`TV6-F-14`, recorded within that boundary and no further.** A party-group-level credit limit **exists in
deployed data**. SMEsPlus's approved credit design (`APR-003`) recognises **one** exposure granularity — the
party. **No target exists for this data.** This is recorded as a `MIGRATION / TBRAC CARRY-FORWARD`, exactly as
the ruling's item 4 requires. **This artefact derives no design from it and recommends none.** Whether
SMEsPlus should *independently* have a party-group exposure concept is a business question that must be
answered from SMEsPlus's own requirements, never from this source — and it is not asked here.

---

## 7. Recommendation, with alternatives

Phase SA is authorized to design; a design gap is not a Boss decision. What follows is design, offered with
the alternatives considered and the reason for the choice. It is a recommendation, not an approval.

### 7.1 `TV6-D-01` — Price determination core: what an extension may extend, and what it may not change

**Recommended core (`INDEPENDENT-TARGET`).** A `PriceRuleSet` resolves a unit price from an ordered,
declarative rule set. The core owns and an extension may **not** change:

| Invariant | Why |
|---|---|
| **P-1. Determinism.** Given the same inputs, determination returns the same price. No rule may consult time-of-day, user identity, or any fact not in the declared input set: party, product, quantity, unit of measure, date, currency, commitment context | Without it, `TV6-F-06`'s provenance record is meaningless |
| **P-2. Total ordering.** Rule precedence is a **declared total order** over (scope specificity, quantity break, validity, sequence). No two applicable rules may tie. An extension may add rules; it may not add a *tie-break* | Learned from `PRC-07`/`PRC-08`'s four-level ladder; strengthened because the reference ordering can tie on equal specificity and resolves by row identity, which is not a business rule |
| **P-3. Provenance is a stored fact.** The resolved rule identity, its version, the basis it used, and the resolved rate are **written onto the commitment line at commitment time** and are immutable thereafter | Closes `TV6-F-06`. This is the price-side application of `BD-ACC-01`'s identity discipline |
| **P-4. Snapshot at commitment.** Price, tax treatment, term and rate are frozen at commitment; later master-data change never rewrites a commitment | Already SMEsPlus's stated position (blob `32b29ad2` §11.3, `INDEPENDENT-TARGET`); this makes it an invariant rather than a control |
| **P-5. One rounding owner per step, declared.** Rule rounding, currency rounding, tax rounding and installment residual are **four named steps in a fixed order**, each with a named owner, and the **installment residual lands on the last installment** | Learned from `PRC-11`, `CUR-07`, `PAY-04/05` and the company tax-rounding method. The reference system has all four and declares the order in code only |
| **P-6. Three discounts, three names, never one.** `TradeDiscountLine`, `TradeDiscountDocument`, `SettlementDiscount`. The first is a price component and posts nothing of its own; the second and third are accounting facts with their own account resolution | Closes `TV6-F-03`. **This is the single highest-value correction in Part A** |
| **P-7. Currency is chosen, not inherited.** The transaction currency is an explicit input to commitment, defaulted from the rule set but **recorded as a decision**. A missing rate **raises**; it never resolves to parity | Closes `TV6-A-09`'s silent-parity defect, which this programme has independently recorded on the accounting side |
| **P-8. Override is a first-class event, not a field write.** Changing a determined price produces a `PriceOverride` fact carrying actor, reason, prior determined price, new price, and variance against the determined price — **before** the commitment can be confirmed | Closes `TV6-F-04`(c) by design rather than waiting on evidence |
| **P-9. Extensions may add rule *kinds* and rule *sources*; they may not change P-1…P-8** | This is the direct answer to `SA16`'s closing question, price half |

**Alternatives considered and rejected.**

| Alternative | Why not |
|---|---|
| **Adopt the reference precedence wholesale** | Forbidden by the clean-room constitution and independently wrong: its ordering can tie, its provenance is not durable, and its unit-of-measure coupling is flagged as not-to-copy by the evidence's own author (blob `ce002d94` line 322) |
| **Price as free input, rules as a suggestion engine** | Simplest, and the reference system is close to this. Rejected: it makes `P-3` provenance vacuous and makes margin governance impossible, since there is no determined price to vary from |
| **Compute-on-read pricing, no snapshot** | Rejected: contradicts `P-4`, and the corpus already records the consequence of compute-on-read for the credit exposure (`TV6-F-09`) |
| **Single unified discount concept** | Rejected: `TV6-F-03` proves three facts with three accounting consequences. Unifying them is precisely the defect |
| **Make the base sell price company-scoped, matching every other commercial fact** | Considered seriously (`TV6-F-07`). **Not recommended as an invariant** — see `TV6-D-03`; it is a genuine business choice, not a defect |

### 7.2 `TV6-D-02` — Credit determination: complete the shape that already exists

`APR-003` (blob `9ec4c968` §04) already fixes the policy shape. It is **adopted unchanged**. What it does not
specify, and this artefact adds:

| Addition | Content | Closes |
|---|---|---|
| **C-1. Exposure is a named, versioned, composed fact.** `CreditExposure` = Σ of explicitly named components, each individually includable: posted-open-receivable, delivered-not-invoiced, confirmed-not-delivered, invoiced-not-due, overdue. **A deployment declares its composition; the composition is part of the policy** | Closes `TV6-F-08`'s coverage question by making it a declared configuration rather than an emergent property of a compute's predicate |
| **C-2. A credit evaluation is a stored event.** Every evaluation at a gate writes actor, timestamp, company, party, the composition used, each component's value, the limit read, and the outcome. Retained whether it blocked, warned, or passed | Closes `TV6-F-09`. **Without this there is nothing for `C-4` to audit** |
| **C-3. The limit is read in the document's company context, never the actor's** | Closes `TV6-F-08`/`TV6-B-08`. The mechanism is now proven, not inferred |
| **C-4. Release is an authorized event.** A blocked commitment is released only by a `CreditRelease` fact carrying actor, reason, the exposure snapshot released against, and an expiry. The releasing actor may not be the commitment's creator | Closes `TV6-F-11`. Consistent with `APR-003` §05's SoD requirement and with the existing `INDEPENDENT-TARGET` *"Credit limit override requires authorization and reason"* (blob `32b29ad2` §11.3) |
| **C-5. Scope.** Exposure is **measured** per Company. A Tenant-level exposure **view** is permitted. A Tenant-level **block** is not | Closes `TV6-F-12`, consistent with `BD-ACC-02`'s permitted-views / forbidden-authority structure |
| **C-6. The policy is evaluated at declared gates, and the gate list is part of the policy** — minimally: commitment confirmation, receivable issue. Never guarded on a pre-commitment state | Closes `TV6-B-04`. The self-erasure was caused by guarding the control on the state it was meant to police |
| **C-7. Extensions may add exposure components and gates; they may not change C-1…C-6** | Answer to `SA16`'s closing question, credit half |

**Alternatives considered and rejected.**

| Alternative | Why not |
|---|---|
| **Adopt advisory-only as the default** | This is what CORR2's phrasing implicitly treats as the finding. Rejected on the same ground `APR-003` gives: it is *one legitimate configuration*, not a target default, and adopting it silently would breach the clean-room constitution's prohibition on inheriting reference defaults |
| **Ship a hard block as the default** | Rejected: `APR-003` deliberately declines to fix a default and correctly routes it to Boss. Fixing one here would be this session overwriting a peer's reserved decision |
| **A single scalar exposure** | Rejected: `TV6-F-08` shows composition already differs between two modules in the reference system, and `P02-F-34a` shows the largest component was mis-measured 24× |
| **Party-group exposure as core** | **Not recommended, and deliberately not designed** — `TV6-F-14`. The only evidence is in a Boss-excluded source family |
| **Log only blocks and warnings, not passes** | Rejected: a control that records only its exceptions cannot report its own coverage — the programme's `Exception list cannot report itself` defect |

### 7.3 `TV6-D-03` — the one genuine Boss election, stated minimally

Everything above is design. **Two** items survive proof as policy/authority choices, and only these are put to
Boss. Both are stated in one line each.

> **`TV6-BOSS-01` — Confirmation Gate Policy default.**
> For a new SMEsPlus company, does credit exposure at commitment confirmation default to **block**,
> **warn-and-allow**, or **allow-silently**?
> *This is `APR-003`'s explicitly deferred item and Fit-Gap candidate #14. It is not new. It has been open
> since the Group A design round and has been re-reported as "undefined" three times since.*

> **`TV6-BOSS-02` — Base sell-price scope.**
> Is a product's base sell price a **Tenant** fact (one price across all companies) or a **Company** fact?
> *Consequence, stated because a decision without one is not a decision:* Tenant-scope is simpler and matches
> the deployed schema (`TV6-F-07`), but makes it structurally impossible for two companies in one tenant to
> price the same product differently **except** through a company-bound rule set — and rule sets are permitted
> to be tenant-global too, so the guarantee is weak. Company-scope aligns price with every other commercial
> fact but is a departure from the deployed shape and increases master-data volume.
> *SMEs Core's recommendation:* **Company-scoped base price with tenant-global rule sets permitted**, because
> a price that cannot differ by company while its cost, its revenue account, its tax convention and its
> rounding all can, will produce cross-company margin figures that no one can defend.

**Nothing else is escalated.** `TV6-A-14`(c) and `TV6-B-03` are bounded research (one query each, §8).
`XD-01`'s Q1/Q2 remain `XD-01`'s.

---

## 8. Disposition of `TVDR-06`

| Item | Status |
|---|---|
| Price determination — mechanism, precedence, inputs, currency, tax boundary, discount, rounding, provenance, scope | **`TARGETED RESEARCH COMPLETE — PROOF ESTABLISHED`** |
| `SA02` / `SA15` `INPUT-EVIDENCE-INSUFFICIENT` on price | **`EVIDENCE-REJECTED`** (`TV6-F-01`) — `SA15` `E2E-01`'s named break *"commercial entry (SA-D21) unevidenced"* no longer holds; its other named break (`XD-01`) does |
| Credit determination — control, evaluation sites, self-erasure, latency, scope, company-context defect | **`TARGETED RESEARCH COMPLETE — PROOF ESTABLISHED`** |
| Exposure **coverage** of delivered-not-invoiced (`TV6-B-03`) | **`MATERIAL HOLD — EXACT UNRESOLVED PROOF GAP`** — one query per deployment |
| Field-level permission on price fields (`TV6-A-14`c) | **`MATERIAL HOLD — EXACT UNRESOLVED PROOF GAP`** — one query per deployment |
| Enforcement in the oldest generation (`TV6-F-10`) | **`MATERIAL HOLD — EXACT UNRESOLVED PROOF GAP`** — inherited from `P02-F-35a`/`B-4`; **not this item's to close**, closable only by acquiring unreadable custom code |
| Confirmation Gate Policy default | **`TV6-BOSS-01`** |
| Base sell-price scope | **`TV6-BOSS-02`** |
| CORR2 blocker 3 as stated | **CORRECTED** (`TV6-F-02`) |

**`TVDR-06` is EXECUTED.** It does not carry into another round as a research item. Two bounded queries and
two Boss elections remain, and neither is a research programme.

---

## 9. Phase SA clean-room acceptance gate — seven answers

**1. Learned facts and business semantics.**
Price is determined by resolving a rule set for a party, then matching one rule inside it under a total order
of specificity, quantity break and validity, then computing from a declared basis with rounding, surcharge and
margin clamps applied in a fixed order. Currency, tax-inclusiveness and rounding convention are each owned by
a different actor. "Discount" names three different facts. Credit is a comparison of a stored threshold
against a computed exposure, evaluated at two sites, recorded nowhere.

**2. What was NOT inherited.**
The reference precedence chain (it can tie); rule-set chaining with a cycle guard (flagged not-to-copy by its
own evidence author); the unit-of-measure conversion coupling before rule matching; the silent parity fallback
on a missing rate; the currency-inherited-from-rule-set coupling; the advisory-only credit default; the
one-word-three-facts discount model; the transient exposure and transient warning; and the entire party-group
credit structure, which is under a **Boss source-learning exclusion** and from which no semantics are derived
here. **This artefact copies no pricing engine and no credit module.** It states the business questions each
answers and answers them from SMEsPlus principles.

**3. Alternatives considered.**
Nine, tabulated in §7.1 and §7.2, each with the reason for rejection. The two that survive as genuine
elections are escalated as `TV6-BOSS-01` and `TV6-BOSS-02`, minimally, with consequences stated.

**4. SMEsPlus rationale.**
Determinism plus stored provenance, because a price without a recorded reason cannot be audited, disputed, or
re-derived after its rule changes. Three named discounts, because two of them post and one does not. A stored
credit evaluation, because a control whose only artefact is a banner cannot demonstrate that it ran.

**5. Tenant / Company / control / audit boundaries.**
Tenant/Company: `TV6-F-07` and `TV6-F-12` — every consuming input is Company-scoped, the base price is not,
exposure is measured per Company and may be viewed but not decided at Tenant level. Control: `P-8` price
override and `C-4` credit release are both first-class authorized events with SoD, not field writes. Audit:
`P-3` and `C-2` make provenance and evaluation durable facts, which is the precondition for any audit trail
existing at all.

**6. What SMEsPlus does better or differently.**
Price provenance is durable where the reference system's is transient. Precedence is a declared total order
where the reference system's can tie. A missing rate raises where the reference system silently assumes
parity. Discount is three named facts where the reference system has one word over three. Credit exposure is
a declared composition where the reference system's is an emergent property of two independently-extended
computes. Every credit evaluation is recorded where the reference system records none. The credit limit is
read in the document's company where the reference system discards the company context at four sites.

**7. Is further Very Deep Research required?**
**No.** Two bounded queries remain (§8), each one query per deployment against evidence the programme has
established is on the host. Neither is a research programme, and neither should re-open `TVDR-06`.

*(The parallel six-check clean-room list at blob `b2220600` §13 is also satisfied: no implementation excerpt
is reproduced; only business behaviour is transferred; no sentence instructs SMEsPlus to copy reference
architecture; every unresolved item in §8 carries an owner and a closure condition; joint Account × Sales
items are not closed unilaterally — `TV6-A-10` and `TV6-B-10` are deferred to their owners; and no Thai
statutory claim is made anywhere in this artefact.)*

---

## 10. Residual uncertainty

**(a) What remains uncertain.**

1. **Generation basis of the deployed-schema instrument.** The column inventory and the model-to-schema
   mapping used throughout §4–§6 are a **single-deployment artefact** (blob `26ed9c8e`, blob `f4b359f6`;
   path resolves under one handoff-documentation package). Its generation is **not established by this
   artefact** — manifest version strings are not a discriminator, per the programme's own version-basis rule.
   Where a claim is generation-sensitive it is marked as such. `TV6-F-10`'s generation table comes from a
   different, explicitly four-generation instrument (`P02`) and is not affected.
2. **Row-level facts are absent from this evidence base throughout.** Every schema claim is about *structure*.
   Every claim about *use* is inherited from artefacts that queried deployed data, and is attributed.
3. **`TV6-F-05`'s negative** — that no artefact places a price difference on the sell side — is bounded by
   `CORR3-FRAME` and by the pattern in §2.2. It is a statement about this corpus, not about the world.
4. **The company default credit limit's storage location.** The switch is a column; the default *value* is a
   settings compute with no column. Whether it lands per-company or tenant-wide is **not established**, and
   if tenant-wide it is a Company-boundary defect. Closure: one metadata query. Not escalated.

**(b) What could not be proven, and the exact proof gap.**

| Gap | Exact closure |
|---|---|
| `TV6-B-03` — whether delivered-not-invoiced is inside the exposure figure | For one deployment: compute the to-be-invoiced component for a party known to have delivered-not-invoiced lines; compare to those lines' value; include a never-transacted party as the negative control |
| `TV6-A-14`(c) — whether the price and discount fields carry a field-level group restriction | Enumerate rows of the field-to-group relation table for those two fields, in two deployments of different generations |
| `TV6-F-10` — enforcement in the oldest generation | Not closable without acquiring the unreadable overriding sell-side code. Owned by `P02` `B-4`. **Not this item's** |
| The company default credit limit's scope | One metadata query for the parameter's storage row |

**(c) The claim a challenger should attack first.**

**`TV6-F-01`** — that the four zeros are vocabulary artefacts and that this, not corpus size, is the root
cause of `SA02`'s negative. It is the load-bearing claim: `TV6-F-02`'s first two corrections rest on it, and
it is a claim about *method* made by the same party whose method it vindicates. Attack it by taking each of
the four fact-searches and testing whether the blobs it returns actually answer the sub-question, or merely
contain the token. If the price-precedence row's 12 blobs do not contain an actual precedence
*rule*, `TV6-F-01` weakens even though its arithmetic holds — and note that one of its four rows has already
been withdrawn on exactly this ground by this artefact's own clean-room sweep (§2.7.1) — the programme's `Predicate vs arithmetic` lesson applies to this artefact
exactly as it applied to `P08`.

**Second, attack `TV6-F-05`** — the assertion that price difference is buy-side only. It is a
negative over a pattern I chose, and it is the one finding here that *contradicts the framing of the brief
that commissioned it*. A finding that conveniently narrows my own scope is exactly the shape the programme's
`Control on the result you like` and `Self-interested classification` lessons warn about, and I am the wrong
party to have validated it.

**Third, attack `TV6-F-09`'s inference chain.** The seven-row stored/not-stored table is proven. The step
from *"not stored"* to *"no credit decision was ever recorded"* assumes no other artefact records it — no
message log, no tracked-field history, no audit module. I did not enumerate those. If a message or tracking
subsystem records the banner, `TV6-F-09` weakens from *"nothing is recorded"* to *"nothing is recorded in a
queryable, structured form"* — still material, but a different finding, and `C-2` would then be an
improvement rather than a first.

---

`CP-SA-C3-13 — TVDR-06 PRICE AND CREDIT DETERMINATION EXECUTED (execution status).`

Checkpoint completion is **not** Boss approval.

No Evidence = No Progress. Never Skip Gate. Unknown is not Fact. Boss remains the sole Final Approver.
