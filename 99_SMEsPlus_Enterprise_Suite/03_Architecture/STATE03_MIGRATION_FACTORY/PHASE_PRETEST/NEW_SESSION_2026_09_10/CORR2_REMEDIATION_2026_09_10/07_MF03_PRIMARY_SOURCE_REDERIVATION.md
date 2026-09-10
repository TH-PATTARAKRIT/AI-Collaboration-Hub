# 07 — `MF-03` PRIMARY-SOURCE RE-DERIVATION

# `NOT DECIDABLE ON CURRENT EVIDENCE · EXCLUSION UNSUPPORTED`

## `CHECKPOINT H`

Session: `[SMEPLUS-26-09-10-PHASE-PRETEST-B7R2-REMEDIATION-NEWSESSION-001]`
Baseline: `c91d5840` · Boss: **SOLE FINAL APPROVER**

> **`§18` requires re-reading the latest controlling evidence and comparing eleven properties.**
> All eleven are compared below. **`§18` also forbids reliance on unbuilt controls — and that
> prohibition is what decides this file.**

---

## 1. THE EVIDENCE BASE — established before it is used

**`§7` of the programme's own standard: the evidence base is itself a claim.** It is measured first.

| Question | Measurement |
|---|---|
| Does the **defining register** for `HX-nn` exist on the frozen baseline? | **NO.** `git ls-tree -r c91d5840 \| grep -i INVENTORY_CROSS_MODULE_HANDOFF` → **not on tree** |
| Where does it exist? | **`2` branches, not `1`** — `origin/design/inventory-final-solution-v1-2026-09-02-001` **and `-v2-…`**, both at `FINAL_SOLUTION/INVENTORY/V1_0/10_INVENTORY_CROSS_MODULE_HANDOFF_V1.md` |
| Do the two copies differ? | **NO — byte-identical**, `sha256 233f56926fb73cfd81a16c7fe2b5615ec773ec70c9340f6858465169bf5cc8f4` on both. **No supersession risk** |
| Does `V2_0` redefine `HX-24`/`HX-25`? | **NO.** `V2_0` holds `12` artefacts, **`0`** carrying `HX-25` |
| Is the payload column **nevertheless** on the baseline? | **YES — and this corrects the second-line record** |

**`CORR2-MF-01` — MODERATE.** `05_PRETEST_MATERIAL_FLOW_CANONICAL_REGISTER.md` **L49, on the frozen baseline**,
transcribes all three rows faithfully:

> *"**Handoff register (`HX`)** | **`HX-23`** master data with a provenance reference · **`HX-24`**
> **certified opening balances, quantity and value** · **`HX-25`** **movement history, or opening plus
> history from the cutover date**"*

and `17_PRETEST_CORE_OBLIGATION_CLOSURE.md` L70 carries `HX-25` again in the same terms.

> **Consequence: the falsification below required no off-baseline evidence.** The second-line challenge
> went off-baseline and classified this target as *not dischargeable against the authorized baseline*.
> **It was dischargeable. The contradiction is internal to the frozen package** (`01_` `R2-F-13`).
>
> **What is genuinely absent from the baseline is the *authoritative* register** — the columns carrying
> guarantee, control references and ownership class. **That absence is real and is recorded**, and it is
> why the eleven-property comparison below is run against the off-baseline primary text and says so.

---

## 2. THE PRIMARY ROWS — verbatim

```
| ID    | From → To                     | Fact handed over                          | Trigger | Receiver's obligation                                   | Menus        | Class                          |
| HX-23 | Migration → Inventory         | Master data with a provenance reference   | Cutover | Validate, load, reconcile counts                        | PR-*, CF-*   | INV-OWNED — provenance does not exist yet (GAP-FS-08) |
| HX-24 | Migration → Inventory/Accounting | Certified opening balances, quantity and value | Cutover | Human certification; cross-proof against the opening trial balance | OP-02, RP-05 | JOINT (JT-11, G-5)   |
| HX-25 | Migration → Inventory         | Movement history, or opening plus history from the cutover date | Cutover | Replay with a stable identity; reconcile | RP-03, RP-04 | INV-OWNED — depends on C-02 |
```

**And the elements, at `SA_CORR3_08` L176–177:**

```
| 14 | WHICH Migration / Replay Batch | ABSENT, and the producer says so: the provenance reference "does not exist yet" |
| 15 | WHICH Idempotency Identity     | ABSENT — see XMC-F-11                                                        |
```

---

## 3. THE ELEVEN PROPERTIES — `MF-01` (`HX-24`) vs `MF-03` (`HX-25`)

| # | Property | `MF-01` / `HX-24` | `MF-03` / `HX-25` | Same? |
|---:|---|---|---|:---:|
| `1` | **Payload** | certified opening balances, **quantity and value** | **movement history**, or opening plus history from the cutover date | **DIFFER** |
| `2` | **Guarantee** | human certification; cross-proof against the **opening trial balance** | **replay with a stable identity**; reconcile | **DIFFER** |
| `3` | **Control references** | `OP-02`, `RP-05` | `RP-03`, `RP-04` | **DIFFER — disjoint** |
| `4` | **Ownership** | **`JOINT` (`JT-11`, `G-5`)** | **`INV-OWNED`** — depends on `C-02` | **DIFFER** |
| `5` | **Stable identity** | not required by the row | **required — element `15`, `ABSENT`** | **DIFFER** |
| `6` | **Replay semantics** | none | **the row's defining obligation** | **DIFFER** |
| `7` | **State transition** | creates an opening position | re-applies history from the cutover date | **DIFFER** |
| `8` | **Quantity effect** | quantity enters **without a movement** | **UNDECIDABLE** — zero **iff** replay is idempotent, and idempotency is element `15`, `ABSENT` | **UNDECIDABLE** |
| `9` | **Value effect** | value enters **without a purchase** | **UNDECIDABLE** — same dependency | **UNDECIDABLE** |
| `10` | **Accounting consequence** | **dual-target** — Inventory **and** Accounting | **single-target** — Inventory | **DIFFER** |
| `11` | **Trigger** | Cutover | Cutover | **SAME** |

```
DIFFER      : 8      SAME : 1      UNDECIDABLE : 2
06_ tested  : 1      — the shared one
```

> **`06_` §2.2 asked one discriminator — *"its own trigger, source state and destination state distinct
> from `MF-01`/`MF-02`?"* — and answered `NO`. `Trigger` is the single column where the answer is `NO`.
> Every other recorded column separates the rows.**

---

## 4. THE CITED GROUND, FALSIFIED TWICE

`06_` §2.2 concludes: *"`MF-03` = `EXECUTION MODE` … established on **`HX-25`** and **element `14`**,
**not** on `RT-E15-05`. … **the ground is now evidence rather than an unbuilt control**."*

**Falsification `1` — `HX-25` does not say what it is cited for.**
`06_` asserts *"`HX-25`/element `14` **describe replay as re-running a migration package**"*.
`HX-25`'s payload at primary text — and **at `05_` L49 on the baseline itself** — is
*"movement history, or opening plus history from the cutover date"*. **That is a payload, not a manner of
performing another flow.** It is also a **different payload** from `HX-24`'s certified opening balances.

**Falsification `2` — the unbuilt control was relocated, not removed.**

| | Old ground (`B7-F-10` defect) | New ground (`06_`) |
|---|---|---|
| cited | `RT-E15-05` | `HX-25` + element `14` |
| rests on | element `15` — **`ABSENT`** | **element `14` — `ABSENT`** (*"WHICH Migration / Replay Batch"*, *"does not exist yet"*) |
| and | — | **`HX-25`'s own stated guarantee is *"Replay with a stable identity"* = element `15` — `ABSENT`** |
| element `14` belongs to | — | **`HX-23`** (*"Master data with a **provenance reference**"*), **not `HX-25`** |

`SA_CORR3_08` L230 places both in one clause: *"`XMC-H-18` … **`14` and `15` `NOT SUPPLIABLE`**"*.

> ## **The exclusion moved from one absent element to another absent element and to the row whose
> ## guarantee is the first absent element. `06_`'s closing claim is false.**

---

## 5. CLASSIFICATION — `§18`

| Class | Test | Result |
|---|---|---|
| **A `FLOW`** | own trigger, source state, destination state distinct from `MF-01`/`MF-02`? | **PARTIALLY SUPPORTED** — `8 of 11` properties distinct, including payload, guarantee, controls, ownership and target cardinality. **But the flow-population test is quantity/value effect, and that is `UNDECIDABLE`** |
| **B `EXECUTION MODE`** | a **manner of performing** another flow? | **NOT ESTABLISHED.** The cited ground is falsified (§4), and the primary register treats `HX-25` as a **row**, not as a mode of `HX-24` |
| **C `DIMENSION`** | an attribute of a row? | **NO** — it carries an act and a receiver obligation, not an attribute |
| **D `CONTROL MECHANISM`** | is it a test? | **NO** — `RT-E15-05` is the test **of** replay; replay is the subject |
| **E `HYBRID`** | — | **not reachable** — a hybrid classification still requires the quantity/value measurement |

> ## `MF-03 CLASSIFICATION = NOT DECIDABLE ON CURRENT EVIDENCE`
>
> **The discriminating measurement is whether replay adds quantity or value. That is idempotency.
> Idempotency is element `15`. Element `15` is `ABSENT`. No classification asserted today is a
> measurement; each is a prediction.**
>
> **On the balance of what *is* recorded, the primary register weighs toward `A FLOW` and against
> `B EXECUTION MODE` — `8` distinguishing properties to `1` shared one. That is not enough to classify,
> and it is more than enough to refuse the exclusion.**

---

## 6. CONSEQUENCE FOR THE FLOW POPULATIONS — `§24`

`MF-03` was **excluded** from the flow population on the `EXECUTION MODE` classification.
**`§24`: an unsupported exclusion counts as `UNRESOLVED` and is NOT removed from the denominator.**

| Register | Published | Membership status | `§24` disposition |
|---|---:|---|---|
| `IR` flows | **`20`** — *"`IR-01…18` + `MF-01`, `MF-02`"* | **UNSUPPORTED** — max distinct `IR-nn` in the frozen path set = **`6`** | denominator **NOT VALID**; `MF-03` a candidate member, `UNRESOLVED` |
| `AR` flows | **`30`** — *"`AR-01…29` + `MF-01`"* | **UNSUPPORTED** — max distinct = **`10`** | as above |
| `IR` reconciled | `14` | cites `SA_CORR2_05`, **not in the frozen path set** | **UNSUPPORTED** |
| `AR` reconciled | `15` | cites `SA_CORR2_06`, **not in the frozen path set** | **UNSUPPORTED** |

**POSITIVE CONTROL on the enumeration instrument:** `PTX-01`…`-11` → **`11` distinct ids in `2` files**
against a declared `11`. **The instrument finds a complete enumeration when one exists.** The `IR`/`AR`
zeros are real shortfalls, not a broken predicate.

> **This is the third independent ground on which exit condition `5` fails (`03_`).**

---

## 7. `MF-01` — the narrowing survives, with a precondition still unmeasured

`B7-F-09`'s disproof of `CC-F-11`'s universal clause (*"no existing valuation rule reaches `MF-01`"*)
is **sound**: under `Standard`, value is a policy attribute of the product rather than a function of a
movement's carried cost, corroborated at `SA_CORR3_03` L178. **`CORE-06` (the counterpart account) is the
correct residue.** `CORR1-F-02`'s `FIFO` layer gap is a genuine sharpening: `HX-24` carries *"quantity and
value"* as an **aggregate**, and `FIFO` requires ordered layers.

**`CORR2-MF-02` — MODERATE, recorded and unmeasured.** The `Standard` asymmetry holds **only if the
product standard cost is itself established independently of the migration.** **In a cutover the standard
cost is itself migrated data.** `06_` §1 neither states nor tests that precondition.
**This is the programme's own unmeasured-consequence-clause shape**: a well-evidenced half carrying an
untested half. It does not overturn the narrowing; it bounds it.

---

## 8. REQUIRED CORRECTION

1. **`MF-03` is `NOT DECIDABLE`.** Do not re-assert `EXECUTION MODE`, and do not assert `FLOW` either.
2. **Carry `MF-03` as `UNRESOLVED` inside the `IR`/`AR` denominators** until element `15` exists.
3. **`IR`/`AR` membership must be enumerated member by member**, or the denominators are invalid.
4. **Test `CORR2-MF-02`** — is the migrated standard cost independent of the migration?
5. **Rule, general:** *"replaced an unbuilt control"* must be proved by naming the new ground **and
   showing the new ground is built.** Here it was neither built nor correctly attributed.

---

## 9. CHECKPOINT

> ## `CHECKPOINT H — MF-03 RE-DERIVED`
>
> Evidence base measured first — **defining register off-baseline on `2` identical copies; payload
> transcribed ON baseline at `05_` L49, so the falsification needed no off-baseline evidence** ·
> **`11` properties compared: `8` DIFFER · `1` SAME · `2` UNDECIDABLE; `06_` tested the `1` shared one** ·
> cited ground **falsified twice** — element `14` `ABSENT` and belongs to `HX-23`; `HX-25`'s own guarantee
> is element `15`, `ABSENT` · **`MF-03 = NOT DECIDABLE ON CURRENT EVIDENCE`** ·
> exclusion **UNSUPPORTED** → `UNRESOLVED` under `§24` · `IR 20` / `AR 30` **memberships unsupported**,
> positive control fires at `PTX 11 / 11` · `MF-01` narrowing **upheld**, precondition **unmeasured** ·
> **`0` reliance on unbuilt controls · `0` classification asserted without its measurement.**

No Evidence = No Progress. Never Skip Gate. Truth over Pass.
**Boss is the sole Final Approver.**
