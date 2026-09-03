# 13 — DEEP LEVEL 6: FOUR EXPERT OPINIONS
**LAYER 2 — AUDIT QUARANTINE**

---

## EXPERT 1 — LEADER FUNCTIONAL DESIGN

**Supported.** §4's single sentence — *none of the production failure cases can even
be expressed* — is the correct and honest result. Fourteen carefully constructed
operational scenarios all collapse into one structural fact, and saying so once is
better than pretending fourteen separate analyses happened.

**Missing.** The level tests the system. It does not test **the people**. Every
finding classed "permitted, no validation" (`FAIL-X02`, `FAIL-A02`, `FAIL-A04`) is
a control that currently depends on an accountant not making a mistake, across 280
records. Nobody has asked what compensating controls exist.

**Risky.** `FAIL-P09`. Machine cost lands in the period the **order completes**, not
the period the machine **ran**. For a concrete plant with continuous production
that may be tolerable. For anything with long orders it is a systematic
misstatement, and SMEsPlus will inherit it silently if it reuses the chain.

**Challenge.** I challenge the framing of §1's conclusion, "the engine holds". It
holds *arithmetically*. `FAIL-D16` is an open lock-date question and `FAIL-D14`
permits changing the depreciation method mid-life with future-only effect — which
is arithmetically clean and, in accounting terms, a change in estimate that
normally requires disclosure. The engine permits it silently. That is not an
arithmetic failure and it is still a failure.

**Evidence required next.** What compensating controls the customer actually
operates today.

**Assumed too early.** That fifteen held attacks means low risk. Fifteen attacks
held **on the part nobody is proposing to change**. Every attack that failed was on
custom code, configuration or cross-module boundaries — which is exactly what
SMEsPlus is proposing to touch.

---

## EXPERT 2 — LEADERSHIP DATABASE DESIGN

**Supported.** `FAIL-X12` and `FAIL-G02` are the two findings I care about most and
both are correctly stated. The invariant is ORM-enforced; the import field is a
sanctioned way to break sub-ledger/GL agreement. Both bear directly on a
mid-migration UAT.

**Missing.** Neither has been **measured**. We know the import field can create
divergence; we do not know whether it was used on the 280, or on how many, or for
how much. That is one query and it converts a risk into a number.

**Risky.** `FAIL-X04`, still. I have raised the duplicate-equipment-link exposure at
three consecutive levels and it remains uncounted. If the SMEsPlus costing design
is going to key machine cost on that association, its uniqueness is not a data
hygiene detail — it is a **correctness precondition**. Two assets pointing at one
machine will double that machine's cost pool.

**Challenge.** I challenge §3's `FAIL-G01` entry, "cannot diverge for posted lines".
That is true only while the entries are read through the same exclusions the engine
uses — reversals excluded, reversed entries excluded, value-change entries excluded
from cumulative depreciation. A report that sums the entries naively **will**
diverge. The invariant is in the engine's reading, not in the data.

**Evidence required next.** Counts, on the UAT: import-field usage, duplicate
equipment links, parent/child relationships, analytic divergence. Four queries.
They have been requested since Level 1.

**Assumed too early.** That the migration used the ORM. Nobody has established it,
and `FAIL-X12` only bites if it did not.

---

## EXPERT 3 — LEAD INTEGRATION & LOCALIZATION

**Supported.** §7. Six tax scenarios, six impossibilities. That is the cleanest
localisation finding in the package and it is now established beyond argument.

**Missing.** The level does not state what the **customer does today** about the
book/tax difference. They have been filing Thai corporate tax returns on these
assets for years. Whatever they do — a spreadsheet, a manual adjustment — is an
existing requirement specification and nobody has asked for it.

**Risky.** §7 combined with `16` §3.4 produces a compounding exposure that neither
finding shows alone. The statutory rates are **ceilings**; the accounting schedule
is the only schedule; and the accounting schedule's monthly amounts depend on a
convention that may have been set by default. So the tax position is being derived
from a single schedule whose configuration nobody has verified. That is the
sentence I want in the Boss pack.

**Challenge.** I challenge §5 `FAIL-R08` being presented as a discovery about
residual. It is more than that. Writing out the **full original cost** against
accumulated depreciation at disposal, with the balance to gain or loss, is the
standard and correct derecognition treatment. What is non-obvious is that the
system **also** silently removes salvage from book value on closure, so the
gain/loss figure and the book value the user last saw are computed on different
bases. That is a presentation inconsistency inside a correct accounting treatment,
and it should be described that way rather than as a residual defect.

**Evidence required next.** `UNR-03` — Thai treatment of depreciation absorbed into
inventory — still unanswered after six levels. And the customer's current book/tax
reconciliation practice.

**Assumed too early.** That "off-balance" is a safe container. §9 admits we never
established how that account type behaves in statutory reporting. The entire
management-ledger design rests on an untested assumption about one account
classification.

---

## EXPERT 4 — LEAD CODE & UI ARCHITECT

**Supported.** §9 is the part of this level I most want preserved: a declared list
of **attacks that could not be executed**. Six of them. That is the difference
between an adversarial review and a confident one.

**Missing.** No attack was mounted against the **custom modules' own failure
modes** beyond the three inert constructs already found. Nobody tested what happens
when the custom equipment-status flip runs against an equipment record that is
already flipped, or archived, or deleted.

**Risky.** `FAIL-X14`. Three constructs in one small custom module target framework
generations that have passed, and **none of them raises an error**. Silent
inertness is the worst failure mode available: the code is present, it is
reviewed, it is believed, and it does nothing. There is no reason to think this
module is unique.

**Challenge.** I challenge §1's scoreboard framing — "sixteen attacks, fifteen
held". Counting attacks makes a robust engine look like a validated system. The
engine was never the risk. Reporting fifteen-of-sixteen as a score risks the reader
concluding the domain is safe. I would delete the scoreboard and keep the findings.

**Evidence required next.** Everything that needs the running system. Six levels
have now produced a consistent list and it has not shortened.

**Assumed too early.** That static analysis can close this domain. It cannot, and
the honest conclusion of Level 6 is that **the remaining risk is concentrated
exactly where static evidence stops**.

---

## AAS+ CONSOLIDATION — LEVEL 6

### Agreements

1. The depreciation engine is arithmetically sound: no drift, no plug entries, no
   off-by-one at any tested boundary including 29 February and the 31st. All four.
2. The risk is not in the engine. It is in configuration, custom code, cross-module
   boundaries and migration. All four.
3. No tax book. Six for six on the tax scenarios. All four.
4. Silent inertness in custom code (`FAIL-X14`) is the most dangerous class of
   defect found. All four.
5. `FAIL-P09` — cost recognised on completion, not on use — will be inherited by
   any design reusing the production chain. All four.

### Disagreements — preserved

| ID | Disagreement | Positions |
|----|-------------|-----------|
| `D6-01` | Whether the §1 scoreboard should be reported at all | Expert 4: delete it, it misleads. Expert 1: keep it but do not call it a pass. **Partially resolved — §1 keeps the count and carries an explicit statement that the engine is not where the risk is. Expert 4's objection stands on the record** |
| `D6-02` | Whether mid-life method change is a failure | Expert 1: yes — a change in estimate permitted silently. Expert 4: not a code failure. **Both correct at different layers; recorded in `39` as a design requirement for SMEsPlus to add disclosure** |
| `D6-03` | Characterisation of `FAIL-R08` | Expert 3: the derecognition is correct; the inconsistency is presentational. **Resolved in Expert 3's favour — `18` §6 rewritten to say so** |

### The Level 6 verdict

Six levels of adversarial work produce one consolidated statement:

> **The reference asset engine is sound and worth learning from. Everything around
> it — the configuration that selects its behaviour, the custom code that extends
> it, the boundaries it does not cross, and the migration that populated it — is
> where every unresolved risk in this session now sits.**

And, as Expert 4 puts it, that is precisely where static evidence stops. The
session's remaining blockers are therefore not failures of research effort; they
are the boundary of what this method can reach.
