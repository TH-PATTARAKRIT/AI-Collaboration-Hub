# C01 — ACCOUNT_WAVE_A_CORR1_MASTER_RECONCILIATION

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001` · Parent `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`
Program `SMEPLUS-26-09-04-ACCOUNT-FULL-DEEP-001` · Wave A — Core Ledger & Closing

## 1. What this round did

| Step | Result |
|---|---|
| Reconciled 20 accepted corrections into the canonical artefacts | `C02` |
| Re-examined the 6 contradicted claims independently | `C03` — 3 `CORRECTED`, 3 `RESCOPED`, 0 retracted |
| Rescoped over-scoped negatives and issued a project-wide standard | `C04`, `SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD` |
| Reconciled the 5 severe findings independently | `C05` |
| FX missing-rate forensic | `C06` + addendum `A1` |
| Date semantic forensic, 7 concepts | `C07` + addendum `A2` |
| Closed `GAP-C04` from the dispatch layer | `C09` |
| Re-ran Level 11 with a balanced-but-wrong register | `C08` → final `C12` |
| Fresh independent L12 with two reviewers who had no prior involvement | `L12_FRESH_REVIEW/`, dispositioned in `C11`, summarised in `C13` |
| Final gate report | `C10` |

## 2. Lineage

```
SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001         branch research/account-wave-a-core-...-001
  ├─ E00 primary evidence base (EV-001..EV-023)
  ├─ files 01..26, four expert reviews, one challenge unit
  └─ E01 corrections COR-01..COR-20                              commit f8bc069
        │
        ▼  branched, never pushed back
SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORR1-001        branch research/account-wave-a-corr1-...-001
  ├─ CORR1/C01..C13
  ├─ CORR1/L12_FRESH_REVIEW/ (2 fresh reviewers)
  ├─ correction banners on 25 parent files — bodies unedited
  └─ 00_PROJECT_STANDARD/ negative-claim standard
```

**No file was deleted or silently overwritten.** Parent artefacts carry a correction banner naming
the corrections that land in them and the governing CORR1 text. Files 18 and 26 are marked
superseded and retained.

## 3. Claim accounting for the whole Wave

| Population | Count | Outcome |
|---|---|---|
| Primary evidence items (`EV-001`..`EV-023`) | 23 | 6 contradicted; 17 stood |
| Corrections accepted in the parent round (`COR-01`..`COR-20`) | 20 | all re-verified before acceptance |
| Fresh L12 reviewer claims (`C11`) | 27 | 13 `VERIFIED`, 9 `PARTIALLY VERIFIED`, 1 `CONTRADICTED`, 4 `NOT PROVEN` |
| Over-scoped negatives found across the programme | **9** | 6 in the parent, **3 authored by CORR1** |
| Vetoes | 2 | both resolved by correction; neither invalidates the model |

## 4. What survived, and what changed

### Survived unchanged
The semantic model of files `06`, `09`, `15`: seven facts, four of which must be immutable; the entry
as the representation *and* the only durable record of an accounting event; balance as the canonical
amount; reconciliation as record + derived state + emitted event; close as a date rather than an
object; and the recommendation to separate the **accounting event** from the **journal entry**.

**No adversarial round contradicted any of it.**

### Changed by correction
- The **fiscal year** exists as a mutable calendar override — which strengthens rather than weakens
  the close finding.
- **Rate types** are derived at query time — which converts a claimed gap into a design pattern worth
  adopting (`ST-05`).
- The **accounting date** finding is narrower in population and unchanged in consequence.
- **Duplicate control**, **provenance carriers**, **revaluation** and **recognition date** all exist
  in narrower or optional forms than "absent"; none exists as a general, mandatory carrier.

### Made worse by correction
- `SF-01` par FX — trigger widened, **detection removed** for invoices and bills.
- `SF-02` entry balance — now **externally reachable** (`C09`).
- `SF-03` accounting date — an additional path found, statutory chain confirmed as mechanics.
- `CONTRA-14` deletion evidence — the protection is a ratchet that by default locks **off**.

## 5. `GAP-C04` disposition and `SF-02` recalculation

**`GAP-C04` — substantially closed** (`C09`).

`VERIFIED FACT`: the framework's remote-call dispatch applies a **client-supplied context dictionary
to the ORM without filtering**, gated only by the called method not being private. `create`, `write`,
`unlink`, `action_post` and `button_draft` are all public.

`INFERENCE`: the six control-suppression flags — including `check_move_validity`, which disables the
debit = credit assertion — are therefore settable by any authenticated user with write access to the
record. An executed call was **not** performed; the chain was read end to end.

**`SF-02` severity recalculated:**

| | Before | After |
|---|---|---|
| Nature | an internal engineering convenience of unknown reach | **an externally addressable control bypass** |
| Actor | server-side code | **any authenticated user who may write an entry** |
| Rank in `C05` | 3rd | **2nd**, behind `SF-01` |
| `Tolerance = 0` proposal | `T0-01` proposed | `T0-01` **reinforced**, and the requirement extended: *an accounting invariant must not be expressible as a request parameter* |

The one qualification, recorded rather than buried: this is not privilege escalation. The user must
already be entitled to write the entry. The finding is that **the same call that legitimately writes
an entry can switch off the invariant that makes it an accounting entry.**

## 6. Compliance scans

| Scan | Result |
|---|---|
| Prohibited verdict vocabulary across the package | **clean** — the only occurrences are the quoted prohibited-form examples inside the standard and `C04` |
| Absolute negatives without a declared boundary, CORR1 files | 3 found and corrected (`NC-19`, `NC-20`, `NC-22`); addenda `A1`, `A2` issued |
| Unsupported "never" / "always" | 1 found (`C07` line 81), **withdrawn** in `A2-03` |
| Inference presented as verified fact | none found; `C09` explicitly marks its final step as `INFERENCE` |
| Negative class letters present and used | `A` 5 · `B` 8 · `C` 14 · `D` 2 · `E` 11 |
| B/C/D promoted to A anywhere | **none** |
| Parent branch modified | **no** — remote head unchanged at `f8bc069` |

## 7. What remains open

Four items are `PARTIALLY VERIFIED` or `NOT PROVEN` and two of them concern **cross-tenant
integrity**:

| # | Item | Why it matters |
|---|---|---|
| `FX-08` | Branch-level rates may be invisible to a root-scoped resolver | a tenant believing rates are loaded while conversion uses par |
| `SB-05` | A null-company rate may re-measure another tenant's postings | **cross-tenant data integrity** — candidate `Tolerance = 0` under constitution principle 13 |
| `FX-07` | The revaluation mechanism may inherit the par fallback | the compensating control would be contaminated |
| `B-05` | An approval engine may exist and be skipped under privilege elevation | would change the maker-checker finding |

All seven Thai statutory items remain `HOLD / EVIDENCE REQUIRED`, routed to `WAVE-D TAX`. Thai names
remain candidate / UNVALIDATED. **No statutory determination was made by this session.**

## 8. Position

The semantic model is intact and has now survived two independent adversarial rounds. The evidence
base is materially stronger than at the parent gate. **The round also demonstrated, on its own
output, that this programme's recurring defect is over-scoped negatives, and that only independent
review catches them.**

Gate recommendation is in `C10`. Boss is the sole Final Approver. Nothing here is approved, no gate
has moved, implementation remains unauthorised, and Wave B has not started.
