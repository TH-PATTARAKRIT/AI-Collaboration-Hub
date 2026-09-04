# 02 — PRIOR RESEARCH LINEAGE REGISTER (LEVEL 7)

**LAYER 2 — AUDIT QUARANTINE.**

Purpose: establish the Evidence Lineage Map required by §5 Level 7. Every material
statement inherited from Levels 1–6 is re-classified here against the six permitted
classes. Nothing is promoted from interpretation to fact without new evidence.

Classes used, per the governing prompt:
`FACT VERIFIED` · `SOURCE-SUPPORTED INTERPRETATION` · `DESIGN CANDIDATE` ·
`BOSS CONTROLLED DECISION` · `UNRESOLVED` · `CONTRADICTED`

---

## 1. Lineage chain

```
57cdb99  ASSET FUNCTION DR (2026-09-03)
            │  worked from public documentation only
            │  self-recorded "no code or database access"
            ▼
6c7512e  ASSET DEEP L1–L6 (2026-09-04)      ← controlled baseline
            │  corrected the access claim; 46 deliverables from primary source
            │  5 prior conclusions confirmed · 4 corrected/split · 2 superseded
            ▼
THIS SESSION  ASSET DR CONTINUATION (2026-09-04)
               re-tested the baseline; 4 corrections issued (§4)
```

`57cdb99` is retained only as lineage. Where `6c7512e` superseded it, the
supersession stands and is not re-opened.

## 2. Re-tested inherited statements

Each row was independently re-derived from primary source in this session. "Method"
records how, not merely that.

| ID | Inherited statement | Method used to re-test | Result |
|---|---|---|---|
| `L-01` | The operation object carries no equipment reference | Read the full field list of the routing/operation model | **FACT VERIFIED** — the only resource reference is the work centre |
| `L-02` | Equipment attaches to the work centre, not to the operation | Read the manufacturing–maintenance bridge module in full | **FACT VERIFIED** — and refined: the relation is many-equipment-to-one-work-centre (`06` §2) |
| `L-03` | A maintenance record carries no monetary field | Field-scan of the maintenance models | **FACT VERIFIED** — re-confirmed; its only production effect is calendar blocking |
| `L-04` | Only three of 797 modules reference the asset record, none operational | Re-ran the exhaustive tree search | **FACT VERIFIED** (exhaustive negative, workspace-bounded) |
| `L-05` | The custom asset↔equipment link's disposal behaviour never executes | Read the module's package initialiser and the wizard file | **FACT VERIFIED** — and widened: **three model files** are also unimported (`16` §3) |
| `L-06` | The link's draft-only restriction does not apply | Searched the platform field engine for the attribute | **FACT VERIFIED** — the attribute does not exist in this platform generation |
| `L-07` | The link's display behaviour never fires | Searched the platform base model for the method | **FACT VERIFIED** — the method was removed from this generation |
| `L-08` | The link has no uniqueness rule | Read the module for constraints | **FACT VERIFIED, with a refinement** — no constraint exists, but a *soft* UI guard does (`06` §5). The refinement weakens neither the finding nor its consequence |
| `L-09` | Confirming an asset silently mutates the operational equipment record | Read the confirm override | **FACT VERIFIED** — re-confirmed |
| `L-10` | The engine offers two incompatible day conventions; 30/360 is the default | Read the field definition and the lifetime-days computation | **FACT VERIFIED** |
| `L-11` | On a 1.2m asset over 5 years, February differs by −8.00% and the full year by −0.05% | Independent arithmetic re-derivation (`08` §2) | **FACT VERIFIED as arithmetic**; the underlying engine transcription remains `SOURCE-SUPPORTED INTERPRETATION` |
| `L-12` | Production costing works end-to-end from a typed hourly rate | Read the whole cost chain from time log to cost of sales | **FACT VERIFIED, with two corrections** — see `§4 C-01`, `C-02` |
| `L-13` | The residual is protected for the whole running life | Read the depreciable-base computation | **FACT VERIFIED** |
| `L-14` | The product structurally forbids off-balance accounts on asset accounts | Read the account-selection domains | **FACT VERIFIED, and materially widened** — the platform forbids mixing off-balance and on-balance accounts in *any* journal entry (`05` §7). This is stronger and more useful than the inherited statement |
| `L-15` | Thai law requires pro-rating from the acquisition date; class rates are maximums | Carried from `LIN-02`'s statutory reading | **FACT VERIFIED** — carried, not re-fetched; not contradicted by the new statutory evidence |
| `L-16` | Whether the daily *unit* is legally required is practice, not statute | Carried | **UNRESOLVED** — unchanged |
| `L-17` | The custom Thai daily method and the platform's calendar mode agree within 0.03 baht | Carried | **SOURCE-SUPPORTED INTERPRETATION** — unchanged; rests on `EV-SIM` |
| `L-18` | No tax book, no impairment, no component depreciation, no capitalisation stage | Carried, spot-checked | **FACT VERIFIED** — and `18` §3 now establishes that the missing component depreciation is a **standard requirement**, not an optional feature |

## 3. Boss decisions carried as controlled decisions

| ID | Decision | Class |
|---|---|---|
| `BD-01` | Internal equipment usage accumulation has no cap, no automatic cut-off, and never reduces residual book value; it is a management/control allocation and must not silently alter statutory depreciation, book value or accumulated depreciation | **BOSS CONTROLLED DECISION** |
| `BD-02` | Every depreciation period must be attributed 100%. Productive depreciation flows Operation → WIP → FG → cost recognition. Non-productive depreciation is classified by cause (maintenance, breakdown, idle, no demand, setup, stoppage, other). Nothing carries forward unclassified | **BOSS CONTROLLED DECISION** |
| `BD-03` | The work centre is not a generic averaging bucket; the routing/operation/equipment relationship must preserve operational meaning | **BOSS CONTROLLED DECISION** (principle) |
| `BD-04` | One primary allocation method is selected per customer/configuration context unless evidence justifies a multi-driver model | **BOSS CONTROLLED DECISION** (constraint on `11`) |

Incorporation and consequences: `04_BOSS_DECISION_INCORPORATION.md`.

## 4. Corrections issued by this session against the baseline

Four. Each is a correction of a **mechanism** statement, none of a business
conclusion. All are preserved rather than silently overwritten.

### `C-01` — The hourly rate is snapshotted at **completion**, not at creation

`LIN-02` (`44` §T5) states the chain "copies the rate onto a work order when it is
created". It does not. The work-order rate field is written in the completion path
only, and the platform's own comment on the field says so explicitly: it stores the
work-centre rate *at the time of work order completion*.

**Severity:** Medium. It changes which design mitigation is needed — the exposure is
a rate change between the last time log and completion, not between order creation
and execution.

### `C-02` — Valuation and the ledger entry **ignore** the snapshot and read the live rate

Stronger than `C-01` and not previously recorded. The cost function used by both the
finished-goods valuation path and the labour ledger entry multiplies logged duration
by the **work centre's current** hourly rate, not by the snapshot. The snapshot field
is read only by the expected/current-cost reporting helpers.

**Consequence:** the snapshot provides no protection to the two paths that matter.
It is protective only in reporting. **Severity: Medium-High for design** — SMEsPlus
must not assume a snapshot exists merely because a snapshot field exists.

### `C-03` — Off-balance isolation is a **platform-wide** structural rule

`LIN-02` established the rule on the asset side only, as an account-selection domain,
and left "whether off-balance accounts are permitted anywhere in the production
costing path" open (`UNR-17`). The platform in fact enforces, on every journal entry:
if any line uses an off-balance account, **every** line must. The rule is a model
constraint, not a UI domain, and it applies to the production-costing entry too.

**Consequence:** `UNR-17` is answered, and the answer is better than hoped —
see `05` §7 for the answer, and `17` `CTR-C-05` for the trap it creates.

### `C-04` — Two custom model files are unimported, not one

`LIN-02` recorded one dead file plus the unimported wizard. Re-reading the package
initialiser shows the model package imports five of eight model files. Three are
unimported. Two of the three are **superseded duplicates** whose live replacements
exist and work — a fact this session verified before, not after, forming a view.

**Severity:** Low for function, Medium for the code-health class already flagged by
`LIN-02`. Recorded because the earlier count understated the dead surface.

## 5. Statements NOT re-tested, and why

| Statement | Reason not re-tested | Class retained |
|---|---|---|
| Population of 280 assets, 217 running, 16 templates, all with no model linked | Requires the running UAT, unreachable this session (`01` §6) | `FACT VERIFIED` at 2026-08-26, carried |
| The custom Thai daily method exists only on the legacy generation | Exhaustive negative already established across the available trees; no new tree became available | `FACT VERIFIED` (workspace-bounded), carried |
| The equivalence of the custom method and the calendar mode within 0.03 baht | Rests on `EV-SIM`; re-running the same transcription would not raise its class | `SOURCE-SUPPORTED INTERPRETATION`, carried |
| The stored disposal gain can differ from the posted gain by the residual | Read once from source in `LIN-02`; not contradicted | `FACT VERIFIED`, carried |

## 6. Lineage integrity statement

No inherited conclusion was deleted. No inherited conclusion was promoted to a higher
class without new primary evidence. Four mechanism statements were corrected, with
the superseded text quoted in §4 so a reviewer can audit the change rather than
having to trust it.

**One inherited qualifier is repeated here because it still binds every negative
finding in this package:** everything that says *does not exist* is bounded by the
source trees available in this workspace. The installed-module list of the running
system has still not been obtained.
