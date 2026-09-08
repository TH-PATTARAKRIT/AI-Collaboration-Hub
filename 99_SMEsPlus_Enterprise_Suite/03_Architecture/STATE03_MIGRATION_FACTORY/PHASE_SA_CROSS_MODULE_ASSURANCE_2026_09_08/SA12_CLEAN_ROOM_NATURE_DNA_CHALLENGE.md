# SA12 — CLEAN-ROOM AND NATURE DNA CHALLENGE

Status: **HOLD** — clean-room integrity of this package is measured; three Nature DNA
obligations are unmet across the wider baseline.
Governing constitution: `02_SMEPLUS_CLEAN_ROOM_NATURE_DNA_CONSTITUTION.md` `c0880b10`;
master prompt §22.

---

## 1. The rule being applied

> SOURCE IS EVIDENCE, NOT DESIGN. LEARN BUSINESS MEANING, NOT VENDOR STRUCTURE.

Nothing is inherited by default: not schema, ORM, module structure, workflow, state model,
menu structure, UI or code architecture. Every SMEsPlus determination requires an independent
rationale. Common terminology may be reused where semantically correct — **similarity is
allowed, dependency is not.**

---

## 2. Clean-room integrity of this package — measured

A clean-room leak is caused by specificity pointed at the wrong surface. It is not visible to a
reader, because the leaked text is *correct*. It is found by a mechanical token count per file,
not by review.

**Sweep executed on every file in this package before each commit.**

| Sweep | Unit | Result |
|---|---|---|
| 1 — vendor/reference technical tokens | file | **0 occurrences across all package files** |
| 2 — prohibited verdict wording | line | 1 line, in the constitution section that *defines* the prohibition; reviewed and retained |
| 3 — identifier consistency | identifier | all cited identifiers defined within the package or in a cited external register |
| 4 — required-artifact presence | file | tracked against the master-prompt §20 list |

**Declared token set** (union of declared and derived, per the standing rule that a vendor name
has no shape and cannot be fully derived): reference model-namespace prefixes, bin-ledger and
replenishment object names, transfer-document object names, internal action prefixes,
privilege-escalation helper, implementation file extension, localization and custom module
prefixes, and the reference product name.

**One correction made during this session:** a warehouse operation term that is ordinary
English but is also a reference object name was removed from `SA00` §7 and replaced with a
neutral equivalent. Count moved 1 → 0. Recorded because a sweep that never finds anything is
usually a sweep that is not looking.

**One false positive in this session's own sweep, corrected:** the initial pattern matched the
SMEsPlus project name itself and the `smeplus_*` namespace the constitution *mandates*. The
sweep was made case-sensitive and both were excluded. A scrub instrument that flags the
project's own approved namespace will be switched off by its next user.

### 2.1 A limit of this sweep, stated

This sweep covers **this package's own files**. The evidence it cites lives on other branches,
some of it Layer 2 audit quarantine. Citing a Layer 2 file by path is permitted; transcribing
its technical content into this Layer 1 package is not, and the sweep is what enforces the
difference. Where an upstream extract carried reference identifiers, this package restated the
business meaning and did not transcribe them.

---

## 3. Nature DNA obligations — status across the baseline

Every material function must answer six questions. Measured against the twenty-two domains:

| Obligation | Status |
|---|---|
| 1. What did we learn? | **Met** for 16 of 22 domains; the six `THIN` domains cannot answer it |
| 2. What did we deliberately NOT inherit? | **Partially met.** `SA09-F-02` is the clearest instance: six unenforced invariants recorded as *facts about the reference estate*, then decided independently. Most other domains have not made this statement explicitly |
| 3. What alternatives were considered? | **Met** where this session made a determination (`SA05` §2.2, `SA06` §1, `SA08` §3). **Unmet** across the inherited Phase S baseline generally |
| 4. Why is the selected design SMEsPlus-specific? | **Partially met** |
| 5. What does SMEsPlus do better or differently? | **Met in four places**, see §4 |
| 6. Is further Very Deep Research required? | **Met** — six triggers raised in `SA16` |

### SA12-F-01 — obligation 2 is the one that fails silently

"What did we deliberately not inherit" is the only obligation that can be satisfied by writing
nothing at all — and then it looks satisfied. A design that silently keeps a reference
behaviour is indistinguishable, on the page, from a design that considered and chose it.

`SA09-F-02` is the model to generalise: list the reference behaviour, mark it as learning, then
state SMEsPlus's own position on each item. Six invariants, six explicit decisions. Carried to
`SA17` as a required element of every Functional Design record.

---

## 4. What SMEsPlus does better or differently — determinations made in this session

Four, each with independent rationale, none inherited:

| # | Determination | Why it is SMEsPlus's own |
|---|---|---|
| ND-01 | **Supply Nature is a resolved, immutable per-line fact, with its resolution inputs retained** (`SA05` §2) | Derived from the requirement that one customer order may mix stocked, manufactured and service lines. A later policy change cannot silently re-route work in flight, and an auditor can reconstruct why a line routed as it did |
| ND-02 | **A single physical-movement ledger, with six non-conflatable quantity concepts named separately** (`SA06` §1) | A second stock ledger creates a reconciliation obligation that can fail silently; under BD-ACC-01 a stock divergence becomes a ledger divergence |
| ND-03 | **An automatic cross-module document creation may not enter a module below that module's own control floor** (`SA03-F-02`) | The reference behaviour is the counter-example: a sale creates a purchase commitment with no demand step, bypassing the gate every human-raised purchase must pass. SMEsPlus inverts this |
| ND-04 | **Recording that an approval occurred is mandatory output, not optional** (`SA08` §3) | `XD-03`: in the reference estate the assignment half was near-universally populated and the occurrence half never was. An approval that leaves no evidence is not a control |

Each is a case of learning a behaviour and **declining** to inherit it.

---

## 5. Namespace constitution

All SMEsPlus-owned persistent business tables use `smeplus_*`. This package defines no physical
tables — physical schema is outside Phase SA authority — so the rule is carried forward as a
binding constraint on the Functional Design and Data Design gates, not applied here.

---

## 6. Source-copying challenge on this package's own determinations

| Determination | Copied from source? | Test applied |
|---|---|---|
| ND-01 Supply Nature per line | No | The reference estate routes by product configuration and document type; ND-01 rejects both (`SA05` §2.2) |
| ND-02 single movement ledger | **Similar to the reference shape** | Adopted on independent rationale, explicitly stated. Similarity is allowed; the rationale is not the reference's existence but the BD-ACC-01 dependency |
| ND-03 control floor | No — inverts the reference behaviour | — |
| ND-04 approval evidence | No — supplies what the reference estate never populated | — |
| Domain split SA-D00…SA-D21 | No | Derived from business natures and Boss boundary decisions, not from any module structure |

ND-02 is the one determination that resembles the reference. It is flagged here rather than
hidden, because a clean-room challenge that never finds a resemblance is not challenging.

---

`SA12 — HOLD`. This package's clean-room integrity is measured at zero vendor-token
occurrences. Nature DNA obligation 2 is unmet across the wider baseline and is carried to
`SA17` as a mandatory Functional Design element.

Boss remains the sole Final Approver.
