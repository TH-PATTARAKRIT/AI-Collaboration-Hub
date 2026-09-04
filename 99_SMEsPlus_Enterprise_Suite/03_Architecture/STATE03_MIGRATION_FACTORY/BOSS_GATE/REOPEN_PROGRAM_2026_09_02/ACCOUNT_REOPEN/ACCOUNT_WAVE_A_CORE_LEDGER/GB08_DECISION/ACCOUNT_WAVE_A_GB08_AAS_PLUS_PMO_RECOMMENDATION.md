# ACCOUNT WAVE A — `GB-08` AAS+ / PMO RECOMMENDATION

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GB08-001` · Layer 1 clean-room
Date `2026-09-04`

> **This is a recommendation. It is not a decision and it does not bind Boss.**
> Boss is the sole Final Approver. Nothing here selects an option on Boss's behalf.

---

# `RECOMMEND BOSS BUSINESS RULING BEFORE RESEARCH CAN CONTINUE`

---

## 1. Why this verdict and not another

The permitted verdicts were `RECOMMEND OPTION 1|2|3|4`, `RECOMMEND HOLD — EVIDENCE INSUFFICIENT`, and
`RECOMMEND BOSS BUSINESS RULING BEFORE RESEARCH CAN CONTINUE`. Each was tested against the evidence:

| Verdict considered | Why not |
|---|---|
| `RECOMMEND OPTION 1` (`S1` company-owned wins) | `S1` is already the reference behaviour and is the **cheapest**, but it **does not answer the question `GB-08` was raised for** — whether a *branch* may own a rate — and it leaves `GB08-F5` and `GB08-F7` untouched. Recommending it would make the blocker look closed while the defects stand |
| `RECOMMEND OPTION 2` (`S2` branch preference) | Requires a **business fact** about how SMEsPlus's multi-branch customers operate. No amount of source research supplies it, and **no reference build implements `S2`** (`GB08-F1`), so there is nothing to inherit or measure |
| `RECOMMEND OPTION 3` (`S3` tenant standard + override) | Blocked by two open items that are **not** `GB-08`: `GB-03` (the null axis) and `T0-04` (what "tenant" means). Recommending it would import two open blockers into a closure |
| `RECOMMEND OPTION 4` (`S4` explicit or block) | AAS+ holds that `S4`'s **failure rule** is not optional (§2). But `S4` is **not a complete semantic** — it says what happens when there is no rate, not who owns one — so it cannot stand alone as the `GB-08` answer |
| `RECOMMEND HOLD — EVIDENCE INSUFFICIENT` | **Rejected as inaccurate.** The reference evidence has converged: 22 roots → **4 distinct variants** → **one** resolution semantic, with the v18 divergence shown inert (`GB08-F1`) and the schema, precedence and fallback shown stable across all four. Calling this "evidence insufficient" would misdescribe a research base that is, on the reference axis, close to complete |
| **`RECOMMEND BOSS BUSINESS RULING BEFORE RESEARCH CAN CONTINUE`** | **Selected.** What is missing is not evidence about the reference implementation. It is a **business fact about SMEsPlus's own customers** — may a branch hold its own exchange rate — and a **programme declaration** — which build ships. Neither is research, and both gate the remaining work |

> **The precise ruling requested of Boss is stated in §5. It is one business question and one
> programme declaration, not a choice among four options.**

---

## 2. AAS+ view — clean-room semantic assessment

AAS+ evaluates clean-room semantic correctness, accounting-event integrity, source-of-truth stability,
event ownership, FX valuation correctness and future architecture risk.

| Axis | AAS+ assessment |
|---|---|
| **Clean-room semantic correctness** | The reference implementation supplies **one** semantic, not two. `GB08-F1` removes the "choose between v18 and v19" framing entirely. A clean-room design therefore has **no vendor tie-break to make** and must be justified from first principles or not at all |
| **Accounting-event integrity** | **Compromised today, in every variant.** `COALESCE(…, 1.0)` converts *"no rate exists"* into *"the rate is 1"*. An accounting event whose measurement input is absent must fail, not resolve. This is the clearest correctness defect in the whole `GB-08` surface (`GB08-F4`, `GB08-F5`) |
| **Source-of-truth stability** | The rate table's schema is **stable across all four variants** — same columns, same `unique (name, currency_id, company_id)`, same nullable `company_id`. Stability is real. **It is the semantics layered on it that are defective, not the table** |
| **Event ownership** | **Unresolved and internally contradictory.** `res_currency_rate.company_id` may name a branch; the record rule shows it; an accounting manager may create it; the resolver never reads it (`GB08-F7`). A data model that permits an owner the code cannot honour has no ownership semantic at all |
| **FX valuation correctness** | Three verified failure modes, all stable: a **future** rate used for a past transaction; **par** used when no rate exists; a **stale owned** rate beating a **current global** one (`GB08-F5`, `GB08-F6`). None is version-dependent |
| **Future architecture risk** | `Δ3` shows the pattern that matters: the reference implementation **adds resolvers over time** in places the previous design did not have one, with no schema change and no migration artefact. Whatever SMEsPlus builds must own its resolver and its count of resolvers, or the same drift will recur on every uplift |

### AAS+ positions — conditional, and not a Boss decision

| # | Position | Conditional on |
|---|---|---|
| `AAS-GB08-1` | **The par fallback must be removed under every option.** `COALESCE(…, 1.0)` is a defect, not a design choice, and AAS+ does not treat its removal as optional | Nothing. AAS+ states this unconditionally |
| `AAS-GB08-2` | **The dead branch-scoped rate row must be resolved either way** — the branch must become authoritative (`S2`) or the column must be constrained so a branch row cannot be created (`S1`, `S3`, `S4`). Leaving it writable-and-ignored is not a state any option should carry forward | Nothing |
| `AAS-GB08-3` | **If Boss rules that branches may not hold their own rates**, AAS+ would favour `S1` + `S4`'s failure rule, inside freeze option `D` | Boss ruling `R1` = NO |
| `AAS-GB08-4` | **If Boss rules that branches may hold their own rates**, AAS+ would favour `S2` inside `D`, with an explicit consolidation translation policy and an explicit migration plan for existing inert rows | Boss ruling `R1` = YES |
| `AAS-GB08-5` | **`S3` is not assessable** until `GB-03` and `T0-04` are closed. AAS+ takes no position on it | `GB-03`, `T0-04` |

> **AAS+ does not rank `S1`–`S4` and does not recommend one.** `AAS-GB08-3` and `AAS-GB08-4` are
> **conditional consequences of a ruling Boss has not yet made**, published so that the ruling's
> implications are visible before it is made.

---

## 3. PMO view — evidence, gate and delivery assessment

| Axis | PMO assessment |
|---|---|
| **Evidence sufficiency** | **Sufficient on the reference axis; insufficient on the business axis.** 22 roots enumerated mechanically, 4 distinct variants identified, every parent claim re-tested — six reproduced exactly, six corrected, none unverifiable. What is missing cannot be closed by more source research |
| **Gate impact** | `GB-08` remains **one of eight open blockers**. This session does not close it and does not reduce the count. Gate recommendation is unchanged: **`RECOMMEND HOLD`** |
| **Implementation timing risk** | **Do not start.** Two of four semantics (`S2`, `S3`) have open preconditions; one (`S1`) is cheap but leaves the defects; one (`S4`) is incomplete alone. Starting any build now commits to a semantic Boss has not ruled on |
| **Downstream Wave B risk** | `D2` remains **HARD** for every foreign-currency AR element and **NONE** for domestic AR. Wave B must not open on the FX path. A domestic-only Wave B slice would not touch `D2` — that is a scoping observation, not a recommendation to split |
| **Jira / GitHub traceability** | **Now sound.** The Wave A package is published on `origin` and re-read from it; the manifest roll-up digest recomputes from the published content; the `ERPPLUS-138` comment carries the branch, HEAD SHA and digest. The parent round's `GITHUB EVIDENCE PUBLICATION NOT VERIFIED` state is cleared |
| **Auditability** | **Improved.** `gb08_evidence.sh` reproduces the entire root-set and divergence result from a declared pattern in one command. `GB08-F1` is a derivation with every premise separately cited to file and line |
| **Can the decision safely move to Wave B?** | **No.** Not until `R1` (branch ownership) and `R2` (missing-rate behaviour) are ruled on. `R3` may be deferred only if the chosen semantic is `S1` or `S2` **and** the null row is separately constrained |

### PMO risks if the ruling is deferred

| Risk | Severity | Note |
|---|---|---|
| Wave B FX AR cannot be specified | **HIGH** | `D2` |
| A silent retrospective revaluation if `S2` is later chosen | **HIGH** | Existing inert branch rows become live, with no DDL and no artefact (`GB08-F7`) |
| Cross-tenant rate leakage persists in any live multi-tenant database | **HIGH** | `GB08-F8`; it is `GB-03`, and it is not waiting on `GB-08` |
| A v19 uplift silently adds aggregate figures that disagree with the ledger | **MEDIUM-HIGH** | `Δ3`; `account.move.line` has no opt-out (`GB08-F11`) |
| Programme continues without declaring its shipped build | **MEDIUM** | `GB08-F10`: path names cannot substitute for the declaration |

---

## 4. Where AAS+ and PMO disagree

Stated rather than smoothed, per the adversarial-section rule:

| Point | AAS+ | PMO |
|---|---|---|
| **Whether `S1` is a viable interim** | **No.** `S1` leaves `GB08-F5` and `GB08-F7` standing and would let the blocker read as closed | **Qualified yes.** `S1` is the lowest-divergence, most reversible position and could be adopted *provisionally* to unblock contract work, if it is explicitly labelled interim |
| **Whether more research is worth commissioning** | **Marginal.** The reference axis has converged; an executed test (`MCU-01`) would confirm `GB08-F1`, not change the ruling | **Worth it.** `MCU-01` is hours of work and converts the programme's most consequential claim from a derivation into a measurement |
| **Whether `Δ3` is a `GB-08` matter at all** | **No** — it is a verified defect (`MCU-20`/`BW-31`) to be fixed under any option | **Partly yes** — it is the mechanism by which a v19 uplift changes reported figures, so it belongs in the build-freeze conversation |

> Both agree on the verdict. **They disagree on what should happen in the meantime**, and that
> disagreement is itself information for Boss.

---

## 5. The ruling requested of Boss

Not a menu selection. **Two statements, and a third only if `S3` is in contemplation:**

| # | What Boss is asked to state | Type | Consequence |
|---|---|---|---|
| `R1` | **May a branch / operating unit hold and be valued at its own exchange rate, distinct from its root company's?** | **Business ruling** | `YES` → `S2` inside `D`, with a consolidation translation policy and a migration plan for existing inert rows. `NO` → `S1` inside `D`, and `res_currency_rate.company_id` must be constrained so a branch row cannot be created |
| `R2` | **When no applicable rate exists, does SMEsPlus block the posting, or substitute a value?** | **Business ruling with an accounting consequence** | `BLOCK` → `S4`'s failure rule, applied under whichever ownership semantic `R1` selects. `SUBSTITUTE` → Boss is accepting recognition at par or at a future rate, and AAS+ records `AAS-GB08-1` as overridden |
| `R3` | *(only if `S3` is in contemplation)* **Is an unowned, database-wide rate row legal in a shared database?** | **Business ruling, gated by `GB-03` and `T0-04`** | Cannot be answered inside `GB-08`; it is `GB-03`'s axis |

**And one programme declaration, which is not a Boss decision but is required before any freeze:**

> **Which build does SMEsPlus ship?** A fact to be stated, not chosen. `GB08-F10` shows it cannot be
> inferred from a directory name.

---

## 6. What this recommendation explicitly does not do

- It does **not** select `S1`, `S2`, `S3` or `S4`.
- It does **not** select freeze option `A`, `B`, `C` or `D`.
- It does **not** declare Wave A closed, converged, or approved.
- It does **not** authorise Wave B, implementation, or any source-code change.
- It does **not** treat reference-implementation behaviour as design authority. Per the decision
  boundary rule, the reference is **evidence**; the SMEsPlus semantic must be justified from
  `Business Fact → Accounting Semantic → Control Requirement → SaaS Boundary → Source of Truth →
  Event Ownership → Failure/Correction Rule`, and `R1`/`R2` are the first two links of that chain.
