# 23 — P02 TARGETED CLOSURE: RECONCILIATION REGISTER

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-TARGETED-FORENSIC-CLOSURE-001`

## 1. Boss-Controlled Policy Versus Source Fact — Kept Separate

The directive requires these to be held apart, and the closure evidence makes that discipline sharp,
because **one deployment happens to match the target policy**.

| # | Statement | Class | Why it is that class |
|---|---|---|---|
| **BP-01** | **Invoice policy ≠ COGS recognition policy.** | **BOSS CONTROLLED — invariant** | A design invariant SMEsPlus adopts. The reference *couples* them (`02` §6): the cost quantity is taken from the invoice line. That coupling is the source fact; the separation is the policy. |
| **BP-02** | **For a normal perpetual storable target, COGS is recognised at DELIVERY.** | **BOSS CONTROLLED — target policy** | **NOT a source fact and NOT supported by the deployed evidence, even though one deployment matches it.** |
| **BP-03** | Revenue on billing versus on performance | **BOSS CONTROLLED — open** | Unresolved; carried from `04` §8. |

**`FACT VERIFIED` — the discipline point that BP-02 exists to protect.** The single database that
recognises cost through this process (`iSMEs`) does so **at delivery** — matching BP-02. **That is a
coincidence of configuration, not evidence for the policy.** It happens because that company has split
recognition off *and* its outbound stock accounts are typed as expense accounts. Change either setting and
the same product recognises cost at invoice, or nowhere. **A deployment matching a policy is not a source
fact about the policy**, and this package does not present it as one.

**`SUPPORTED INTERPRETATION` — and the closure evidence makes BP-02 harder, not easier, to implement on
the reference.** Under v19 — 92 of 93 deployed company records — **there is no delivery-time entry at all
for an ordinary customer sale** (`22` §3.2). Achieving "COGS at delivery" on the v19 line requires either
a location valuation account on every outbound path, or a mechanism the product does not provide. BP-02 is
therefore a **design requirement with a known implementation gap**, not a setting to switch on.

## 2. Six Tolerance-Zero Candidates — Reconciled

Each is re-stated with what the closure evidence added, and given a disposition.

| # | Candidate | Closure evidence | Disposition |
|---|---|---|---|
| **TZ-01** | Completed outflow with no financial record | **MEASURED — `22` §14.2.** On real-time-valued products, **1,044 layers carry no journal entry**; excluding zero-value and extreme rows, **291 layers carry a net −25,489,905.40 with no accounting entry at all**. The benign confound (16,075 manual-valuation layers) is separated out. | **CONFIRMED LIVE — magnitude measured, per-case cause `UNRESOLVED`.** Not closed. |
| **TZ-02** | Posting into a locked period is silently redirected; the redirect is capped at today and may land back inside the locked window | **91 of 93 deployed company records have NO lock date at all** (`22` TC-06). The control is not switched on in the estate. | **HOLD — and downgraded in practice, upgraded in principle.** Cannot fire where no lock exists; but it means the estate has *no* period control, which is worse. **Confirmed independently by P08.** |
| **TZ-03** | Matching and unmatching are not period-controlled | Same as TZ-02: no lock dates deployed, so nothing to bypass today. | **HOLD.** Structural finding stands. |
| **TZ-04** | A context sentinel disables the lock check entirely, including the irreversible lock | Unchanged. Not measurable from data. | **HOLD.** |
| **TZ-05** | A missing exchange rate silently substitutes an unrelated rate, or 1.0 | **MEASURED — `22` §14.5.** 34,733 foreign-currency lines; **2 posted with no rate on or before their date, both at an implied rate of exactly 1.000000**. Both are cancelled and net to zero. | **CONFIRMED REACHABLE AND DEMONSTRATED — nil material effect here.** The mechanism is no longer hypothetical. |
| **TZ-06** | A customer deposit is recognised as revenue when an account property is unset | **MEASURED — `22` §14.1.** The property is set **0** times in the deployed database, against sibling controls of 27 and 26 on the same mechanism. | **CONFIRMED LIVE DEFECT.** Deposits in this deployment are recognised as immediate revenue. **The only candidate the closure closed — and it closed against the system.** |

**`FACT VERIFIED` — of 6 tolerance-zero candidates, 5 are now measured against deployed data:**

| Candidate | Outcome of measurement |
|---|---|
| **TZ-06** | **CONFIRMED LIVE DEFECT** — deposits recognised as revenue |
| **TZ-01** | **CONFIRMED LIVE** — 291 layers, net −25.5M, no accounting entry; per-case cause unresolved |
| **TZ-05** | **CONFIRMED REACHABLE AND DEMONSTRATED** — fallback fired at exactly 1.0; nil material effect here |
| **TZ-02, TZ-03** | **NOT CURRENTLY FIRING** — because the control they subvert is not deployed at all (91 of 93 company records have no lock date). Not closure; a larger finding. |
| **TZ-04** | **UNMEASURABLE from data** — a code-path bypass, not a data state |

**None is closed in the sense EC-04 requires — closed means the risk is eliminated, and none is.** Three
moved from theoretical to demonstrated, which moves EC-04 **further from** satisfaction, not closer.

**None is closed in the sense EC-04 requires — closed means the risk is eliminated, and none is.** TZ-06 is
"closed" only in the sense that the question is answered: the answer is that the defect is live.

**`FACT VERIFIED` — a seventh candidate is raised by the closure:**

| **TZ-07** | **The deployed estate has no period control at all.** 91 of 93 company records carry no lock date of any kind. Every period-integrity finding in the package describes a control that, in practice, is switched off. | **NEW — OPEN.** |
| **TZ-08** | **The inventory valuation ledger and the general ledger disagree, undetected, by up to 9×10¹⁶.** 30 valuation layers carry values above 10¹²; 25 are linked to a journal entry; **the general ledger contains no line above 10¹² across 447,384 lines.** Measured — `22` §14.3–14.4. | **NEW — CONFIRMED LIVE.** Cause is P03/Inventory's; the **absent tie-out** is P02's and P08's. |

## 3. Eight Exit Criteria — Reconciled

| EC | Before closure | After closure | Movement |
|---|---|---|---|
| **EC-01** Scope bounded | PARTIAL | **PARTIAL** | Database denominator now closed (6 of 6, deduplicated, with a positive control). Source denominator now spans **two generations**, which the previous scope did not declare. Eight business scenarios still open. |
| **EC-02** Enumeration converged | NOT | **NOT** | The closure produced a **generation split that falsifies the scoping of the whole cost analysis** (C-20). That is a material delta, so convergence is further away, not closer. |
| **EC-03** Unknown exhausted | PARTIAL | **PARTIAL** | C-04 now has a precise, evidenced verdict — **not exhibitable in the available estate** — and a precisely specified requirement. Four measurable-but-unmeasured items are newly named. |
| **EC-04** Tolerance-zero closed | NOT | **NOT** | 0 of 6 eliminated. **Two confirmed LIVE by measurement** (TZ-01, TZ-06), and **two new candidates raised** (TZ-07, TZ-08). The criterion moved decisively **away** from satisfaction. |
| **EC-05** Contradiction resolution | PARTIAL | **PARTIAL** | 20 contradictions registered, three added by the closure (C-18, C-19, C-20), all with disposition and lineage. |
| **EC-06** Negative claim controlled | NOT | **NOT** | The closure found **two further** evidence-base failures of the same class as `RE-13`: the archive count was wrong (5 vs 6) and the tooling was not exhausted (two archives unreadable with the default binary). **A control that fails a third time in the same package is not a control.** |
| **EC-07** Two consecutive clean passes | NOT | **NOT** | A second independent challenge is running against the closure; the first was not clean. |
| **EC-08** Knowledge package complete | PARTIAL | **PARTIAL** | Deployed evidence now substantial. **Runtime evidence still absent** — and it is the only thing that can close C-04. Jira lineage still absent. |

**`FACT VERIFIED` — 0 satisfied, 4 partial, 4 not satisfied.** Unchanged in count. **The composition
changed for the worse in two places** (EC-02 and EC-06) and for the better in one (EC-03).

## 4. Scope-Aware Determination For The Newly Discovered Objects

Per `SMEPLUS-26-09-04-ACC-REV2-CORR1`. **Tenant and company context are not forced.** New objects only —
the existing matrix in `20` stands.

| Object | Ownership | Configuration | Execution | Operational | Financial | Reference | Tag |
|---|---|---|---|---|---|---|---|
| **v19 company valuation mode** (`inventory_valuation`) | COMPANY | **COMPANY** | COMPANY | COMPANY | **COMPANY — it decides whether cost of sales exists at all** | — | `FACT VERIFIED` at company level |
| **v19 company costing method** (`cost_method`) | COMPANY | COMPANY | COMPANY | COMPANY | COMPANY | — | `FACT VERIFIED` |
| **v19 company stock journal / valuation account** | COMPANY | COMPANY | COMPANY | — | **COMPANY** | — | `FACT VERIFIED` |
| **Location valuation account** (v19) | **COMPANY** — a location belongs to a company | COMPANY | COMPANY | COMPANY | **COMPANY** | — | `FACT VERIFIED` |
| **`product.value` change history** (v19) | COMPANY | — | COMPANY | — | **COMPANY** | — | `FACT VERIFIED` |
| **Product valuation mode** (category property, else company) | **TENANT** for the product identity; **COMPANY** for the valuation property | **COMPANY** | COMPANY | COMPANY | COMPANY | TENANT may reference | `DESIGN CANDIDATE` for the tenant half |

**`FACT VERIFIED` — SC-04 (NEW SCOPE FINDING).** v19 **moves the valuation configuration up from the
product category to the company**, and the category property becomes an optional override. This is a
**scope migration in the reference itself**: a setting that was per-category-per-company becomes
per-company with a per-category exception.

**Scope consequence.** It makes the *default* correct-by-construction at company level — an improvement on
v18, where a company-dependent property had to be set on every category — but it also means **one setting
now decides whether an entire company recognises cost of sales**, which is exactly the concentration the
package's `DC-02-01` warns against. **Both readings are recorded; neither is resolved here.**

**`SUPPORTED INTERPRETATION` — the three scope holds from `20` §4–§6 are unaffected** by the closure
evidence. Currency-rate scope, chart-of-accounts scope and intercompany execution scope remain
`HOLD — SCOPE EVIDENCE REQUIRED` and are routed to P11.

## 5. Event Durability — Revalidated Against Deployed Evidence

| Layer | Source position | Deployed position | Net |
|---|---|---|---|
| **Physical event** | immutable — a completed outflow cannot be cancelled or reversed | 103,949 movements in the one archive with volume | **strongest layer; unchanged** |
| **Inventory valuation** | v18: a layer row keyed only by creation timestamp, no accounting date of its own. **v19: the model does not exist** | 74,982 rows in v18; **table absent in all five v19 archives** | **v19 REMOVES this layer entirely** |
| **Accounting event** | reversible; reset-to-draft destroys derived lines; the guard that would prevent it is wired purchase-side only | 0 cost lines exist to destroy | **unchanged in principle** |
| **Settlement history** | freely destructible; **not lock-date gated** | **91 of 93 company records have no lock date** | **worse in practice than in principle** |
| **Reconciliation history** | same as settlement | same | **worse in practice** |

**`FACT VERIFIED` — TC-19 restated as a durability finding.** The generation change **deletes a durability
layer**. In v18 the valuation layer is an immutable record of what a unit was worth when it moved. In v19
there is no such record; `product.value` logs **manual value changes**, which is a change log, not a
valuation ledger. **A design that relies on being able to ask "what was this unit valued at when it left?"
cannot ask that question of a v19 database.**

## 6. Peer Handoffs

| To | Item | Status |
|---|---|---|
| **P11** | `22` TC-01…TC-19 in full — none of it existed when P11 synthesised | **NEW INPUT** |
| **P11** | C-19 — P02 accepts P06's `P06-XC-01`; agrees with the proposed reconciliation | **AGREED, closes a P11 candidate** |
| **P11** | The generation split (C-20) — **every peer's cost analysis needs the same v18/v19 scoping check** | **ESCALATION** |
| **P01** | P02 independently confirms the v19 structural absence from the **outbound** side; P01 found it inbound. The withdrawn P02 symmetry question is now answered: **neither direction has the structure in v19** | **RECONCILED** |
| **P01, P10** | **Denominator correction: 6 distinct archives, all 6 readable.** Both peers recorded 4 and 3-of-4 respectively; two archives need PostgreSQL 18 tooling, which is installed | **CORRECTION ISSUED** |
| **P06** | P02 adopts P06's sharper `root_id` statement into `20` SF-06 | **ADOPTED** |
| **P07** | C-18 cash-basis switch; and `P02-F-50`/`P02-F-52` sales-side withholding and tax-group findings, which P07 reached independently | **ROUTED** |
| **P08** | Corroboration of the lock-relocation and no-event-object findings | **CORROBORATED** |
| **P03** | Cost-injection counterpart; the v19 generation change affects P03's cost analysis too | **ESCALATION** |

**`PEER DEPENDENCY OPEN`** on P01, P03, P06, P07, P08, P10 and P11 — **none blocks a P02 conclusion.**
Every P02 finding above stands on P02's own verified evidence.

## 7. What Remains Measurable And Was Not Measured

Named precisely, because "maximum available evidence" is a claim that must be falsifiable.

1. ~~Valuation layers on real-time categories with no journal entry~~ — **MEASURED**, `22` §14.2.
2. ~~The down-payment account property~~ — **MEASURED**, `22` §14.1.
3. ~~Multi-currency receivables and applied rates~~ — **MEASURED**, `22` §14.5.
4. **Delivered-not-invoiced ageing** in `iSMEs` — quantifies the residual class directly.
5. **The four unexamined custom-addon roots** for O2C overrides — P06 and P08 both found their
   highest-severity items in custom modules, and P02 has examined **none**.

**`FACT VERIFIED` — item 5 is the largest unexamined surface in this package.** Two peer processes found
their most severe findings in custom modules; P02's declared path set contains **no custom module at all**.
That is a declared exclusion, not a verified absence, and it is the first thing a next round should take.
