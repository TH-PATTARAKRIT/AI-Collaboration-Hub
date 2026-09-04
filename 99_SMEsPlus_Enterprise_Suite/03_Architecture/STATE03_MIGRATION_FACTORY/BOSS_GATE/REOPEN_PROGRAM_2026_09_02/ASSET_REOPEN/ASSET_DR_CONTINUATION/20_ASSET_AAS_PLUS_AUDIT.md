# 20 — AAS+ INDEPENDENT AUDIT (LEVEL 22)

**LAYER 2 — AUDIT QUARANTINE.**

AAS+ challenge across the thirteen required review areas. Each area receives one of
**PASS · FAIL · HOLD · VETO**, per §22. Consensus is not forced; where the audit
disagrees with the research it says so.

**Independence limitation, stated first because it qualifies everything below.** This
audit was performed by the same session that produced the work. It is a structured
self-challenge, not an independent review. No human and no separate agent has reviewed
this package. A reader should weight the verdicts accordingly, and should treat any
`PASS` below as "no defect found by the party that wrote it".

---

## 1. Verdicts

### Architecture integrity — **HOLD**

The four-truths separation is coherent and the entity model follows from evidence rather
than from taste. Two things prevent a clean verdict:

- The design depends on a **normal-capacity register that does not exist anywhere** in
  the reference product and has no proven precedent in this business. Its numbers will
  be estimates from day one.
- **`BLK-07` is unresolved.** The allocation arithmetic — the centre of the design — is
  awaiting a Boss reading of `BD-02`. Architecture cannot be called sound while its
  central computation has two candidate forms, one of which breaches the standard.

### Accounting integrity — **PASS, narrowly**

The statutory basis is now primary and specific: TAS 2 ¶12 requires the absorption, ¶13
prescribes the basis, the destination of the remainder and the high-output cap. The
model in `09` §3 satisfies all four. The off-balance boundary is established on primary
regulatory evidence.

**Narrowly**, because it rests on one standard text and one regulatory form obtained in
a single session, and because TAS 16's *standard text* was not retrieved — three
conclusions rest on TFAC's manual, which states on every page that it is not part of the
standard. Those three are correctly down-classified in `18` §4, and none is load-bearing
for the costing model.

### Inventory integrity — **HOLD**

`CTR-C-09` is not adequately answered. Machine cost enters inventory value only under
two of three costing methods and reaches the ledger only under one of two valuation
modes. `19` §7 rule 10 states the requirement; **the research does not establish how a
standard-costed product is to comply.** That is a real gap, and calling it a design
detail would be understating it.

### Manufacturing integrity — **PASS**

The measurement chain is understood at the level of individual objects. The
work-centre-as-cost-bucket hypothesis was challenged at its strongest, including the
statutory argument in its favour, and the rejection is reasoned rather than assumed. The
downtime taxonomy finding is genuinely useful and materially reduces what must be built.

### SaaS integrity — **FAIL**

Not a failure of the research, which found the vectors, but of the **current state** the
research describes. Company-optional master data on equipment, work centres, bills of
materials and operations, plus an asset rule that traverses to parent companies, is not
a multi-tenant-safe foundation. `19` §8 states the correct rules. Until they exist, any
statement that the platform is tenant-safe is unsupported.

`CTR-C-10` also carries an unmeasured exposure: **nobody has checked whether the pilot
data actually contains company-less equipment or work centres.** It is a two-minute
query and it is not in the blocker list. **The audit adds it** — `22` §4 `Q-05`.

### Data integrity — **HOLD**

Two unmeasured populations gate real decisions: the day convention across 280 assets
(`BLK-01`) and duplicate machine links (`BLK-02`). Additionally `CTR-06` stands — the
schedule-closes-to-zero invariant is application-enforced and the live data was
bulk-loaded through a path that bypasses it. **No data-quality check has ever been run
against the migrated assets.**

### Identity integrity — **PASS**

The asset↔machine link is correctly identified as the identity spine; uniqueness,
company alignment and bidirectionality are correctly treated as correctness
preconditions rather than hygiene. The one-way-ratchet finding is a genuine addition.

### Migration integrity — **HOLD**

`CTR-03` remains the most under-appreciated item in the whole programme: on the legacy
generation, daily depreciation and the machine link were attached to **two different
asset records**. **No single legacy record ever had both.** Any migration target
described as "the old system's asset, with its machine link, depreciating daily" is a
composite that never existed. This has been recorded twice now and has not yet changed
anyone's plan.

### Thai business reality — **PASS**

Improved materially this session. The statutory position rests on the standard text and
the regulator's own prescribed forms rather than on secondary commentary. Items that
remain practice rather than statute — most importantly the daily unit — are correctly
held.

### User fitness — **HOLD**

The design asks operators to record **which machine** they used. `19` §3 mitigates this
by defaulting where a resource group holds one machine. **The mitigation is untested and
unquantified:** nobody knows what proportion of this business's resource groups hold
exactly one machine. If most hold several, the capture burden is the project's largest
adoption risk and it has not been sized. **The audit adds this** — `22` §4 `Q-06`.

### Auditability — **PASS**

The period reconciliation as a hard gate, dated records for every rate, capacity and
assignment, reversal instead of deletion, and `OTHER` as a reported control rather than
a bucket — these together give a stronger audit position than the reference product
offers, and each is traceable to a specific finding.

### Clean-room compliance — **PASS**

Layer discipline is declared and observed. `19` and `25` are written in neutral domain
terms. Source was read for semantics; nothing was copied. The learning in `16` §4 is
expressed as business lessons, not implementations.

### Contradiction risk — **HOLD**

Sixteen open contradictions, five High. The most serious is not in the register's
severity column at all — it is `CTR-C-08`'s sibling, the **double-counting** exposure in
`19` §5: two mechanisms already carry machine depreciation into cost, a third is
proposed, and each reconciles against itself. **A design that double counts and
reconciles is worse than one that visibly fails.**

## 2. VETO

**One veto is issued.**

> **VETO — no implementation of the costing model may begin before `BLK-07` is decided
> and the single-mechanism condition in `19` §5 is proved.**

Reasoning. The two candidate readings of `BD-02` produce **different arithmetic in every
period**, and the wrong one breaches TAS 2 ¶13 while still satisfying the Boss's
100%-attribution instruction and still reconciling to zero. Building first and choosing
after would mean rebuilding the allocation engine, the period close and the
reconciliation. Separately, if a third mechanism is added while two live ones remain,
every product's cost is overstated and **no report in the design would detect it**.

The veto is on **implementation**, not on the research, the design work, or the Boss's
Final Gate review, none of which it obstructs.

## 3. Findings the audit raises against the research

| # | Finding | Severity |
|---|---|---|
| 1 | Standard-cost compliance under `CTR-C-09` is asserted as a rule but not designed | **Medium-High** |
| 2 | Nobody has checked the pilot data for company-less equipment or work centres | Medium — a two-minute query |
| 3 | The single-machine-per-resource-group mitigation is unquantified | Medium — an adoption risk, not a correctness one |
| 4 | `CTR-03`'s consequence for the migration target has been stated twice and acted on zero times | **High** |
| 5 | The internal-usage rate base (`10` §3) has no evidential basis at all — all three candidates are reasoned, none observed | Medium — correctly marked, but the Boss should know the choice is unaided by evidence |
| 6 | No data-quality check has ever been run against the 280 migrated assets | Medium |

## 4. Overall

| | |
|---|---|
| Areas assessed | 13 |
| PASS | 6 |
| HOLD | 6 |
| FAIL | 1 |
| VETO | 1, scoped to implementation start |

**AAS+ position: HOLD.**

The research is materially stronger than the baseline it continues, and two of the four
inherited blockers closed on primary statutory evidence rather than on argument. But the
central computation is awaiting a Boss reading, the multi-tenant foundation is
demonstrably unsafe as it stands, and the double-counting exposure is real and
undetectable by the design's own controls.

**Recommended terminal state: READY FOR BOSS FINAL GATE.** Not a freeze, not an
approval, not an authorisation to develop.
