# 54 — P05 RESEARCH ERROR RECONCILIATION `RE-07` … `RE-23`

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

## 1. Error Class Tally

| Class | Count |
|---|---|
| **Evidence-base / denominator** | **7** (`RE-07`, `RE-11`, `RE-12`, `RE-14`, `RE-15`, `RE-20`, `RE-21`, `RE-22`) |
| Interpretation | 2 (`RE-10`, `RE-18`) |
| Tool capability | 2 (`RE-08`, `RE-13`) |
| Decision-authority / statutory boundary | 2 (`RE-16`, `RE-17`) |
| Omission | 1 (`RE-19`) |
| Over-generalisation | 1 (`RE-23`) |
| Staleness | 1 (`RE-09`) |
| Arithmetic | **0** — every published number reproduced exactly under independent recomputation |

> **The dominant failure mode is not arithmetic and not reasoning. It is the population.**
> Eight of seventeen errors are the same defect: a claim whose *denominator* was chosen by the author
> and never proved. `RE-07` and `RE-20` are the same error committed **twice, one round apart**, after
> the first was written up and a standing control adopted.

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
