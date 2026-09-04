# 19 — P03 AAS-03 EXPERT CHALLENGE

**LAYER 2 — AUDIT QUARANTINE.**

Four AAS-03 experts challenge every level of this package. Per
`smeplus-adversarial-section-not-summary-rule`, **the corrections in §5 and §6 are the
part of this file that downstream work must cite — not the headline tables in `01`–`15`.**

---

## 1. The four challengers

| Expert | Stance |
|---|---|
| **E1 — Cost Accountant** | Is the accounting reasoning right, and is the standard applied correctly? |
| **E2 — Source Forensics** | Does the code say what the package claims it says? |
| **E3 — Enumeration & Denominator** | Is every count and every negative claim properly bounded? |
| **E4 — Governance & Boundary** | Did the session stay inside its authority and its layer? |

---

## 2. E1 — Cost Accountant

**Challenge 1: is `DC-01` really a double count, or two operators legitimately costing two labour-hours?**

Sustained against the package, in part. The employee half is correctly two hours — two
people worked. The **machine** half is not: one machine was occupied for one hour.
`05` §2 states this correctly but the finding's title, *"one machine-hour, N injections"*,
invites the misreading that all conversion cost doubles. **Correction `C-01`: the
inflation is confined to the machine component.**

**Challenge 2: is `DC-07` a defect at all, given the field's help text documents it?**

Not sustained. Documented behaviour that produces a wrong period result is still a wrong
period result, and `PROJECT_CONSTITUTION.md` principle 13 designates financial-integrity
failures as `Tolerance = 0` regardless of whether they are documented. The package's
framing — a *silent default*, in the same family as the Wave A FX fallback — is correct.

**Challenge 3: does `10` §4 overstate by calling the netting "the single most dangerous property"?**

Sustained. Two residues net in one account **only when both defects are present in the
same company on the same product category**, which requires a mixed standard-and-actual
costing configuration. **Correction `C-02`: the claim must be conditioned on that
configuration, not stated absolutely.**

---

## 3. E2 — Source Forensics

**Challenge 4: `DC-08` cites `_post_inventory` without line numbers, unlike every other finding.**

Sustained. `09` §1 and `05` §5 quote the code but give no line range, while `17` §3 lists
the finding with a bare function name. **Correction `C-03`: `DC-08`'s citation is weaker
than the rest of the package and must be recorded as such.** The quoted code was read in
place; the omission is of precision, not of evidence.

**Challenge 5: does `_set_duration` really fire when `_post_inventory` writes `duration`?**

**Not established by this session.** `05` §5 and `09` §1 assert that writing `duration`
creates or adjusts time logs. `_set_duration` exists (`mrp/models/mrp_workorder.py`,
inverse of `duration`) and was seen, but its body was **not read**.
**Correction `C-04`: the *mechanism* by which the forced duration becomes cost is
`SUPPORTED INTERPRETATION`, not `FACT VERIFIED`.** The *outcome* — that a zero-duration
work order ends up costed at expected duration — follows from `_cal_price` reading
`_cal_cost` and is unaffected. `DC-08`'s severity is unchanged; its classification is
corrected.

**Challenge 6: `DC-12` claims a double currency conversion. Is the second multiplication not a different factor?**

Sustained as written. `mrp_workorder_hr_account/report/mrp_cost_structure.py:43-44` applies
`currency_rate` on both lines, and `:47` then multiplies by duration. But the package does
not note that `:47` reads `l[-1] * l[-2]`, i.e. cost × hours, so the **duration** factor is
correct and only the rate is doubled. **Correction `C-05`: state the error as
rate-squared, not as a general miscomputation.**

---

## 4. E3 — Enumeration & Denominator

**Challenge 7: `02` §3 declares POPULATION, PATTERN, PATH SET and UNIT. Do the other enumerations?**

Partly. `03` §2 (`extra_cost`), `05` §7 (`employee_analytic_account_line_ids`), `11` §3
(`rework`) and `01` §6 (target baseline) each declare all four. **`12` §4 (payroll bridge)
declares POPULATION, PATTERN and UNIT but its PATTERN is stated as a concept — "any
reference reconciling absorbed labour to posted payroll" — not as a mechanical search
string.** A conceptual pattern is not reproducible.
**Correction `C-06`: `DEP-07`'s negative claim is weaker than the others and must be
labelled `NO EVIDENCE FOUND — PATTERN NOT MECHANICAL`.**

**Challenge 8: `02` §1 says "eleven have exactly one path, and eight have none". Does that account for all twenty?**

No. Eleven plus eight is nineteen. `CC-15` (landed production cost) is classified
"1, foreign" and belongs to neither group. **Correction `C-07`: the sentence must say
eleven, eight, and one foreign path, or it miscounts its own register.** This is precisely
the defect `smeplus-account-wave-a-final-closure-status` records as a package miscounting
its own closures.

**Challenge 9: is `01` §6's "0 of 15 module specifications" a complete denominator?**

The count is of `MODULE_SPEC_*.md` files at the suite root. `MODULE_SPECIFICATION_PACK_INDEX.md`
and `MODULE_EXPANSION_PLAN.md` exist alongside them and **were not examined**. A planned
manufacturing module could be named there.
**Correction `C-08`: the claim must be bounded to "0 of 15 existing module
specifications", and the expansion plan must be checked before the absence is treated as
settled.**

---

## 5. E4 — Governance & Boundary

**Challenge 10: does P03 silently resolve any Asset blocker?**

No. `04` §6 states `BLK-07` as HOLD, quotes it, adds an observation and explicitly declines
to recommend. `14` §2 lists what P03 stopped short of. **Not sustained — the boundary held.**

**Challenge 11: does `04` §5's requirement list constitute design?**

Borderline. `R-01` … `R-06`, `R-07` … `R-10`, `R-11` … `R-14` are stated as requirements
and marked `DESIGN CANDIDATE`, and `04` §5 says no implementation is authorised. But
fourteen numbered requirements across three files, with no consolidated register, read as a
specification in fragments.
**Correction `C-09`: the requirements are legitimate as `DESIGN CANDIDATE` but must be
consolidated in one place and explicitly marked as not constituting a design, or the AAS+
veto is at risk of being eroded by accumulation.**

**Challenge 12: is the Layer 1 / Layer 2 split actually enforced?**

Asserted in `00` §1 but **not yet mechanically verified** at the time of the challenge.
`smeplus-clean-room-rules` requires a mechanical grep scan over outputs before commit,
recorded in the session closure. **Correction `C-10`: the scan must be run and its result
recorded, or the layer claim is unevidenced.**

---

## 6. Corrections carried forward

| ID | Correction | Effect |
|---|---|---|
| `C-01` | `DC-01`'s inflation is confined to the machine component | Scope narrowed; severity unchanged |
| `C-02` | `10` §4's netting claim is conditional on mixed costing configuration | Claim conditioned |
| `C-03` | `DC-08`'s citation lacks line precision | Recorded as weaker evidence |
| `C-04` | **`DC-08`'s mechanism is `SUPPORTED INTERPRETATION`, not `FACT VERIFIED`** | **Classification corrected** |
| `C-05` | `DC-12` is a rate-squared error specifically | Precision |
| `C-06` | `DEP-07`'s pattern is not mechanical | Negative claim weakened and labelled |
| `C-07` | **`02` §2 miscounts its own register — 11 + 8 ≠ 20** | **Arithmetic corrected** |
| `C-08` | `01` §6's denominator excludes the expansion plan | Claim bounded |
| `C-09` | The 14 requirements need consolidation and an explicit non-design marker | Governance |
| `C-10` | The clean-room scan must be run and recorded | Governance |

**Ten corrections from self-challenge.** `smeplus-adversarial-section-not-summary-rule`
records that self-review has historically found roughly a sixth of what independent review
then finds. **This package should be assumed to contain materially more defects than the
ten found here**, and `20_P03_AAS_PLUS.md` §4 states what an independent reviewer should
attack first.
