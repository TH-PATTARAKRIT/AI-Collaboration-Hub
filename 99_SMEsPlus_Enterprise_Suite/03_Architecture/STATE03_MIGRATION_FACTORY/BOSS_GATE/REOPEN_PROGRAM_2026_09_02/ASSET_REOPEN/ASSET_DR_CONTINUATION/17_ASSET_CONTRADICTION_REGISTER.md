# 17 — CONTRADICTION REGISTER (LEVEL 19)

**LAYER 2 — AUDIT QUARANTINE.**

Every contradiction carries evidence, severity, affected architecture, resolution path
and remaining uncertainty. The nine challenge questions the prompt names are each
answered in §3, including the ones whose answer is "the challenge fails".

**Independence declaration.** This attack was executed by the same session that produced
the findings it attacks. That is a real limitation and is not dressed up: a reviewer
should treat §3's self-defences with more suspicion than §2's inherited contradictions.
No human review has occurred.

---

## 1. Inherited contradictions — status

The six from `LIN-02` (`37_CONTRADICTION_REGISTER.md`), re-assessed.

| ID | Contradiction | Prior severity | Now |
|---|---|---|---|
| `CTR-01` | The configured depreciation method has no verified implementation on the target generation | High | **Open, unchanged.** Reduced by reproducibility-through-configuration; closes with `BLK-01` |
| `CTR-02` | The link module's disposal behaviour does not execute | Medium; High as a class | **Open, and widened.** Three model files are also dead, and the claim mechanism is a one-way ratchet (`16` §3) |
| `CTR-03` | On the legacy generation, daily depreciation and the machine link were attached to **two different asset records** — no single record ever had both | Medium | **Open, unchanged.** Still the most under-appreciated item in the package |
| `CTR-04` | Confirming an asset silently changes an operational record, with no way back | Medium | **Open, and worse.** "No way back" is now verified as literal: nothing anywhere resets the status |
| `CTR-05` | The posted disposal gain and the stored gain can differ by the residual | Low in the ledger; Medium for readers | **Open, unchanged** |
| `CTR-06` | The rule guaranteeing a schedule closes to zero is enforced by the application only, and the live data was bulk-loaded | Medium | **Open, unchanged.** Closes only with a data check on the UAT |

## 2. New contradictions found this session

### `CTR-C-01` — `BD-01` says "must not silently alter"; the evidence permits a stronger rule

| | |
|---|---|
| Evidence | The off-balance firewall (`05` §7) makes any statutory alteration by the management ledger structurally impossible within a journal entry, at no cost |
| Severity | **Low** — it strengthens the decision rather than opposing it |
| Affects | `10` §5, `19` §6 |
| Resolution | Adopt the stronger form: the management ledger must not alter statutory figures **at all**. Recommended for Boss confirmation |
| Remaining uncertainty | None |

### `CTR-C-02` — 100% attribution and TAS 2 ¶13 conflict under the obvious reading

| | |
|---|---|
| Evidence | TAS 2 ¶13 standard text versus the naïve reading of `BD-02` set out in `09` §2 |
| Severity | **High** |
| Affects | `09`, `11`, `13` — the whole costing model |
| Resolution | The normal-capacity reading in `09` §3 satisfies both. **`BLK-07`** |
| Remaining uncertainty | Whether the Boss intends that reading. The instruction is genuinely ambiguous and cannot be resolved by evidence |

### `CTR-C-03` — `BD-02` treats MAINTENANCE as one cause; TAS 2 ¶13 requires two

| | |
|---|---|
| Evidence | Normal capacity is defined to take account of capacity lost to **planned** maintenance; unplanned is not mentioned and falls to the unallocated-overhead rule |
| Severity | **Medium** |
| Affects | `09` §4, §6; `12` §5 |
| Resolution | Split the cause. The data already exists (`06` §4). **`BLK-08`** |
| Remaining uncertainty | None mechanical; a Boss confirmation only |

### `CTR-C-04` — `BD-04` requires one driver; the standard requires two

| | |
|---|---|
| Evidence | TAS 2 ¶13 prescribes normal capacity for fixed overhead and actual use for variable overhead |
| Severity | **Medium** |
| Affects | `11` |
| Resolution | One driver **per cost class**, configurable within the variable class. Declared as a departure in `04` and `11` §4 |
| Remaining uncertainty | Boss acceptance of the departure |

### `CTR-C-05` — Off-balance accounts are selectable, and not postable, on the costing path

| | |
|---|---|
| Evidence | The work-centre expense account has no exclusion domain (`16` §2 row 17); the firewall constraint refuses the resulting entry (row 16) |
| Severity | **Medium** — the failure surfaces at manufacturing-order completion, not at configuration |
| Affects | `05` §8, `19` §7 |
| Resolution | Apply the asset module's exclusion domain to every account selector on a costing object |
| Remaining uncertainty | The user-visible failure mode is `SOURCE-SUPPORTED INTERPRETATION`; it follows from three verified facts but was not executed |

### `CTR-C-06` — The rate snapshot exists and is not used by the paths that matter

| | |
|---|---|
| Evidence | `16` §2 rows 18–20 |
| Severity | **Medium-High** for design |
| Affects | `08` §5, `13` §3 |
| Resolution | Either the snapshot is authoritative or it does not exist. Do not carry a field nothing consumes |
| Remaining uncertainty | None |

### `CTR-C-07` — The labour ledger entry is dated at posting, not at production

| | |
|---|---|
| Evidence | `16` §2 row 22 |
| Severity | **High for period integrity** |
| Affects | `13` `T-02` |
| Resolution | The costing entry carries the costing period's date, and is refused if that period is locked |
| Remaining uncertainty | None |

### `CTR-C-08` — Cancellation deletes allocation records in the same product that never edits a depreciation entry

| | |
|---|---|
| Evidence | `16` §2 row 25 versus row for the depreciation reversal discipline |
| Severity | **Medium** |
| Affects | `15` `EC-19`, `19` §7 |
| Resolution | Reversal only, never deletion |
| Remaining uncertainty | None |
| Note | The interest is that **one product holds both disciplines**. Copying "the reference product's approach" without saying which part is copied would import the wrong one |

### `CTR-C-09` — Machine cost reaches inventory only under two of three costing methods

| | |
|---|---|
| Evidence | `16` §2 rows 21 and 23 |
| Severity | **High if unnoticed** |
| Affects | `08` §3, `12` §2 |
| Resolution | SMEsPlus must state explicitly, per costing method, whether conversion cost enters inventory — and under TAS 2 it must, for all methods. A standard-cost product whose standard omits machine cost is understating inventory |
| Remaining uncertainty | None |

### `CTR-C-10` — Company-optional master data contradicts the no-cross-tenant requirement

| | |
|---|---|
| Evidence | `14` §2, §4 |
| Severity | **High for SaaS** |
| Affects | `14` §5, `19` §8 |
| Resolution | Mandatory company on every costing record; tenant isolation above the application |
| Remaining uncertainty | Whether the pilot data contains company-less equipment or work centres — a UAT question, added to `22` §4 |

## 3. The nine challenge questions

**Q1 — What if the Boss's assumption is wrong?**
Tested individually. No Boss assertion about the **business** was contradicted. Two
carry implicit technical assumptions the evidence does not support: that daily
computation is the system default (it is not — `05` §3), and that the daily *unit* is a
legal requirement (pro-ration is; the unit is practice — `18` §4). Two decisions need
extension for statutory reasons: `CTR-C-02`, `CTR-C-03`. **The Boss's business model
survives the attack; two mechanism assumptions do not.**

**Q2 — What if the reference behaviour is configuration-specific?**
Substantially true, and it is the reason `BLK-01` still blocks. Three behaviours are
configuration-dependent and change the answer: the day convention, the product costing
method (`CTR-C-09`), and the valuation mode. **A finding stated without naming its
configuration is not a finding**, and this package names the configuration wherever one
applies.

**Q3 — What if historical journal behaviour differs from the current setup?**
Unresolvable without the UAT. `CTR-06` stands: the schedule-closes-to-zero invariant is
enforced by the application, and the live data was bulk-loaded through an import path
that bypasses it. **Migrated data cannot be assumed to satisfy an invariant that was
never applied to it.**

**Q4 — What if source and UI disagree?**
They do, and it is recorded: seven misleading labels in the baseline, of which the day
convention is the dangerous one. This session adds `CTR-C-06` — a field whose *name*
promises a snapshot and whose *consumers* ignore it. **Source was treated as
authoritative throughout; the UI was treated as a hypothesis about source.**

**Q5 — What if the accounting standard differs from operational convenience?**
It does, decisively, and this is the session's main result. Operational convenience says
divide the month's depreciation across the month's hours. TAS 2 ¶13 forbids it.
**The standard wins; `09` §3 is the reconciliation.**

**Q6 — What if management cost allocation is mistakenly posted into the statutory GL?**
Structurally prevented **within a journal entry** by the firewall. **Not prevented
through a valuation field** — `15` `EC-27` second limb. This is the residual leak and it
is the one a reviewer should press hardest, because the firewall creates a false sense
that leakage is impossible.

**Q7 — What if post-depreciation internal cost is double counted?**
Four independent grounds against, in `10` §10. Two are verified facts; two are
properties of the design and hold only if built as specified. The one case where double
counting is genuinely live is **re-entry** — a fully depreciated asset made depreciable
again while internal usage runs. `10` §7 suspends internal usage precisely there.

**Q8 — What if WIP already includes another machine-cost mechanism?**
**It does.** The existing chain absorbs `hours × typed rate` into WIP today. If SMEsPlus
adds a derived rate without removing or replacing that, every product carries machine
cost twice. And there is a second, quieter path: depreciation already reaches production
cost centres through the **analytic distribution** (`05` §4). **Two live mechanisms, and
a third proposed.** `19` §5 requires the design to state which single mechanism is
authoritative and to prove the others are off. This is the most likely way the project
produces a wrong number that reconciles.

**Q9 — What if manual adjustment destroys source traceability?**
It can, today: rate-bearing configuration changes with no audit trail; a sanctioned
import field can separate the sub-ledger from the ledger; and no reconciliation report
exists. `15` `EC-27` and `19` §7 specify system-controlled accounts, dated rate records
and a mandatory sub-ledger-to-ledger reconciliation.

## 4. Severity summary

| Severity | Count | IDs |
|---|---|---|
| High | 5 | `CTR-01`, `CTR-C-02`, `CTR-C-07`, `CTR-C-09`, `CTR-C-10` |
| Medium | 9 | `CTR-02`, `CTR-03`, `CTR-04`, `CTR-06`, `CTR-C-03`, `CTR-C-04`, `CTR-C-05`, `CTR-C-06`, `CTR-C-08` |
| Low | 2 | `CTR-05`, `CTR-C-01` |
| **Total open** | **16** | 6 inherited, 10 new |

None is resolved by assertion. Four close on the UAT, four on a Boss decision, and eight
are design rulings already specified in `19`.
