# 62 — P05 AAS-03 EVIDENCE-BASE CHALLENGE

`LAYER 2 — AUDIT QUARANTINE` · `CP-P05E24`
**This file and `54` govern over any headline table in the package (`ER-AASR-1`).**

Four disjoint challenge classes, each briefed to **disprove**, each bound by the negative-claim
classes, the prohibition on `PASS`/`FAIL` wording, and a strict read-only constraint.

| Class | Mandate | Status |
|---|---|---|
| **A** | Evidence population / denominator | **COMPLETE — and it contradicted this round's own foundation** |
| **B** | Tooling / extraction / method | **COMPLETE** |
| **C** | Finding / accounting semantics | **COMPLETE** |
| **D** | Decision authority / cross-process ownership | **COMPLETE** |

## Mandated Adversarial Attempts — outcomes

| Attempt to disprove | Outcome |
|---|---|
| *"`hr_expense_petty_cash` is not installed in the verified deployment population"* | **DISPROVED by the author's own reconstruction** — it **is** installed on the v18 target. `RE-21`. |
| *"`scgl_advance_expense_request` is not installed"* | **NOT disproved.** Uninstalled or absent in all six read registries incl. v18. Strengthened. |
| *"`scgl_purchase_advance_payment` is live in all four relevant deployed databases"* | **DISPROVED** — not installed on the v18 target; installed in 4 of 6; exercised 21× in one. `RE-22`. |
| *"Vendor down payments fail to deduct from final vendor bills"* | **Source defect NOT disproved.** Financial effect **never demonstrated** — class `C`. |
| *"`sudo()` bypass creates an authorization defect"* | **NARROWED** to `PARTIAL AUTHORIZATION`; reach class `C`. |
| *"5,426 / 5,863 WHT lines lack `tax_line_id`"* | **NOT disproved** at v16; **superseded** by the v18 target measurement — **358/358 = 100.00%**, reproduced exactly by Challenge C. |
| *"Screen and CSV use materially different eligibility semantics"* | **NOT disproved.** Confirmed from source, from the ORM field definition, and from data on both platforms. |

## Challenge A — the round's own foundation contradicted

Dispatched to disprove *"the archive population is now complete."* **It succeeded on three counts.**

| # | Finding | Author verification |
|---|---|---|
| 1 | `iErpOCC` (**271,259,809 B**) and `iSCErP` (**52,672,227 B**) were recorded in `41 §3` as **"0 B — unreadable — cloud placeholder"**. Both are fully readable with valid headers. | **confirmed** — `stat` + `pg_restore -l` |
| 2 | **`iSMEs182_2025-01-18_14-07-44.zip`** — an **Odoo 18.0+e** native backup (`dump.sql` 68.6 MB + `manifest.json` + `filestore/`) — a **10th identity**, inside the declared path set, invisible because the pattern excluded `.zip` | **confirmed** — `unzip -l` |
| 3 | **38 Docker containers; two Postgres running now**, one (`occ-odoo18-db`) backing **`occ-odoo18-webtest`, a live Odoo 18.0 app, up 5 days**; plus named volumes and two local Homebrew clusters. **Structurally invisible to any filename search.** | **confirmed** — `docker ps` |

It also **read `pankhamhom`**, which the author had declared class `C` and left unread: **Odoo 18.0,
1,338 modules, 478 installed, `hr_expense_petty_cash` INSTALLED 18.0.1.2** — so petty cash is installed
in **two** v18 databases — and **`scgl_purchase_advance_payment` INSTALLED**, which corrects the
author's "not on the v18 target" to a **per-database, not per-version** scoping (`RE-30`).

> **Verdicts on the mandated attacks:**
> *"`hr_expense_petty_cash` is not installed in the verified population"* — **DISPROVED**, and the
> author's implicit "installed nowhere else" is **also disproved**.
> *"`scgl_advance_expense_request` is not installed anywhere"* — **UPHELD**, class `A` within 9
> registries, class `B` beyond.
> *"The archive population is now complete"* — **DISPROVED, decisively.**

**Posture on the live containers:** existence is host metadata. **No connection was made; none is
authorised** (`U-20`, `HOLD — RUNTIME / CONNECTION AUTHORIZATION REQUIRED`). They are nonetheless the
most direct available route to the live-posting evidence `TZ-01` needs.

## Challenge C — the decisive result

**Challenge C overturned the author's own headline reversal.** The author had declared `TZ-01`
`CONTRADICTED` on the strength of 386-of-387 credit lines landing on the petty cash account.
Challenge C ran the test the author did not — `create_date`, `create_uid`, journal **name** — and found:

| Test | Result |
|---|---|
| `create_date` of all 387 petty-cash moves | **100% = 2026-08-25**, a single day |
| `create_uid` | **100% = 1** (system/migration user) |
| Journal name | **`"COA Migration 2026"`**, type `general` |
| Sequence prefix | **100% `MIG26/`** |
| Accounting dates | back-dated, Jan–Aug 2026 |
| **All expense-sheet-linked moves created outside 2026-08-25** | **0 of 712** |

Author independently re-ran every one of these and confirmed them exactly.

> **The entire petty-cash GL population is migration output. Not one entry was produced by the live
> application posting an expense.** `TZ-01` is a claim about live posting behaviour; this evidence
> cannot speak to it either way. **`TZ-01` → `C — NOT DECIDABLE FROM THIS EVIDENCE`.** `RE-27`.
>
> Challenge C also supplied the simpler explanation the author missed for the `entry`/general-journal
> /no-payment signature — migration, not a divergent code copy. `RE-28`.

Author's response: **accepted in full**, and the same standard was then applied to `PC-01`, which the
author had just published — its counts are class `A`, its *reading* as an audit-trail defect is now
`C — NOT DECIDABLE`. Challenge C had let `PC-01` stand; the author downgraded it anyway.

## Challenge B — extraction integrity

Dispatched on the hypothesis that COPY-block parsing silently drops rows with embedded tabs/newlines.
**Hypothesis disproved, for a structural reason:** `pg_restore --data-only` emits COPY **TEXT** format,
which always escapes embedded tab/newline/backslash as two-character sequences — the failure mode is
real for CSV-format COPY and does not apply here. Zero mismatches across **nine** files.

Published counts independently reproduced from the raw archives: **183,590** journal entries ·
**5,201** certificates · **993** expenses · **332** v18 certificates. **No published count is an
undercount.**

**New tool landmine found (did not reach any published number):**
`pg_restore --data-only --table=public.hr_expense` — schema-qualified — **silently returns zero rows,
exit 0, empty stderr**, while the bare `--table=hr_expense` returns all 993. This is the `RE-13` class
again: a filter that cannot express the positive it is trusted for. The package uses bare names
throughout (grepped, class **A**), so nothing published is affected. **Added to the standing controls.**

Also: `$PG16` **fails loudly** on a v1.16 archive rather than misreading it; `$PG16` and `$PG18`
produce byte-identical data where both can read. And the session's own helper scripts contain
`if len(f)!=len(cols): continue` with **no counter** — architecturally capable of silent loss, verified
not to have fired.

## Challenge D — decision authority

Six findings, all accepted and applied: severity words surviving in **filenames** (`RE-24`), imperative
instructions to a peer (`RE-25`), and a withdrawn pre-answer still live in another file (`RE-26`).
Confirmed the P01 narrowing is **substantive, not cosmetic**, and found **zero** statutory assertions
in `50`/`51`.

## Aggregate

| Measure | This round |
|---|---|
| Author findings published this round | 6 principal |
| **Overturned by challenge** | **4** — the `TZ-01` contradiction; the divergent-code-copy inference; **the completeness of the evidence base itself**; the per-version scoping of the P01 module |
| Corrected for authority/framing | 3 |
| Confirmed and reproduced exactly | `TX-01` (both platforms), `PC-01` counts, all module states, all extraction integrity |
| New findings from challenges | 3 tool/method + 1 scope boundary + **1 tenth database + 1 live-instance population** |
| **Corrections originating from the author, unprompted** | **1** — the `PC-01` downgrade |

> **All four challenge classes found material defects, and the two most severe were in the round's own
> corrective work**: the evidence-base reconstruction (Challenge A) and the headline reversal built on
> it (Challenge C). **A round convened to repair an evidence-base failure reproduced that failure in a
> new form.**
