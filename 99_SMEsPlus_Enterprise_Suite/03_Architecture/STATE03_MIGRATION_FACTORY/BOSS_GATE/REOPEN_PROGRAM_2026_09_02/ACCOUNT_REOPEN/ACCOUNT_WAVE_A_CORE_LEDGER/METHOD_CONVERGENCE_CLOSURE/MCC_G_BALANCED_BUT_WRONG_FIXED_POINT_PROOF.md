# MCC_G — BALANCED-BUT-WRONG FIXED-POINT PROOF

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-MCC-001` · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver.**
> **The instruction is explicit: do not optimise for increasing the count.** Every addition below
> arrived as a by-product of proving `GB-03`, `FX-08` or a gating unknown. None was hunted for its
> own sake, and two candidates were **rejected** on verification (§5).

---

## 1. The test applied to every class

For each class, four questions, and a class is only *established* when all four are answered:

`Can debit = credit still hold?` · `Can the ledger and trial balance still appear internally
consistent?` · `What independent control detects the semantic error?` · `What evidence proves that
control exists?`

---

## 2. The 19 inherited classes, re-tested against the round instruction's challenge list

| Dimension the instruction requires | Inherited class exists? | Instances | Status after this round |
|---|---|---|---|
| wrong FX | yes | many | **WIDENED** — §3 `BW-28`, `BW-29`, `BW-30`, `BW-31` |
| wrong date | yes | ≥1 | unchanged |
| wrong period | yes | ≥1 | **WIDENED** — `T0-08`, entry number vs accounting date |
| wrong company | yes | several | **WIDENED** — §3 `BW-32` |
| wrong tenant | yes | — | unchanged; reduces into `GB-01` |
| wrong account | yes | ≥1 | **WIDENED** — §3 `BW-32`, `BW-33` |
| wrong journal | yes | ≥1 | **WIDENED** — `T0-08` |
| wrong partner | yes | ≥1 | unchanged |
| wrong source linkage | yes | ≥1 | **WIDENED** — §3 `BW-32` |
| duplicate accounting event | yes | ≥1 | **WIDENED** — `T0-08` |
| missing accounting event | yes | ≥1 | **WIDENED** — §3 `BW-32` (no intercompany balance created) |
| wrong reversal lineage | **class exists, ZERO instances** | 0 | **STILL ZERO AND STILL NEVER SEARCHED.** `MCU-15`, class `C` |
| wrong reconciliation state | yes | ≥1 | **WIDENED** — §3 `BW-32` |
| **wrong opening provenance** | **class existed, ZERO instances** | 0 | **NO LONGER EMPTY** — §3 `BW-30` |
| wrong lock behaviour | yes | ≥1 | **WIDENED** — `T0-10` |
| wrong account/currency ownership | yes | ≥1 | **WIDENED** — §3 `BW-28`, `BW-31` |
| unauthorised but balanced posting | yes | ≥1 | **WIDENED** — `T0-10` |
| stale configuration | yes | ≥1 | **WIDENED** — §3 `BW-30` |
| fallback preserving debit=credit but corrupting valuation | yes | several | **WIDENED** — §3 `BW-28`, `BW-29`, `BW-31` |

> **Two classes were empty when this round began. One is now populated by a verified instance; the
> other has still never been searched.** That asymmetry is the single most useful thing this section
> can tell Boss: **the one empty class that was searched turned out to contain a real defect on the
> first look.** It is not evidence that the other is empty. It is evidence that emptiness in this
> taxonomy has so far meant *unsearched*, not *absent*.

---

## 3. New cases established this round

Each is `VERIFIED FACT` at source unless marked otherwise. `BW-16` is **withdrawn** (`MCC_C` §6);
the register's floor therefore moves 29 → **35** (29 − 1 + 7).

### `BW-28` — an amount is posted at a rate the report converting it cannot see

**Mechanism.** The posting-time resolver **admits** a company-less rate row. Every one of the
reporting currency table's builders **excludes** it — SQL equality never matches a null — and then
substitutes **par** through an undeclared `ELSE 1`.

| Question | Answer |
|---|---|
| Debit = credit? | **Yes.** All items on the entry share one factor |
| Ledger internally consistent? | **Yes.** The trial balance foots in both the ledger and the report, at different values |
| Detecting control? | **None.** The error is in the correspondence between two resolvers, not inside either |
| Evidence the control exists? | **None found.** Six resolvers admit the row; six refuse it; nothing reconciles them |

### `BW-29` — the undated earliest-rate fallback

**Mechanism.** When no rate exists at or before the posting date, the resolver runs a **second query
with no date bound at all** and takes the **earliest rate ever recorded** for that currency in scope.
Par is only the *third* outcome.

> **This is more dangerous than par and the programme has been tracking the wrong one.** Par is
> visible to an attentive reader; a real-looking historical rate is not. It applies to **every**
> company, including single-company installations.

### `BW-30` — opening and onboarding valued at a 2010 rate

**Mechanism.** A demo-seeded or template-cloned database carries **162** shipped rate rows, **157 of
them dated `2010-01-01`**, owned by the root company active at installation. Any company inside that
root's tree that has not loaded its own rates resolves **every** foreign-currency posting — including
opening balances — at the 2010 rate, by `BW-29`. A **second root company** in the same database sees
none of them and gets **par** instead.

> **Two different wrong answers from one seeding decision, neither announced.** This is the instance
> that empties the *wrong opening provenance* class of its emptiness.
> **Corrected mechanism** — the rows are root-company, not company-less; see `MCC_E01 MCCX-01`.
> The correction changes the *owner* of the rows and **not** the consequence.

### `BW-31` — v19 aggregates monetary columns at today's rate, outside every record rule

**Mechanism.** The v19 ORM **core** adds a raw-SQL rate resolver used by grouped monetary
aggregation. It converts at **today**, not at each record's date; it bypasses every record rule; and
when no rate exists at or before today it takes the **earliest FUTURE rate** — a fourth fallback
semantic, disagreeing with all three others.

| Question | Answer |
|---|---|
| Debit = credit? | **Not applicable, and that is the point.** This is an aggregation, not a posting — the underlying entries are untouched and remain correct |
| Ledger internally consistent? | **Yes.** Only the *displayed total* is wrong |
| Detecting control? | **None.** The number appears in an ordinary list or pivot column |
| Evidence? | `VERIFIED FACT` at the v19 ORM core; **zero occurrences in either v18 core** |

**Gate significance:** it is on the version SMEsPlus targets, and it is reachable from any monetary
column aggregated in any list or pivot view.

### `BW-32` — a receivable settled by cash that never entered its company

**Mechanism.** The sole eligibility guard on reconciliation tests the **root**, not the company. For
items in two branches of one root the guard passes. The settlement record is then assigned to one of
the two companies by a heuristic; the exchange-difference entry's company is a two-record set
**truncated to its first element**, so the FX result is booked in an arbitrarily chosen legal entity
using that entity's journal and accounts on lines carrying the other's; and the resulting link is
written onto both companies' items by **raw SQL**, below the ORM, the record rules and every lock
check. The reconciliation models carry **no record rule anywhere in the tree** and full write rights
for ordinary accounting roles.

| Question | Answer |
|---|---|
| Debit = credit? | **Yes**, in every move involved |
| Ledger internally consistent? | **Yes**, in both companies separately |
| Detecting control? | **None.** No assertion that a settlement's two legs share a company; no completeness report grouping matched pairs by company |
| Evidence? | `VERIFIED FACT` (mechanism) · `NOT PROVEN` (runtime — not executed) |

**No intercompany balance is created.** The two companies' books each foot, and between them an
amount has moved with no carrier.

### `BW-33` — a control-account attribute silently flipped by imported data

**Mechanism.** During import matching, an account that does not permit reconciliation is **switched to
permit it**, with an informational log line and no user-visible message or approval.

`VERIFIED DEFECT`, minor severity, and it belongs in this taxonomy because the resulting entries
balance and the changed configuration is invisible afterwards.

### `BW-34` — a posted move rewritten through a suppression flag on the bank path

**Mechanism.** The list of fields unmodifiable on a posted move is exempted under a skip flag whose
**only production consumers in the accounting addon** are four writes to **posted** moves in the
bank-statement path. That flag sits inside a bucket of 48 generic skip tokens that was **counted and
never assessed**.

---

## 4. Tolerance-zero position — three boundaries added

| id | Boundary | Status |
|---|---|---|
| `T0-01` … `T0-06` | inherited | **UNRESOLVED**, unchanged |
| `T0-07` | Cross-company rate resolution in raw SQL, outside every record rule, with an undeclared par fallback | **CHARACTERISED — and worse than registered.** 8 raw-SQL reads over three addons; **four** distinct fallback semantics, not one; the two halves of the system disagree about the company-less row. **UNRESOLVED** |
| **`T0-08`** | **Entry identity** — one posted entry, one unambiguous immutable number, unique within the company and the period | **NEW.** Six independent weakening mechanisms, including a **declared uniqueness constraint whose definition string is empty**, a real control scoped by **journal rather than company**, a lock documented as conditional, a missing index degrading to a **log line**, a wizard that **deliberately blanks the number to escape the index**, and a database-wide key disabling number/date alignment. **UNRESOLVED** |
| **`T0-09`** | **Declared-but-inert control** — a control present to a reader and absent to the machine | **NEW.** Two bounded instances: **16** company-consistency guards on the company model, on the destination accounts of automatically generated ledger facts, where automatic checking is never enabled and the check is never invoked; and the empty constraint definition above. **UNRESOLVED** |
| **`T0-10`** | Cross-company creation and revocation of the control that relaxes the period lock | **NEW.** `MCU-10`. **UNRESOLVED** |

**Ten boundaries. None resolved. Tolerance = 0 is not met, and `CONDITIONAL PASS` remains unavailable
by rule rather than by judgement.**

---

## 5. Candidates REJECTED on verification

Recorded so the count is not read as a target.

| Candidate | Why rejected |
|---|---|
| A rounding asymmetry in a cross-company transfer wizard | **VERIFIED SAFE.** A branch cannot hold a currency different from its root's, enforced at four layers, so the asymmetry has no state in which it can arise |
| A client-callable conversion endpoint silently returning par for an unauthorised company | **REDUCED, not rejected.** The endpoint routes through the active-companies mechanism, which **raises** for a company the user cannot access. The par outcome remains reachable **within** the user's own allowed companies, so it survives as an instance of `BW-28`, not as a boundary-crossing case |
| A null-company tax-repartition row | **REJECTED — `VERIFIED SAFE`.** The owning tax's company is required at both the ORM and the database layer, so the repartition model's null disjunct is unreachable code |
| `BW-16` (branch-scoped rate invisible to its resolver) | **WITHDRAWN.** `MCC_C` §6. Its residual content is absorbed by `BW-01` and `BW-29` |

---

## 6. Verdict

> ## `PARTIALLY VERIFIED` — the taxonomy is more complete and is still not proven complete
>
> **19 classes · floor 35 cases · 10 tolerance-zero boundaries · 0 resolved.**
>
> **Every material Wave A failure dimension the round instruction lists is now represented except
> one** — *wrong reversal lineage* — which has **never been searched**. The one other class that was
> empty for the same reason was searched this round and **produced a verified defect immediately**.
>
> **A taxonomy is not proven complete by having no empty cells.** It is proven complete when every
> cell has been *searched*. On that test the taxonomy is at **18 of 19**, and the one gap is known,
> named, bounded and cheap.

---

## 7. ADDENDUM — the last empty class was searched, and it is not empty either

> **Added after §6 was written, because `ER-CORE-4` obliged it.** The section above reported *"18 of
> 19 classes searched; the one gap is known, named, bounded and cheap."* **Cheap enough to do.** It
> was done, and the result changes the section's own verdict.

### `BW-35` — wrong reversal lineage

**Search boundary, declared.** Every occurrence of the reversal-lineage field and its inverse across
the accounting addon in `.py` and `.xml`, excluding tests and translations — **11 sites, complete** —
plus the reversal wizard read in full and the entry model's reversal region read in full.

**Findings, all `VERIFIED FACT` at source:**

1. **There is no constraint of any kind on the lineage field.** No application-level constraint hook,
   no storage-level constraint, no validation anywhere among the 11 sites. Nothing checks that the
   entry a reversal points at is the entry it actually reverses — not the amounts, not the signs, not
   the accounts, not the period.
2. **The link is not unique.** Nothing prevents **N** reversals pointing at one original. An entry can
   be reversed repeatedly, and **every one of those reversals balances**.
3. **`readonly` on the field is a client-side attribute**, and the addon itself writes the field
   directly on a server-side path. It is not a control.
4. **No delete behaviour is declared** on the link, so it takes the framework default and the lineage
   is **severable** — the pointer can be silently cleared without either entry changing.
5. **The reversal is auto-reconciled with its original only when the caller asks to cancel.** In the
   ordinary reversal case, the lineage **pointer is the only carrier of the correction relationship**,
   and nothing validates it.
6. The wizard's only pre-check on the target is that the journal **type** matches.

| Question | Answer |
|---|---|
| Debit = credit? | **Yes** — both entries, always. The reversal is a copy with negated balances |
| Ledger internally consistent? | **Yes.** The trial balance foots with one, two or ten reversals of the same entry |
| Detecting control? | **None found in the searched scope** |
| Evidence the control exists? | **None.** 11 sites, no guard among them |

**Class: `A — verified absence of a lineage control, within the declared pattern and path set.`**

### What this does to §6's verdict

> **Both classes that stood at zero instances were empty because nobody had looked. Both produced a
> verified defect on the first search.**
>
> The taxonomy is now **19 of 19 searched**, floor **36 cases**, and `MCU-15` closes.
> **`ER-CORE-4` is no longer an inference from one case; it is a rule with a 2-of-2 record.**
>
> §6's verdict is otherwise unchanged and remains **`PARTIALLY VERIFIED`** — a taxonomy with no
> unsearched cells is still not a taxonomy proven complete, because completeness of the *class list*
> was never tested, only completeness of its *cells*. **That distinction is the next thing this
> method has to learn, and it is stated here so the next round does not have to discover it.**

---

## 8. SECOND CORRECTION NOTICE — from the expert/audit challenge, verified at source before acceptance

> Governing record: `MCC_J`. Every correction below was **re-read at primary source by this session**
> before it was accepted. Original text stands.

| # | Claim in this file | Correction |
|---|---|---|
| `G-C1` | **`BW-28`** — *"an amount is posted at a rate the report converting it cannot see"*, and its supporting 6-include / 6-exclude symmetry | **CONTRADICTED IN ITS CENTRAL MECHANISM.** The reporting currency table joins on **`other_company.currency_id`** — the *company's* functional currency — never on the journal item's transaction currency; and companies sharing the consolidating company's currency are emitted at **rate 1 by construction**. The posting resolver translates **transaction → functional**; the currency table translates **subsidiary functional → group presentation**. Under IAS 21 these are different measurement objects that **must** use different rate sources. `BW-28` reads correct consolidation semantics as an error, and `MCC_B` §5's symmetry counts scoping rules across two objects as one population. **`BW-28` is WITHDRAWN as registered** |
| `G-C2` | `BW-28`'s *"Detecting control? **None.** … Evidence the control exists? **None found.**"* | **CONTRADICTED — a class-`A` absence asserted where a class-`B` search would have found the control.** The multicurrency revaluation report computes, per line and per account, the retranslation difference between the booked company-currency balance and the foreign-currency balance at a report rate, **and that rate is user-overridable per currency**, with a warning raised when it is. An accountant supplying the correct closing rate sees a par-valued or 2010-valued balance as an enormous adjustment. **The file was item 10 of this round's own 20-file surface and this round never asked what it does.** Bounded limit: the control covers only **open balance-sheet monetary items in a foreign currency, on non-excluded accounts**, and does **not** compare the ledger against the consolidation currency table — so for `G-C3` the "no detecting control" statement **stands** |
| `G-C3` | **NEW, replacing `BW-28`** — `BW-28a` | **`VERIFIED DEFECT`, and more severe than what it replaces.** When the consolidating root holds **no rate row for a subsidiary's functional currency**, that subsidiary's **entire** balance sheet and income statement are translated into the group presentation currency at **1.0**, silently, with no warning line and no reconciling item. A third par substitution exists inside the day-weighted average builder, where it contaminates a *blended* rate rather than replacing one. **This is a whole-entity consolidation failure, not a per-posting rate failure**, and it becomes `T0-07`'s headline instance |
| `G-C4` | `BW-33` graded *"minor severity"* | **UNDERSTATED.** The same five lines that flip the account's reconcile attribute then reconcile **with exchange-difference and cash-basis generation both switched off**. On posted moves this means realised FX gain or loss is **not recognised** and cash-basis tax entries are **not generated**, automatically, with only an informational log. Re-graded **MEDIUM** and cross-listed under *missing accounting event* |
| `G-C5` | `BW-34` — *"the **only** production consumers in the accounting addon are four writes to posted moves in the bank-statement path"* | **SCOPE STATEMENT CONTRADICTED.** True of the accounting addon; false of the accounting application. **Seven** production consumers exist across two addons, and one of them — in the accountant addon's *reset to draft* path — writes a **new accounting date onto a posted deferral reversal**. That is a **period reassignment**, a different failure dimension from the one `BW-34` is filed under. Class `B` presented as `A`, by this round, in the round that convicts its parent of exactly that |
| `G-C6` | §4 `T0-09` — *"two bounded instances", one being the empty constraint definition* | **INSTANCE 2 FALLS.** An empty definition string is a **deliberate ORM delegation idiom**, not an inert control: the framework drops any existing constraint of that name and then registers a **post-init assertion that the matching custom index exists**, which raises if it does not. The real defect at that site is the index's **scope**, not its declaration form. **`T0-09` is left with one instance and is therefore NOT bounded** — see `G-C7` |
| `G-C7` | §4 `T0-09` — *"16 company-consistency guards … that can never execute"* / *"absent to the machine"* | **DEFECT CONFIRMED IN SUBSTANCE, OVERSTATED IN WORDING, UNDERSTATED IN POPULATION.** The 16 declarations **do** generate a client-side field domain, so the control is **present in the view layer and absent at write** — a different finding with a different remedy. And the population is larger: a declared cross-tabulation over the accounting addon finds **a floor of 30 such declarations across 4 files**, of which this round named one |
| `G-C8` | §1's four-question establishment test | **NOT APPLIED TO 4 OF 7 NEW CASES.** Only three of the seven carry the four-question table, yet §3 asserts all are established and moves the floor to 35. **Under this file's own rule the established floor is 31, not 35.** The four unestablished cases are not withdrawn — they are **re-classified as `NOT YET ESTABLISHED`** pending the test |

### Restated position

| Measure | Was | Now |
|---|---|---|
| New cases this round | 7 (`BW-28`…`BW-34`) + `BW-35` | **7** — `BW-28` withdrawn, `BW-28a` added, `BW-35` retained |
| Established under §1's own test | asserted 8 | **4** (`BW-28a`, `BW-31`, `BW-32`, `BW-35`) |
| Register floor, established | claimed **35/36** | **32** (29 − 1 withdrawn − 1 withdrawn + 4 established + `BW-35`) |
| Tolerance-zero boundaries | 10 | **10**, with `T0-09` reduced to one instance and **not bounded**, and `T0-07` restated with `BW-28a` as its headline |

> **Two new tolerance-zero boundaries were returned by the challenge and are recorded in `MCC_J`:
> the entry-balance invariant is enforced in ONE currency dimension only, and the balance assertion
> itself is suppressible by context on three shipped production paths.**
> **`unbalanced-and-posted` is reachable. That is a worse state than balanced-but-wrong, and this
> taxonomy has no cell for it.**
