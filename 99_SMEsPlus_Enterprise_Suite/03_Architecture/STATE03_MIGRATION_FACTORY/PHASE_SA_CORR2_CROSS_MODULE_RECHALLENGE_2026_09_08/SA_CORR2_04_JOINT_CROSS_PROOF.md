# SA_CORR2_04 — ACCOUNT × INVENTORY JOINT CROSS-PROOF
## CP-SA-C2-30 — JOINT CROSS-PROOF COMPLETE

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Authority to convene: **already granted.** Master prompt §5 — *"Convene the previously authorized
joint cross-proof if repository evidence confirms it was already approved but never executed. Do not
escalate a new Boss approval for an already authorized proof activity."*
Evidence frame: `SA_CORR2_00` §2 as corrected by `C2-I-02`.

---

## 1. Authority verified before convening

| Control | Status, verbatim | Where, and how read |
|---|---|---|
| 22-scenario cross-proof baseline | `BOSS APPROVED / EFFECTIVE` | `.../ACCOUNT_INVENTORY_JOINT/02_BOSS_APPROVAL_JOINT_22_SCENARIO_CROSS_PROOF_BASELINE_2026_09_02.md`, **read from the `origin/SMEsPlus` tree**, commit `296b495` |
| 16-element Minimum Handoff Data Contract | `BOSS APPROVED / EFFECTIVE` | `.../ACCOUNT_INVENTORY_JOINT/03_BOSS_APPROVAL_INVENTORY_TO_ACCOUNTING_MINIMUM_HANDOFF_DATA_CONTRACT_2026_09_02.md`, **read from the `origin/SMEsPlus` tree**, commit `d9e845e` |
| Eleven-topic agenda | exists, every topic `PENDING JOINT SESSION 3` | `.../BOSS_DECISION_LEGAL_TAX_ROUTING_EXECUTION/07_ACCOUNT_INVENTORY_JOINT_SESSION_3_ROUTING_BRIEF.md` |
| Execution record | *"**N/A — no session has yet occurred**"* | `.../BATCH_A_CONTROLLED_RESEARCH_ROUTING_EXECUTION/04_ACCOUNT_INVENTORY_JOINT_SESSION_3_EXECUTION_RECORD.md` |
| The gating condition | Boss directive gates the joint work behind full accounting-core closure | attested in `SA13` §5 and `SA19` §20 |
| **Whether the gate has lifted** | **YES** — `CP-SC-15 — PHASE S CONDITIONALLY CLOSED / PHASE SA ENTRY AUTHORIZED` | `.../PHASE_S_CLOSURE/.../04_PHASE_S_CONDITIONAL_CLOSURE_AND_PHASE_SA_ENTRY.md`; parent gate `be5d1595` |

**`C2-F-11` — and it matters for the honesty of this whole register.** `SA13` §5 and `SA19` §20
described these two controls as established *"by challenge search across all 183 branches"*. They
are **not** on any of the 183 branch diffs. **They are on `origin/SMEsPlus` itself**, which the
declared PATH SET could not reach (`C2-I-02`). Every prior description of them in this programme was
therefore a **secondary rendering** — accurate, as it turns out, but never checked against the
primary text.

**They are checked now.** The 16 elements below are transcribed from the approval document itself.

---

## 2. The 16-element contract — primary text, and one correction to the programme's reading

Verbatim from `d9e845e` §3, *"Every material Inventory → Accounting handoff must prove that the
following information is **known, traceable, and evidence-backed**"*:

| # | Element, verbatim | Conditional in the primary text? | Current status |
|---:|---|---|---|
| 1 | `WHAT happened` — business event/fact that occurred | No | **SUPPLIABLE** |
| 2 | `WHO owns the fact` — source-domain ownership and accountable fact owner | No | **SUPPLIABLE** |
| 3 | `WHEN physical event occurred` | No | **SUPPLIABLE** — carried as two distinct dates |
| 4 | `WHEN financial recognition occurs` — *"or explicit pending/hold condition"* | No | **HELD** — `ACCOUNTING COGS GAP` |
| 5 | `HOW MUCH quantity` | No | **SUPPLIABLE** |
| 6 | `WHICH UOM` | No | **SUPPLIABLE** — conversion rounding defaults upward, carried |
| 7 | `WHAT valuation/cost basis applies` — *"or explicit `N/A / HOLD` with reason"* | No | **HELD** — `ACCOUNTING COGS GAP` |
| 8 | `WHICH Product / Lot / Serial` | *"where applicable"* | **SUPPLIABLE** — strengthened: identity is the resolved tuple, never the bare value |
| 9 | `WHICH Warehouse / Location` | *"as applicable"* | **SUPPLIABLE** — strengthened |
| **10** | `WHICH Company / Tenant` — **"mandatory company and tenant context"** | **NO — unconditional** | **NOT SUPPLIABLE AS A GUARANTEE** — see §3 |
| 11 | `WHICH Source Document` | No | **SUPPLIABLE** |
| 12 | `WHICH Original Event` | No | **PARTIAL** — depends on element 15 |
| 13 | `WHICH Reversal / Correction` | *"where applicable"* | **PARTIAL** — depends on element 15 |
| **14** | `WHICH Migration / Replay Batch` | **YES — "where the handoff is created/replayed through migration or recovery"** | **NOT SUPPLIABLE** — the provenance reference does not exist |
| **15** | `WHICH Idempotency Identity` — *"deterministic identity used to prevent duplicate processing/effect"* | **No qualifier at §3.** §4 adds *"when idempotency is required"* | **NOT SUPPLIABLE** — no stable identity exists |
| 16 | `WHAT Evidence proves it` | No | **PARTIAL** |

### 2.1 The refinement, verified against primary text

A prior Inventory review (`REV-F-02`) refined the claim that all three unsuppliable elements block
all ten material handoffs: **element 14 is contractually conditional and element 10 is not.**

**CORR2 verifies this against the approval document itself and it holds exactly.** Element 14 reads
*"where the handoff is created/replayed through migration or recovery"*; element 10 reads
*"mandatory company and tenant context"* with no qualifier of any kind.

> **Element 10 alone is sufficient to produce the 0-of-22 result. The conclusion does not depend on
> element 14 at all.**

---

## 3. `C2-F-12` — the blocker's stated ground is superseded, and the conclusion survives on a narrower one

This is the most consequential finding in this register, and it changes what the remediation is.

**`RISK-U03`, as written**: element 10 cannot be supplied because *"the Inventory-side multi-tenant
invariant set **does not exist**."*

**Measured now.** It exists. Two packages, **35 unique text paths (U2)**, including a dedicated
problem statement for `RISK-U03` itself, an invariant set, a conformed revision, an isolation proof
matrix, an enforcement point matrix, a negative access test specification and a Boss decision
package:

```
02_RISK_U03_GAP_FS10_PROBLEM_STATEMENT.md      03_INVENTORY_MULTI_TENANT_INVARIANT_SET.md
03_MTI_INVARIANT_SET_R2_CONFORMED.md           07_L9_ISOLATION_PROOF_MATRIX.md
05_FUNCTION_ENFORCEMENT_POINT_MATRIX.md        09_NEGATIVE_ACCESS_TEST_SPECIFICATION.md
06_CROSS_MODULE_HANDOFF_CONTRACT_FIELDS.md     14_BOSS_DECISION_PACKAGE.md          … 35 in total
```

*(First published as "52 files", which counted **path-blob rows**, not unique paths — a unit
conflation, in the register that turns on one. Corrected after adversarial challenge.)*

Its own status line, verbatim: `50 CARRIED + 8 ADDED = 58 INVARIANTS SPECIFIED — 0 PROVEN —
14 RE-SPECIFIED — DESIGN / SPECIFICATION ONLY — NOT DEVELOPMENT FINAL GATE`.

**So `RISK-U03` as stated is false today.** The set exists.

**And element 10 is still not suppliable**, because the contract's standard is
*"known, traceable, **and evidence-backed**"* — three conjuncts — and the isolation programme's own
controlling standard says the same thing from the other side:

> an element must be **known, traceable and evidence-backed**; a specification satisfies none of the
> three on its own.

Element 10's current status in the handoff-contract register is exactly right:
**`Specified, not built, not verified`.**

### 3.1 Why this is worth a finding rather than a footnote

**The blocker moved from *absent* to *specified-and-unproven*, and no register that depends on it
noticed.** The `0 of 22` figure is quoted, unchanged, in roughly fifty places. It is still correct.
But its **cause** changed, and the cause is what determines the remedy:

| | Remedy implied |
|---|---|
| `RISK-U03` as written — *the invariant set does not exist* | **Write it.** (Done. 58 invariants.) |
| `RISK-U03` as it actually stands — *58 invariants specified, 0 proven, 0 of 13 enforcement surfaces, 0 of 52 negative access tests executable "because no implementation exists"* | **Build and prove it** — which is a Pre-Test / Development activity, not a specification activity |

> **A correct number carried forward on a superseded reason is how a programme keeps commissioning
> work that is already done.** This is the same class as `SA09`'s stale exception register
> (`XD-04`), one level up: not a stale *status*, a stale *cause*.

---

## 4. The joint cross-proof, convened

Convened on the authority verified at §1. SMEs Core perspectives participating, per master prompt §5,
all of them **same-model internal challenge** (`SA_CORR2_11`): Functional, Sales/AR, Purchase/AP,
Inventory, Manufacturing, Accounting/Posting, Tax, Bank/Payment, Data/Integration, SaaS/Security,
Audit/Standards, Clean-room.

### 4.1 The 22 scenarios, with the joint result

Boss numbering, as enumerated in the Inventory-side proof register. Inventory-side state carried by
pointer (`AUTO-C2-01`); **the Accounting-side column and the joint result are produced by this
session** — that is what convening adds.

| # | Scenario | Inventory side | **Accounting side (CORR2)** | **Joint result** |
|---:|---|---|---|---|
| 1 | Purchase receipt → handoff | NOT PROVABLE — dependency | GRNI evidenced, `FACT VERIFIED`, and it is **a swept suspense account, not an item-matched bridge** | `NOT PROVABLE` — el.10 |
| 2 | Vendor bill timing variation | NOT PROVABLE — dependency | `FACT VERIFIED`; **no prior-period attribution mechanism exists** | `NOT PROVABLE` — el.10 + a real gap |
| 3 | Sales delivery → cost handoff | NOT PROVABLE — dependency | Recognition point generation-split (`C2-F-03`) | `NOT PROVABLE` — el.10 |
| 4 | Customer invoice timing variation | NOT PROVABLE — `JT-04` NOT DECIDABLE | **`JT-04` DISCHARGED by CORR2** — `C2-F-03` | `NOT PROVABLE` — el.10 only |
| 5 | Partial receipt | NOT PROVABLE — dependency | Under/over-receipt rows evidenced | `NOT PROVABLE` — el.10 |
| 6 | Partial delivery | NOT PROVABLE — dependency | Billable-quantity semantics evidenced | `NOT PROVABLE` — el.10 |
| 7 | Backorder | NOT PROVABLE — structural | Never-mode remainder cancellation evidenced, **no document trail** | `NOT PROVABLE` — el.10 + structural |
| 8 | Purchase return | NOT PROVABLE — dependency | Evidenced | `NOT PROVABLE` — el.10 |
| 9 | Sales return | NOT PROVABLE — `JT-05` NOT DECIDABLE | Credit note reverses revenue, AR, tax and cost, `FACT VERIFIED` | `NOT PROVABLE` — el.10 + `JT-05` |
| 10 | Cancellation before execution | NOT PROVABLE — `C-01` unarbitrated | **CORR2: decomposed to 2 decisions + 1 delivery** (`SA_CORR2_01` §3) | `NOT PROVABLE` — el.10 + Boss decision |
| 11 | Correction after execution | NOT PROVABLE — structural | The only route is a return, evidenced | `NOT PROVABLE` — el.10 |
| 12 | Count / adjustment | NOT PROVABLE — closest to specifiable | Evidenced | `NOT PROVABLE` — el.10 |
| 13 | Scrap / damage / write-off | NOT PROVABLE — salvage undefined | Scrap has **no cost causality** | `NOT PROVABLE` — el.10 + design |
| 14 | Internal transfer — no inappropriate financial effect | NOT PROVABLE — no independent check | **Rule now stated**: internal→internal emits no valuation fact (`SA_CORR2_03` §3.3) | `NOT PROVABLE` — el.10; neutrality still configuration-protected |
| 15 | Multi-company / tenant boundary | NOT PROVABLE — 0 of 8 isolation proofs | Company-dependent account resolution defect, currently unable to fire | `NOT PROVABLE` — **this scenario IS element 10** |
| 16 | Manufacturing RM → WIP → FG | NOT PROVABLE — dependency | Evidenced; fixed-overhead injection absent | `NOT PROVABLE` — el.10 |
| 17 | Manufacturing reversal / scrap / variance | NOT PROVABLE — no variance mechanism | One variance of nine recognised | `NOT PROVABLE` — el.10 + design |
| 18 | Stockable / consumable / service routing | NOT PROVABLE — tie-break undefined | **CORR2: the correct application level is the line item, evidenced** (`SA_CORR2_03` §3.1) | `NOT PROVABLE` — el.10; tie-break still open |
| 19 | Period-end / cut-off | NOT PROVABLE — dependency | `FACT VERIFIED`, and **re-dating past a lock is the default behaviour**; **no accounting-period object** | `NOT PROVABLE` — el.10 + a real gap |
| 20 | Historical migration across fiscal years | NOT PROVABLE — structural | — | `NOT PROVABLE` — el.10 + el.14 |
| 21 | Migration mapping + deterministic reconciliation | NOT PROVABLE — structural | — | `NOT PROVABLE` — el.10 + el.14 |
| 22 | Retry / idempotency / replay | NOT PROVABLE — direct expression of `RISK-C02` | **`FE-01` duplicate posting REACHABLE — no accounting-event identity, no idempotency key**; `XM-01` `HOLD — DESIGN DECISION REQUIRED` | `NOT PROVABLE` — **el.15, from both sides independently** |

**Joint result: 22 of 22 covered on both sides. 0 of 22 declarable verified. Unchanged.**

### 4.2 What convening produced that not convening could not

The session was not a formality. Four results exist only because both sides were read together:

| # | Result | Why one side alone could not produce it |
|---|---|---|
| `JCP-01` | **`JT-04` is discharged** — *when financial recognition occurs* was `NOT DECIDABLE` because two Account packages held incompatible positions and neither knew of the other. Resolved on primary evidence at `SA_CORR2_01` §5 | The conflict was **inside** Accounting; Inventory could not see it, and neither Account package compared itself to the other |
| `JCP-02` | **`RISK-U03`'s ground is superseded** (§3) — the remedy changes from *specify* to *build and prove* | Inventory wrote the invariant set; the register that consumes it as a blocker is Inventory's own, one round earlier. Only a reader of **both rounds at once** sees the supersession |
| `JCP-03` | **Element 15 fails from both sides independently, for the same reason** — Inventory records *"no stable identity making retry safe"*; Accounting records *"no accounting-event identity and no idempotency key exist"*, and `XM-01` at `HOLD — DESIGN DECISION REQUIRED`. **This is one missing object, recorded twice, owned by neither** | Each side registered it as its own gap. Neither proposed to originate it, because each could reasonably assume the other would |
| `JCP-04` | **The COGS dependency is not the binding constraint, and the joint result proves it arithmetically** — elements 4 and 7 are the only COGS-caused ones, and elements 10 and 15 fail on every scenario regardless. *"Resolving the entire COGS Gap tomorrow would move the Inventory cross-proof result from 0 of 22 to 0 of 22."* CORR2 confirms this from the Accounting side too | The COGS gap is the loudest item in both programmes. Only the joint arithmetic shows it is not load-bearing for this control |

### 4.3 `JCP-03` promoted — the one item this session escalates as a design obligation

> **`C2-F-13`. The deterministic accounting-event identity is an object that both domains require,
> both domains have recorded as missing, and neither domain owns.**

`BD-ACC-01` already answers the ownership question — *Accounting Core owns the canonical immutable
Accounting Event Identity.* It is a **ruling with no contract**, which is `XD-06`, and here is what
that costs: element 15 blocks scenario 22 on the Inventory side and `FE-01` makes duplicate posting
reachable on the Accounting side, **and both were recorded as open by parties who each had grounds
to expect the other to close it.**

Owner: **SMEs Core**, to publish the contract. Boss confirms at the Functional Design gate. **This
is not a new Boss question** — the ruling exists.

---

## 5. The eleven agenda topics — dispositioned

| # | Topic | Disposition by this session |
|---:|---|---|
| 1 | Receipt posting | `PENDING` — el.10 |
| 2 | Delivery / COGS posting | **ADVANCED** — recognition point resolved (`C2-F-03`); `BP-02` shown unselectable on the current generation |
| 3 | Return basis conflict | `PENDING — INVENTORY INTERNAL RESOLUTION FIRST` — unchanged, not this session's to take |
| 4 | Adjustment | `PENDING` |
| 5 | Landed cost | `PENDING` |
| 6 | Manufacturing | **ADVANCED** — `SA-D20` supplies the missing half of `SA11-F-01` (`SA_CORR2_03` §3.4) |
| 7 | Price difference | **ADVANCED** — the product-mismatch filter is measured live: 13 rows drop layers, against a 14,335 control |
| 8 | Opening balance cross-proof | `PENDING` — el.14 |
| 9 | Monthly close sequence | `PENDING` — **and no accounting-period object exists** (`G-11`) |
| 10 | Year-end retained earnings | `PENDING — ACCOUNT HALF NOT YET JOINT-READY` |
| 11 | Product category dual ownership | **ADVANCED, AND ESCALATED** — this is `C2-D-03`: a kit and its components may sit in different Product Categories, and `BD-ACC-03A/03B` set policy at category level |

**Four of eleven advanced — topics 2, 6, 7 and 11. None closed. Seven remain `PENDING`.** All eleven
require either element 10 or a Boss decision.

*(**Corrected after adversarial challenge.** First published "Five … Six require". Counted by reading
the disposition column: `ADVANCED` = 4, `PENDING` = 7. 4 + 7 = 11.)*

### 5.1 The clean-room veto checkpoint was honoured

The convening brief required that Inventory's proposal to use *"an Accounting lock-exception model as
template"* be treated as **a clean-room VETO checkpoint at the start of the joint session, not
assumed**. It was tested. **CORR2's position: rejected as a template, adopted as a requirement**, in
the form already determined independently at `ND-07` — *a period lock is a property of the entry, not
of the path that reaches it.* The rationale is the evidenced two-path lock defeat, not the existence
of the Accounting model. Similarity is allowed; dependency is not.

---

## 6. Convening pre-conditions that remain open, stated rather than waived

| Pre-condition | Status |
|---|---|
| Inventory-side attendee / package reference | `NOT CONFIRMED` in the source brief. **CORR2 convened on the packages, not on named attendees** — this is a same-model internal proceeding and is labelled as such throughout |
| Neutral clean-room reviewer for the veto checkpoint | `NOT CONFIRMED`. The checkpoint was tested by this session, which is **not** neutral. Carried to `SA_CORR2_11` |
| Agenda scheduled | `ROUTED, NOT SCHEDULED` |

**This register does not claim that a Boss-convened joint session with independent parties has been
held.** It claims that the authorized proof activity was executed against the approved controls, on
existing evidence, by an internal body — which is what the master prompt authorized and all it
authorized.

---

## 7. What the joint proof determines for Boss

1. **The cross-proof is executed and its result is `0 of 22`, unchanged — and the reason is now
   exact.** It is element 10, unconditionally, on every scenario.
2. **The remedy has changed and nobody had noticed.** `RISK-U03`'s specification half is **done**.
   What remains is build-and-prove, which belongs to Pre-Test and Development, not to research or
   design. Commissioning further specification work here would duplicate 58 invariants across 35 artefacts.
3. **The COGS gap is not the binding constraint**, confirmed from both sides.
4. **One object — the deterministic accounting-event identity — blocks the most and is owned by
   nobody**, despite a ruling that assigns it. That is a contract to publish, not a decision to take.

---

`CP-SA-C2-30 — JOINT CROSS-PROOF COMPLETE (execution status).` The proof is complete; **its result
is that nothing is provable yet**, and the register says so.

Checkpoint completion is **not** Boss approval.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
