# 03 — ASSET BLOCKER RECONCILIATION REGISTER

**LAYER 2 — AUDIT QUARANTINE.** Mandatory first action under §3 of the governing prompt.

---

## 1. Method

The authoritative blocker population was taken **from repository evidence**, not from
the prompt's arithmetic and not from memory. Two documents in the controlled baseline
(`6c7512e`) state a blocker population, and **they do not agree**. That disagreement
is reported rather than resolved by preference.

## 2. The source disagreement, stated plainly

| Source | Blocker list |
|---|---|
| `41_UNRESOLVED_EVIDENCE_REGISTER.md` §Summary | `UNR-02`, `UNR-08`, `UNR-03`, `UNR-B3`, `UNR-23`, and *"the design decision behind item 2"* — a **terminating rule** for cumulative internal usage |
| `44_BOSS_FINAL_REVIEW_PACK.md` §Y | `UNR-02`, `UNR-08`, `UNR-03`, `UNR-23`, `UNR-B3` (unbounded accumulation), and `UNR-18` — **where unabsorbed depreciation goes** |

Five of six are identical. The sixth differs: `41` names a *terminating rule for the
accumulator*; `44` names *unabsorbed depreciation*. `41` additionally lists `UNR-18`
in its **non-blocking** tier, which is a self-inconsistency inside the baseline.

**Reconciliation ruling.** Both candidate sixth items are carried, giving a
**reconciled population of seven distinct items**, of which six were reported. This
is deliberately conservative: it cannot understate what the Boss must decide. The
prompt's expected population of six is therefore **confirmed as reported** and
**exceeded by one on reconciliation**. The number 4 was not forced anywhere.

| | Count |
|---|---|
| Reported by the baseline | 6 |
| Distinct on reconciliation | **7** |
| Delta | +1 — `UNR-18` and the accumulator terminating rule are **different questions**, not two names for one |

## 3. Mapping the two resolved Boss decisions onto the register

| Boss decision | Closes | Basis |
|---|---|---|
| `BD-01` — no cap, no cut-off, no reduction of residual book value | `UNR-B3` **and** the terminating-rule item | The decision answers both halves: no bound, and the terminating *condition* is operational eligibility for production use, not an amount |
| `BD-02` — 100% attribution, cause-based non-productive classification, nothing carried forward unclassified | `UNR-18` | The decision states where unabsorbed depreciation goes: into a classified non-productive bucket, in the period |

Both closures are **CLOSED — BOSS DECISION**. Neither required research.

## 4. Reconciled register — full record per §3

### `BLK-01` (`UNR-02`) — Which day convention the live assets actually use

| | |
|---|---|
| Original source | `41` Tier 1, `44` §Y1 |
| Original description | The prorata computation mode across the 280 assets was never captured; the model export's provenance is unclear |
| Original status | BLOCKING — one pilot-database query |
| **Current status** | **HOLD — UAT EVIDENCE REQUIRED** |
| New evidence this session | None. The UAT was unreachable (`01` §6) |
| Boss decision reference | — |
| Remaining evidence requirement | Distribution of the prorata computation mode across all 280 asset records, grouped; plus the origin of the Asset Model export |
| Contradiction status | Related to `CTR-01` (baseline), unchanged |
| Closure eligibility | Immediate, on one grouped read |
| Gate impact | **Blocks the migration decision.** Does not block the SMEsPlus design, because `19` §4 mandates an explicit recorded convention per asset regardless of what the live data shows |

### `BLK-02` (`UNR-08`) — Whether several assets share one equipment record

| | |
|---|---|
| Original source | `41` Tier 1, `44` §Y2 |
| Original description | The custom link has no uniqueness constraint and nothing reports duplicates |
| Original status | BLOCKING for costing |
| **Current status** | **HOLD — UAT EVIDENCE REQUIRED** |
| New evidence this session | Partial and **adverse to the original framing**: the link does carry a *soft* guard (`06` §5). The guard reduces the probability of duplicates created through the screen; it does not prevent duplicates from import, from direct write, or from multiple draft assets. The question is unchanged; only the prior probability moves |
| Boss decision reference | — |
| Remaining evidence requirement | Count of assets with the link populated; count of equipment records referenced by more than one asset; parent/child relationships among the 280 |
| Contradiction status | None |
| Closure eligibility | Immediate, on two counts |
| Gate impact | **Blocks the per-machine costing design** — uniqueness is a correctness precondition, not data hygiene |

### `BLK-03` (`UNR-03`) — Does Thai practice permit depreciation absorbed into inventory?

| | |
|---|---|
| Original source | `41` Tier 2, `44` §Y3 |
| Original description | "Not a software question. Precondition for the entire SMEsPlus costing proposition" |
| Original status | BLOCKING — Accounting-Tax track |
| **Current status** | **CLOSED — EVIDENCE VERIFIED** |
| New evidence this session | **TAS 2 *สินค้าคงเหลือ*, ¶12, standard text.** Conversion cost of inventories comprises directly related costs plus a systematic allocation of fixed and variable production overhead, and fixed production overhead is defined to include *"ค่าเสื่อมราคา และค่าบำรุงรักษาอาคารโรงงาน อุปกรณ์โรงงาน และสินทรัพย์สิทธิการใช้ที่ใช้ในกระบวนการผลิต"* — the depreciation and maintenance of factory buildings, factory equipment and right-of-use assets used in the production process. Corroborated by TFAC's own TAS 16 manual: depreciation is recognised in profit or loss *except where it must be included in the carrying amount of another asset* |
| Boss decision reference | — |
| Remaining evidence requirement | **None for the question as asked.** |
| Contradiction status | None. The finding is stronger than the question: absorption is not merely permitted, it is **required** |
| Closure eligibility | Closed |
| Gate impact | **The costing proposition's statutory precondition is satisfied.** It also creates `BLK-06` below |

### `BLK-04` (`UNR-23`) — How are off-balance accounts treated in Thai statutory statements?

| | |
|---|---|
| Original source | `41` Tier 2, `44` §Y4 |
| Original description | Never established. The management-ledger design rests on it |
| Original status | BLOCKING — Accounting-Tax track |
| **Current status** | **CLOSED — EVIDENCE VERIFIED** (for the question as asked) |
| New evidence this session | **ประกาศกรมพัฒนาธุรกิจการค้า — prescribed line items, แบบ 2 (บริษัทจำกัด).** The prescribed statement of financial position, statement of comprehensive income, statement of changes in equity and cash-flow statement contain **no off-balance-sheet, memorandum or นอกงบดุล line item of any kind.** Verified by exhaustive text search of the prescribed form |
| Boss decision reference | — |
| Remaining evidence requirement | None for presentation. See the residual note below |
| Contradiction status | None |
| Closure eligibility | Closed |
| Gate impact | **The management ledger has no statutory presentation surface**, which is exactly the isolation the Boss required. Statutory contamination is therefore not a presentation risk; it can only arise if a management amount is posted to an on-balance account, which `05` §7 shows the platform structurally prevents within a single entry |
| **Residual, declared** | Absence of a prescribed line is a fact about **presentation**. It is not affirmative authorisation for the **bookkeeping**. Whether Thai bookkeeping law constrains a memorandum ledger is a distinct, narrower question, carried as `UNR-C-04` in `22` §5 at Low severity. It does not block design |

### `BLK-05` (`UNR-B3` + terminating rule) — May internal usage accumulate without bound?

| | |
|---|---|
| Original source | `41` Tier 2 and `41` §"six items the experts added" item 2; `44` §Y5 |
| Original status | BLOCKING for the management ledger |
| **Current status** | **CLOSED — BOSS DECISION** (`BD-01`) |
| New evidence this session | Corroborating, not deciding: nothing in the reference product, in TAS 2, in TAS 16 or in the prescribed statutory forms constrains a memorandum accumulator, because none of them recognise one |
| Remaining evidence requirement | None |
| Contradiction status | The reviewers' split recorded in the baseline (`D5-01`) is **resolved by decision**, not by evidence. Recorded as such |
| Gate impact | Closed |

### `BLK-06` (`UNR-18`) — Where does unabsorbed depreciation go?

| | |
|---|---|
| Original source | `41` Tier 3 (non-blocking) and `44` §Y6 (blocking) — the baseline's own inconsistency |
| Original status | Disputed within the baseline |
| **Current status** | **CLOSED — BOSS DECISION, reinforced by evidence** (`BD-02`) |
| New evidence this session | **TAS 2 ¶13, standard text**, independently reaches the same destination: *"ค่าใช้จ่ายในการผลิตที่ไม่ได้ถูกปันส่วนให้รับรู้เป็นค่าใช้จ่ายในงวดที่เกิดค่าใช้จ่ายนั้น"* — unallocated production overhead is recognised as an expense **in the period in which it is incurred**. The Boss's rule and the standard agree |
| Remaining evidence requirement | None for the destination. The *mechanism* raises `BLK-07` |
| Gate impact | Closed |

## 5. New blockers raised by this session

Honest reconciliation adds as well as removes. Two items became blocking **because**
`BLK-03` closed.

### `BLK-07` — The allocation denominator must be normal capacity, not actual hours

| | |
|---|---|
| Source | TAS 2 ¶13, obtained this session |
| Description | The standard requires fixed production overhead to be allocated **on the basis of the normal capacity of the production facilities**, and states that the amount allocated per unit **shall not increase when production falls or ceases**. Allocating a month's depreciation across that month's *actual* machine hours does exactly what the standard forbids: in a low-production month the per-unit charge rises |
| Why it is new | It could not arise while `BLK-03` was open. It is a direct consequence of closing it |
| Impact | Determines the arithmetic of the productive allocation. It does **not** contradict `BD-02` — 100% attribution remains satisfiable, and `09` §3 shows the one reading under which both hold |
| Status | **HOLD — DESIGN DECISION REQUIRED** (Boss confirmation of the reading in `09` §3, plus who sets normal capacity and how often) |
| Owner | Boss, with the Accounting-Tax track |
| Blocks | The allocation-driver selection in `11` and the period-close model in `13` |

### `BLK-08` — Planned maintenance sits inside normal capacity; unplanned downtime does not

| | |
|---|---|
| Source | TAS 2 ¶13, obtained this session |
| Description | Normal capacity is defined *"โดยคำนึงถึงกำลังการผลิตที่สูญเสียอันเกิดจากการบำรุงรักษาตามแผนที่วางไว้"* — taking into account capacity lost to **planned** maintenance. Planned maintenance is therefore already inside the rate and is absorbed into product cost; unplanned breakdown and abnormal idleness are not, and fall to period expense |
| Why it is new | The Boss's cause list (`BD-02`) treats MAINTENANCE as a single non-productive category. The standard splits it |
| Impact | The non-productive taxonomy needs one more axis — planned versus unplanned — or MAINTENANCE must be split into two causes. Small change, real consequence: getting it wrong misstates both inventory and period expense |
| Status | **HOLD — DESIGN DECISION REQUIRED** |
| Owner | Boss |
| Blocks | The non-productive model in `09`; nothing else |

## 6. Reconciled position

| Status | Count | IDs |
|---|---|---|
| CLOSED — EVIDENCE VERIFIED | **2** | `BLK-03`, `BLK-04` |
| CLOSED — BOSS DECISION | **2** | `BLK-05`, `BLK-06` |
| HOLD — UAT EVIDENCE REQUIRED | **2** | `BLK-01`, `BLK-02` |
| HOLD — DESIGN DECISION REQUIRED | **2** (new) | `BLK-07`, `BLK-08` |
| **Total open** | **4** | |

**The prompt's expected remaining population of 4 is met — but not by the composition
it expected.** The expectation was 2 UAT plus 2 unresolved decision/research items,
with the two Accounting-Tax questions still open. In fact **both Accounting-Tax
questions closed on primary statutory evidence**, and **two new design decisions
opened in their place**, created by those closures. The arithmetic coincides; the
substance moved. That movement is the main result of this session and is not a
bookkeeping accident.
