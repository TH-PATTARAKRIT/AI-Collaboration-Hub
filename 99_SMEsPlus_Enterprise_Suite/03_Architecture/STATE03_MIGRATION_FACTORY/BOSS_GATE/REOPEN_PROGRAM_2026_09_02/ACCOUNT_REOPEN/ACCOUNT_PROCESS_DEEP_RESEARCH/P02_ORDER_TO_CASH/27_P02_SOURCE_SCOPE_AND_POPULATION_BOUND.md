# 27 — P02: THE SOURCE SCOPE IS NOT THE DEPLOYED CODE

`LAYER 2 — AUDIT QUARANTINE` · Session `SMEPLUS-26-09-04-ACC-P02-O2C-TARGETED-FORENSIC-CLOSURE-001`

Produced after a second peer exchange (P04). **This is the most package-bounding file in P02** and it
should be read before any source-derived negative claim anywhere in the package.

## 1. The Check, And Why It Was Run

P04 reported that against its own deployment, **27 of 361 installed modules were in neither of its declared
source roots**, and warned that *a source scope named by a build string does not identify code*.

P02 ran the same check against `idemo18_uat` — the v18 deployment P04 supplied, and the only deployed
database on the generation P02's entire source analysis was written against.

## 2. Result

**`FACT VERIFIED` — SC-01. Of 361 installed modules, 66 are NOT in P02's declared v18 source root.**

| | |
|---|---|
| Modules installed in the deployment | **361** |
| Present in the declared root | **295** |
| **Absent from the declared root** | **66 (18%)** |

**`FACT VERIFIED` — SC-02. The build string does not identify the code.** Two directories on this host
carry the same build `18.0+e.20250608` and hold **797** and **799** addons respectively. P02 declared one
of them by path and cited it as *the* v18 root throughout.

## 3. The Modules That Matter To P02

Among the 66 absent modules, by name alone:

| Module | Why it bounds a P02 finding |
|---|---|
| **`inherit_sales`** | By name, an override of the sales module — **the module P02 is about**. |
| **`inherit_inventory`** | By name, an override of the inventory module — the other module P02 is about. |
| `account_invoice_fixed_discount` | Directly concerns `11` §7a, P02's discount analysis. |
| `account_payment_multi_deduction` | Directly concerns `09`, P02's settlement analysis. |
| **`l10n_th_withholding_tax`** | See §4. |
| **`l10n_th_withholding_tax_cert`** | See §4. |
| **`l10n_th_withholding_tax_cert_form`** | See §4. |
| **`l10n_th_withholding_tax_report`** | See §4. |
| `om_data_remove` | The module a peer process recorded as its **highest-severity finding**. |
| `full_summarize_bills`, `journal_entries_report`, `print_voucher_request` | Accounting-document behaviour, unexamined. |

**`FACT VERIFIED` — SC-03. `inherit_sales` and `inherit_inventory` are installed in the deployment and
exist NOWHERE on this host.** The code that modifies sales and inventory behaviour in the only deployed
v18 system **cannot be read at all**.

## 4. C-32 — A Published `VERIFIED ABSENCE` Is Refuted

`L2_AUDIT_QUARANTINE/T3` §5 and §10 published, as **`VERIFIED ABSENCE` within the population**:

> *"No withholding certificate model … not found in the entire addons root (791 module dirs, all file
> types, recursive) under the patterns `is_withholding`, `withholding_sequence`"*, and
> *"no module directory matches `*withhold*` or `*wht*`."*

**Refuted.** The deployment has **four** Thai withholding modules installed —
`l10n_th_withholding_tax`, `l10n_th_withholding_tax_cert`, `l10n_th_withholding_tax_cert_form`,
`l10n_th_withholding_tax_report` — and **all four exist on this host, in three copies each**, in
directories entirely outside the declared root.

**The negative was true within its stated boundary and false in use** — precisely the failure P04
described in its own census. The boundary was declared honestly; **the boundary was the wrong one**, and
nothing in the claim signalled that the root it named was not the code the system runs.

**Consequence for the Thai track:** `06` §3's *"Withholding-tax accrual or certificate event on a customer
receipt — `VERIFIED ABSENCE`"* is **withdrawn**. P02 cannot say whether customer-side withholding is
handled, because the modules that would handle it were never read. **Routed to P07**, which owns Thai tax
and has independently recorded findings about these same modules.

## 5. What This Bounds

**Every source-derived negative claim in this package is scoped to a code base that omits 18% of the
deployed modules, including two that by name override the two modules P02 is about.**

That does **not** invalidate the mechanism analysis — reading how the standard product works is exactly
what clean-room benchmark learning requires, and the mechanisms are correctly read. It **does** mean:

| Claim class | Status |
|---|---|
| *"The standard product does X"* | **stands** — correctly read from the standard product |
| *"No mechanism for Y exists"* | **bounded, and one is already refuted** (§4) |
| *"The deployment behaves as X"* | **not supported** — 66 modules unread, 2 unreadable |

**`FACT VERIFIED` — SC-04.** P02's declared path set has now failed on **three axes**: the archive path
set (`RE-20`), the runtime path set (`RE-21`), and now the **source** path set. In every case
POPULATION, PATTERN and UNIT were declared and executed, and the **path set was chosen and not
validated against what the system actually runs**.

## 6. RE-22 — A Sixth Evidence-Base Failure: Publishing A Partial As A Total

`26` §9 published *"16 database-bearing artefacts … 7 distinct databases"*.

**That was a read of a background job that was still running.** On completion it stood at **26 artefacts
and climbing**, including an entire location P02 had not considered — **iCloud Drive**
(`~/Library/Mobile Documents/…`), holding at least five further deployed databases.

**`FACT VERIFIED` — three further distinct deployed databases**, each confirmed from its own manifest:

| Database | Generation | Journal lines | **COGS** |
|---|---|---|---|
| `iMSCG` | **16.0+e** | 1,083 | **0** |
| `pankhamhom` | **18.0+e-20250223** | 956 | **0** |
| `T805efaplus` | **18.0+e-20250223** | 0 | **0** |

**`FACT VERIFIED` — TC-02 SURVIVES ITS FIFTH POPULATION EXTENSION.** **At least 10 distinct deployed
databases, three generations — zero cost-of-sales entries in every one.**

**`FACT VERIFIED` — the population is OPEN and P02 no longer publishes a total.** Every count published so
far — 5, 6, 8/5, 16/7 — has been superseded. The sweep was still running when this file was written.
**P02's position is now the invariant, not the count:** *no deployed database yet tested, on any
generation, contains a cost-of-sales journal line.*

## 7. Two Controls Applied To Results P02 Likes

P04 supplied the rule: **a test run only when it confirms is not a test; the control belongs on the
results you like.** Applied to P02's headline:

**`FACT VERIFIED` — SC-05. The zero-COGS instrument is positively controlled.** Taking a real 40,353-row
extract, the counter returns **0**. Injecting **one** synthetic cost-of-sales row into the same data and
re-running the same counter returns **1**. **The instrument can see a cost line and returns zero because
there are none — not because it cannot see them.** This control had never been run before; the headline
had gone six databases without one.

**`FACT VERIFIED` — SC-06. The symlink trap does not inflate P02's sweep.** `/Volumes/iMac` **is** a
symlink to `/` on this host, as P04 reported. P02's sweep used a non-following `find`, and **0 of its
results lie under that path** — verified rather than assumed.

## 8. Peer Handling

| Item | Disposition |
|---|---|
| P04's two traps | **Both verified independently.** The symlink is real and did not affect P02 (§7); the seven-snapshot/one-identity point P02 had already found independently by uuid. |
| P04's census total | **Not adopted**, as P04 advised and as P02 already practises. P02 also does not adopt P07's reported 15/7/3. **Two independent sweeps agreeing on 7 identities and 3 generations is corroboration; the file counts differ and should.** |
| P04's rule | **Adopted and applied** — §7. |
| P04's withdrawal of its own confirmation | Noted as the mirror of P02's result and as the better outcome of the two: P04 ran the control, the control cost it a confirmation, and it withdrew. |
| Returned to P04 | The source-scope check they suggested — run, and it refuted a published P02 absence (§4). |
