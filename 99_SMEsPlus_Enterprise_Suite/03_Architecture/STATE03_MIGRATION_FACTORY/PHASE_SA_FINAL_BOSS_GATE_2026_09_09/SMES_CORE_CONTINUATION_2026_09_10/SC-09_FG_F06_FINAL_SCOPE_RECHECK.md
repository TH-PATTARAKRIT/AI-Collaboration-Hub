# SC-09 — `FG-F-06` FINAL SCOPE RE-CHECK AND SMT DISPOSITION

## `CP-SA-SC-90 — FG-F-06 CORRECTED SCOPE RE-CHECK AND SMT DISPOSITION COMPLETE`

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001` · head consumed `25f727a9`
Primary text read: `99_SMEsPlus_Enterprise_Suite/00_Project_Governance/SMEPLUS_VERY_DEEP_RESEARCH_8_CRITERIA_UNIVERSAL_EXIT_CONSTITUTION.md`
Blob `50a60201` — **identical at `HEAD` and at `origin/SMEsPlus`**, so there is no version ambiguity.
**This file does not answer `FG-F-06`. Only Boss may state the scope of a Boss-approved constitution.**

---

## 1. The question, unchanged

> **Does `SMEPLUS-DR-EXIT-8C-001` (`BOSS APPROVED / PROJECT-WIDE MANDATORY`) bind the Phase SA exit?**

- **Reading A** — it binds. `EC-07` then requires two consecutive clean independent passes; **zero** have
  occurred; `B-7` becomes **gate-blocking**.
- **Reading B** — it does not bind this architecture exit; it applies to research and State-exit contexts
  as specified. The gate stands on `SC-05`'s categories.

---

## 2. Clause-by-clause, at primary text

**Header** — `Scope: ALL MODULES / ALL STATES / ALL FUTURE VERY DEEP RESEARCH`. Three subjects. *Phase*
is not among them.

| Clause | Exact subject | Engaged by the Phase SA → Pre-Test exit? |
|---|---|---|
| **§2.1** Every Module undergoing Very Deep Research | **Module** | **No** — Phase SA is not a Module |
| **§2.2** Every Domain/Wave inside a Module | **Domain/Wave** | **No** |
| **§2.3** Every STATE before advancement to the next STATE | **STATE** | **No** — carried forward from `SC-04`; Phase SA sits **inside** `STATE03` |
| **§2.4** *Cross-Module and Whole-System State Integration Review* | **a named review** | **CONTESTED — Reading A's principal ground. See `SC-F06-01`** |
| **§2.5** programmes *designated by Boss as Very Deep Research* | **a Boss designation** | **CONTESTED — see `SC-F06-02`** |
| **§4** Module Exit Rule — *"No **Module** may advance to its next controlled phase or State"* | **Module** | **CONTESTED — Reading A's second ground. See `SC-F06-03`** |
| **§5** State Exit Rule — *"a State Integration Very Deep Review … **at State level**"* | **STATE** | **No, not yet** — carried forward from `SC-04` |
| **§6** Research Depth Rule — the `/L99999.99999` label | **a depth label** | **Not an independent ground — see `SC-F06-02`** |
| **§9** AAS+ / Design Handoff Rule | **AAS+ provisional design** | **No** — `AR-F-02`; withdrawn as a Reading A ground at `SC-04` §6.3 |
| **`EC-07`** — *"Before **Final Research Gate**"* | **a Research Gate** | **Consequence, not ground.** Phase SA's gate is an architecture gate; Phase S was the research |
| **§11** *"NO MODULE MAY ADVANCE TO THE NEXT CONTROLLED **STATE**"* | **Module → STATE** | **No — and see `SC-F06-03`** |

---

## 3. Three findings this re-check adds

### `SC-F06-01` — the sequence-position test `SC-04` already trusted is not carried to §2.4

`SC-04`'s clause table resolves **§2.3** and **§5** with one test: *does this gate sit at the
`STATE03 → STATE04` boundary?* Both answer **No**, because Phase SA's exit is to Pre-Test.

**It then leaves §2.4 open on a different and weaker test** — activity similarity:

> *"Phase SA's own artefact directories are `PHASE_SA_CROSS_MODULE_ASSURANCE`, `..._CROSS_MODULE_RECHALLENGE`,
> `..._CROSS_MODULE_CONTRACT_PROOF`. **Whether that is the named review is the question**."*

**§2.4's referent is not free-floating. The instrument defines it.** §2.4 names
*"Cross-Module and Whole-System **State Integration Review**"*; **§5 names the same review and schedules
it**: *"the State must undergo a **State Integration Very Deep Review** using the same eight criteria
**at State level**"*, in a mandatory sequence whose position is exact:

`Module VDR → Module 8-Criteria Exit Gate → All in-scope Modules evidence-ready → `**`State Integration Very Deep Review`**` → State 8-Criteria Exit Gate → Boss Final State Decision → Next State`

**The review §2.4 names is the step §5 places immediately before the State Exit Gate and the Boss Final
State Decision.** The Phase SA → Pre-Test gate does not occupy that position — on `SC-04`'s own finding
that §5 is *"No, not yet"*.

> **Applying `SC-04`'s own test to §2.4 answers it the same way it answered §2.3 and §5.**
> **On resemblance of activity, §2.4 is Reading A's strongest ground. On position in the sequence the
> instrument itself defines, it is not engaged.**

**What this does NOT settle.** Boss may have intended §2.4 to attach to the **activity** wherever it
occurs, precisely because §2.4 is the one item in §2 that names an activity rather than a unit. That
reading is available on the text and **is not disproved here**. `SC-F06-01` moves §2.4 from *undetermined*
to *determined-by-intent*, and intent is Boss's alone.

### `SC-F06-02` — §6 and §2.5 are one ground, and it runs backwards

§2.5 engages only for *"research programmes **designated by Boss** as Very Deep Research."* The evidence
offered for that designation is the `/L99999.99999` label carried by every Phase SA prompt.

**§6 is what defines that label, and it makes designation the antecedent, not the consequent:**

> *"**For Boss-designated Very Deep Research**, the operating research depth is: `VERY DEEP / L99999.99999`.
> … It is the project control label meaning research must continue beyond L12 whenever evidence, unknowns,
> contradictions, failure classes, dependencies, or convergence defects require deeper investigation."*

The rule reads *designated → label*. Offering the label as proof of the designation **affirms the
consequent**. `SC-V-01` already measured the antecedent directly and found it absent: the Phase S
conditional-closure ruling and the Boss-approved architecture rulings return **0** hits for
`EC-01`…`EC-08`, `8C-001`, *8-Criteria* and *eight criteria*, on an instrument that fires **19** times on
`SA_FINAL_06`.

**So §6 is not a second ground; it is the evidence offered for §2.5, and it is the weaker direction of a
conditional.** The prompt's own §4.3 instruction — *"Do not infer that `/L99999.99999` alone makes Phase SA
Very Deep Research"* — is what the clause itself says.

**What this does NOT settle.** Only Boss knows whether the label was attached **as** a designation. If it
was, §2.5 engages and the direction of the conditional is irrelevant.

### `SC-F06-03` — §4's ground rests on the constitution's single use of the word *phase*, and §11 drops it

| Shape | Instrument | Result |
|---|---|---|
| **1** | `grep -oic "phase"` over the whole 257-line constitution | **1** occurrence |
| **2** | `grep -nE "No Module may advance\|NO MODULE MAY ADVANCE"` — the two operative sentences | **L158** *"next controlled **phase** or State"* · **L251** *"THE NEXT CONTROLLED **STATE**"* |

**The word *phase* appears exactly once in the instrument**, at §4 L158. §11 — the *Project-Wide
Constitutional Rule*, the clause that states the constitution's effect *"Effective immediately"* — restates
the same Module rule and **its destination is `STATE`, not phase**.

Reading A's §4 ground therefore rests on a single word that the instrument's own project-wide restatement
does not carry. **And §4's subject is in any case the *Module*** — the gated entity is a Module advancing,
not a phase exiting.

**What this does NOT settle.** §4 is the operative Module Exit Rule and §11 reads as a summary; **a summary
that omits a term does not necessarily repeal it.** And if the Account **Module** is what moves from
Phase SA to Pre-Test, then Pre-Test is that Module's *"next controlled phase"* and §4 engages on its
plain words. **That is a live reading and is not disproved here.**

---

## 4. Phase S research closure vs Phase SA architecture exit

Carried forward, not re-opened: the Boss closure describes Phase SA as *"synthesis; architecture;
conceptual/domain design … **and controlled return to Very Deep Research where required**"* — language that
treats Phase SA as **not itself** Very Deep Research, and that presupposes a **return** would be a distinct
act. `EC-07`'s trigger is *"Before **Final Research Gate**"*. Phase S was the research and is
**conditionally closed**; Phase SA's gate is an architecture gate.

**Reading A's answer to this** is that §2.4 is precisely the clause that reaches a review which is not
itself a Module's research — so "Phase SA is not research" does not by itself exclude it. **That answer
is available and is not refuted.**

---

## 5. SMT first-line challenge — Governance / Architecture SMT

**Why this SMT.** `SC-03` dispositioned **8 of 8 decision families** and **did not disposition
`FG-F-06`** (`SC-08` §3, two shapes, both controls firing). The subject is the scope of a governance
instrument, so the challenge sits with Governance/Architecture rather than a domain SMT.

| # | Challenge put to SMEs Core | Outcome |
|---:|---|---|
| `SC-SMT-12` | *"`SC-F06-01` uses §5 to fix §2.4's referent. Does §5 actually define the same review, or is that an inference from similar wording?"* | **Sustained in part.** §2.4 *"State Integration Review"* and §5 *"State Integration Very Deep Review"* differ by two words. The finding is stated as **referent identification, not proof**, and the intent reading is preserved |
| `SC-SMT-13` | *"Does `SC-F06-03` overstate a word count into a legal conclusion?"* | **Sustained.** The finding was re-worded to *narrows*, not *decides*; the §11-as-summary counter is now stated in the finding itself |
| `SC-SMT-14` | *"All three findings narrow Reading A. Is that a bias artefact?"* | **Material.** See §6 — the direction is declared and the counter-test was run |
| `SC-SMT-15` | *"Is any of this new evidence requiring targeted Very Deep Research re-entry?"* | **No.** All three findings are re-readings of one already-held instrument. **No new evidence gap. No re-entry required** |
| `SC-SMT-16` | *"Does anything here let SMEs Core answer `FG-F-06`?"* | **No.** All three findings terminate in Boss intent — what §2.4 attaches to, what the label designated, what §4's scope is |

> ## SMT DISPOSITION — `FG-F-06`
> # `BOSS-ONLY SCOPE CLARIFICATION`

**Basis:** each surviving ground reduces to a question about what a Boss-approved instrument was intended
to cover. `CF-D-01` fixes the authority: *"only Boss may state what a Boss ruling covers."*

---

## 6. Neutrality control — prompt §4.4, tested rather than asserted

**Declared direction of this round's findings: all three narrow Reading A.** That is exactly the shape a
bias artefact would take, so it was tested rather than left to assurance.

**The counter-test — what would strengthen Reading A, searched for deliberately:**

| Test | Result |
|---|---|
| Does any clause name *phase* as a gated unit? | §4 L158 is the only use of the word, and it is the destination, not the subject — **searched, found, and recorded as Reading A's ground, not suppressed** |
| Does §2.4 describe what Phase SA did? | **Yes** — cross-module contracts, whole-system integration. **Recorded as Reading A's principal ground and left live on the intent reading** |
| Is there a Boss designation of Phase SA as Very Deep Research? | `SC-V-01`, **0 hits with a 19-hit positive control**. Reported as measured, and the label reading is preserved as Boss's to confirm |
| Does the header Scope reach it? | `ALL STATES` — and Phase SA's work feeds the `STATE03` exit. **Left open; not argued away** |

**And the decisive neutrality fact:** **not one of the three findings changes the disposition.** Reading A
narrowed from five clauses and a precedent, to three clauses and no precedent (`SC-04`), to **two contested
clauses on the text plus a live intent reading of §2.4** — and the disposition is
`BOSS-ONLY SCOPE CLARIFICATION` either way. **A finding set that cannot move the outcome it is accused of
favouring is not steering it.**

> **SMEs Core offers NO preference between Reading A and Reading B, and this file states the reason
> plainly: Reading B is the reading that opens this gate, and SMEs Core is the party that benefits from
> the gate opening. Prompt §4.4 forbids choosing it for that reason, and no other reason is available
> without Boss's intent.**

---

## 7. Checkpoint

> ## `CP-SA-SC-90 — CLOSED`
> **`FG-F-06` re-checked clause by clause at primary text · §2.4 / §4 / §2.5 remain the contested grounds ·
> §9 stays withdrawn (`AR-F-02`) · §2.3 and §5 remain not engaged · three new findings `SC-F06-01`…`-03`,
> each narrowing Reading A and each terminating in Boss intent · SMT disposition
> `BOSS-ONLY SCOPE CLARIFICATION` · no targeted Very Deep Research re-entry required · no preference
> offered, and the reason for offering none is published.**
