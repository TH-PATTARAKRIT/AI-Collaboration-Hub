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
| `iEVING` 2026-07-23 | v1.14 | READS | not examined — different product line |

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

### 4.5 `P07-F-51` — REFINED, and partly refuted

The finding said the third-party withholding path is *inert on a fresh install of the
declared set*, because no account carries the withholding flag and the Thai chart template
has no column for it. In this database **3 of 586 accounts carry `wt_account = true`**, and
`account_withholding_tax` holds **10 rows**.

So the path is **not** inert here. The finding is corrected to: *the shipped localisation
provisions nothing, and the path requires a manual configuration step the localisation does
not perform.* This deployment shows an operator performed it. The "inert as shipped" half
stands; the "cannot work" implication does not, and was never stated but could be read in.

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
  product line).
- No transaction-scale evidence exists for any finding. Six moves cannot support a claim
  about operational behaviour, and none is made.
- The database was read table-at-a-time with no restore, so no join was executed by a server;
  every cross-table statement above was assembled by reading two extracts. That is weaker
  than a query and is declared as such.

## 7. Four Databases, Not One — One Finding Constrained, One Strengthened

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

**Read this table together with §3.1.** The two deployments where the defect fires are the two
a stock client cannot open. Anyone testing this finding with default tooling sees only the
two that work.

### 7.2 `P07-F-42` holds in EVERY database examined

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
| `P07-F-01` | verified, asserted universal | verified, **1 of 3 database identities** (2 of 4 snapshots, both the same identity — §7.4); universality claim withdrawn |
| `P07-F-42` | verified in 1 database | verified in **4 of 4**, 6 company sets |
| `P07-F-15` | source-derived | supported: group naming varies between deployments (`TAX n%` vs `WHT n%`) |
| §6 count | "three dumps" | five databases in nine files; four examined |
| `P07-U-27` | four unexamined | one unexamined (`iEVING`, different product line) |

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
| **Database identities examined** | **3 of 3** |
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
| `account_tax_unit` rows | 0 | 0 | 0 | 0 | **`P07-F-61` HOLDS** — 3 of 3 identities |
| lines carrying `tax_period_date` | 0 of 23 | 0 of 32 | **18,197 of 447,384** | 0 of 563 | **`P07-F-03` CONSTRAINED** |

### 8.1 `P07-F-60` is REFUTED — `REV-E-29`

It read: *withholding is configured and **no statutory certificate has ever been issued**.*
`iSMEs` holds **5,201** certificates and `BK12MAY26` holds one. Two of three identities issue
them; one issues them at scale. **Withdrawn.**

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

### 8.3 The scoping error underneath all three — `REV-E-30`

`iTEST02` has **23 move lines**. `iSMEs` has **447,384**. This session built its entire
runtime section on the smallest database available and generalised from it, because it was the
one inside the declared PATH SET and was therefore opened first. Convenience of location
determined the evidence base.

That is the same defect as `REV-E-26` (generalising `P07-F-01` from `n = 1`) and
`REV-E-28` (snapshots counted as identities), now for the third time in one file — and this
time it cost a published finding rather than a qualifier. The corrective is not "open more
databases" but **rank them before choosing**: `iSMEs` is four orders of magnitude larger and
should have been read first.

`iSMEs` is now the reference population for any claim about operational behaviour in this
package. Nothing in §4 or §7 was derived from it except the group-name comparison at §7.1,
which is why those sections are configuration claims and are labelled as such.

### 8.4 Net

| Finding | Before §8 | After |
|---|---|---|
| `P07-F-60` | new finding, 1 snapshot | **WITHDRAWN**; replaced by `P07-F-62`, which is stronger |
| `P07-F-61` | 1 snapshot | **holds**, 3 of 3 identities |
| `P07-F-03` | "populated nowhere" | source finding unchanged; population claim bounded, and the 4.1% supports the mechanism |
| `P07-F-62` | — | **new**: 5,201 certificates carry a correct income-type taxonomy the statutory export ignores |

Client version for every row above: `postgresql@18` `pg_restore 18.6`. Generations opened:
four snapshots, three identities. Not opened: `iEVING` (`P07-U-27`).
