# 36 — G02-P02 END-TO-END O2C ACCOUNTING TRUTH MATRIX

`LAYER 2 — AUDIT QUARANTINE.` Task **C7**. Baseline `ff8be51`.

**The four evidence classes are kept apart everywhere below:**

`SOURCE CAPABILITY` != `CONFIGURATION REACHABILITY` != `DEPLOYED REALITY` != `RUNTIME PROOF`

| Class | What it means here | How much of it exists |
|---|---|---|
| **SOURCE CAPABILITY** | the standard code can do it | v18 + v19 read; v16/v14 roots partial (59 / 127 dirs) |
| **CONFIGURATION REACHABILITY** | a setting combination reaches it | derived from source + `ir_default` |
| **DEPLOYED REALITY** | it is observed in a deployed database | 17 databases, 4 generations, 2,553,914 journal lines |
| **RUNTIME PROOF** | it was observed executing | **almost none — see §3** |

---

## 1. The Matrix

| # | Stage | Business fact | Canonical owner (benchmark) | SMEsPlus proposed owner | Trigger | Occurrence date | Recognition / accounting date | Scope | Journal / subledger effect | Source | Deployed | Runtime | Contradiction / gap | Handoff |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Quotation / Order | a promise exists | `sale.order` | same | confirm | order date | **none** | COMPANY | **none** | ✔ | ✔ 172k+ lines measured | — | order carries no accounting identity | P02 |
| 2 | Delivery / performance | goods left | `stock.move` / `stock.picking` | same | `button_validate` | movement date | **movement date, not an accounting date** | COMPANY | none by itself | ✔ | ✔ | — | `P02-F-16b` unpicked completion via mixed picking | P02 |
| 3 | Inventory / valuation | value left stock | `stock.valuation.layer` (v14–18); **model deleted in v19** | **single owner required** | movement, gated on `property_valuation='real_time'` | movement date | posting date of the generated entry | COMPANY | Dr interim / Cr valuation — **only if configured** | ✔ | ✔ 47,242 layers → **0 entries** (`551ab874`) | — | **`P02-F-28d`** outcome 3 measured | P02 → P08 |
| 4 | **COGS** | cost of the thing sold | v18 invoice-side generator gated on `anglo_saxon_accounting`; v19 `…realtime…`, anglo gate removed | **`BP-02`: physical delivery / stock-out** | invoice post (v18) / invoice (v19) | — | invoice accounting date | COMPANY | Dr expense / Cr interim | ✔ | **`display_type='cogs'` = 0 in all 17 DBs** | **none** | **the mechanism has never executed anywhere measurable** | P02 |
| 5 | Invoice | a receivable exists | `account.move` | same | `action_post` | invoice date | **accounting date, silently re-dated by lock** | COMPANY | Dr AR / Cr revenue / Cr tax | ✔ | ✔ | — | `P02-F-08b` lock redirect capped at today | P02 → P08 |
| 6 | Revenue / AR / tax | earned + owed | `account.move.line` | same | with the invoice | invoice date | accounting date | COMPANY | as above | ✔ | ✔ | — | **`BP-03` open**: billing vs performance | **P10** |
| 7 | Receipt | cash arrived | `account.payment` | same | register | payment date | payment accounting date | COMPANY | Dr bank/outstanding / Cr AR | ✔ | ✔ | — | `CA-04` multi-deduction widens the residual route | **P06** |
| 8 | Allocation / reconciliation | receipt meets receivable | `account.partial.reconcile` | same | reconcile | — | — | COMPANY | none | ✔ | ✔ | `TC-16` outbound stock accounts `reconcile=false` — matching impossible in principle | P02 → P06 |
| 9 | Bank confirmation | the bank agrees | `account.bank.statement.line` | **needs a first-class confirmed flag** | statement | statement date | statement accounting date | COMPANY | Dr bank / Cr outstanding | ✔ | ✔ | **P06: no field means "the bank confirmed this"** | **P06** |
| 10 | Return | goods came back | reverse `stock.move` | same | return picking | movement date | — | COMPANY | reverses valuation only | ✔ | ✔ | independence from the credit note not enforced | P02 → P08 |
| 11 | Credit note | the receivable reduces | `account.move` type `out_refund` | same | post | credit date | accounting date | COMPANY | Dr revenue / Cr AR | ✔ | ✔ | — | return ↔ credit note not linked | P02 |
| 12 | Refund | cash returned | `account.payment` | same | register | payment date | accounting date | COMPANY | Dr AR / Cr bank | ✔ | ✔ | — | — | P06 |
| 13 | Correction / reversal | an entry was wrong | `account.move.reverse` | **event identity required** | reverse | reversal date | accounting date | COMPANY | mirror entry | ✔ | ✔ | **physical event immutable, accounting event reversible** | P02 → P11 |
| 14 | Period close | the period is shut | company lock dates | **close-means-closed** | manual / `date_range` archive | — | — | COMPANY | none | ✔ | ✔ | **`CA-02`: a cron named "close old periods" sets no lock and blocks no posting** | **P08** |

---

## 2. `P02-F-36a` — Where The Spine Actually Breaks

Reading the matrix down the **date** columns rather than across:

- Stages 1–3 carry **occurrence** dates (order, movement) and **no accounting date at all**.
- Stages 5–13 carry **accounting** dates, and stage 5's is **system-derived and silently re-datable**.
- **Stage 4 — COGS — is the join between the two halves, and it is the one stage with zero deployed
  evidence of ever having run.**

**The two halves of O2C are joined by the single mechanism that has never executed in any of 17
databases.** That is the package's headline restated structurally: not "a setting is wrong" but "the
bridge between the physical and accounting timelines is the least-exercised code in the process".

## 3. `P02-F-36b` — The Runtime Column Is Almost Empty, And That Is The Honest Finding

**Fourteen stages. Runtime proof exists for none of them as a *transaction*.** The only runtime facts
obtained this round are **configuration** facts (`P02-F-33b/c/d`), read from a live but
**never-transacted** lab. `C-04` is the request to fill exactly one cell of that column (§`33`).

**No stage below is promoted on the strength of source capability alone.** Where deployed reality
contradicts source capability — stage 4 most sharply — **deployed reality governs the finding and source
governs only the explanation.**

## 4. Scope Column — `CORR1` Compliance

Every stage above resolves at **COMPANY** scope. **No stage requires TENANT and none is PLATFORM.**
Two qualifications, both evidenced:

- `SF-03` — company-dependent configuration (valuation mode, the three stock accounts) resolves from the
  **environment** company, not the record's. `SF-09` — v19 resolves one value from **two** company
  sources in a single expression.
- `CA-01` — one deployment has added a genuine **structural** product↔company scope control at the data
  layer, defaulting to *global = allowed*.

**`MISSING REQUIRED SCOPE = DENY` is satisfied nowhere in the benchmark.** The closest real
implementation is `CA-01`, and it implements *conflict = deny*, not *missing = deny*.
