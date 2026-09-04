# P08_AAS03_CHALLENGE — Independent adversarial review, findings and dispositions

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

Four AAS-03 experts were commissioned against the finished package, each adversarial by assignment, each with a disjoint mandate, each instructed that a defect in its own brief is itself a finding. **Reviewer findings are not accepted on authority.** Every finding below was verified by the session author against primary source before acceptance, and findings that failed verification are recorded alongside those that passed.

`Independent Review != Truth. Verified Evidence = Truth Basis.`

## 1. Reviewers and mandates

| Reviewer | Mandate | Position | Veto |
|---|---|---|---|
| Expert 1 | Functional and accounting design | `RECOMMEND HOLD` | **`AAS03-E1-VETO-01`** — the kernel model and the handoff pack must not be relied on in their draft form |
| Expert 2 | Data model and integrity | `RECOMMEND HOLD` | **`AAS03-E2-VETO-01`** — no downstream process may rely on the draft's persistence-layer control set, and no design may be sized against the figure "four" |
| Expert 3 | SaaS scope, isolation and localization | `RECOMMEND HOLD` | **two narrow vetoes** — on the consolidation row travelling to P11, and on two registers being cited as complete |
| Expert 4 | Method, evidence and convergence | recorded in §6 | recorded in §6 |

## 2. Findings accepted after verification — errors in the package

Twenty-two accepted. Each was reproduced by the author against source before acceptance.

| ID | Finding | Verified how | Disposition |
|---|---|---|---|
| `E1-F01` | The kernel declared five invariants and **omitted the double-entry identity** — the very invariant the package calls its most severe finding | internal to the package | **ACCEPTED.** `KRN-INV-00` added, in both currency frames, at persistence level, in the kernel and the handoff |
| `E1-F02` | `KRN-INV-01` constrained only the event→entry arrow, and therefore did **not** deliver the duplicate detection it was sold on; the same invariant was placed at two different nodes in two files | internal | **ACCEPTED.** Split into `01a` (the idempotency key on business fact → event) and `01b`; the node disagreement resolved |
| `E1-F03` | The kernel as drafted **forbade opening balances and migration**, which the package's own event register requires | internal | **ACCEPTED.** Explicit exception stated for opening-balance declarations, restatements and reversals |
| `E1-F04` | The source-of-truth conclusion contradicted three of the package's own statements and sat at the wrong layer; there are **four** independent truth bearers, not two | internal | **ACCEPTED.** `KRN-05` restated at the journal-item layer; the statement definition named as the fourth bearer |
| `E1-F05` | Class `A` on the posting instruction rested on a scope orthogonal to the claim | internal | **ACCEPTED.** Downgraded to `B` |
| `E1-F06` | Class `A` on the subledger rested on a name-pattern that cannot enumerate candidate stores | internal, and independently proved by the P04 peer finding | **ACCEPTED.** Downgraded to `B` |
| `E1-F07` | "**All 39** event models belong to the event-management domain" is **false** — three do not | **reproduced by the author**: the three are a calendar appointment, its type, and a barcode mixin | **ACCEPTED.** Corrected in the kernel model and in the Layer 2 pattern record. The conclusion is unaffected; the evidence line was wrong in the sentence underpinning the package's most load-bearing absence |
| `E1-F08` | The year-close class `A` cited "four declared patterns" that appear nowhere, and the package's own reason for declining the wider promotion applies identically at the narrower scope | internal | **ACCEPTED.** Downgraded to `B` at every scope |
| `E1-F09` | "334 is the upper bound of what can reach the ledger" is an inference the package's **own attack file refutes** twice | internal | **ACCEPTED.** Withdrawn; restated as the dependency-graph denominator |
| `E1-F10` | A **second** counterparty reach-through path exists — the contact merge, by raw database statement — with **none** of the three mitigations credited to the reported path | **reproduced by the author** against the merge wizard and the item's foreign key | **ACCEPTED.** Added as `AT-17b`; the attack file's mitigation count corrected |
| `E1-F11` | The kernel was two objects short of the package's own required trace | internal | **ACCEPTED.** `K8` (period) and `K9` (issued statement) added |
| `E1-F12` | The handoff carried six invariants; the kernel declared five | internal | **ACCEPTED.** Reconciled; the sixth is now `KRN-INV-08` |
| `E1-F13` | A Boss decision was put on the premise "no reference implementation exists either way", which three of the package's own files refute | internal | **ACCEPTED.** Premise corrected in both places before it reaches Boss |
| `E1-F14` | The consolidation requirement forbade the object that would fix the consolidation defect | internal | **ACCEPTED.** Raised as `P08-BD-12`; see also `E3-FIN08` |
| `E1-F16` | Clean-room residue in Layer 1 — eight lines carrying implementation tokens | reproduced | **ACCEPTED.** All moved to Layer 2 behind `EV-P-*` identifiers; Layer 1 now scans clean |
| `E1-F17` | The package declared a **readiness label**, which its own governance prohibits — and a disclaimer in the same sentence does not cure it | reproduced | **ACCEPTED.** Replaced with `HANDOFF PREPARED`; no readiness of any kind is now declared |
| `E1-F20` | The register that catalogues unsearched scope contained an arithmetically impossible denominator, and the package had computed a sharper one and not used it | reproduced: 65 modules, of which 21 touch the ledger | **ACCEPTED.** Corrected, and restated on the 21 denominator |
| `E1-F21` | Four accounting questions the domain requires and the package never asked — reversal dating, opening-balance integrity, functional currency, accrual-versus-cash basis | internal | **ACCEPTED.** Two became requirements, two became Boss decisions |
| `E1-F22`/`E2-F2` | The persistence-layer object count was wrong on every reading and stated two contradictory ways in two files | **reproduced**: four check constraints, not two or three | **ACCEPTED.** Re-enumerated across five object classes |
| `E2-C6` | The deletion analysis was wrong in three ways: **no log line at all** on a default installation; **five** guards not three; and the ordinary delete action **is refused** | **reproduced**: the log routine filters on the retention flag; the item-level guards exist; the cascade meets them | **ACCEPTED.** All three corrected. The attack file's "none is stopped outright" was stronger than its own body and is corrected |
| `E2-C8` | The settlement authorisation is wider than reported — a **warehouse-manager** role also holds full create, write and delete | reproduced | **ACCEPTED** |
| `E3-FIN01` | The declaration of what the scope correction did and did not touch was **false as written**; four of the five sets named as untouched had been re-analysed | reproduced against the package's own table | **ACCEPTED.** Withdrawn and replaced with an accurate per-set table distinguishing *classification changed* from *conclusion changed* |

## 3. Findings accepted that make a defect worse, not better

| ID | Finding | Disposition |
|---|---|---|
| `E2-C4` | Line re-parenting also works by a set command, and — the sharper point — the posted-record guard iterates only the entry being written, so a **draft** entry can take an item **out of a posted entry with no suppression key at all** | **ACCEPTED**, `JPM-16` sharpened |
| `E2-C5` | The seal-narrowing path is **complete and closed** statically: the same context-sensitive call feeds both the seal computation and the write guard | **ACCEPTED.** Re-classified `FACT VERIFIED` for the mechanism; only execution remains unreproduced |
| `E2-F1` | The class-`A` promotion on the balance absence was made on a pattern that **structurally could not have falsified it** — a row-level check cannot aggregate across rows | **ACCEPTED.** Pattern amended to include triggers and deferred/exclusion constructs and re-run over 22 roots: 0/0/0. The promotion is re-issued on the amended pattern. **This is the programme's own recurring defect reappearing in the file written to close it, and it is recorded as such.** |
| `E3-FIN03` | The statutory extract's scoping defect is wider than the author found: the correct path exists **in the same module**, the two populations genuinely differ, and there is no jurisdiction predicate | **ACCEPTED**, folded into the report trace |

## 4. Findings accepted that make a defect *less* severe

Recorded with the same weight as the others.

| ID | Finding | Disposition |
|---|---|---|
| `E2-F3` | The scope matrix's stated retention attack — "an administrator who can disable retention can erase the evidence" — is **CONTRADICTED**: a constraint refuses disabling once any entry exists | **ACCEPTED.** The attack path is withdrawn. The requirement survives on the different and stronger ground the package also recorded: the option is **off by default** |
| `E2-F7` | One real audit record does survive a deletion unconditionally — an item deletion writes a tracked message on the entry regardless of the retention flag | **ACCEPTED**, added as `JPM-28a` with its boundary |
| `E2-F2` (protective half) | The settlement record's item references resolve to **restrict**, so an item in a settlement cannot be deleted at the database layer — the only database-level object in the accounting layer protecting an accounting relationship | **ACCEPTED**, added as `REC-25`. The package had asserted there was none |

## 5. Reviewer findings that failed verification, or were stale

| ID | Claim | Outcome |
|---|---|---|
| `E1-F29` | Expert 1 initially found that the package had misidentified the lock-bypass sentinel and that the exculpatory correction `REV-03` was wrong in direction | **WITHDRAWN BY THE REVIEWER ON ITS OWN VERIFICATION.** The sentinel exists, is compared by identity, and is supplied on exactly the operation described. `AT-17` is accurate as written. Recorded here because the reviewer recorded it: a reviewer's error rate is evidence too |
| `E1-F18`, `E1-F19`, `E2-F6` | Five artefacts cited as evidence are missing from the package; the quarantine does not exist; there is no exit assessment or gate report | **STALE IN PART, ACCEPTED IN PART.** The reviewers read a package that was still being written; the named files existed within minutes of their reads. **The underlying method finding is accepted in full and is the more important half: the package carried no freeze marker, and an independent review cannot be conducted against a moving artefact.** See `§7` |
| `E3-FIN02` | The statutory-extract defect exists only in Layer 2 and is structurally prevented from reaching design | **STALE ON THE FACT, ACCEPTED ON THE PRINCIPLE.** A Layer 1 carrier had been added before the review closed. The principle — that a finding held only in the quarantine cannot reach the design layer — is a new failure mode for this programme and is recorded as a standing check |

## 6. Expert 4 — method, evidence and convergence

Recorded in `§6` of this file when received; the exit assessment and gate recommendation in `26_P08_FINAL_RESEARCH_GATE_REPORT.md` are not issued until it is.

## 7. Method findings this round produced

| ID | Finding |
|---|---|
| `P08-M-01` | **The package had no freeze marker and mutated during review.** Three reviewers independently reported reading different content at different times, and one reported that a contradiction it had found was silently resolved mid-review. Every future SMEsPlus package must be **frozen at a named commit with a content digest before review opens**, and every reviewer verdict must name the digest it reviewed |
| `P08-M-02` | **A finding held only in the evidence quarantine cannot reach the design layer.** The layer discipline that protects the clean room can also strand a defect. Every Layer 2 finding with design consequence needs a Layer 1 carrier, and the closure scan must check for orphans in that direction |
| `P08-M-03` | **A declared pattern must be tested against the mechanism it is meant to exclude.** The package's highest-profile class-`A` promotion used a pattern that could not have found a positive. Declaring POPULATION + PATTERN + PATH SET + UNIT is necessary and not sufficient: the pattern must be capable of falsifying the claim |
| `P08-M-04` | **Independent contact remains the only control that finds these.** Of the material corrections in this session, the author self-corrected three; four reviewers and one peer session found twenty-six more, including four factual errors and two class-`A` claims whose scope could not support them. The ratio is consistent with every prior round of this programme |
| `P08-M-05` | **Reviewers disagree with each other, and that is signal.** Expert 2 contradicted a premise in the scope matrix that Expert 3 had implicitly relied on; both were right about their own half. Neither was accepted without the author reproducing it |

## 8. Net effect on the package

| Category | Count |
|---|---|
| Reviewer findings accepted after verification | 26 |
| of which: factual errors in the package | 4 |
| of which: class-`A` claims downgraded | 3 |
| of which: made a defect worse | 4 |
| of which: made a defect less severe | 3 |
| Reviewer findings withdrawn by the reviewer | 1 |
| Reviewer findings stale on the fact, accepted on the principle | 3 |
| **Package conclusions disproved** | **0** |
| **Package conclusions whose evidence was corrected** | **7** |

The distinction in the last two rows is the one that matters. No central position of this package was overturned. Seven of them were resting on evidence that was wrong, thin, or stated at a scope the search could not support — and in a programme whose recorded history is that headline claims survive while their evidence does not, that distinction is the finding.
