# 54 — P05 RESEARCH ERROR RECONCILIATION `RE-07` … `RE-30`

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E15`
The register is **not** continuous from `RE-01`: `RE-01`..`RE-06` belong to round 1 and live in `15`.
This file reconciles `RE-07`..`RE-23`. **Four are new in this round.**

| ID | Original claim | Error class | Corrected finding | Affected |
|---|---|---|---|---|
| `RE-07` | "No runtime or database evidence exists for P05" | **evidence-base** | Five readable dumps were on the host | `U-02`, `EC-02` |
| `RE-08` | Clean-room scan hit on `quant` | tool / pattern | Word-bounded → 0 | `18 §6` |
| `RE-09` | Peer table current | staleness | 5 peers had pushed | `12 §3` |
| `RE-10` | "78.5% of certificates misdated" | **interpretation** — assumed which column was truth | `date` correct in **97.79%**; `payment_date` = `create_date` in **100%** | `TX-20`, `30`, `33` |
| `RE-11` | "32 payments hold multiple live certificates" | **denominator/decomposition** | **1** exact duplicate in 5,201 | `TX-13`, `DUP-09` |
| `RE-12` | "No v19 certificate population exists" | **denominator** — root inside own declared path set | `BK12MAY26` holds 1 | `25 §4` |
| `RE-13` | "No constraint exists" from `pg_restore -s -t` | **tool capability** — filter cannot emit constraints | Unfiltered schema: PK + 10 FKs, no index | `DB-01`, `DB-02` |
| `RE-14` | "**the** deployed estate" | **decision-authority / population** | Convenience sample; class B for any wider claim | `24` |
| `RE-15` | "Five real business databases" | **counting unit** | Two files = one `iTEST02`; four distinct DBs | 7 files |
| `RE-16` | "potentially already-filed" certificate | **statutory leak** | Withdrawn; nothing tracks filing status | `07 TX-12` |
| `RE-17` | "(legitimate)" in P05's own column | **decision-authority** | Withdrawn; P07's question | `30 H-P07-2` |
| `RE-18` | `R-01` withdrawal under CORR1 | **scope reasoning** — rule applied to unverified facts | Reinstated, narrowed to late-failure | `22 R-01'`, `04 §4` |
| `RE-19` | Lineage destroyed by severing the FK | **omission** — never asked what survives | Chatter + attachments survive 3 of 4 paths | `08 SR-07a` |
| **`RE-20`** | **"No Odoo 18 database carrying the P05 surface exists in the available evidence"** | **evidence-base / denominator — SECOND INSTANCE OF `RE-07`'s CLASS** | **`idemo18_uat`, 44 MB, v18, on this host throughout.** The search was folder-scoped, not exhaustive. | **`U-01`, `EC-01`, `EC-03`, all of `26`, all of `44`** |
| **`RE-21`** | **"`hr_expense_petty_cash` installed in none of six registries"** | **denominator** — population excluded the target platform | **INSTALLED `18.0.1.2` on the v18 target; 634 of 993 expenses use it** | `TZ-01`, `TZ-02`, `26`, `45` |
| **`RE-22`** | "`scgl_purchase_advance_payment` live in all four distinct databases" | **denominator + severity** | Installed in 4 of 6 read registries; **not** on the v18 target; exercised 21× in one; **effect not observed** | `TZ-11a`, `TZ-12`, `49` |
| **`RE-23`** | "All seven WHT codes point at one account; `WHT3%` rate is 0" | **over-generalisation from one database** | v16-specific. v18: **4 accounts, 4 companies, 40 codes, no zero-rate** | `TX-01a`, `50 §2` |
| **`RE-24`** | Severity words `CRITICAL` / `LIVE RISK` in **filenames and titles** of `49`/`47` while those documents class the financial effect `C — NOT OBSERVED` | **decision-authority / severity inflation** | Both renamed; caveat now survives the title layer | `49`, `47` |
| **`RE-25`** | "**Required** P01 Follow-up" with four bare imperatives to a peer | **decision-authority** | Rewritten as routed questions; P05 cannot require action of a peer | `49 §4`, `48 §5` |
| **`RE-26`** | The pre-answer "legitimate", withdrawn from `30` last round, was **still live in `34`** | **incomplete propagation of a withdrawal** | Scrubbed; the judgment is P07's wherever it appears | `34` |
| **`RE-27`** | **"`TZ-01` is CONTRADICTED by production data"** | **evidence-population — the tested population never exercised the behaviour** | **All 712 expense-sheet-linked entries are migration output** (`create_uid=1`, one day, journal "COA Migration 2026", `MIG26/` prefix). `TZ-01` → **`C — NOT DECIDABLE`**; source defect unrebutted | `TZ-01`, `44`, `45`, `58` |
| **`RE-28`** | "The deployed module is not the source copy analysed" | **inference — simpler explanation not considered** | The `entry`/general-journal/no-payment signature is **ordinary for migration entries**. `U-16` remains open on its own merits but this data is not evidence for it | `45 §4` |
| **`RE-29`** | **"Exhaustive search → 9 identities, 7 readable"; "no further Odoo 18 database exists anywhere"** | **evidence-population — THIRD CONSECUTIVE ROUND** | (a) `iErpOCC` (271 MB) and `iSCErP` (52 MB) were recorded **0 B/unreadable** — both fully readable, class `E`; (b) `iSMEs182.zip`, an **Odoo 18** native backup, missed because the PATTERN excluded `.zip`; (c) **38 Docker containers, two live Postgres, one backing a running Odoo 18 app** — structurally invisible to any filename search | `41`, `43`, `56 EC-01`, `59` |
| **`RE-30`** | "`scgl_purchase_advance_payment` is not installed on **the v18 target**" | **scoping — version treated as a proxy for database** | Installed on `pankhamhom`, **also v18**. Correct scoping is per **database**, not per version | `43 §3`, `47`, `49` |

## 1. Error Class Tally

| Class | Count |
|---|---|
| **Evidence-base / denominator / population** | **11** (`RE-07`, `RE-11`, `RE-12`, `RE-14`, `RE-15`, `RE-20`, `RE-21`, `RE-22`, `RE-27`, **`RE-29`**, **`RE-30`**) |
| Interpretation / inference | 3 (`RE-10`, `RE-18`, **`RE-28`**) |
| Tool capability | 2 (`RE-08`, `RE-13`) |
| Decision-authority / statutory boundary | **5** (`RE-16`, `RE-17`, **`RE-24`**, **`RE-25`**, **`RE-26`**) |
| Omission | 1 (`RE-19`) |
| Over-generalisation | 1 (`RE-23`) |
| Staleness | 1 (`RE-09`) |
| Arithmetic | **0** — every published number reproduced exactly under independent recomputation |

> **The dominant failure mode is not arithmetic and not reasoning. It is the population.**
> **Nine of twenty-two** errors are the same defect: a claim whose *denominator* was chosen by the
> author and never proved. `RE-07`, `RE-20` and `RE-27` are that error committed **three times across
> three rounds**, each time after the previous one was written up and a control adopted.
>
> `RE-27` is the sharpest instance of *the wrong population*: 712 migration entries cannot answer a
> question about live posting behaviour, however precisely counted. **A large, correct, reproducible
> measurement over the wrong population is still no evidence.**
>
> **`RE-29` is the sharpest instance of *an incomplete population*, and the most humbling in the
> programme.** This round opened by diagnosing two prior population failures, adopted a control
> against them, ran a filesystem-wide search, declared the population, and **was still wrong three
> ways** — two files misread as empty, one archive format outside the pattern, and an entire class of
> live databases that no filename search can reach. **A live Odoo 18 instance was running on the
> machine throughout.**
>
> The lesson is not "search harder". It is that **a search is bounded by the *form* of evidence it
> can perceive**, and that form is chosen by the author. Path set and pattern were both declared —
> and both were still author-chosen. The only control that caught it was an independent party asked
> to attack the boundary with a *different* form.

## 2. Why the Standing Control Failed Again

After `RE-07` the control adopted was: *"search for evidence at rest, not only for live access."*
Round 2 **did** search for evidence at rest — and still missed `idemo18_uat`, because it searched the
folders where it had already found dumps rather than the whole filesystem. The control addressed the
*category* of evidence and not the *boundary* of the search.

**Control now adopted (`RE-20`):** *an evidence-population claim is only as good as the root of its
search. State the root and the pattern, and make the root the filesystem — not a folder in which
something was already found.* The command in `41 §2` is the reference implementation.

## 3. Preservation

Every corrected claim remains in the package **struck through in place, with its original text**, per
`ER-AASR-1`. Nothing was silently rewritten. Commit messages that carry superseded figures
(`f0037b8`, `068c71c`) cannot be rewritten without altering published history and are **corrected by
reference** from this file.
