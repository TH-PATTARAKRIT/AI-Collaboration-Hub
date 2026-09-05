# P06_P08_INTAKE_AND_DEPENDENCY_REFRESH.md

**Session:** P06 — SUPPLEMENTAL CRITICAL-RISK CLOSURE (CP-P06S17)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Trigger:** the directive required peer availability to be re-checked rather than carried forward. **It had changed.**

---

## 1. Peer refresh — executed, not assumed

`git ls-remote --heads origin "refs/heads/research/*"` at this round returns **20 refs**. Process branches:

| Process | Round 3 | **Now** |
|---|---|---|
| **P08 Record-to-Report** | **NOT PUBLISHED** | **`research/account-p08-record-to-report-2026-09-04-001` — PUBLISHED, 39 files** |
| P01 Procure-to-Pay | NOT PUBLISHED | **still NOT PUBLISHED** |
| P02, P03, P04, P05, P07, P09, P10, P11 | published | published |

**8 of 9 peers now read. Only P01 remains.**

---

## 2. THE HEADLINE — P08 independently found `om_data_remove`

**PIN-F-01 — A peer process, working separately, found the same module and cited the same lines.**

`ACCOUNT_P08_RECORD_TO_REPORT/LAYER2_EVIDENCE_QUARANTINE/E02_COA_AND_IDENTITY.md:125`:
> `EV-CUST-04 | om_data_remove/models/model.py:24-27 "delete from %s" + self._cr.commit(); :165-176 remove_account; :199-250 remove_account_chart; :334-348 remove_all; menu group om_data_remove/views/view.xml:119; no ACL file`

And as an attack — `16_P08_ORPHAN_DUPLICATE_POSTING_ATTACK.md:107`, `AT-21` *"Erase the ledger from a settings screen"*:
> *"**No company predicate appears in any statement** — the delete is whole-table, therefore whole-database, across every company. Because it never passes through the object layer it is constrained by no posted-state guard, no retention option, no seal, no lock date and no isolation rule. A failure part-way through is **committed**, not rolled back."*

**This is the strongest possible corroboration of `P06-B-50`: two processes, different evidence paths, same lines, same conclusion.** P06 arrived via the custom-module delta; P08 via a ledger-integrity attack. Neither read the other.

**PIN-F-02 — And P06 answers the exact question P08 left open.**
P08's status line on `AT-21`:
> *"`FACT VERIFIED` for the code. The menu entry is restricted to the system-administrator group; **whether the underlying methods are reachable by a lower-privileged direct call is `D UNKNOWN`.**"*

**P06 has now traced that chain end to end** (`45_`): the route is `auth="user"`; `get_public_method` blocks only private and `@api.private` methods; `call_kw` performs **no** access check; the method body performs no ORM operation on its own model. The `res.config.settings` ACL is `base.group_system` — and is **never invoked on this path**.

**P08's `D UNKNOWN` is answered: `NO SERVER-SIDE AUTHORIZATION VERIFIED`.** This is the single most valuable thing P06 returns to a peer this round, and it should be delivered to P08 directly, not only through P11.

**PIN-F-03 — P08 raises it as a tolerance-zero boundary P06 must adopt.**
`27_P08_TOLERANCE_ZERO_REGISTER.md`:
> `P08-T0-08` — **No path may write to the ledger outside the object layer.** … *"a settings action erases ledger tables by direct statement, whole-table, every company."* **OPEN.**

P06 adopts `P08-T0-08` as the correct formulation of its own `AUTH-R-02`, and records that P08 stated it first.

---

## 3. Three further findings P06 gains from P08

**PIN-F-04 — A second destructive path, and it is P06's `B-37`.**
`AT-22` *"Backdate by discarding identity"*: a custom utility *"returns posted entries to unposted, **sets the number to empty**, overwrites the date and the document date with an operator-chosen value, and re-posts — allocating a new number and leaving the original as an unexplained gap."*
**That is `cr_effective_date_entries`, P06's `B-37`.** Independent corroboration, and P08 adds the consequence P06 did not state: *"**Entry identity and number continuity do not [survive]**."*

**PIN-F-05 — The reference product itself contains a `DELETE FROM` on a ledger table.**
`E02_COA_AND_IDENTITY.md:25` — `EV-COA-18`: `account/wizard/account_merge_wizard.py:194-201 DELETE FROM account_account`.
**New to P06.** P06's destructive analysis was scoped to the custom estate; the merge wizard is core. Recorded as **`P06-B-56`** and routed for follow-up — it is P08's finding, cited here, not re-derived.

**PIN-F-06 — Forced deletion of a posted entry leaves no evidence on a default installation.**
`05_P08_JOURNAL_POSTING_MODEL.md` `JPM-28`: the deletion-log routine *"filters to entries whose company has the retention option **enabled**. On a default installation that option is off, so a forced deletion of a posted entry leaves **no log line and no database record — no evidence at all**."*
**This materially worsens `P06-B-12`** (deletability is a company toggle): the toggle governs not only whether deletion is allowed but **whether it is recorded**.

---

## 4. The four items P06 held pending P08 — resolved

| Item | Disposition |
|---|---|
| **`F-06`** posting-state authorship | **RESOLVED — P08 CLAIMS IT.** `15_` §2 owned rows include *"the posting engine and its controls"*. P08 adds `JPM-02`: *"**Posting has two doors and only one of them validates** … An entry with **no lines at all** can reach the posted state through the second door."* **P06 removes this from CONTESTED.** |
| **`F-17`** lock/close status ownership | **RESOLVED — P08 CLAIMS IT** (*"period, lock, close, reopen"*), scopes it (`SC-CL-03` finality = COMPANY; `SC-CL-04` derogation grant = **TENANT or above**, COMPANY may never self-grant), and answers the substantive question: `PC-17` — *"**no field anywhere answers 'is month M closed?'** — only 'is date D at or before cut-off L, for this user'."* |
| **`F-15`** cash/bank GL balance ownership | **STILL OPEN — P08 EXPLICITLY DISCLAIMS IT TO P06.** `15_` §2 "Not owned by P08: … *bank statement flow and payment instruments — P06*". No peer now claims it. **It returns to P06 as genuinely unowned**, with new P08 evidence attached (`REC-21`, `REC-22`, `REC-23`, `FR-15`, `FR-16`). |
| **`B-46`** correction spanning a close lands in two periods | **STILL OPEN — but P08 supplies both the mechanism and the remedy.** `REC-08`: *"**Two entries born of one matching event are dated by two different rules.**"* `PC-32`: *"Entries carry no adjustment marker."* Remedy `KRN-INV-01`: *"A **reversal** is a `K2` in its own right, **linked to the `K2` it reverses**."* **P06 adopts P08's requirement as the closure path.** |

---

## 5. Where P08 and P06 independently agree

| Finding | P06 | P08 |
|---|---|---|
| Un-matching is not lock-gated | attack A6, five-file zero-hit denominator | `REC-11` — *"`A VERIFIED ABSENCE`, scope = the two settlement models in full … every lock-check symbol"* |
| Undoing a bank reconciliation destroys rather than reverses | attack A5 | `REC-22` — *"destroys rather than reverses, and deletes the associated settlement records"* |
| Statement completeness compares a figure to itself | `B-11` | `REC-23` — *"compares the system's own figure to itself by default"* |
| Bank "reconciled" is a structural test, not a match test | `BER-F-03`, `is_reconciled` terminal branch | `REC-21` — *"An entry recoded directly to a final account shows as reconciled **with no match behind it**"* |
| The bulk matching tool ignores a partner filter without an account filter | `RM-F-34` | `REC-20` — same, *"pairing solely on equal absolute amounts"* |
| Automatic matching rewrites posted entries | `RM-F-01` (delete-and-rebuild) | `REC-18` — *"**runs unattended and rewrites posted entries**"*; `AE-14` |

**PIN-F-07 — Six independent convergences, zero contradictions with P08.** P06's reconciliation findings are the most heavily corroborated in the package.

---

## 6. New inbound dependency — P08 asks P06 for something P06 has not supplied

**PIN-F-08 — `XP-05` / `HO-03`: *"the settlement event's own date — P08 requires one and the benchmark has none."***
Recorded three times in P08 (`15_` §4, `18_` §2, `25_` §4) as `PEER DEPENDENCY OPEN` with **P06 named owner**.

P08's supporting finding, `REC-05`: *"**A match carries no event date.** Its as-of date is the later of the two matched documents' dates. Matching two prior-period items today retroactively closes them in a re-run of that prior period's ageing, with nothing in the data to explain the difference."*

**P06 ACCEPTS this dependency and confirms the gap from its own evidence.** The reconciliation act has no date of its own — a fact P06 documented from the other direction (`RM-F-01`: the widget clears and rebuilds the entry, recording no event). **Raised as `P06-B-57` and added to the target requirements:**
> **A settlement event carries its own date, distinct from the dates of the documents it settles, and that date determines its period.**

**PIN-F-09 — And P08 recorded the interface without waiting**, per its own rule: *"P08 therefore **records the interface and does not wait**."* That is the correct peer-intake discipline and P06 adopts the same posture for its outbound items.

---

## 7. Dependency status after refresh

| ID | Depends on | Status |
|---|---|---|
| `D-01` | **P01** | **PEER DEPENDENCY OPEN** — still unpublished |
| `D-02` | **P08** | **CLOSED for `F-06` and `F-17`; OPEN for `F-15` and `B-46`** |
| `D-03` | P02 | **RECONCILED** — `52_`, routed to P11 as `P11-C-08` |
| `D-05` | P11 | open — 31 event→GL rows still unreconciled at P11 |
| `D-10` | → P07 | three BLOCKING dependencies, see `54_` |
| **`D-16`** | **← P08** | **NEW — the settlement event's own date. `P06-B-57`.** |

---

## 8. Open items

| ID | Item | Class |
|---|---|---|
| `P06-B-56` | `DELETE FROM account_account` in the reference merge wizard — P08's finding, not re-derived by P06 | C |
| `P06-B-57` | The settlement event has no date of its own — P08 inbound `XP-05` | **accepted, open** |
| `P06-OQ-109` | P08's `P08-T0-04` (a difference entry selects its owning company by recordset position) touches P06's write-off path and was not independently verified by P06 | C |
