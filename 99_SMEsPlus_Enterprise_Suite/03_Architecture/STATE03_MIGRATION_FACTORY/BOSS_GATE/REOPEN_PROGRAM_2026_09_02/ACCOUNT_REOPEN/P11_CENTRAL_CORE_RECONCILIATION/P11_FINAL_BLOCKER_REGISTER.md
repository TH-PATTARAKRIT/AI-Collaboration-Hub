# P11 — FINAL BLOCKER REGISTER

Session `SMEPLUS-26-09-04-ACC-P11-CORE-RECON-REV2-001` · Layer 1 clean-room
Every blocker ends as **exactly one** of the ten permitted statuses. No vague status is used.

> **Recommendation only. Boss is the sole Final Approver.**

---

## 1. P11's own blockers

| id | Blocker | Final status |
|---|---|---|
| `P11-B-01` | **`P01`–`P10` have published nothing.** 0 artefacts at 0 commits across 10 processes | **`HOLD — PEER PROCESS REQUIRED`** |
| `P11-B-02` | **No accounting-event identity exists** (`UAE-29`). `C1` fails 44 of 44; `DC-01` unguardable; 9 of 23 dependencies sit downstream | **`HOLD — BOSS DECISION REQUIRED`** — the root |
| `P11-B-03` | **0 of 17 double-counting classes has a working guard.** 4 of the 17 are root-independent design failures | **`HOLD — BOSS DECISION REQUIRED`** |
| `P11-B-04` | **The programme has no declared output path.** Six sibling sessions wrote to six locations; this is a seventh | **`HOLD — BOSS DECISION REQUIRED`** (`P11-F-01`) |
| `P11-B-05` | **`BC-02` binds Inventory → Accounting only.** Nine producing processes hand facts to the ledger under no contract | **`HOLD — BOSS DECISION REQUIRED`** (`P11-F-02`) |
| `P11-B-06` | **`DC-09` double cost absorption.** TAS 2 ¶12 requires absorption; building it without an explicit relief of the period-expense line charges depreciation twice. **No relief mechanism exists in anything the programme has read** | **`HOLD — BOSS DECISION REQUIRED`** — new at P11 |
| `P11-B-07` | **`DC-07` candidate double tax recognition** — `M-02` auto-reverses on unmatch, `M-03` is not stated to | **`HOLD — SOURCE EVIDENCE REQUIRED`** — new at P11 |
| `P11-B-08` | **Four objects have no determinable scope**: tax configuration, equipment/machine ownership, budget, migration/replay batch | **`HOLD — SCOPE EVIDENCE REQUIRED`** |
| `P11-B-09` | **`AASR`'s parent baseline predates its parent's closure** — `V-SYS-2` applied to `AASR` itself | **`HOLD — CONTRADICTION`** (`P11-C-01`) |
| `P11-B-10` | **The `22`-scenario cross-proof baseline stands at 0 of 22 evidenced** — 30 of 30 producer debit/credit cells withheld, 0 of 10 handoffs contract-compliant | **`HOLD — PEER PROCESS REQUIRED`** |
| `P11-B-11` | **Analytic is not a subledger of record**, so no `P09` figure reconciles to the ledger across a correction | **`HOLD — BOSS DECISION REQUIRED`** |
| `P11-B-12` | **`P05` and `P10` producer contracts are not established at all** | **`HOLD — PEER PROCESS REQUIRED`** |
| `P11-B-13` | **The unified event-to-GL matrix has not been reconciled against the published peer matrices** (`P03`, `P04`, `P06` each publish one; `P06` alone carries 31 event→entry rows) | **`HOLD — PEER PROCESS REQUIRED`** |
| `P11-B-14` | **The exception to "unrelated independent companies = separate tenants by default" is undeclared, and no granting authority is named** (`P11-SR-01`) | **`HOLD — BOSS DECISION REQUIRED`** → `D-11` |
| `P11-B-15` | **Whether a company hierarchy may span a tenant boundary is unruled, and no enforced tenant-assignment invariant exists** (`P11-SR-02`) | **`HOLD — BOSS DECISION REQUIRED`** → `D-12` |
| **`P11-B-16`** | **`T0-13` — an accounting fact may be SILENTLY MUTATED, at any scope.** Widened at Delta 04: the defect needs **no tenant boundary and no company hierarchy** — inside a single company an entry aimed at a locked period is already re-dated with no refusal and no trace (`P04-F-68`, `FACT VERIFIED`). **Reachable today, so it stands whatever the Boss rules on `D-12`.** Close condition **REFINED at Delta 08 §2**: `UAE-05` is a **second** re-dating path that **fires with no lock configured**, so there is nothing to refuse — **where a mutation path has no violation to detect, an attributable trace is MANDATORY, not alternative.** A design satisfying this boundary by implementing refusal alone would leave `UAE-05` live | **`HOLD — BOSS DECISION REQUIRED`** · **tolerance-zero** · **present defect** · **found narrow three times** |

**18 blockers. 0 closed by this session.**

| id | Blocker | Final status |
|---|---|---|
| **`P11-B-18`** | **Five of the nine `P11-E-26` repairs were made as unmarked replacements**, so a later edit could erase them undetectably (`P04`'s defect (b); `P11-G-03`). The erasure audit ran clean **over the marked set only** and cannot see these | **`HOLD — DESIGN RESOLUTION REQUIRED`** · CORR1 |
| **`P11-B-17`** | **The CRITICAL challenge finding `X2-F06` is UNREPAIRED.** `P11_SUBLEDGER_ARCHITECTURE.md` §1 states *"failing `S3` **or** `S4` ⇒ derived view"*; §2 applies *fails both*. Re-running the ten rows against the **stated** rule takes the register's headline *"3 unqualified"* to **0** (`X2-F07`). **Head of the CORR1 correction backlog.** Deliberately not repaired in-session — *bodging a critical logic error to clear an audit is how it went unrepaired for 30 commits* (`P11-E-26`) | **`HOLD — DESIGN RESOLUTION REQUIRED`** | `P11-B-13`…`P11-B-16` added by Deltas 01–03.

## 2. Inherited blockers P11 carries forward without weakening

| id | Blocker | Status as its owner declared it |
|---|---|---|
| `GB-01`…`GB-08` | Account Wave A's eight | **`HOLD`**; `GB-08` `BOSS DECISION REQUIRED` |
| `MCU-21` | **The reference core root set is undeclared. 22 roots exist** | **`HOLD — BOSS DECISION`**; cost to close **hours, mechanical** |
| `T0-01`…`T0-12` | Twelve inherited tolerance-zero boundaries | **`UNRESOLVED` ×12, `0` resolved.** `CONDITIONAL PASS` unavailable **by rule** |
| `MCU-01`…`MCU-20` | 17 standing gating unknowns, 8 ledger-gating | **`HOLD`** |
| `JT-01`…`JT-12` | Twelve Joint decisions | **12 open; `JT-01`/`JT-04`/`JT-05` `NOT DECIDABLE`** |
| `BLK-01`, `BLK-02` | Asset UAT items | **`HOLD — UAT REQUIRED`** |
| `BLK-07`, `BLK-08` | Asset design decisions | **`HOLD — DESIGN DECISION REQUIRED`**; AAS+ veto on costing implementation |
| `GAP-FS-07`, `GAP-FS-08`, `RISK-U03`, `RISK-C02` | Inventory structural gaps behind contract elements 10, 14, 15 | **open** |
| `CF-F-04`, `CF-F-05` | Inventory MTI conformance structural gaps | **open** |
| `RC-V-01`, `AAS-V-02`, `AASR-VETO-01`, Asset costing veto | Four standing vetoes | **none discharged** |

## 3. What closes what — ranked by cost, not by severity

| Cost | Items | Work |
|---|---|---|
| **One query each, minutes** | `Q-04` installed-module list (**caps every negative finding in two packages**), `Q-01` day convention, `Q-02` duplicate machine records | UAT, read-only, under ten minutes total |
| **A declaration, hours** | `MCU-21` root set; `P11-B-04` output path; `P11-B-08` four scope determinations | No new research. Closing `MCU-21` **re-scopes `MCU-18`, `MCU-19b`, `GB-07`, `GB-08` and every class `A` absence at once** |
| **A Boss decision, no research closes it** | `P11-B-02` event identity, `GB-08`, `BLK-07`, `JT-03`, `P11-B-05` contract scope, `P11-B-06` absorption relief | — |
| **Business-SME input — no AI may answer** | `SME-Q-02`, `SME-Q-03` → `JT-04`, `JT-05` | — |
| **Thai statutory** | `TH-NEW-01`, `TH-NEW-02`, `TX-H01`…`TX-H07` | Authoritative evidence only |
| **A running instance** | `MCU-01`, `MCU-20`, `T0-03`, `T0-07` runtime half, the live FIFO-return test | Executed runtime behaviour has no substitute |
| **CORRECTED — `P11-F-09`** | ~~`MCU-19`~~ | **`MCU-19` is a DATABASE question, not a runtime one** — *"does any migrated/restored **database** hold a rate row whose company has a parent?"* **Readable PostgreSQL dumps exist on this host.** Cost restated: **`UNKNOWN, plausibly cheap`**, not *a running instance*. **Not answered here** — see the declared boundary below |
| **Peer publication** | `P11-B-01`, `P11-B-10`, `P11-B-12`, and 15 of the 30 withheld cells | `P01`–`P10` |

### `P11-F-09` — a capability claim in P11's own register, tested and found over-stated

Prompted by `P04` @ `7d4ca03`, applying `P07`'s generalisation of `P04-REV-19`: **a statement that
something is unavailable to this session is a capability claim, and a capability claim is evidence.**
`P04` applied it to its own *"no database access was attempted"* and recovered two findings from
evidence it had declared away.

**P11 tested its own analogous classification. Executed this session:**

| Check | Result |
|---|---|
| Readable PostgreSQL dumps on this host | **Yes — 4+**, in `~/Downloads` and subdirectories |
| `pg_restore` / `psql` installed | **Yes** |
| `BK12MAY26_2026-08-03` archive header | **readable** — Dump Version `1.14-0`, **19,957 TOC entries** |
| `iTEST02_2026-07-14` archive header | **NOT readable** — *"unsupported version (1.16) in file header"* |
| Table-data extraction | **NOT PERFORMED — refused by this session's permission boundary** |

> **Boundary declared, so this is not read as more than it is.** P11 established that database
> evidence **exists and is at least partly readable**. P11 did **not** establish that `MCU-19` is
> answerable from it, because the extraction was refused. The honest cost is **`UNKNOWN, plausibly
> cheap`** — and the previous *running instance* classification was a capability claim P11 never tested.

**Two facts that outlive `MCU-19`:**

1. **Readability is not uniform** — one dump is readable by the installed client and another is not, on
   a version boundary. *"Database evidence is available"* and *"no database access"* are **both** wrong;
   the true statement is **per artefact**.
2. **This is the programme's recorded failure mode, not a new one.** The lineage already carries
   *never declare no code access from a working-tree search*, and a prior process missed these same
   dumps with four independent challenges missing it too. **P11 inherited it into a Boss-facing cost
   column.**

### `P11-F-10` — instrument-selected evidence bias: a default toolchain can choose the subset where the defect is absent

Reported by `P07` @ `1c8b879` as a **research** item, derived from `P11-E-25` and `P04`'s per-artefact
readability rule. Stamping the client version against all five of its databases:

> **Both deployments in which `P07-F-01` fires are `v1.16` and cannot be opened by the host's default
> client. Both in which it does not fire are `v1.14` and open with stock tooling.**
>
> *"A reader reproducing my finding with default tooling can open **only** the deployments where the
> defect is absent, and would reasonably conclude I am wrong."*

**Generalised, and this is the part that reaches every process:**

> **Tool capability can correlate with the evidence's own generation.** Where it does, a default
> toolchain does not merely see *less* evidence — it sees a **biased subset**, and if the defect
> distribution also correlates with generation, the bias runs **against** the finding.
>
> **This is not a completeness gap. It is a named wrong conclusion**, reachable by a competent reader
> following correct procedure with stock tools.

**Consequences P11 records:**

1. **`D-3b` is amended.** Authorisation to read the host's dumps must **specify the client version and
   require every generation to be opened**, or the reading reproduces the bias it was meant to remove.
2. **Every negative claim in this programme resting on database evidence must state the client version
   used and the generations actually opened.** Under `DR-NC-01`, a class `A` *verified absence* derived
   from default tooling over one generation is bounded to that generation, **and the boundary is
   invisible because the tool failed silently on the others.**
3. **P11's own `P11-F-09` correction is now insufficient as written.** *"All dumps tested are readable
   with the right client"* is true and incomplete: it does not say that **which** client was used can
   determine **which conclusion** is reached. Corrected here.

### `P11-F-11` — convenience of location chose the evidence base, in P11's package as well

`P07` @ `55a67bb` reports, as **research**, that applying `P11-F-10` to its own three database-derived
negatives **refuted one of its own findings**: one claim held on 3 of 3 identities, one was constrained,
and **`P07-F-60` was withdrawn** — 5,201 withholding certificates exist in a database it had never
opened. The cause it names is not tooling:

> *"`iTEST02` has **23** move lines. `iSMEs` has **447,384**. I built my entire runtime section on the
> **smallest database available**, because it sat inside my declared PATH SET and was therefore the one
> I opened first. **Convenience of location determined my evidence base.** The corrective is not 'open
> more databases' but **rank the population before choosing** — I had the file sizes in front of me and
> did not use them."*

**P11 ranked them independently rather than accepting the report** — a peer's message is a summary of
its evidence. Executed this session:

| Bytes | `TABLE DATA` entries | Dump version | File |
|---|---|---|---|
| **155,443,710** | 651 | `1.14-0` | **`iSMEs_2026-07-11`** |
| 64,303,340 | 1,315 | `1.16-0` | `iTEST02_2026-07-14` |
| 35,679,594 | 881 | `1.14-0` | `BK12MAY26_2026-08-03` |
| 24,911,161 | 875 | `1.14-0` | `iEVING_2026-07-23` |

> ### The finding applies to P11. **The largest database — 2.4× the next — was never opened.**
> `P11-F-09` tested `iTEST02` and `BK12MAY26`: **the first two a `find` returned.** P11 selected by
> **traversal order**, not by rank, and never looked at the sizes it had already listed. Same defect,
> different process, and P11 was the process that published the tooling rule which exposed it.

**Two facts about the ranking itself, recorded because the method is the point:**

- The `find`-driven loop **failed to rank two files** whose paths contain spaces (`SOURCE CODE/`,
  `ACCOUNT/01 ACCOUNT/`). It failed **visibly** — `stat:` errors in the output — which is the only
  reason it is a footnote and not a fifth inert-pattern instance. **A loop that breaks loudly is not
  the same defect as one that returns silence.**
- Both unranked files are copies of `iTEST02_2026-06-14`, an **earlier** snapshot than the one tested.

**`D-3b` is amended a third time.** The authorisation must now require: **(1)** the client version be
stated; **(2)** every generation be opened; **(3)** **the population be ranked before selection**.
Condition (3) is the one that binds — a reader could satisfy (1) and (2) and still build a runtime
section on a 23-line database, which is exactly what happened to a peer.

**Intake note for the Boss and for `P01`–`P10`.** If peer packages have collectively treated database
evidence as unavailable, that is a **capability claim across the programme**, and it is testable per
artefact. **P11 asserts nothing about what any other package did** — `P04` declined to, having twice
asserted a third package's behaviour unverified, and P11 committed the same error at `P11-E-20`.

> **The cheapest column is also the most leveraged.** Four queries and three declarations —
> **hours of mechanical work, no new research** — would close or re-scope `Q-01`, `Q-02`, `Q-04`,
> `MCU-21`, `MCU-18`, `MCU-19b`, `GB-07`, `P11-B-04`, `P11-B-08`, and bound every class `A` negative
> claim in the programme. **None of it is blocked on `P01`–`P10`.**
