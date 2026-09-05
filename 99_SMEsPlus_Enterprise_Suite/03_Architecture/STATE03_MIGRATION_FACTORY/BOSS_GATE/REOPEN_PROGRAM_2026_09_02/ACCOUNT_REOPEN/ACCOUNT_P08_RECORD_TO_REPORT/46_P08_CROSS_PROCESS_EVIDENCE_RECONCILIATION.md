# P08_CROSS_PROCESS_EVIDENCE_RECONCILIATION

Session `SMEPLUS-26-09-04-ACC-P08-R2R-TARGETED-FORENSIC-CLOSURE-001` · `CP-T12`

Supersedes `18_P08_DEPENDENCY_REGISTER.md` §2, which recorded *"At P08's close, no peer process had committed output."* **That statement is now false, and it was the single largest gap in P08's evidence base.**

## 1. The evidence base changed, and P08 measured it rather than assumed it

**ENUMERATION.** POPULATION: refs under `refs/remotes/origin/research/account-p*` in the session clone. PATTERN: `git branch -r`, then `git log -1 --format=%cI` per ref. PATH SET: the whole clone. UNIT: **one process branch**. POSITIVE CONTROL: the pattern returns P08's own branch, whose tip is known independently.

**Result: 9 process branches present. Eight peers have committed packages. P01 is absent.**

| Peer | Branch tip (committer date) | Package read by P08 |
|---|---|---|
| P02 Order-to-Cash | 2026-09-04T23:45 | yes |
| P03 Manufacture-to-Cost | 2026-09-05T08:02 | yes |
| P04 Acquire-to-Retire | 2026-09-05T08:12 | yes |
| P05 Expense-to-Pay | 2026-09-05T07:43 | yes |
| P06 Bank-to-Reconcile | 2026-09-05T07:38 | yes |
| P07 TH Tax-to-Compliance | 2026-09-05T08:08 | yes |
| P09 Plan-to-Analyze | 2026-09-05T07:49 | yes |
| P10 Time-Based Recognition | 2026-09-05T07:57 | yes |
| **P01 Procure-to-Pay** | **no branch under this naming** | **`C NOT YET SEARCHED` — other naming not swept** |

### 1A. A mutual-visibility contradiction, recorded not harmonised

**Six peer packages state that P08 is unpublished** and gate work on that basis — P06 (`B-54`, `D-02`, `D-15`, `F-06`, `F-15`, `F-17`, and its evidence manifest recording *19 refs, 9 process branches, P01 and P08 absent*), P05 (`12` §41, `30` §108), and P03 (`41` §21, *"not read"*).

**P08's branch is present on origin with a tip committed 2026-09-04T23:41 — roughly eight hours before those packages' own tips.**

`P08-CONTRA-21`. **Not resolved, and P08 does not claim the peers were careless.** Commit date is not push date; the clone cannot recover when the ref first appeared on origin. Two readings survive the evidence:

1. P08 was pushed after those peers measured — their measurement was correct at the time.
2. The ref existed and the peers' enumeration missed it.

**What matters is the same under both readings:** those gated items are answerable now, and P08 answers them in §3. **Two peers did read P08** — P10 at head `4bdf8a2` and P09 — which is itself evidence that the ref was reachable to at least some sessions.

### 1B. The method incident inside this intake

The first pass of this intake returned **zero P08 references in all eight peer packages.** The pattern was `git grep -E '\bP08\b'`; the engine in use does not honour `\b` under `-E`, so **the pattern could not match anything**. A plain-substring control returned hundreds of hits and exposed it. Re-run under `-P`, the same eight packages return **197 references**.

`P08-M-10` — **the third instance in this session of a pattern that cannot fire.** A zero result was again indistinguishable from absence, and again only a positive control separated them. This one would have caused P08 to publish *"no peer routes anything to P08"* — the exact inverse of the truth.

---

## 2. Inbound — peer findings that bear on P08, with disposition

Each row states whether **P08 verified it independently** or is carrying it as peer-supplied.

| ID | Peer | Finding | P08 disposition |
|---|---|---|---|
| `XP-11` | **P05** `H-P08-1` | A sealed entry can be forced to a cancelled state by a raw write, because the posting state **is not a member of the integrity hash field set** | **VERIFIED INDEPENDENTLY BY P08 AT 18.0.** The entry-level hash covers name, date, journal and company — **four fields, and the posting state is not among them.** Positive control fired on known members. **This is the same hole P08 reached from the opposite direction**: `43` records a company-level write executing four raw statements that flip posting state directly. Two processes, two entry points, one uncovered field. `FACT VERIFIED` |
| `XP-12` | **P05** `H-P08-4` | The accounting date is taken from the clock in two of three branches; the third computes the first open period **after** the lock and books there | **CONFIRMS AND EXTENDS P08.** P08's own finding is that the *core posting path* relocates. P05 shows a **feeder process independently implementing the same relocation** — so relocation is not one routine's behaviour, it is a pattern peers reproduce. Carried as peer-supplied; P08 did not re-derive the expense path |
| `XP-13` | **P05** `H-P08-7` | A period can close containing **draft** entries, because entries are created at approval and posted later | **CONFIRMS P08.** P08 established there is no period object and no completeness gate; P05 supplies the operational instance. Bears on `P08-BD-17` |
| `XP-14` | **P05** `H-P08-2`, `H-P08-3` | Four paths sever the claim-to-entry link, and the partial-deletion guard reads a field the other three have already cleared; entries are created under elevated privilege at approval so approvers need no accounting rights | **ADOPTED as evidence for `41`'s provenance finding.** This is a **named mechanism** for the 17.00% of items carrying no provenance mark: the link is not merely absent, it is **actively cleared by four code paths**. Peer-supplied; P08 did not enumerate the four paths |
| `XP-15` | **P06** `28` §5 (five inputs) | (1) reconciliation must be inside the close regime; (2) RELOCATE is not an acceptable default; (3) lock inheritance across possibly-distinct legal entities must be a declared decision; (4) the pre-close control is one-time only; (5) **no accounting-relevant field may be written by raw SQL that bypasses the guard layer** | **ACCEPTED as design inputs; input (5) is INDEPENDENTLY CONFIRMED BY P08.** `43` documents exactly such a path in the accounting core. **Two processes reached the same prohibition from different modules.** Inputs (1)–(4) are recorded for P11 and the Boss; P08 does not decide them — see §5 |
| `XP-16` | **P04** `P04-B-43` | The effective hard lock is the **maximum over the whole parent chain**, computed with elevated privilege, including archived companies, irreversible | **ACCEPTED, peer-supplied, and it sharpens P08's scope work.** `37` treats the lock as a company-scope control. P04 shows it is a **hierarchy-scope** control that binds companies the scope model may treat as separate legal entities. Recorded against `P08-BD-17` and CORR1. **P08 did not re-derive the traversal.** Class: peer-supplied `FACT VERIFIED`, carried as `B` for P08's own scope |
| `XP-17` | **P04** `P04-B-45` | A **second re-dating path that involves no lock at all**, firing on a document-date change on any non-sale document | **MATERIAL, and P08 had not found it.** P08's period work assumed relocation is lock-driven. If a date can move with no lock configured, then the deployed measurement — 0 of 89 companies locked — **does not bound the exposure**. `C NOT YET SEARCHED` for P08; routed to §4 as the highest-value remaining search |
| `XP-18` | **P07** `X-11`, `X-12`, `X-13`, `H-06` | Every tax report selects on P08's accounting date; a tax-period state distinct from the accounting close is needed; and a month-end tax settlement to named accounts is described in the chart but its mechanism is unconfirmed | **X-11/X-12 ACCEPTED as design inputs.** P08's evidence — no period object, close is a date comparison — means P07's tax period **cannot** be expressed today except as another date range. **X-13/H-06 ANSWERED in part:** P08 found no posted period-closing mechanism of any kind, tax or profit-and-loss; the year-end result is derived at report time. `A VERIFIED ABSENCE` for a closing **entry**, bounded to 22 roots; `C` for a tax-specific settlement wizard, which P08 did not search by name |
| `XP-19` | **P09** `H08-1`, `H08-2`, `H08-3` | The allocation carrier is at **row** granularity while the attribution's subject is the **event**; no account-type or row-type test gates the management record | **CONFIRMS `41` FROM AN INDEPENDENT DIRECTION.** P09 found granularity mismatch in the analytic dimension; P08 found provenance sitting one level above the object the statements read. **Same defect shape, two subsystems.** Recorded as one structural finding with two instances |
| `XP-20` | **P09** `H08-5`, `H08-6`, `H08-7` | Three core-accounting instances re-routed to P08: the cut-off pair where **the analytic cut-off does not happen**, the change-account transfer, and the accrued-orders residue | **ACCEPTED, `C NOT YET SEARCHED` by P08.** Routed to §4 |
| `XP-21` | **P03** `R-16` | Idempotence must be solved once at the ledger, not per process; the locked-period re-dating hits every programmatic post | **CONFIRMS P08** and matches `38`. P03 independently concluded the owner is P08 |
| `XP-22` | **P10** `OUT-01`, `OUT-03` | The nets-to-zero attribution defect also occurs in deferred recognition; and **the untested path is the live one** — the lock refusal is covered by a test on a generation path **zero deployed companies use**, while the silent re-date sits on the live path | **`OUT-03` IS MATERIAL AND CORROBORATES P08's DEPLOYMENT FINDING.** P08's recurring structural finding is *controls present in source, unengaged in deployment*. P10 supplies its mirror: **test coverage present on a path deployment does not use.** Recorded as an extension of that finding, peer-supplied |
| `XP-23` | **P02** | No P08-addressed handoff found in the P02 package under the searched pattern | `B NOT FOUND IN SEARCHED SCOPE` — 0 of 197 references. P02's ledger-relevant finding (zero cost-of-sales lines in the deployed data) reached P08 through the shared database evidence, not through a handoff |

---

## 3. Outbound — corrections P08 owes its peers, and they are not minor

**P08 has retracted a claim that at least two peers built on.** This section exists because a peer's package will otherwise carry P08's error.

### `OUT-P08-01` — the withdrawn accounting-event claim. **URGENT.**

P08 published, at head `4bdf8a2`:

> *"No accounting-event object exists in any of the 22 declared roots, so `ONE FACT → ONE ACCOUNTING EFFECT` is unenforceable."*

**P10 adopted this as `IN-05` and, on its basis, RELOCATED ITS CENTRAL DESIGN ELEMENT** — writing that P08, not P10, must author the accounting-event object, and that P10 must specialise rather than define one (`25` §2, `19` `D-14`/`E-01`, `27`). **P09 records the same absence as `H08-4`, its standing blocking dependency and the stated ground for `AAS+-VETO-01`.**

**P08 has WITHDRAWN that claim as `CONTRADICTED`** — see `39_P08_ACCOUNTING_EVENT_IDENTITY_FORENSIC.md`. Database-enforced identity carriers **do** exist for specific inbound channels, verified directly. The census pattern that produced the absence searched model names for the token *event*; **none of the carriers is named with it.**

**The corrected finding, which peers must use instead:**

> Durable accounting-event identity **exists for a minority of inbound channels, is enforced by database constraint where it exists, is not a platform property, and is unpopulated in the deployed data — 0 of 13,814 bank statement lines carry either key.**

**Effect on the peers' own conclusions — stated by P08, decided by them:**

| Peer item | Effect |
|---|---|
| P10 `IN-05` / `E-01` / `D-14` | The *premise* changes; **P08's assessment is that the conclusion largely survives** — a per-channel key populated nowhere is not a platform event identity, so P10's relocation is still supportable. **But it now rests on a different and weaker fact, and P10 must re-state its ground.** P08 does not re-classify a peer's finding |
| P09 `H08-4` / `AAS+-VETO-01` | Same. A veto grounded on *"no identity exists"* must be re-grounded on *"identity exists per channel, is not a platform property, and is unpopulated"* |
| P10 `IN-07` | *"…no database-level enforcement in 22 of 22 roots"* — **partially contradicted by the same forensic pass.** Database-level uniqueness constraints do exist on some carriers |

### `OUT-P08-02` — the root-set constraint peers adopted is out of date, **in P08's favour**

P10 adopted `IN-14` / `CN-03` / `RF-01`: *"P08 closed the root-set defect for only 3 of ~23 class-A claims; carry the rest as class C."* **That was correct against head `4bdf8a2`.**

`34_P08_CLASS_A_ROOT_SET_REVALIDATION.md` has since re-run the class-A patterns across all 22 roots, each with a positive control. **The prohibition is now closed for 16 of 19 claims**, and **three first-pass results were withdrawn as pattern artefacts rather than quietly corrected.** Peers holding P08 claims as class `C` on root-set grounds alone may re-read them at their published class — **except** the three withdrawn, which must not be carried at all.

### `OUT-P08-03` — the version premise

P08's source observations are product line **18.0**. The deployed databases are **16.0, 19.0, 19.0**. **No deployed database matches the source line** (`40`). Any peer that combined a P08 source statement with a P08 deployed count as a single fact should re-read it as two facts with two scopes.

### `OUT-P08-04` — corroborations P08 supplies back

| To | P08 evidence |
|---|---|
| **P05** | The posting state is outside the integrity hash — **independently verified at 18.0 by P08**, so `H-P08-1`'s premise is confirmed from two packages |
| **P06** | Input (5) — a raw-SQL write of an accounting-relevant field bypassing the guard layer — **exists in the accounting core**, not only in the modules P06 examined |
| **P04**, **P06**, **P10** | The lock relocates rather than refuses: verified by P08 against source and by the product's own test. **And extended by deployment evidence P08 alone holds: 0 of 89 companies have any lock set, so the relocation path was never reached in the measured estate** |
| **P07** | No posted period-closing entry of any kind exists — the year-end result is derived at report time. This bears directly on `X-13` |
| **all** | 447,384 items, 1,851 transaction-currency imbalances, 83,820 origin-less entries, 6,418 backdated beyond a year, 0 of 64 journals sealed. **Peers reasoning from source alone have been reasoning about controls that are switched off** |

---

## 4. What this intake opened that P08 has not closed

| ID | Item | Class | Owner |
|---|---|---|---|
| `P08-U-13` | **The lock-free re-dating path** (`XP-17`). If a date moves with no lock configured, the 0-of-89 measurement does not bound the exposure | `C NOT YET SEARCHED` | **P08 — highest-value remaining search** |
| `P08-U-14` | P09's three core-accounting instances (`XP-20`), including an analytic cut-off that does not occur | `C NOT YET SEARCHED` | P08 |
| `P08-U-15` | Whether a tax-specific settlement mechanism exists under a name P08 did not search (`XP-18`) | `C NOT YET SEARCHED` | P08 with P07 |
| `P08-U-16` | Whether P01 published under a different branch naming | `C NOT YET SEARCHED` | P08 |
| `P08-U-17` | P04's hierarchy-wide lock traversal, not re-derived by P08 | peer-supplied, `B` for P08 | P08 |

## 5. What P08 does not decide here

P06's inputs (1)–(4), P07's tax-period state, P10's kernel authorship and P09's veto ground are **design and governance positions**. P08 supplies evidence and its own corrections; it does not adjudicate another process's finding, does not close another process's blocker, and does not author the target architecture. Those belong to **P11 and the Boss**.

**Contradictions are preserved, not harmonised.** `P08-CONTRA-21` stands unresolved. No peer finding was rewritten to agree with P08, and where a peer's premise came from P08 and P08 was wrong, §3 says so plainly rather than leaving the peer to discover it.

---

## 6. `P08-U-13` DISCHARGED — the lock-free re-dating path is real, and P08 had missed it

`XP-17` was recorded above as P08's highest-value remaining search. **It was run, and P04's finding is CONFIRMED at 18.0 source, with a deployed measurement P04 did not have.**

### 6.1 The mechanism — 18.0 source, `FACT VERIFIED`

The entry's accounting date is a **computed field that depends on the document date**. It fires on any change to that date. Its body does two things:

1. **It exempts sale documents.** For a sale document the accounting date is simply the document date.
2. **For every non-sale document it calls the accounting-date routine** — the same routine that performs lock relocation.

**And that routine relocates even when no lock exists.** The lock branch is one guarded block inside it; **below that block, with the lock set empty, two branches still run for non-sale documents:**

| Condition | Result |
|---|---|
| The document date is in a **month earlier** than today | the accounting date becomes the **last day of the document's month** |
| The document date is in the **current month** | the accounting date becomes **the later of the document date and today** |

**No lock is consulted for either. The accounting date of a purchase document is system-derived from the clock, and the deployed evidence that 0 of 89 companies configure a lock does not bound this at all.**

### 6.2 The deployed measurement — `DB-SM`, product line 16.0

**ENUMERATION.** POPULATION: 183,590 entries in `DB-SM`, restricted to posted entries carrying both a document date and an accounting date. PATTERN: direct comparison of the two date columns, partitioned by document class. PATH SET: the account-entry extract. UNIT: **one posted entry**. POSITIVE CONTROL: the same pattern returns 3 divergences in the sale class, so it can fire on both sides of the partition and a zero would have been meaningful.

| Document class | Posted entries | Accounting date ≠ document date | Share |
|---|---|---|---|
| **Sale** | 2,605 | **3** | **0.12%** |
| **Purchase** | 36,961 | **7,745** | **20.95%** |

**The asymmetry is 175×, and it is exactly the asymmetry the mechanism predicts** — the sale class is exempted in the code, the purchase class is not.

### 6.3 Where the author stops short of the causal claim

Direction of the 7,745:

| | Count | Share |
|---|---|---|
| Accounting date **later** than the document date | 2,123 | 27.41% |
| Accounting date **earlier** than the document date | **5,622** | **72.59%** |

**The 18.0 mechanism can only move a date forward or to a month-end. It cannot move one backward.** So the majority of the divergence is **not** explained by it.

Testing the 2,123 forward-movers against the mechanism's two signatures:

| Signature | Count | Share of forward-movers |
|---|---|---|
| Stays within the document's own month — the *later of document date and today* branch | 1,890 | **89.02%** |
| Lands on a month-end — the *prior month* branch | 249 | 11.73% |
| **Explained by one branch or the other** | | **~100%** (the two overlap slightly) |

### 6.4 Classification

| Claim | Class |
|---|---|
| A non-sale document's accounting date is system-derived from the document date **with no lock involved**, and sale documents are exempt | **`FACT VERIFIED`** — 18.0 source |
| Accounting-date divergence is **175× more common** on purchase documents than sale documents | **`FACT VERIFIED`** — 16.0 data, measured independently of the source read |
| The mechanism **caused** the 2,123 forward divergences | **`SUPPORTED INTERPRETATION`** — ~100% carry one of its two signatures, but 16.0 source was not read |
| What produced the **5,622 backward** divergences | **`UNRESOLVED — EVIDENCE REQUIRED`.** Manual accounting-date entry is the obvious candidate and was not tested |

### 6.5 Why this matters more than the lock finding it extends

P08's period work rested on: *the lock relocates rather than refuses, and 0 of 89 companies set a lock, so the relocation path was never reached.* **The second half of that is now wrong as a bound.**

> **Relocation is not a lock behaviour that a lock-free estate escapes. It is the default behaviour of the accounting date for every non-sale document, and it ran on 20.95% of purchase entries in a database with no lock configured anywhere.**

`P08-CONTRA-31`. This corrects P08's own framing in `36` §3, credits P04 with the finding, and returns to P04, P06 and P10 a deployed measurement none of them held. `P08-M-13` — **a measurement that bounds an exposure by a control's absence is only as good as the assumption that the control is the sole cause.**
