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
| Tool | `postgresql@18` `pg_restore 18.6`, table-at-a-time extraction; **no server, no restore, read-only** |
| Population | Small: 6 `account_move`, 23 `account_move_line`, 586 `account_account`, 19 `account_tax` |
| Relationship to other evidence | **Not** the database named in any runtime capture referenced elsewhere in the programme |

**What this scope supports and does not support.** Findings about *configuration and schema*
— what the chart, the taxes, the groups and the return types actually contain — are
well-supported: those tables are fully populated. Findings about *transaction volume* are
not: six moves is a configuration snapshot, not an operational one. Every result below is
labelled accordingly.

## 4. Results

### 4.1 `P07-F-01` — VERIFIED. It was the package's headline inference; it is now fact.

The predicate at `smesplus_account_reports/models/account_generic_tax_report.py:88` admits a
row only if the tax group's raw stored name equals `{'en_US': 'VAT 7%'}`. The deployed value
is:

    id 5 | {"en_US": "VAT 7%", "th_TH": "ภาษีมูลค่าเพิ่ม 7%"}

A two-key mapping. The equality is **false for every row**, so in this database both SMEsPlus
statutory VAT registers return **no data at all**, silently.

This was reached independently by two adversarial reviewers as a source-derived escalation
and carried at `SRC-CHAL`. It is now **verified against a deployed database of the declared
generation**. All five tax groups carry Thai translations; the condition is not exceptional,
it is the shipped state of a Thai deployment.

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

- The other three dumps on this host were **not** examined. Whether any is a Thai tax
  deployment of this generation is `P07-U-27`.
- No transaction-scale evidence exists for any finding. Six moves cannot support a claim
  about operational behaviour, and none is made.
- The database was read table-at-a-time with no restore, so no join was executed by a server;
  every cross-table statement above was assembled by reading two extracts. That is weaker
  than a query and is declared as such.
