# 08 — P04 PRIOR EVIDENCE RECONCILIATION

Layer: **2 — audit quarantine**.

The governing prompt requires prior Asset research to be imported as
**PRIOR EVIDENCE / PRIOR HYPOTHESIS / BOSS CONTROLLED DECISION / AUDIT LINEAGE**,
and forbids restarting it. This file records the import, and — more importantly —
records what **fell out of the registers between packages**.

---

## 1. Audit lineage

| Pkg | Package | Branch | Research commit | Head | Terminal wording |
|-----|---------|--------|-----------------|------|------------------|
| **P1** | Asset function deep research, 2026-09-03 | `audit/asset-function-deep-research-2026-09-03-001` | `57cdb99` | `57cdb99` | **BLOCKED — MATERIAL EVIDENCE REQUIRED** |
| **P2** | Asset deep research L1–L6, 2026-09-04 | `research/asset-deep-l1-l6-2026-09-04-001` | `6c7512e` | `78067d2` | **COMPLETE TO MAXIMUM AVAILABLE EVIDENCE — MATERIAL BLOCKERS REMAIN — READY FOR BOSS FINAL REVIEW GATE** |
| **P3** | Asset DR continuation L7→Final, 2026-09-04 | `research/asset-deep-continuation-2026-09-04-001` | `a852b6e` | `54db9e1` | **READY FOR BOSS FINAL GATE** |

P2's commit `6c7512e` is the **controlled baseline**. All three branches are
intact and unmerged. Jira issue `ERPPLUS-17` carries comments from P2 and P3 and
is **not** transitioned to done.

## 2. Boss-controlled decisions — imported verbatim, standing preserved

| ID | Decision | Standing after P3 | P04 position |
|----|----------|-------------------|--------------|
| **BD-01** | Internal equipment usage accumulation may be lower than, equal to, or higher than residual book value. **No cap. No automatic cut-off. No reduction of residual book value.** Usage may continue while the equipment remains operationally eligible. It is a management/control allocation concept and **must not silently alter** statutory depreciation, book value, carrying amount or accumulated depreciation unless separately authorised by a valid accounting event | **STANDING and reinforced** | **Supported by new evidence** — see `07` §4.3, P04-F-31. TAS 16 itself contemplates a zero charge on a fully depreciated asset still in use |
| **BD-02** | **Every depreciation period must be attributed 100 %.** No amount may remain permanently unclassified. Productive depreciation flows operation → order → work in progress → finished goods → cost recognition. Non-productive depreciation is assigned by cause. Unclassified depreciation is not carried forward | **STANDING as to destination; ambiguous as to method** | **Ambiguity now resolvable in a new way** — see `06` §7, a third compliant option. And **two new breaches of it by the reference behaviour** — P04-F-52 and P04-F-53 |
| **BD-03** | The work centre is not a generic averaging bucket. The routing/operation/equipment relationship must preserve actual operational meaning | **STANDING — structurally vindicated** | **Re-verified this session** — `05` §3, P04-F-37 |
| **BD-04** | Machine hour, work-centre hour and production quantity are the controlled candidates; one primary method per context unless evidence justifies multi-driver | **STANDING with one declared departure** awaiting Boss confirmation | Unchanged by this session |

**Three things `BD-01` does not decide**, carried forward open: the rate base for
the accumulator (three candidates, **none evidence-based**); re-entry after a
capital improvement; and terminal behaviour at disposal.

**One refinement raised against `BD-01`** and still open: the evidence permits a
stronger rule than "must not silently alter" — namely that the management ledger
must not alter statutory figures **at all**.

## 3. Statutory positions — imported, not re-researched

Imported unchanged from P3, all **FACT VERIFIED** from primary or standard text:
pro-ration from acquisition; statutory rates are **ceilings** not schedules;
TAS 2 ¶12 **requires** absorption; TAS 2 ¶13's four constraints; planned
maintenance sits **inside** normal capacity; the DBD prescribed statement forms
carry **no** off-balance line.

Imported as **HOLD**: the pro-ration **unit** being specifically the day;
Thai **tax** acceptance of absorbed depreciation; the TAS 16 **standard text**
(as distinct from the explanatory manual); the one-baht residual convention;
whether Thai tax permits **suspending** depreciation; the bookkeeping standing
of a memorandum ledger.

**Added by this session** (see `07` §4 and §5, and `13`): TAS 16 derecognition
criteria; TAS 16 on impairment, compensation and separate events; TAS 16 on
depreciation cessation and units-of-production; the Revenue Department
destruction instructions and their **scope**; the fixed-asset destruction ruling;
and the hire-purchase VAT instruction.

## 4. Blocker population — the reconciliation ruling preserved

P3 recorded that the two baseline documents of P2 **disagree** on the sixth
blocker: one names a terminating rule for the internal-usage accumulator, the
other names unabsorbed depreciation; and the first lists that second item in its
**non-blocking** tier, which is a self-inconsistency **inside P2**.

P3 carried **both**, giving **seven distinct items against six reported**.

> **That ruling is preserved unchanged.** A continuation must not re-derive a
> population of six from P2 alone. Recorded here so the ruling survives one more
> package boundary.

Inherited state: **7 distinct / 8 rows in P3's final register · 4 closed · 4
open.** The four open are the day convention on the live population; whether
several assets share one machine; the allocation denominator (`BLK-07`); and
whether maintenance splits into planned and unplanned (`BLK-08`).

## 5. **The handover residue — items that fell out of the registers**

This is the material governance finding of the import. Three groups of items
were **not closed** and **not carried**; they simply stopped appearing.

| Group | Items | Where last seen | Status now |
|-------|-------|-----------------|------------|
| **A — P2's preserved expert disagreements** | Seven of eight: capitalization absent-versus-partial; the revaluation boundary; whether to retire a piece of terminology; the severity of the unguarded confirm path; whether maintenance costing is a genuine differentiator; where machine identity should live; whether to report an internal scoreboard | P2's independent-challenge file | **NOT CLOSED, NOT CARRIED.** The eighth was escalated and resolved by `BD-01` |
| **B — the tax book** | Named in P2 as *"the largest single functional gap for a Thai deployment"*, with six tax scenarios shown impossible against statutory rates that are ceilings | P2 | **NOT CARRIED INTO P3 AS A BLOCKER AT ALL** |
| **C — P1's Thai retire-end holds** | Documentation requirements for disposal and write-off; tax treatment of gain on disposal | P1 | **DROPPED, NOT CLOSED** |

> **P04-F-58.** Between three packages that each declared lineage integrity,
> **at least ten registered items ceased to appear without being closed**. Each
> package's own lineage statement is true as written — no conclusion was deleted
> and none was promoted without evidence — and the residue still occurred,
> because a lineage statement about **conclusions** does not protect **open
> items**.
> Class: **FACT VERIFIED** from the registers themselves. Severity **High for
> governance**.

**Action taken by this session, rather than noted:**

| Group | Action |
|-------|--------|
| **C** | **Partly closed on new primary evidence.** `07` §5 establishes the destruction-evidence regime for fixed assets, its authority, and precisely what remains open. The gain-on-disposal tax item is **re-opened unchanged** as `P04-B-25` — this session did not research it, and says so |
| **A** | **Re-registered as open**, `12_P04_CONTRADICTION_REGISTER.md` §3. Two are advanced by this session's evidence: the capitalization absent-versus-partial dispute is settled by `01` (**partial** — one automatic path exists, and the dispute was about whether to call it that), and the revaluation-boundary dispute is settled by `07` §4.1 (**four of seven TAS 16 derecognition requirements have no host**) |
| **B** | **Re-registered as a blocker**, `P04-B-13`. It is not a P04 finding — it is a P08 one — but it must not vanish a second time |

## 6. Corrections this session makes to prior evidence

| ID | Prior statement | Correction | Class |
|----|-----------------|------------|-------|
| **P04-REV-01** | The reference population is **797 modules** — stated in three packages and by two research streams this session | It is **797 entries / 791 directories / 790 installable modules**. No negative finding changes; the denominator does | FACT VERIFIED |
| **P04-REV-02** | *"Two live mechanisms carry machine cost, and a third is proposed"* | **Nine distinct paths** exist under a declared enumeration. The veto's second limb is **wider**, not narrower | FACT VERIFIED |
| **P04-REV-03** | *"Depreciation already reaches production cost centres through the analytic distribution"* — one of the two live mechanisms | **It nets to zero.** Both entry lines carry the distribution and the analytic amounts cancel | FACT VERIFIED |
| **P04-REV-04** | The custom asset-to-equipment module has **two** unimported model files (P3's correction of P2's one) | **Three** are unimported | FACT VERIFIED |
| **P04-REV-05** | Company-optional master data across four object classes is a multi-tenant-safety failure | **Narrowed** under the scope-aware correction: a defect for the work centre, **not** a defect for the machine register | See `20` §4.1 |
| **P04-REV-06** | The upward-traversing visibility rule is a SaaS-security defect | **Re-classified**: certainly a company-scope accounting-visibility defect; a tenant-security defect **only if** hierarchies span tenants — which P04 cannot determine | See `20` §4.2 |

## 7. What this session deliberately did **not** re-test

Preserved at their prior classification, and stated so that the omission is
visible rather than silent: the 280 / 217 / 16 population figures; the custom
Thai depreciation method existing only on the legacy generation; the numerical
equivalence of the two depreciation arithmetics; the stored-versus-posted
disposal gain divergence (re-confirmed only as to its cause); the absence of a
monetary field on a maintenance request; and the whole of the depreciation-board
algorithm, which P2 established from primary source and which P04 has no reason
to re-derive.
