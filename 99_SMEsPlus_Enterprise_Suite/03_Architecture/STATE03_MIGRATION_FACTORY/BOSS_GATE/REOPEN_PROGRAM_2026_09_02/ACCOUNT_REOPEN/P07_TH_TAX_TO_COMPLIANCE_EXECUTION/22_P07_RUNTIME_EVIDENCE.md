# P07 — RUNTIME EVIDENCE, AND THE INCAPACITY CLAIM THAT CONCEALED IT

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-05`

## 1. Why This File Exists

Every behavioural statement in files `00`–`21` is source-derived, bounded by `U-02`
(*no database was queried*) and by `13 §7`. At `r8` that entry was re-marked `ASSUMED`
rather than `TESTED`, after a peer registered having asserted an incapacity it had never
checked.

It was then **tested, and it was false.**

## 2. The Error, Recorded First — `REV-E-24`

A PostgreSQL dump sits **inside this session's own declared PATH SET**:

    ACCOUNT/01 ACCOUNT/SOURCE CODE/iTEST02_2026-06-14_14-41-19.dump    65,444,053 bytes

`13 §2` declares that directory as one of the three roots of the research universe. The
session listed that directory **in its first minutes of execution**, and the dump appears in
that listing. It was read past, and `U-02` was published over the top of it.

This is worse than the peer instance that prompted the check, in two respects:

1. The peer's dumps were elsewhere on the host. **This one was inside the declared scope**,
   in a directory whose enumeration is the evidentiary basis of `EC-01`.
2. It was **printed by a tool this session ran and read**. That is the `§2.1a` mechanism of
   the method proposal — *tool output plus a plausible reason not to open the source* — with
   the plausible reason being that the session was looking for modules, and a `.dump` is not
   a module.

The first attempt to read it also failed in a way worth recording: the host's default
`pg_restore` is 16.15 and the archive is format v1.16, which reports
`unsupported version (1.16) in file header`. **Stopping there would have produced a
`TESTED` incapacity that was still false** — a newer client is present on the same host
(`postgresql@18`) and reads it. A capability test that stops at the first failing tool is
not a capability test.

## 3. Scope of This Evidence — Declared Before Any Result

| Attribute | Value |
|---|---|
| Database | `iTEST02`, archive created `2026-06-14 14:41:20 +07` |
| Generation | `ir_module_module` carries `19.0.1.0` — **the same v19 generation as the declared source set** (`13 §2`) |
| Tool | `postgresql@18` `pg_restore 18.6`, table-at-a-time extraction; **no server, no restore, read-only**. Per-artefact readability is stamped at §3.1 — this is a **reproduction caveat, not a footnote**. |
| Population | Small: 6 `account_move`, 23 `account_move_line`, 586 `account_account`, 19 `account_tax` |
| Relationship to other evidence | **Not** the database named in any runtime capture referenced elsewhere in the programme |

**What this scope supports and does not support.** Findings about *configuration and schema*
— what the chart, the taxes, the groups and the return types actually contain — are
well-supported: those tables are fully populated. Findings about *transaction volume* are
not: six moves is a configuration snapshot, not an operational one. Every result below is
labelled accordingly.

### 3.1 Per-Artefact Readability — and a Correlation That Defeats Naive Reproduction

Contributed by P04: *readability is per artefact; the unit is the (artefact, tool) pair, and
a negative result binds only the tool used.* Applied here, it produces something sharper than
a caveat.

| Database | Archive | Stock client `pg_restore 16.15` | `postgresql@18` | Does `P07-F-01` fire? |
|---|---|---|---|---|
| `iTEST02` 2026-06-14 | **v1.16** | **FAILS** | reads | **YES** — registers empty |
| `iTEST02` 2026-07-14 | **v1.16** | **FAILS** | reads | **YES** — registers empty |
| `iSMEs` 2026-07-11 | v1.14 | READS | reads | no |
| `BK12MAY26` 2026-08-03 | v1.14 | READS | reads | no |
| `iEVING` 2026-07-23 | v1.14 | READS | reads | **no** — examined at `§10`, see below |
| `iEVING` 2026-03-30 | zip/`dump.sql` | n/a | n/a | **no** — examined at `§10` |
| `BK12MAY26` 2026-08-03 (2nd) | zip/`dump.sql` | n/a | n/a | **no** — examined at `§10` |

> **This row was wrong twice, and the second way is worse — `REV-E-43`.** As published it
> was one column short, and its excluded-reason read *"not examined — **different product
> line**"*. That reason was never verified against `ir_module_module`; it is false —
> `iEVING` is `19.0.1.3`, the declared generation. So `§10` was not an oversight being
> corrected. **The identity was excluded from the population by an unverified assertion
> written into the evidence table**, which is a stronger defect than forgetting it: a reader
> auditing the population would have found a stated reason and stopped. A negative about
> the evidence base needs the same authority as a negative about the subject.

**The correlation is exactly inverse to the convenient one.** Both databases in which the
defect fires are `v1.16` and **cannot be opened by the host's default client**. Both in which
it does not fire are `v1.14` and open with stock tooling.

So a reader attempting to reproduce `P07-F-01` with default tooling **can only open the two
databases in which the defect is absent**, would observe functioning registers, and would
reasonably conclude the finding is wrong. Reproduction requires `postgresql@18`, and its
absence produces a confident false negative rather than an error.

That is not a caveat about completeness. It is a caveat about a **specific wrong conclusion**
a competent reader would reach, and it is recorded first because it governs how everything
below should be checked.

## 4. Results

### 4.1 `P07-F-01` — VERIFIED. It was the package's headline inference; it is now fact.

The predicate at `smesplus_account_reports/models/account_generic_tax_report.py:88` admits a
row only if the tax group's raw stored name equals `{'en_US': 'VAT 7%'}`. The deployed value
is:

    id 5 | {"en_US": "VAT 7%", "th_TH": "ภาษีมูลค่าเพิ่ม 7%"}

A two-key mapping. The equality is **false for every row**, so in this database both SMEsPlus
statutory VAT registers return **no data at all**, silently.

This was reached independently by two adversarial reviewers as a source-derived escalation
and carried at `SRC-CHAL`. It is **verified** against this database.

**CONSTRAINED at §7 — the first issue of this paragraph over-generalised from one database.**
It said the condition "is not exceptional, it is the shipped state of a Thai deployment".
That was an inference from `n = 1`. Across four snapshots the condition holds in two — and per
§7.4 those two are **one database identity observed a month apart**, so the base is **1 of 3
identities examined**, not 2 of 4. See §7.1 and §7.4.

### 4.2 `P07-F-42` — VERIFIED. `P07-U-20` is CLOSED.

Held at `INF` — a complete seven-step chain with one unexecuted link (record-creation order
at template load) — and deliberately not upgraded on two reviewers' agreement. The database
settles it:

| Tax (`en_US`) | Rate | Use | `tax_group_id` | Group |
|---|---|---|---|---|
| `Input VAT 0%` | 0.0000 | purchase | **1** | `WHT 1%` |
| `Output VAT 0%` | 0.0000 | purchase | **1** | `WHT 1%` |
| `0% EXEMPT` | 0.0000 | sale | **1** | `WHT 1%` |
| `V0% EXP` | 0.0000 | purchase | **1** | `WHT 1%` |
| `7%` | 7.0000 | sale | 5 | `VAT 7%` |

Group 1 carries `tax_payable_account_id = 64`, `tax_receivable_account_id = 19`. Group 5
carries `63` / `18`. **Zero-rated and exempt VAT therefore settle against the withholding
control accounts, not the VAT ones**, in a deployed database. The inference was correct and
the class moves from `INF` to verified.

**STRENGTHENED at §7.2**: the same assignment holds in **every database examined** — four of
four, across six independent company tax-group sets.

### 4.3 `P07-F-40` and `P07-F-37` — VERIFIED

- `res_company.account_return_periodicity = 'monthly'`. The statutory monthly VAT period is
  correct **by platform default**, exactly as the finding stated — not by any Thai assertion.
- `account_return_type` holds three rows. The Thai one,
  `{"en_US": "Tax", "th_TH": "ภาษี"}`, has `deadline_periodicity = NULL`. The other two —
  `Annual Closing: Corporate Tax` and `Audit` — both carry `{"1": "year"}`.

So the localisation's own return type is the one with no periodicity configured, while
return types created in the same database do carry one. `P07-F-37`'s provisioning gap is
confirmed and is not an artefact of the framework being unused.

### 4.4 `P07-F-03` — CONFIRMED, with its population declared

| Field | Populated |
|---|---|
| `account_move.tax_period` | **1 of 6** moves |
| `account_move_line.tax_period_date` | **0 of 23** lines |

There are 2 genuine tax lines in the database. The header field is in use by an operator; the
line-level field is populated **nowhere**, including on the one move whose header carries a
value. That is exactly the mechanism the finding describes — written only in `create()`, with
no `write()` override — now observed. Bounded to this database's 23 lines.

### 4.5 `P07-F-51` — SPLIT into its two claims, and both are stronger for it

The finding as published asserted **two different kinds of claim in one sentence** and never
said which evidence supported which — the shape P04 identified in its own `F-81`. Split, with
each half on the right kind of evidence:

| Half | Kind | Claim | Evidence | Status |
|---|---|---|---|---|
| `a` | **configuration** | The Thai chart template has **no `wt_account` column**, and nothing in the shipped set flags an account. Without a flagged account the withholding-account domain is empty, the certificate wizard's required field has an empty domain, and enabling withholding on any shipped tax raises. | source: `account.account-th.csv` header; `l10n_th_withholding_tax/models/account.py:78-81` | **holds, unchanged** |
| `b` | **population** | Operators supply the flag. | runtime, 3 of 3 identities examined — **2 of 2 in-generation** (`iTEST02` 3 of 586, `BK12MAY26` 2 of 544) plus `iSMEs` 1 of 339 as **v16 corroboration** (§9) | **holds, and is new** |

The published version rested half `b` on a **single** database — and on `iTEST02`, the
*configuration* database, which is the wrong kind for a population claim (`§8.3`). Re-run
across identities it does not merely survive; it **strengthens half `a`**:

> Every deployment examined performed a provisioning step the localisation does not perform.
> Three independent deployments, three independent operators, the same manual repair.

That is a materially better statement than *"this deployment provisioned it"*, and it was
unavailable while the two halves shared one sentence. `REV-E-34`.

The correction from the first issue stands: **"inert as shipped" is correct; "cannot work" is
withdrawn** and was never stated, only readable.

**And the split concealed a finding, not just a distinction — `P07-F-63`.** P04 reported the
same effect on splitting its own compound claim, and the shape holds here. Half `b` at full
strength is not *"operators supply the flag"*. It is:

> **Every deployment examined independently discovered and performed an undocumented
> provisioning step that the localisation never performs — and each arrived at a different
> answer.** Three identities, three operators, three counts: 3 of 586, 1 of 339, 2 of 544.
> In-generation alone it is two operators and two different answers.

So the flag is not an optional refinement: it is a **de facto requirement the shipped
localisation omits**, and because it is omitted there is no guidance on *which* accounts
qualify — producing divergent configurations of a field that gates the entire withholding
path (`half a`). That statement was unavailable while the halves shared a sentence, because
the configuration half read as a property of the chart rather than as a **consistent
independent action by every operator**.

**A compound claim does not merely under-describe its evidence; it can conceal the
finding.** P04's formulation, and this is the second instance of it in two packages.

### 4.6 Two New Findings from the Data

| ID | Finding | Evidence |
|---|---|---|
| `P07-F-60` | **Withholding is configured and no statutory certificate has ever been issued.** `account_withholding_tax` = 10 rows, `wt_account` accounts = 3, and `withholding_tax_cert` = **0 rows**. The s.50 bis certificate is due *immediately on every withholding* (`S-31`). Configuration-scope observation: it shows the certificate model is installed and unused, not how many withholdings occurred. | `withholding_tax_cert`, `account_withholding_tax` |
| `P07-F-61` | **The cross-company tax-unit mechanism is unused.** `account_tax_unit` = **0 rows**, while the SMEsPlus VAT reports declare `filter_multi_company = tax_units`. So `P07-F-39`'s unbounded-company-search exposure is **latent in this deployment**, not active. Scoping for `P07-U-14`, which remains open. | `account_tax_unit` |

## 5. What Changes in the Package

| Finding | Was | Now |
|---|---|---|
| `P07-F-01` | `SRC-CHAL` | **verified against a deployed database** |
| `P07-F-42` | `INF`, `P07-U-20` open | **verified**, `P07-U-20` **CLOSED** |
| `P07-F-40`, `P07-F-37` | `SRC` / `MEAS` | **verified** |
| `P07-F-03` | `SRC-CHAL` | **confirmed**, population declared |
| `P07-F-51` | `SRC-CHAL` | **refined**; "inert as shipped" stands, "cannot work" withdrawn |
| `P07-F-39` | `SRC` | scoped: latent in this deployment |
| `U-02` | "no database was queried" | **superseded by this file** for the tables listed in §3 |
| `P07-U-20` | open | **CLOSED** |

**No finding was withdrawn and none was weakened except `P07-F-51`, which is now more
precise.** Two were upgraded from inference to fact — and both were the two that independent
challenge had escalated and that this session had refused to upgrade without runtime
evidence. Holding them at `INF` and `SRC-CHAL` was correct; so was going and getting the
evidence.

## 6. What Is Still Not Done

- ~~The other three dumps on this host were not examined.~~ **Miscounted, and since
  corrected — see §7 and §7.4.** There are **five snapshots of four database identities across
  nine files**; four snapshots covering three identities have now been examined. `P07-U-27` is narrowed to the one remaining (`iEVING`, a different
  product line). **Both figures and the reason are superseded at `§10`: 7 snapshots, 5
  identities, and `iEVING` is `19.0.1.3` — in-generation, not a different product line.
  `P07-U-27` CLOSED, all opened.**
- No transaction-scale evidence exists for any finding. Six moves cannot support a claim
  about operational behaviour, and none is made.
- The database was read table-at-a-time with no restore, so no join was executed by a server;
  every cross-table statement above was assembled by reading two extracts. That is weaker
  than a query and is declared as such.

## 7. Four Snapshots, Three Identities — One Finding Constrained, One Strengthened

Written after P04 reported that its own dump enumeration had been bounded to a single
directory, which prompted P07 to test its own bound. Two defects surfaced, one of them in the
§6 text above.

### 7.0 The enumeration defects

| # | Defect | Correction |
|---|---|---|
| `a` | §6 stated *"the other three dumps"* — a self-describing count that was **never executed**, the exact class this session has documented six times. | Enumerated by magic bytes (`PGDMP`) over both roots, any extension, any depth: **nine files holding five snapshots of four database identities** — and see §7.4, where the *unit* of that count was itself wrong — `iTEST02` (five identical copies of the 2026-06-14 snapshot, one of them inside the declared PATH SET), `iTEST02` at 2026-07-14, `iSMEs` at 2026-07-11 (155 MB, the largest), `BK12MAY26` at 2026-08-03 (the most recent), `iEVING` at 2026-07-23. |
| `b` | P07's original search was bounded: `-maxdepth 6`, `-size +1M`, four extensions. | Re-run unbounded returns 3,613 hits — but the excess is Odoo source `.sql` fixtures, so the size filter was **doing real work** and this bound, unlike the count, survives its own test. Recorded because a bound that survives should be published alongside one that does not. |

### 7.1 `P07-F-01` is DEPLOYMENT-DEPENDENT, not universal — a correction against this session

| Database | Stored `VAT 7%` group name | Predicate `== {'en_US': 'VAT 7%'}` | Statutory VAT registers |
|---|---|---|---|
| `iTEST02` 2026-06-14 | `{"en_US": "VAT 7%", "th_TH": "ภาษีมูลค่าเพิ่ม 7%"}` | **false** | **return no rows** |
| `iTEST02` 2026-07-14 | `{"en_US": "VAT 7%", "th_TH": "ภาษีมูลค่าเพิ่ม 7%"}` | **false** | **return no rows** |
| `iSMEs` 2026-07-11 | `{"en_US": "VAT 7%"}` | true | function |
| `BK12MAY26` 2026-08-03 | `{"en_US": "VAT 7%"}` | true | function |

**Two of four.** The claim that the failing condition is "the shipped state of a Thai
deployment" is withdrawn: it is the state of *some* deployments and not others, and nothing
distinguishes them to a user.

This makes the finding **more** dangerous to rely on, not less, and the reason is worth
stating plainly: a defect that fires in half of deployments and is silent in the other half
is one that **cannot be found by testing a system that works**. Two of these databases would
pass any smoke test of the statutory register; two would return an empty report that looks
like a quiet month. Severity `S1` is unchanged.

Also visible: `iSMEs` names its withholding groups `TAX 1%`…`TAX 5%` rather than `WHT n%`,
so the tag- and name-based classifications in `P07-F-15` face the same variability.

**Read this table together with §3.1.** The two *snapshots* where the defect fires — both of
the **same deployment**, a month apart (§7.4) — are the two a stock client cannot open.
Anyone testing this finding with default tooling sees only the deployments where it does not
fire.

### 7.2 `P07-F-42` holds in EVERY identity examined

| Database | Zero-rated / exempt taxes | Group they land in |
|---|---|---|
| `iTEST02` 2026-06-14 | 4 | group 1 = `WHT 1%` |
| `iTEST02` 2026-07-14 | 4 | group 1 = `WHT 1%` |
| `iSMEs` 2026-07-11 | 4 | group 1 = `Taxes` / `ภาษี` — not a VAT group either |
| `BK12MAY26` 2026-08-03 | 12, across **three companies** | groups 1, 6 and 11 — **each company's own `WHT 1%`** |

**Four of four snapshots, three of three database identities, six independent company
tax-group sets, no exception** (unit per §7.4). The
`BK12MAY26` case is the strongest: three separate companies were configured independently
and the misassignment reproduced in each, which is what a deterministic
lowest-id-wins fallback predicts and coincidence does not.

`P07-F-42` is now the most robustly evidenced finding in this package — better evidenced
than `P07-F-01`, which was the headline. That inversion was produced entirely by checking a
second database.

### 7.3 What this changes

| | Before §7 | After §7 |
|---|---|---|
| `P07-F-01` | verified, asserted universal | verified, **1 of 2 in-generation identities** (§9; 1 of 3 examined, 2 of 4 snapshots both the same identity — §7.4); universality claim withdrawn |
| `P07-F-42` | verified in 1 snapshot | verified in **2 of 2 in-generation identities** (§9), 4 of 4 snapshots, 6 company sets, plus v16 corroboration |
| `P07-F-15` | source-derived | supported: group naming varies between deployments (`TAX n%` vs `WHT n%`) |
| §6 count | "three dumps" | five snapshots of four identities in nine files; four snapshots covering three identities examined |
| `P07-U-27` | four unexamined | one unexamined (`iEVING`, different product line) — **both the count and the reason superseded at `§10`; `iEVING` is in-generation and is two identities, all now opened. CLOSED.** |

Neither correction was found by re-reading. Both came from a peer reporting a bounded
enumeration of its own and P07 testing the same bound.

## 7.4 The Unit of §7 Was Wrong — `REV-E-28`

P04 re-ran its own dump enumeration on this session's method, found its bound survived but its
**unit** did not, and restated *"four v18-line databases"* as *"four v18-line snapshots across
three identities"*. The same conflation is in §7 above, in the evidence base of this package's
headline finding, and it was found by running P04's correction against this file.

### Executed breakdown

    FILES (magic byte, any extension, any depth) : 9
    SNAPSHOTS (identity + date)                  : 5
        iTEST02   2026-06-14   (5 identical copies)
        iTEST02   2026-07-14
        iSMEs     2026-07-11
        BK12MAY26 2026-08-03
        iEVING    2026-07-23   (unexamined)
    DATABASE IDENTITIES                          : 4

**§7.0 said "five distinct databases". There are five *snapshots* and four *identities*.**
Examined: four snapshots across **three** identities.

### What this does to `P07-F-01` — it weakens its base

§7.1 reported **"two of four"**. Both of those two are `iTEST02` — **the same database at two
dates**. Restated with the unit declared:

| Unit | Fires | Does not fire |
|---|---|---|
| Snapshots examined | 2 of 4 | 2 of 4 |
| **Database identities examined** | **1 of 3** (`iTEST02`) | 2 of 3 (`iSMEs`, `BK12MAY26`) |
| **In-generation identities only** (§9) | **1 of 2** (`iTEST02`) | 1 of 2 (`BK12MAY26`) — `iSMEs` is v16 and out of scope for a v19 predicate |

So the defect is observed in **one deployment**, not two. The second observation is the same
deployment a month later, which is worth something it was not credited for — it establishes
**persistence**: the condition was present on 14 June and still present on 14 July, so it is
not a transient of one backup. But it is one identity, and "2 of 4" implied two.

`P07-F-01` remains `S1`, for the reason at §7.1 that a defect firing in some deployments and
silent in others cannot be found by testing one that works. Its **evidence base is one
identity observed twice**, and that is now what the file says.

### What this does to `P07-F-42` — it survives, and the inversion sharpens

| Unit | Result |
|---|---|
| Snapshots examined | **4 of 4** |
| **Database identities examined** | **3 of 3** — of which **2 of 2 in-generation**, `iSMEs` being v16 corroboration (§9) |
| Independent company tax-group sets | **6 of 6** |

Every identity, every snapshot, every company set. The restatement costs `P07-F-42` nothing.

**The inversion is therefore larger than §7.2 claimed.** The finding held longest at
inference and upgraded most reluctantly rests on **three database identities and six company
sets**; the headline rests on **one identity observed twice**. The gap between the two is
wider under the corrected unit than under the wrong one — which is the opposite of what a
convenient error would have produced.

### The correction did not propagate — `REV-E-31`

P04 reported its own unit restatement recurring in three sibling locations **within one commit
of naming it**, and gave the operational rule: *the only step that catches it is a grep for the
corrected phrase across the package, not a re-read.*

Run here, with a positive control. **Four survivors, all in this file** — §4.1, §6, §7.2 and
§7.3 were still asserting "four databases" and "2 of 4 deployments" while §7.4, in the same
document, corrected them. Worse than P04's in one respect: their stragglers were in sibling
files; mine were in the **same file as the correction**.

That is the fourth instance of this class here and the second of *corrected-in-one-place-only*.
Naming a defect does not immunise a package against it, and re-reading does not catch it —
only the grep does. Corrections in this package now end with a package-wide grep for the
superseded phrase.

### The propagation check was itself pattern-bounded — `REV-E-33`

P04 re-ran its own sweep and found the remedy carrying the defect one level up: its grep
searched an **enumerated list of phrases**, and two survivors used different wording — *"the
three databases named"*, *"the five databases named"* — one of them the class line of the
corrected finding's own sibling. **The fix for an enumeration defect was itself
pattern-bounded.**

The same was true here. `REV-E-31`'s sweep searched six literal strings. Re-run with a broad
pattern — any numeral or number-word within forty characters of
`database|deployment|snapshot|identit`, with a control on the sweep itself — it returned
**five more**, including:

- the **section heading** *"## 7. Four Databases, Not One"* — the most-read line in the
  section it corrects;
- a sentence that had become **factually wrong** after §7.4: *"the two deployments where the
  defect fires"*, when §7.4 had established they are **one deployment observed twice**;
- the §7.3 summary table, in two cells.

So the corrected step is not *grep after correcting*. It is **grep with a broad pattern and a
positive control on the sweep**, because an enumerated phrase list is bounded in exactly the
way the count it is fixing was. Third round of this class here; the first two were found by a
peer sending the method, and so was this.

### Method note

Both bounds of this session's own enumeration were tested, per the practice of publishing a
surviving bound beside a failing one:

- the **magic-byte selector** survives — it is what distinguishes 9 real archives from 3,613
  extension matches;
- the **unit** failed, twice: once as an uncounted total (`REV-E-27`), once as
  snapshots-counted-as-identities (this entry).

Neither was found by re-reading. Both came from a peer running a correction against its own
package first and sending the method rather than the conclusion.

## 8. The Database-Derived Negatives, Tested Across Identities — One REFUTED

P11 generalised the tooling caveat into a rule that reaches back into this file:

> Every negative claim resting on database evidence must state the **client version used** and
> the **generations actually opened**. A class `A` verified absence from default tooling over
> one generation is bounded to that generation — and the boundary is **invisible**, because
> the tool failed silently on the others.

§4.6 published two negatives and §4.4 a third, all from **one snapshot** — `iTEST02`
2026-06-14, a 6-move configuration database — and none stated its bounds. Tested across all
four examined snapshots:

| Claim | `iTEST02` 06-14 | `iTEST02` 07-14 | `iSMEs` 07-11 | `BK12MAY26` 08-03 | Verdict |
|---|---|---|---|---|---|
| `withholding_tax_cert` rows | 0 | 0 | **5,201** | 1 | **`P07-F-60` REFUTED** |
| `account_tax_unit` rows | 0 | 0 | 0 | 0 | **`P07-F-61` HOLDS** — 2 of 2 in-generation, plus v16 (§9) |
| lines carrying `tax_period_date` | 0 of 23 | 0 of 32 | **18,197 of 447,384** | 0 of 563 | **`P07-F-03` CONSTRAINED** |

### 8.1 `P07-F-60` is REFUTED — `REV-E-29`

It read: *withholding is configured and **no statutory certificate has ever been issued**.*
`iSMEs` — a **v16** deployment (§9) — holds **5,201** certificates, and `BK12MAY26`, which is
in-generation, holds one. So the negative fails in-generation on a single certificate and
fails decisively out of generation. **Withdrawn.**

What replaces it is more useful than the negative was. A population of 5,201 certificates is
passing through the model this package identified as holding *the most statutorily faithful
classification in the declared set* — a 15-value s.40 income-type taxonomy — while the PND
export ignores that field and derives income type from the tax rate instead (`W-K-01`,
`W-K-04`). The divergence is not theoretical: there is a real, sizeable population on the
correct side of it. **`P07-F-62`**, and it strengthens `W-K-04` rather than weakening it.

### 8.2 `P07-F-03` is CONSTRAINED, and the constraint supports its mechanism

The empirical gloss *"populated nowhere"* was `iTEST02` only. `iSMEs` populates the
line-level field on **18,197 of 447,384** lines — 4.1%.

The **source finding is unchanged**: written only in `create()`, no `write()` override, and no
report, compute, domain or SQL reads it. And the observed 4.1% is *consistent with* that
mechanism rather than against it — a create-only write populates the field precisely when tax
lines already exist at create time, which is a minority of paths. The number supports the
finding; the sentence that said "nowhere" did not survive.

### 8.3 The scoping error underneath — restated, because the first statement of it was too broad

The first issue of this section said this session *"built its entire runtime section on the
smallest database available"* and that *"convenience of location determined the evidence
base"*. Ranked properly, that is **too broad**, and P11's own rule applies to it — *an
over-broad self-blame is still an inaccurate record*.

**The ranking inverts depending on its unit**, which is the same defect this file has now
recorded four times, one level up:

| Database | Bytes | Tables **with data** | `account_move_line` rows |
|---|---|---|---|
| `iSMEs` 2026-07-11 | **155,443,710** | 651 | **447,384** |
| `iTEST02` 2026-06-14 | 65,444,053 | **1,395** | 23 |
| `iTEST02` 2026-07-14 | 64,303,340 | 1,315 | 32 |
| `BK12MAY26` 2026-08-03 | 35,679,594 | 881 | 563 |
| `iEVING` 2026-07-23 | 24,911,161 | 875 | not examined |

`iSMEs` is 2.4× the largest by bytes and by rows. `iTEST02` has **more than twice as many
populated tables** — it is the **broadest module install**, and `iSMEs` is the **deepest data
set**. Neither is simply "bigger", and a ranking that does not say which is being ranked
repeats the unit defect it was introduced to fix.

**So the corrected self-assessment is narrower and more accurate:**

| Claim type | Right database | What this session used | Verdict |
|---|---|---|---|
| Configuration and schema — §4.1–4.5, §7: tax groups, tax templates, return types, the withholding-account flag | `iTEST02` — most populated tables, the broadest install | `iTEST02` | **defensible, arguably optimal** |
| Population and operational negatives — §4.6, §8: certificates issued, lines carrying a field | `iSMEs` — 447,384 rows against 23 | `iTEST02` | **wrong, and it cost `P07-F-60`** |

The error was **not** picking the smallest database. It was **using a configuration database
to support population negatives** — and then not stating which of the two kinds each claim
was. §4's configuration findings stand on the database they were taken from; §4.6's
population negatives never should have been.

`REV-E-30` is restated accordingly and `REV-E-32` records this correction of it. The
corrective stands and gains a clause: **rank the population before choosing, and declare the
unit you ranked by** — because the right database depends on the claim, and this session had
two kinds of claim in one file without saying so.

### 8.4 Net

| Finding | Before §8 | After |
|---|---|---|
| `P07-F-60` | new finding, 1 snapshot | **WITHDRAWN**; replaced by `P07-F-62`, which is stronger |
| `P07-F-61` | 1 snapshot | **holds**; superseded by `§10.3` — present and empty in **7 of 7 snapshots / 5 of 5 identities** |
| `P07-F-03` | "populated nowhere" | source finding unchanged; population claim bounded, and the 4.1% supports the mechanism |
| `P07-F-62` | — | **new**: 5,201 certificates carry a correct income-type taxonomy the statutory export ignores |

Client version for every row above: `postgresql@18` `pg_restore 18.6`. Generations opened:
four snapshots, three identities. Not opened at the time of writing: `iEVING` (`P07-U-27`).
**Superseded — `P07-U-27` is CLOSED at `§10`:** `iEVING` proved to be *two* identities, both
opened, and the population is 7 snapshots / 5 identities. This line is left standing with its
correction attached rather than rewritten, so the record shows what the section claimed when
it was published.

## 9. `iSMEs` Is v16 — a Generation Error That Was Wrong When Written — `REV-E-35`

P04 reported finding a claim in its own **scope** paragraph that was *wrong at the time of
writing*, not merely stale, and noted that a scope block is the one place a reader is entitled
to trust without checking. Applying that test here found the same category, and it is the most
substantive correction in this file.

### 9.1 The check

`§3` declared `iTEST02`'s generation from **one regex hit on one module row**. Re-run properly
over `ir_module_module`, counting installed modules and their major versions:

| Database | Installed modules | `base` version | Major-version spread |
|---|---|---|---|
| `iTEST02` 2026-06-14 | 486 | `19.0.1.3` | `{19: 485}` |
| `BK12MAY26` 2026-08-03 | 251 | `19.0.1.3` | `{19: 251}` |
| **`iSMEs`** 2026-07-11 | 190 | **`16.0.1.3`** | **`{16: 189}`** |

**`iSMEs` is a v16 deployment.** It is not the declared generation, and nothing in `§7` or
`§8` said so.

### 9.2 What was wrong when written

`§7.1` compared the stored `VAT 7%` group name across four snapshots and concluded the
`P07-F-01` predicate is deployment-dependent. **Two of those snapshots are v19 and one is
v16.** The predicate is a v19 code path; a v16 database's tax-group naming is not a valid test
of it. The comparison was invalid at the moment it was made, not invalidated later.

`§8.3` went further and recommended `iSMEs` as *"the reference population for any operational
claim"* in this package, on the strength of its 447,384 accounting lines. **Withdrawn.** It is
the largest dataset on the host and it is the wrong generation; recommending it was the
ranking error in a new form — ranked by depth, never checked for eligibility.

### 9.3 Corrected statements

| Finding | Published | Corrected |
|---|---|---|
| `P07-F-01` | deployment-dependent, 1 identity of 3 | **1 of 2 in-generation identities** (`iTEST02` fires, `BK12MAY26` does not). Sample halves; the finding stands and its base is now honestly two. |
| `P07-F-42` | 3 of 3 identities | **2 of 2 in-generation identities**, plus `iSMEs` as **cross-generation corroboration** — the same misassignment in v16. That is arguably *stronger* for a mechanism claim, since the fallback predates v19, but it is not the same population and is now labelled as corroboration rather than sample. |
| `P07-F-62` (5,201 certificates) | "in one deployment" | **in a v16 deployment.** The statutory divergence it evidences is a v16 observation; whether the v19 line carries the same population is unknown — `BK12MAY26`, the other v19 identity, holds one certificate. |
| `P07-F-51` half `b` | 3 of 3 identities | **2 of 2 in-generation**, plus v16 corroboration. Conclusion unchanged. |
| `P07-F-61` (`account_tax_unit` empty) | 3 of 3 | **2 of 2 in-generation**, plus v16. Unchanged. |

### 9.4 What this does not change

No finding is withdrawn. `P07-F-01` and `P07-F-42` remain verified in the declared
generation — the database inside the declared PATH SET is v19 and is where both were first
observed. What changes is **sample size and the labelling of corroboration**, and one
withdrawn recommendation.

### 9.5 The class

This is the **fifth** distinct unit failure in this file, and the first to be a *generation*
rather than a count: files, snapshots, identities, ranking-unit — and now **eligibility**. A
population can be correctly enumerated, correctly ranked, correctly unit-declared, and still
contain members that do not belong to the question being asked.

`§3`'s generation claim was made from one regex hit and was true of the database it described.
It was never extended to the databases added at `§7`, and the scope block was not revisited
when the population grew. **A scope declared before the first result does not survive the
population changing under it.**

---

## 10. The Population Was Wrong — Two Snapshots and One Identity Missing — `REV-E-38`…`REV-E-42`

P04 reported an **eligibility** failure in its own scope block: a population correctly
enumerated, ranked and unit-declared can still contain — or omit — members that do not belong
to the question, because eligibility is decided *before* the four disciplines run and none of
them looks at membership. P04's version was three deployments labelled `v18-line` that are
`v19`. Their table named `iEVING` as **v19**, an identity this file had recorded as
**unexamined**. That is a member of the eligible population, so the check was run here.

### 10.1 What the re-derivation found

`iEVING` is v19 — `base` = `19.0.1.3`, read from `ir_module_module`, not inferred. P04's
claim verified independently. Two further defects surfaced from re-deriving rather than
patching:

**Snapshots: 5 → 7.** The census was taken by *extension* (`*.dump`). Two database snapshots
are `.zip` archives containing `dump.sql` and were invisible to it. Re-run by **format**
(`file -b`), the population is **7 snapshots** — but the *method* claim in that sentence was
false even though the number was right; see `§10.7`. This is the archive-denominator rule that a
peer process published after making the same error; it was available and not applied here.

**Identities: 4 → 5.** The identity unit was the **filename**. Keyed on `database.uuid` from
`ir_config_parameter`, two artefacts both named `iEVING` are **two different databases**:
`f4a44cce-…` (created 2026-03-18) and `1f6338ae-…` (created 2026-03-30). They are not two
snapshots of one system — they hold 237 and 544 accounts. **A database name is not a database
identity.** Conversely `BK12MAY26`'s two artefacts share one uuid and are one identity.

### 10.2 Corrected population

| Identity (by `database.uuid`) | Snapshots | `base` | Generation |
|---|---:|---|---|
| `a1430edc-…` | 2 | `19.0.1.3` | in-generation |
| `f4a44cce-…` | 1 | `19.0.1.3` | in-generation |
| `1f6338ae-…` | 1 | `19.0.1.3` | in-generation |
| `66d1b52a-…` | 2 | `19.0.1.3` | in-generation |
| `45a8e08e-…` | 1 | `16.0.1.3` | **out of generation** |

**7 snapshots, 5 identities, 4 of them in-generation.** — **SUPERSEDED AND A LOWER BOUND at
`§12`: ≥ 8 snapshots / 6 identities.** This census was drawn over two directories that were
chosen and never declared as a path set; a sixth identity, in a third generation, sits outside
them. Left standing with its correction attached rather than rewritten, because a census that
has not finished is not a number. Every denominator in §7–§9 was written
over 2 in-generation identities. The eligible number was 4.

### 10.3 Every runtime finding re-derived at the corrected population

| | `a1430edc` | `f4a44cce` | `1f6338ae` | `66d1b52a` | `45a8e08e` (v16) |
|---|---|---|---|---|---|
| VAT-group name carries `th_TH` (`F-01`) | **yes** | no | no | no | no |
| zero-rate taxes | 4 | 4 | 12 | 12 | 4 |
| …all landing in a **non-VAT** group (`F-42`) | **yes** | **yes** | **yes** (3 sets) | **yes** (3 sets) | **yes** |
| `account_tax_unit` rows (`F-61`) | 0 | 0 | 0 | 0 | 0 |
| accounts / flagged (`F-63`) | 586 / **3** | 237 / **0** | 544 / **2** | 544 / **2** | 339 / **1** |
| withholding certificates (`F-62`) | 0 | 0 | 0 | 1 | 5,201 |
| companies | 1 | 1 | 44 | 44 | 1 |

### 10.4 What this changes, finding by finding

**`P07-F-01` is weakened again — `REV-E-40`.** Published as firing in **1 of 2** in-generation
identities. At the corrected population it fires in **1 of 4**. The severity argument is
untouched and is the reason the finding stands: a defect silent in three deployments out of
four cannot be found by testing a system that works. But the prevalence figure was wrong, and
wrong in the direction that flattered the headline.

**`P07-F-42` is strengthened — `REV-E-41`.** Published as 2 of 2 in-generation identities. It
now holds in **4 of 4 in-generation identities, 8 of 8 in-generation company sets**
(enumerated at `§10.7`; 9 including the v16 identity). It is the best-evidenced finding in the package by a wider margin than before, and
it is still the one held longest at `INF`. Two successive population corrections have both
widened the gap between it and the headline — which is not what a convenient error does.

**`P07-F-63` is PARTLY REFUTED, ninety minutes after publication — `REV-E-39`.** It was
published this session as *"3 of 3 identities independently performed it"*. The fourth
in-generation identity, `f4a44cce`, has **237 accounts and zero flagged** — the step was not
performed there at all. The claim of universality is withdrawn.

What survives is stronger for being narrower. `f4a44cce` holds **0 move lines**: it is a fresh
deployment. So the corrected statement is:

> A freshly installed v19 identity has **zero** withholding accounts flagged — direct
> confirmation that the localisation never provisions the field. Every identity that went on
> to transact flagged some, **and no two that did so agree**: 3 of 586, 2 of 544, 1 of 339.

The refutation and the confirmation come from the same row. The universality claim was
unsupported; the *never-provisioned* claim now has a positive control it did not have before —
an unconfigured deployment showing the zero state the localisation actually ships.

**`P07-F-61` — the test could not previously tell empty from absent.** `0 rows` was being read
off a filter that returns `0` for a table that does not exist. Re-run against the archive TOC,
`account_tax_unit` is **present in all 7 snapshots and empty in all 7**. Same conclusion, but
until now it rested on a control that could not detect its own failure.

**`P07-F-62` — unchanged in substance, sharper in scope.** 5,201 certificates sit in the v16
identity; across the 4 in-generation identities the total is **one**.

### 10.5 A filter that could not fire — `REV-E-42`

The first `F-42` pass on `f4a44cce`/`1f6338ae` reported **0 zero-rate taxes**. The filter
matched the literal strings `0`, `0.0`, `0.000000`; the stored format is `0.0000`. There were
12. The error was caught by a positive control printing the value distribution, not by
inspection — and the false negative would have been published as *"the F-42 population does
not exist in this deployment"*, i.e. as evidence **against** the best-evidenced finding in the
package. A numeric comparison (`$a+0==0`) replaces it throughout.

### 10.6 The class

P04's statement, confirmed on a second package:

> The four disciplines all operate on a set already assumed eligible. None of them looks at
> membership.

And the mechanism in both cases is the same one: **a scope declared before the first result
does not survive the population changing under it.** This file's population was fixed when
three dumps had been read. It was never re-derived at seven — and `iEVING` sat in the same
directory as three of the dumps that were read, for the whole session.

The asymmetry is worth recording: P04's eligibility error **included** ineligible members;
this one **excluded** an eligible member. Inclusion errors are visible in the evidence — a
wrong row is there to be checked. Exclusion errors are invisible by construction: nothing in
the package pointed at `iEVING`, and no control here would have. It took a peer publishing a
version table that named it. `REV-E-38`.


---

## 10.7 Two of `§10`'s Own Claims Were Wrong — `REV-E-46`, `REV-E-47`

P04's rule, adopted: **a total that survives a correction to its own unit has not been
confirmed by surviving; it has only failed to move. Check composition, never the sum.**
Applied to `§10`'s own output it found one total that did not survive and one method claim
that was false.

### `10 of 10 company sets` was never counted — `REV-E-46`

`P07-F-42`'s company-set figure was carried from `6 of 6` to `10 of 10` by a **regex
substitution across the register**, in the same commit that corrected four other denominators.
It was never enumerated. Enumerated now, per identity, as distinct `company_id` holding at
least one zero-rate tax:

| identity | company sets |
|---|---:|
| `a1430edc` | 1 |
| `f4a44cce` | 1 |
| `1f6338ae` | 3 |
| `66d1b52a` | 3 |
| **in-generation total** | **8** |
| `45a8e08e` (v16) | 1 |
| grand total | 9 |

**The correct figure is 8 of 8 in-generation, not 10 of 10.** The finding is unaffected —
every set in which the population exists still resolves to a non-VAT group — but the number
supporting it was asserted. This is the defect the package has a written rule against,
committed **while correcting other people's denominators**.

### The census claim was false even though the count was right — `REV-E-47`

`§10.1` published the snapshot census as re-run **"by format (`file -b`)"**. It was not. The
input list was an **extension glob** (`*.dump`, `*.zip`); `file` was then run on the files that
glob had already selected, and its output reported. **Selecting by extension and reporting the
format is not censusing by format.**

Re-run properly — walking `~/Downloads` and `/Volumes/iMacSys` with no extension filter,
testing content: `PGDMP` signature, ZIP central directory containing `dump.sql`, and the gzip
class inspected rather than assumed (tested for `dump.sql` / `*.dump` members: none; they are
source distributions) —

**11 artefacts · 7 snapshots · 5 identities.** Snapshot and identity counts unchanged, so
nothing downstream moves. The *method* statement was wrong, and P04's mirror failure shows why
that matters independently of the number: their census **was** content-based, matching the
`PGDMP` signature — and missed both `.zip`-borne dumps, because **an enumeration by magic bytes
is only as complete as the set of signatures it enumerates.** "By format, not extension" is not
one check; it is *one check per format*. Signature set declared: `PGDMP`, ZIP-containing-
`dump.sql`, gzip-inspected-and-excluded.

The artefact count differs from P04's 10: this sweep finds an eleventh copy of the `a1430edc`
06-14 snapshot at a path outside the accounting tree. Copies, not snapshots — the identity map
is unchanged, and it is reported so their file census can be reconciled.

### Adopted: `manifest.json` carries the generation directly

Verified in both `.zip` artefacts: `version_info [19, 0, 0, 'final', 0, 'e']`, `version
19.0+e`, `db_name` stated. A **direct** generation signal, better than the `ir_module_module`
reading used at `§10.1` because it requires no inference from a module row. Both agree here.
Preferred wherever a `manifest.json` exists.

### The uncomfortable half, which P04 stated first

P04 records that a memory of its own already named both of its failure points and was not
consulted before publishing. The same is true here, and worse, because these are two rules
this package carries **in its own text**: the archive-census rule and the totals rule. Both
were written down. Both were broken in the commit that corrected other people's denominators.
**Having the rule, recalling the rule, and running the rule are three different things**, and
only the third is a control.


---

## 11. An Excluded Root Supplies the Modules Every Deployment Runs — `P07-F-64`, `P07-F-65`

P04 ran this package's `REV-E-44` rule against its own exclusions — *an exclusion furnished
with a stated reason stops the audit that would have checked it* — found its own exclusion was
**true**, and registered it as a finding anyway, on the ground that **the class is about
authority, not outcome**. Run here against `13 §2.1`, the same audit does not come back true.

### 11.1 The exclusion

`13 §2.1` excludes `ODOO/ODOO-COMMUNITY/ODOO19/efaplus-custom/*` (59 manifests) with the stated
reason **"Different products. Out of scope."** That reason was never tested against anything.

### 11.2 What the runtime evidence says

Every in-generation database in this package's population carries table owner role **`efaplus`**
— the same token as the excluded root. Suggestive only, so the decisive test is module
membership: intersect each database's **installed** module set with the excluded root's
contents.

| identity | installed modules | also present in the excluded root |
|---|---:|---:|
| `a1430edc` | 486 | **35** |
| `1f6338ae` | 232 | **24** |
| `66d1b52a` | 251 | **24** |

The intersection is not incidental. It contains `l10n_th_withholding_tax`,
`l10n_th_withholding_tax_cert`, `l10n_th_reports_ext`, `l10n_th_partner`,
`bm_thai_rd_vat_company_search` and `convert_amount_text_to_thai` — **the modules this
package's withholding and Thai-reporting findings are drawn from.**

**`P07-F-64` — the stated exclusion reason is false.** The root excluded as *"different
products, out of scope"* supplies modules installed in **3 of 3** in-generation identities
tested. Class `MEAS`.

### 11.3 The copies are not the same code

Every one of those six modules exists in **both** the declared path set and the excluded root,
and every one **differs**. Python-only, ignoring `__pycache__`/`.po`:

| module / file | changed lines |
|---|---:|
| `l10n_th_reports_ext/models/tax_report_vat.py` | 279 |
| `l10n_th_withholding_tax_cert/models/withholding_tax_cert.py` | 214 |
| `l10n_th_withholding_tax_cert/wizard/create_withholding_tax_cert.py` | 125 |
| `l10n_th_withholding_tax/models/account.py` | 105 |
| `l10n_th_withholding_tax/models/account_move.py` | 101 |
| `l10n_th_withholding_tax/models/account_tax.py` | 31 |
| `l10n_th_withholding_tax/models/tax_report_pnd.py` | 16 |

Those are the files carrying `P07-F-51`, `P07-F-57`, `P07-F-63` (`models/account.py`),
`P07-F-11` (`tax_report_pnd.py`) and `P07-F-62` (the certificate module).

### 11.4 Which copy is deployed — decided for one module, unresolved for the rest

| module | declared set | excluded root | installed in all 3 | verdict |
|---|---|---|---|---|
| `l10n_th_withholding_tax_cert` | **19.0.1.5** | 19.0.1.4 | **19.0.1.4** | **the declared copy is a version AHEAD of every deployment** |
| `l10n_th_withholding_tax` | 19.0.1.4 | 19.0.1.4 | 19.0.1.4 | **undecidable by version** |
| `l10n_th_reports_ext` | 19.0.1.4 | 19.0.1.4 | 19.0.1.4 | **undecidable by version** |

**`P07-F-65` — two different code bodies ship under one version string.** For two of the three
modules, the declared copy and the excluded copy carry the *same* `version` while differing by
31–279 lines of Python. A version string therefore **cannot identify which copy is deployed**,
and `P07-U-01` is not closable by reading manifests. Class `MEAS`.

The `_cert` row is decided and it is the uncomfortable direction: the declared path set holds
`19.0.1.5` — including a migration folder and a cache-invalidation companion (`models/
account_account.py`) that the other copy lacks entirely — while **every deployment examined
runs `19.0.1.4`**. Source findings drawn from that copy describe code that is running nowhere
in this package's population.

### 11.5 Blast radius, stated precisely and not more widely

- **Runtime results are unaffected.** `P07-F-42`, `P07-F-63`, `P07-F-01`'s prevalence,
  `P07-F-61` and `P07-F-62`'s counts are read out of the databases, not out of either copy.
- **`P07-F-01` is unaffected.** Its predicate lives in `smesplus_account_reports/models/
  account_generic_tax_report.py`, a different module; neither copy of `tax_report_vat.py`
  contains the literal it tests — checked, 0 occurrences in both.
- **Source-side attribution is what is now open.** For `P07-F-11`, `P07-F-51`, `P07-F-57`,
  `P07-F-62` and `P07-F-63`'s source half, the *line* cited is from the declared copy, and
  whether that copy is the deployed one is decided against it in one module and undecidable in
  two. **Opened as `P07-U-28`.** The findings are not withdrawn: their runtime halves stand,
  and no re-reading has yet shown the cited behaviour differs between copies. What is withdrawn
  is the assumption that the declared copy is the deployed one.

### 11.6 The class, and why P04's framing is the right one

P04 registered its own **true** exclusion as a finding because *a reader could not tell its
case from a false one*. That is the entire value of the rule, and this section is what the
other outcome looks like. Both exclusions were written the same way, with the same authority —
none — and only running the check separated them.

The declared path set was never wrong about what it contained. It was wrong about **what it
left out and why**, and that reason sat in the register a reader would consult to audit the
scope. Same shape as `REV-E-44`, one level up: there the population was defined by an
assertion inside the evidence table; here the **source scope** is.


---

## 12. A v18 Identity, Newer Than Every Artefact Enumerated, Outside Both Roots — `P07-F-66`

P04 re-ran its census over a **declared** path set instead of the two directories it had been
using, and found a database neither package had enumerated. Verified here independently before
any of it was used.

### 12.1 The identity

`~/OCC_BACKUP/idemo18_uat_pre_scgl_occ_website_20260830_085432.dump` — `dbname: idemo18_uat`,
`database.uuid 551ab874-…`, created 2026-08-18, **`base 18.0.1.3`**, **40,353 move lines**,
4 companies. Dated 2026-08-30: **newer than every artefact in `§10`'s census.** It needs the
newer client, so a default client reports it *unreadable*, not *absent*.

**`P07-F-66` — a sixth identity, in a third generation, with a real transacted population.**
`§10.2` published **7 snapshots · 5 identities** as a corrected census. It was marked **SUPERSEDED AND A LOWER BOUND** rather than
replaced while the full content sweep was still executing. **That sweep has since finished:
15 snapshots · 7 identities · 3 generations — see `§13`.**

### 12.2 Why `§10` missed it, which is not the reason `§10` gave

`§10` corrected an *eligibility* error and, in doing so, declared its own census method. That
method was two directories — `~/Downloads` and `/Volumes/iMacSys` — **chosen and never
written down as a path set.** The artefact sits in `~/OCC_BACKUP`, a sibling of one of them.

So `POPULATION`, `PATTERN` and `UNIT` were declared and executed at `§10.7`, correctly, and
`PATH SET` — the one clause this programme fixed first, and the one `13` exists to declare —
was silently author-chosen for the runtime evidence while being rigorously declared for the
source evidence in the same package.

**P04's formulation, adopted: raising the authority of a statement about a population does
nothing for a population that was drawn wrongly.** And the fourth rung on the ladder from
`REV-M-22`: **having the rule, recalling it, running it, and running it on the right set.**
`REV-M-25`.

**No check in the four-check sweep could have caught this**, and that is a property of the
sweep, not an oversight in it: identifiers, table structure, manifest hashes and the Layer-1
scrub all have the *package* as their unit. **No check whose unit is the package can find
evidence that is not in it.**

### 12.3 The battery, re-run on the v18 identity

| | result | effect |
|---|---|---|
| `P07-F-01` — VAT group name | `{"en_US": "VAT 7%"}`, no `th_TH` | **does not fire.** Prevalence unchanged at 1 of 4 *in-generation*; this identity is v18 and out of generation |
| `P07-F-42` — zero-rate taxes | 16 of 80, **all** in groups `2, 7, 12, 17` | **fires** |
| `P07-F-42` — target group names | all four `{"en_US": "TAX 1%"}` | **fires, in a naming variant** |
| `P07-F-61` — `account_tax_unit` | present in TOC, **0 rows** | holds; now **6 of 6 identities** |
| `P07-F-63` — flagged accounts | **2 of 658** | a fourth distinct configuration |
| `P07-F-62` — certificates | **332**, `income_tax_form` 205 `pnd53` / 125 `pnd3` / 2 null | second real certificate population |

### 12.4 `P07-F-42` is now cross-generation in three generations, and its mechanism is confirmed

The four target groups are **exactly the lowest-id tax group belonging to each of the four
companies** — company 2 → id 2, company 3 → id 7, company 4 → id 12, company 1 → id 17. That
is the mechanism `P07-F-42` states, observed in a generation where the id ordering differs from
every previously examined identity, so it is not an artefact of ids starting at 1.

And the group is named **`TAX 1%`**, not `WHT 1%` — an independent confirmation of `P07-F-15`
(group naming varies between deployments). The finding does not depend on the name: in **v16 it
was `Taxes`, in v18 `TAX 1%`, in v19 `WHT 1%`**, and in all three it is a **withholding or
generic group and never a VAT group**. `P07-F-42` now holds in **v16, v18 and v19**.

### 12.5 `P07-F-62` strengthened, and one figure in it made precise

A second real certificate population, in a different generation, carries a populated s.40
income-type taxonomy:

| identity | cert lines | income types observed |
|---|---:|---|
| `45a8e08e` (v16) | 6,159 | `5` ×4,381, `6` ×1,766, `2` ×12 |
| `551ab874` (v18) | 348 | `5` ×332, `6` ×16 |

**Precision correction to the register:** `P07-F-62` describes the field as *"the 15-value s.40
taxonomy"*. Fifteen is the **domain**; the **observed** distribution is three values across two
generations and 6,507 lines. The finding — that a correct per-line income type is stored and
the export derives income type from the tax rate instead — is unaffected and now rests on two
generations rather than one. `REV-E-50`.

### 12.6 What is NOT claimed

The other artefacts P04 lists by name — further `iEVING`, `BK12MAY26`, `iMSCG`, `pankhamhom`,
`iErpOCC`, `iSCErP` copies and a simulation-lab set — are **name-matched candidates, not
counted here**. Turning a candidate list into a census is the error this section exists to
record. They are counted when the content sweep finishes and each is keyed on `database.uuid`.


---

## 13. The Census, Finished — 15 Snapshots · 7 Identities · 3 Generations — `P07-F-67`

`§12` marked the population a **lower bound** rather than publishing a number that was not
finished. The sweep has finished. This is the number, with the root set declared.

### 13.1 Declared method

**Roots:** `$HOME` and **every entry in `/Volumes`** — enumerated at run time, not chosen.
**Filter:** none by extension. **Signatures:** `PGDMP` magic bytes; ZIP central directory
containing `dump.sql`. Files under 1 MB skipped. **Identity key:** `database.uuid` from
`ir_config_parameter`. **Generation key:** `base` row of `ir_module_module`.

### 13.2 A raw path count is not an artefact count

The sweep returns **57 path hits**. That is not the answer. `/Volumes/iMac` is a **mount of
this same machine**, containing `/Users/admin` and `/Volumes/iMacSys` again — and containing
them **twice**, once directly and once under `System/Volumes/Data`. Every artefact therefore
appears three times, and one appears fifteen.

**A content census over mounted roots inflates whenever one root is a mirror of another**, and
the inflation is invisible in the total: 57 is a perfectly reproducible number that means
nothing. Deduplicated: **19 real file paths, 15 distinct artefacts.**

### 13.3 The population

| identity (`database.uuid`) | snapshots | `base` | generation |
|---|---:|---|---|
| `a1430edc-…` | 2 | `19.0.1.3` | v19 |
| `f4a44cce-…` | 1 | `19.0.1.3` | v19 |
| `1f6338ae-…` | 1 | `19.0.1.3` | v19 |
| `66d1b52a-…` | 2 | `19.0.1.3` | v19 |
| `551ab874-…` | 1 | `18.0.1.3` | **v18** |
| `a6664233-…` | **7** | `18.0.1.3` | **v18** |
| `45a8e08e-…` | 1 | `16.0.1.3` | v16 |

**15 snapshots · 7 identities · 3 generations.** Published census history for this one
population: **5 · 4 → 7 · 5 → 15 · 7.** Every correction came from a peer, none from a check
inside this package.

`a6664233` is a **simulation lab**: seven sequential snapshots of one database taken within a
single day, six in a `snapshots/` directory and one filed under `evidence/`. Seven files, one
identity — the filename-is-not-identity rule from `§10.1` cutting the other way, and the
reason `15 · 7` is not `15 · 13`.

### 13.4 Every finding re-run at the final population

**`P07-F-01` — prevalence unchanged: 1 of 4 in-generation identities.** The two new identities
are v18 and store `{"en_US": "VAT 7%"}` with no Thai translation, so they neither confirm nor
weaken it. Three census corrections have not moved this figure once the generation filter is
applied, which is the first stable denominator in this file.

**`P07-F-42` — 7 of 7 identities, 3 of 3 generations.** `P07-F-67`. In `a6664233` the 16
zero-rate taxes land in groups `1, 6, 11, 16`; in `551ab874`, groups `2, 7, 12, 17`. Both sets
are **exactly the lowest-id tax group of each company**, and in `551ab874` the ids do not begin
at 1. The target group is named `Taxes` in v16, `TAX 1%` in both v18 identities, `WHT 1%` in
v19 — **and is a withholding or generic group in every one of the seven, never a VAT group.**
This is now the best-evidenced finding in the package by a very large margin, and it remains
classed `INF` on the load-order link.

**`P07-F-63` — a second fresh install, in a second generation, also zero.** `a6664233` holds
**0 move lines** and **0 of 152 accounts flagged**; `f4a44cce` (v19) holds 0 move lines and 0
of 237. Two never-transacted installs in two generations, both zero. Every transacted identity
flags some and **no two agree**: 3 of 586, 2 of 544, 2 of 544, 2 of 658, 1 of 339. The
never-provisioned half now has two independent positive controls rather than one.

**`P07-F-61` — corrected precision, `REV-E-52`.** Published as *"present and empty in all 7
snapshots"*. At 15 snapshots that is wrong in one identity: in `a6664233` the table is **absent
from the archive TOC entirely** — the module is not installed — not present-and-empty. Correct
statement: **present and empty in 6 of 7 identities; absent in the seventh.** The conclusion is
unchanged; the distinction is exactly the empty-versus-absent one this file introduced at
`§10.4`, so publishing it wrongly one section later is worth the record.

**`P07-F-62` — unchanged.** Certificates exist in 2 of 7 identities (`45a8e08e` 5,201,
`551ab874` 332); the five others hold 0 or 1.

### 13.5 What this does not settle

Seven identities is what **this host** holds. It is not a claim about deployments, and no
finding here is denominated over customers, sites or installations — only over databases found
on one machine. `P07-U-01` remains open, and `P07-U-28` is untouched by any of this: which
**copy of the source** these databases run is a separate question from how many databases there
are, and it is still decided against the declared path set in one module and undecidable in two.


---

## 14. The Declared Source Set Is Not the Deployed Set — `P07-F-68`, `P07-F-69`

`§11` asked whether an **excluded** root overlapped the deployed modules. P04 asked the
stronger question — **how many installed modules are in NO declared root at all** — and got 27
on its own package. Run here.

### 14.1 Declared PATH SET against installed modules

Declared set: **1,507 manifests / 1,512 distinct module names** across the three roots of
`13 §1`. (Published as *1,502 module directories* from a `-maxdepth 2` walk — corrected at
`§16.4`, `REV-E-60`; the counts below are unchanged, re-run against the corrected set.)

| identity | installed | in declared set | **in NO declared root** | declared, not installed |
|---|---:|---:|---:|---:|
| `a1430edc` v19 | 486 | 460 | **26** | 1,042 |
| `1f6338ae` v19 | 232 | 218 | **14** | 1,284 |
| `66d1b52a` v19 | 251 | 233 | **18** | 1,269 |
| `551ab874` v18 | 361 | 312 | **49** | 1,190 |

**`P07-F-68` — the declared set is not the deployed set in either direction.** Union of
installed-but-undeclared across the four: **85 modules**. Of those, fourteen are accounting- or
tax-adjacent by name, including `account_payment_multi_deduction`, `scgl_account_coa_control`,
`scgl_date_range_auto_period`, `journal_entries_report` and **`scgl_tax_period_date`**.

`account_payment_multi_deduction` is **installed** in two identities. `P07-F-20` reports it as
*not installable from the declared set* and classes that as a set-composition artefact; the
runtime now says the module is deployed, which confirms the classification and removes any
reading of `P07-F-20` as a capability gap.

### 14.2 `P07-F-69` — the tax-period module this package analysed is installed nowhere

Tax-period membership is one of the two structural causes this package rests on. The module
analysed throughout is `smesplus_tax_period_date`, in the declared set.

| module | in declared set | installed in `a1430edc` | `1f6338ae` | `66d1b52a` | `551ab874` |
|---|---|---|---|---|---|
| `smesplus_tax_period_date` | yes | **no** | no | **no** | no |
| `scgl_tax_period_date` | **no — in no declared root** | **yes** | no | **yes** | no |

**`smesplus_tax_period_date` is installed in 0 of 4 identities.** The module that is installed
carries a different **technical** name, the **same display name** *Tax Period Date*, and the
**same version** `19.0.0.1`.

### 14.3 And the deployed one is the same code — which is why the finding survives

Diffed after normalising line endings: `models/tax_period.py`, `__init__.py` and the view are
**identical**; `__manifest__.py` differs in one field, `author`. The raw diff reported **72
changed lines**, and **every one of them was a CR**.

So `P07-F-03`, `P07-N-02`, `04 §4` and the tax-point matrix rows **transfer intact** — the
deployed code is the analysed code. What is wrong is every statement that identifies the
mechanism by its **technical module name**: those name a module no examined deployment has
installed. Corrected in place rather than restated, since the behaviour is unchanged.

This is `P07-F-65` at a second level. There, two code bodies shared one version string. Here,
**two technical identities share one display name and one version, and the code is the same** —
the failure mode inverted. Neither name, nor version, nor display name identifies deployed
code. Only the installed-module list does.

### 14.4 `§11.3`'s diff counts were inflated — `REV-E-54`

Having found a 72-line diff that was 100% line endings, the published `§11.3` counts had to be
re-run the same way. They are **real differences**, but smaller than published:

| file | published | normalised |
|---|---:|---:|
| `l10n_th_reports_ext/models/tax_report_vat.py` | 279 | **174** |
| `l10n_th_withholding_tax_cert/models/withholding_tax_cert.py` | 214 | **179** |
| `l10n_th_withholding_tax_cert/wizard/create_withholding_tax_cert.py` | 125 | **106** |
| `l10n_th_withholding_tax/models/account.py` | 105 | **94** |
| `l10n_th_withholding_tax/models/account_move.py` | 101 | **102** |
| `l10n_th_withholding_tax/models/account_tax.py` | 31 | **30** |
| `l10n_th_withholding_tax/models/tax_report_pnd.py` | 16 | **17** |

`P07-F-65` stands — the copies genuinely differ, by 17 to 179 lines. The magnitudes were
overstated by up to 38%. **A raw diff line count is not a measure of code difference until
line endings are normalised**, and the same command that produced the `§11.3` table produced a
count that was entirely artefact one section later. `REV-M-28`.

### 14.5 A false zero that would have reversed a live finding — `REV-E-55`

The first re-run of the table above returned **0 for all seven files**. Not because there were
no differences: the shell loop used `set -- $spec` to split a two-word string, and **zsh does
not word-split unquoted parameters**, so `diff` ran on paths that did not exist and reported
nothing. Seven clean zeros, perfectly reproducible.

Published, that would have read *"the `§11.3` differences were line-ending artefacts"* — a
**withdrawal of `P07-F-65` caused entirely by a broken command.** What caught it was an
existence control printing whether both paths resolved; the zeros themselves were
indistinguishable from a real result. Same class as `REV-E-42`, opposite direction: there a
filter that could not fire produced evidence *against* the strongest finding; here a loop that
could not run produced evidence *against* a fresh one.

### 14.6 The pattern P04 named, with this package's instance of it

Three undeclared bounds, each one level further out: archive **signature set** (`§10.7`),
archive **path set** (`§12.2`), and now the completeness of the **source set** against
deployment. P04's formulation, adopted: **a scope is a claim, and a claim written as prose has
no denominator.** This package declared its source scope as three paths with manifest counts —
better than a description — and it was still never tested against what is installed. **Naming
the root is not the same as testing the root.**


---

## 15. The Control on the Result I Liked — `P07-F-42` Is Latent, Not Live — `P07-F-70`

P04's rule, and the reason this section exists: **a test run only when it confirms is not a
test. The control belongs on the results you like, not only the ones you doubt.** `P07-F-42`
is the best-evidenced finding in this package — 7 of 7 identities, 3 of 3 generations — and
it had never been asked the discriminating question.

### 15.1 The question never asked

`P07-F-42` states that zero-rated and exempt VAT taxes resolve into a withholding tax group and
**therefore settle against the withholding control accounts**. Everything published tested the
*first* clause — which group the tax resolves to. Nothing tested the second: **has that ever
posted?**

### 15.2 The control, with its own positive control

Run on the two identities with real transaction volume:

| | `551ab874` v18 | `45a8e08e` v16 |
|---|---:|---:|
| move lines | 40,353 | 447,384 |
| **control** — lines that are a tax line at all | 5,202 | 33,114 |
| **control** — tax lines for a **non-zero** tax | 5,202 | 33,114 |
| **result** — tax lines for a **zero-rate** tax | **0** | **0** |
| base lines carrying a zero-rate tax | 0 | **15,973** |

The controls fire: thousands of real tax lines exist, posting to 9 and 6 distinct accounts. The
query works. **And zero-rate taxes have produced no tax line in either deployment** — in the
v16 identity, across **15,973 base lines that do carry one.**

The reason is structural, not accidental: a tax whose amount is zero generates no tax line, and
the tax group's control account is only reached **through** a tax line. So the misassigned group
has no vehicle to post through.

### 15.3 What is withdrawn and what survives

**`P07-F-70` — `P07-F-42`'s accounting consequence is LATENT, not live.** The posting-path
claim — *"settle against the withholding control accounts"* — has **never occurred** in either
transacted deployment, and cannot while the rate is zero. `P07-F-42` is reclassified from a
posting-path finding to a **configuration and reporting** finding.

What survives is not small, and one part of it is arguably worse than what it replaces:

1. **The configuration defect is live and universal** — 7 of 7 identities, **17 of 17 company
   sets that hold zero-rate taxes** (enumerated: 1+1+3+3+4+4+1), every one resolving to a
   withholding or generic group and never a VAT group. Untouched.
2. **The reporting consequence is live and measurable.** In `45a8e08e`, **15,973 posted base
   lines carry a zero-rate tax whose group is not a VAT group.** Any report that selects by tax
   group — including the two s.87 registers at the centre of `P07-F-01` — cannot see those
   lines as VAT supplies. That is a live statutory-reporting effect on a five-figure line
   population, and it was sitting underneath a claim about control accounts.
3. **The posting consequence remains conditional, not disproved.** It would fire for any tax in
   these groups whose rate ceases to be zero, and the group assignment is what would carry it.
   Recorded as conditional; not counted as evidence.

### 15.4 Why this is the same instrument three times

`f4a44cce` turned a refutation of `P07-F-63` into a positive control for its surviving half.
P04's `P04-F-95` turned 1,720 draft entries — large, and in the expected direction — into a
negative, because every one was future-dated. This turns a 7-of-7 confirmation into a latency
finding. **In all three the confirming number arrived first and the discriminating question
second**, and in all three the second question was the one that decided what the number meant.

`P07-F-42` keeps its `S1` severity: a misconfiguration that silently removes a five-figure line
population from the statutory VAT registers is not less serious than one that posts to a wrong
account. It keeps class `INF` on the load-order link. What it loses is a mechanism it never had.

### 15.5 `§13.2`'s stated reason was wrong — `REV-E-57`

`§13.2` explained the 57-vs-15 inflation by saying `/Volumes/iMac` is *"a mount of this same
machine"*. P04 checked rather than accepted it: it is a **symlink to `/`** (`lrwxr-xr-x iMac ->
/`). The mechanism is therefore different — `os.walk` does not follow symlinks it *encounters*,
but this sweep passed the symlink as a **starting root**, which resolves. The doubling under
`System/Volumes/Data` is macOS firmlink structure, not a second mount.

**The count of 15 artefacts is unaffected; the reason given for it was wrong.** Third time this
session a *stated reason* has failed while the number it explained held — after the `iEVING`
exclusion (`REV-E-44`) and the `efaplus-custom` exclusion (`P07-F-64`). A number and the story
told about it are two claims, and only one of them tends to get checked.


---

## 16. Code Identity Is Not Decidable From a Snapshot — and Why — `P07-F-71`

P04 named four axes, each failing one level further out: **signature set → path set → source
scope → code identity**, and observed that the fourth *"is the only one of the four that no
amount of declaring fixes."* This section tried to close it for the two modules `P07-F-65`
left undecidable, failed, and the failure is more useful than the attempt.

### 16.1 The attempt, and the false discriminator — `REV-E-59`

If the two copies of a module declare **different fields**, `ir_model_fields` in a deployed
database says which is installed. A first pass appeared to find exactly that in
`l10n_th_reports_ext`: `date_from_str` / `date_to_str` in the declared copy against
`date_from` / `date_to` in the other. The deployed model carried `date_from` / `date_to` and
no `_str` variants in **3 of 3** v19 identities — an apparently decisive result against the
declared copy.

**It was false.** The pattern was `^\s*name = fields.X`, and what it matched was

```
date_from_str = fields.Date.to_date(date_from).strftime('%d/%m/%Y')
```

a **local variable inside a method**, not an ORM field declaration. The `date_from` /
`date_to` fields on that model come from elsewhere entirely. A regex that cannot distinguish a
class-body assignment from a method-body assignment produced a confident, reproducible, wrong
answer — and it pointed the way the author already suspected.

Third instance this session of a pattern matching something other than what it claimed, after
the literal `0` filter (`REV-E-42`) and the zsh loop that never ran (`REV-E-55`).

### 16.2 Done properly, with coverage declared

Re-run with an AST walk taking **class-body assignments only**:

| module pair | files parsed (declared / other) | parse failures | class-level fields | difference |
|---|---|---:|---:|---|
| `l10n_th_reports_ext` | 4 / 4 | 0 | 0 / 0 | **none** |
| `l10n_th_withholding_tax` | 14 / 14 | 0 | 19 / 19 | **none** |
| `l10n_th_withholding_tax_cert` | 12 / 10 | 0 | 37 / 37 | **none** |

View XML compared the same way: **no differing lines in any of the three pairs.**

### 16.3 `P07-F-71` — and it narrows `P07-U-28` rather than closing it

**The two copies differ only in Python method bodies.** Identical class-level field sets,
identical view XML — **nothing that differs is persisted**. So code identity for these modules
is not decidable from any database snapshot, not for want of a better query but because the
divergence leaves no trace in the database by construction.

That is a bounded and useful result, because it splits the exposure:

- **Source findings that cite structure are discharged.** Both copies declare the same models,
  fields and views, so which copy is deployed cannot change them.
- **Source findings that cite method logic remain open**, and those are the ones at risk:
  `P07-F-11` (the PND branch selection), `P07-F-51` / `P07-F-63` (the provisioning guard),
  `P07-F-57` (the index error), `P07-F-52` (the wizard's field read). All live in method
  bodies, which is exactly where the copies diverge by 17–179 lines.

`P07-U-28` is **narrowed to behavioural claims** and remains open. Closing it needs the
deployment's addons directory, which is not on this host — a runtime request, not research.

### 16.4 Two corrections that came with it

**`REV-E-60` — the declared set was understated.** `§14.1` gave it as **1,502 module
directories**, from a `-maxdepth 2` walk. The full walk finds **1,507 manifests / 1,512
distinct module names**: five modules are nested deeper. `P07-F-68`'s counts are **unchanged**
— re-run against the corrected set, the per-identity figures are still 26 / 14 / 18 / 49 and
the union is still 85, because the ten extra names are installed nowhere. The denominator was
wrong; the finding was not. This is the `-maxdepth` class that `REV-E-05` caught in this
package's first week, recurring in the section that measures scope completeness.

**`REV-M-31` — coverage goes out with the result**, adopted from P04. Their twin test first
reported **11 twins**, ten of which were a single bogus group: the manifest parser failed on
10 of 65 manifests, recorded each as name `?`, and **the failures collided with each other**.
At 65/65 the answer was 0. Run here with coverage declared: **1,507 of 1,507 manifests parsed,
0 failures, 21 display-name twins — all of them the reference product's own
community/enterprise pairs**, none of the `P07-F-69` kind.

### 16.5 The sharper rule, which is P04's and needs both halves

> A broken test produced **seven clean zeros** that would have withdrawn a live finding.
> A broken parser produced **eleven confident hits** that would have manufactured one.

**A null that behaves like a value is worse than a null that behaves like nothing, because it
collides** — the ten `?` names grouped themselves into precisely the shape the test was looking
for. And a null that behaves like nothing is not safe either: it reads as a clean negative.
The two failure modes are opposite in appearance and identical in cause — **the test could not
see its inputs, and said nothing about that** — so the control is the same for both: publish
what the test could see, next to what it found.


---

## 17. The Headline's Unmeasured Clause — `P07-F-01`'s Trigger Is Refuted — `P07-F-72`, `P07-F-73`

P04 sharpened `REV-M-30` one level in: **a finding and the clause of it that was never measured
are two claims, and only the measured one was ever defended** — adding that *the exhaustive
testing of the first clause is what made the second one feel safe.* `P07-F-42` had that shape
and `§15` cost it a mechanism. Applied to the headline finding of this package, it costs more.

`P07-F-01` as published: *the registers admit a row only if the group name equals
`{'en_US': 'VAT 7%'}`; that name is translatable; **installing Thai — the expected act for a
Thai deployment — changes the stored value and empties both registers, silently.*** The
predicate was verified in source and the stored name measured in 7 identities. **Neither the
trigger nor the consequence was ever measured.**

### 17.1 The trigger is refuted — `P07-F-72`

| identity | `th_TH` active | partners on `th_TH` | group name carries `th_TH` |
|---|---|---:|---|
| `a1430edc` | **yes** | 12 | **YES — fires** |
| `1f6338ae` | no | 0 | no |
| `66d1b52a` | **yes** | 5 | **no** |
| `551ab874` v18 | **yes** | **3,480** | **no** |
| `45a8e08e` v16 | **yes** | 15 | **no** |

**Thai is active in 4 of 5 identities and only 1 carries the translation.** Installing Thai
does **not** put a `th_TH` value into the tax group's name. The published trigger — the single
sentence that made this finding urgent — is **false**.

**What the data does show.** In the firing identity all five groups were created **in one
transaction, already carrying both languages, and never edited** (`create_date` =
`write_date` = 2026-02-02 12:46:35, `create_uid` = `write_uid` = 1). In `66d1b52a` the groups
were created `en_US`-only and Thai was activated **afterwards** — and activating it did not
retro-translate them. In the v16 identity one group *was* edited later and does carry a Thai
name; the VAT group, untouched, does not.

So the condition is **the chart template being loaded while Thai is already active** — an
**install-order** property, not a language-installation one. `FACT` for the data pattern
(create/write timestamps, 7 identities); `SUPPORTED INTERPRETATION` for the mechanism, since
the loader has not been executed. `P07-U-29` opened to close it by execution.

### 17.2 The consequence was never measured either — `P07-F-73`

| identity | move lines | **VAT-7% tax lines** | fires? |
|---|---:|---:|---|
| `a1430edc` @06-14 | 23 | **2** | **YES** |
| `a1430edc` @07-14 | 32 | **3** | **YES** |
| `1f6338ae` | 15 | 3 | no |
| `66d1b52a` | 563 | 12 | no |
| `551ab874` v18 | 40,353 | **5,202** | no |
| `45a8e08e` v16 | 447,384 | **32,672** | no |

**The only identity in which the defect fires holds 2 to 3 VAT-7% tax lines.** The two
deployments where an empty statutory register would matter — 5,202 and 32,672 rows — are
exactly the two that do not fire. **The consequence has never been observed on a populated
deployment**, and in the deployment where it does occur the register would return two rows if
the predicate worked.

### 17.3 What `P07-F-01` is, restated

- **The defect is real and unchanged.** A statutory register's row predicate compares a
  translatable field against an untranslated literal. Verified in source; not disputed.
- **The exposure is prospective, and its magnitude is now measured.** Any populated deployment
  that loads or reloads the Thai chart while Thai is active takes the predicate out — **5,202
  and 32,672 VAT-bearing tax lines** in the two populated identities are what would be at risk.
  That is a better statement for a decision-maker than the one it replaces, because it is a
  number rather than an adjective.
- **The severity argument survives and is sharpened.** *A defect silent in three deployments of
  four cannot be found by testing a system that works* — and it is worse than that: **the
  defect fires only where there is no data to reveal it**, and every deployment with data to
  lose is one install-order away from it.
- **What is withdrawn** is *"installing Thai empties both registers"* as a statement of
  observed cause, and *"the single most serious finding of this research"* as a claim resting
  on an unmeasured consequence. Severity stays `S1`; the basis changes from realised to
  prospective-with-measured-magnitude.

### 17.4 Both headline findings reduce to template load order

`P07-F-42` is classed `INF` on an unexecuted **load-order** link (`P07-U-20`). `P07-F-01`'s
real trigger is now measured as a **load-order** condition. **The two headline findings of this
package share a root cause that neither of them named**, and it is the one thing about a
deployment that leaves no trace afterwards: the order in which language and chart were
installed. `P07-U-20` and `P07-U-29` should be closed together, by execution, not by reading.

### 17.5 The pattern, three instances deep

Three compound findings this session, all the same shape: `P07-F-51` (split, revealed
`P07-F-63`), `P07-F-42` (mechanism withdrawn, `P07-F-70`), `P07-F-01` (trigger refuted,
consequence unmeasured). In each the measured clause was tested across every identity available
and the unmeasured clause travelled with it untouched. P04's diagnosis is exactly right:
**the exhaustive testing of the first clause is what made the second one feel safe.** A
7-of-7 result on one clause is not evidence about the other, and it reads like it is.
