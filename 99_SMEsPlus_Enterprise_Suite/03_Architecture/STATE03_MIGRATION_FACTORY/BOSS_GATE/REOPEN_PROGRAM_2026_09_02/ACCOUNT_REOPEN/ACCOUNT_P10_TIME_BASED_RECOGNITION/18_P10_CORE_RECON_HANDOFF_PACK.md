# P10 — CORE ACCOUNTING RECONCILIATION HANDOFF PACK

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1
**Terminal state: `READY FOR CORE ACCOUNTING RECONCILIATION`**

This is the document the reconciliation reads first. **Read §4 before relying on anything in `01`–`09`.**

---

## 1. What P10 Hands Over

| # | Asset | Use in reconciliation |
|---|-------|-----------------------|
| `H-1` | The six-primitive recognition model (`01` §2) | The vocabulary every peer process must reconcile against |
| `H-2` | The scope ownership matrix (`10b`) | Feeds `P11`'s cross-process scope reconciliation directly |
| `H-3` | The event-to-ledger matrix (`09`) and its seven requirements `R-01`..`R-07` | The ledger contract P10 asks `P04` A2R to accept |
| `H-4` | Twelve peer dependencies (`19` §1) and six obligations P10 imposes (`19` §2) | The reconciliation agenda |
| `H-5` | Six Boss decisions (`16` §5) | The rulings that unblock design |
| `H-6` | Nine dispositioned contradictions, 22 controlled negatives, 15 dispositioned unknowns | What must not be re-derived, and what must not be asserted |
| `H-7` | The gate report (`20`) | The honest state of the evidence |

## 2. The Three Things Reconciliation Must Not Get Wrong

1. **A recognition event is not a journal entry.** Every defect in this package follows from treating them as one thing. If any peer process's design collapses them again, the collapse propagates.
2. **The allocation convention is a company binding value, resolved from the company that owns the financial effect.** Not from whoever is executing. Not from the tenant, except as a default.
3. **The service window is a tenant fact; the period grid is a company fact.** Forcing either to the other's scope breaks inter-company recharge in one direction and legal-entity autonomy in the other.

## 3. Direct Inputs to Each Peer

| Peer | Take this |
|------|-----------|
| `P01` P2P | `03` deferred expense trace; obligation `E-03` (record measurement rate and date with any window) |
| `P02` O2C | `02` deferred revenue trace; obligation `E-04` — **one field pair currently carries three different meanings and they must be separated** |
| `P04` A2R | `09` `R-01`..`R-07`; decisions `P10-D-02` and `P10-D-05`; the finding that a locked-period recognition entry is silently re-dated |
| `P05` E2P / `P06` B2R | Scope boundary questions `D-07`, `D-08` |
| `P07` Tax TH | `11` `P10-C-05` and `P10-C-06`, both `HOLD / EVIDENCE REQUIRED`. **P10 makes no statutory claim of any kind** |
| `P11` | `10b` in full, including the three PLATFORM assignments and the one TENANT assignment |
| Asset programme | `08` in full, especially §1's two refutations and §5's division of responsibilities |

## 4. Limitations — Read Before Relying

1. **Two evidence layers, not one and not four.** Source, plus deployed schema and stored data (`22`). No runtime, no UI, no migration evidence; one deployed archive unreadable by the host's tooling. The package originally claimed a single layer — see `14` `P10-R-08`.
1a. **The estate is not on one product line.** One deployed database has no deferral structure at all and carries a periodic-transfer mechanism the others lack. Any reconciliation assuming a uniform mechanism set across the estate is wrong.
1b. **The live configuration is the weakest path.** All 44 companies in the two databases that carry the function generate on source-document validation — the path with no lock-date check and no catch-up. Zero recognition entries have ever been generated.
2. **Two gating findings are unreproduced inferences.** The company-boundary defects are verified in code and not observed in behaviour.
3. **The mechanism population is a floor.** At least eight; no total is supportable. Any downstream text must say "at least".
4. **Nine challenge findings were admitted without author re-verification** and are marked class `B` in `15` §2. None is the sole support for a gate-changing conclusion.
5. **Three surfaces are declared unsearched**: asset lifecycle paths, localisation overlays, client-side behaviour. `NC-16`, `NC-17`, `NC-18`, all class `C`. **An unsearched surface is not an empty one.**
6. **The correction sections govern.** `14_P10_REVISION_LOG.md` corrects seven of the author's statements, including one that a summary reader would otherwise carry as fact — that no deferral catch-up exists. It holds for one path only. Cite `14` and `11`, not the headline tables.
7. **Research gate is `RECOMMEND HOLD`.** Three of eight criteria unsatisfied, one of them tolerance-zero. Reconciliation may proceed on the semantics; **no gate may be closed on this package.**

## 5. Standing Veto

`AASP-VETO-01` — no implementation of any P10 mechanism may start until `P10-D-02` (may a posting constraint alter a recognition period?) is ruled. Design work is not blocked. The veto is not lifted by this handoff.

## 6. Clean-Room Scan Result

A mechanical scan for vendor tokens was run over all Layer 1 documents in this package before commit. Layer 1 carries **no** vendor model names, file paths, method names, line numbers or source identifiers; every source reference is an `E-P10-nnn` identifier resolving into the Layer 2 quarantine. The scan command and its output are recorded in the evidence manifest.

Layer 2 material — the raw citation register, the enumeration outputs and scripts, and the four challenge records — is **Boss / PMO / AI-Audit only** and must not be transcribed into any reference package or Team B artefact.

## 7. Terminal Declaration

P10 has produced a bounded semantic model of time-based recognition, three traces, five matrices, a scope determination under the corrected constitution, nine dispositioned contradictions, a controlled negative-claim register, fifteen dispositioned unknowns, four independent adversarial challenges, and a six-item Boss decision package.

It has **not** closed its research gate, and it does not claim to.

> **`READY FOR CORE ACCOUNTING RECONCILIATION`**
