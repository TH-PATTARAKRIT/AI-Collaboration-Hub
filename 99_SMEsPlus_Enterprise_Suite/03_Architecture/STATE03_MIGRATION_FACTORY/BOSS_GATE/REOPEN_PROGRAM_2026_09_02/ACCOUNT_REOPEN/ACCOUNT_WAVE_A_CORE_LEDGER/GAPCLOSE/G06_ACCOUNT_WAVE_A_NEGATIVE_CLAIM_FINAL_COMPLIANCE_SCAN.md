# G06 — NEGATIVE CLAIM FINAL COMPLIANCE SCAN

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GAPCLOSE-001`
Scanned against `DR-NC-01` … `DR-NC-06` of `SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD`

**No silent edits.** Every flagged claim is restated here at its supported scope. Bodies are retained
unedited; **this file governs where it conflicts with them.**

---

## 1. Method

Mechanical scan of **45 canonical Wave A files** (parent `01`–`26`, `CORR1/C01`–`C13`,
`GAPCLOSE/G02`–`G05`) for the prohibited forms and strength words in the standard §5, then manual
triage of every hit.

A line was treated as **already bounded** if it named a search scope, carried a class letter
(`A`–`E`), or was itself the standard's quoted prohibited example.

## 2. Raw results

| Category | Unbounded hits |
|---|---|
| `never` | 66 |
| `always` | 15 |
| `cannot` | 68 |
| absolute absence (`does not exist` / `there is no` / `no such` / `anywhere in the tree`) | 50 |
| system-wide absence phrasing | 1 |

## 3. Triage

| Class | Count | Treatment |
|---|---|---|
| **Prescriptive / normative** — "SMEsPlus must never…", "…should not…", `REJECT` / `EXTEND` requirements | **~120 of 149** | **Compliant.** These are requirements for the system being designed, not factual negatives about the reference system. `DR-NC` governs claims about what exists, not statements of what SMEsPlus shall do |
| **Quotation of a prior claim or of the rule itself** | 6 | Compliant — includes the standard's own prohibited-form examples and prior claims being corrected |
| **Bounded by an immediately preceding citation** — e.g. "there is no branch in `_get_rates`, `_get_conversion_rate` or `_convert` that can raise" | 8 | Compliant in substance; the boundary is the named methods. Retained |
| **Factual negatives at unstated or domain-wide scope** | **17** | **Non-compliant — rescoped in §4** |

## 4. Rescoped claims

Each restated at the scope the evidence supports. `DR-NC-06` lineage preserved: the original wording
stays in place, and this table governs.

| # | File:line | Claim as written | Class | Rescoped wording |
|---|---|---|---|---|
| `RS-01` | `21:87` `GAP-B02` | "No accounting-event identity and no provenance carrier exist **anywhere in the domain**" | **`E`** — contradicted in part | "No **general, mandatory** accounting-event identity or provenance carrier was found in `addons/account`. **Typed origin links exist** for specific generated entries (payment, recurring, cash-basis, statement line) and a free-text origin field exists. A genuine database uniqueness key exists for bank-statement imports in the optional module `account_bank_statement_import`." |
| `RS-02` | `14:37`, `04:117`, `07:67` | "No maker-checker / approval-before-posting step exists" / "no such step exists" | **`E`** — contradicted at domain scope | "No approval step distinct from the posting permission was found **in `addons/account`**. A generic, user-configurable approval engine exists in `addons/web_studio` which can gate the posting action; it cannot gate the underlying write, and it is skipped under elevated privilege. See `G05`." |
| `RS-03` | `12:31` | "Year-end closing entry **does not exist anywhere in the tree**" | **`B`** | "No year-end result-transfer entry was found within `addons/account` and `addons/account_reports`. The only closing entry found is a tax-return posting. Localization and third-party modules were not searched." |
| `RS-04` | `01:62`, `01:138`, `01:150`, `10:68`, `12:16`, `06:188` | "There is no period object" | **`A` within scope, after `COR-01`** | "No period object carrying state, a close action, a closer, a basis, or a link from any entry was found in `addons/account`, `addons/account_accountant` or `addons/account_reports`. A fiscal-year **calendar** record does exist (`COR-01`)." |
| `RS-05` | `06:43`, `06:50`, `06:177`, `09:48` | "There is no separate accounting-event object / no event object" | **`B`** | "No accounting-event object distinct from the journal entry was found in `addons/account`. See `RS-01` for the partial carriers that do exist." |
| `RS-06` | `09:49`, `26:153` | "Provenance / lineage — no owner, does not exist" | **`B`** | "No general provenance carrier was found in `addons/account`. Typed origin links and one optional-module import key exist — see `RS-01`." |
| `RS-07` | `15:27`, `15:97` | "**Four identities that a ledger needs do not exist**" | **`B`** | "Four identities — accounting event, source event, tenant, period — were not found in `addons/account`, `addons/account_accountant` or `addons/account_reports`. Partial carriers exist for the first two; see `RS-01`." |
| `RS-08` | `06:188`, `15:97` | "There is no temporal validity model **anywhere**" | **`A` within scope** | "No effective-dating or version fields were found on the account, journal, entry, item or company models in `addons/account`. Other modules were not searched for this purpose." |
| `RS-09` | `18:105` | "Item-level identity is positional; there is no stable business key" | **`B`** | "No stable business key for the journal item was found in `addons/account`." |
| `RS-10` | `04:218`, `04:248`, `04:254`, `07:63` | "There is no separate reopening authority / no close artefact / no closer, no close date" | **`A` within scope, qualified** | "No distinct reopening authority and no close artefact were found in `addons/account`. Lock-date changes **are** field-tracked and lock exceptions **are** first-class records (`B-09`), so a trace of the change exists — what is absent is an artefact attesting the close itself." |
| `RS-11` | `04:236` | "There is no second-person approval" on lock exceptions | **`A` within scope** | "No second-person approval was found on the lock-exception model in `addons/account`. The same role grants and revokes (`COR-04`)." |
| `RS-12` | `C07:25` | "**Posting timestamp** — no carrier" | **`B`** | "No accounting fact recording when a posting occurred was found on the entry model in `addons/account`. The framework's generic record-audit fields exist and were not assessed as a substitute." |
| `RS-13` | `C07:34` | "Because there is no tax point…" | **`E` in part** | Superseded by addendum `A2-02`: "No **stored** tax-point field was found on the entry or item in `addons/account`. A **derived** tax point exists for cash-basis taxes via the reconciliation date." |
| `RS-14` | `C06:147`, `C06:235` | "There is no forward control" / "no detection signal at all" | **`A` within scope** | Bounded by the detectability table above each; scope is the conversion path and the controls enumerated in `C06` §6. Retained with scope made explicit here. |
| `RS-15` | `C10:122` | "…tenant boundary **does not exist**" | **`A` within scope** | "No tenant entity is present in `addons/account`, `addons/account_accountant`, or the company model. Deployment- and hosting-layer tenancy was not searched." |
| `RS-16` | `03:105` | "**This is the entire fiscal-year model**" | **`E`** | Superseded by `COR-01`: two company integers **plus** an optional fiscal-year calendar record in `addons/account_accountant`. |
| `RS-17` | `26:149`–`26:153` | Gate-report answers restating the above as bare absences | **inherits** | Superseded by `C10`, itself superseded by `G10`. Each answer inherits its rescoped form above. |

## 5. Inference presented as verified fact

Scanned separately. **Zero instances found.** Every inference in the package carries an explicit
`INFERENCE` label, including:
- `C09`'s final step (context-key reachability) — explicitly `INFERENCE`, executed test recommended;
- `G02` §2.4 — SQL generation is `VERIFIED FACT`, resulting precedence is labelled `INFERENCE`;
- `G02` §2.6 — the PostgreSQL `NULLS DISTINCT` consequence is labelled `INFERENCE`, not tested here;
- `G03` §7 residuals — labelled `INFERENCE` from two verified code paths.

## 6. Rule-by-rule result

| Rule | Result |
|---|---|
| `DR-NC-01` absence within scope ≠ absence system-wide | **17 breaches found, all rescoped in §4** |
| `DR-NC-02` every material negative declares its boundary | breached by the same 17; **now compliant** |
| `DR-NC-03` "not found" distinguished from "verified absent" | compliant after §4 — 5 claims are `A` within a stated scope, 8 are `B`, 4 are `E` |
| `DR-NC-04` system-wide claims need system-wide evidence | **no remaining system-wide negative** in the package |
| `DR-NC-05` independent review challenges high-impact negatives | **satisfied** — 4 expert reviews, 1 challenge unit, 2 fresh CORR1 reviewers, 2 fresh gate reviewers |
| `DR-NC-06` contradicted negatives rescoped with lineage | **satisfied** — `E01`, `C04`, addenda `A1`/`A2`, and this file; nothing deleted or silently edited |

## 7. Programme total

**Over-scoped negatives found across Wave A: twenty-six.**
Six in the parent round · three authored by CORR1 · **seventeen found by this compliance scan**.

`INFERENCE:` the count rose because this is the first round to scan **mechanically** rather than rely
on reviewers encountering claims incidentally. That is itself the finding: `DR-NC-05` (independent
review) catches the *high-impact* negatives, but only a mechanical scan catches the *long tail*. Both
controls are needed, and the scan is cheap.

`RECOMMENDATION:` the mechanical scan in §1 should become a mandatory pre-gate step for every
SMEsPlus research package, and its script should be kept with the standard.

## 8. Effect on conclusions

**None of the seventeen rescopings changes a decision, a severity, or a gate blocker.** Every
`REJECT` and `EXTEND` in the transfer register rests on a **positive** finding of observed behaviour.
The rescopings narrow claims about what the reference system *lacks*; they do not alter what it was
observed to *do*.
