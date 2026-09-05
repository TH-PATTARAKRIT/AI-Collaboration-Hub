# 39 — P05 RESEARCH ERROR AND REVISION LOG (CONTINUATION)

`LAYER 2 — AUDIT QUARANTINE`
Continues `15`, which remains the authoritative log for the original round (`RE-01`..`RE-06`,
`GR-01`..`GR-03`). This file adds the continuation's errors and revisions. **Per `ER-AASR-1` this
file governs over any headline table in the package.**

## 1. Research Errors Found in This Continuation

### `RE-07` — **the package asserted that evidence did not exist, when it did** *(most serious)*

| | |
|---|---|
| **The claim as published** | `13 §5`: *"Live database access this session: **NONE.** No connection was attempted or available."* and *"**No P05-equivalent dump exists.**"* `20 U-02`: *"**No runtime or database evidence exists for P05.** Every behavioural claim is derived from source reading."* `19 §9`: `EC-02` **NOT MET** — *"no runtime evidence"*. |
| **What was actually true** | Six real `ir_module_module` registries and four production database dumps were sitting in the operator's own `~/Downloads` directory and in `~/OCC_Odoo18_Simulation_Lab/snapshots/`, readable offline with `pg_restore -f`, no server and no connection required. One of them holds **183,590 journal entries and 5,201 withholding certificates**. |
| **How it was found** | Only because this continuation's directive ordered the *highest available evidence class* for `U-01` and forbade inferring deployment from source directories. That instruction forced a search the original round never ran. |
| **Why it happened** | The original round searched for a **live database** — `psql`, a running server, a connection — found none, and generalised that to "no database evidence exists". It never searched for **database evidence at rest**. A dump file is not a live database, and it is not source code either; it fell between the two categories the session was looking in. |
| **Class of error** | Exactly the class the project standard names: a negative claim published at class **A** (*"no evidence exists"*) when the search boundary supported only class **B** (*"no live connection found"*). The scope was never declared, so nobody could see the gap. |
| **Impact if it had stood** | `U-02` would have remained a permanent gating unknown routed to Boss for a runtime authorisation that was never needed. Two findings that are now empirically confirmed at production scale (`TX-13`, `TX-20`) would have stayed at `SUPPORTED INTERPRETATION`. The severity inversion at `26 §5` — which is the single most decision-relevant output of the whole package — would never have been discovered. |
| **Correction** | `13 §5` and `20 U-02` are superseded by `24` and `25`. `EC-02`'s basis is restated in `27`. |

> **This is the third time in this programme that a session has declared "no access" from a search
> that did not cover where the evidence actually was.** The project memory records the 2026-09-03
> Asset session concluding "no source code or database access exists" after searching only its working
> tree. The rule derived then — *report negatives with their scope attached, never as absolutes* —
> was written down, was available, and was still not applied here. Writing the rule is evidently not
> sufficient to make it operate; only a directive that forces the search has worked.

### `RE-08` — a shell-glob defect recurred, in a second form

The original round's `RE-06` was an unquoted `--include=*.py` expanded by zsh. This continuation hit
the same class again in the clean-room scan: an unbounded token `quant` matched the ordinary English
word *quantity*, reported as a vendor-token leak. Re-run with `\bquant\b` the count was zero.
Recorded at `18 §6` rather than silently dropped.

**Both instances share one root cause: a pattern that does not mean what its author intended, and no
second form run to catch it.** The standing control adopted after `RE-06` — *a zero result is never
accepted without re-running the same query in a second form* — was applied to zero results, but
`RE-08` was a **non-zero** false positive, which that control does not cover. The control is
extended: **a surprising result in either direction is re-run in a second form.**

### `RE-09` — the peer-session table went stale during execution

Recorded at commit `9b1006b`. The table said P01/P02/P03 had no committed output; five peers pushed
while the session ran. Accurate when written, wrong at publication. Corrected in `12 §3`.

### `RE-10` — **the `TX-20` mechanism was inverted** *(published, then contradicted by review)*

| | |
|---|---|
| **Published** | `25 §3`: *"4,081 of 5,201 certificates — 78.5% — carry a date that is not the payment date"*, attributed to the certificate `date` being set from a create-time default. Promoted to `FACT VERIFIED` and carried into `30 §3 H-P07-3`, `33`, and the commit message. |
| **What is true** | `payment_date == create_date::date` in **5,201 of 5,201 rows — 100.00%**. Joined to the real payment date (`account_payment.move_id → account_move.date`, 3,794 certificates, 0 unjoinable): `cert.date` is **correct in 97.79%**; `cert.payment_date` is correct in **16.05%**. The deltas are **negative** — certificates are keyed *before* the payment is dated. |
| **The error** | The author compared two columns and **assumed which one was the truth**, without ever joining to the payment. The column named `payment_date` was taken to mean the payment's date because of its name. |
| **Caught by** | AAS-03 Expert 2. Not by the author. Every counter-measurement was then re-run by the author and reproduced exactly. |
| **Disposition** | Original claim class **E — CONTRADICTED**. The corrected finding is retained and is arguably worse: a `NOT NULL` column named `payment_date` **carries no payment information in 100% of rows**. |

### `RE-11` — **`TX-13` was overstated roughly thirtyfold**

| | |
|---|---|
| **Published** | *"32 payments hold multiple live statutory certificates with no substitution link between them"*, one carrying nine. |
| **What is true** | 21 of the 32 are **one certificate per distinct supplier** on bulk payment runs — a certificate is issued per payee, so N payees require N certificates. That is correct behaviour. Of the 11 same-supplier groups: 8 are different withholding **rates** (1% / 3%), 2 are `done`+`draft` pairs, and **1 is a genuine exact duplicate** (payment 659, certificates 124/126, identical number `JRCSH12023100176`, identical line). |
| **The error** | Two compounding mistakes: the author filtered `state != 'cancel'`, which **admits `draft`**, and never grouped by supplier — so it counted a legitimate multi-payee structure as duplication. |
| **Caught by** | Expert 2. Author-verified: every figure reproduces. |
| **Disposition** | Original figure class **E**. `TX-13` survives as a **control defect with one production instance** — the schema half is confirmed (`DB-01`: no UNIQUE, no index) and one duplicate proves reachability. It is no longer a mass-duplication finding. |

### `RE-12` — a negative contradicted by the package's own declared roots, for the second time

`25 §4` stated *"`iTEST02` (v19) holds 0 certificates and `iEVING` holds 0, so no v19 population
exists to measure."* The enumeration was **author-chosen** rather than driven by the registry set the
package had already declared one file earlier: it omitted `BK12MAY26`, listed at `24 §2` as v19
registry `R-d` with the certificate module installed. `BK12MAY26` holds 1 certificate. Class **E**.

This is the **second** instance in this package of a negative claim contradicted by a root inside its
own declared path set — the first was `21 NC-E-05`, where `NC-A` was bounded to `ENT18/addons` while
`addons_archive` sat in the same declared path set. **The same defect, twice, in the same package,
after it had been written up.** The denominator rule (`POPULATION + PATTERN + PATH SET + UNIT`, none
author-chosen) does not fail because it is unknown here; it fails because the author re-chose the set
at the moment of making the claim instead of iterating the declared one.

### `RE-13` — a schema read that could only ever return a false negative

The author read the certificate schema with `pg_restore -s -t withholding_tax_cert`. That returns
**only** the `CREATE TABLE` statement: constraints, indexes and foreign keys are separately-named
archive objects which the `-t` filter **excludes**. Verified — the filtered extract yields **0**
matches for `CONSTRAINT|CREATE INDEX`; the unfiltered schema yields a primary key, ten foreign keys,
and the fact that no index exists.

**Any "no constraint exists" conclusion drawn from `-s -t` is unfalsifiable by construction** — the
command cannot produce the evidence that would refute it. This is the *executed-not-quoted* defect
class in a new disguise: the command ran, the output was real, and the output could not contain the
answer. The rule is extended: **before accepting a negative from a filtered extract, prove the filter
can express a positive.**

### `RE-14` — an unearned population claim, after the caveat had already been written

`24` disclosed at §4 that the six registries are a **convenience sample**, then wrote
"**the** deployed estate" three times elsewhere in the same file, including in its §5 disposition
table. The caveat and the violation shipped together. Class **E** for the population claim; withdrawn
package-wide, and every §3 claim re-classed **A** for the six named files, **B** for anything wider.
*Caught by AAS-03 Expert 1.*

### `RE-15` — two snapshots of one database counted as two deployments

The package's "**five real business databases**" — a phrase load-bearing for the `TZ-11`/`TZ-12` reach
claim and the P01 handoff — counted `iTEST02-Jun` and `iTEST02-Jul` as separate systems. Author-verified
from the archive headers: **both are `dbname: iTEST02`**, one month apart. The corrected identity set is
**four distinct databases across two owners** (`scgl`, `efaplus`), one of them named as a test
environment (class **C**). Corrected in seven files. *Caught by AAS-03 Expert 1.*

> `RE-14` and `RE-15` are the same defect at two scales: **counting the artefacts found rather than
> the things they represent.** A file is not a deployment, and a folder is not a population.

### `RE-16` — a soft statutory leak in a package that claims to make none

`07 TX-12` wrote *"a `done` — **potentially already-filed** — certificate…"*. Nothing in the source or
the data tracks filing status; this was an unsourced real-world assumption used to motivate a HIGH
severity, carrying no `HOLD` tag, in a file whose own opening rule is that a mechanical fact is never
presented as a statutory conclusion. **Withdrawn.** *Caught by AAS-03 Expert 3, whose full audit
otherwise found no hard statutory assertion anywhere in `07`.*

### `RE-17` — P05 answered, in its own column, a question it was routing to P07

`30` `H-P07-2` labelled the per-payee certificate group "**(legitimate)**" while the adjacent column
posed *"Is a payment permitted multiple certificates?"* as still open for P07. **Withdrawn.**
Related routing gap also fixed: `BD-06`, `BD-07` and `BD-08` were posed directly to Boss with no P07
routing, though two of them are Thai-statute territory — Boss would have been deciding P07's substance
without P07 in the loop. *Caught by AAS-03 Expert 3.*

### `RE-18` — a `CORR1` scope withdrawal that was itself wrong

`22 §3 R-01` **withdrew** a finding on the argument that `res.partner` is tenant-scoped so
`REFERENCE SCOPE ≠ FINANCIAL SCOPE` made `check_company` unnecessary. Both halves are refuted from
source: `res.partner` carries its own optional `company_id`, and **Odoo core applies `check_company=True`
to partner references for exactly this case**. The argument was contradicted by the platform's own
design pattern. **Reinstated, narrowed** — the true defect is *late failure* (enforcement exists at
move creation/posting, and `sudo()` does not bypass it), which also corrects `04 §4`'s
"no gate at any layer" in the opposite direction. *Caught by AAS-03 Expert 4.*

> **`RE-18` is the most instructive error in this log.** It was produced by the *correction round* —
> the scope-aware revalidation whose whole purpose was to stop the author asserting requirements
> instead of deriving them. The author then asserted a *non*-requirement instead, from a
> characterisation of `res.partner` it had not checked. **Applying a rule is not the same as verifying
> the facts the rule operates on.**

### `RE-19` — an entire lineage-survival channel never examined

A full-package grep for `mail.message` / `chatter` / `tracking` / `ir.attachment` / `message_post` /
`_creation_message` returns **zero hits across all 39 files**. The package concluded that severing the
foreign key destroys the claim-to-entry trail without ever asking whether the trail survives elsewhere.
It partly does — a permanent chatter message and directly-addressed attachments survive three of the
four mechanisms. Recorded as `08 SR-07a`; it **bounds** `SR-07` rather than overturning it.
*Caught by AAS-03 Expert 4.*

## 2. Revisions Forced by the New Evidence

| ID | Revision | Effect |
|---|---|---|
| `GR-04` | `U-01` re-dispositioned from `BOSS DECISION REQUIRED` (a blanket unknown) to **PARTIALLY RESOLVED** — resolved for the deployed estate at class A, `HOLD — DATABASE EVIDENCE REQUIRED` for the v18 target at class D. | `24 §5` |
| `GR-05` | `U-02` split into a database half (**closed**) and a runtime-execution half (**`HOLD — RUNTIME EVIDENCE REQUIRED`**), with the specific write authorisation named rather than assumed. | `25 §6` |
| `GR-06` | **Severity inversion.** Two axes introduced — `DEFECT STATUS` and `REACH`. Six boundaries reclassified `LATENT`; the purchase-advance and WHT boundaries reclassified `LIVE`. **No boundary was closed on deployment evidence**, and the position defending that is stated at `26 §2`. | `26` |
| `GR-07` | `TX-13`, `TX-20`, `TX-15` promoted from `SUPPORTED INTERPRETATION` to `FACT VERIFIED` **for the v16 database only**; the v18 inference is held at `SUPPORTED INTERPRETATION` and explicitly **not** upgraded. | `25 §3-§4` |
| `GR-08` | `HE-08` (non-deductible) re-dispositioned from a reported gap to `NOT APPLICABLE — EVIDENCE VERIFIED`. | `28 §3` |
| `GR-09` | `EC-07` measured against its quoted definition rather than asserted: the counter reads **0 of 2**, and the reason is structural — pass 1 was not clean, so even a clean pass 2 gives one clean pass, not two consecutive. | `29` |

## 3. What This Continuation Did **Not** Do

Per the continuation directive: no reset, no restart at L1, no discarded evidence, no re-run of
unaffected research. Preserved unchanged: all source findings and citations (`01`–`13`), the original
four challenge verdicts and the 18 brief errors they found (`16`), the 20 typed contradictions and 6
self-corrections (`11`, `15`), the `CORR1` revalidation (`22`, confirmed in `31`, not re-derived),
and the full commit lineage.

## 4. Corrections Made to the Continuation's Own Artefacts

`RE-10`..`RE-13` above are all corrections to artefacts **this continuation published**, all four
raised by the single AAS-03 challenge that completed, and all four author-verified before adoption.
`25 §3` and `§4` were rewritten in place with the original claims struck through rather than deleted.

**Downstream propagation of `RE-10`/`RE-11` was checked and corrected:** the contradicted figures had
already been carried into `30 §3` (`H-P07-2`, `H-P07-3`), `33 §2`, `26 §3` and the commit message for
`f0037b8`. Those are corrected in the same commit as this log. The commit message for `f0037b8`
cannot be rewritten without rewriting published history, so it stands as-is and is **corrected by this
entry** — a reader of that commit message must read `39 RE-10`/`RE-11` alongside it.

## 5. Independent-Review Coverage Actually Achieved

The continuation directive required all four AAS-03 experts to challenge the closure results.
**Only one of four completed.** See `36 §1` — this is reported as a shortfall, not absorbed.

## 6. Standing Method Controls, updated

| Control | Origin | Status |
|---|---|---|
| A zero result is re-run in a second form | `RE-06` | in force; **extended by `RE-08`** to any surprising result |
| Declare POPULATION + PATTERN + PATH SET + UNIT for every enumeration | project standard | in force; the unit omission was itself caught by a reviewer (`16 §3` #14) |
| Never upgrade a class B/C/D negative to class A | project standard | in force |
| **Search for evidence at rest, not only for live access** | **`RE-07`, new** | **adopted.** Before any "no access" claim: enumerate dumps, exports, snapshots and archives, and state the search boundary. |
| **Never assume which of two columns is the truth — join to the authority** | **`RE-10`, new** | **adopted.** A field's *name* is not evidence of its content. |
| **Decompose a count before publishing it as a defect** | **`RE-11`, new** | **adopted.** Group by the dimension the business rule actually keys on before calling a multiplicity a duplicate. |
| **Iterate the declared root set; never re-choose it at claim time** | **`RE-12`, second instance** | **adopted.** The claim's enumeration must be generated *from* the declared path set, not retyped. |
| **Prove a filter can express a positive before accepting its negative** | **`RE-13`, new** | **adopted.** Extends *executed-not-quoted*: a command that cannot produce refuting evidence cannot support a negative. |
| **Count the things, not the artefacts that represent them** | **`RE-14`/`RE-15`, new** | **adopted.** A dump file is not a deployment; a folder is not a population. Deduplicate by identity before counting. |
| **A written caveat does not license the violation two paragraphs later** | **`RE-14`, new** | **adopted.** After disclosing a sampling bound, grep the same file for the definite-article form of the claim. |
| **Verify the facts a rule operates on, not just the rule** | **`RE-18`, new** | **adopted.** The scope correction round produced its own scope error by characterising an object it had not read. |
| **Before concluding a channel is destroyed, enumerate the other channels** | **`RE-19`, new** | **adopted.** Ask what *survives*, not only what is severed. |
| Independent review inside the phase, disjoint, adversarial, briefed to report errors in the brief | project standard | in force; produced 18 brief errors in round 1 |
