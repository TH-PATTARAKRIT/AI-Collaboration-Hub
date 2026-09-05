# P06_TARGETED_BLOCKER_REGISTER.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Rule observed:** *"No vague OPEN status in the final targeted closure register."* Every blocker below carries exactly one of the fourteen permitted dispositions.

---

## 1. Leverage grouping, and the order actually executed

| Group | Meaning | Count at start | Executed |
|---|---|---|---|
| **A** — one query / high leverage | one action closes several | 1 | **YES — first** |
| **B** — source-resolvable | closable by reading source | 12 | **YES** |
| **C** — database-resolvable | needs the target DB | 6 | attempted; no target DB exists |
| **D** — runtime-resolvable | needs execution | 3 | not possible read-only |
| **E** — peer-dependent | needs sibling packages | 5 | **YES — 7 of 9 peers read** |
| **F** — statutory | Accounting-Tax track | 4 | routed, unchanged |
| **G** — true design decision | Boss/architecture | 9 | packaged, not decided |
| **H** — invalid / superseded | to be withdrawn | 2 | **YES — see §4** |

**Executed in leverage order, not ID order**, as directed.

---

## 2. Closure ledger — what changed this continuation

### 2.1 CLOSED

| ID | Disposition | Basis |
|---|---|---|
| `P06-B-27` | **CLOSED — SOURCE EVIDENCE VERIFIED** | `root_id` is a fiscal/currency hierarchy; the delegated set is 5 fields and excludes `vat` and `company_registry`. See `22_`. |
| `P06-B-28` | **CLOSED — SOURCE EVIDENCE VERIFIED** | Token scope fully determined across six dimensions; severity **downgraded HIGH → MEDIUM** after adversarial test. See `31_`. |
| `P06-B-40` | **CLOSED — SOURCE EVIDENCE VERIFIED** | The required second, independently-worded search was run on both principal Class-A negatives (identity, fees). Both survive. See `26_`, `29_`. |
| `P06-B-03` | **CLOSED — CROSS-PROCESS EVIDENCE VERIFIED (partial → substantive)** | 7 of 9 peers read. P01 and P08 remain, and are re-raised as `P06-B-54` rather than leaving B-03 ambiguous. See `35_`. |

**4 closed.**

### 2.2 Open items closed (`P06-OQ-*`)

| ID | Disposition |
|---|---|
| `P06-OQ-21` | **CLOSED — SOURCE EVIDENCE VERIFIED** — `BYPASS_LOCK_CHECK` NOT FOUND across 19,982 files in four custom roots |
| `P06-OQ-71` | **CLOSED — SOURCE EVIDENCE VERIFIED** — `om_data_remove` fully traced; produced `P06-B-50` |
| `P06-OQ-81` | **CLOSED — SOURCE EVIDENCE VERIFIED** — custom approval estate searched; restored `P06-B-22` to Class A |
| `P06-OQ-20` | **NARROWED** — PC-F-07's scoping defect no longer depends on the untested block |

**3 closed, 1 narrowed.**

### 2.3 Findings whose classification CHANGED

| Item | Change | Direction |
|---|---|---|
| Attack **A4a** | HOLD → **CONFIRMED DEFECT** | **upgrade** — the guard cannot enforce the boundary it names |
| **RM-R-10** | conditional → **reinstated unconditionally** | upgrade |
| **C-13** | severity HOLD → **HIGH restored** | upgrade |
| `P06-B-22` | Class B → **Class A within an enlarged scope** | upgrade |
| **SCOPE-R-02** | HOLD — SCOPE EVIDENCE REQUIRED → **HOLD — DESIGN DECISION REQUIRED** | reclassified, **not closed** |
| **C-11 / A4c** | HIGH → **MEDIUM** | **downgrade** |
| P06's self-framing as terminal consumer | → **P06 is a producer of three accounting events** | corrected by P11 |

**5 upgrades, 1 downgrade, 1 reclassification, 1 correction. A round that only upgrades is not a review.**

### 2.4 NEW blockers raised by this continuation

| ID | Blocker | Disposition |
|---|---|---|
| `P06-B-43` | The payment-register wizard is root-scoped in the same defective shape as A4a, in a second location | **HOLD — DESIGN DECISION REQUIRED** |
| `P06-B-44` | **GENERATION GAP (severity raised by AAS-03 E2-C-03).** The only deployment evidence available is from **Odoo 19** databases, while the entire P06 research target is the **v18** line. If the programme's target generation has moved, a material fraction of this package is scoped to a superseded line. The missing target registry is the *second* half of this blocker, not the first. | **HOLD — DATABASE EVIDENCE REQUIRED** |
| `P06-B-45` | Lock dates inherit up the hierarchy, strictest ancestor wins, **including archived companies and with elevated privilege** (P04 `P04-B-43`); the hierarchy may span legally distinct companies | **HOLD — DESIGN DECISION REQUIRED** |
| `P06-B-46` | RELOCATE splits a correction across two periods with nothing linking them; P04 shows this lives in the **generic** posting routine | **HOLD — PEER PROCESS REQUIRED (P08)** |
| `P06-B-47` | **Derived ownership** is the common root of A4b and A4c — an owner reached through two hops cannot be independently verified | **HOLD — DESIGN DECISION REQUIRED** |
| `P06-B-48` | `iso20022_uetr` is a globally-unique outbound tracker with **no inbound counterpart**; CAMT parses the inbound end-to-end id into a **note** | **HOLD — DESIGN DECISION REQUIRED** |
| `P06-B-49` | No import-batch object; a re-import cannot be identified, audited or reversed as a unit | **HOLD — DESIGN DECISION REQUIRED** |
| `P06-B-50` | **HIGHEST-SEVERITY FINDING IN THE P06 PACKAGE (elevated by AAS-03 E4-C-01).** `om_data_remove` deletes bank statements, payments, moves, partial reconciles and chatter by unconditional `DELETE FROM` with an auto-commit, then rewinds the bank/cash/invoice sequences to 1. **No server-side authorisation** — no `security/` directory, no ACL file, no `has_group` check; the only gates are a menu `groups=` attribute and a client-side confirm string on `res.config.settings` object handlers. Present in **all four** custom roots. It bypasses the ORM entirely, so every control attack A7 and A8 analysed is inapplicable on this path. | **CLOSED — SOURCE EVIDENCE VERIFIED** as a finding; remediation is a Boss decision |
| `P06-B-51` | The custom approval framework's own execution path sets the context flag that disables its gate. **DOWNGRADED CONFIRMED → PLAUSIBLE by AAS-03 E4-C-03:** the flag (`run_python_code: 1`, `:616`) and its consumer (`check_rule` returning `True`, `:692`) are both quoted, but **no end-to-end execution was traced**. `P06-OQ-96`. | **CLOSED — SOURCE EVIDENCE VERIFIED** as an evidenced concern, classified **PLAUSIBLE** not CONFIRMED |
| `P06-B-52` | The custom write-off producer grants full CRUD to any Invoicing user, no amount ceiling | **CLOSED — SOURCE EVIDENCE VERIFIED** as a finding |
| `P06-B-53` | **An eighth settlement door**: the advance cash-return path moves cash through a bank journal with **no payment object**, invisible to the matching model. **INHERITED FROM P05 `SR-04` — not a P06 discovery. Flagged for deduplication at P11** so it is not counted twice across registers. | **HOLD — PEER PROCESS REQUIRED (P05)** |
| `P06-B-54` | P01 and P08 packages unpublished; vendor-payable ownership and the close architecture cannot be reconciled | **HOLD — PEER PROCESS REQUIRED** |
| `P06-XC-01` | **Cross-package contradiction with P02** on headline (i), registered nowhere; routed to P11 as candidate `P11-C-08` | **HOLD — CROSS-PROCESS RECONCILIATION REQUIRED** |

**13 new items (12 blockers + 1 cross-package contradiction).**

---

## 3. Verified population after this continuation

**UNIT DECLARATION (read this before the numbers).** Two different units are in play and they must not be added together: `P06-B-*` **blockers**, and `P06-OQ-*` **open items**. A third unit, `P06-XC-*` **cross-package contradictions**, has exactly one member. **A closed blocker stays in the population** — closure is a *partition* of the population, not a subtraction from it.

| Measure | Unit | Prior | Now |
|---|---|---|---|
| **Blocker population** | `P06-B-*` | 42 | **55** (42 + 13 new: `B-43`…`B-55`) |
| — CLOSED | `P06-B-*` | 0 | **7** — `B-03`, `B-27`, `B-28`, `B-40`, `B-50`, `B-51`, `B-52` |
| — open (HOLD, all sub-classes) | `P06-B-*` | 42 | **48** |
| **Open-item population** | `P06-OQ-*` | 36 verified (42 reported in error) | **44** (36 + 8 new: `OQ-90`…`OQ-97`) |
| — CLOSED | `P06-OQ-*` | 0 | **4** — `OQ-21`, `OQ-71`, `OQ-81`, `OQ-90` |
| — open | `P06-OQ-*` | 36 | **40** |
| **Cross-package contradictions** | `P06-XC-*` | 0 | **1** — `P06-XC-01` |

**Counts verified by execution at package close, not by declaration:** `grep -oh 'P06-B-[0-9]\+' *.md | sort -u | wc -l` → **55**; the same command for `P06-OQ-` → **44**.

> **COUNT DRIFT, recorded (REV-E-08).** An earlier state of this table read 54 / 39. Both were correct **when executed** and both went stale as later files (`41_`, `42_`, `43_`, `38_` §2a) raised `B-55` and `OQ-93`…`OQ-97`. **A count is only true at the moment it is run.** The figures above were re-executed after the final file was written. Any count in this package that is not marked as executed at close should be treated as a floor, not a total.

**REV-E-06 — the first draft of this table got its own arithmetic wrong, in exactly the way this programme has been warned about.** It read *"42 − 4 closed + 13 new = 51"*. Three defects in one line: (a) it **subtracted closed blockers from the population** when closure is a partition, not a removal; (b) it counted **13 new items** when only **12** are `P06-B-*` — the thirteenth, `P06-XC-01`, is a different unit; (c) the resulting 51 disagreed with the executed count of 54 and was published without running it.
This is the **`count unit vs population`** defect and the **`declared-pattern-not-run`** defect in the same sentence, committed by the author of a file whose §1 declares unit discipline. Corrected here in place, and recorded rather than quietly amended.

**The blocker population went UP by 13, and that is the correct outcome.** The objective was *"maximum evidence-based blocker reduction"*, not a lower number. Seven blockers closed on evidence; thirteen new ones were **discovered** by the same evidence work — including one (`P06-B-50`) that defeats the premise of an entire prior attack, and one (`P06-B-53`) that reopens a denominator. **A targeted closure round that only removes items has not looked hard enough.**

---

## 4. Group H — invalid or superseded findings

Assessed as directed. **Two candidates, and only one qualifies.**

| Candidate | Verdict |
|---|---|
| P06's self-description as a terminal *consumer* process | **SUPERSEDED** by P11's producer characterisation (PH-F-01). Corrected in `35_`; the underlying findings are unaffected. |
| `P06-B-22` (no write-off approval control) | **NOT invalid.** It was downgraded to Class B at the prior round's challenge for a good reason, and the search that reason demanded has now been run. **Restored, not withdrawn.** |
| Attack A7's premise (statement-line deletion via the ORM `unlink` path) | **NOT superseded, but no longer sufficient.** `P06-B-50` shows a path that bypasses `unlink()` entirely, so every control A7 analysed is inapplicable there. A7 stands for the ORM path; `P06-B-50` covers the SQL path. Both recorded. |

---

## 5. Full register — all 51 blockers with final disposition

**Boss / governance (5)**
`B-01` no receiving process specification — **HOLD — DESIGN DECISION REQUIRED** · `B-02` no Jira work item — **HOLD — DESIGN DECISION REQUIRED** · `B-03` **CLOSED — CROSS-PROCESS EVIDENCE VERIFIED** · `B-42` deliverable-list gap — **HOLD — DESIGN DECISION REQUIRED** · `B-54` P01/P08 unpublished — **HOLD — PEER PROCESS REQUIRED**

**Scope (5)**
`B-26` unowned bank accounts — **HOLD — DESIGN DECISION REQUIRED** (a `DENY` case under P11's Delta 02 rule) · `B-27` **CLOSED — SOURCE EVIDENCE VERIFIED** · `B-28` **CLOSED — SOURCE EVIDENCE VERIFIED** · `B-43` **HOLD — DESIGN DECISION REQUIRED** · `B-47` **HOLD — DESIGN DECISION REQUIRED**

**State & settlement (11)**
`B-04` — **HOLD — DESIGN DECISION REQUIRED** (owner now named: P05 operates the door, P06 owns it) · `B-05` — **HOLD — DESIGN DECISION REQUIRED** · `B-06` no bank-confirmation fact — **HOLD — DESIGN DECISION REQUIRED**, semantics now specified in `25_` · `B-07` — **HOLD — DESIGN DECISION REQUIRED** · `B-16` internal transfer unpaired — **HOLD — DESIGN DECISION REQUIRED** · `B-30` accounting outside the webhook — **HOLD — DESIGN DECISION REQUIRED** · `B-31` unverified-input order cancel (v14 copy) — **HOLD — DATABASE EVIDENCE REQUIRED** (deployment unknown) · `B-33` no cash session — **HOLD — DESIGN DECISION REQUIRED** · `B-34` PDC not migrated — **HOLD — DESIGN DECISION REQUIRED** (re-verified: no PDC concept in v18 reference at all) · `B-35` returned payment not migrated — **HOLD — DESIGN DECISION REQUIRED** (re-verified: no `payment.return` model, no chargeback) · `B-53` eighth settlement door — **HOLD — PEER PROCESS REQUIRED**

**Identity & controls (13)**
`B-10` per-door identity — **HOLD — DESIGN DECISION REQUIRED**, re-verified · `B-11` self-satisfying completeness check — **HOLD — DESIGN DECISION REQUIRED** · `B-12` deletability is a setting — **HOLD — DESIGN DECISION REQUIRED** · `B-13` identity mutable without trace — **HOLD — DESIGN DECISION REQUIRED** · `B-14` six silent-drop behaviours — **HOLD — DESIGN DECISION REQUIRED** · `B-15` statement↔entry 1:1 by convention — **HOLD — DESIGN DECISION REQUIRED** · `B-19` voided cheque numbers — **HOLD — DATABASE EVIDENCE REQUIRED** · `B-22` no write-off approval — **HOLD — DESIGN DECISION REQUIRED**, Class A restored · `B-29` identity enforced wider than owned — **HOLD — DESIGN DECISION REQUIRED** · `B-48` UETR no inbound counterpart — **HOLD — DESIGN DECISION REQUIRED** · `B-49` no import batch — **HOLD — DESIGN DECISION REQUIRED** · `B-50` **CLOSED — SOURCE EVIDENCE VERIFIED** · `B-52` **CLOSED — SOURCE EVIDENCE VERIFIED**

**Accounting determination (6)**
`B-17` no owner for fees/interest/commission — **HOLD — DESIGN DECISION REQUIRED**, re-verified · `B-18` no ageing on suspense/transit — **HOLD — DESIGN DECISION REQUIRED** · `B-20` no intercompany carrier — **HOLD — DESIGN DECISION REQUIRED** · `B-23` two chains fail silently to `False` — **HOLD — DESIGN DECISION REQUIRED** · `B-24` chart-of-accounts mutated as a side effect — **HOLD — DESIGN DECISION REQUIRED** · `B-25` net-vs-gross settlement — **HOLD — DESIGN DECISION REQUIRED**

**Period close (2)**
`B-45` lock inheritance — **HOLD — DESIGN DECISION REQUIRED** · `B-46` RELOCATE splits corrections — **HOLD — PEER PROCESS REQUIRED (P08)**

**Custom estate (5)**
`B-36` duplicated divergent override — **HOLD — DESIGN DECISION REQUIRED** · `B-37` effective-date module resequences posted entries — **HOLD — DESIGN DECISION REQUIRED** · `B-38` auto-posting without idempotency — **HOLD — DESIGN DECISION REQUIRED** · `B-39` version-stamped without migration — **HOLD — DESIGN DECISION REQUIRED** · `B-51` **CLOSED — SOURCE EVIDENCE VERIFIED**

**Package quality (2)**
`B-40` **CLOSED — SOURCE EVIDENCE VERIFIED** · `B-41` scope revalidation scanned tokens not the deeper pattern — **HOLD — DESIGN DECISION REQUIRED**. **AMENDED:** now also carries the **missing severity model**, recommended by AAS+ at the prior round (`AASP-F-04`, rank by *precondition reachability*) and still not built after two rounds. Twelve blockers were added this continuation without ranking.

**Deployment (1)**
`B-44` no target module registry — **HOLD — DATABASE EVIDENCE REQUIRED**

**Statutory (4)**
`B-08` FX rate source — **HOLD — STATUTORY EVIDENCE REQUIRED** (P11 `DEP-14`: packaged, not decided) · `B-09` journal/GL cardinality — **HOLD — STATUTORY EVIDENCE REQUIRED** · `B-21` vendor advance account — **HOLD — STATUTORY EVIDENCE REQUIRED** · `B-32` tolerance-control inversion — **HOLD — DESIGN DECISION REQUIRED**

**Cross-package (1)**
`P06-XC-01` — **HOLD — CROSS-PROCESS RECONCILIATION REQUIRED**

---

## 6. Exact evidence required to close the remaining HOLDs

| Evidence artefact | Closes |
|---|---|
| `ir.module.module` export from the **SMEsPlus target database** | `B-44`, `B-31`, `B-19`, and upgrades `F02` |
| One query: `SELECT id, parent_id, vat, company_registry FROM res_company` | confirms `B-45` exposure (the *control defect* is already closed) |
| `SELECT model_id, domain, state_field FROM multi_approval_type` | `P06-OQ-91` |
| P01 and P08 packages published | `B-54`, `B-46`, `B-04` |
| Boss decision on the seven-plus confirmed defects | the 26 `HOLD — DESIGN DECISION REQUIRED` items |
| Thai Revenue Code / TFRS sources | the 3 statutory HOLDs |
| A known-good Odoo 18 enterprise distribution to diff | `P06-OQ-63` |

**Twenty-six of the forty-four open blockers are `HOLD — DESIGN DECISION REQUIRED`. That is not an evidence deficit — it is the work of design, and it is correctly outside a research session's authority.**

---

# End
