# P07 — RUNTIME EVIDENCE, AND THE INCAPACITY CLAIM THAT CONCEALED IT

Session ID: `SMEPLUS-26-09-04-ACC-P07-TAX-TH-REV2-001`
Classification: `LAYER 2 — AUDIT QUARANTINE`
Date: `2026-09-05`

## 1. Why This File Exists

Every behavioural statement in files `00`–`21` is source-derived, bounded by `P07-U-02`
(*no database was queried*) and by `13 §7`. At `r8` that entry was re-marked `ASSUMED`
rather than `TESTED`, after a peer registered having asserted an incapacity it had never
checked.

It was then **tested, and it was false.**

## 2. The Error, Recorded First — `REV-E-24`

A PostgreSQL dump sits **inside this session's own declared PATH SET**:

    ACCOUNT/01 ACCOUNT/SOURCE CODE/iTEST02_2026-06-14_14-41-19.dump    65,444,053 bytes

`13 §2` declares that directory as one of the three roots of the research universe. The
session listed that directory **in its first minutes of execution**, and the dump appears in
that listing. It was read past, and `P07-U-02` was published over the top of it.

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
| `P07-U-02` | "no database was queried" | **superseded by this file** for the tables listed in §3 |
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

> **POPULATION BANNER — every count in this section is SUPERSEDED.** The figures below were
> correct when written and are left standing as the record of what was published. The current
> population is **15 snapshots · 7 identities · 3 generations** (`§13`), and the current
> denominators are: `P07-F-01` **1 of 4** in-generation identities (not 1 of 2); `P07-F-42`
> **7 of 7** identities and **17 of 17** company sets (not 2 of 2 / 6); `P07-F-61` **present
> and empty in 6 of 7 identities, absent in the seventh** (not 2 of 2); `P07-F-63` **two
> never-transacted installs at zero against five transacted identities that never agree** (not
> 3 of 3). Wherever a figure here disagrees with `§13`, `§13` governs.



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

> **POPULATION BANNER — every count in this section is SUPERSEDED.** The figures below were
> correct when written and are left standing as the record of what was published. The current
> population is **15 snapshots · 7 identities · 3 generations** (`§13`), and the current
> denominators are: `P07-F-01` **1 of 4** in-generation identities (not 1 of 2); `P07-F-42`
> **7 of 7** identities and **17 of 17** company sets (not 2 of 2 / 6); `P07-F-61` **present
> and empty in 6 of 7 identities, absent in the seventh** (not 2 of 2); `P07-F-63` **two
> never-transacted installs at zero against five transacted identities that never agree** (not
> 3 of 3). Wherever a figure here disagrees with `§13`, `§13` governs.



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
opened, and the population at that point was 7 snapshots / 5 identities — itself superseded by
**15 / 7** at `§13`. This line is left standing with its
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
| VAT-group name carries `th_TH` (`P07-F-01`) | **yes** | no | no | no | no |
| zero-rate taxes | 4 | 4 | 12 | 12 | 4 |
| …all landing in a **non-VAT** group (`P07-F-42`) | **yes** | **yes** | **yes** (3 sets) | **yes** (3 sets) | **yes** |
| `account_tax_unit` rows (`P07-F-61`) | 0 | 0 | 0 | 0 | 0 |
| accounts / flagged (`P07-F-63`) | 586 / **3** | 237 / **0** | 544 / **2** | 544 / **2** | 339 / **1** |
| withholding certificates (`P07-F-62`) | 0 | 0 | 0 | 1 | 5,201 |
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

The first `P07-F-42` pass on `f4a44cce`/`1f6338ae` reported **0 zero-rate taxes**. The filter
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

**11 artefacts · 7 snapshots · 5 identities** — superseded by **15 · 7** at `§13`, which the
next section's root set corrects. Snapshot and identity counts unchanged **at this root set**, so
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


---

## 18. The Axis Closed for One Module, and a Fifth Axis That Cannot Be — `P07-F-74`

P04 closed the code-identity axis for one of its modules by whole-tree hashing rather than
per-file diffing, and reported that its own first run of that test returned **44 copies in 3
groups, 42 of which hashed to `e3b0c44298fc…` — the SHA-256 of empty input** — because paths
containing spaces were word-split by the shell and the walk visited directories that do not
exist. That is this package's `REV-E-55` defect, reproduced in P04's shell **one message after
it was reported**, inside the test written to apply the lesson.

Their observation about *how* it failed is the one worth keeping, and it corrects `REV-M-32`:

> An empty result and a unanimous result are the same shape, because **emptiness is perfectly
> self-consistent**.

Forty-two failed walks did not scatter — they **collapsed into one group** and read as *"42
identical copies"*, the strongest possible agreement, in the direction the author wanted.

### 18.1 Adopted: the empty-input sentinel

Every hash comparison in this package now prints `e3b0c44298fc…` explicitly, prints the **file
count** behind each hash, and flags any group equal to the sentinel or holding zero files.
Applied below.

### 18.2 `P07-F-74` — code identity CLOSED for the tax-period module

`P07-F-69` established that `smesplus_tax_period_date` (declared, installed **nowhere**) and
`scgl_tax_period_date` (undeclared, installed in 2 of 4) share a display name and version. Five
copies exist on this host. Whole-tree hash, CR-normalised, over `.py`/`.xml`/`.csv`, excluding
`__manifest__.py`:

| copy | files hashed | tree hash |
|---|---:|---|
| declared `smesplus_tax_period_date` | 4 | `9353002540a70c0b…` |
| `scgl_tax_period_date` (Extra19) | 4 | `9353002540a70c0b…` |
| `scgl_tax_period_date` (worktree) | 4 | `9353002540a70c0b…` |
| `scgl_tax_period_date` (extra-module set) | 4 | `9353002540a70c0b…` |
| `scgl_tax_period_date` (home addons) | 4 | `9353002540a70c0b…` |

**One distinct tree from five copies.** Not the empty sentinel; four real files each. The only
difference anywhere is the manifest `author` field.

**So for the tax-period module the axis is CLOSED, not narrowed.** Which copy is deployed
cannot change any finding drawn from it — structural **or** behavioural. `P07-F-03`,
`P07-N-02`, `04 §4` and the tax-point matrix rows are **fully discharged** on code identity,
and `P07-U-28` no longer covers them.

As P04 said of its own closure: this is stronger than the `§16` result **only because these
copies happen not to have diverged**, not because the method improved. The three `l10n_th`
modules diverge by 17–179 real lines and stay under `P07-U-28`. A host-wide enumeration and
hash of every copy of those three is executing; **it is not reported here, because a partial
enumeration is not a result.**

### 18.3 The fifth axis — a fact that no longer exists to be looked at

P04's reading of `REV-M-33`, adopted, and it is a category the other four do not contain:

> Signature set, path set, source scope, code identity — each is about **where you looked**.
> Load order is about **a fact that no longer exists to be looked at.**

`P07-F-42` sits at class `INF` on an unexecuted load-order link; `P07-F-72` measures
`P07-F-01`'s real trigger as a load-order condition. Both headline findings of this package
turn on **the order in which language and chart were installed** — and a database records the
*result* of that order, never the order. The five translated rows created in one transaction
(`§17.1`) are the closest thing to a trace, and they are consistent with the mechanism without
establishing it.

**No archive either package holds can settle it**, which is why `P07-U-20` and `P07-U-29` are
not closable by more reading, more snapshots, or a wider census. They need a controlled
install, executed twice in opposite orders. That is a runtime request, and it is the single
most useful thing that could be asked of a deployment engineer on P07's behalf.

**And it changes what a HOLD means here.** Every other open item in this package is open
because something was not yet read. These two are open because the evidence was never
recorded by anyone — including the deployments themselves.


---

## 19. The Code-Identity Question Was a False Dichotomy — `P07-F-76`

`P07-F-65` and `P07-U-28` were framed as a **two-way** choice: the declared copy or the
excluded root's copy. The host-wide enumeration promised at `§18.2` has finished, and the
framing was wrong.

Every copy of the three modules on `/Volumes/iMacSys` and `$HOME`, whole-tree hashed
CR-normalised over `.py`/`.xml`/`.csv` excluding `__manifest__.py`, file count printed per
hash, empty-input sentinel flagged:

| module | copies | **distinct trees** | declared vs excluded |
|---|---:|---:|---|
| `l10n_th_withholding_tax` | 61 | **20** | different trees |
| `l10n_th_withholding_tax_cert` | 49 | **15** | different trees |
| `l10n_th_reports_ext` | 13 | **3** | different trees |

**`P07-F-76` — the deployed code for `l10n_th_withholding_tax` is one of twenty candidate
bodies on this host, not one of two.** `P07-U-28`'s exposure is 20-, 15- and 3-wide
respectively. `P07-F-65` is confirmed and understated: it reported that *two* copies differ
under one version string; there are twenty.

### 19.1 What the enumeration also shows

- **The declared copy is not unique in its own tree.** In all three modules an identical
  second copy sits under `STEP040301_SOURCE_INDEX/01_EXTRACTED/` inside the same working
  volume — same hash, so harmless, but it means the declared path set holds two paths to one
  body and a naive count of "copies in scope" would say 2.
- **Two single-file trees** (`1438dfe0…`, `74549d6f…`, one file each) — real content, not the
  sentinel, so these are **partial or truncated module copies**, not failed walks. The
  distinction is only visible because the file count is printed beside the hash, which is
  P04's control adopted at `§18.1` doing exactly what it was added for.
- **Prior generations are present**: v12, v14, v16 and v18 copies of these modules all exist
  on the host and hash distinctly. Any comparison that does not filter by generation first is
  comparing across product lines.

### 19.2 What it does not change

`P07-F-74` is untouched: the tax-period module's five copies are still one tree, so that
closure holds. `P07-F-71` is untouched: whatever the deployed body is, the copies compared at
`§16.2` agree on fields and views, so **structural claims stay discharged**. What widens is the
**behavioural** exposure, and it widens from *two candidates* to *twenty*.

`P07-U-28` restated: **which of 20 / 15 / 3 same-named code bodies each deployment runs is
undecidable from this host**, and the modules' method bodies are where the divergence lives.
`NOT ON THIS HOST` is the correct classification and the correct size is now stated.

### 19.3 A false positive in the check that found this — `REV-E-64`

Extending the orphan check to every identifier family (`§5`) made it match **bare** `F-nn` as
well as `P07-F-nn`. It reported `P07-F-81` as an orphan. There is no `P07-F-81`: the match was
`` `F-81` `` in `§7.4` of this file — **P04's identifier, cited in a passage about P04's own
package.**

**An identifier check that accepts bare identifiers collides with peer packages' identifiers**,
and in a two-package exchange that is not a rare case. The check now requires the `P07-`
prefix for this package's families and reports bare matches separately as *peer references*.
Caught in the first run of the extended check, by reading what it matched rather than trusting
the count — the same discipline that caught the false discriminator at `§16.1`.


---

## 20. Family Coverage — the Check Saw 8 of 46 — `P07-F-77`

`§5` extended the orphan check across identifier **families** and found 12 orphans in `P07-U`.
P04 ran the same extension and reported the mirror result: its check covered **2 of 14** owned
families, and produced **19 apparent orphans of which none were genuine**, because its package
uses at least **four definition conventions** — backticked table rows, bold text, prose, and a
peer's identifiers cited correctly — and the check knew one.

**Two failure modes of the same check, and they are opposite.** This package's check
under-reported: right convention, wrong scope. P04's over-reported: right scope, wrong
convention coverage. P04's observation is the one to keep — **19 false positives are worse
than a check that finds nothing, because they train a reader to dismiss the output**, so a
genuine orphan appearing later is lost in noise the check itself manufactured.

### 20.1 Coverage audit of this package's check

Every identifier-shaped token in backticks, counted by family: **46 families cited, 8 covered
by the sweep.** Of the 38 uncovered, seven are **foreign by attribution** and correctly not
this package's to define — `P04-B`, `P04-F`, `P11-G`, and the licence and external-document
tags `LGPL`, `OPL`, `OEEL`, `FR-TEN` — and five are governance/prompt identifiers. That leaves
**26 owned families that had never been enumerated against their citations**, the largest being
`S` with **319 citations**: the statutory source register, which backs every legal claim in the
package.

### 20.2 The result, with coverage stated

Run over all 26, accepting four definition conventions (table row, bold, heading, list item):

| | |
|---|---:|
| owned families audited | **26** |
| definitions found | 253 |
| citations resolved | 253 |
| **orphans** | **0** |
| conventions actually in use | **1** (table row; `W-K` also uses a list item) |

**`P07-F-77` — no orphans in any owned family beyond the `P07-U` set already corrected**, and
in particular **`S-01`…`S-40` all resolve**: no legal claim in this package cites a statutory
source that has no register row. That is a clean negative and it is reported with its coverage,
per `REV-M-31`.

It also localises the earlier defect precisely: `§5`'s 12 orphans were a **scope** failure and
not a convention failure. This package uses one definition convention throughout, which is why
extending the scope was sufficient here and would not have been sufficient for P04.

### 20.3 P04's refinement of `P07-F-71`, adopted

`P07-F-71` said: where copies agree on fields and views, **structural claims are discharged and
logic claims stay exposed**. P04 sharpened it against its own second module — 11 copies, 3
trees, the divergence being a presentational `span`/`div` wrapper and a multi-record-safety
change on a note write, **with the function actually cited byte-identical in both**:

> Not *views identical ⇒ structural claims safe*, but **compare the difference against the
> specific claim.** A presentational wrapper cannot carry a structural claim; a note write
> cannot carry an accounting one.

That is stronger than the version this package published, because it discharges claims
**individually** rather than by category, and it can discharge a claim even where the trees
differ. Applied here it becomes a per-finding test: for `P07-F-11`, `-F-51`, `-F-52`, `-F-57`
and `P07-F-63`'s source half, the question is not *which of 20 trees is deployed* but **whether
the cited function differs across the same-generation candidates at all.**

That test is executing over the v19-generation candidates and **is not reported here.**
`P07-U-28` stands as classified until it returns.


---

## 21. `P07-U-28` CLOSES — the Claim-Level Test Discharges All Four — `P07-F-78`

The per-finding test proposed at `§20.3` has returned. **P04's refinement did in one pass what
three sections of category reasoning could not.**

### 21.1 Two filters, applied in order

**Generation first.** Of the 61 copies of `l10n_th_withholding_tax`, **13 declare version 19.x**.
The other 48 are v12, v14, v16 and v18 bodies; comparing across them was comparing product
lines, which is what made the exposure look 20-wide.

**Then the claim.** Hashing only the **cited** files across those 13:

| cited file | finding | distinct bodies |
|---|---|---:|
| `models/account.py` | `P07-F-51`, `P07-F-63` | **2** (9 copies : 4) |
| `models/account_move.py` | `P07-F-57` | **2** (9 : 4) |
| `models/tax_report_pnd.py` | `P07-F-11` | **2** (11 : 1, 1 absent) |
| `wizard/account_payment_register.py` | `P07-F-52` | **1** |

**Two candidate bodies per cited file, not twenty.** `P07-F-76` stands as a statement about
*trees on the host*; it overstated the exposure to *these claims* by a factor of ten.

### 21.2 The four claims, tested against the difference

**`P07-F-11` — DISCHARGED.** The two bodies of `tax_report_pnd.py` differ **only in the
`title` column**: the declared body computes it from a partner company-type lookup (two
`LEFT JOIN`s and a `CASE`), the other binds `%(title)s`. **The PND branch selection and the
reported-event logic are byte-identical.** The difference cannot carry the claim — a display
title is not a branch predicate.

**`P07-F-51` and `P07-F-63` — DISCHARGED.** Both bodies contain the guard:
`if not account_id.wt_account: raise UserError("%s is not a Withholding account.")`. The
difference is an import list, a nesting level and a trailing comma in a signature.

**`P07-F-57` — DISCHARGED.** Both bodies index `invoice_repartition_line_ids[0].tag_ids[0]`
while guarding only on the **union** `invoice_repartition_line_ids.tag_ids`. The declared body
does it in one `.filtered()` with a chained `and`; the other splits it across two `.filtered()`
calls. **Same guard, same index, same latent error** — the second `.filtered()` sees only
records that passed the first, so the two are equivalent.

**`P07-F-52` — DISCHARGED, and byte-identically.** `wizard/account_payment_register.py` is
**0 changed lines** between the bodies, cited line 56 character-identical, and
`depends = ['account', 'l10n_th_reports']` in both — so the missing dependency on the
certificate module, which is the finding, holds in both.

### 21.3 `P07-U-28` is CLOSED

**Every behavioural claim under `P07-U-28` holds in both same-generation candidate bodies.**
Which copy is deployed cannot change any of them. The item is closed **on evidence**, and it is
the first open item this package has closed that way rather than by correcting itself.

`P07-U-01` stays open and stays `NOT ON THIS HOST` — *which* copy runs is still undecidable,
and `P07-F-76`'s 20 trees remain the correct answer to that question. What has changed is that
the answer no longer matters for any published finding. **`§5`'s classification moves: 4 closed,
20 `NOT YET READ`, 1 `NOT ON THIS HOST`, 2 `EVIDENCE NEVER RECORDED`.**

### 21.4 Why the category test could not have done this

`P07-F-71` discharged claims **by category** — structure safe, logic exposed — and by that
rule all four of these stayed exposed, because all four are logic. P04's rule discharges them
**individually, against the actual difference**, and three of the four are discharged by a
difference that is real code and simply cannot carry the claim: a display title, an import
line, a filter chained differently.

> **A presentational wrapper cannot carry a structural claim; a note write cannot carry an
> accounting one** — P04's formulation, and the generalisation is that *the size of a diff is
> not the size of the exposure.* `§11.3` measured 17–179 changed lines and treated that as the
> risk. The risk was four functions, and three of them were untouched.

This is the second time in this exchange that a finding's replacement was better than the
finding: `P07-F-70` traded a mechanism for a larger consequence, and here a 20-wide exposure
resolves to zero.


---

## 22. The Coverage Audit Had an Undeclared Floor — `P07-F-79`

P04 re-counted its own families after `§20` and found that the *"14 owned families"* it had
reported was itself author-chosen: families appearing twice or more, filtered at **a frequency
floor never declared**, then picked by eye. Enumerated with no floor: **43**, of which 17 owned,
and **four families had never been checked at all** — the largest being its event register, the
spine of one of its files.

**The same defect is in `§20.1` of this file, in the same clause.** The family census there
carried `if c < 2: continue`. It was never stated. So the correction of an under-scoped check
was itself computed over an under-scoped population — P04's phrasing, and it is exact.

### 22.1 Re-run with no floor, classified with reasons

| | families | citations |
|---|---:|---:|
| **owned — audited** | **34** | **1,861** |
| foreign by attribution | 10 | `P04-B`, `P04-F`, `P04-REV`, `P11-G`, bare `F` where it means P04's, the prompt and governance ids, `AASR-P07-VETO`, `FR-TEN` |
| not identifiers | 4 | `LGPL-3`, `OPL-1`, `OEEL-1`, `ACC-8` (a comment marker inside quoted source) |
| **unclassified** | **0** | — |

**48 families, not 46.** The floor hid exactly two, both singletons and both benign — `ACC-8`
and `P04-REV-19`. **The number moved by two and the method was wrong either way**, which is the
`REV-M-30` shape again: had the floor hidden an owned family with one citation, the audit would
have reported clean coverage over a family it never looked at.

### 22.2 P04's rule inverted — and this package had the inverse defect

`REV-E-64` required the `P07-` prefix so that a peer's identifier is not read as this package's.
P04 reports the converse: **`HOLD-02`, `HOLD-03`, `HOLD-05` are prior-package identifiers, and
where they were cited without attribution they were indistinguishable from unresolved local
ids.** *A foreign identifier without its attribution is an orphan to every reader and every
checker.*

Audited here, the defect is present in the **other** direction: **11 citations of this
package's own findings written bare** — `` `F-01` ``, `` `F-42` ``, `` `F-61` ``, `` `F-62` ``,
`` `F-63` `` in the `§10.3` results table and elsewhere. The prefix-requiring fix made them
**invisible to the checker**, while a reader mid-exchange could read them as P04's. All 11
written out in full. The two remaining bare `F-81` references are P04's and are attributed in
the prose that carries them.

**Both defects have one root: an identifier without its package prefix is ambiguous, and the
ambiguity resolves differently depending on which way the checker leans.** Requiring the prefix
converts a false positive into a silent omission. Neither is safe; only writing identifiers out
in full is. `REV-E-66`.

### 22.3 Two method points adopted

**`REV-M-42` — a family's class is a judgement, and the check must be re-run after the
judgement changes.** P04 reclassified `HOLD` as foreign and its sweep still reported those ids
as orphans for one run, register and checker disagreeing after the finding was written. The
classification above is a judgement of the same kind, so it is stated in the file and the sweep
re-run against it, not before it.

**`REV-M-43` — neither diagnosis was derivable from one package.** This package's 12 orphans
were a **scope** failure with one convention throughout; P04's 19 were a **convention** failure
with adequate scope. Extending scope was sufficient here and would have been useless there;
fixing conventions would have been useless here. **That is a stronger result for the exchange
than any single finding traded**, because it is about the method rather than the estate: the
same symptom — a check reporting the wrong thing — had opposite causes in two packages, and
each was invisible from inside.

P04's sharpening of the timing asymmetry, adopted as the better statement: **a silent check
fails at the moment it is trusted; a noisy one fails later, when someone stops reading it.**

### 22.4 One category, three items, not one price

P04 has accepted that `P04-B-47` admits a cheaper route than `P07-U-20` and `P07-U-29`: a
second capture of one identity at a different time, or the deployment's own audit trail, would
settle it without a controlled install. **That belongs in the ask.** If only part of a runtime
request is granted, the decision-maker should be told which part costs least rather than left
to infer it — and it is P04's item, not this package's, that is the cheap one.


---

## 23. What `P07-U-28`'s Closure Does Not Cover — `P07-F-80`

P04 applied `REV-M-41` to its widest number and narrowed `P04-B-46` from 27 to 9, then stated
the limit precisely: `ir_model_data` covers only records carrying an XML id, so **a module can
override `write`, `create` or `_post` in Python with no new field and no view and declare
nothing.** Nine is *a floor on what demonstrably touches, not a ceiling on what could affect.*

**That limitation lands on `P07-U-28`'s closure, and testing it found something.** `§21` closed
`P07-U-28` by comparing the **cited files of the cited module** across candidates. It answers
*which copy of `l10n_th_withholding_tax` is deployed*. It does not answer **what else is
installed on the same models.**

### 23.1 The instrument, and the control that fired first

Resolving `ir_model_data` through `ir_model_fields.model` and `ir_ui_view.model` into the
**business** model each module declares on. The naive reading — `ir_model_data.model` directly
— reports **0 modules touching `account.move`** in both identities tested. A clean, plausible,
completely wrong negative; P04's equivalent naive run said 1. Published, per `REV-M-32`,
because plausible-and-wrong is the kind that survives.

Resolved: **59** and **43** installed modules declare on a model this package's findings turn
on. Of those, the ones **installed but outside the declared PATH SET**:

| module | declares on | identity |
|---|---|---|
| `account_payment_multi_deduction` | `account.payment`, **`account.payment.register`** | `a1430edc` |
| `scgl_tax_period_date` | `account.move`, `account.move.line` | both |
| `account_discount_catalog` | `account.move` | both |
| `scgl_product_image` | `account.move`, `account.move.line` | `a1430edc` |

`scgl_tax_period_date` is already discharged — `P07-F-74` proved all five copies one tree.

### 23.2 `P07-F-80` — one of them wraps the method `P07-F-16` reports

`account_payment_multi_deduction` (v19.0.1.0.2, installed, **not in the declared PATH SET**)
declares `_inherit = ["account.payment.register", "analytic.mixin"]`.

**It does not touch `P07-F-52`'s surface** — zero references to `move_line_ids` or `wt_tax_id`
anywhere in it — so `P07-F-52`'s discharge at `§21.2` stands.

**But it overrides `_prepare_move_line_default_vals`**, which is the method carrying
`P07-F-16`'s base guard:

```
line_vals_list = super()._prepare_move_line_default_vals(write_off_line_vals, force_balance)
if not self.is_multi_deduction and write_off_line_vals:
    ...
    self._update_vals_writeoff(write_off_line_vals, line_vals_list, check_keys, update_keys)
return line_vals_list
```

The base, at the line `P07-F-16` cites, has **already discarded** the write-off contribution
when withholding lines are present (`if withholding_lines and write_off_lines: write_off_lines
= []`). The override calls `super()` **first** and then post-processes — so its write-off
handling runs over a list the guard has already stripped.

**Whether that changes the posted figures is not established here**, and it is not asserted.
What is established: **`P07-F-16` was analysed on a stack that is not the deployed stack.** An
installed module the declared PATH SET never contained wraps the exact method the finding turns
on. Classification `SUPPORTED INTERPRETATION` on the interaction; `FACT` on the override's
existence, its `_inherit`, and its call order. **`P07-U-30` opened.**

### 23.2a The copy question, asked before relying on the module

`P07-F-65` exists because this package once read a module without asking which copy it was
reading. So: **21 copies of `account_payment_multi_deduction` on this host, 5 distinct
(tree, version) groups — and every v19 copy is ONE tree** (`21497f9adaaa…`, 10 copies). The
override above is therefore **not copy-dependent**: whichever v19 copy is deployed, it is that
code.

One detail worth recording as the **inverse** of `P07-F-65`: two of those copies declare
`19.0.1.0.2` and `19.0.1.0.3` and hash to the **same tree** — *two versions, one body*, where
`P07-F-65` found *one version, two bodies*. A version string is unreliable in both directions.

### 23.3 The asymmetry between the two narrowings, stated in P04's terms

P04's narrowing **cannot close** `P04-B-46`: it has the deployment's declarations and can ask
what a module *declares* — a weaker question with a one-directional answer, so its other 18 are
*undemonstrated rather than cleared*.

This package's `§21` narrowing **did** close `P07-U-28`, because it had the cited code and could
ask whether the difference carries the claim. **But `§21` answered a narrower question than
`P07-U-28`'s citations were being used for**, and this section is that gap measured. The
closure stands as written; what it covers is now stated, and what it does not cover is
`P07-U-30`.

**The general form:** *a claim discharged against the right module is not discharged against
the deployed stack.* Copy-identity and stack-completeness are two questions, and closing the
first reads like closing the second.


---

## 24. Count the Forms, Not the Identifiers — and a Stem Collision — `P07-F-82`

P04's operative rule, which is narrower than either of our statements and generalises better:

> **A family is safe when it has exactly one canonical form and the check audits that form.**
> The failure mode is a family existing in **two** forms. Count the forms, not the identifiers.

Applied to this package's 34 owned families:

| | families |
|---|---:|
| **single-form — safe by construction** | **31** |
| dual-form | 3 (`P07-F`, `P07-D`, `D`) |

That explains the disparity P04 noticed — this package's 11 bare citations against its 1 —
without either of us being more careless: **most of P04's families never had a second form to
be silent about, and neither did 31 of these.**

### 24.1 The residue in `P07-F` is self-describing, and bounded rather than listed

Fifteen bare `` `F-nn` `` remain. Two are P04's `F-81`, attributed in the prose that carries
them. **The other thirteen are quotations inside the sentences that document the defect** —
`REV-E-66` and `§22.2` cannot state *"eleven citations were written bare"* and name them
without writing them bare.

P04 hit the same recursion and reports the terminating move, adopted here verbatim:

> **A self-describing register changes what it describes, so the only stable declaration is one
> taken last and expressed as a bound rather than a list.**

**Declared bound:** every bare `` `F-nn` `` in this package is either an attributed citation of
P04's identifier or a quotation inside text describing this defect. There are no others. Chasing
the residue to zero would require the finding to stop describing what it found.

### 24.2 `P07-F-82` — two owned families share a stem, and both were reported safe

The other two dual-form entries are not two forms of one family. **They are two different
families colliding on one stem:**

| identifier | family | meaning |
|---|---|---|
| `P07-D-01` | dependency register (`12`), 31 members | `l10n_th_withholding_tax_multi` → `account_payment_multi_deduction`, **BROKEN** |
| `D-01` | document matrix (`05`), 10 members | **Tax invoice (ใบกำกับภาษี)** — the most consequential statutory document in the package |

A reader meeting `` `D-01` `` in `10 §2` or `12 §3` could not tell which was meant, and **the
identifier check reported both families clean** — because both had definition rows, and the
collision is *semantic*, not structural. This is the one defect in this exchange that neither
the orphan check, the structural check, the manifest check nor the scrub could ever have found:
**every identifier resolved; two of them resolved to different things under the same name.**

**Corrected:** the document family is renamed `DOC-01`…`DOC-10`. 16 occurrences across three
files; the dependency family verified unchanged at 47 citations before and after, as the
control on the rename. **All 34 owned families now have exactly one canonical form and no
shared stem.**

### 24.3 P04's qualification of `REV-M-43`, which matters for how it is read

Adopted as stated, because the general version invites the wrong reply:

> *Neither diagnosis was derivable from one package* is true, but the reason is specific — **the
> same symptom had opposite causes, and each of us had the cause the other lacked a way to see.
> A method defect is invisible in the direction of its own bias, and only a differently-biased
> instrument reads it.**

That is not *two reviewers are better than one*. More of either package's own review would not
have found it: this package's check was correct in its convention and blind in its scope, and
more careful convention-checking would have returned clean every time.


---

## 25. Which Findings Carry the Stack Exposure, and Which Do Not — `P07-F-83`

`§23` established that four installed modules outside the declared PATH SET declare on models
this package's findings turn on, and opened `P07-U-30`. It did **not** say *which findings*.
P04 made that move on its own package and got the first clean positive of the exchange — no
installed module outside its declared roots declares on `account.asset`, so its pure asset
findings are on a fully declared stack while its asset–equipment findings are not.

Run here, per model, across three in-generation identities:

| model | modules declaring | outside the declared PATH SET | findings |
|---|---:|---|---|
| **`account.tax.group`** | 2 | **none** | **`P07-F-01`, `P07-F-42`, `P07-F-67`** |
| **`account.tax`** | 9 | **none** | `P07-F-42`, `P07-F-70` |
| **`account.account`** | 13 | **none** | `P07-F-51`, `P07-F-63` |
| **`withholding.tax.cert`** | 3 | **none** | `P07-F-62` |
| **`withholding.tax.cert.line`** | 1 | **none** | `P07-F-62` |
| **`withholding.tax.report`** | 1 | **none** | `P07-F-11` |
| `account.move` | 52 | `account_discount_catalog`, `scgl_product_image`, `scgl_tax_period_date` | `P07-F-03`, `P07-F-57` |
| `account.move.line` | 34 | `scgl_product_image`, `scgl_tax_period_date` | `P07-F-03`, `P07-F-70` |
| `account.payment` | 14 | `account_payment_multi_deduction` | `P07-F-16` |
| `account.payment.register` | 7 | `account_payment_multi_deduction` | `P07-F-52`, `P07-F-16` |

### 25.1 `P07-F-83` — both headline findings are on a fully declared stack

**No installed module outside the declared PATH SET declares on `account.tax.group`,
`account.tax`, `account.account`, `withholding.tax.cert`, `withholding.tax.cert.line` or
`withholding.tax.report`.** So `P07-F-01`, `P07-F-42`, `P07-F-67`, `P07-F-51`, `P07-F-63`,
`P07-F-62` and `P07-F-11` — **including both headline findings** — rest on a stack every member
of which is inside the declared scope and has been read.

**This is the first result in this exchange that made findings safer rather than narrower**, and
it exists only because P04 asked the question in that form. Every prior round widened, refuted
or reclassified something.

### 25.2 The exposed set, named rather than resolved

- **`P07-F-16`, `P07-F-52`** — `account_payment_multi_deduction`. Already `P07-F-80` /
  `P07-U-30`; `P07-F-52` separately discharged at `§21.2` because that module holds zero
  references to its cited surface.
- **`P07-F-03`, `P07-F-57`, `P07-F-70`** — three modules on `account.move`/`account.move.line`.
  One of them, `scgl_tax_period_date`, is already discharged by `P07-F-74` (five copies, one
  tree, and its whole body is a `create` hook writing `tax_period_date`). The other two,
  `account_discount_catalog` and `scgl_product_image`, are **named and not assessed** —
  `P07-U-30` widened to cover them.

`P07-F-57` is the case worth flagging: it was discharged at `§21.2` on **copy identity** and it
now carries a **stack** exposure. The two are different questions, exactly as `REV-M-44` states,
and a finding can be clear on one and open on the other.

### 25.3 The limit binds here as it does for P04

`ir_model_data` records only declarations carrying an XML id. A module can override `create`,
`write` or `_post` on any of these models and appear nowhere in that table. So **"none outside
the declared roots" is a floor on the declared stack, not proof of a complete one.** The
sharpest available statement, in P04's words: **no undeclared module is shown to act on these
models, and none is shown not to.**

`P07-U-30` therefore stays open, and `§25.1` is a **strengthening of confidence, not a
discharge**. No blocker moves and no exit criterion is claimed.

### 25.4 What the exchange produced, stated once

Four times in this package a finding moved: `P07-F-51` split and revealed `P07-F-63`;
`P07-F-42` lost a mechanism and gained a larger consequence; `P07-F-01` lost its trigger and
gained a measured prospective magnitude; `P07-F-16` lost the assumption that it was analysed on
the deployed stack. P04 reports four of its own. **In none was the original sloppy.** Each moved
because a differently-biased instrument asked the next question, and **each replacement was more
decision-relevant than what it replaced.**

That is the honest summary of what this was worth. It is not *"errors were found"* — most of
what changed was **what the findings were about**.


---

## 26. Sweep Unit `1c`, and What It Actually Caught — `P07-F-84`

P04 found `P04-LAW` was **two registers under one name** — statutory sources with letter
suffixes, legal conclusions with digit suffixes — and the digits then colliding with a third,
inherited family holding sources again. Three kinds of thing on one stem. It added sweep unit
`1c` for stems carrying two families with overlapping numbers.

### 26.1 The rule this package did not have, and would have got wrong

P04's fix is the portable half and this package could not have derived it, because **both
colliding families in `P07-F-82` were its own**, so renaming was free. Two of P04's are
**inherited from a prior package**, and renaming them would sever the only link back:

> **Rename what is yours; attribute what is inherited.** A rename that severs lineage is a
> worse defect than the ambiguity it fixes.

Checked here: `DOC-nn` and `P07-D-nn` are both this package's, so `P07-F-82`'s rename was the
right instrument. The inherited families in this package — `EC-nn` from
`SMEPLUS-DR-EXIT-8C-001`, `P04-*`, `P11-G`, `AASR-P07-VETO` — are **attributed and not
renamed**, which was already the practice and is now the stated rule. `REV-M-50`.

### 26.2 Unit `1c` run here: 4 stems flagged, **0 genuine collisions**

| stem | definition-shaped rows in | overlapping suffixes | verdict |
|---|---|---|---|
| `P07-D` | `12`, `22` | `01` | same object — `22 §24.2` quotes the register |
| `P07-F` | `00`, `03`, `07`, `12`, `22` | 12 | same objects — subset restatements |
| `P07-N` | `02`, `03`, `05`, `06`, `08`, `11` | 10 | same objects — negatives stated in both their argument file and the register |
| `P07-U` | `00`, `09`, `12`, `22` | 9 | same objects — consolidated register plus originals |

**The unit is false-positive-prone in this package's shape**, exactly as P04 warned a noisy
check would be: every flag was a family legitimately restated across registers, not two
families sharing a stem. Reported with that verdict rather than as four findings.

### 26.3 `P07-F-84` — but the restatements were stale, and that is the real catch

Asking *why* one identifier has definition-shaped rows in five files led to the check that
mattered: **do the restatements agree with the current figure?** Fifteen did not.

`§7.4`, `§8` and `§8.4` carry before/after tables from earlier rounds whose **"after" column is
itself now superseded** — `P07-F-01` at *"1 of 2 in-generation"*, `P07-F-42` at *"2 of 2"*,
`P07-F-61` at *"2 of 2"*, `P07-F-51` half `b` at *"2 of 2"*, and three population statements at
7 · 5. All were corrected at `§10.4` and `§13`, and **none of those corrections reached the
tables that had stated them**.

**This is the fourth occurrence of the propagation defect in this package** (`REV-E-31`,
`REV-E-49`, `REV-E-58`, now this), and the first found by an **identifier-level** check rather
than a phrase grep — which is why the earlier greps missed it: they searched for wordings, and
these rows state the same figures in a different wording each time.

**Corrected by banner, not by rewrite.** `§7.4` and `§8` now open with a population banner
naming every superseded denominator and stating that `§13` governs. The historical tables stand,
per the practice of leaving a record with its correction attached rather than tidying it away.

### 26.4 The method claim, which is P04's and is the strongest sentence in the exchange

> A stem collision satisfies **every unit** of a package's sweep by construction — both families
> defined, every citation resolving, no malformed table, no stale hash, nothing in Layer 1 — and
> it is plainly wrong to a reader.
>
> **A defect can be invisible to every control a package owns and still be obvious on the page.**

That is stronger than *checks miss things*, and this section is a second instance of it: the
stale restatements passed the orphan check, the structural check, the manifest check and the
scrub, and any reader comparing `§8.4` with `§13` would see the disagreement immediately.


---

## 27. The Qualifier Check — `P07-F-85`

P04 found the counterpart of `§26`'s fifteen: `P04-F-100` narrowed `P04-F-99` in two files and
left it standing in five, each phrased differently — *"the only v18 deployment"*, *"the only
same-generation deployment"*, *"one plan, zero accounts"*, *"latent"*. **Four wordings of one
superseded figure**, which is why four phrase greps missed them. Its rule:

> **When a finding is narrowed, enumerate its citations by identifier and require the qualifier
> on each — never grep for the old wording, because the wording is what varies.**

### 27.1 Run here, and a refinement the first run forced

Eight findings were narrowed in this package: `P07-F-01`, `-F-42`, `-F-16`, `-F-51`, `-F-61`,
`-F-62`, `-F-65`, `-F-20`. Applied literally, the rule reports **162 unqualified citations** of
them.

**That number is not a defect count and publishing it would have been the noisy-check failure.**
Most citations only *name* the identifier — section headings, method notes, cross-references,
`see also` rows. Requiring a qualifier on those is absurd, and a reader shown 162 stops reading
the output.

**The discriminator is whether the citation asserts the narrowed claim.** Re-run over citations
that make a standing-or-figure assertion, outside the register, revision log and this file —
which is where the corrections already live:

**3 assertive unqualified citations, all of `P07-F-01`.**

| location | what it asserted | why it is stale |
|---|---|---|
| `02 §7` | *"it is the highest-severity finding in this package"* | still `S1`, but the **basis** moved realised → prospective |
| `16 §4` | *"empties both statutory registers on a Thai-language install"* | **the refuted trigger** — `P07-F-72` |
| `17 §5` | *"`P07-F-01` is the highest-severity finding"* | same basis change |

**`P07-F-85`.** Fifth occurrence of the propagation defect. `02` is a live model file and is
**corrected in place**; `16` and `17` are records of what a challenge round and the AAS+ review
said at the time, so the correction is **attached and the record left standing**, per the
practice this package has followed throughout.

### 27.2 The rule as adopted, with the refinement stated

> When a finding is narrowed, **enumerate its citations by identifier** — never by wording —
> and require the qualifier on **every citation that asserts the narrowed claim**. Citations
> that merely name the identifier are out of scope, and treating them as in scope produces a
> check nobody reads.

The first half is P04's and is the part that works: it is indifferent to phrasing, which is
precisely the property four phrase greps lacked. The second half is what this package's run
added, and it is the same lesson as `§26.2` — **a check that flags 162 where 3 are real is
worse than no check**, because it trains the reader to skip it.

### 27.3 P04's sharpening of the bias claim, which completes it

`REV-M-47` said a method defect is invisible along your own bias. P04 adds the harder half:

> **A rule is also unusable along your own bias, even when you wrote it down and are running
> it.**

The evidence is symmetric and neither of us could have supplied both halves. P04 wrote *count
the forms* and used it only on the bare/prefixed question it came from; run here it found a
**stem collision** — two registers under one name. This package wrote *compare the difference
against the claim* and used it on **copy** identity; run there it found what a copy-closure does
not cover — the **stack**. **Both times the rule was one party's and the productive use was the
other's.** `REV-M-52`.

That is a stronger claim than *review helps*: it says a rule's author is systematically the
person least able to see its full range, so **a written-down method is not a controlled method
until someone with a different bias runs it.**


---

## 28. Settled Negatives Whose Boundary Has Moved — `P07-F-86`

P04's qualifier check, run with the discriminator this package added, found something neither
of us was looking for: a **settled negative** — *"No sixth database exists under the stricter
method"* — that had been **false for eleven commits**, and that had survived the correction of
the *identical sentence* in its own revision log. Same claim, same session, two locations, one
corrected and one not.

That is a class this package is exposed to more than P04 is, because **this session moved two
boundaries**: the archive population (5 · 4 → 7 · 5 → **15 · 7**) and the source scope (the
declared PATH SET proven not to be the deployed set, `P07-F-68`). **Every negative bounded by
either is a candidate.**

### 28.1 The audit

Seventeen negative-claim rows in `11 §5`. Classified by declared boundary:

| boundary | negatives | status |
|---|---:|---|
| the **declared PATH SET** (`13 §2`) | `P07-N-01`, `-N-02`, `-N-06` | boundary **proven incomplete** by `P07-F-68` — 85 installed modules lie outside it |
| the **storage volume** `/Volumes/iMacSys` | `P07-N-03`, `P07-N-25` | boundary **proven incomplete** by `§13` — `$HOME` holds addon trees and 8 of the 15 database snapshots |
| the Thai module population only | `-N-05`, `-N-08`, `-N-09`, `-N-14` | explicitly narrow and **correctly stated as such** — `P07-N-09` even carries *"this must not be read as SMEsPlus has no tenant"* |
| stated locally in their own section | `-N-10`…`-N-13`, `-N-16`…`-N-24` | unaffected |
| withdrawn | `P07-N-15` | already replaced by `P07-F-37` |

**`P07-F-86` — five of seventeen negatives were bounded by a scope this session subsequently
proved incomplete, and none of them was re-run when the boundary moved.**

The four narrowly-scoped ones are the interesting counter-case: they were written with their
limitation stated in the row itself, and **they are the ones that did not go stale.** A negative
that declares a narrow boundary survives a boundary change; a negative that declares the widest
boundary available at the time does not.

### 28.2 The one that matters, and the one being re-run

- **`P07-N-02`** — *no functional consumer of `tax_period_date`*, bounded to "all three roots".
  The deployed module (`scgl_tax_period_date`) is **outside** those roots (`P07-F-69`).
  **Conclusion survives** because `P07-F-74` proved all five copies one tree — but it survived
  by luck of the code being identical, not because the boundary held.
- **`P07-N-03`** — bounded "declared set and whole volume". The v14 comparison it rests on is
  unaffected by `$HOME`, since it is a claim about the *declared set*.
- **`P07-N-25`** — *"No tenant ORM model exists anywhere on the storage volume"*, bounded to
  **all `.py` files under `/Volumes/iMacSys`**. This is the negative underpinning `P07-F-50`,
  the tenant-boundary finding — *specified at status NEW with zero tenant ORM models anywhere*.
  **`$HOME` was never searched**, and this session has since found addon trees there
  (`bhpro92-addons`, `Desktop/SMEsPlus/…`, `OCC_Odoo18_Simulation_Lab/addons`, `SMEsPlus/…`)
  and eight of the fifteen database snapshots.

A re-run of `P07-N-25` over the corrected root set — `/Volumes/iMacSys` **and** `$HOME`, all
`.py`, with a positive control — **is executing and is not reported here.** `P07-F-50` stands
as published until it returns; if a tenant model exists under `$HOME`, that finding is refuted
and this section will say so.

### 28.3 P04's sharpening of `REV-M-53`, accepted

> In every one of the four instances **the author was actively running the rule at the time**,
> not neglecting it. Neither of us failed to apply our own rule; we applied it to the case that
> generated it and could not see the adjacent case. **That is a claim about scope of
> imagination, not diligence** — which is why more review by the same party does not fix it.

That is the correct word, and it changes what the line recommends: not *try harder with your own
rule*, but **put the rule in different hands**. `REV-M-54`.

P04 also notes the counter-example that keeps this honest: this package's unit `1c` run returned
**4 flags, 0 genuine collisions**, reported as false-positive-prone rather than as four findings.
**A rule can over-reach in someone else's hands too**, and an exchange that only ever confirmed
the other party's rules would be mutual amplification rather than review.


---

## 29. Three Routes to the Residue — and the Two Claims No Route Reaches — `P07-F-87`

P04 ran the boundary audit on its ten negatives: **nine survive, one does not**, and all three of
its exposure analyses — which models have a complete stack, which findings carry exposure, which
negatives carry it — **converge on one module, one model, six findings, one negative.** Three
questions, one answer, which bounds the residue rather than restating it.

Run here, the convergence holds **and then fails in a way that is the more useful half.**

### 29.1 The three routes

| route | clean | exposed |
|---|---|---|
| **models** (`P07-F-83`) | `account.tax.group`, `account.tax`, `account.account`, `withholding.tax.cert(.line)`, `withholding.tax.report` | `account.move`, `account.move.line`, `account.payment(.register)` |
| **findings** (`P07-F-83`) | `P07-F-01`, `-F-42`, `-F-67`, `-F-51`, `-F-63`, `-F-62`, `-F-11` | `P07-F-03`, `-F-57`, `-F-70`, `-F-16`, `-F-52` |
| **negatives** (`P07-F-86`) | the four narrowly-scoped ones | `P07-N-01`, `-N-02`, `-N-06`, `-N-03`, `-N-25` |

**Three of the five superseded negatives — `P07-N-01`, `P07-N-02`, `P07-N-06` — sit on
`account.move` and `account.move.line`: exactly the models the finding route already flagged.**
So for model-scoped claims the routes converge here as they did for P04, and the residue is one
coherent surface rather than three separate ones.

### 29.2 `P07-F-87` — but two negatives are not reachable by any of the three routes

`P07-N-03` and `P07-N-25` **concern no model at all.** *"No tenant ORM model exists anywhere on
the storage volume"* is not a claim about a model; it is a claim about **the absence of a class
of model**, and no analysis that starts from *which modules declare on which models* can bound
it. The same is true of `P07-N-03`, a claim about module presence in a tree.

**This is where the two packages differ, and it is a property of the claims, not of the rigour.**
All ten of P04's negatives are bounded to **modules**, so its model route reached every one. Two
of this package's seventeen are **whole-product** claims, and they are precisely the two the
convergence cannot cover. `P07-F-87`.

**So the residue has two classes:**

1. **Model-scoped residue** — bounded, and the three routes agree on it: `account.move` /
   `account.move.line` / `account.payment(.register)`, three modules, five findings, three
   negatives. Nothing outside it is at risk from the source-scope boundary change.
2. **Whole-product residue** — `P07-N-03` and `P07-N-25`, unbounded by construction, each
   requiring its own re-run. `P07-N-25`'s is still executing.

### 29.3 P04's rule for what to do when a re-run succeeds, adopted

> If it survives, **the surviving statement should be re-declared narrowly** — *"no tenant model
> in modules X, Y, Z"* — or it will rot again at the next boundary change. **Re-running restores
> its truth; re-scoping is what stops it recurring.**

That is the operational form of `REV-M-55` and this package had only the diagnosis. Adopted:
whichever way `P07-N-25` returns, **it will not be re-published in whole-product form.** If it
survives it is re-declared over a named module set; if it is refuted, `P07-F-50` is refuted with
it. `REV-M-56`.

### 29.4 The recommendation, in P04's actionable form

`REV-M-53` said *put the rule in different hands.* P04 sharpens it to the form that can be acted
on:

> **Give your rule to someone whose evidence base differs from yours, and let them run it on
> their own material.** A reviewer reading my package with my rule would have found nothing,
> because they would have applied it where I did.

All four instances in this exchange worked exactly that way. And the counter-example belongs in
the same paragraph, not in a footnote: this package's unit `1c` run returned **four flags, zero
genuine hits**, reported as false-positive-prone. **A rule that only ever confirms is not being
run, it is being cited.** `REV-M-57`.


---

## 30. `P07-N-25` Settled — by the Route That Needs Neither Map Nor Path Set — `P07-F-88`

`§29` called `P07-N-03` and `P07-N-25` **unreachable**, on the ground that a claim about *the
absence of a class of model* cannot be bounded by an analysis starting from which modules
declare on which models. P04 accepted the reasoning and supplied the route it rules out:

> **Enumerate `ir_model` — the deployment's own authoritative model registry — and test for a
> model of that shape across all of it. That needs no module map and no path set**, which is
> exactly what made the leftovers unreachable.

### 30.1 The result

| identity | generation | models in registry | controls (`account.tax` / `res.company`) | **tenant-shaped models** |
|---|---|---:|---|---|
| `a1430edc` | v19 | 1,115 | 1 / 1 | **none** |
| `1f6338ae` | v19 | 749 | 1 / 1 | **none** |
| `66d1b52a` | v19 | 756 | 1 / 1 | **none** |
| `551ab874` | v18 | 944 | 1 / 1 | **none** |
| `45a8e08e` | v16 | 601 | 1 / 1 | **none** |

**4,165 model rows across 5 identities and 3 generations. Zero tenant-shaped models. Controls
fire in every row.**

**`P07-N-25` SURVIVES — and on a stronger basis than the one it was published on.** It was a
source-tree claim bounded to one volume, with `$HOME` never searched. It is now a **deployment**
claim tested against the registry every deployed identity maintains for itself. `P07-F-50` —
the tenant boundary specified at status `NEW` and not built — **stands, strengthened.**

### 30.2 Re-scoped, per the commitment made before the result was known

`REV-M-56` committed this package to not re-publishing `P07-N-25` in whole-product form
whichever way it returned. The re-scoped statement, with P04's two limits carried:

> **`P07-N-25` (re-scoped).** No model whose name denotes a tenant exists in the model registry
> of any of the **five deployed identities examined** — `a1430edc`, `1f6338ae`, `66d1b52a`
> (v19), `551ab874` (v18), `45a8e08e` (v16) — comprising 4,165 model rows.
> **Bounds the estate on this host, not the product**: a model absent here may exist in an
> install not on this host. **Absence of a model is not absence of a behaviour**: a capability
> can live in a field or a method, so this is decisive only for a claim phrased about a missing
> **record type** — which is how `P07-N-25` is phrased, and why the route fits it.

The filesystem walk over both roots is no longer the load-bearing evidence and is superseded as
the primary route; the registry answers the question the walk was asked.

### 30.3 The near-miss check — the inversion on live counter-examples

P04 reports that `stock.scrap`, `account.transfer.model` and a revaluation model **all exist**
in its deployment, so a whole-product phrasing — *"no scrap concept exists"* — **would have been
falsified by them**, and its claims survive only because they were bounded to the asset module.
*The narrow boundary was not modesty; it was what made the claim true.*

Run here against 944 models, asking what a looser phrasing of `P07-N-25` would have hit:

| looser phrasing | would have hit |
|---|---|
| *no tenant construct* | none |
| *no multi-company / isolation construct* | none |
| **no organisational-boundary construct** | **`scgl.multi.approve.organization`** |
| *no subscriber / customer-account construct* | none |

**One near-miss, and it is enough to make the point on this package's own material.**
`scgl.multi.approve.organization` is an approval-workflow grouping, not a security boundary — so
`P07-N-25` as phrased survives, **and a broader phrasing of the same finding would not have.**
`REV-M-58`.

### 30.4 What is still unreachable

`P07-N-03` — *four Thai tax-document modules absent from the declared set* — is a claim about
**module presence in a tree**, not about a record type, so the registry route does not settle
it. It remains in the whole-product residue with its boundary superseded, and it is now the only
member. `P07-U-31` opened to re-run it over the corrected root set.

**So `§29`'s two-class residue narrows to one open item**, and the class is not unreachable in
general — it was unreachable *by the routes this package had*. P04's contribution was not a
better answer to the question but **a route that does not need what made the question hard**,
which is the fourth time in this exchange that the tool has mattered more than the estate.


---

## 31. `P07-F-88` Was Run Over Five Identities of Seven — `REV-E-74`

P04 ran the registry route across **six** identities and reported that **the row where its
control fails is the strongest one**: in a never-transacted v18 install the asset module is not
installed, so `account.asset` is genuinely absent and the control correctly reports absent.

> **Five identities where the control fires and one where it correctly does not is a better
> validation than six where it fires** — it shows the instrument distinguishes a real absence
> from a failed read.

Checking that against `§30`'s run exposed two defects in it.

### 31.1 The denominator, in the section about denominators

**`§30` was run over 5 identities. The census (`§13`) says 7.** `f4a44cce` and `a6664233` were
omitted — the two never-transacted installs, which by this exchange's own repeated result are
the most informative rows available. The figure *4,165 model rows across 5 identities* was
correct as executed and **drawn from a population this package had itself corrected to 7 four
sections earlier.**

### 31.2 The controls were all positive

`§30` used `account.tax` and `res.company`, and **both fire in every row**. A control that fires
everywhere proves the read worked; it **cannot distinguish an instrument that reads correctly
from one that reports `present` for anything asked of it.** P04's run had that discrimination
and this one did not.

### 31.3 Re-run: 7 of 7, with negative controls

| identity | gen | models | `res.company` (+) | `account.tax.unit` (−) | `withholding.tax.cert` (−) | tenant-shaped |
|---|---|---:|---|---|---|---|
| `a1430edc` | v19 | 1,115 | yes | yes | yes | **none** |
| `f4a44cce` | v19 | 633 | yes | yes | yes | **none** |
| `1f6338ae` | v19 | 749 | yes | yes | yes | **none** |
| `66d1b52a` | v19 | 756 | yes | yes | yes | **none** |
| `551ab874` | v18 | 944 | yes | yes | yes | **none** |
| **`a6664233`** | v18 | 335 | yes | **ABSENT** | **ABSENT** | **none** |
| `45a8e08e` | v16 | 601 | yes | yes | yes | **none** |

**7 of 7 identities · 5,133 model rows · 3 generations · zero tenant-shaped models.**

**And the negative controls fire correctly in exactly one row.** `a6664233` is the
never-transacted v18 lab; neither the tax-unit nor the withholding-certificate module is
installed there, and the instrument **reports both absent while still finding `res.company`.**
That is the discrimination `§30` lacked: this instrument distinguishes a real absence from a
failed read, demonstrated rather than assumed.

**`P07-N-25` and `P07-F-50` are unaffected in direction and strengthened in basis** — the
re-scoped statement now reads over **seven** registries, not five.

### 31.4 The never-transacted install, for the third time

`f4a44cce` turned a refutation of `P07-F-63` into a positive control. `a6664233` confirmed
`P07-F-42`'s mechanism where the id ordering differs. Now `a6664233` supplies the negative
control that validates the registry instrument. P04 reports the same pattern on its own side.

> **A never-transacted deployment is the most informative row in the table, and it is the row
> most likely to be dropped** — because it looks empty, and because every question one starts
> with is about what a system does rather than what it ships. Both omissions here were of
> exactly those two identities.

`REV-M-60`.


---

## 32. Disproving a Batch Absence — `P07-F-89`

P04 reproduced `REV-M-60` in its own hands within the hour: it ran six identities against a
census of eight, and **one of the two it dropped was the never-transacted install.** Two
packages, same omission, same victim class, independently — which makes it a property of the
question rather than of either author's sampling.

Its more important report is a failure mode neither package had recorded:

> A **batch harness reported three identities absent that individual runs disprove.** In a loop,
> three returned *no `ir_model` block*; run singly, the same command on the same files returns
> 1,080, 510 and 633 models.
>
> **A run that fails on every row announces itself as a tooling error. A run that fails on three
> of eight rows inside an otherwise-successful table reads as a finding about those three** —
> and here it would have said the two never-transacted installs *have no model registry*, which
> is exactly the shape of an interesting result.

### 32.1 Where that lands here: the absences that validate the instrument

`§31`'s negative controls are **absences inside an otherwise-successful table** — precisely the
shape P04 describes. And they are the highest-stakes absences in this package, because they are
what licenses the claim that the registry instrument distinguishes a real absence from a failed
read. **They had not been disproved by a second route.**

Re-tested, `a6664233`, **single runs, three independent instruments, each with its own control**:

| instrument | result | its control |
|---|---|---|
| `ir_model` | no `account.tax.unit`, no `withholding.tax.cert` | `res.company` **present** |
| `ir_module_module` | **no row at all** for `l10n_th_withholding_tax_cert` | `base` **installed** `18.0.1.3`; 41 modules installed; `account` **installed** |
| archive TOC | `account_tax_unit` **0**, `withholding_tax_cert` **0** | `account_move_line` **1** |

**Three instruments, three positive controls firing, three absences agreeing.** The negative
controls are genuine, and `§31`'s discrimination claim stands. `P07-F-89`.

**One caveat found while doing it, stated rather than smoothed:** `account.tax.unit` is absent
from that registry although the `account` module **is** installed there, whereas the other v18
identity has both. Why the model is absent under an installed parent module is **not
established**, and it is **not needed** — the control's purpose is to show the instrument can
report absent, which three instruments agree it correctly does. Recorded so no reader infers an
explanation this package has not given.

### 32.2 A batch absence from `§25`, likewise disproved singly

`§25` reported *"none — fully declared stack"* for six models, computed in a batch across
identities. One spot-checked by single run on `66d1b52a`, with harness controls printed:

- `ir_model_data` **62,445 rows**, `ir_model_fields` **16,009**, `ir_ui_view` **3,516** — all
  three blocks read, so no silent harness failure.
- Modules declaring on `account.tax.group`: **`account`, `point_of_sale`** — both inside the
  declared PATH SET, **none outside**.
- Positive control, same query for `account.move`: **75 modules**.

The `§25` absence is genuine on that row.

### 32.3 The rule, adopted

> **Always disprove a batch absence with a single run before it becomes a row** — and print the
> harness's own read counts beside the result, so a missing block is visible as a missing block
> rather than as an empty one.

**And the asymmetry P04 identified is the part that makes it urgent:** a *uniform* failure
announces itself as tooling; a *partial* failure inside a working table **reads as a finding**,
and it will preferentially look like a finding about whichever rows are unusual — which, in both
these packages, means the never-transacted installs. **The two failure modes this exchange has
been recording all session — a null that is self-consistent, and a control that cannot fail —
have a third sibling: a null that is selective.** `REV-M-62`.


---

## 33. The Census Declared Its Roots and Not Its Exclusions — `P07-F-90`

P04's host census landed at **39 artefacts** — 27 `PGDMP` plus 12 zip-borne — against this
package's **15**. It also measured, rather than argued, the symlink point it owed: **zero
artefacts reached via `/Volumes/iMac`**, confirming that `find`/`os.walk` do not traverse it and
that the earlier 57-vs-15 inflation came from passing it as a *starting root*.

The gap between 39 and 15 is not a difference of diligence. **It is two undeclared narrowings in
this package's census script, and `§13.1` declared everything except them.**

### 33.1 What `§13.1` declared, and what it did not

`§13.1` published: roots (`$HOME` + every `/Volumes` entry), no extension filter, two signatures,
a 1 MB size floor, identity keyed on `database.uuid`, generation from `ir_module_module`. What
it did **not** publish:

**1. Eight directory exclusions.** The walk carried
`{'.git','node_modules','.venv','__pycache__','Library','.Trash','.cache','.npm','.cargo'}`.
**`Library` is the material one** — `~/Library/CloudStorage/` holds the Google Drive trees that
this package's own module enumeration (`§19`) reported dozens of module copies from. A census
that declares its roots and silently prunes a subtree of one of them **has declared a boundary
it did not use**.

**2. A narrower zip signature.** This package accepted a zip only if it contained a member
literally named `dump.sql`. P04's accepted any `.sql` member **or** a `manifest.json`, and found
two exports carrying `dump.sql` with **no** manifest — a different export shape. Mine would
catch those; mine would **miss** any export whose payload is named otherwise. **Two signatures
were declared and the ZIP one was tighter than stated.**

**`P07-F-90` — `§13`'s "15 snapshots · 7 identities · 3 generations" is a floor, not a census.**
It was published as a finished number with a declared root set, and the root set was declared
while the exclusions were not. This is `P07-F-79`'s defect — *the correction of an under-scoped
check computed over an under-scoped population* — recurring at the next level out, and it is the
**third** undeclared narrowing this package has had to record after publishing the thing it
narrowed.

### 33.2 What is being measured, and what is not claimed

A re-run over the excluded `~/Library` subtree, same size floor, with the **widened** zip
signature, **is executing and its result is not reported here.** No number in `§13` is amended
until it returns.

**No finding moves either way.** Every database-derived finding in this package is bounded to a
**named identity**, and all seven named identities were keyed on `database.uuid` and read. What
a wider census can add is identities, not corrections to the eight — P04 states the same for its
own: *"the census settles the artefact question and leaves the identity question exactly where
it was."*

The candidate names P04 reports as newly visible and never keyed by either package —
`iErpOCC`, `iSCErP`, `iSMeO2C`, `iSMEs182`, `iMSCG` ×2, `odoo_cff_golive`, two packaging
exports, two archives inside a messaging app's media store — are **not counted here**. Turning a
candidate list into a census is the error `§12.6` exists to record.

### 33.3 P04's disproof, and the mechanism this package could not establish

P04 ran `§32`'s three-instrument method on its own licensing absence and got the stronger
result:

| | this package (`a6664233`) | P04 (`96548e18`) |
|---|---|---|
| `ir_model` | model absent | model absent |
| `ir_module_module` | **no row at all** | row present, state **`uninstalled`** |
| archive | table absent | blocks absent |

**A missing row leaves *why* undetermined; a row reading `uninstalled` establishes it.** P04's
identity is not an incomplete capture but a **complete capture of an install that chose not to
run the module** — the *not deployed versus not available* distinction from its `P04-F-97`,
which is a stronger licence for a negative control than absence alone. This package's caveat at
`§32.1` stands as written: not established, and not needed.

### 33.4 Where the return went, stated as P04 put it

> **The last estate fact either of us found was `idemo18_uat`, and everything since has been
> about how we know things.**

That is the accurate description. The checks did change what several findings were *about* —
`P07-F-42` lost a mechanism and gained a larger consequence, `P07-F-01` lost its trigger and
gained a measured prospective magnitude, `P07-F-16` lost the assumption that it was analysed on
the deployed stack — but **no new defect in the estate has been found since that database**, and
this section is one more instance of the pattern rather than an exception to it. `REV-M-63`.


---

## 34. The Narrowings Live in the Error Handling and the Branch Nobody Ran — `P07-F-91`

P04 asked `§33`'s question of its own census and found two, reporting the honest headline first:
**neither moved the number.** Its `2>/dev/null` had silently dropped unreadable directories and
no count had ever been taken — measured, **141 stderr entries against 1,070,459 directories**,
all macOS privacy containers. And its gzip branch decompressed 200 bytes and matched one
string, so **a gzipped custom-format archive, whose payload begins `PGDMP` and contains no such
text, would have been missed entirely**; re-tested over all 72 gzip archives with a control that
fires on a known dump after gzipping it, none is a database.

> **A script's declared parameters are the ones its author was thinking about; the narrowings
> live in the error handling, the defaults, and the branch nobody exercised.**

Both are in this package's census, and **the second is worse here than there.**

### 34.1 The suppressed walk errors

`fullcensus.py` carried `os.walk(r, onerror=lambda e: None)`. Identical defect, identical
omission: **no count was ever taken.** A measurement is executing.

### 34.2 The signature set was declared at three and executed at two — `P07-F-91`

`§10.7` published the signature set as **`PGDMP`, ZIP-containing-`dump.sql`, and
"gzip-inspected-and-excluded"**. `§13.1` published it as **two** signatures. The census script
has **no gzip branch at all.**

So the third signature was **declared in one section and absent from the census that the other
section published** — and the inspection it refers to covered **two files** in an earlier,
narrower sweep, not the declared roots. That is worse than P04's narrow gzip test: theirs ran
and was too tight; **mine was described and never ran over the census population.** It is this
package's own `declared-pattern-not-run` defect, recorded in its first week, recurring in the
section that declares the method.

### 34.3 The control, built before the result

Per `REV-M-61`, a positive control that can distinguish a working branch from an absent one —
a known custom-format dump, gzipped, then tested by the same code:

| | result |
|---|---|
| control: 3,821,347-byte `PGDMP` dump → 1,615,667-byte gzip | first 5 decompressed bytes `PGDMP` |
| **`PGDMP`-in-gzip branch** | **fires** |
| `"PostgreSQL database dump"` text present | **no** |
| negative control: a genuine source tarball | neither signature — correctly not a dump |

**This is exactly P04's case, reproduced:** a gzipped custom-format dump carries no identifying
text, so a text-only gzip test misses it and an absent branch misses it doubly. The two-signature
test catches it, and the negative control shows it does not simply say yes.

A re-run over every gzip archive ≥ 1 MB under the declared roots, both signatures, **is
executing and is not reported here.**

### 34.4 P04's asymmetry, which is the useful part and is not comparative

> Mine dropped directories the OS refuses to anyone; yours dropped **a subtree your own module
> enumeration had already drawn dozens of copies from.** Mine could not have contained the
> evidence; yours demonstrably did contain evidence you had used.

That is correct and it is the right way to rank the two. **A narrowing that excludes a place you
have already found things is a different severity from one that excludes a place nothing could
be** — and this package's `Library` exclusion is the first kind. `REV-M-65`.

### 34.5 The constraint accepted for whatever the re-runs return

P04 published **39 as a file count and refused to state an identity count**, and asks that this
package hold the same line:

> **`15 · 7` should not be replaced by a new pair unless every artefact behind it is
> uuid-keyed.**

Accepted and recorded before the results are known, as `REV-M-56` was. If the re-runs surface
artefacts, **the file count may move and the identity count may not** — an identity enters
`§13.3` only by `database.uuid` read from `ir_config_parameter`. Anything else is a candidate
list, and `§12.6` exists because this package once nearly published one.

**And P04's summary of its own outcome is the one to carry:** *the number did not move and the
basis did.* That is the most common honest result of this entire exchange, and it deserves
saying plainly rather than reporting as a clean bill.


---

## 35. The Excluded Subtree Held More Artefacts Than the Census Found — `P07-F-92`

The `~/Library` re-run promised at `§33.2` has returned.

**36 database artefacts under the subtree the published census silently pruned** — against
**15** in the census itself. **The undeclared exclusion dropped more than the declared scan
found.**

| | artefacts |
|---|---:|
| published census (`§13`), `$HOME` + `/Volumes`, `Library` pruned | 15 |
| **the pruned `~/Library` subtree alone** | **36** |
| **floor, by file** | **≥ 51** |

They are disjoint by construction — the census excluded exactly the subtree this run covers.

Almost all sit under `~/Library/CloudStorage/GoogleDrive-*/` — the two Drive accounts whose
module trees this package's own `§19` enumeration had already read dozens of copies from. One,
`premiumflexiblepackaging-pfp-odoo-staging-…`, is under `~/Library/Mobile Documents/`, and is
one of the artefacts P04 named as newly visible in its census: **the two sweeps agree on a file
that mine could not see.**

### 35.1 What moves, and what does not — the constraint held

`REV-M-66` committed this package, before the result was known, to not replacing `15 · 7` with a
new pair unless every artefact behind it is uuid-keyed. The result is reported under that
constraint:

- **The file count is superseded.** `§13`'s **15** is a floor; the measured floor is **≥ 51**.
- **The identity count is unchanged at 7** — *keyed on `database.uuid` and read*. **None of the
  36 has been keyed.** They are artefacts, not identities, and `§10.1` is the reason: two files
  named `iEVING` were two different databases and four files named `iTEST02` were one.
- **Population state: OPEN**, exactly as P04 published its own — *"the census settles the
  artefact question and leaves the identity question where it was."*

**`P07-F-92`.** The census figure of `15 · 7 · 3` published at `§13` as a finished number, and
re-marked a floor at `§33`, is now **measured** to be a floor by at least 36 artefacts.

### 35.2 No finding moves, and why that is a statement about the findings

Every database-derived finding in this package is bounded to a **named** identity — `a1430edc`,
`f4a44cce`, `1f6338ae`, `66d1b52a`, `551ab874`, `a6664233`, `45a8e08e` — all seven keyed and
read. **A wider census can add identities; it cannot alter what was read in these seven.** The
denominators that would move are the *prevalence* figures, and they are already stated as
in-generation ratios over named identities rather than as claims about the estate.

**What this does change is the reading of `P07-F-01`'s prevalence.** *1 of 4 in-generation
identities* is now explicitly *1 of 4 **examined***, with an open population behind it. That
was true when written and is now visibly true, which is the difference between a bounded claim
and a lucky one.

### 35.3 The severity ranking P04 gave was right, and this measures it

> Mine could not have contained the evidence; yours demonstrably did contain evidence you had
> used.

**Measured: 36 artefacts, in a subtree this package had already mined for module copies.** P04's
141 suppressed directories were OS privacy containers holding none. **A narrowing that excludes
a place you have already found things is a different severity from one that excludes a place
nothing could be**, and the ratio here is 36 to 0.

### 35.4 Not done, and named

The 36 are **not keyed**, **not read**, and **not counted as identities**. Keying them is a
`NOT YET READ` item, not a defect in what is published — but it is now the largest single
unexamined evidence set this package has named. **`P07-U-32` opened.**

The gzip re-run of `§34.3` is still executing and is separately unreported.


---

## 36. The 36 Was 22 — the Two Sweeps Reconcile Exactly — `P07-F-93`

P04 declined to adopt `§35`'s figure and asked for **the path list, not the count** — the
declared-halves rule both packages have been applying: *a joint tally is executable by neither
party; two declared halves, each executed by its owner.* It reported **22** in the same subtree
and had tested three candidate causes of the gap, each with a firing control, finding **none**.

**It was right to refuse, and the gap is entirely this package's over-count.**

### 36.1 The reconciliation

`§35`'s scan accepted a zip if it contained a member named `dump.sql`, **or any member ending
`.sql`**, or a `manifest.json`. Re-classified by *why each matched*:

| matched because | count | is it a database? |
|---|---:|---|
| `PGDMP` magic bytes | 10 | **yes** |
| zip containing `dump.sql` | 12 | **yes** |
| zip containing some other `.sql` member | **14** | **no** |
| `manifest.json` clause alone | **0** | — |

**Strict criterion — `PGDMP` magic or a zip containing `dump.sql` — gives 22. P04 reports 22.**
Two independently-written, independently-bounded sweeps agree **exactly**.

**The 14 are source-code archives.** `odoo-16.0.zip`, `odoo-19.0.zip`,
`web_and_web_enterprise.zip`, `01 ACCOUNT.zip`, `02 OTHER.zip` and similar — each matched on a
**0 KB `neutralize.sql`** or an equivalent data file shipped *inside a module*. None is a
database, and one of them is a zip of this package's own declared source set.

**`P07-F-93` — `§35`'s 36 is corrected to 22.** The floor by file becomes **15 + 22 = 37**, not
51. This is the first correction in this exchange that **reduces** one of this package's
numbers, and it is worth marking as such: every previous one widened a population or weakened a
claim.

**A hypothesis of this package's own was also wrong and the data says so.** `§36`'s first
suspicion was the `manifest.json` clause; it contributed **zero**. The over-inclusion was
entirely the any-`.sql` clause. Recorded because the wrong guess was made in the same breath as
the right method.

### 36.2 What survives unchanged

- **The severity ranking is unaffected: 22 against 0.** P04's suppressed directories held no
  artefacts; this package's `Library` exclusion held 22 real ones, in a subtree it had already
  mined. `REV-M-68` stands with a corrected numerator.
- **The identity position is unchanged**, because `REV-M-66` forbade converting artefacts into
  identities in the first place: **7 keyed and read, population OPEN**, and `P07-U-32` now names
  **22** unkeyed artefacts rather than 36.
- **`premiumflexiblepackaging-pfp-odoo-staging-…` still cross-validates.** It is in P04's 39 and
  in this package's 22 — **the only artefact either census has that two independently-bounded
  sweeps both found**, and the strict criterion keeps it.

### 36.3 The two remaining measurements from `§34`, now returned

**Suppressed walk errors: 996**, against 3,527,728 directories traversed — `Library` 504,
permission-denied 269, operation-not-permitted 216, `Trash` 6, other 1. Every sampled entry is
an OS privacy container (`Photos Library.photoslibrary`, `Application Support/CloudDocs`,
`com.apple.TCC`, `CallHistoryTransactions`). **The number now exists to judge against, which is
the whole point of `P04-F-127`'s finding** — it was never that the directories mattered, it was
that no count had been taken.

**Gzip: 481 archives ≥ 1 MB under the declared roots, tested on 4,096 decompressed bytes against
both signatures. Database dumps found: 0.** The only two hits are **this package's own control
file**, written minutes earlier and reached twice via the `/Volumes/iMac` mirror — so the branch
**fires on a real gzipped custom-format dump and on nothing else present**. The missing gzip
branch (`P07-F-91`) cost the census **nothing**, exactly as P04's too-tight one cost it nothing.

### 36.4 The rule that produced this, stated once

P04 refused to adopt a peer's count and asked for paths. **That is the only reason this is
resolved rather than recorded as an unexplained disagreement.** Had it adopted 36, both packages
would now carry a wrong number with two-party corroboration behind it — which is worse than
either carrying it alone.

> **Corroboration between two parties multiplies whatever it is applied to. Applied to a count,
> it multiplies the count's error; applied to a method, it exposes it.** The declared-halves
> rule is what forces the second.

`REV-M-69`.


---

## 37. The Shape, Not the Name — 22 Becomes 20 — `P07-F-94`

P04 corrected its own method statement rather than its number: its census predicate was
**`dump.sql` by name**, not the looser clause it had twice published, and it determined that
**behaviourally rather than from memory**. The consequence for this package is the sentence it
drew from its two withdrawals:

> **The discriminator that separates a backup from source is `dump.sql` at the archive ROOT with
> `manifest.json` beside it** — the shape the product actually writes. **Neither of our published
> clauses said so, and a name-anywhere test cannot get there, however tight the name.**

`§36` tightened from *any `.sql`* to *a member named `dump.sql`*. **P04 was already at that
tightness and was still admitting two source archives.** Tested here, so is this package — and
**the same two.**

### 37.1 The twelve zip hits, by shape

| archive | root `dump.sql` | root `manifest.json` | verdict |
|---|---|---|---|
| `iSMEs182`, `iSMeO2C`, `iMSCG` ×2, `T805efaplus`, `pankhamhom`, two uuid-named | yes | yes | **backup shape — 8** |
| two `premiumflexiblepackaging-*` | yes | **no** | root dump, **different export shape — 2** |
| **`CFF.zip`** | **no** | no | **nested only — source archive** |
| **`docker-compose-magento.zip`** | **no** | no | **nested only — source archive** |

**`CFF.zip`'s `dump.sql` is sample data inside a Gantt charting library**
(`gantt_7.0.11_commercial/samples/common/dump.sql`). **`docker-compose-magento.zip`'s is a
Magento acceptance-test fixture** (`dev/tests/acceptance/tests/_data/dump.sql`). Both are
exactly what P04 described, found independently here by applying its structural test — **the
same two archives, reached from the other side.**

### 37.2 `P07-F-94` — the corrected composition

| | |
|---|---:|
| `PGDMP` magic | 10 |
| zip, backup shape (root `dump.sql` + root `manifest.json`) | 8 |
| zip, root `dump.sql`, no manifest — **different export shape, counted** | 2 |
| **total** | **20** |
| excluded: nested-only `dump.sql` inside source archives | 2 |

**22 → 20.** The two `premiumflexiblepackaging` exports are **kept**, following P04's own
reasoning that excluding an unfamiliar export shape would be the narrow-pattern error it has
recorded twice — but they are now **declared as a distinct shape** rather than counted silently
alongside the rest.

**This package's figure has moved 36 → 22 → 20, downward each time, and each time because a
peer named a sharper discriminator than the one it was using.** The first correction removed a
clause that was too loose; this one removes a *test class* that cannot express the distinction
at all. **A name test asks what a file is called; a shape test asks what wrote it.**

### 37.3 What this does not change

**Nothing downstream.** The 20 are unkeyed artefacts; `P07-U-32` is renumbered from 22 to 20;
the identity position is untouched — **7 keyed on `database.uuid` and read, population OPEN** —
because `REV-M-66` forbade converting artefacts into identities before any of these numbers
existed. **The severity ranking is unaffected: 20 against 0.**

The backup-shape names are worth recording because they cross-validate P04's list of newly
visible identities: `iSMEs182`, `iSMeO2C`, `iMSCG` ×2, `pankhamhom`. **Named, not counted as
identities**, and unkeyed.

### 37.4 The inverse of `REV-M-69`, which P04 supplied and I would not have predicted

`REV-M-69` said corroboration applied to a count multiplies its error. P04 reports the inverse
running the same day: **its re-run of my number exposed a false description of its own
predicate** — a description nothing in its package contradicted, and under which **every count
it produced was right.**

> **The corroboration exposed a method error while confirming the number it produced.**

That is the case the rule predicts and the one neither of us would have believed in advance: a
package can be arithmetically correct throughout and still be describing a different instrument
than the one it ran. **Only an outside party asking *why* a number differs reaches it**, because
inside the package there is nothing to disagree with. `REV-M-70`.

### 37.5 The census thread, closed

Four tooling defects between the two packages — a missing gzip branch, a too-tight gzip test, an
undeclared directory exclusion, suppressed walk errors — and **four nil results**: 996 errors all
privacy containers, 481 gzip archives with 0 databases, and P04's 141 and 72 likewise. **Nothing
was found; everything is now bounded.** That is the honest summary, and it is P04's phrasing.


---

## 38. The Shape Test Applied to the Census Itself — Thread Closed — `P07-F-95`

P04 reported that it had withdrawn its two source archives **by hand, on inspection**, and had
never run the test across the other ten. Run systematically, its composition became executable
without moving its number: 27 `PGDMP` + 10 backup-shape + 2 declared-shape + 2 withdrawn = 39.

**The same gap was here.** `§37` applied the shape test to the `~/Library` subtree and **not to
`§13`'s own zip candidates**, which had been admitted on the same name-based clause the section
had just rejected.

### 38.1 Run

| archive | root `dump.sql` | root `manifest.json` | verdict |
|---|---|---|---|
| `iEVING_2026-03-30_02-30-18.zip` | yes | yes | **backup shape** |
| `BK12MAY26_2026-08-03_11-28-04.zip` | yes | yes | **backup shape** |
| **control** — `odoo-19.0.zip` | no | no | **correctly rejected** |

The other 13 members of `§13` are `PGDMP` by magic bytes, where the magic **is** the shape.

**`P07-F-95` — `§13`'s 15 stands, and its basis is replaced.** The two zip members were admitted
by a name clause and are now licensed by an executable predicate, with a control that rejects a
known source archive. **Fourth instance in this thread of a count surviving while its basis was
replaced** — after 141 exclusions enumerated, 72 gzip candidates tested, and P04's 12 archives
re-run.

### 38.2 The census, finally composed

| scope | `PGDMP` | backup shape | declared shape | rejected | total |
|---|---:|---:|---:|---:|---:|
| `§13` census (roots as declared, `Library` pruned) | 13 | 2 | 0 | 0 | **15** |
| `~/Library` subtree (the undeclared exclusion) | 10 | 8 | 2 | 2 | **20** |
| **floor by file** | 23 | 10 | 2 | 4 | **35** |

**35, not 37** — `§36` computed the floor as 15 + 22 before `§37` corrected 22 to 20, and the
arithmetic was carried forward one section too far. Corrected here.

**Identity position unchanged and unchanged by anything in this thread: 7 keyed on
`database.uuid` and read, population OPEN, 20 unkeyed artefacts named at `P07-U-32`.**

### 38.3 What the two sweeps actually agreed on

P04's closing observation is the one this file should end on, because it is a claim about the
kind of agreement rather than the amount of it:

> Everything else we agreed about was a **fact** — a database, a count, a model registry. This
> was agreement about a **test**: proposed there, applied here, returning **the same two
> rejections out of two different candidate sets**. **A fact can be agreed by coincidence; a
> test agreeing on rejections neither party had shown the other cannot.**

`CFF.zip` and `docker-compose-magento.zip` were rejected on both sides by the same predicate,
from candidate sets neither package had exchanged. That is the only discriminator-level
agreement in the exchange.

### 38.4 The census thread, closed

**36 → 22 → 20 here; 39 → 39 → 39 there.** Downward or steady at every step, each step forced
by a sharper discriminator from the other party. **Four tooling defects between the two
packages — a missing gzip branch, a too-tight gzip test, an undeclared directory exclusion,
suppressed walk errors — and four nil results: 996 errors all privacy containers, 481 gzip
archives with 0 databases, and 141 and 72 on the other side.**

**Nothing was found. Everything is now bounded.** That is not a disappointing outcome for a
census; it is what a census is for.

**And `REV-M-70`'s credit is joint, as P04 records it:** it supplied the instance — a false
description of its own predicate, surviving because every count it produced was right — and
this package supplied the account of why that is the interesting case. Neither half is worth
much alone. *A self-consistent package has no internal signal for a wrong self-description, and
the number being right is exactly what removes the last reason to look.*

**Both packages are terminal on this thread. Neither will initiate again.**


---

## 39. The Complement — What the Census Could Have Missed — `P07-F-96`

P04's closing result names a gap **every re-audit in this thread shared, on both sides**:

> Every re-audit either of us ran tested what a census **ADMITTED**. **None tested what it could
> have MISSED.** A backup whose payload carried any name other than `dump.sql` — with a root
> `manifest.json` beside it — **was never a candidate**, and no shape test run afterwards could
> reach it, because a shape test only looks at what was already recorded.

And the asymmetry that makes it structural rather than an oversight:

> **Tightening a predicate can only ever shrink what it admits.** So all three of its earlier
> re-audits could confirm the census was **not too loose**, and **not one of them could show it
> was not too narrow.**
> **A discriminator validates the set it accepted; only its complement validates the set it
> never saw.**

Its run returned **zero**. The same test was unrun here.

### 39.1 Both controls, built before the result

**Control 1 — the test must exclude a known backup.** `iEVING_2026-03-30_02-30-18.zip` carries
root `manifest.json` **and** root `dump.sql`; the inverse predicate (*manifest and NOT dump*)
does **not** fire. Correctly excluded from the candidate set.

**Control 2 — the test must be able to fire at all.** A synthesised archive with root
`manifest.json` and a payload named **`backup.sql`** instead of `dump.sql`: the inverse
predicate **fires**, and the original census clause **would have missed it** (`dump.sql`
present = false).

**So the class is real, constructible, and reachable by this test — and was unreachable by every
predicate this package published.** That is the point: `§37` and `§38` tightened the test and
`§36` loosened then re-tightened it, and **none of those three operations could have surfaced a
single member of this class.**

### 39.2 The run

A sweep of every `.zip` ≥ 1 MB under `$HOME` and every `/Volumes` entry — including `~/Library`,
excluding the `/Volumes/iMac` mirror measured at zero in `§36` — testing for the inverse shape,
**is executing and its result is not reported here.** `P07-F-96` is registered with the method,
the controls and the population; the finding is completed when the sweep returns.

**No number in `§38` is amended in the meantime**, and the identity position is untouched
regardless of the outcome: **7 keyed on `database.uuid` and read, population OPEN**.

### 39.2a Two controls, not one — and P04's own complement test had half — `REV-M-76`

P04 reports that what it shipped with its complement result was an **exclusion** control only:
a known backup shows both members and is correctly *not* flagged. **That proves the predicate
does not misfire. It says nothing about whether it fires at all** — which is the
control-that-cannot-fail pattern, a defect P04 had itself recorded **one commit earlier**.

Re-run with the construction from `§39.1`, its zero is now controlled in both directions: the
inverse predicate **fires** on a synthesised archive, its own original clause **misses** the
same artefact, and a real backup is **correctly excluded**. Conclusion unchanged; evidentiary
standing changed.

**The generalisation, which P04 attributes to this package's construction and this package
attributes to P04 having found the gap in its own published result:**

> An **exclusion** control and a **firing** control are different instruments, and a negative
> needs both. Proving a predicate does not misfire is worthless without proving it **can** fire
> — and the second is usually only obtainable by **constructing an instance that does not exist
> in the population**, which is precisely why it gets skipped.

`REV-M-61` said *pair every positive control with a negative one*. This is the sharper form:
when the result **is** a zero, the firing control is not an optional companion — **it is the
only thing standing between the zero and a broken test**, and it generally has to be built
rather than found.

**Fifth instance in this thread of a rule recorded and not applied in the adjacent case**, and
it is P04's own: it had the control-that-cannot-fail written down and shipped a finding whose
entire content is a zero, guarded on one side.

### 39.3 The mirror-image gap, and what it actually is

P04 identifies this package's version, and it is exact:

> Your closing round had the same gap in mirror image — **the shape test run on one subtree and
> not on your own earlier candidates.** Both are the same shape: **the test was applied where
> the author was already looking.**

That is `REV-M-53` in its narrowest form. The earlier statements were about a rule's **range** —
*a rule is unusable along your own bias even when you wrote it down and are running it.* This is
about the **set the rule is pointed at**, which is a smaller and more mechanical thing and
therefore easier to guard: **when a new discriminator is adopted, enumerate every set the old
one produced and re-run it on each, including its complement.** `REV-M-74`.

### 39.4 Where the last defect came from

P04's closing observation about the thread's final correction:

> Your arithmetic catch is the right note for you to end on — `15 + 22` carried one section past
> the correction to 20, floor 35 not 37. **Caught inside your own re-run, not by me. The last
> defect in this thread was found by a package auditing itself**, which is the only outcome that
> suggests the discipline outlives the exchange.

Recorded as stated, including that it is the exception rather than the pattern: of the defects
in this thread, that one and very few others were self-caught. **The discipline was built by the
exchange; whether it survives without one is not established by a single instance**, and this
package will not claim more than that. `REV-M-75`.
