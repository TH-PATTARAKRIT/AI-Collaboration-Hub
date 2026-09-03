# 12 — DEEP LEVEL 6: CONTRADICTION / BOUNDARY / FAILURE ANALYSIS
**LAYER 2 — AUDIT QUARANTINE**

§65: this level is adversarial. It searches for failure, not confirmation. Where an
attack **failed** — where the system held — that is reported too, because a negative
attack result is evidence.

## 1. Depreciation failure cases — §66

Every case below was executed against the transcribed algorithm (`EV-SIM`), asset
1,200,000.00, straight line, no salvage unless stated.

| ID | Attack | Result | Verdict |
|---|---|---|---|
| `FAIL-D01` | 28-day February | Constant: 20,000.00. Daily: 18,400.87 | **Both correct for their convention. The two disagree by 8%** — `16` §3.4 |
| `FAIL-D02` | 29-day February (2028) | Constant: 20,000.00. Daily: 19,058.05 | Both self-consistent; disagree by 4.7% |
| `FAIL-D03` | 30- and 31-day months | Constant: identical. Daily: ±1.9% | Held |
| `FAIL-D04` | Acquisition on the **31st** | 61 lines; first period = a single day (645.16 constant / 657.17 daily); total exact | **Held** |
| `FAIL-D05` | Acquisition on **29 February** in a leap year | 61 lines; last day 2033-02-27; total exact | **Held** — no off-by-one |
| `FAIL-D06` | 60 months producing 61 lines | Reproduced | Expected behaviour, not a defect — `16` §5 |
| `FAIL-D07` | Partial first + partial final reconciliation | **Exactly one full period, to the cent, in both conventions** | **Held** |
| `FAIL-D08` | One-period asset acquired mid-month | 2 lines, total exact | **Held** |
| `FAIL-D09` | Residual = 1 unit | 12 lines, 11,999 depreciated, 1 retained | **Held** |
| `FAIL-D10` | Rounding drift across 61 periods | **Zero.** Every scenario totals exactly to the depreciable base | **Held** — by construction, `16` §1 |
| `FAIL-D11` | Currency rounding at the final line | No plug entry needed in any scenario | **Held** |
| `FAIL-D12` | Change duration mid-life | Catch-up + rebuild; history untouched | Held, by design — `24` |
| `FAIL-D13` | Change residual mid-life | Bounded: new residual ≤ current book value; the excess becomes a **child asset** | Held — `24` |
| `FAIL-D14` | Change method mid-life | Permitted; **future only**; the declining rebase point moves | Held with a caveat — `24` |
| `FAIL-D15` | Pause / resume | Calendar shift; end date extends; total unchanged | Held — `30` semantics, `06` §3.4 |
| `FAIL-D16` | Locked accounting period | Disposal and re-evaluation are guarded. **Confirm and pause are not guarded in this module** | **NOT HELD / UNRESOLVED** — `UNR-09` |

**Result of the attack on the depreciation engine: it holds.** Sixteen attacks,
fifteen held, one unresolved and that one is about lock dates rather than
arithmetic. The engine is arithmetically sound.

**The engine is not where the risk is.** The risk is that the *right convention* be
selected — `FAIL-D01` and `FAIL-D02` are not defects, they are two correct answers
to two different questions, and only one of them is the question Thai monthly
reporting asks.

## 2. Data failure cases — §67

| ID | Attack | Result |
|---|---|---|
| `FAIL-X01` | Asset Model changed after asset creation | **No effect.** Model values are copied at selection; there is no live inheritance. Runtime confirms: **all 280 UAT assets have no model linked at all** |
| `FAIL-X02` | Asset field overridden away from the model | Permitted, silently, permanently |
| `FAIL-X03` | Missing equipment relation | Permitted — the custom field is optional |
| `FAIL-X04` | **Duplicate equipment relation** | **Nothing prevents it.** `Many2one`, no inverse, no unique constraint. N assets may claim one machine | **NOT HELD** — `UNR-08` |
| `FAIL-X05` | Orphan asset (no source bill) | Permitted — the manual-creation route |
| `FAIL-X06` | Orphan equipment (no asset) | Permitted and normal — `20` |
| `FAIL-X07` | Company mismatch across asset / accounts / journal | Blocked by company checks on every relational field |
| `FAIL-X08` | Account mismatch — off-balance account on an asset account | **Blocked by field domain** — `04` §2.5 |
| `FAIL-X09` | Account changed after posting | Permitted via the modify wizard; **prior entries keep the old account** |
| `FAIL-X10` | Journal changed after posting | Same |
| `FAIL-X11` | Analytic changed mid-life | Permitted; **future entries only**; the asset row and its own history then disagree with nothing flagging it | **NOT HELD** — `UNR-11` |
| `FAIL-X12` | **Migration bypassing the ORM** | The board invariant is a **model constraint**, evaluated on write. A direct load can leave it violated with no error. The UAT is mid-migration with 280 records | **NOT HELD** — `CTR-06` |
| `FAIL-X13` | Custom module removed | The custom field and its data disappear; **no financial impact**, because nothing financial consumes it |
| `FAIL-X14` | Framework upgrade past the custom module's target generation | **Already happened.** Three constructs in the custom asset-link module target generations that have passed. They raise no error; they simply do nothing — `19` |

## 3. GL failure cases — §68

| ID | Attack | Result |
|---|---|---|
| `FAIL-G01` | Board ≠ GL | **Cannot diverge for posted lines** — the board *is* the entries. It can diverge for **draft** lines |
| `FAIL-G02` | Book value ≠ sub-ledger | Book value is derived from the entries, so they cannot disagree — **unless** the import field is used, which reduces the board **with no journal entry at all** | 
| `FAIL-G03` | Accumulated depreciation ≠ GL | Same. But note there is **no accumulated-depreciation field** to disagree with |
| `FAIL-G04` | Entry reversed | Handled: reversal creates a compensating line and a replacement is generated at the following period |
| `FAIL-G05` | Period locked | See `FAIL-D16` |
| `FAIL-G06` | Account changed after posting | `FAIL-X09`: the sub-ledger's account triple no longer describes its own history |
| `FAIL-G07` | Company changed | Blocked |
| `FAIL-G08` | Duplicate posting | Guarded by the board rebuild, which deletes drafts and reverses posted futures before re-creating |
| `FAIL-G09` | Missing posting | Possible if a draft entry is never posted; the board invariant does **not** check posted status |
| `FAIL-G10` | **No reconciliation function exists** | `VERIFIED GAP` — `22` |

**`FAIL-G02` is the most important GL finding in this level.** The *already
depreciated on import* field is the one documented way to make the sub-ledger and
the general ledger disagree by design — and it is exactly the field a migration
uses. On a UAT carrying 280 migrated assets this is not theoretical, and no
mechanism in the product detects it.

## 4. Production failure cases — §69

Every case in §69 was tested against the model. The result is uniform and it is
worth stating once rather than fourteen times:

> **None of the production failure cases can even be expressed**, because the
> objects they are about are not connected. There is no path from an operation to
> a machine, and no path from a machine to a cost.

| ID | Case | Result |
|---|---|---|
| `FAIL-P01` | Equipment in a work centre that the operation does not use | **The distinction does not exist.** Operation → Work Center only |
| `FAIL-P02` | An operation using one of many machines | Cannot be recorded |
| `FAIL-P03` | Routing changed | Affects operations and work centres; no equipment consequence |
| `FAIL-P04` | Machine replaced mid-order | Not recordable |
| `FAIL-P05` | Breakdown mid-operation | Recordable as a maintenance request; **costs nothing** |
| `FAIL-P06` | Machine idle | Not recorded at all |
| `FAIL-P07` | Planned / unplanned maintenance | Blocks **capacity**; no cost |
| `FAIL-P08` | Production started, no finished goods yet | Work-order cost accrues to the order; absorbed only on completion |
| `FAIL-P09` | WIP spanning periods | The labour entry posts on completion, so cost lands in the **completion** period regardless of when the work happened | **Real timing distortion**, and it will affect any depreciation-derived rate |
| `FAIL-P10` | Multiple orders sharing equipment | Shared implicitly through the work centre, averaged |
| `FAIL-P11` | One order using several machines | Not recordable |
| `FAIL-P12` | Equipment without an asset | Normal |
| `FAIL-P13` | Asset without equipment | Normal — and the majority case |
| `FAIL-P14` | Fully depreciated machine still operating | **Invisible.** No state, no flag, no report — `10` §3.2 |

`FAIL-P09` deserves emphasis because it is a defect the SMEsPlus design will
inherit if it reuses links 2–6: **machine cost is recognised when the order
completes, not when the machine ran.** A monthly depreciation-derived rate fed into
that chain will land in the wrong month for any order spanning a month end.

## 5. Residual failure cases — §70

| ID | Case | Result |
|---|---|---|
| `FAIL-R01` | Residual = 1 | Held — `FAIL-D09` |
| `FAIL-R02` | Residual = 0 | Held; the asset depreciates to zero book value |
| `FAIL-R03` | Residual unusually high | Held; the depreciable base shrinks accordingly |
| `FAIL-R04` | Sold above / below residual | The difference falls into gain or loss — `25` |
| `FAIL-R05` | Equipment runs 20 years past full depreciation | **Not representable.** No state, no cost, no record |
| `FAIL-R06` | Cumulative internal usage exceeds residual | **Cannot be evaluated** — the concept does not exist. Contested design item, `D5-01` |
| `FAIL-R07` | Residual changed after full depreciation | Permitted. **Raising it creates a child asset**; lowering it posts a value decrease |
| `FAIL-R08` | Disposal immediately after full depreciation | **Residual is removed from book value on closure and written out through gain/loss** — `18` §6 |

`FAIL-R08` is the case that matters most to the Boss's design and it is the one
that behaves least as expected. **The residual does not survive disposal as an
identifiable amount.**

## 6. Analytic failure cases — §71

| ID | Case | Result |
|---|---|---|
| `FAIL-A01` | No analytic | The key is **omitted entirely** from the entry rather than set empty — deliberate, so that other computations can still fill it |
| `FAIL-A02` | Wrong analytic | No validation |
| `FAIL-A03` | Multiple distributions | Supported; balance-weighted at inheritance |
| `FAIL-A04` | Distribution ≠ 100% | **Not validated at the asset level** |
| `FAIL-A05` | Analytic archived | Not checked by the asset |
| `FAIL-A06` | Analytic company mismatch | Not checked by the asset |
| `FAIL-A07` | Changed mid-life | `FAIL-X11` — future only, silently |
| `FAIL-A08` | Historic entry locked | Cannot be corrected; the divergence is permanent |

## 7. Accounting vs tax failure cases — §72

| ID | Case | Result |
|---|---|---|
| `FAIL-T01` | Financial life ≠ tax life | **Cannot be represented.** One schedule only |
| `FAIL-T02` | Financial rate ≠ statutory ceiling | Cannot be represented |
| `FAIL-T03` | Different residual for tax | Cannot be represented |
| `FAIL-T04` | Different method for tax | Cannot be represented |
| `FAIL-T05` | Different day convention for tax | Cannot be represented |
| `FAIL-T06` | Different disposal treatment | Cannot be represented |

**Six for six.** The absence of a tax book is the single largest functional gap in
the reference asset domain for a Thai deployment, and Royal Decree 145's rates are
**ceilings**, which is exactly the condition that produces book/tax differences.

`VERIFIED GAP`. This was flagged by Expert 3 at Level 1 and it is confirmed here.

## 8. Source contradiction cases — §73

| Comparison | Result |
|---|---|
| UI vs code | **Seven material divergences** — `04` §4 |
| Code vs database | Consistent where checkable |
| Database vs journal | Consistent by construction; `FAIL-G02` is the exception |
| Documentation vs runtime | Not tested — no product documentation was used as evidence in this session |
| Standard vs custom | **`CTR-03`** — two asset models in the legacy system, with the two capabilities the Boss relies on attached to different ones |
| Boss assertion vs source | **Five assertions tested — `38`** |
| Prior AI finding vs new evidence | **Eleven prior findings re-tested — `29`** |

## 9. Attacks that could not be executed this session

Stated explicitly rather than omitted (§21, §22 — a blocked lane does not stop the
others, but it must be declared):

| Attack | Why not executed |
|---|---|
| Confirm into a locked period | Requires a running system — `UNR-09` |
| Migration bypassing the ORM | Requires the UAT database — `CTR-06` |
| Duplicate equipment links, counted | Requires the UAT — `UNR-08` |
| Analytic divergence, counted | Requires the UAT — `UNR-11` |
| Transactional failure mid-modify | Requires a running system — `UNR-10` |
| Whether the off-balance account type is excluded from statutory reports | Requires product and statutory evidence not obtained — `UNR-17` |

## 10. Four Expert opinions

See `13_LEVEL6_FOUR_EXPERT_OPINIONS.md`.
