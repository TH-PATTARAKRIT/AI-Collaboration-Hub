# 05 — DEEP LEVEL 2: FOUR EXPERT OPINIONS
**LAYER 2 — AUDIT QUARANTINE**

---

## EXPERT 1 — LEADER FUNCTIONAL DESIGN

**Supported.** The misleading-label table (`04` §4) is the most functionally
valuable output of this level. `UI-01` and `UI-03` are real user-harm findings,
not documentation nitpicks.

**Missing.** We now know 13 fields are invisible. We do not know what a user is
*required* to fill in. The form's required markers, the onchange cascade, and what
actually stops a confirm are still unexamined. Until then we cannot describe the
user's real task.

**Risky.** One wizard driving five accounting events (`UI-06`) is a training and
control risk, not just a UI oddity. A user who picks the wrong option in that
dialog can create a second asset record, or permanently close a running asset,
from the same button. There is no distinct permission on the individual actions.

**Challenge.** I challenge the phrase "Depreciation Board" being carried forward
at all. There is no board object. There are journal entries with a shared link. If
SMEsPlus builds a "board" entity it will diverge from the semantics on day one.

**Evidence required next.** What happens functionally when the user changes the
computation mode on a **running** asset. That is a Level 3 question and it is the
one I care about most.

**Assumed too early.** That the 217 running assets were configured deliberately.
Given that **all 280 are detached from their templates**, it is equally consistent
with a migration that set fields directly and never linked a model. That changes
what "the source system's configuration" even means.

---

## EXPERT 2 — LEADERSHIP DATABASE DESIGN

**Supported.** The field register does what I asked for at Level 1: it separates
stored from computed from related, and it confirms the recursion on book value.
`G1-04` is properly closed.

**Missing.** Indexes and constraints. One index is visible (the grouping field) and
one uniqueness question is wide open — see my challenge. Also: nothing yet states
which fields are `copy=False`, which decides what a duplicate asset inherits.

**Risky.** §6 states the finding I consider the most important in the whole level:
**the asset row is not the source of truth for its own value.** Residual is derived
from posted entries; book value is a recursive aggregate. Any migration, any
report, any integration that treats the asset table as authoritative will produce
numbers that do not tie. This should be written into the SMEsPlus data contract as
a first-class rule.

**Challenge.** I challenge the register's silence on **cardinality of the custom
equipment link**. A `Many2one` from asset to equipment with no inverse and no
unique constraint permits N assets to claim the same physical machine. On a
population of 280 assets this is not theoretical. I want it counted, and I am
raising it as a verification item, not an opinion.

**Evidence required next.** A count on the UAT of duplicate equipment references
across assets, and a count of parent/child asset relationships (`G1-03`).

**Assumed too early.** That the runtime counts describe a clean population. 35
records with no accounts and 280 records with no template is not a clean
population. It is a mid-migration snapshot, and every conclusion drawn from it
inherits that.

---

## EXPERT 3 — LEAD INTEGRATION & LOCALIZATION

**Supported.** The account-domain finding in `04` §2.5 is a genuine contribution
and it lands directly on a Boss design. The product **forbids off-balance accounts
on all three asset accounts**, from the field definitions, not from documentation.

**Missing.** This level still says nothing about Thai requirements. That is by
design, but it means the Off-Balance finding is currently only half of the
analysis: we know the product forbids it *there*; we do not yet know whether Thai
statutory reporting permits the Boss's construction *anywhere*.

**Risky.** The discovery that a Thai depreciation method exists **only in the v14
line** is the single highest-risk item in the session. If the UAT is running
without it, then 217 running assets are being depreciated on a convention that
does not match the one the business believes it uses, and the difference is not
cosmetic — it is a different amount in every month with 28, 29 or 31 days.

**Challenge.** I challenge the framing of the Thai method as a "custom module". It
is not an enhancement. It is a **compliance control** that somebody built because
the product could not meet a local requirement. Losing it in a version migration
is a compliance regression, and it should be recorded in those terms rather than
as a feature gap.

**Evidence required next.** Primary Thai statutory text — obtained at `26` — and
the actual computation mode of the 217 running assets on the UAT.

**Assumed too early.** That the standard *based on days per period* mode is an
acceptable substitute for the custom Thai method. They are both "daily" and they
are **not** the same arithmetic. Nobody has yet compared them line by line. I
insist that comparison happen before anyone proposes the standard mode as the fix.

---

## EXPERT 4 — LEAD CODE & UI ARCHITECT

**Supported.** Field visibility was extracted from the view definitions and diffed
against the model, which is the correct method. The menu finding — one menu item
in the entire module — is exactly the kind of fact that menu-first research misses.

**Missing.** The trace still stops before the method layer. We have fields and
views; we do not yet have the call chain from a button to a journal entry. That is
Level 3 and it is where the real answers are.

**Risky.** 13 invisible fields include two that drive money: the pause-day
accumulator and the stored gain-on-sale. A field that changes the schedule and
cannot be seen is an audit hole.

**Challenge.** I challenge `04` §5's module table on completeness grounds, again.
It lists modules found in this workspace. Three separate v18-line trees were found
carrying near-identical copies of the same custom modules at different version
strings. Which of those is deployed is unknown. Treating any of them as "the"
custom code is an assumption, and I want it labelled as one everywhere it is used.

**Evidence required next.** `G1-01` and `G1-02`, unchanged from Level 1. They did
not close and they will not close from static evidence.

**Assumed too early.** That reading the newest-looking copy of a custom module
tells us what runs. It does not.

---

## AAS+ CONSOLIDATION — LEVEL 2

### Agreements

1. The asset row is a derived view over its journal entries, not the source of
   truth for its own value. All four. **This is the level's headline.**
2. The product forbids off-balance accounts on the asset account triple. All four.
3. Seven UI labels materially misdescribe behaviour; `UI-03` is critical. All four.
4. The custom Thai depreciation method has no copy in any v18-line tree in this
   workspace. All four — with Expert 4's standing caveat that workspace ≠ server.

### Disagreements — preserved

| ID | Disagreement | Positions |
|----|-------------|-----------|
| `D2-01` | Whether the standard calendar-day mode can substitute for the custom Thai method | Expert 3: not until proven line-by-line equivalent. Experts 1/4: plausible substitute worth testing. **Deferred to `17`, which resolves it — see the AAS+ note below** |
| `D2-02` | Whether "Depreciation Board" should survive as a term | Expert 1: no, there is no such object. Expert 2: yes, as a report concept, provided it is never modelled as an entity. **Unresolved — recorded in `39`** |
| `D2-03` | Status of the runtime population | Expert 2: a mid-migration snapshot, weak basis for inference. Expert 1: still the only evidence of intent we have. **Both stand** |

**AAS+ note on `D2-01`:** Expert 3's demand was met inside this session. `17`
compares the two arithmetics directly and finds them **not equivalent**. Expert 3's
position is upheld on evidence. The disagreement is recorded as resolved-by-evidence
rather than deleted.

### Contradictions surfaced at Level 2

| ID | Summary | Register |
|----|---------|----------|
| `CTR-01` | The configured depreciation method has no implementation in the target version line | `37` |
| `CTR-03` | Two different asset models existed simultaneously in the legacy system, and the two custom capabilities the Boss relies on were attached to **different ones** | `37` |

### Evidence gaps — status

| ID | Gap | Status after Level 2 |
|----|-----|---------------------|
| `G1-01` | UAT installed module list | **Open** → `41` `UNR-04` |
| `G1-02` | UAT build identity | **Open** → `41` `UNR-05` |
| `G1-03` | Parent/child relationships among the 280 | **Open** → `41` `UNR-06` |
| `G1-04` | Field storage / recursion | **Closed** — `04` §2 |
| `G1-05` | Field visibility | **Closed** — `04` §3 |
| `G1-06` | Thai statutory text | Open, closes at `26` |
| `G2-01` | Duplicate equipment references across assets | **New, open** → `41` `UNR-08` |
| `G2-02` | Actual computation mode of the 217 running assets | **New, open, high priority** → `41` `UNR-02` |

### Consolidated position at the end of Level 2

The UI is a poor guide to this domain and, in seven identified places, an actively
misleading one. The functional truth lives in the method layer, which Level 3 now
has to open. Two structural facts are established and should not be re-litigated:
**value lives in the entries, not the asset row**, and **off-balance accounts are
forbidden on the asset account triple**.

The session's risk profile changed at this level. Before Level 2 the principal
risk was "SMEsPlus may design against a misunderstood source". After Level 2 it is
"**the running UAT may already be depreciating 217 assets on the wrong convention**".
That is an operational risk with a live population attached, and it is escalated to
the Boss pack accordingly.

### Gate to Level 3

Open. Level 3 must open the method layer and must, as its first priority, produce
the arithmetic comparison Expert 3 demanded.
