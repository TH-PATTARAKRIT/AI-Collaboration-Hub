# 03_CROSS_PXX_HANDOFF_AND_PROPAGATION_MATRIX

**Session** `[SMEPLUS-26-09-06-ACC-P06-P08-P09-P11-XRECON-001]` · branch `audit/account-xrecon-2026-09-06-001`

---

## 1. The correction-propagation law applied

A correction is **not** complete because one sentence changed. Every live carrier is traced:
source analysis · correction register · evidence register · validation table · summary · terminal report ·
handoff · peer receipt · downstream package · PMO pack · Boss decision pack · auto-resume state · checkpoint
register.

**Allowed states, and no state is skipped without evidence:**
`NOT STARTED` → `ORIGIN CORRECTED / PROPAGATION OPEN` → `PROPAGATED / RE-TEST OPEN` →
`RE-TESTED / FRESH CHALLENGE OPEN` → `FRESH CHALLENGE COMPLETE / VETO OPEN` →
`TECHNICAL EVIDENCE COMPLETE / AUTHORITY OPEN` → `AUTHORIZED CLOSED`

**No root defect in this package has reached `AUTHORIZED CLOSED`. None is beyond `TECHNICAL EVIDENCE
COMPLETE / AUTHORITY OPEN`.**

## 2. Cross-Pxx dependency edges, as measured

Direction is **producer → consumer**. Only edges evidenced on the frozen surfaces are listed.

| Edge | Vehicle | What crosses | Integrity at freeze |
|---|---|---|---|
| **P06 → P11** | `70_P06_P11_SUPPLEMENTAL_CRITICAL_RISK_HANDOFF.md`, `18_P06_CORE_RECON_HANDOFF_PACK.md` (both in `union_212.txt`:90, :83) | `om_data_remove` installed, unauthorised, reachable → `P11-B-21` `CRITICAL`, `T0-14`, `CI-12` | **Substance intact.** The wrong counts in the same files (`XRD-003`) **did not cross** — measured. **But the pin is stale** (`@249b7c2`, `XRD-005`) |
| **P08 → P11** | `58_P08_P11_RECONCILIATION_BOUNDARY_HANDOFF.md`, `54_…HANDOFF_PACK.md` | what the ledger can/cannot supply — 5 supplied, 8 not supplied; `HO-13`, `HO-14` | **DEFECTIVE.** Carries `IVR-F-16` (no-referent figure, **crossed** — `XRD-011`), `IVR-F-11` (malformed row), `IVR-F-13` (collided ids, **crossed** — `XRD-006`). Pin stale (`@194efcb`) |
| **P09 → P11** | `D25_P09_CHALLENGE_CORRECTION.md` | analytic position — 12 of 23 centres net exactly 0.00; gross **43×** net → `CI-11` | Substance received. **Pin stale at `@5441f8d`** — two generations behind `4778792` (`XRD-005`, `XRD-008`) |
| **P11 → P09** | P09's own reading of P11 | P09 **corrected** a false claim: *"P11 has published no branch"* **withdrawn in 3 files**; P11 **has** published, at CORR3 | **Corrected by P09 at `4778792`.** The correcting party was the consumer, not the producer |
| **P11 → P08** | `B-29` | blocked on `P08 AAS+-VETO-01` C-1 | **Open — correctly routed, not assumed** |
| **P11 → P07** | `19_P07_CORE_RECON_HANDOFF_PACK.md` | company-spanning tax-grouping scope ruling **routed to P11** | **NEVER OPENED — three rounds.** `B-36` HIGH. Inside the union, inside `ADDRESSED`, unopened |
| **P06 → P08 / P08 → P06** | `53_P06_P08_INTAKE_AND_DEPENDENCY_REFRESH.md`; `36_`:42-43 | P06 gates four items on *"P08's absence"* | **DEFECTIVE** — P08 was published and read in round 3; P06 requirement 7 |
| **P08 → P07 / P11 → P07** | `HO-14` vs `P07-F-02`/`F-03` | statutory register period bases; 5,228 entries | **UNRESOLVED — `B-39`.** May be two generations (`P07` says removed in v19; `HO-14`'s 5,228 is a `DB-SM` 16.0 count) |

## 3. Propagation matrix — root defect × carrier

`●` = defect present and live · `○` = carrier exists, defect **measured absent** · `—` = not applicable

| Root defect | Origin | Terminal report | Correction / evidence register | Validation table | Auto-resume | Checkpoint | Outbound handoff | Peer receipt | Boss / PMO pack |
|---|---|---|---|---|---|---|---|---|---|
| `XRD-001` P06 addendum totals | P06 IEV `b423eff` | **●** :14,:24,:30 | **●** :83 | — | **●** :22,:33,:43 | **●** :19 | — | — | **●** *(this prompt's own brief)* |
| `XRD-002` validation YES over 65 | P06 IEV | ○ | — | **●** `INSTRUMENT_CONTROL`:45 | ○ | ○ | — | — | — |
| `XRD-003` P06 count families | P06 src `1b018c1` | — | **●** `13_`:94,:95 · `40_`:288 | **●** `46_`:124 | — | — | **●** `18_`:214 · `70_`:108 | **○ P11 — measured absent** | — |
| `XRD-004` non-firing pattern | P06 src `56_`:99 | — | **●** `56_`:99 | — | — | — | — | — | **●** via `FTB-F-07` (1,752 dirs) |
| `XRD-005` stale peer pins | P11 `dc4cc4a` | — | — | — | **○ corrected (`B-37`)** | — | **●** `CANDIDATE_PACK`:18,:28,:29 | **●** `CONVERGENCE_REG`:28,:29,:30 | **●** inherited by gate pack |
| `XRD-006` `HO-` namespace | P08 `25_`/`54_`; P06 | — | — | — | **●** P11 :71 | — | **●** `54_`, `58_`, `25_` | **●** P11 :125,:129,:130,**:148**,:149 | **●** `BOSS_DECISION_MATRIX_CORR1`:34 |
| `XRD-007` requirement cross-ref | P08 IEV `bd95d1d` | ○ | **●** :317, :339 | — | ○ | ○ | — | — | — |
| `XRD-008` `B-38` premise | P11 `dc4cc4a` | — | **●** `CORR3_POPULATION_REGISTERS`:83 | — | **●** :71 | — | — | — | **●** one of 35 open blockers |
| `XRD-009` independence | both IEV tracks | **●** both | — | — | **●** both | — | — | — | **●** reserved to Boss |
| `XRD-010` unchallenged surfaces | P06 / P09 / P11 | **●** ×3 | — | — | **●** P09 `M-2`; P11 item 7 | — | — | — | **●** ×3 |
| `XRD-011` no-referent figure | P08 `58_` §1 | — | **●** P08 `58_`:13 | — | — | — | **●** `58_` → P11 | **●** P11 :124, :106, **:15 (`F-02`)** | **●** `CI-01` in gate pack |

## 4. Peer packages that consumed superseded information

| Consumer | Consumed | At | Superseded by | Consequence |
|---|---|---|---|---|
| **P11** | P06 handoffs | `249b7c2` | `1b018c1` → and the IEV's 25 defects **on `1b018c1` itself** | `XRD-005`. **Note: `1b018c1` is not a clean target either** — it is the surface the P06 IEV found 25 defects in |
| **P11** | P08 boundary handoff | `194efcb` | `00ccd66` → and the IEV's 17 defects **on `00ccd66`** | `XRD-005`, `XRD-011` |
| **P11** | P09 challenge correction | `5441f8d` | `92de8a1` → **and substantively `4778792`** | `XRD-005`, `XRD-008` |
| **P11** | P08's *"3 at 1e-7"* | `00ccd66` | `IVR-F-16` — exact Decimal gives **0 at every tolerance** | **`XRD-011` — P11's `F-02` falsification and a derived method rule both rest on it** |
| **Boss** | P06 IEV totals | this prompt's §2 brief cites **25 / 2 / 19** | the P06 **terminal report** still publishes **18 / 15** | `XRD-001` — **the Boss is reading a figure the package's own terminal report contradicts** |

## 5. The one propagation edge that has never been opened

**`19_P07_CORE_RECON_HANDOFF_PACK.md`** — inside P11's union of 212, dispositioned `ADDRESSED`, and
**never opened at any SHA across three rounds** (`B-36`, HIGH). It is titled *"CORE ACCOUNTING RECONCILIATION
HANDOFF PACK"*, its terminal state reads *"READY FOR CORE ACCOUNTING RECONCILIATION"*, and it carries a
**company-spanning tax-grouping scope ruling routed to P11**.

P11's own CORR4 ordering places it at item 6 — **after** five instrument repairs. This session does not
re-order P11's work, but records the exposure plainly: **an unopened inbound artefact is the one class of
defect that no amount of re-measuring the opened ones can detect.** `P07` is READ-ONLY here under §6 of the
governing prompt and is **routed, not opened**.

## 6. Propagation state summary

| Root defect | Current state |
|---|---|
| `XRD-001` | ORIGIN CORRECTED / PROPAGATION OPEN |
| `XRD-002` | NOT STARTED |
| `XRD-003` | NOT STARTED |
| `XRD-004` | NOT STARTED |
| `XRD-005` | ORIGIN CORRECTED / PROPAGATION OPEN |
| `XRD-006` | NOT STARTED (cross-Pxx) · ROUTED (P08-internal) |
| `XRD-007` | NOT STARTED |
| `XRD-008` | NOT STARTED |
| `XRD-009` | TECHNICAL EVIDENCE COMPLETE / AUTHORITY OPEN |
| `XRD-010` | PROPAGATED / RE-TEST OPEN (P09) · NOT STARTED (P06, P11) |
| `XRD-011` | NOT STARTED — **and unregistered by its consumer** |
