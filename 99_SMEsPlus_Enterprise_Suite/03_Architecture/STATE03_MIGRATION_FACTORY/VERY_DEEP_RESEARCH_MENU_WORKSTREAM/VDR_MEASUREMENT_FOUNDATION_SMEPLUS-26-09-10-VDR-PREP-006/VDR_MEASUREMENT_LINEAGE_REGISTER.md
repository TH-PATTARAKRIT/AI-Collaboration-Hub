# VDR_MEASUREMENT_LINEAGE_REGISTER.md
# Every result traceable through seven stages, none of them missing

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 05.

---

## 1. The required chain

```
RAW OBSERVATION → NORMALISED OBSERVATION → DERIVED FACT → CLASSIFICATION
                → COVERAGE ELIGIBILITY → NUMERATOR / DENOMINATOR → COVERAGE RESULT
```

**No stage may disappear.** Below, each measurement this round produced is traced through all seven.

## 2. Hop-0 population — the lineage in full

| Stage | Artefact |
|-------|----------|
| **Raw observation** | 12,075 Python files, 660 XML files, 44 access files; five deployment registries |
| **Normalised observation** | AST nodes and XML elements → `(kind, module, identity, pointer)`; COPY rows → registry records, malformed rows rejected and counted |
| **Derived fact** | the anchor set (51 models) → the domain set (99 modules) by the declared property test |
| **Classification** | each entity tagged `BOTH` / `SOURCE ONLY` / `RUNTIME ONLY` |
| **Coverage eligibility** | three kinds excluded from the agreement basis as structurally single-method, named and counted |
| **Numerator / denominator** | 4,537 corroborated / 9,170 comparable |
| **Coverage result** | **49.5% corroboration → population NOT CERTIFIED** |

## 3. Source presence — INS-01

| Stage | Artefact |
|-------|----------|
| Raw observation | the file at the pointer's path, and its line count |
| Normalised observation | `(path, line)` split from the pointer |
| Derived fact | does the path exist; is the line within the file |
| Classification | `SOURCE_RESOLVED` / `SOURCE_FILE_ONLY` / `SOURCE_UNRESOLVED` |
| Eligibility | entities carrying a pointer field |
| Numerator / denominator | resolved / eligible |
| Result | produced only for instruments the validator certifies |

## 4. Runtime observation — INS-02

| Stage | Artefact |
|-------|----------|
| Raw observation | the deployment's own registry record |
| Normalised observation | the identity namespace mapped between runtime and source form |
| Derived fact | the set of deployments carrying the entity |
| Classification | `OBSERVED` / `ABSENT` |
| Eligibility | entities for which a registry record **can** exist |
| Numerator / denominator | observed / eligible |
| Result | as above |

## 5. Where the chain broke in earlier rounds — recorded so it can be checked against

| Round | Stage that was missing | Consequence |
|-------|------------------------|-------------|
| PREP-003 | **observation** — a grade was an unconditional literal | 100% on a dimension no row could fail |
| PREP-004 | **observation** — six grades read a field the measurement wrote | 44.01% coverage that measured its own authoring |
| PREP-004 | **normalised observation** — a company-dependent value read without its company scope | a retraction of a correct finding |
| PREP-005 | none identified for the process dimension | the chain held; the result stood |

**Every one of those is a missing *observation* stage.** The register was read where an artefact should
have been.

## 6. The two breaks caught inside this round, before publication

| Break | Stage | Caught by |
|-------|-------|-----------|
| Two different field populations compared as one | **eligibility** | disbelief at the size of the disagreement |
| Two identity namespaces compared unnormalised | **normalised observation** | disbelief at a 0% agreement |

Both would have produced a publishable number. Neither reached a document.
