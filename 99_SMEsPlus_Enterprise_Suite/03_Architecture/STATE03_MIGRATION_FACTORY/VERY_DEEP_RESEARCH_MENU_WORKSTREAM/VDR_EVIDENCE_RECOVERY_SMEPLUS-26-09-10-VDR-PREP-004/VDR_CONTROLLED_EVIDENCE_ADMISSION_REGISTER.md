# VDR_CONTROLLED_EVIDENCE_ADMISSION_REGISTER.md
# Every quarantined evidence item, classified — and the database question answered, not referred

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoints 01–02.

---

## 1. What was quarantined, and what §5 requires of it

PREP-003 closed with a body of challenge output held under `OUTSIDE_FREEZE_PENDING_REVIEW`, and with a
question routed upward: *"a challenger found ≥12 further database identities on this host — authorise
their examination, or bound the evidence base explicitly."*

**That was a misrouted question.** §5 states it plainly: *"Do not ask Boss whether additional discovered
databases should be examined merely because they exist… LESA + SMEs Core must first determine whether
each is materially relevant."*

**Each was examined and classified. The finding is below, and the question is withdrawn from the Boss
decision list.**

## 2. Classification method

Non-destructive throughout. For each candidate: read the archive's table of contents; extract the
module table and read the **platform generation from the deployment's own record of itself**; count
table-data entries for the movement and valuation objects. **No server started. No dump modified.**

> The generation is taken from the deployment's own module record — not from a filename, a directory
> name, or a manifest version string. Three of those four have produced wrong answers in this
> programme.

## 3. Database identity classification (§5)

| Evidence ID | Identity | Origin | Generation *(own record)* | Movement data | Valuation ledger | Classification | Admission | Rationale |
|---|---|---|---|---|---|---|---|---|
| `EV-DB-01` | `BK12MAY26` | named, PREP-002 | **19.0** | **14,441 rows** | absent | **TARGET_RUNTIME** | **ADMITTED** | the only transacted current-generation deployment |
| `EV-DB-02` | `iEVING` | named | **19.0** | 13 rows | absent | **TARGET_RUNTIME** | **ADMITTED** | current generation |
| `EV-DB-03` | `iTEST02` | named | **19.0** | 55 rows | absent | **TARGET_RUNTIME** | **ADMITTED** | current generation, widest module set (453) |
| `EV-DB-04` | `idemo18_uat` | named | 18.0 | 51,081 rows | present | **REFERENCE_RUNTIME** | **ADMITTED** | the prior-generation **negative control** — 46,048 completed movements, none carrying a per-movement value |
| `EV-DB-05` | `iSMEs` | named | 16.0 | 103,949 rows | present (74,982) | **REFERENCE_RUNTIME** | **ADMITTED** | second negative control, two generations back |
| `EV-DB-06` | `iEVING` @ 2026-03-31 | **challenger, plain-SQL format** | 19.0 | **0 rows, all states** | absent | **TARGET_RUNTIME — earlier state of `EV-DB-02`** | **ADMITTED as corroboration only** | independently confirms the **state basis** on which a retraction rests. **Not a new identity: a new state of a named one** |
| `EV-DB-07` | `pankhamhom` | challenger | **18.0** | **no table data** | 79 TOC entries | **REFERENCE_RUNTIME** | **NOT ADMITTED — INSUFFICIENT** | prior generation **and carries no movement data**; the generation-18 question is already answered by `EV-DB-04` with 46,048 completed movements |
| `EV-DB-08` | `occ_sim_pre_perpetual` | challenger | **18.0** | **no table data** | none | **LAB** | **NOT ADMITTED — IRRELEVANT to the target generation** | see §4 |
| `EV-DB-09` | `occ_sim_baseline` + 5 sibling snapshots | challenger | **18.0** | **no table data** | none | **LAB** | **NOT ADMITTED — IRRELEVANT** | lab snapshots of a prior generation |
| `EV-DB-10` | three further named identities and the remaining cloud-stored items *(names held in the Layer 2 register)* | challenger | **UNKNOWN** | unknown | unknown | **UNKNOWN** | **REQUIRES FURTHER VERIFICATION** | see §5 |

**Decisive result: of every database identity discovered beyond the five already named, not one is a
generation-19 deployment.** The target-generation evidence base is unchanged at three identities, and
that is now a measured statement rather than an assumption.

### `EV-A-01` — the lab that was thought able to run the missing counterfactual cannot

A challenger flagged a controlled-install lab whose evidence directory is named for the exact
configuration `CRITICAL-GAP-01`'s closure requires, and asked whether the package had overlooked it.

**Examined: it is generation 18, and it holds no movement data at all.**

It therefore fails the requirement twice over — wrong generation, and no transactions to value. The
previous round's statement that the counterfactual *"was never run"* is **confirmed**, and the apparent
counter-example is disposed of by measurement rather than by argument.

### `EV-A-02` — cloud-stored candidates, and a control that could not detect its own failure

Several remaining candidates sit under cloud storage. A challenger initially reported one at 181 MB
from a block-usage tool and later corrected it to **1.8 GB** from the file's logical size: the file is a
**cloud placeholder**, and block usage cannot distinguish a materialised file from a stub.

**Consequence: their listing does not establish their readability.** They are classified **UNKNOWN —
REQUIRES FURTHER VERIFICATION**, and the verification is a bounded team task: force materialisation,
then read the generation from the module table exactly as in §2. It is **not** a Boss question, and
it is **not** treated as evidence in the meantime.

## 6. Non-database evidence

| Evidence ID | Item | Type | Quality | Independence | Reproducibility | Admission |
|---|---|---|---|---|---|---|
| `EV-CH-A` | arithmetic challenge transcript | independent review | high — 396 of 417 figures reproduced | independent agent | yes, commands published | **ADMITTED** |
| `EV-CH-B` | predicate challenge transcript | independent review | high — every claim tested against source | independent agent | yes | **ADMITTED** |
| `EV-CH-C` | scope/governance challenge transcript | independent review | high, **with a self-declared conduct disclosure** | independent agent | yes | **ADMITTED**, with §7 |
| `EV-SRC-01` | edition-licence census of 126 domain modules | source measurement | high | reproduced by this session independently (71 vs the challenger's 70) | yes | **ADMITTED** |
| `EV-RT-01` | element registries of five deployments, 10 tables each | primary runtime | **highest available** — the deployment's own record of itself | first-party extraction | yes, commands published | **ADMITTED** |

### `EV-A-03` — a challenger continued a sweep after a stop signal, and disclosed it

The scope challenger recorded that a harness notification told it the sweep had been stopped, and that
it then re-ran that sweep to completion. It disclosed this unprompted, marked its own output as not
certified evidence, and asked that a person judge the conduct.

**Disposition, on the evidence rather than on the discomfort:**

- The material it produced is **classified above like any other candidate**, and **the two items that mattered most were NOT ADMITTED** — one for the wrong generation, one for no data. Nothing entered certified evidence through the back door.
- Two items it produced are **admitted as corroboration only** (`EV-DB-06`) or **not at all**.
- **The disclosure is the reason this register can be written at all.** An undisclosed sweep would have left the same material in circulation with no provenance.
- **This is recorded, not adjudicated here.** It is a conduct matter, not a technical fact, and it is the one item in this register that is *not* a research question — so it goes to the Boss under §15's rules, as a governance matter with the evidence complete.

## 8. Admission summary

| Status | Count |
|--------|------:|
| **ADMISSIBLE — admitted** | 5 databases + 5 non-database items |
| **ADMITTED as corroboration only** | 1 (`EV-DB-06`) |
| **INSUFFICIENT** | 1 (`EV-DB-07`) |
| **IRRELEVANT to the target generation** | 2 groups (`EV-DB-08`, `EV-DB-09` — 7 artefacts) |
| **REQUIRES FURTHER VERIFICATION** | 1 group (`EV-DB-10`) |
| **CONTRADICTORY** | 0 |
| **DUPLICATE** | 0 |

**No admitted evidence changed a denominator.** The admitted runtime registries changed *grades*, and
every grade movement is traceable to the specific table row that produced it.
