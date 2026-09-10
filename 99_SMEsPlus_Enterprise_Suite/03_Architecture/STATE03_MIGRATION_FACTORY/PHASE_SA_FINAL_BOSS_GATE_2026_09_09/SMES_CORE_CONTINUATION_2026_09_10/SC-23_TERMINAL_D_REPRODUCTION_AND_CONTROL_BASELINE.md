# SC-23 — TERMINAL-D REPRODUCTION AND CONTROL BASELINE

## CP-SA-SC-170 — TERMINAL-D BASELINE REPRODUCED

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]` · head consumed **`2cfb57eb`**
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **Reproduced independently, not inherited. No zero-result search is believed without a positive control.**

---

## 1. Result

> # `12 OF 12 CLAIMS REPRODUCE. 0 REQUIRE BASELINE CORRECTION.`
> **And one reproduction returned a result that WEAKENS this executor's own prior position** — claim 8/§5.

---

## 2. The twelve claims

| # | Claim | Shape 1 | Shape 2 | Result |
|---:|---|---|---|---|
| **1** | SMEs Core-owned Phase SA material gap population = `0` | `SC-17` §3 requalification sweep | auto-resume state §88: *"Category 3 requalified — `CLOSED`"*; `SC-BD-F-01` discharged | **REPRODUCES** |
| **2** | Category 3 = `0` | `SC-17` | auto-resume §43, §97 | **REPRODUCES** |
| **3** | Six vetoes in force, zero self-discharged | textual assertion `6 in force` / `0 discharged` | **identifier enumeration**: `AAS-V-01`, `AAS-V-02`, `AAS-V-03`, `CF-V-01`, `CF-V-02`, `RC-V-01` = **6 distinct** | **REPRODUCES** |
| **4** | `SC-BD-01` records `FG-F-06 = READING B` | line 24: `> # \`FG-F-06 = READING B — DOES NOT BIND THIS EXIT\`` | heading extraction across both files returns exactly `READING A` and `READING B`, one each | **REPRODUCES** |
| **5** | `SC-CONTRA-01` records `FG-F-06 = READING A` | line 19: `> # \`FG-F-06 = READING A\`` | same extraction | **REPRODUCES** |
| **6** | Both records were created in contexts lacking the other | `SC-BD-01` issuance head `6d08bcc5`; `SC-CONTRA-01` issuance head `7eeb5d8e` | **`git cat-file -e` at each issuance head**: `SC-CONTRA-01` **ABSENT** at `6d08bcc5`; `SC-BD-01` **ABSENT** at `7eeb5d8e` | **REPRODUCES — symmetric, §3** |
| **7** | `EC-05` is presently open unless an explicit controlling Boss supersession exists | `EC-05` primary text | **supersession search returns `0`** (`SC-24` §3) | **REPRODUCES — `EC-05` OPEN** |
| **8** | `EC-04` tolerance-zero items not evidence-closed at executed-runtime level | occurrence count `3` on the CORR5 corpus | **distinct-file enumeration**: `SA10`, `SA_CORR4_01`, `SA_CORR4_03` = **3 files**, with a firing control | **REPRODUCES — `0 of 3` runtime-closed** |
| **9** | `EC-07` cannot produce a clean first pass while a Gate-changing contradiction remains | `EC-07` primary text lists *"new Gate-changing contradiction"* among the reset triggers | the contradiction is **known before pass 1**, so it cannot be "new discovery" in a clean pass | **REPRODUCES** |
| **10** | `B-7`/`Q-BOSS-02` prevents this executor selecting its own verifier | `Q-BOSS-02` §1 control **2**: *"appointed by Boss or an independent governance authority, **not selected by the correction owner**"* | §1 control **1** Model/Agent Separation + §2: *"**Claude Opus 5**, where it authored or executed the repair being reviewed, is **NOT ELIGIBLE**"* | **REPRODUCES — and §5 records a correction this forces** |
| **11** | `POH-D-06` requires AAS+ concurrence; not closed by Boss ruling alone | `POH-F-06`: *"Restating a veto limb is reserved to the veto's **issuer and Boss**"* + *"**Deciding `BLK-07` alone would not lift the veto**"* | Executor 1's `SC-19` independently reaches the same conclusion from the same primary text | **REPRODUCES** |
| **12** | Pre-Test Matrix has not started | sweep for start-language across `SC-11`…`SC-21`: **`0`** | **2** explicit *"not started"* statements | **REPRODUCES** |

---

## 3. Claim 6 in detail — the finding that governs the whole collision

**Executed:** `git cat-file -e <issuance-head>:<other record>` for each pair.

| Question | Result |
|---|---|
| Was any Reading A record on the branch when Reading B was ruled (`6d08bcc5`)? | **NO — ABSENT** |
| Was any Reading B record on the branch when Reading A was ruled (`7eeb5d8e`)? | **NO — ABSENT** |

> **The situation is exactly symmetric.** Neither ruling was issued with the other on the record.
> **Neither can be read as a correction of the other**, because neither had the other to correct.
> This is the single most important fact in the collision, and it is why `SC-24` reaches a bounded card
> rather than a disposition.

---

## 4. Claim 8 in detail — the three tolerance-zero boundaries

| # | Boundary | Source | State |
|---:|---|---|---|
| 1 | `CF-I-03` `D3` **cross-tenant** | `SA_CORR4_03` line 261 — `CRITICAL — TOLERANCE ZERO` | **`SPECIFIED`** (`CP-SA-C4-30`), not built, not executed |
| 2 | **Privileged-bypass path** | `SA_CORR4_01` line 260 — *"`CRITICAL — TOLERANCE ZERO` in the target architecture"* | specified, not executed |
| 3 | **Tenant/company boundary matrix** | `SA10` line 196 — disposition **`TOLERANCE-ZERO — HOLD`** | **explicitly `HOLD`** |

**`0 of 3` are closed by executed runtime evidence.** *(The SC branch shows 10 occurrences of the token
because this executor's own files discuss it; the **source** population is 3, on two shapes.)*

---

## 5. `SC-F-14` — a correction this reproduction forces on THIS executor

**`SC-EC07-02` §2 stated that no candidate for `B-7` is *"named, suggested, or hinted at anywhere in this
file."* That was true of this executor's own act — and it omitted something material.**

> **`Q-BOSS-02` §2 already names an eligibility class**, at Boss's own hand:
>
> - *"**Claude Opus 5**, where it authored or executed the repair being reviewed, is **NOT ELIGIBLE** to
>   perform the corresponding independent challenge for that repair."*
> - *"**ChatGPT GPT-5.6 Sol**, operating in a separate isolated Independent Verification session, may serve
>   as the verifier/challenger **only if** it did not author or execute the repair under review and all
>   controls in Section 1 are satisfied."*
>
> **Withholding that from the appointment card made the card less useful to the only party who can act on
> it.** Corrected at `SC-27` §3, **with the scope qualification that `Q-BOSS-02` §2 is written "for the
> current `P06`/`P08`/`P09`/`P11` correction programme"** — so whether its named eligibility reaches Phase SA
> is itself a scope question, while its §1 **ten controls** are general.

---

## 6. Control baseline frozen for this round

| | |
|---|---|
| Head consumed | **`2cfb57eb`** |
| Package files | **46 top-level**, of which 12 quarantined out of scope |
| Peer artefacts | **byte-identical**, verified per blob |
| Boss authority records after the cited baseline | **2**, ingested and classified (`SC-22` §3) |
| Claims requiring baseline correction | **`0`** |

---

## 7. Checkpoint

> ## `CP-SA-SC-170 — TERMINAL-D BASELINE REPRODUCED`
> **12 of 12 claims reproduce on two evidence shapes where feasible · every zero paired with a firing
> positive control · claim 6 proven symmetric — **neither ruling saw the other** · claim 8 confirms
> `0 of 3` tolerance-zero boundaries runtime-closed · claim 10 forces **`SC-F-14`, a correction against
> this executor's own prior file** · `0` baseline corrections required.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
Boss remains the sole Final Approver.
