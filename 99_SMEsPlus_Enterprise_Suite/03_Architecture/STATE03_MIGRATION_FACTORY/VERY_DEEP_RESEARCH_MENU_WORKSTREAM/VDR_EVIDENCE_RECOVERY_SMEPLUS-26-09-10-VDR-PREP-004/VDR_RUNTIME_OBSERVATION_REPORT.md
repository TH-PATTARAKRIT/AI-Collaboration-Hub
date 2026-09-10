# VDR_RUNTIME_OBSERVATION_REPORT.md
# Element-level runtime observation — the largest evidence advance in this programme

Session `[SMEPLUS-26-09-10-VDR-PREP-004]` · Layer: **LAYER 1 — CLEAN-ROOM.**
Checkpoint 08. Register **V5**.

---

## 1. What changed, and why it is not a relaxed predicate

PREP-003 closed with **Runtime Observed Coverage = 1.52% (77 items)**. Everything else was
*module-installed*, which is an inference about an element from a fact about its container.

The gap was never a reasoning gap. It was that **the table which records, per deployment, every element
that deployment actually installed had never been extracted.** This round extracted it, from all five
deployment identities, without starting a database server.

> **The number moved because new evidence was read, not because the bar was lowered.** The bar is
> unchanged and is stated in §3: an element is `RUNTIME OBSERVED` only when the deployment's **own
> registry** carries a record of **that element**, joined on the element's own identity.

## 2. Evidence base and instrument

| Clause | Value |
|--------|-------|
| **POPULATION** | the 5,074 frozen learning items |
| **PATH SET** | five deployment identities across three generations, extracted to `LAYER2_AUDIT_QUARANTINE/MACHINE_REGISTERS/runtime/` |
| **PATTERN** | `pg_restore --data-only -t <table>` per table, then a COPY-block parser; **no server started, at any point** |
| **UNIT** | one *(item, deployment)* observation |
| **TABLES READ** | the element registry, the field registry, the installed-module table, the group table, the access table, the constraint table, the scheduled-job table, the parameter table, the company table — **10 tables × 5 deployments** |

Registry sizes actually parsed — published so a reader can see the instrument had something to work on:

| Deployment | Generation | Registry records | Field records | Models | Constraints | Installed modules |
|-----------|-----------|-----------------:|--------------:|-------:|------------:|------------------:|
| `BK12MAY26` (transacted) | 19 | 62,445 | 16,009 | 756 | 3,545 | 251 |
| `iEVING` | 19 | 39,985 | 15,622 | 749 | 3,502 | 232 |
| `iTEST02` | 19 | 192,054 | 23,112 | 1,035 | 5,308 | 453 |
| `iSMEs` | 16 | 107,873 | 11,992 | 507 | 2,696 | 190 |
| `idemo18_uat` | 18 | 225,529 | 19,431 | 819 | 4,503 | 361 |

### Controls

- **Positive control, drawn from the corpus:** an identity taken from the deployment's own registry is found. **Negative control:** a fabricated identity is not found. *The predicate can fire and can fail* — the second half is the one this programme has repeatedly omitted.
- **Coverage assertion:** every COPY block's parsed row count is published above; rows whose field count does not match the declared column list are counted and rejected rather than silently padded — a generation-specific schema defect this programme has on record.
- **Second shape:** module-level installation was derived independently from the installed-module table and cross-checked against element presence; the two disagree in exactly the direction expected (elements are a subset of installed modules), never the reverse.

## 3. The evidence grades — and the honest boundary of each

An element is graded by **what record actually exists for it**, never by what would be convenient.

| Tier | Meaning | Classes | Applicable | Observed | % |
|------|---------|---------|-----------:|---------:|--:|
| **ELEMENT** | the deployment's own registry holds a record of **this element** | field · view · action · menu · extension menu · rule · group · scheduled job · sequence · object · constraint · settings field · handoff object | **3,319** | **2,854** | **86.0%** |
| **INDIRECT** | the element has **no record of its own**; its immediate parent was observed | button (parent view observed) · access rule (governed model observed) | 611 | 542 | 88.7% |
| **MODULE** | **no ORM record can exist** for this kind of thing | behaviour (a Python method) · gated view sub-element · system parameter | 1,144 | 1,061 | 92.7% |
| **ALL** | | | **5,074** | **4,457** | **87.8%** |

**Only the ELEMENT tier is graded RESEARCH-VERIFIED.** The other two are `DETERMINED`. This matters:
**2,854 is the honest runtime number, not 4,457**, and the 1,144 MODULE-tier items are not a research
failure — a Python method and a view sub-element are not database records, and no amount of further
extraction will make them so. §9 requires that limitation to be documented and ruled on by SMEs Core
rather than asserted by the producer; it is documented here and carried to them.

### Per class

| Class | n | Observed | % | Route |
|-------|--:|---------:|--:|-------|
| FIELD | 1,846 | 1,589 | 86.1% | its own field record |
| VIEW | 493 | 429 | 87.0% | its own registry record |
| ACTION | 201 | 187 | 93.0% | its own registry record |
| SETTING | 237 | 180 | 75.9% | its own settings-field record |
| MENUX | 134 | 110 | 82.1% | its own registry record |
| OBJECT | 96 | 90 | 93.8% | model registered |
| HANDOFF | 90 | 79 | 87.8% | model registered |
| MENU | 62 | 53 | 85.5% | its own registry record |
| RULE | 46 | 44 | 95.7% | its own registry record |
| GROUP | 44 | 43 | 97.7% | its own registry record |
| CONSTRAINT | 32 | 29 | 90.6% | constraint record |
| SEQUENCE | 12 | 10 | 83.3% | its own registry record |
| **AUTOMATION** | **26** | **11** | **42.3%** | its own registry record |
| BUTTON *(indirect)* | 431 | 368 | 85.4% | parent view observed |
| ACL *(indirect)* | 180 | 174 | 96.7% | governed model observed |
| BEHAVIOUR *(module)* | 614 | 553 | 90.1% | not an ORM record |
| GATEDELEM *(module)* | 525 | 504 | 96.0% | not an ORM record |
| SYSPARAM *(module)* | 5 | 4 | 80.0% | not an ORM record |

## 4. Findings

### `R4-F-01` — Runtime Observed Coverage rises from 1.52% to 56.25% of the applicable population
2,854 of 5,074 items are now observed **as themselves** on at least one real deployment. Measured
against the sub-population for which an element record can exist at all, it is **2,854 of 3,319 = 86.0%**.
Both figures are published; neither is presented as the other.

### `R4-F-02` — 617 items are determined ABSENT, and that is a result
Their own record is in no deployment's registry. This is not "unmeasured" and not a gap: it is a
determination, from the deployment's own record of itself. They remain in the population, are not
excluded, and are the honest complement of the 2,854.

### `R4-F-03` — scheduled jobs are the weakest class at 42.3%, and they are the class that acts unattended
Only 11 of 26 automations are present on any observed deployment. Automations act without a user
present, so an unobserved automation is the least visible kind of unverified element in the domain.
This is now the lowest-covered element class and the one whose absence of evidence carries the most
operational risk.

### `R4-F-04` — the previous round's 62-menu figure resolves to 53, from the deployments' own records
PREP-003 published 62 menus runtime-verified; a challenger corrected it to 49 by removing menus
installed on no deployment. Measured directly against the registries: **53 of 62 menus are observed**.
The correction's *direction* was right and its *value* was not, because it was derived by subtracting a
suspect group rather than by joining to the authority. **Both prior figures are superseded by the
join.**

### `R4-F-05` — the domain's element surface differs across generations by more than module count suggests
The current-generation transacted deployment carries 756 models and 16,009 fields; the 16-generation
deployment carries 507 and 11,992. The 18-generation deployment carries the largest registry of all
(225,529 records) on 361 modules. **Registry size does not track module count**, so any inference from
"how many modules are installed" to "how much surface exists" is unsafe — including the inference the
MODULE tier above is forced to make for 1,144 items.

## 5. What this does NOT establish

- **Observed is not exercised.** An element present in a registry has been *installed*, not *used*. Row-level use was measured separately for persistent objects only.
- **The MODULE tier stays inferential** for 1,144 items, and no extraction can change that. Closing it needs controlled execution or log evidence, and is stated as outstanding work rather than as a limitation of the evidence base.
- **The five deployments are not established as the whole population of deployments.** That question belongs to the evidence-admission register, not here.
