# 37 — G02-P02 RISK / BLOCKER / TZ / CONTRADICTION RECONCILIATION

`LAYER 2 — AUDIT QUARANTINE.` Task **C8**. Baseline `ff8be51`.

**Populations are re-derived, not inherited.** Every family below was enumerated mechanically at this
baseline. **A live defect is not closed by having been measured. A blocker closes only when its own
stated closure condition is satisfied.**

---

## 1. Re-Derived Identifier Populations

| Family | Population | Contiguity |
|---|---|---|
| `C-` contradictions | **33** | C-01 … C-33, no gaps |
| `RE-` revisions | **27** | RE-01 … RE-27, no gaps |
| `SC-` source/population controls | **19** | no gaps |
| `SF-` scope findings | **9** | no gaps |
| `TZ-` tolerance-zero | **8** | no gaps |
| `TC-` targeted-closure | **40** | no gaps |
| `EC-` exit criteria | **8** | no gaps |
| `P02-F-` findings | **53** | no gaps |
| `EV-P02-` evidence | **127** | **no gaps** — verified with the instrument that reads both the register's bare `\| NNN \|` rows **and** the full `EV-P02-nnn` form |

**Instrument note, recorded because it has now misfired twice.** A full-form-only regex reports
**7 phantom gaps** (`3, 27, 34, 69, 108, 109, 110`) because the register's own rows are bare three-digit
numbers. **The register is contiguous; the naive instrument is not.**

**`RE-28` — an identifier collision found and corrected this round.** The design candidates first issued
in `38` as `DC-1` … `DC-6` collided with the package's existing two-part scheme (`DC-08-02`, `DC-11-01`,
…). Renamed to **`DC-38-01` … `DC-38-06`** to conform. **A new family invented beside an existing one is
a defect even when every individual row is correct.**

---

## 2. Tolerance-Zero — Re-Derived Disposition

| TZ | Statement | Re-derived status this round |
|---|---|---|
| **TZ-01** | Completed outflow with no financial record | **QUESTION ANSWERED — RISK LIVE.** Widened decisively: `SF-F` shows **47,242 valuation layers with 0 accounting entries** in `551ab874`, against a spread reaching 100%. Not closed. |
| **TZ-02** | Locked-period posting silently redirected, capped at today | **QUESTION ANSWERED — RISK LIVE, NOT CURRENTLY FIRING.** See TZ-07: the control it subverts is deployed almost nowhere. |
| **TZ-03** | Matching/unmatching not period-controlled | **as TZ-02** |
| **TZ-04** | A context sentinel disables the lock check, including the irreversible lock | **UNMEASURABLE FROM DATA — code-path bypass.** Now sharper: **`hard_lock_date` is set on 0 of 127 company records**, so the irreversible lock this sentinel can disable **is used by nobody**. |
| **TZ-05** | Missing rate silently substitutes 1.0 | **DEMONSTRATED, nil effect measured.** RISK LIVE. |
| **TZ-06** | Customer deposit recognised as revenue when a property is unset | **CONFIRMED LIVE DEFECT.** Unchanged. |
| **TZ-07** | The deployed estate has no period control | **RE-DERIVED AND STRENGTHENED — see §3.** |
| **TZ-08** | Valuation ledger and GL disagree, undetected, by up to 9×10¹⁶ | **QUESTION ANSWERED — RISK LIVE.** Routed to P08. |

**0 of 8 tolerance-zero items eliminated.** Two were widened this round (TZ-01, TZ-07). **The criterion
has moved further from satisfaction, not closer** — which is the honest direction given what was found.

## 3. `P02-F-37a` — TZ-07 Re-Derived On The Full Population

Previously published as *"91 of 93 company records carry no lock date"*, on the then-population.
Re-measured across **all 17 databases**:

| Measure | Result |
|---|---|
| Company records, all databases | **127** |
| With a fiscal-year lock date | **6 (4.7%)** |
| With a tax lock date | **6** |
| **With a hard (irreversible) lock date** | **0 — in every database where the column exists** |

**121 of 127 company records carry no fiscal-year lock, and not one company anywhere uses the
irreversible lock.** The earlier figure held its direction and its denominator grew by 37%. `hard_lock_date`
does not exist before 18.0, so its zero is measured only where the column exists — stated rather than
averaged away.

---

## 4. Blockers — Exact Remaining

| ID | Item | Class | Closure condition |
|---|---|---|---|
| **B-1** | `C-04` cost-of-sales idempotency | **BLOCKED — BOSS AUTHORISATION** | One authorised run per `33` §5. Read-only routes exhausted **and evidenced** (`P02-F-33a`). |
| **B-2** | Behaviour of **189** P02-relevant installed modules with no readable source | **SOURCE GAP** | Obtain the deployed addons for `inherit_sales`, `inherit_inventory` and the `cu_*`/`cff_*` estate. **No conclusion may be drawn until then.** |
| **B-3** | Six of eight scenario negatives still single-instrument, v18/v19 only | **EVIDENCE REQUIRED** | A disjoint second instrument per `35` §6. |
| **B-4** | Whether 14.0 enforces its 1,204 configured credit limits | **EVIDENCE REQUIRED** | `P02-F-35a`. The v18/v19 negative does not transfer. |
| **B-5** | Value (not quantity) of the delivered-not-invoiced position | **EVIDENCE REQUIRED** | Cost basis governed by unreadable custom code. |
| **B-6** | Revenue: billing vs performance | **BOSS DECISION** (`BP-03`) | Boss ruling. P02 supplies `P02-F-34b`. |
| **B-7** | Three scope holds — currency rate, chart of accounts, intercompany execution | **PEER-OWNED — P11** | P11 convergence. |
| **B-8** | Thai VAT/WHT statutory treatment | **STATUTORY** | P07 + statutory source. |

**No unnamed `OPEN` remains.**

## 5. Specially Reconciled Items Required By C8

| Item | Status |
|---|---|
| **C-04** | `BLOCKED — BOSS AUTHORISATION`. Reclassified from evidence-absence by `L-01`/`L-03`. |
| **Period-lock controls** | §3. Live, and unused in the estate. |
| **Missing-rate behaviour** | TZ-05 demonstrated; nil measured effect; risk live. |
| **Customer advance / deposit** | TZ-06 confirmed live defect. |
| **Valuation ↔ GL divergence** | TZ-08 live; `SF-F` adds a second, larger instance. Routed P08. |
| **Physical completion without financial effect** | TZ-01, `SF-F`, `P02-F-34c`. **Live across generations.** |
| **Source-scope negatives** | **Materially restricted.** `31` §4: every source-derived negative is inapplicable to the 1.7M-line v14 deployment; `35` §2 withdraws `N-1` for 14.0/16.0. |
| **Revenue/cost period mismatch** | `RE-18` direction stands; `P02-F-34b` adds that **billing ahead of delivery dominates** in the Thai deployments. Routed P10. |
| **Return / credit-note independence** | `36` stages 10–11: not linked, not enforced. P02 retains. |
| **Payment / bank / reconciliation separation** | `P02-F-43` widened by `CA-04`. Routed P06. |

## 6. Contradictions — Disposition

All **33** carry a disposition and preserved lineage. The two raised this round:

- **`C-33`** — the package asserted a guard in `00` §3b and its absence in `22` §13 and published both.
  **Corrected in place; four sibling statements verified as still correct.**
- **`RE-27`** — a boolean predicate that could not fire, caught by a positive control, which changed
  scenario 8 from "no deployed population" to **9 templates across 3 deployments**.

**Both were self-found in this round, and both were instrument defects rather than reasoning defects** —
consistent with the pattern this package has recorded since `RE-13`.
