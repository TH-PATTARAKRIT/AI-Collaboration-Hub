# P11 — C3 · `D-3b` EVIDENCE-SELECTION CONTROL, v4

`[SMEPLUS-26-09-05-ACC-P11-CORE-RECON-CORR1-001]` · CP-P11C03 · Layer 1 clean-room

> **Recommendation only. Boss is the sole Final Approver. `D-3b` is a Boss decision; this file
> specifies it, it does not grant it.**

---

## 1. Lineage — four versions, each forced by a peer

| v | Content | Forced by |
|---|---|---|
| v1 | *"Authorise reading the PostgreSQL dumps already on the host"* | `P11-F-09` / `P11-E-24` — `MCU-19` mis-filed as needing a running instance |
| v2 | \+ **state the client version**; \+ **open every generation** | `P11-F-10` — `P07`'s instrument-selected bias |
| v3 | \+ **rank the population before selection** | `P11-F-11` — `P07`'s convenience-of-location |
| **v4** | \+ **declare the unit ranked by**; \+ **claim-relevant coverage, not blanket coverage** | `P07` @ `29a659f` unit clause; and this prompt §7 C3, which forbids turning `D-3b` into *"open every dump for every claim"* |

## 2. The five separable elements — the prompt's C3 requirement

**They are separated because they have different owners, costs and failure modes, and collapsing them
is what produced v1–v3.**

| # | Element | Owner | Failure mode if omitted |
|---|---|---|---|
| `E1` | **Access authorisation** | **Boss** | No evidence at all |
| `E2` | **Tool / client version** | Executor, **declared** | A *tested* incapacity that is still false (`P11-E-25`) |
| `E3` | **Generation coverage** | Executor, **claim-relevant** | A biased subset that inverts the finding (`P11-F-10`) |
| `E4` | **Ranking unit** | Executor, **declared before selection** | Right artefact for the wrong question (`P07-F-60`, withdrawn) |
| `E5` | **Claim-specific selection objective** | Executor, **declared with the claim** | The other four satisfied and the wrong artefact still chosen |

## 3. `D-3b` v4 — the control as it should be put to Boss

> **`D-3b`** — Authorise reading the PostgreSQL dumps already present on the execution host, **subject
> to the following being recorded with any claim derived from them**:
>
> 1. **`E1`** the authorisation itself, and its scope;
> 2. **`E2`** the client binary and version actually used — *and, where a read fails, whether another
>    client on the same host succeeds*;
> 3. **`E5`** the **claim type** being made, declared **first**;
> 4. **`E4`** the **ranking unit and objective** appropriate to that claim type, declared **before**
>    any artefact is opened;
> 5. **`E3`** the artefacts **materially relevant to that claim** — every generation the claim's own
>    unit requires, and **not** every artefact on the host;
> 6. the **excluded** artefacts and **why**.

## 4. Claim-type → unit map, so `E3` is bounded rather than blanket

**This table is the mechanism by which `D-3b` avoids becoming "open everything".**

| Claim type | Governing unit | Required coverage | Example |
|---|---|---|---|
| **Readability / capability** | dump **format version** | every distinct **version** | `P11-F-09` — 2 of 2 versions ⇒ complete |
| **Population negative** (*"X has never occurred"*) | **row count** in the bearing table | the artefact(s) **maximising** that row count | `P07-F-60` — failed: used a 23-row database |
| **Configuration / schema presence** | **populated tables** / installed modules | the **broadest** install | `P07` §4.1–4.5 — correct: used the broadest |
| **Cross-company / tenancy** | **company count** | every artefact with **>1 company** | untested in P11 |
| **Date / period coverage** | **date span** of the bearing table | artefacts spanning the periods claimed | untested in P11 |
| **Generation divergence** | **source generation** | **≥1 per generation** | `P01`'s v18-vs-v19 bridge question |

> **The same host, the same authorisation, four different correct answers to *"which database?"*
> depending only on the claim.** That is why `E4` and `E5` cannot be dropped, and why blanket coverage
> is not a substitute for them: opening every artefact still permits reasoning from the wrong one.

## 5. What v4 does **not** do

- It does **not** require every dump to be opened for every claim. **Explicitly forbidden by this
  prompt's C3 and by `P11-F-10`'s own logic** — coverage must be claim-relevant and denominator-declared.
- It does **not** authorise anything. `E1` is Boss's.
- It does **not** assert what the dumps contain. P11's extraction attempt was **refused by this
  session's permission boundary**; that refusal stands and is not worked around.

## 6. Cost, restated honestly for the decision

| Element | Cost |
|---|---|
| `E1` Boss authorisation | a decision |
| `E2` client version | **one command**, already executed by P11 — both versions present, `postgresql@18` reads all four |
| `E4` ranking | **one command**, already executed by P11 — the ranking is published at `P11-F-11` |
| `E3` coverage | claim-dependent; **≤4 artefacts** on this host |
| `E5` objective | free — it is a sentence written before opening anything |

> **Four of the five elements are already discharged or cost one command.** `D-3b` remains, as first
> filed, **among the cheapest unresolved items on the board** — and it is now specified precisely
> enough that discharging it cannot reproduce `P07-F-60`.
