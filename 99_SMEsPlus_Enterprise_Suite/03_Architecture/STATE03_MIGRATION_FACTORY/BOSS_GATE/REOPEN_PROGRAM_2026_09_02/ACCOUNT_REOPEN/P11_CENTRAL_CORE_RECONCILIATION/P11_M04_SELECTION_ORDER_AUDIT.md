# P11 — C2 · `P11-M-04` PROGRAMME-WIDE SELECTION-ORDER AUDIT

`[SMEPLUS-26-09-05-ACC-P11-CORE-RECON-CORR1-001]` · CP-P11C02 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**
> **The prompt's instruction is explicit and is obeyed: do not assume `P11-M-04` only affects
> databases.**

---

## 1. The rule being applied

> **`P11-M-04`** — a declared scope register **bounds** the evidence and, in doing so, also **orders**
> it. If the register is consulted before the ranking, **the register *is* the ranking**, and its
> ordering was chosen for containment rather than relevance.

**Audit question, asked of every selection P11 made:** *did something other than a declared relevance
unit determine what P11 looked at first, or looked at at all?*

## 2. The seven ordering surfaces, audited

| # | Surface | Did it silently select? | Evidence |
|---|---|---|---|
| `S1` | **Database / dump order** | **YES — `P11-F-11`** | `find` traversal order chose the readability sample. Corrected at C1 §4 |
| `S2` | **Peer handoff order** | **YES — NEW, `P11-F-12`** | See §3. **The most consequential finding in this audit** |
| `S3` | **Branch enumeration order** | **NO** | `peer_intake.sh` enumerates *all* refs (`134`, then `140`) and declares the denominator before filtering. The pattern was defective once (`P11-E-12`) but the **population** was never ordering-selected |
| `S4` | **Directory / path-set order** | **NO, with a caveat** | P11's package path was self-chosen (`P11-F-01` records that the programme declared none), so no register ordered it. **But P11's own output path is one of seven divergent ones** — the absence of a register is why, not its ordering |
| `S5` | **Size ordering** | **YES, latterly** | Ranking by bytes was adopted at `eef2757` **and was itself unit-blind** until `P07` supplied the unit clause. Corrected at `7f701cd` |
| `S6` | **Module / installed-list order** | **NOT APPLICABLE** | P11 reads no reference source and enumerates no module list. Recorded so the negative is bounded rather than absent |
| `S7` | **Evidence-class order** (`PEER-PUBLISHED` before `PEER-WIP`) | **NO — and it is a positive** | The class rule excluded uncommitted peer work **on a declared principle** (no SHA ⇒ not citable), not on availability. A principled exclusion is not a silent ordering |

## 3. `P11-F-12` — peer handoff order silently selected P11's reconciliation depth

**This is the audit's real result and it is new.**

P11's synthesis was written when **0** peers had published. It then consumed peers **in the order they
happened to publish** — `P03`, `P04`, `P06` first, then `P07`. Four deltas were written against those
four. **`P01`, `P02`, `P05`, `P08`, `P09`, `P10` were never consumed at all** until this run.

> **Publication order — an ordering P11 did not choose and could not influence — determined which
> peers P11 reconciled against, how deeply, and therefore which of P11's own findings were
> corroborated or corrected.**

**The concrete distortion, now measurable.** `P08` — Record-to-Report, the process whose subject
*is* P11's core-ledger substrate — published late and was **never consumed**. It holds:

- the **declared root set** (22, independently reproduced) — the closure of the programme's standing
  enumeration defect, which P11 had been carrying as its top-ranked cheap Boss action (`D-1`);
- **`A VERIFIED ABSENCE` across all 22 roots** for the accounting-event identity — the exact claim
  P11 had been obliged to carry as class `C`;
- **no database constraint enforces the balance invariant in any of the 22 roots** — the strongest
  available form of P11's `SRP-03` / `T0-12`.

**P11 spent four deltas reconciling against three peers while the peer holding the answers to its own
top-ranked items had not published.** That is not a criticism of any session; it is the ordering doing
the choosing, exactly as `P11-M-04` describes, on the surface P11 did not think to audit.

**Corrective, and it is not "consume peers faster":**

> **`P11-G-04`** — where peers publish asynchronously, **rank the peer population by relevance to the
> consuming process's own open items before consuming any of them**, and record which peers are
> *unavailable* rather than merely *unconsumed*. An unpublished peer is a **declared gap**; a peer
> consumed only because it published first is an **undeclared selection**.

## 4. Findings whose evidence base was ordering-selected

| Finding | Ordering surface | Material? | Disposition |
|---|---|---|---|
| `P11-F-09` readability | `S1` | **No** — sample complete on the governing unit | restated at C1 §4 |
| `P11-F-11` | `S1`, `S5` | **Yes** | restated at C1 §4 |
| `P11_PEER_INTAKE_DELTA_01`…`05`, `07`…`10` | `S2` | **Yes — depth, not correctness** | No delta is withdrawn. Each is accurate over the peers available when written; **all nine are now bounded by `P11-F-12`** and superseded in coverage by C8 |
| `P11-B-13` (event-to-GL not reconciled against peer matrices) | `S2` | **Yes** | **Now actionable for the first time** — see C8 |

## 5. Position

| Measure | Result |
|---|---|
| Ordering surfaces audited | **7** |
| Surfaces where silent selection occurred | **3** (`S1`, `S2`, `S5`) |
| New findings | **1** — `P11-F-12`, peer handoff order |
| New governance positions | **1** — `P11-G-04` |
| Findings withdrawn | **0** |
| Findings bounded | **9 deltas + 2 findings** |

> **`P11-M-04` was published as a database lesson and is not one.** Its most consequential instance in
> P11's own package is **peer publication order**, which no participant chose and which determined the
> shape of four deltas.
