# 45 — EVIDENCE MANIFEST
**LAYER 2 — AUDIT QUARANTINE**

§81. Every evidence item with its identity, provenance and the claims it supports.
Detailed locators are in `28_SOURCE_LINK_REGISTER.md`; this file is the index plus
the integrity record.

## 1. Evidence classes used

| Class | §9 priority | Items | Used for |
|---|---|---|---|
| Primary source code — target generation | **1** | 15 | The whole of Levels 1–6 |
| Primary source code — project custom modules | **1** | 9 | `19`, `20`, `17`, `CTR-01`…`CTR-04` |
| Primary source code — legacy generation | **1** | 2 | `17` §2.1, `CTR-03` |
| Runtime system evidence | **2** | 3 | `04` §7, `14` §5 |
| Actual database records (via runtime read) | **3** | 2 | Population, account triples, template links |
| Project execution record | 5 | 1 | Corroboration of the runtime population |
| Official Thai authority | **7** | 2 | `26` §2 — **primary statutory text** |
| Professional / practice secondary | 11 | 2 | Corroboration only; never load-bearing alone |
| Derived analytic reproduction | — | 2 | Every numeric scenario, classified `SUPPORTED INTERPRETATION` |
| Prior AI research | 12 | 1 | Audit lineage only — `29` |

**Total distinct source identifiers: 39.**

## 2. Evidence NOT used, deliberately

| Not used | Why |
|---|---|
| **Official product documentation** (§9 priority 6) | Deliberately excluded. The prior session was confined to it; this session tests its conclusions against source. Using it here would have re-imported the same limits |
| Forum, community and vendor blog material about the reference product | Same reason |
| Prior AI interpretation as a basis for new conclusions | Used only as lineage to be re-tested (`29`) |

## 3. Integrity of the derived evidence

`EV-SIM-01` and `EV-SIM-02` are the only artefacts this session produced that
generate numbers. Their integrity rests on three things, all stated so a reviewer can
attack them:

1. **They are transcriptions, not re-implementations.** Each method corresponds
   one-to-one with a named method in primary source, in the same order, with the same
   guards.
2. **Their standing assumption is declared**: fiscal year = calendar year, not
   verified per company. Any non-calendar fiscal year changes period boundaries.
3. **They are classified `SUPPORTED INTERPRETATION` everywhere their output is
   used**, and never `FACT VERIFIED`. Their outputs should be confirmed against one
   real asset on the pilot system before any migration decision relies on them.

Where a simulated result is also corroborated by runtime evidence or by the project's
own records, that is stated at the point of use.

## 4. Claim-to-evidence coverage

| Deliverable | Primary evidence | Runtime | Statutory | Derived |
|---|---|---|---|---|
| `02` `03` Level 1 | ✔ | ✔ | — | — |
| `04` `05` Level 2 | ✔ | ✔ | — | — |
| `06` `07` Level 3 | ✔ | ✔ | — | ✔ |
| `08` `09` Level 4 | ✔ | — | — | — |
| `10` `11` Level 5 | ✔ | ✔ | — | — |
| `12` `13` Level 6 | ✔ | ✔ | — | ✔ |
| `14` `15` | ✔ | ✔ | — | — |
| `16` `17` | ✔ | — | ✔ | ✔ |
| `18` | ✔ | — | — | ✔ |
| `19` `20` | ✔ | — | — | — |
| `21` `22` | ✔ | — | — | — |
| `23` `24` `25` | ✔ | — | — | — |
| `26` | — | — | ✔ | — |
| `27` | ✔ | — | — | — |
| `30`–`36` matrices | ✔ | ✔ | ✔ | ✔ |
| `37` `38` `39` `40` `41` | ✔ | ✔ | ✔ | ✔ |

**No deliverable rests on derived evidence alone.**

## 5. Package integrity

A SHA-256 manifest of all files in this package is generated at commit time and
stored as `SHA256SUMS.txt` alongside these files.

Repository, branch, and commit identity are recorded in the session record and
reported at the Final Gate handoff (§95).

## 6. Reviewer

Executed and self-reviewed by the AI session, with four independent expert
perspectives applied at every level and a final independent challenge at `42`.
**No human review has occurred.** PMO verification is at `43`. Boss Final Review is
the next and only approval point.
