# 20 — P03 AAS+ AUDIT

**LAYER 2 — AUDIT QUARANTINE.**

AAS+ **preserves dissent**. Where the four AAS-03 experts disagreed, or where an expert's
challenge was not sustained, the minority position is recorded here rather than dissolved
into a consensus.

---

## 1. Preserved dissent

### `D-01` — E1 vs the package on `DC-07`'s severity

**Package position:** Critical. Absorbed labour crediting a COGS account misstates gross
margin in the production period.

**E1's dissent, not sustained but preserved:** the misstatement self-corrects when the
batch sells, and for a fast-turning SME with a monthly cycle it may never cross a period
boundary. E1 argues Critical overstates the *typical* case and should be High.

**AAS+ ruling: the package position stands, and E1's dissent is recorded as legitimate.**
Severity is assigned on the failure mode, not on the expected frequency —
`PROJECT_CONSTITUTION.md` principle 13 forbids averaging financial-integrity failures into
a low overall rate. **But E1 is right that the package nowhere states the frequency
assumption**, and a reader may infer a permanent error where there is a timing error.
`AASP-01`: `DC-07` must be described as a **period-attribution** failure, not a permanent
one.

### `D-02` — E2 vs E3 on whether `DC-01` should be the headline

**E2:** `DC-01` is the strongest finding — a clean, code-level contradiction between two
modules, provable without configuration assumptions.

**E3:** `DC-01`'s *financial* impact is entirely configuration-dependent (`UNR-P03-01`),
whereas `DC-11` breaches a tenant-isolation boundary in **every** multi-company
configuration and needs no special usage pattern. E3 holds that `DC-11` should lead.

**AAS+ ruling: both retained, no ranking imposed.** `05` §1 lists `DC-01` first and
`DC-11` at equal Critical severity. **E3's point is materially strengthened by CORR1**:
`18` §3 establishes that the labour entry is a canonical `COMPANY`-scoped financial event,
so `DC-11` is a breach of a scope rule that the corrected constitution states explicitly,
not of an inferred one. **`AASP-02`: an independent reviewer should treat `DC-11` as at
least co-equal with `DC-01`.**

### `D-03` — E4's minority position on the requirements

E4's challenge 11 was answered by consolidating the requirements (`C-09`). E4 maintains a
narrower objection that consolidation does not answer: **the act of numbering requirements
`R-01` … `R-15` creates an artefact that a later session may treat as a specification
baseline**, regardless of how it is labelled.

**AAS+ ruling: dissent preserved and acted on in part.** The consolidated register in
`21_P03_PMO.md` §3 carries an explicit non-baseline marker. E4's position that the marker
is insufficient protection is recorded, unresolved.

## 2. Findings AAS+ challenges that AAS-03 did not

### `AASP-03` — the package's own biggest untested assumption

Every finding rests on the premise that the declared source root is the code that will
inform SMEsPlus. `DEP-04` records that the running system's installed-module list is
unknown and is an Asset-package priority-1 UAT query.

**AAS+ position: this is under-weighted.** `02` §3 bounds the negative claims correctly,
but `02` §2's conclusion — *the reference product has no mechanism to capitalise fixed
production overhead* — is stated with a confidence the scope does not fully support. Eight
"no path" rows all fall together if one unexamined module supplies an overhead path.

**Required:** `02` §2 must carry the `DEP-04` caveat inline, not only by reference.

### `AASP-04` — a structural gap in the package

P03 traces cost **into** WIP and FG exhaustively. It traces cost **out of** FG in one
sentence (`03` §5), on the grounds that COGS belongs to another track at terminal HOLD.

That boundary is correct. **But the prompt's chain explicitly ends at
`Report/Close`, and P03's coverage of the *report* end is thin** — `15` §3 is the only
place a reporting surface is assessed, and it assesses one view.

**AAS+ position: the package is asymmetric between its cost-in and cost-out halves, and
says so nowhere.** Recorded as a known limitation rather than repaired, because repairing
it inside this session would mean entering the COGS track's territory while it is on HOLD.

### `AASP-05` — CORR1 arrived after most of the package was written

The scope correction was received mid-session, after `01`–`17` were drafted. `22` §3
records the revalidation. **AAS+ notes that a revalidation performed by the same session
that made the original assumption is the weakest form of review available**, and that
`smeplus-adversarial-section-not-summary-rule` records self-review as historically finding
a small fraction of what independent review finds.

**Required:** the scope revalidation in `18` and `22` §3 must be treated as a **candidate**
for P11's cross-process reconciliation, not as a settled result. This is already how `18`
§6 frames it; AAS+ endorses that framing and records that it is load-bearing.

## 3. What AAS+ does **not** dispute

Recorded so the endorsement is as explicit as the criticism:

| Item | AAS+ position |
|---|---|
| `DC-01`'s code reading | **Sound.** Three functions read in full; the contradiction is direct |
| `DC-03`, `DC-04` residue arithmetic | **Sound.** Derived from code, and the derivation is shown |
| `05` §9's discarded hypothesis | **Exemplary.** The falsification is recorded with the reasoning that made it plausible |
| The Asset-boundary discipline | **Sound.** `BLK-07` and `BLK-08` are quoted, not resolved; `CTR-C-06` is confirmed, not closed |
| `16` §4's clean cross-check | **Sound**, and correctly recorded as a finding in itself |
| `18` §2's ownership/availability distinction | **Sound**, and the strongest thing CORR1 produced in this session |

## 4. Where an independent reviewer should attack first

Ranked, so the next reviewer does not have to choose blind:

| # | Target | Why |
|---|---|---|
| 1 | `02` §2's eight-row negative conclusion | Highest consequence, weakest scope support — `AASP-03` |
| 2 | `DC-08`'s mechanism | Already downgraded to `SUPPORTED INTERPRETATION` by `C-04`; `_set_duration` was never read |
| 3 | `UNR-P03-02` — setup/cleanup charged per backorder | Asserted from code reading with no runtime confirmation; would be a further double count if true |
| 4 | The scope determinations in `18` §3 | Same-session revalidation — `AASP-05` |
| 5 | `03` §6's multi-level compounding claim | `SUPPORTED INTERPRETATION` from recursion alone; no multi-level evidence was available |

## 5. AAS+ veto position

`ASSET_DR_CONTINUATION` carries an **AAS+ veto on starting any costing implementation**
until `BLK-07` is decided.

**AAS+ upholds that veto here, and extends its reasoning with P03 evidence:**
`02` §2 and `18` §4 together show that the reference product has neither an overhead
absorption model nor a correctly scoped rate object. Any implementation begun before
`BLK-07` would have to invent both, and would do so without the capacity denominator that
makes either meaningful.

**`AASP-VETO-01`: no P03 costing implementation may begin.** This is a continuation of the
Asset veto, not a new one, and it is not a Boss decision that this session can take or
lift.
