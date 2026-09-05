# P08_TOLERANCE_ZERO_REGISTER

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

**These are proposals.** Under the programme's constitution only Boss may designate a tolerance-zero boundary. This session proposes; it designates nothing.

**Identifier note.** An independent reviewer found `T0-02` and `T0-03` referenced nowhere while `T0-01`, `T0-04`, `T0-05`, `T0-06` and `T0-07` were in use — an undeclared gap in a tolerance-zero sequence. The gap arose because the numbering was drafted against the prior programme's list and then diverged. The sequence is **re-issued complete below**; the two previously undefined identifiers are now defined, not retired.

| ID | Boundary | Basis in this package | State |
|---|---|---|---|
| `P08-T0-01` | **The entry-balance invariant must be enforced where a caller cannot reach it.** | `JPM-07`..`JPM-11`, `AT-10`, `AT-11`. The assertion is application-level, suppressible by a caller-supplied parameter, asserted in one currency frame only, and **no database-level object enforces it in 22 of 22 declared roots** on the amended pattern. | **OPEN.** The single most important requirement in the package. |
| `P08-T0-02` | **A posted financial fact must be immutable in every attribute, with no caller-supplied waiver.** | `JPM-12`..`JPM-16`, `AT-12`, `AT-13`, `AT-16`. Nine header attributes protected, waived by a context key; a posted item's account, counterparty, label, reference and cost allocation editable in place; a draft entry can take an item out of a posted entry with no key at all. | **OPEN.** *(Newly defined — the identifier was in use nowhere.)* |
| `P08-T0-03` | **A posted fact must never be deleted, and the deletion control must not be a company option.** | `JPM-26`..`JPM-29`, `AT-15`, `AT-21`. Five guards each with a defeat; retention off by default; **no evidence at all** of a forced deletion on a default installation; a custom module erases the ledger whole-table by direct statement. | **OPEN.** *(Newly defined.)* |
| `P08-T0-04` | **A settlement has exactly one owning company, and a difference entry never selects its owner by list order.** | `REC-06`, `REC-07`, `AT-18`. The guard compares the root of the company tree; the difference entry takes the first company by recordset position. | **OPEN.** |
| `P08-T0-05` | **Retention of posted facts is a platform floor a company may extend and never shorten.** | `SC-CL-05`, `JPM-28`. **The draft's stated attack path was contradicted** — the option cannot be disabled once entries exist. The boundary survives on the different ground that it is **off by default**. | **OPEN**, on corrected grounds. |
| `P08-T0-06` | **A statement value that is not derived from facts is a governed, auditable object — never an edit made on a cell.** | `FR-11`..`FR-13`, `SC-RP-04`. Three stored value classes reach no ledger control; one ordinary role holds full create/update/delete with no change history. | **OPEN.** |
| `P08-T0-07` | **A tenant-scope mutation may never rewrite a company-scope posted fact, and may never silently change a company-scope issued statement.** | `AT-17`, `AT-17b`, `REC-15`, `FR-23`, `KRN-INV-05`. Two independent reach-through paths, one of which bypasses the object layer entirely and therefore meets none of the mitigations credited to the other. | **OPEN.** |
| `P08-T0-08` | **No path may write to the ledger outside the object layer.** | `AT-20`, `AT-21`, `AT-22`, `REC-15`. A custom access-check override defeats permission and isolation for read, write and delete on known identifiers; a settings action erases ledger tables by direct statement, whole-table, every company. | **OPEN.** *(Newly raised by this session.)* |

**Closed: none. 8 raised, 0 closed.**

None of the eight is closable by further source reading alone. `P08-T0-01`, `-02`, `-03`, `-06` and `-07` are clean-room design decisions — the reference behaviour is to be rejected, not adapted. `P08-T0-04` and `-05` need a Boss scope decision. `P08-T0-08` needs a deployment fact: whether the custom modules concerned are installed.

**Standing rule inherited and honoured:** `CONDITIONAL PASS` is unavailable by rule while tolerance-zero boundaries stand unresolved. A conditional pass whose conditions are the tolerance-zero set is a pass with a different label.

---

# CLOSURE DELTA — boundary status after the targeted closure

**No boundary closed. Two moved in the wrong direction; one is newly evidenced as live.**

| Boundary | Movement |
|---|---|
| **Immutable posted facts** | **WORSENED.** The balance invariant has exactly one line of defence, at the object layer, disabled by a caller-supplied value (`43`). The posting state is outside the integrity seal — verified by the author and, independently, by a peer process from a different entry point. A raw-statement path flips posting state with no parameter at all |
| **Irrecoverable data loss** | **LIVE AND DEPLOYED.** The whole-table erase module with no company predicate is **installed in 3 of 3 databases** |
| **Unauthorised / duplicate posting** | **UNCHANGED as a boundary; the supporting measurement is CORRECTED.** Scoped to the population the detector covers, the figure is 677 of 36,961 with a largest group of 14 — not the swamping the package claimed (`P08-CONTRA-35`) |
| **Company isolation** | **WORSENED.** A statutory register query with no company predicate is installed on two 44-company databases (`P08-U-19`) |
| **Period integrity** | **WORSENED.** Relocation is not gated on a lock at all (`P08-CONTRA-31`); 0 of 89 companies configure any lock; the retention control is present in the 19.0 estate and unset on 88 of 88 |

`CONDITIONAL PASS` is unavailable for these by constitution. **Tolerance-zero closure: 0 closed.**
