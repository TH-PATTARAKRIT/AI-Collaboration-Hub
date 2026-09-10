# PT-12 — CANONICAL PHASE PRE-TEST MATRIX

## `CP-PT-12 — PRE-TEST MATRIX COMPLETE: PRESENT AND POINTED, NOT PROVEN`

*(master-prompt checkpoint name: `CP-PT-12 — PRE-TEST MATRIX COMPLETE`)*

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-NEWSESSION-001]`
Branch: `architecture/account-phase-pretest-new-session-2026-09-10-001` · head consumed `eb4e760b`
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **`47` rows · `0` runtime-verified · `0` vetoes discharged · `E2E-04 NOT TRAVERSABLE`.**
> **`COMPLETE` here means every row is present with a pointer and a disposition. It does NOT mean proven.**

---

## 1. Row-contract compliance — how the `34` required fields are carried

**The master prompt §4 requires `34` fields on every material row. Carrying `47 × 34 = 1,598` cells
individually would bury the discriminating content in repetition — so each field is classified
**UNIVERSAL** (identical on every row, stated once **with its authority**) or **PER-ROW**.**

**A field is UNIVERSAL only where a single named authority fixes it for the whole population.
`9` qualify; `25` are per-row.**

### 1.1 The `9` universal fields, with authority

| # | Field | Universal value | Authority |
|---:|---|---|---|
| 19 | **Tenant boundary** | `SCOPE-AWARE` (`PLATFORM`/`TENANT`/`COMPANY`); element 10 **specified, not built**; `0 of 8` isolation proofs, `0 of 60` negative cases, `0 of 13` enforcement surfaces | `SA10` §8.2 · `AAS-V-01` |
| 20 | **Company boundary** | statutory tax is **company-scoped**; **no cross-company statutory posting, offsetting or filing** | `BD-ACC-02` |
| 21 | **Identity / idempotency** | the deterministic identity is the **six-part basis** `XMC-C-A2` + attempt identity `A14`; **required always** — `BD-ACC-01`'s sentence is unqualified; **specified, NOT BUILT**; `0 of 13,814` dedup keys | `BD-ACC-01` · `SC-SMT-03` · `SA_CORR5_01` |
| 22 | **Reversal requirement** | a reversal is **a new event referencing the original**, original unchanged; **value basis `JT-05` = ORIGINAL COST** | `BD-ACC-01` · `XMC-C-A8` · **`SC-BD-05`** |
| 26 | **Evidence class** | **`PTE-3` EXECUTION-DESIGN READY** on every scenario row | `PT-10` §3 |
| 27 | **Required evidence artifact** | executed runtime proof **+ independent reproduction** | `8C-CLARIFICATION-01` cl. 3 |
| 31 | **Gate effect** | **`0` rows gate Pre-Test entry.** All attach to the **Module / State 8-Criteria Exit Gates** | `SC-AUTH-02 = Reading C` |
| 32 | **Veto linkage** | `AAS-V-01`, `CF-V-01`, `RC-V-01` bar **implementation start** for every row; **`0` discharged** | `SC-04` |
| 34 | **Independent challenge status** | **`NOT INDEPENDENTLY CHALLENGED` — B-7 outstanding, `0` candidates named** | `SC-57` · `B7-00` |

### 1.2 Two universal *process* obligations, carried on every row

- **`ND-09`** — a cross-module fulfilment producing revenue **must** produce a cost recognition **bound to
  the same identity**, **or an explicit recorded determination that it does not**.
- **`ND-03`** — an automatic cross-module document **may not enter a module below that module's control
  floor**. *(Breached on the procurement route — `PT07-F-03`.)*

---

## 2. Population A — the `22` Boss-approved cross-module scenarios

**Universal for this table:** evidence class `PTE-3` · cross-proof result **`HOLD`** · runtime proof
**required (`Y`)** · `0 of 22` verified · Inventory convergence `IC = C` on all `22`.

| ID | Scenario / route trigger | Downstream consumer(s) | Accounting impact | Missing input | `PT` | Disposition |
|---|---|---|---|---|---|---|
| `X-01` | Stockable purchase receipt → handoff | Accounting; AP | receipt valuation | el.`4`/`7`; **el.`12` weakened — swept suspense, not item-matched** | `GATED`* | `HOLD` |
| `X-02` | Vendor bill, receipt timing variation | Accounting; AP | bill vs receipt basis | el.`4`/`7`; **no prior-period attribution mechanism at all** | `GATED`* | `HOLD` |
| `X-03` | Stockable sales delivery → cost handoff | Accounting; AR | **COGS** | el.`4`/`7`; **`BP-02` not selectable** | `GATED`* | `HOLD` |
| `X-04` | Customer invoice, delivery timing variation | Accounting; AR | revenue/cost timing | el.`4`/`7` | `GATED`* | `HOLD` |
| `X-05` | Partial receipt | Accounting; AP; Purchase | partial valuation | **over-receipt tolerance undefined** | `GATED`* | `HOLD` |
| `X-06` | Partial delivery | Accounting; AR | partial COGS | **`H-05` draft invoice consumes billable qty, posts nothing, freely deletable** | `GATED`* | `HOLD` |
| **`X-07`** | **Backorder** | **`R-17` — NO CONSUMER** | — | **remainder-supply record has NO CONSUMER; never-mode cancellation leaves NO document trail** | `WRITABLE` | **`HOLD` — `producer→∅`** |
| `X-08` | Purchase return | Accounting; AP | debit/reversal | el.`4`/`7`; return basis `PENDING` | `GATED`* | `HOLD` |
| `X-09` | Sales return | Accounting; AR | credit/reversal | el.`4`/`7`; **`JT-05` now RULED = original cost** | `GATED`* | `HOLD` |
| `X-10` | Cancellation before physical execution | Accounting | none by design | `C-01` symmetry; `C2-F-01` durability; **`XD1-P1` RULED = `BLOCK`** | `GATED`* | `HOLD` |
| **`X-11`** | Correction after physical execution | Accounting | correcting entry | **corrected-entry link DOES NOT EXIST; only route is a return** | `WRITABLE` | `HOLD` |
| `X-12` | Inventory count / adjustment | Accounting | adjustment | **approval mechanism absent; can silently reduce a reservation** | `WRITABLE` | `HOLD` |
| `X-13` | Scrap / damage / write-off | Accounting; Tax | write-off | **salvage undefined; scrap has NO COST CAUSALITY** | `WRITABLE` | `HOLD` |
| `X-14` | Internal transfer — no financial effect | Accounting | **NO POSTING BY DESIGN** | **`R4-F-18` no independent check; neutrality configuration-protected only** | `WRITABLE` | `HOLD` |
| **`X-15`** | **Multi-company / tenant boundary** | all | isolation | **THIS SCENARIO *IS* ELEMENT 10** — `0 of 8`, `0 of 60`, `0 of 13`; **two lock-defeat paths** | `WRITABLE` | **`HOLD` — TOLERANCE-ZERO** |
| `X-16` | Manufacturing RM → WIP → FG | Accounting; Inventory | consumption/output | el.`4`/`7`; **fixed overhead has NO INJECTION PATH** (`R-22`) | **`GATED`** | `HOLD` |
| `X-17` | Manufacturing reversal / scrap / variance | Accounting | variance | **NO VARIANCE MECHANISM — `1 of 9`** | **`GATED`** | `HOLD` |
| `X-18` | Stockable vs consumable vs service routing | Accounting; Inventory | route-dependent | **two-axis tie-break undefined; `BD-ACC-01` SILENT FOR SERVICES** | `GATED`* | `HOLD` |
| `X-19` | Period-end / cut-off | Accounting | close | el.`4`/`7`; **no accounting-period object exists** | `WRITABLE` | `HOLD` |
| `X-20` | Historical migration across fiscal years | Accounting | opening balances | **el.`14` — provenance reference DOES NOT EXIST, must be originated** | `WRITABLE` | `HOLD` |
| `X-21` | AI migration mapping + reconciliation | Accounting | certified opening | **el.`14`; `MTI-42` bars inferring context** | `WRITABLE` | `HOLD` |
| **`X-22`** | **Retry / idempotency / replay** | all | none directly | **THIS SCENARIO *IS* ELEMENT 15** — `UAE-29` the root | `WRITABLE` | **`HOLD` — DEPENDENCY GATE** |

**`*` = `GATED` as measured 2026-09-09; the gating decision has since been RULED (`PT10-F-01`). The
`10 WRITABLE / 12 GATED` split is carried UNCHANGED and is NOT re-derived here.**

---

## 3. Population B — the `18` end-to-end scenarios

**Universal:** `0 of 18` verified · runtime proof required · `PTE-3`.

| ID | Route | Traversability | Business nature | Required input not established | Boss family — **status now** |
|---|---|---|---|---|---|
| `E2E-01` | Customer → Sales → Stock → Delivery → AR → Payment → Bank → Accounting | NAMED BREAK | `BN-01` | `TV6-BOSS-01`, `TV6-BOSS-02`, `XD1-P1` | **`F2` RULED** |
| `E2E-02` | Purchase demand → … → Payment | **TRAVERSABLE** | `BN-02` | **none** (A2 approval logic open) | — |
| `E2E-03` | Sales → Manufacture → RM → FG → Delivery → AR | NAMED BREAK | manufacture | `B-6`, `POH-D-02` | **`F5` PARTLY — `POH-D-02` withheld** |
| **`E2E-04`** | Sales → Manufacture → **RM shortage** → Purchase → Production | **NOT TRAVERSABLE** | `BN-04` | **the shortage state has NO SUPPLY EXIT — a DEFECT, not an election** | `F4` **RULED**; **grade NOT changed** |
| `E2E-05` | Sales → Dropship → Purchase → vendor-to-customer → AR/AP | NAMED BREAK | `BN-05` | `H-02` incompatible, `H-03` **NO IDENTITY** | **`F3` RULED** — no exception class |
| `E2E-06` | Sales → MTO/Buy → Purchase → Receipt → Delivery | NAMED BREAK | `BN-06` | order→purchase linkage; reservation semantics | — |
| `E2E-07` | Sales → Kit → component inventory → Delivery | **TRAVERSABLE** | `BN-07` **`PARTIAL`** | **none stated — BUT see risk** | none |
| `E2E-08` | Service → completion evidence → AR | NAMED BREAK | service | none — `XMC-C-C2` specifies asserter/time/basis | — |
| `E2E-09` | Purchase → capitalization → depreciation | NAMED BREAK | asset | Equipment-side semantics; **`XMC-H-09` NO CONSUMER** | — |
| `E2E-10` | Expense → approval → payable → payment | NAMED BREAK | expense | approval **occurrence** record (`XD-03`) | — |
| `E2E-11` | Sales return → inventory return → credit | NAMED BREAK | return | **`JT-05` RULED = original cost** | **`F1` RULED** |
| `E2E-12` | Purchase return → inventory return → debit | NAMED BREAK | return | return basis `PENDING` | **`F1` RULED** |
| `E2E-13` | Mfg scrap / by-product / variance | NAMED BREAK | scrap | by-product valuation; **`F1`'s card omitted this scenario (`CHF-18`)** | **`F1` RULED** |
| `E2E-14` | Month close → valuation → AR/AP → Bank → **Tax** → GL | NAMED BREAK | close | period object; **analytic data; statutory register content** | **not a Boss election** (`CHF-10`) |
| **`E2E-15`** | Correction / reversal / **retry / duplicate** | NAMED BREAK | cross-cutting | **element 15 — specified, NOT BUILT** | **`F8` RULED** — design input, **exit criteria `PTX-01`…`-11`** |
| `E2E-16` | Quality hold → availability → cost timing | NAMED BREAK | quality | **the Quality object is ABSENT** | — |
| `E2E-17` | Work order → breakdown → maintenance → resume | NAMED BREAK | maintenance | `BLK-08`; `9 of 12` routes close | **`F5` PARTLY** |
| `E2E-18` | Project → source facts → analytic → derived view | NAMED BREAK | analytic | derivation mechanism; reversal behaviour | — |

### 3.1 Bounded risk attached to `E2E-07` by `PT05-F-02`

> **`E2E-07` is graded `TRAVERSABLE` with `none` outstanding. Its own business nature `BN-07` is
> `PARTIAL`, and half two carries a named silent failure: *the purchase price-difference correction filter
> contains no kit predicate at all; where the bill line's product differs from the ordering line's product
> the layer set empties and the correction is silently skipped.*** **Carried as a bounded risk on the row.
> The grade is NOT changed.**

---

## 4. Population C — the `7` Pre-Test additions

| ID | Scenario | Routes to | Coverage reason | Class |
|---|---|---|---|---|
| `PT-S-01` | Sale with statutory tax consequence → VAT/WHT → register → GL | Sales · **Tax** · Accounting | `VAT`/`WHT` = `0` in all three scenario registers | **`PTE-4`** — `POH-D-02`, statutory |
| `PT-S-02` | Direct buy → sell, no manufacture | Purchase · Inventory · Sales · Accounting | `0` corpus representation as one commercial act | `PTE-3` |
| `PT-S-03` | Make-to-stock vs make-to-order contrast | Manufacturing · Inventory · Accounting | `make-to-stock` = `0` in `192` files | `PTE-3` |
| `PT-S-04` | Partial **invoice** and partial **payment** | Sales/Purchase · AR/AP · Payment | `partial payment` = `0`; §7 requires all four partials | `PTE-3` |
| `PT-S-05` | Return **before** vs **after** invoice | Sales/Purchase · Inventory · Accounting | the timing discriminator is undefined | `PTE-3` |
| `PT-S-06` | **Reversal after downstream consumption** | any producer → any consumer → Accounting | `X-11` is a different predicate (physical, not module) | `PTE-3` |
| `PT-S-07` | Out-of-order / stale arrival / partial mid-chain failure | cross-cutting | `event order` = `0`, `out-of-order` = `1` | `PTE-3` |

---

## 5. `PT-C-01` — the composed row `PT09-F-02` requires

**Three separately-recorded open items whose composition is recorded nowhere.**

| | |
|---|---|
| **Scenario** | Goods shipped → invoiced → customer returns → **the period has closed** → a downstream module already consumed the original output |
| **INPUT** | original movement + invoice + return request + closed-period state + downstream consumption record |
| **PROCESS** | correction after a completed movement → **must become a return** (`X-11`) |
| **OUTPUT** | return movement + reversal event referencing the original, **at original cost** (`JT-05` RULED) |
| **DOWNSTREAM** | Inventory · Accounting · Tax · **the module that already consumed the original** |
| **Reversal** | `XMC-C-A8` — original unchanged **byte-for-byte** |
| **CONFLICT** | **`H-07`: matching is *"not an entry"* and matching rows are freely destructible across a closed period — and cash-basis tax keys off it** (`PT09-F-03`) |
| **Exception path** | **NOT SPECIFIED** — `PT-S-06` has no representation |
| **Expected result** | `HOLD / EVIDENCE REQUIRED` |
| **Class** | **`PTE-3`** + **UNSPECIFIED COMPOSITION** |

---

## 6. Cross-cutting control rows — the `11` from `SA17` §3, and the `11` exit criteria

**All `22` are `PTE-3`. `2` are order-gated. `0` are provable by document.**

| Group | Rows | Order constraint |
|---|---|---|
| `SA17` §3 controls | `11` — approval occurrence · control floor · non-interface write paths · **period lock binds the entry (`ND-07`)** · reservation survives adjustment · transfer neutrality · **same-event retry** · no cross-company statutory posting · reason class refused · grant-revoked-`SUSPECT` · one-tenant-at-a-time totals | retry ⟵ element 15 · `CF-I-03R` ⟵ `MTI-50` |
| **Exit criteria `PTX-01`…`PTX-11`** | `RT-E15-01`…`-09` + deterministic-identity proof + the order gate | **`MTI-50` → `CF3-C-01`…`C-04` → only then any positive test** |

---

## 7. Disposition summary

| Population | Rows | Verified | Disposition |
|---|---:|---:|---|
| A — Boss cross-proof `X-01`…`X-22` | `22` | **`0`** | `22 × HOLD` |
| B — end-to-end `E2E-01`…`E2E-18` | `18` | **`0`** | `2` traversable · `15` named break · **`1` NOT TRAVERSABLE** |
| C — Pre-Test additions `PT-S-01`…`-07` | `7` | **`0`** | `NEW — UNPROVEN` |
| Composed | `1` (`PT-C-01`) | **`0`** | `HOLD` — composition unspecified |
| **Scenario total** | **`48`** | **`0`** | |
| Control rows (`SA17` §3) | `11` | `0` | all `PTE-3` |
| Exit criteria (`PTX`) | `11` | `0` | all `PTE-3`, none adopted |

> **The scenario population is `48`, not `47`** — `PT-01` fixed `47` and `PT-09` produced the composed row
> `PT-C-01`, which `PT-12` carries as a scenario. **The denominator moved inside this session, and it is
> published rather than absorbed.**

---

## 8. Checkpoint

> ## `CP-PT-12 — PRE-TEST MATRIX COMPLETE (PRESENT AND POINTED, NOT PROVEN)`
>
> **`48` scenario rows + `11` control rows + `11` exit criteria, each with a source pointer and a
> disposition · the `34`-field row contract carried as **`9` universal fields with named authority + `25`
> per-row**, the classification stated rather than assumed · **`0` rows omit downstream routing** ·
> **`0` verified, `0` proven, `0` graded up** · `E2E-04` `NOT TRAVERSABLE` and `E2E-07`'s silent-skip risk
> both carried on the row · the `10 WRITABLE / 12 GATED` split carried **unchanged and marked pre-ruling** ·
> **the scenario denominator moved `47 → 48` inside this session and is published, not absorbed.**
>
> **`0` vetoes discharged · `0` ruled denominators re-scoped · `0` Phase SA artefacts rewritten.**

Next checkpoint: `PT-13 — SMEs Core Falsification`.

No Evidence = No Progress. Never Skip Gate. A missing consumer is a defect. Truth over Pass.
Boss remains the sole Final Approver.
