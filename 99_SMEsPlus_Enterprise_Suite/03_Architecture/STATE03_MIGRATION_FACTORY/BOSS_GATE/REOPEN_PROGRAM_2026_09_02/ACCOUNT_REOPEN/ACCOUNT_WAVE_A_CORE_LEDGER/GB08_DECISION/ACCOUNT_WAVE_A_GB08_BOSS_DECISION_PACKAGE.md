# ACCOUNT WAVE A — `GB-08` BOSS DECISION PACKAGE

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GB08-001` · Layer 1 clean-room
Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-FC-001` · Programme `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001`
Date `2026-09-04`

> **Supersedes** `FINAL_CLOSURE/ACCOUNT_WAVE_A_GB08_BOSS_DECISION_PACKAGE.md` (published at commit
> `ba0b747`). That file remains published and citable; **six of its claims are corrected here** and the
> corrections are itemised in `ACCOUNT_WAVE_A_GB08_EVIDENCE_TRACE.md §13`.

> # `BOSS DECISION REQUIRED — GB-08`
>
> **This file does not select an option.** Boss is the sole Final Approver. No implementation, freeze
> or architecture decision is taken here. Reference-implementation behaviour is **evidence, not design
> authority**.

**Companion documents**

| File | Contains |
|---|---|
| `ACCOUNT_WAVE_A_GB08_OPTIONS_REGISTER.md` | The option set, both axes, every required field, unranked |
| `ACCOUNT_WAVE_A_GB08_EVIDENCE_TRACE.md` | Every claim below, with file, line and a re-runnable script |
| `ACCOUNT_WAVE_A_GB08_DOWNSTREAM_DEPENDENCY_MAP.md` | What breaks, where, and how hard |
| `ACCOUNT_WAVE_A_GB08_AAS_PLUS_PMO_RECOMMENDATION.md` | The recommendation — separate from the decision |
| `LAYER2_GB08_EVIDENCE/gb08_evidence.sh` | `VOL=/Volumes/iMacSys bash gb08_evidence.sh` reproduces §3–§6 |

---

## 1. What `GB-08` is

`GB-08` is the open question of **how SMEsPlus defines canonical FX-rate ownership and rate-selection
precedence**.

| Element | Value |
|---|---|
| **Concept** | *Which exchange-rate row values a transaction, and who owns that row* |
| **Table** | `res_currency_rate` (model `res.currency.rate`) |
| **Resolvers** | `res.currency._get_conversion_rate` → `_compute_current_rate` → `_get_rates`; and, in v19 only, a second resolver in `orm/models.py` reached by grouped monetary aggregation |
| **Why it is Wave A** | Every foreign-currency measurement in the ledger passes through it: initial recognition, unrealised revaluation, realised FX, consolidation, and every monetary aggregate on screen |

**It was raised** because the reference implementation appeared unstable across the versions SMEsPlus
spans. **This session tested that appearance and it does not hold** — see §7. What `GB-08` actually
comes down to, on the evidence, is three questions the reference implementation answers *implicitly*
and SMEsPlus must answer *explicitly*:

| | Question | What the reference does today |
|---|---|---|
| `R1` | **May a branch own an exchange rate?** | The schema, the UI and the record rule all say **yes**; the resolver silently says **no**. A branch-scoped rate row can be created, saved and displayed, and **will never value anything** (`GB08-F7`) |
| `R2` | **What happens when no applicable rate exists?** | It **never fails**. It falls forward to a **future** rate, and failing that substitutes **par, `1.0`** — silently, in every variant (`GB08-F4`, `GB08-F5`) |
| `R3` | **Is an unowned, database-wide rate row legal?** | **Yes** — `company_id` is nullable, the global record rule admits `company_id = False` to every user, and any `group_account_manager` can create one (`GB08-F8`). This is `GB-03`'s axis |

---

## 2. Why this is a Boss decision, not a technical finding

A technical finding says *what the code does*. `GB-08` asks *what SMEsPlus should do*, and the evidence
is now clear that the code cannot answer it:

1. **There is no vendor position to defer to.** The 22 discovered roots carry **4 distinct**
   `res_currency.py` contents, and all four resolve rates the **same way** — root-scoped, ownership
   before recency, three-tier silent fallback. The one apparent divergence (`Δ1`) **does not change the
   rate selected** (`GB08-F1`). *There is no "which version do we follow" question left to answer.*
2. **The remaining question is a business fact about SMEsPlus's own customers.** Whether a Thai
   multi-branch entity's branch transacts at its own rate or at the group's is a fact about how those
   businesses operate. **No amount of source research produces it.**
3. **The failure rule is a business trade-off with an accounting consequence.** Blocking a posting when
   no rate exists is more correct and less convenient. That balance is Boss's to strike, not
   engineering's.
4. **Both choices are irreversible in the ledger.** Recognition amounts, realised FX and comparatives
   are all downstream. Changing the rule later does not restate what was already posted, and — because
   none of this touches DDL — **there is no migration artefact for any reviewer to review**.
5. **The programme's own rule requires it.** Per the decision boundary: the SMEsPlus semantic must be
   justified from `Business Fact → Accounting Semantic → Control Requirement → SaaS Boundary → Source of
   Truth → Event Ownership → Failure/Correction Rule`. **`R1` and `R2` are the first link — the Business
   Fact — and only Boss supplies it.**

---

## 3. Which source roots were searched

**Declared before the result, per the denominator rule:**

| Element | Declaration |
|---|---|
| **POPULATION** | Every reference core root on the evidence volume |
| **PATTERN** | The literal path suffix `addons/base/models/res_currency.py` |
| **PATH SET** | Whatever that pattern returns under `/Volumes/iMacSys`, unfiltered, unranked |
| **UNIT** | One directory containing that file = one reference core root |

**Result: 22 roots.** All 22 were searched, not a sample. The full list, with each root's
`res_currency.py` digest, its `Δ1` result under two independent tests, its `sum_currency` file count and
its manifested-module count, is in `LAYER2_GB08_EVIDENCE/gb08_evidence_output.txt` and is regenerated by
one command.

| Line | Roots | Δ1 |
|---|---|---|
| **v18** | 13 | 5 PRESENT · 8 ABSENT |
| **v19** | 9 | 0 PRESENT |

---

## 4. Why the root count changed — and it was not a counting dispute

**Earlier rounds searched one root.** Wave A's declared research root was
`/Volumes/iMacSys/CLAUDE AI/SMEsPlus18/odoo-18.0+e.20250608/odoo`. No artefact stated that a choice of
root had been made, so no artefact bounded the conclusions drawn from it.

**The method was validated before the new number was used.** Applying this round's manifest count to the
**parent's own** root returns **1,753** modules. The parent declared **791** (`addons/`) + **961**
(`addons_archive/`) = 1,752, +1 for the root manifest. **The two agree exactly.** The change from 1 root
to 22 is therefore a **change of path set, not of counting method** — the arithmetic was never in
dispute.

**And this session found the same defect one level down.** The parent published *"1,753 of 23,530
modules"*. That denominator **overlaps**: mechanical prefix testing shows `t8master` (2,636) *contains*
`smeplus-server` (1,304), which *contains* `odoo` (637) and `odoo_old` (28).

> ### `GB08-F3` — `23,530` is **not** a count of distinct modules.
> The disjoint sum is **21,561 over 19 disjoint roots**. `PATTERN` and `PATH SET` were declared; `UNIT`
> was not tested for disjointness. **The correction moved the enumeration defect from the root level to
> the unit level; it did not remove it.** This is the same lesson as `GB-07` and `FC-F4`, at the next
> level down, and it is now recorded rather than repeated.

---

## 5. What the 22-root enumeration proves — and what it does not

| **It proves** | **It does not prove** |
|---|---|
| That the programme's evidence volume holds **22** directories matching a **declared** pattern | That 22 is the **total** number of reference core roots. A root that omits or relocates `addons/base/models/res_currency.py` is invisible to this pattern |
| That those 22 carry **only 4 distinct** `res_currency.py` contents | That 4 is the total number of behavioural variants **anywhere** — only within this path set |
| That `Δ1`'s text is present in exactly 5 of the 22, under **two independent tests** that agree | That `Δ1`'s presence means branch-preferred behaviour. **It does not** — `GB08-F1` |
| That `sum_currency` is absent from **all 13** v18 roots and present in **all 9** v19 roots | That `sum_currency` is the only v19 resolver addition — only that it is the one found |
| That `res.currency._get_rates` and `_get_conversion_rate` are each defined **exactly once per root** | That no module **outside** the declared path set overrides them |
| That the earlier one-root basis was **unbounded**, and every class `A` absence in Wave A is bounded to ≤1 root of 22 | That any of those absences is **wrong**. Bounding a claim is not falsifying it |

> **Class `A` bounded enumeration over a declared pattern.** `NO EVIDENCE FOUND` is not
> `FUNCTION DOES NOT EXIST`, and this section exists so that distinction survives into the decision.

---

## 6. What `5 / 22 roots` means — and what it does not

`Δ1` — the three-line branch-preference edit in `_get_conversion_rate` — is present in **5 of the 22
roots**: `MIGRATION/ODOO18/18.0.1`, `MIGRATION/ODOO18/18.0.2_community_enterprise`,
**`MIGRATION/ODOO18/18.0.3_smeplus`**, `MIGRATION/ODOO18/odoo-18.0.post20260605`, and
`ODOO/SOURCE CODE/ODOO 18/odoo-18.0.post20260605`.

**Three qualifications, each material, and each new this round:**

1. **`5 of 22` counts copies, not behaviours (`GB08-F2`).** All five roots hold the **same bytes** —
   digest `277f428f0566`. The behavioural denominator is **4 distinct variants**, of which **1** carries
   `Δ1`. Two of the five are independent copies of the same `post20260605` build. *Five roots reads as
   breadth of adoption; it is one variant, duplicated.*
2. **The 22 are not disjoint (`GB08-F3`).** Any fraction with 22 as its denominator is over an
   overlapping population.
3. **`Δ1` does not do what it says (`GB08-F1`).** Whatever the count, the behaviour it is counting is
   **inert** — see §7.

**And one qualification on version identification (`GB08-F10`):**
`./CLAUDE AI/MIGRATION/ODOO18/enterprise` is filed under an **`ODOO18`** path, carries the **v19**
`res_currency.py` digest, and contains **11** files using `sum_currency`, which exists in no v18 root.
**It is a v19 tree in an ODOO18 directory.** Any control that identifies a build from its path is
unsound.

---

## 7. Why Wave A's research root did not show the behaviour — and why that matters less than it appeared

**The mechanical answer.** Wave A's declared root, `SMEsPlus18/odoo-18.0+e.20250608/odoo`, carries
digest `784a62e190a7`, an **earlier** v18 content in which the `Δ1` hunk had not yet been written. The
root whose name asserts the SMEsPlus line, `MIGRATION/ODOO18/18.0.3_smeplus/odoo`, carries `277f428f0566`
and **has** it. Wave A researched a build that may not be the target, and no artefact said which build
was the target. **That finding stands.**

**The important answer — and it changes the risk.** This session diffed the two v18 variants in full:

```diff
@@ -266,7 +266,10 @@
     def _get_conversion_rate(self, from_currency, to_currency, company=None, date=None):
         if from_currency == to_currency:
             return 1
-        company = company or self.env.company
+        if company == self.env.company.root_id:
+            company = self.env.company  # Get rates through branch if selected company
+        else:
+            company = company or self.env.company
```

**That hunk is the entire difference between the two files.** And it is **inert**:

- `_get_conversion_rate` does not read rates. It calls `with_company(company)` and reads `.inverse_rate`.
- `_compute_current_rate` then calls `_get_rates(self.env.company, date)`.
- `_get_rates` uses that company **once**, as `company.root_id.id`, in
  `('company_id','in',(False, company.root_id.id))`.
- `res.company.root_id` is the **topmost ancestor** (`res_company.py:115–118`), so
  `branch.root_id == root.root_id == root`.
- **`Δ1` swaps a root for one of its branches; `.root_id` collapses both back to the same root. The
  domain — and therefore the rate row selected — is identical.**
- The only other company-dependent input, `company.currency_id`, cannot differ either: a subsidiary's
  currency is **constrained equal to its parent's** (`res_company.py:95–103, 422–429`).
- Neither method is overridden **anywhere in the 22 roots**.

> ### `GB08-F1` — `Δ1` does not change which rate row is selected.
> And the v18 and v19 `_get_conversion_rate` bodies are, apart from this inert hunk, **byte-identical**.
> **There is no v18-versus-v19 branch-rate divergence to decide between.**
>
> **Bound:** this is a **static derivation from source, not an executed test.** `MCU-01` — an executed
> test on a running root + branch instance — remains open, and its value has **risen**: it would confirm
> or overturn the programme's most consequential single claim in hours.

**Why this matters more, not less.** The risk is not that two builds disagree. It is that:

- a change that **reads** as a branch-preference feature, complete with a comment saying so, shipped in
  five roots and **does nothing** — so anyone reasoning from the source will reach the wrong conclusion,
  exactly as the parent round did;
- meanwhile the branch axis **is** broken, permanently and in every variant, in a different way:
  `GB08-F7`, the branch rate row that can be entered and will never be used.

---

## 8. Why this creates downstream risk

| # | Risk | Mechanism |
|---|---|---|
| 1 | **A foreign-currency amount can be recognised at par** | `COALESCE(…, 1.0)` in `_get_rates` in **all four variants**, and again in `Δ3`. *"No rate exists"* becomes *"the rate is 1"* with no error and no trace (`GB08-F4`) |
| 2 | **A past transaction can be valued at a future rate** | Fallback tier 2 is `order='company_id.id, name ASC'` with **no upper date bound** (`GB08-F5`) |
| 3 | **A stale owned rate beats a current global one** | `order='company_id.id, name DESC'` — ownership first, recency second (`GB08-F6`) |
| 4 | **A branch rate can be entered and silently ignored** | Nullable, editable `company_id`; record rule shows it; manager ACL creates it; resolver never selects it (`GB08-F7`) |
| 5 | **One tenant's rate row can value another tenant's ledger** | Global record rule admits `company_id = False`; any `group_account_manager` can create such a row (`GB08-F8`) |
| 6 | **A v19 uplift silently changes reported figures** | `Δ3` converts grouped monetary totals at **today**, outside the record rule, with a par fallback — and `account.move.line` has **no opt-out**, while three non-ledger models do (`GB08-F9`, `GB08-F11`) |
| 7 | **None of 1–6 produces a migration artefact** | All are behavioural. **No DDL change, nothing for a DDL-shaped migration gate to inspect** (`J-15`) |
| 8 | **Comparatives are not reproducible** | Resolution depends on the rows present at posting time (risk 3), and there is **no journal entry recording why a rate was chosen** |

**Risks 1, 2, 3, 4, 5, 7 and 8 are present in every variant.** They are **not** removed by choosing a
version. **Only risk 6 is version-dependent.**

---

## 9. Which semantics are affected

Full treatment in `ACCOUNT_WAVE_A_GB08_DOWNSTREAM_DEPENDENCY_MAP.md §3–§6`. In summary:

| Domain | Affected |
|---|---|
| **Accounting** | Initial recognition · unrealised revaluation · realised FX · comparatives and restatement · consolidation · presentation-currency reporting. TAS 21 is the governing standard **by name**; its specific paragraph obligations are **not verified in this session and are held** under the programme's statutory-claim rule. The mechanical fact stands regardless: **par substitution is not a spot rate** |
| **SaaS / tenant / company** | Tenant isolation of rate data (**breached by design today**, `GB08-F8`) · allowed-company scoping on aggregates (**ignored by `Δ3`**, `GB08-F9`) · branch as a sub-boundary (**a half-boundary**: writable and visible, never authoritative, `GB08-F7`) |
| **Migration** | No DDL change on any axis · no artefact for any behavioural divergence · **`S2` carries a silent retrospective revaluation risk** if inert branch rows exist · **`S3` is the only option producing a reviewable data migration** · **build identity cannot be read from a path** (`GB08-F10`) |
| **Reporting** | Every monetary field in list, pivot and graph emits `sum_currency` on v19 — opt-out by field definition, not opt-in. The rule-bypassing query **executes** on essentially every grouped monetary read; the wrong figure **surfaces** only on groups spanning two or more currencies |

---

## 10. Why this blocks the Wave A Final Gate and Wave B readiness

**Wave A Final Gate.**

| Gate dimension | Status |
|---|---|
| Gate recommendation | **`RECOMMEND HOLD`** — unchanged. `GB-08` is one of eight open blockers (`GB-01`…`GB-08`) |
| `CONDITIONAL PASS` | **Unavailable** — tolerance-zero boundaries remain unresolved, and `GB08-F7` / `GB08-F8` are tolerance-zero in kind |
| `FAIL` | **Not recommended** — the semantic model has not been substantively disproved. This session corrects six parent claims and disproves none of the model |
| `% Board` / `% STATE` / `% STEP` | **Not calculable** — and `GB08-F3` shows the previously published denominator itself overlaps |
| `MCU-04` | **`VERIFIED DEFECT`** — unchanged by this session |
| `GB-08` | **`BOSS DECISION REQUIRED`** |

**Wave B.** `NOT READY — EXACT DEPENDENCIES`. `D2` is `GB-08`, and it is **HARD** for every
foreign-currency AR element — invoice recognition, payment, realised FX, credit notes, aged AR,
cross-currency reconciliation — and **NONE** for domestic-only AR. Wave B has **not** been started.

**And `GB-08` is not the root of its own tree.** `MCU-21` is above it; `GB-03` and `T0-04` gate two of
its four semantic options. A ruling on `GB-08` unblocks `D2` **only** if the chosen semantic is `S1` or
`S4`.

---

## 11. What is *not* a `GB-08` Boss decision

| Item | Owner |
|---|---|
| Which build SMEsPlus actually ships | **Programme declaration** — a fact to be stated, not a decision. `GB08-F10`: it cannot be read from a path |
| An executed test on a running root + branch instance | **Research** — `MCU-01`, open; now more valuable, because `GB08-F1` is a derivation |
| `Δ3`'s `today`-dated conversion, par fallback and rule bypass | **Verified defects** (`MCU-20` / `BW-31`), not options |
| The dead branch-scoped rate row | **Verified defect** — `GB08-F7`, new. Broken under every option |
| `GB-03`'s null axis | **Open verified defect** with a database-level route; it is `GB-03`, and it is a **precondition** of `S3` |

---

## 12. The decision

> # `BOSS DECISION REQUIRED — GB-08`
>
> **`R1` — May a branch or operating unit hold, and be valued at, its own exchange rate, distinct from
> its root company's?**
>
> **`R2` — When no applicable rate exists, does SMEsPlus block the posting, or substitute a value?**
>
> *(`R3` — is an unowned, database-wide rate row legal? — only if `S3` is in contemplation; it is
> gated by `GB-03` and `T0-04` and cannot be settled inside `GB-08`.)*
>
> The option set for each is in `ACCOUNT_WAVE_A_GB08_OPTIONS_REGISTER.md`, unranked and with the
> evidence for and against each. The recommendation — **`RECOMMEND BOSS BUSINESS RULING BEFORE RESEARCH
> CAN CONTINUE`** — is in `ACCOUNT_WAVE_A_GB08_AAS_PLUS_PMO_RECOMMENDATION.md` and is a recommendation
> only.
>
> **A genuine Boss-only decision remains. Nothing in this package selects it.**
