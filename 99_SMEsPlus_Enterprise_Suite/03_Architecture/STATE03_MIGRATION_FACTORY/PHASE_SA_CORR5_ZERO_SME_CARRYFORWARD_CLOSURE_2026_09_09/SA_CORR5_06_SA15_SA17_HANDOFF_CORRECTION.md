# SA_CORR5_06 — `SA15` / `SA17` HANDOFF CORRECTION

## CP-SA-C5-60 — PRE-TEST HANDOFF DATA CORRECTED

Session: `[SMEPLUS-26-09-09-PHASE-SA-CORR5-ZERO-SME-CARRYFORWARD-001]`
Branch: `architecture/phase-sa-corr5-zero-sme-carryforward-closure-2026-09-09-001`
Workstream: **F** · Closes: **`C4-07-F-03`** and every other readiness over-grade found in the two
handoff artefacts.
Boss: **SOLE FINAL APPROVER**

---

## 1. Method — supersede, never overwrite

The historical `SA15` and `SA17` (`PHASE_SA_CROSS_MODULE_ASSURANCE_2026_09_08/`) are **untouched**.
Two controlled versions are published in this package with a supersession notice and every correction
marked `[CORR5]` with its basis:

| Historical | Controlled version | Governs |
|---|---|---|
| `SA15_END_TO_END_SCENARIO_REGISTER.md` | `SA15_END_TO_END_SCENARIO_REGISTER_CORR5_CONTROLLED.md` | this package |
| `SA17_PRE_TEST_MATRIX_HANDOFF_BASELINE.md` | `SA17_PRE_TEST_MATRIX_HANDOFF_BASELINE_CORR5_CONTROLLED.md` | this package |

The programme's *a-revision-log-is-not-a-correction* rule is applied in the only way that also honours
*historical artefact superseded, not overwritten*: **the correction is in the controlled text, on the row
that names the identifier, and the historical text remains readable as evidence of `C4-07-F-03`.**

---

## 2. Every correction, with its basis — reconciled against CORR2, CORR3 and CORR4

| # | Artefact · row | Was | Now | Basis | Class of defect |
|---:|---|---|---|---|---|
| 1 | `SA17` §2 row 18 `E2E-15` | `TRAVERSABLE` · expected evidence *"idempotent retry; ordering-independent reconciliation"* · bounded risk *"Strongest established area"* | `WITH NAMED BREAK` · expected evidence: reversal event referencing the original (established); **retry and duplicate detection may not be expected until built** · risk: *weakest proven area*; **raised to a dependency gate** | `C4-07-F-03`; `SA_CORR2_09` §3 idempotency `NOT ESTABLISHED`; `SA_CORR3_06` scenario 22 `HOLD`; `SA_CORR5_01` `specified, not built, not verified` | **unsupported readiness upgrade** — a grade resting on a superseded citation |
| 2 | `SA15` §2 row `E2E-15` | `TRAVERSABLE` — *"strongest area: idempotency and ordering-independence established (`SA09`)"* | `WITH NAMED BREAK`; break = element 15 | same | same |
| 3 | `SA15` status line and §4 | *4 traversable (E2E-02, -11, -12, -15)* | **1 traversable (E2E-02)**; 15 with named break; 2 not traversable — **E2E-11/-12 regraded after self-challenge `CHB-03`**: the class table admits no route/value split, and `SA_CORR5_10` grades the same flows Boss-gated on `JT-05` | rows 1–2, 10 | consequential |
| 4 | `SA15` §4 check line | *"4 + 7 + 7 = 18"* over a table enumerating 13 identifiers with printed counts 4/7/2 | **1 + 15 + 2 = 18**, all 18 identifiers enumerated | `JCP3-F-11` (CORR3, `MINOR`, never applied) | **a self-check that was false as written** |
| 5 | `SA15` §2/§3 `E2E-05`, `-08`, `-16`, `-17`, `-18` | `NOT TRAVERSABLE` in the row text (the header's supersession block said otherwise) | `WITH NAMED BREAK` in the rows themselves, with the named break stated | `SA_CORR2_01` §4.3; `SA_CORR2_03` §3.1–3.3 | **revision-log-not-correction** — the supersession block corrected the summary and not the rows |
| 6 | `SA17` §2 rows 2, 5, 6, 9, 10 (`E2E-05`, `-08`, `-16`, `-17`, `-18`) | `NOT TRAVERSABLE` | `WITH NAMED BREAK`, inputs updated (Boss elections named; `XMC-C-C2` specified; `SA_CORR3_04` 9 of 12) | same | same, propagated to the consumer that never received it |
| 7 | `SA17` §2 row 4 `E2E-07` | *"which level carries cost"* undetermined | costing level **resolved** (`SA_CORR3_02`, `C2-D-03` → 0 Boss decisions); resolution point remains | CORR3 | stale input |
| 8 | `SA17` §2 row 1 `E2E-01` | *"price and credit determination (SA-D21); the accounting fact that blocks cancellation (`XD-01`)"* | executed at `SA_CORR3_13` / `SA_CORR3_01`; residual **Boss elections** `TV6-BOSS-01`/`-02`, `XD1-P1` | CORR3 | stale input → correctly attributed to Boss |
| 9 | `SA17` §2 row 7 `E2E-03` | fixed-overhead injection path absent | chain studied (`SA_CORR3_03`); residual Boss restatement `B-6` | CORR3 | stale input |
| 10 | `SA17` §2 rows 16–17 and `SA15` rows `E2E-11`/`-12` | `TRAVERSABLE`, *"—"* (no inputs) | **`TRAVERSABLE WITH NAMED BREAK`**; `JT-05` Boss election; return basis conflict `PENDING` | `SA_CORR3_06` rows 8–9; `SA_CORR5_10` §3; `CHB-03` | **a `TRAVERSABLE` grade carrying an undecided accounting value** — the first freeze of this file kept the grade and was corrected |
| 11 | `SA17` §2 row 14 `E2E-13` | *"normal vs abnormal scrap; cost causality"* undetermined | scrap **classes specified** (`SA_CORR5_07` §3.3); cost causality = COGS residual | CORR5 | partial closure |
| 12 | `SA17` §3 control row *"Same-event retry is idempotent…"* | listed as a control to exercise | **testable only after element 15 is built**; until then a specification, not a control | `SA_CORR5_01` §9 | **a specification listed as a control** — `ND-06`'s own rule applied to the register that states it |
| 13 | `SA17` §1, §7 | no readiness vocabulary | **mandatory reading rule added** — `TRAVERSABLE`/`SA CONTRACT COMPLETE` = *a test can be written*; idempotency never low-risk on a carrier's existence; isolation/idempotency/joins untestable until built | master prompt §9 | principle |
| 14 | `SA17` new §2a–§2c | absent | dependency order (`MTI-50` → `CF-I-03`; instrument controls first), the three prohibitions verbatim, the runtime-obligation registers | `SA_CORR4_07` §5.1–5.2; CORR5 workstreams | **the three things CORR4 §9 said Pre-Test must inherit, now inherited** |
| 15 | `SA17` §3, §4, §6 | — | three controls added (`MTI-33`, `CF-I-03R`, `MTI-29`/`TRG-02`); `ND-09`, `-10`, `-11`, `-12` carried in; **`ND-13`, `-14` added** *(first draft numbered them `ND-12`/`-13`, colliding with CORR2's `ND-12` — `CHB-01`)*; bounded risks gain element 15 and the COGS residual | CORR2/CORR5 | completion |
| 16 | `SA_CORR4_07` §5 row *"Element 15 — must not be written"* | a prohibition on writing the case | **may be written, may not be executed or read as passing** until built — the object is now specified | `SA_CORR5_01`; `CHA-14` | reading corrected, prohibition's executable half unchanged |

**16 corrections; 2 artefacts; 0 historical bytes changed.**

### 2.1 Reconciliation sweep for other over-grades — what was tested and not changed

| Claim in `SA15`/`SA17` | Tested against | Result |
|---|---|---|
| `E2E-02`, `-11`, `-12` `TRAVERSABLE` | `SA_CORR2_01`, `SA_CORR3_06` rows 1, 8, 9 | **Routes traverse** on evidence; **values** for 8/9 carry `JT-05`/return-basis — corrected as inputs (row 10), grade retained |
| `SA17` §7 *"nine Account interfaces `READY-WITH-DELTA`"* | `SA13` §4; CORR2 `SA_CORR2_00` | grade unchanged; **reading rule added**: deltas are named, not closed |
| `SA17` §6 *"58 invariants specified, 0 proven"* | `SA_CORR4_06`, `SA_CORR5_10` §4 | true; **kept, with the reclassification pointer** |
| `SA17` §3 `XD-03` *"0 of 27,874 rows"* | historical, generation-qualified | kept |

---

## 3. Recalculated scenario readiness

| Register | Before | After |
|---|---|---|
| `SA15` traversable / named break / not traversable | 4 / 7 (table) — 12 (header) / 2 | **1 / 15 / 2** |
| `SA17` scenarios graded `TRAVERSABLE` with an undecided accounting value | 0 declared | **0** — `E2E-11`/`-12` regraded to `WITH NAMED BREAK` (`CHB-03`) |
| `SA17` scenarios inheriting an over-graded idempotency dimension | **18 of 18** (via `E2E-15`'s implicit gate) | **0** — the dimension is specified-not-built on all, stated once in §2b and enforced by the §2a order |
| Prohibitions travelling verbatim | 0 | **3** |
| Runtime-obligation register families attached (enumerated in `SA17` §2c) | 0 | **8** |

**Recalculation of the 22 joint cross-proof scenarios by dimension is at `SA_CORR5_10`**, which
consumes this file; the two registers here are the 18 end-to-end business scenarios.

## 4. Owner disposition

CORR4 recorded the correction owner as *"`SA15`/`SA17`'s owner, as a Phase SA act."* Phase SA is the
owner; this session is Phase SA; the act is performed. **No document-owner item remains on these two
artefacts.** The historical files carry no supersession pointer to this package — adding one would
overwrite historical bytes, which the master prompt forbids; the controlled versions are discoverable
from this package's manifest and from `SA_CORR5_15`'s evidence index.

## 5. Checkpoint

> ## `CP-SA-C5-60 — PRE-TEST HANDOFF DATA CORRECTED`
> **16 corrections across 2 controlled versions · `C4-07-F-03` closed · `JCP3-F-11` applied · 5
> propagation failures repaired at the row · 3 prohibitions and the dependency order now travel with
> the baseline · 0 historical bytes overwritten · `SA15`: 1 / 15 / 2 · corrected by `CHB-01`, `-03`,
> `-16`, `CHA-14`.**

No Evidence = No Progress. Never Skip Gate. Boss remains the sole Final Approver.
