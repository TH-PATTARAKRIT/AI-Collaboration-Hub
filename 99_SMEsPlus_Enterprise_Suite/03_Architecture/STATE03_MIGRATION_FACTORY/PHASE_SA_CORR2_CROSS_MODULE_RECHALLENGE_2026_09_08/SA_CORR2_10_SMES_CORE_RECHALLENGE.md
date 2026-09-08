# SA_CORR2_10 — SMEs CORE MULTI-SPECIALIST RE-CHALLENGE
## CP-SA-C2-80 — SMEs CORE RE-CHALLENGE COMPLETE

Session: `[SMEPLUS-26-09-08-PHASE-SA-CORR2-XMOD-001]`
Governing law: master prompt §10 — *"SMEs Core must attempt to falsify the corrected package. No
single specialist may declare the flow ready."*
**Independence label, applied to every layer below: `INTERNAL ADVERSARIAL SELF-CHALLENGE`** — see
`SA_CORR2_11` §1. Not independent assurance.

---

## 1. How the re-challenge was constituted

Master prompt §10 requires falsification of the **corrected** package. The package was therefore
**frozen first**, at commit `e280611a`, before any challenge layer was given access to it. A
challenge run against a moving target measures nothing.

| Layer | Scope at dispatch | Knew the author's conclusions? |
|---|---|---|
| Five domain extractions | A question per domain, and the corpus | **No** — dispatched before the corresponding register was written |
| One adversarial challenge | The frozen package plus the parent, and told to falsify it | Yes — that is the point |
| Author self-check | Mechanical sweeps only | n/a |

**`AUTO-C2-06` satisfied:** every corrected material defect was re-tested by the relevant role, and
the re-test is what produced the correction in the first place — the domain extractions ran *before*
`SA_CORR2_01`…`SA_CORR2_09`, not after.

---

## 2. The twenty challenge dimensions

| # | Dimension | Result |
|---|---|---|
| 1 | Functional correctness | **FINDING** — `SA09` graded wrong item and wrong quantity as one class with one answer; they have opposite answers (`SA_CORR2_09` §2.1) |
| 2 | Input completeness | **FINDING** — `SA02`'s *"price determination is not evidenced"* survives; commercial policy is the one domain that stayed thin |
| 3 | Output completeness | **FINDING** — three outputs still have no consumer (`SA03-F-01`); unchanged and carried |
| 4 | Conditional routing correctness | **FINDING** — `SA05`'s seven `HOLD` natures were produced by an undeclared pattern (`C2-F-07`); all seven discharge |
| 5 | Inventory impact | **FINDING** — a stock-affecting flow existed that no register carried: maintenance part issue, `IR-18` (`C2-F-15`) |
| 6 | Manufacturing impact | **FINDING** — machine cost is not causally connected to machine use, `FACT VERIFIED`, `0 of 4` deployments |
| 7 | Purchase / AP impact | **FINDING** — the price-difference filter drops layers on a product mismatch with **no kit predicate**; 13 live rows against a 14,335 control |
| 8 | Sales / AR impact | **FINDING** — a **draft** invoice already consumes billable quantity while posting nothing (`H-05`) |
| 9 | Accounting Event / posting | **FINDING** — `BD-ACC-01` is complete for goods and **silent for services** (`C2-F-17`) |
| 10 | Tax impact | **NO NEW FINDING** — `SA08`'s position stands; the fiscal-position rule base remains *a black box in this evidence set*. **No statutory claim is made** |
| 11 | Bank / payment impact | **FINDING** — matching rows are freely destructible across a closed period, so the settlement state is **not durable** (`H-07`) |
| 12 | Data identity / ownership / lineage | **FINDING, and it is the largest** — the deterministic accounting-event identity is required by both domains, recorded missing by both, and owned by neither (`C2-F-13`) |
| 13 | Tenant / company isolation | **FINDING** — `RISK-U03`'s stated ground is superseded; 58 invariants now exist, `0` proven. The remedy changed and no consumer noticed (`C2-F-12`) |
| 14 | Approval / SoD / control | **NO NEW FINDING** — `XD-03` stands: the occurrence half populated on `0 of 27,874` rows |
| 15 | Auditability / traceability | **FINDING** — every established exception class writes into a ledger that can be silently re-dated past a lock (`C2-F-26`) |
| 16 | Standards applicability | **FINDING** — the ISO/SOC/GDPR overclaim is on **183 of 183 branches**, and one line of it escapes every standards pattern (`C2-F-19`, `C2-F-20`) |
| 17 | Clean-room independence | **FINDING IN THIS PACKAGE'S OWN WORK** — three leaks, all in correct text (`K2-15`) |
| 18 | Operational / UX recoverability | **FINDING** — a period lock that *"re-dates instead of refusing"* makes cut-off tests **self-confirming**; the user is told nothing |
| 19 | Unnecessary complexity | **NOT FOUND** — no register added structure not required by a business nature or a Boss boundary. `SA16`'s consolidated research programme is the opposite defect: **over-scoped**, and is reduced (`C2-F-10`) |
| 20 | Missing SMEsPlus advantage | **FINDING** — four determinations were missing and are added: `ND-09` cross-module cost identity, `ND-10` `Perpetual` defined explicitly, `ND-11` the service assertion, `ND-12` declare the complement |

**17 of 20 dimensions returned a finding.** Three did not, and each says why rather than being left
blank.

---

## 3. Material dissent register

| # | Challenger | Issue | Evidence | Severity | Correction | Resolution | Residual risk |
|---|---|---|---|---|---|---|---|
| `D-01` | Functional-domain specialist | `SA01`'s domain figures are not reproducible — `SA00` §6 says *"any declared term"* and declares none | `grep` for `pattern\|regex\|token\|declared` over the whole of `SA01` returns 6 lines, none naming a pattern | **MATERIAL** | Re-measured with the pattern published | **ACCEPTED IN FULL** — `SA_CORR2_03` §2 | The re-measurement is this session's own instrument and shares its bias |
| `D-02` | Functional-domain specialist | The declared PATH SET structurally excludes the mainline, so the five governing Boss decisions were unreadable | `awk '$1=="origin/SMEsPlus"' bpb.tsv` → **0 rows**; mainline carries 1,069 text files | **MATERIAL** | Corpus rebuilt; 2,748 → 3,789 blobs | **ACCEPTED IN FULL** — `C2-I-02` | The same defect is in the parent package and in every register that consumed it |
| `D-03` | Functional-domain specialist | *"`a11c9e7b` §3 is quoted from `SA05`, not from Boss — unverifiable from this population"* | Its population genuinely could not reach the decision body | SUBSTANTIVE | Author read the decision body directly | **DISSENT NOT SUSTAINED** — `SA05`'s transcription is **verbatim accurate** (`N-16`). The caution was correct given the challenger's population and wrong about the world | A challenger bounded to a defective corpus produces correct-but-false cautions |
| `D-04` | Exception specialist | `SA09` read **one of three blob versions** of a register — the only one lacking the section closing the gap it reported | 3 blobs at the path: 8,994 / 16,287 / 15,128 bytes; §13A absent from the first only | **MATERIAL** | Three of four classes re-adjudicated | **ACCEPTED IN FULL** — `C2-F-25` | 223 paths in the corpus carry multiple versions; no register uses that fact |
| `D-05` | Exception specialist | `SA09` graded idempotency `ESTABLISHED` while four Accounting packages record it absent — and the owning package had explicitly warned *"the two halves must not be collapsed into one tag"* | `FE-01`, `XM-01 HOLD`, `RISK-C02` | **MATERIAL** | Regraded downward | **ACCEPTED** | `SA09`'s count moves in **both** directions, which is the honest result |
| `D-06` | Governance specialist | The programme contradicts itself on `PASS`: a **Boss ruling** requires a *"PASS / HOLD recommendation"* | Boss approval line 12, verified by the author at source | **MATERIAL** | `SA13-F-01` re-framed | **ACCEPTED** — `C2-F-22` | The re-framing **removes an accusation**, which is convenient for the package; it rests on one quoted line, and that line was verified independently by the author |
| `D-07` | Governance specialist | The corpus cannot prove *"live on every branch"* — a diff-based corpus records a byte-identical file once | `bpb.tsv` shows 1 branch for that path | SUBSTANTIVE | Author used a per-branch tree lookup instead | **DISSENT SUSTAINED AS A METHOD POINT, CLAIM CONFIRMED** — 183 of 183, byte-identical | — |
| `D-08` | Governance specialist | Case-insensitive `COSO` matches a vendor name and inflates ~9× | 18 vs 2 blobs | SUBSTANTIVE | Case-sensitive counts used | **ACCEPTED** | Any earlier count run through the case-insensitive helper is suspect |
| `D-09` | Cross-proof specialist | The two Boss controls were read *"by commit citation, not from the working tree"* in every prior round | They are on mainline, which no branch diff reaches | **MATERIAL** | Author read both primary texts | **ACCEPTED** — `C2-F-11`. Both renderings turn out **accurate**, and element 14's conditional / element 10's non-conditional are confirmed verbatim | Accuracy here was luck, not control |
| `D-10` | Cross-proof specialist | *"Convening does not make anything provable"* — `0 of 22` is produced by element 10 alone, which is not COGS-caused | `REV-F-02`, verified verbatim by the author | **MATERIAL** | Recorded as the joint result | **ACCEPTED IN FULL** | The joint proof's honest output is that nothing is provable |
| `D-11` | Author self-check | Two of this package's own check-claims were false as written | Mechanical enumeration returned 24 of 29 and 6 of 18 | SUBSTANTIVE | Rows written out; re-verified | **ACCEPTED** — `C2-F-29` | A check line is the one claim readers never test |
| `D-12` | Author self-check | Three clean-room leaks in this package's Layer 1 files | Per-file token count against a parent baseline of 0 | SUBSTANTIVE | Scrubbed; scrub effect measured and published | **ACCEPTED** — `K2-15` | The leaked text was **correct** in all three cases |

---

## 4. Adversarial challenge of the frozen package

An adversarial challenge was commissioned against commit `e280611a` with instructions to falsify,
not to summarise. **Its findings and their dispositions are recorded at §6.**

---

## 5. `ND-05`…`ND-08` put through the source-copying test they never had

`SA20` §4 accepted that `SA12` §4 said *"Four"* determinations when there were eight, **so
`ND-05`…`ND-08` never went through `SA12` §6's source-copying test.** `K2-11` corrects the count;
the test itself is run here.

| # | Determination | Copied from the reference? | Test applied |
|---|---|---|---|
| `ND-05` | A reservation is a first-class, addressable business fact | **No — inverts it.** The reference holds reservation as a quantity on a balance record, which is exactly why an adjustment can silently break a customer promise | The reference shape is the counter-example, quoted in `SA06-F-04` |
| `ND-06` | A control that exists only in the user interface is not a control | **No — supplies what the reference lacks.** Three independent findings share the "enforced by the screen" mechanism | It is the complement of a rule the isolation set already carries for deferred work |
| `ND-07` | A period lock is a property of the entry, not of the path that reaches it | **No — inverts it.** The evidenced failure is precisely that the control was attached to paths | Two defeat paths, one leaving no record |
| `ND-08` | SoD degrades to a **recorded** compensating control, never a silent exception | **No.** The reference pattern for inventory SoD is `None evidenced`; this supplies a behaviour that does not exist there | A two-person SME must not be forced to bypass |
| `ND-09` | A cross-module fulfilment producing revenue must produce a cost recognition bound to the same identity | **No — inverts it.** The reference recognises the two halves in two modules on two dates with no identity between them | `TC-31` is the counter-example |
| `ND-10` | `Perpetual` and `Periodic` are defined explicitly wherever they appear | **No — the reference's own label moved between generations**, which is the reason for the rule | Primary-source field labels, two generations |
| `ND-11` | A service recognition event carries asserter, time and basis | **No — supplies what the reference does not record.** *"how is the performance of a service evidenced? The reference's answer is that it is not"* | Quoted counter-example |
| `ND-12` | An assurance activity declares its population **and its complement** | **No — not a reference behaviour at all.** It is a governance rule derived from this programme's own repeated failure | `C2-I-02`, three rounds |

**Eight tested, eight pass.** `ND-01`…`ND-04` were tested in `SA12` §6 and are not re-tested here
(`AUTO-C2-01`). `ND-02` remains the one determination flagged as *resembling* the reference shape,
adopted on independent rationale and **not hidden**.

---

## 6. Adversarial findings and dispositions

An adversarial challenge of the package frozen at `e280611a` returned **11 MATERIAL, 6 SUBSTANTIVE
and 3 MINOR findings.** Every material finding was independently re-measured by the author before
disposition; **none was adopted on the challenger's word.**

### 6.1 Material findings

| # | Finding | Author's re-measurement | Disposition |
|---|---|---|---|
| `A-01` | **`K2-08` claims corrections to `SA05`, `SA07` and `SA09` that received zero bytes of edit.** *"closes all seven"*, *"Four of the five share one shape"* and *"map one-to-one"* still stood verbatim | `git diff --name-only f0548a20 e280611a` → 8 files touched; `SA05`, `SA06`, `SA07`, `SA09`, `SA16`, `SA01` **untouched**. All three sentences confirmed still standing | **UPHELD IN FULL.** Corrected at `K2-16`…`K2-19`. **This is the package's own headline defect, committed at larger scale than the round it corrects** — `C2-F-30` |
| `A-02` | **Every status upgrade was absent from the register it upgrades**; and CORR2 rewrote `SA15`'s header from a table it declined to update | `SA06` `IR-12/13/14` confirmed still `NOT RECONCILED`; `grep -c 'TRAVERSABLE WITH A NAMED BREAK' SA15` → **0** | **UPHELD IN FULL.** `K2-17`, `K2-20`. The `K2-02` header rewrite was the aggravating instance: it published a count derived from a table CORR2 knew to be stale |
| `A-03` | **CORR2's own edits broke the parent's SHA-256 manifest** while `SA_CORR2_00` §3 published it as *"23 of 23 OK"* | `shasum -a 256 -c` → **8 FAILED, 15 OK** | **UPHELD.** `K2-24`: manifest regenerated, supersession noted, and §3's claim re-scoped to the state it actually tested |
| `A-04` | **Clean-room: residual vendor tokens** — a reference product version used as identity, a vendor name, a selection key | Confirmed by per-file sweep | **UPHELD.** Neutralized. Full sweep now **0 across all files**. *(Three earlier leaks had already been found by the author's own sweep at `K2-15`; these are additional)* |
| `A-05` | **`SA_CORR2_08` §2.1's *"twenty paths, purely from two extra negation forms"* is wrong by an order of magnitude** | Re-run inside one implementation: 12-term **275/271**, 14-term **273/269**. **Delta = 2, not 20** | **UPHELD.** The published 269 **does** reproduce; the *demonstration* did not. Corrected — and the corrected version is stronger: **two implementations of the same declared list gave 271 and 289**, so the list is necessary and not sufficient |
| `A-06` | **Six status-summary tables state class tallies that contradict their own rows** — each summing to the correct total, which is why none was caught | All six re-counted by reading the status column | **UPHELD IN FULL.** `SA_CORR2_05` 13/4/1 → **14/3/1**; `_06` 16/13/0 → **15/14/0**; `_02` 1/14/3 → **1/13/4**; `_04` five advanced → **four**; `_08` seven → **eight**; `_00` summary re-derived. **An identifier check cannot see a mis-assigned class** |
| `A-07` | **The dropship attribution table sets a parent directory against three of its own children as if disjoint**; total 76 vs 91 | Measured: total **91**, under `STATE03_MIGRATION_FACTORY` **78**, elsewhere **13**. The three "siblings" are children | **UPHELD.** Table rebuilt as one disjoint attribution plus one explicitly non-disjoint programme breakdown. **The load-bearing sub-claim reproduces exactly: `ACCOUNT_REOPEN` = 20, of which 16 in Order-to-Cash** |
| `A-08` | **`SA_CORR2_09` §3's partition is broken** — three classes double-counted, and `SA09`'s fifth `NOT ESTABLISHED` row silently dropped | Confirmed | **UPHELD.** Re-partitioned by enumerating all twenty class members: **16 established / 4 not established** |
| `A-09` | ***"the only one of the five that survives"* is contradicted two paragraphs later in the same file**; and `SA_CORR2_07`'s *"36 hits, all read"* is not reproducible | Verb sweep → **48 occurrences / 45 blobs / 45 paths**, not 36 under any unit | **UPHELD.** Both universals narrowed. Two of `SA09`'s five survive; the standards claim restated as a **bounded** negative naming the 30 unextracted binaries |
| `A-10` | **§1 exculpates 269 `PASS` occurrences with a Boss instruction covering 18**, and refuses to apply the same logic to `B-35`, where the same document authorizes *"certification"* by name | Boss approval line 21 confirmed: *"GATE-05 B-35 full twelve-control independent certification"* | **UPHELD, AND IT IS THE MOST IMPORTANT ONE.** The error ran in the direction that removes an accusation from a pack Boss reads. Scope corrected to 18; the `B-35` asymmetry corrected; the surviving finding — `B-35` recorded both `CERTIFIED` and `NOT CERTIFIED` — is unaffected |
| `A-11` | **Ten citations to files that did not exist**, four of them the evidence pointers for `N-01`…`N-04`; two written **into the parent package** | Confirmed at the frozen commit | **PARTIALLY UPHELD.** `SA_CORR2_10` and `SA_CORR2_13` now exist and every pointer resolves. **The finding stands as a process defect**: a package must not ship citing artefacts it has not yet written, and two dangling pointers were written into a parent register whose pointer integrity `SA_CORR2_00` §3 had just certified |

### 6.2 Substantive findings

`S-01` the `SA_CORR2_01` header cited the superseded v1 frame including the retired `U2 2,606`
figure — **upheld, corrected**. `S-02` `E2E-05` was upgraded with wording that read as claiming the
hops are sound while §6 grades two of them broken — **upheld, wording corrected; the classification
stands, because a *named break* is what it is**. `S-03` *"52 files"* counted path-blob rows not
unique paths — **upheld, 35**. `S-04` re-published the parent's `223` without re-measuring — **upheld,
222**. `S-05` `SA_CORR2_02` counted its own scope three ways — **upheld, scope declared**. `S-06`
duplicate `### 4.4` anchor — **upheld, renumbered**.

### 6.3 What the challenge could not falsify

Reported because a challenge report that lists only hits is not a result. Everything below was
re-run by the challenger and reproduced exactly: the 183-branch population on three command shapes;
the corpus figures and controls; **every figure in `SA_CORR2_03` §2.2, both units**; `\bcancel`
under Order-to-Cash = 23 on four units; **title-passage = 6 paths, all inside the Phase SA package,
`ACCOUNT_REOPEN` = 0**; the 183-of-183 byte-identical compliance claim; **the three blob sizes on
which `C2-F-25` turns**; and **ten verbatim quotations, with no misattribution and no
`PROVISIONAL`/`CANDIDATE` source passed off as `FACT VERIFIED`**.

### 6.4 `C2-F-31` — where the defects clustered, and what that says

| Class | Count | Caught by |
|---|---|---|
| **Corrections claimed but not applied** | 2 (`A-01`, `A-02`, spanning 6 registers) | adversarial challenge only |
| **Counting / partition** | 4 (`A-05`…`A-08`) | adversarial challenge only |
| **Over-wide universal** | 2 (`A-09`, `A-10`) | adversarial challenge only |
| **Clean-room** | 1 (`A-04`) | author's sweep found 3, challenge found 3 more |
| **Evidence-pointer / process** | 2 (`A-03`, `A-11`) | adversarial challenge only |
| **Reasoning defect** | **0** | — |

**Not one finding overturned a conclusion.** Every material status change, every falsification of a
parent claim, and every quotation survived. **What failed was the bookkeeping around them** —
which is precisely the pattern `SA18-F-02` recorded for the parent package and warned should not be
read as strength. It is not read as strength here either: **a package whose reasoning survives an
adversarial pass that finds eleven material bookkeeping defects has been challenged on its
bookkeeping, not on its reasoning**, and the challenger was the same model as the author
(`SA_CORR2_11`).

---

## 7. What no specialist declared

Per master prompt §10, **no single specialist declared any flow ready, and none is declared ready
here.** Every status change in this package is a change in *what is determined*, not in *what is
proven*. The proof obligations remain at zero (`SA_CORR2_12` §7).

---

`CP-SA-C2-80 — SMEs CORE RE-CHALLENGE COMPLETE (execution status).` 17 of 20 dimensions returned a
finding; 12 specialist dissents recorded (10 accepted, 1 not sustained, 1 sustained as method only);
**and an adversarial pass against the frozen package returned 11 material findings, 10 upheld in
full and 1 partially, every one of them re-measured by the author before disposition.**

Checkpoint completion is **not** Boss approval.

Boss remains the sole Final Approver. No Evidence = No Progress. Never Skip Gate.
