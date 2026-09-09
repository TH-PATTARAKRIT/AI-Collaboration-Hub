# SC-16 — FINAL CANONICAL ADVERSARIAL RE-CHECK

## CP-SA-SC-140 — CANONICAL PACK RE-CHALLENGED

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Execution host: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **This is `INTERNAL ADVERSARIAL SELF-CHALLENGE`. It is not independent assurance and is not offered as
> any part of one.**

---

## 1. Result

| | |
|---|---|
| Falsification classes run | **15 of 15** |
| Classes returning a finding | **4** |
| Findings raised | **4** |
| Findings corrected before publication | **4 of 4** |
| **Instrument failures caught by their own controls** | **2** — and both are published rather than quietly re-run |
| Findings that changed a Boss-facing number | **1** (`SC-F-10`) |

---

## 2. The fifteen classes

| # | Class | Method | Result |
|---:|---|---|---|
| **1** | Hidden duplicates across SC and AR | Parsed `SC-10`'s family table programmatically; extracted every atomic ID; tested for membership in more than one family | **CLEAN.** 8 families, declared counts match extracted IDs, **`0` IDs in two families**, total **23** |
| **2** | Boss-reserved item decided by SMEs Core | Enumerated every SMEs Core closure this round and tested each against *"is this an election, or a consequence of an adopted rule?"* | **1 candidate, handled** — §3.1 |
| **3** | SMEs Core item wrongly escalated to Boss | Re-ran the removal tests on all 30 candidates | **CLEAN.** `0` removable, agreeing with two prior independently-derived populations |
| **4** | Wrong atomic count | Summed the register's own rows rather than restating a headline: `2+3+1+2+6+4+4+1` | **`23` ✓** — matches the declared total |
| **5** | Wrong family mapping | Checked every atomic ID appears in **both** `SC-10` and `SC-11` | **CLEAN.** `0` missing in either |
| **6** | Secondary-source claim contradicting primary source | Re-read `SA_CORR3_03` and the constitution directly for the two load-bearing peer claims | **1 finding** — §3.2 (`SC-F-08`, raised at `SC-08`) |
| **7** | Suppressed clause | Checked whether any quotation in this pack omits a clause that changes its meaning | **CLEAN** — and the pack **adds** two clauses prior rounds suppressed (`POH-F-06`'s *"reserved to the veto's issuer and Boss"* and *"Deciding `BLK-07` alone would not lift the veto"*) |
| **8** | Stale conclusion from pre-AR evidence | Swept every `SC-*` file for `2[456] Boss` / `all 2[456]` / `the 2[456] decisions` | **1 finding** — §3.3 (`SC-F-10`) |
| **9** | Unsupported COGS freeze claim | Swept every file for `COGS` co-occurring with freeze/already-ruled/approved-direction language | **CLEAN.** The **only** hit is the pack's own denial: *"no prior Boss COGS freeze claimed"*. **`SC-11` `F1` states the premise does not resolve** |
| **10** | Vendor/reference behaviour treated as SMEsPlus policy | Swept for adoption language tied to reference/vendor/generation | **CLEAN.** `0`. `SC-11` `F3` states the opposite explicitly and grounds its recommendation on `XMC-F-03` and `BD-ACC-03A`, **not** on either generation |
| **11** | `SMT` naming drift in current-state text | Counted `\bSMT\b` in every `SC-08`…`SC-18` file and classified each occurrence | **1 finding, corrected** — §3.4 |
| **12** | Veto ownership error | Compared this pack's six rows against the peer's six rows, issuer by issuer | **CLEAN.** Both tracks: issuer **AAS+** on all six, two co-owned with Boss. **`0` discrepancies** |
| **13** | False independence claim | Swept for `independent assurance/review complete|performed|achieved` | **CLEAN.** `0`. Every match on `independent` is a **negation** (*"`0` structurally independent Phase SA reviews performed"*) or an act description |
| **14** | Phase-SA vs runtime proof conflation | Checked whether any runtime obligation is counted in class A | **CLEAN.** Class A `= 0`; all 8 runtime obligation families sit in class C with a stated reason each |
| **15** | Boss route lineage contradiction | Traced `BOSS-ROUTE-01` across `SC-07`, `SC-08`, `SC-09` | **CLEAN.** `SC-07` records **OPEN** (true at `c4949ec6`), `SC-08` §2 states *"`OPEN` … Closed at `SC-09`"*, `SC-09` records **CLOSED**. **A marked supersession, not a contradiction** |

---

## 3. The four findings

### 3.1 `SC-F-11` — one SMEs Core closure sits closest to the Boss-reserved line, and it is handed back

**Class 2.** Six items were closed by SMEs Core this round. Five are consequences of adopted rules —
`F2`'s `M-1`…`M-6`, `C2-D-01`'s shortage exit, `F3`'s endpoint semantics, `F4`'s declaration authority,
`F8`'s "always required" ground. **The sixth, `C2-D-02`, is the only one that removes an item from the Boss
list**, and it is therefore the only one whose misclassification would matter.

> **Correction applied: `SC-BOSS-LEVER-01` is published on the `F3` card's face** (`SC-11`) and in the
> register (`SC-10` §4). **If Boss judges the binding identity a policy election, `C2-D-02` is reinstated
> and the canonical count is `24`, not `23`** — one word, no further work.
>
> **The master prompt forbids deciding a Boss-reserved election to shorten the list. This closure is
> offered against that test with the reversal in Boss's hands, not around it.**

### 3.2 `SC-F-08` — a peer's number adopted, a peer's reason corrected

**Class 6.** The peer grounded `AR-F-01` on *"veto limb 2 is `POH-G-03`, an SMEs Core design gap, not a
Boss decision, and is removed from the decision population entirely."*

**Primary source refines it.** `POH-F-06`: *"Limb 2 … is an SMEs Core proof obligation"* — **the peer is
right about discharge** — but also: ***"Restating a veto limb is reserved to the veto's issuer and Boss"***,
and `POH-D-06`'s cell extends its restatement request to limb 2. **Limb 2 is absorbed into `POH-D-06`, not
excluded from the population.**

**The number `6` stands** — confirmed independently by `POH-F-16`: *"The Boss residue is **six items**"* —
**and two consequences neither track carried are now published**: `POH-D-06` requires **AAS+ as well as
Boss**, and *"Deciding `BLK-07` alone would not lift the veto."*

**Also recorded: the peer offered to let this session off on `AR-F-01`** (*"no correction is proposed to
`SC`"*, both units defensible). **The offer was declined** — `8` is reachable only by slicing one governance
act into subjects **and** adding a third the source does not put in the decision population. That is a
membership error on top of a unit choice, not an alternative unit.

### 3.3 `SC-F-10` — a stale `26` survived in `SC-00` and reached the pack

**Class 8.** `SC-00` §1 read *"…which turns on the **26** Boss decisions…"*. **`26` is the parent's
defective count.** `SC-01`, `SC-04` and `SC-06` were corrected at `SC-07`; **`SC-00` was not swept, because
the correction was scoped by the files that carried the *conclusion* rather than by the files that carried
the *number*.**

> **Correction applied.** The figure is **removed** from `SC-00` — not restated — with a supersession note
> pointing to `SC-10`, because that file's subject is the mainline act and the count is not its to hold.
>
> **This is the programme's recorded *correct-by-population-not-disposition* class:** a correction scoped
> to where the argument lived, missing where the digit lived. **The sweep that caught it is by figure, not
> by argument.**

### 3.4 `SC-F-12` — legacy `SMT` identifiers carried into current-state text unmarked

**Class 11.** `SC-08`…`SC-18` contain **no** use of `SMT` as the name of the active body. But `SC-10` and
`SC-11` cite **`SC-SMT-01`…`SC-SMT-11`** — finding identifiers minted in `SC-03` before the nomenclature
control — **unmarked**.

> **Correction applied.** Both files now carry an **IDENTIFIER NOTE** stating that these are historical
> finding identifiers, retained verbatim so citation lineage is not severed, marked
> **`LEGACY NAME — CURRENT BODY = SMEs CORE`**, and that they name findings, never the active body.
>
> **They are not renamed.** Renaming identifiers already published at `2139088b` would sever lineage to
> satisfy a naming rule — the wrong trade.

---

## 4. Two instrument failures, caught by their own controls

**Both are published rather than quietly re-run.**

| # | Instrument | Failure | How caught | Fix |
|---|---|---|---|---|
| `SC-I-03` | Check 9's regex | `grep -E` returned **`error: exceeds complexity limits`** — an **error**, not a zero. **Reading it as "no hits" would have published a clean result from an instrument that never ran** | the error text was read instead of the empty output | re-run with two simple patterns and a positive control |
| `SC-I-04` | Check 13's first form | Returned **file paths with no line content**, which reads as two hits | re-run with `-h` and the actual matching lines printed | **`0` real hits**; every `independent` match is a negation or an act description |

**With the two from earlier in this session (`SC-F-01`, and the `C-02` substring/word-boundary pair) and
the peer's two (`AR-I-01`, `AR-I-02`), six instrument failures have been caught by controls across the two
tracks in this programme's last two rounds. Every one would have produced a plausible, publishable, wrong
result.**

---

## 5. What this re-check did NOT do

1. **It did not re-grade `E2E-04`.** A prior round's re-grade was withdrawn under challenge; reversing that
   on this session's own specification is held for the independent reviewer.
2. **It did not answer `FG-F-06`.** `NO AUTHORITY TO SELF-SELECT`.
3. **It did not discharge, re-word or narrow any veto.**
4. **It did not modify any peer artefact.** The AR branch was read-only throughout.
5. **It is not independent assurance**, and this pack claims none.

---

## 6. Checkpoint

> ## `CP-SA-SC-140 — CANONICAL PACK RE-CHALLENGED`
> **15 of 15 falsification classes run · 4 findings, **4 of 4 corrected before publication** · 1 changed a
> Boss-facing number (`SC-F-10`) · 1 peer reason corrected while its number was adopted (`SC-F-08`) ·
> 1 legacy-identifier marking applied (`SC-F-12`) · **2 instrument failures caught by their own controls
> and published** · the closure nearest the Boss-reserved line handed back with a reversal lever
> (`SC-F-11`) · `0` duplicates · `0` wrong mappings · `0` false independence claims · `0` vendor behaviour
> as policy · `0` COGS freeze claimed.**

No Evidence = No Progress. Never Skip Gate. Internal challenge is not independence.
Boss remains the sole Final Approver.
