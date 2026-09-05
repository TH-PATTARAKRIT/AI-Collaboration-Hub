# P06_RESEARCH_ERROR_AND_REVISION_LOG.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Relationship to `14_P06_REVISION_LOG.md`:** that file logs the first round (REV-E-01 … REV-E-04). This one continues the same numbering. **Neither file is superseded.**

---

## 1. Author errors in this continuation

**REV-E-05 — The prior round's open-item count added two different units together.**
The published figure was *"42 open items — C:18 · D:16 · HOLD:8"*. The three parts sum to 42, but the **HOLD bucket counted `P06-B-*` blockers** while C and D counted **`P06-OQ-*` open items**. Executed count of distinct `P06-OQ-*` identifiers: **36**.
**Detected by:** running the count at the start of this continuation rather than carrying the reported figure forward — which is what the continuation prompt explicitly required.
**Resolution:** verified baseline of 42 blockers / 36 open items adopted; recorded in `21_` §3.

**REV-E-06 — The targeted blocker register's own arithmetic was wrong, in the same defect class, one file later.**
First draft: *"Blockers | 42 | **51** (42 − 4 closed + 13 new)"*. Three defects in one line:
1. it **subtracted closed blockers from the population**, when closure partitions a population rather than shrinking it;
2. it counted **13 new items** when only **12** are `P06-B-*` — the thirteenth, `P06-XC-01`, is a different unit;
3. the result (51) disagreed with the executed count (**54**) and was **published without running the command**.
**Detected by:** executing `grep -oh 'P06-B-[0-9]\+' *.md | sort -u | wc -l` after publication.
**Resolution:** corrected in place in `40_` §3, with a unit declaration added above the table and the error recorded rather than amended away.
**Significance:** this is the `count unit vs population` defect **and** the `declared-pattern-not-run` defect, committed together, by the author of a file whose own §1 declares unit discipline. **Writing a rule does not make one immune to it** — the prior round recorded the same lesson at REV-E-02 and it recurred anyway.

**REV-E-07 — A gap was declared "the first action for a successor round" when it was executable in-session.**
`38_` §2 first stated that the localisation-pack search (`OQ-90`) was *"the single largest self-inflicted gap"* and deferred it.
**Resolution:** it was then run. Result: 0 files across both patterns; both Class-A negatives survive; and the search **produced a new finding** (`P06-B-55`) about the evidence base being a filtered distribution.
**Significance:** deferring a two-minute grep to a future session, and *documenting* the deferral, is a way of converting work into paperwork. Recorded because the first draft is what would have shipped.

**REV-E-08 — Two published counts went stale between execution and package close.**
`40_` §3 and `13_` §2 recorded 54 blockers / 39 open items. Both figures were **correct when executed**. They then went stale because `41_`, `42_`, `43_` and `38_` §2a subsequently raised `B-55` and `OQ-93` … `OQ-97`.
**Detected by:** re-running the count as the last action before commit.
**Resolution:** final executed figures — **55 blockers, 44 open items** — propagated to `40_`, `18_` and `13_`, with the drift itself recorded rather than overwritten.
**Significance:** this is not the unit-conflation defect of REV-E-05/06. It is a subtler one: **a count is only true at the instant it is run**, and a package that keeps writing after its counts are taken will invalidate them. The fix is procedural — take the counts last — and it is now recorded as the closing step of the manifest.

---

## 2. Findings revised this continuation

Per the CORR1 §6 shape. **The superseded wording is retained verbatim so the change stays legible.**

### R-09 — Attack A4a, cross-company reconciliation
- **Superseded wording:** *"HOLD — SCOPE EVIDENCE REQUIRED. Whether this crosses a COMPANY boundary depends on whether companies sharing a `root_id` are branches of one legal entity or distinct legal entities."*
- **Why it was wrong:** the question was mis-specified. It asked what a deployment *contains* when the decisive fact is what the model *constrains*.
- **Correct analysis:** the root-delegated set is five fields (`currency_id`, `fiscalyear_last_day`, `fiscalyear_last_month`, `account_storno`, `tax_exigibility`) and **excludes `vat` and `company_registry`**. So `root_id` is a fiscal/currency hierarchy that leaves legal identity free.
- **Updated classification:** **CONFIRMED DEFECT.** The guard names the company boundary and tests a different one; it is structurally incapable of enforcing what it claims, for every deployment.
- **Architecture impact:** `RM-R-10` reinstated unconditionally; `SCOPE-R-02` reclassified to a design decision.
- **Cross-process impact:** P02 `SF-06` reached the same conclusion independently and stated the legal-entity consequence outright. P11 may strike `P06-B-27` from decision `D-3`.

### R-10 — P06's self-characterisation
- **Superseded wording:** *"P06 owns nothing else."* (`09_` §6)
- **Why it was wrong:** P06 emits three accounting events by the act of matching — exchange difference, its reversal on unmatch, and cash-basis tax recognition. A process that emits accounting events is not a terminal consumer.
- **Correct analysis:** P06 is a **producer** that owns none of the three events it emits. Adopted from `P11_SETTLEMENT_RECONCILIATION_ARCHITECTURE.md` §1.
- **Updated classification:** SUPERSEDED. The underlying findings are unaffected; the framing is corrected.
- **Cross-process impact:** each emitted event must name its owning process and its own recognition date (P11 `SRP-05`).

### R-11 — Payment token contradiction (`C-11` / `A4c`)
- **Superseded wording:** severity **HIGH**.
- **Why it was over-stated:** the transaction's token domain is provider-restricted and the provider carries the company, so cross-company *charging* is blocked. The real exposure is cross-company **visibility and selection**.
- **Updated classification:** **CONFIRMED DEFECT, severity MEDIUM.** A downgrade produced by adversarially testing the package's own finding.
- **Architecture impact:** visibility and usability need separate scopes for credential-bearing objects.

### R-12 — Currency-rate scope
- **Superseded wording:** *"Currency rate is TENANT-scoped."* (`19_` SCOPE-F-01)
- **Why it was incomplete:** it answered with one scope where two objects exist.
- **Correct analysis:** the rate **observation** and the rate **selection** are different objects at different scopes — adopted from P11 `SC-05` and P02 `P02-SC-01`. P06 adds that the tenant is the correct custodian of the observation table where the platform does not supply it.
- **Updated classification:** **P06 position changed on peer evidence.** P11's `T0-07` remains UNRESOLVED and P06 does not close it.

### R-13 — `P06-B-22`, write-off approval control
- **Superseded wording:** at the prior round's challenge, downgraded Class A → **Class B**, because the custom approval estate had not been searched.
- **Correct analysis:** it has now been searched — 3 modules, 46 files, PATTERN `account\.payment|account\.move|writeoff|write_off|reconcile` → **0 hits**. The only hook is a `write`-time state-field gate that exempts administrators and covers neither `create` nor `unlink`.
- **Updated classification:** **restored to Class A within the enlarged declared scope.**
- **And it produced two new findings:** the approval framework's own execution path sets the context flag that disables its gate (`P06-B-51`), and the custom write-off producer grants full CRUD to any Invoicing user (`P06-B-52`).

### R-14 — Attack A7's premise
- **Superseded wording:** statement-line deletion analysed exclusively through the ORM `unlink()` path and its `force_delete` bypass.
- **Why it was insufficient:** `om_data_remove` deletes the rows by unconditional SQL with an auto-commit, bypassing the ORM entirely. Every control A7 analysed — audit-trail retention, `_check_reconciliation`, lock dates, the hash chain — is **inapplicable on that path**.
- **Updated classification:** A7 **stands for the ORM path**; `P06-B-50` covers the SQL path. **Not superseded, but no longer sufficient on its own.**

### R-15 — The ingestion-door denominator, again
- **Superseded position:** seven doors, corrected once already at REV-E-01.
- **Why it is still incomplete:** P05 `SR-04` found a path where cash moves through a bank journal producing **no `account.payment` at all**, invisible to the matching model.
- **Correct analysis:** that is a *settlement* door on a different axis from the seven *ingestion* doors, not an eighth ingestion door. Recorded as `P06-B-53` and routed to P11 for the unified register.
- **Significance:** **the second time an outside pass corrected a P06 denominator.** The first was REV-E-01.

---

## 3. Corrections P06 made to peers

Per peer-intake discipline: verify before adopting, and correct their record where their package will carry the error.

| Peer | Correction offered |
|---|---|
| **P11** | `P06-B-27` is on P11's `D-3` minutes-to-close list as a UAT query. **It is closed on source evidence and needs no query.** P11 may strike it. |
| **P11** | `P06-XC-01` (the P02 verdict conflict) is registered nowhere. `P11_CONTRADICTION_REGISTER.md` runs `P11-C-01`…`P11-C-07` with no row for it, because P11 ingested P02 and P06 in separate deltas and did not cross-read them. Raised as candidate `P11-C-08`. |
| **P10** | `X-08` is answered and may be closed. |
| **P09** | Its class-B claim about P06's widget is **correct in shape and should stay class B** — P06 confirms the overwrite mechanism and did not trace the analytic specifics. |
| **P11** | P10 routes its close and FX dependencies to P04, while P11 and P02 route the same questions to P08. Since no P08 exists, P10's dependencies are addressed to a process that cannot answer. Flagged, not adjudicated (`OQ-93`). |

---

## 4. What did not change

Stated because a revision log that lists only changes implies everything else moved.

- **All six headline findings stand.** Two were independently re-verified this continuation (identity, fees) and both survived; four were corroborated by peers.
- **No contradiction was withdrawn.** `C-13` had its defect severity restored, not reduced.
- **The two AAS+ vetoes stand** pending the recheck in `42_`.
- **All statutory HOLDs are unchanged**, and P05, P06 and P07 hold the WHT question identically — which is the correct outcome.

---

## 5. Error pattern across both rounds

**Eight** author errors are now recorded (REV-E-01 … REV-E-08). Their distribution is the useful part:

| Detected by | Count |
|---|---|
| Independent pass (subagent, peer package) | **3** — REV-E-01, REV-E-04, and R-15 (the door denominator, corrected by P05) |
| Executing a command the author had only declared | **3** — REV-E-02, REV-E-06, REV-E-08 |
| Author, unaided | **2** — REV-E-05, REV-E-07 |

**Six of eight were caught by something other than the author reading their own work** — and the three counting defects (REV-E-05, REV-E-06, REV-E-08) were **all** caught by running a command rather than by re-reading a table. That is consistent with the programme's standing finding that independent review is the discovery engine — and it is the reason `42_` and `43_` exist as separate steps rather than as sections of this file.
