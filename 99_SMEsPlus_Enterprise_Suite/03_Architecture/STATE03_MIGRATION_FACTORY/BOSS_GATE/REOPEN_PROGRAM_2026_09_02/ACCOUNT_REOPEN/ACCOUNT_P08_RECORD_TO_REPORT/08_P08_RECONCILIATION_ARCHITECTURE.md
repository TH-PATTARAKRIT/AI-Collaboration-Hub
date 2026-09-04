# P08_RECONCILIATION_ARCHITECTURE

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001` · Layer 1

## 1. The model

| ID | Statement | Class |
|---|---|---|
| `REC-01` | A **match** is a stored, amount-bearing link between exactly one debit item and one credit item, carrying the matched amount in three currency frames simultaneously; the two transaction-currency amounts need not agree with each other. | FACT VERIFIED |
| `REC-02` | A **full settlement** is a derived label over a connected component of matches. It holds no amount, no date and no party. | FACT VERIFIED |
| `REC-03` | The open-item balance is **recomputed from an aggregate over matches**, and is stored. Storage plus recomputation is what makes drift possible. | FACT VERIFIED |
| `REC-04` | The **subledger is a projection** of journal items net of matches — and, in the party dimension, partly a projection **of the matches themselves**: an item posted without a counterparty is attributed to the counterparty of whatever it was matched against. Un-matching removes it from that party's statement. | FACT VERIFIED |
| `REC-05` | **A match carries no event date.** Its as-of date is the later of the two matched documents' dates. Matching two prior-period items today retroactively closes them in a re-run of that prior period's ageing, with nothing in the data to explain the difference. | FACT VERIFIED |

`REC-04` is the answer to the directive's subledger question, and `REC-05` is the finding that matters most for restatement.

## 2. The guards, and the one that is wrong

Five guards exist and they are all in one routine: no item already settled · every item posted · all items on one account · **the companies must share a root** · the account must permit matching, or be of a liquidity type.

`REC-06` — **The company guard compares the root of the company tree, not the company.** Two different legal entities in one tree may be matched against each other, and the error message asserts a same-company condition the code does not check. `FACT VERIFIED`, reported independently by two agents of this session and verified against the source.

`REC-07` — **The difference entry arising from such a match is posted into one company chosen by recordset position.** The whole gain or loss lands in one entity's books with no compensating entry in the other, no error and no warning. `FACT VERIFIED` for both code facts; `SUPPORTED INTERPRETATION` for end-to-end reachability.

`REC-06` plus `REC-07` is a tolerance-zero item: `P08-T0-04`.

## 3. What settlement emits

Three system paths and one operator-driven path emit accounting facts on matching. Journal and accounts are single company-level configuration values; absent configuration halts the settlement rather than defaulting.

`REC-08` — **Two entries born of one matching event are dated by two different rules.** The difference entry takes the later of the matched dates, moved forward if that falls in a closed period. The cash-basis tax entry takes **the system clock's current date** whenever the matched documents predate the lock. `FACT VERIFIED`.

`REC-09` — Difference generation can be **switched off system-wide** by a configuration value that has no company or tenant dimension. `FACT VERIFIED`.

## 4. Un-matching

`REC-10` — Un-matching **compensates, it does not restore**. The entries the match created are reversed, not removed; a match-then-unmatch cycle permanently adds two entries per difference entry. `FACT VERIFIED`.
`REC-11` — Un-matching is **not blocked in a closed period**. `A VERIFIED ABSENCE`, scope = the two settlement models in full and the entire reconciliation-plan region of the item model; the pattern set covered every lock-check symbol. Only the compensating reversal is date-shifted.
`REC-12` — Un-matching is a **silent side effect** of two operations whose stated purpose is something else: returning an entry to unposted, and reversing an entry.
`REC-13` — **Removing a match removes its own audit trail.** Neither settlement model carries a change log or field tracking (`A VERIFIED ABSENCE`, scope = both model files in full). The only durable evidence a match existed is the reversal entry it leaves behind, and only when it generated one.

## 5. Divergences that produce a wrong answer while every equation holds

`REC-14` — **Line-level and document-level settlement use different tests.** An item counts as settled only when settled in both currency frames; a document counts as settled when settled in its transaction currency alone. A document can therefore report as paid while its item still carries a reporting-currency balance that the ageing report continues to show. `SUPPORTED INTERPRETATION`, mechanism traced end to end.
`REC-15` — **Stored open amounts can be overwritten out of step with the matches.** Enabling matching on an account that already carried matches under a type-based exemption rewrites every partially matched item's stored open amount back to its gross value by direct database statement, leaving the matches intact and triggering no recomputation. Open items are overstated. The mirror-image operation is guarded; this one is not. `SUPPORTED INTERPRETATION`, code-traced.
`REC-16` — An account's matching flag governs the **reported** open amount independently of the matching data: items on an account with matching switched off report zero open amount whatever matches exist. `FACT VERIFIED`.

## 6. Automation

`REC-17` — Matching rules may post to **any account** the configurator names — the restriction is a screen-level field domain, not a server-side constraint — and may derive the amount from free text on the bank line by a user-written pattern, where a failed extraction yields zero rather than an error. A rule may also raise a new customer or supplier document. `FACT VERIFIED`.
`REC-18` — **Automatic matching runs unattended and rewrites posted entries**: a scheduled process deletes and recreates the line detail of posted bank entries under the two suppression parameters, then matches the result. The only human control is the switch that enables the rule; the only notification is a note written after the fact. `FACT VERIFIED`.
`REC-19` — The "needs review" marker on a rule **blocks nothing**. `FACT VERIFIED`.
`REC-20` — The bulk matching tool **silently ignores a counterparty filter** unless an account filter is also supplied, then matches across every account and counterparty in the window, pairing solely on equal absolute amounts with no reference to the underlying documents. `FACT VERIFIED`.

## 7. Bank versus accounting reconciliation

`REC-21` — They are different mechanisms sharing a word. Bank status is a **structural test on the shape of the bank entry** — whether a clearing leg remains — and reports "reconciled" whenever none does, without consulting the matches at all. An entry recoded directly to a final account shows as reconciled with no match behind it. `FACT VERIFIED`.
`REC-22` — Undoing a bank reconciliation **destroys rather than reverses**, and deletes the associated settlement records. `FACT VERIFIED`.
`REC-23` — The statement completeness check **compares the system's own figure to itself by default**, because the externally supplied closing balance defaults to the computed one. `FACT VERIFIED`.

## 8. Authorisation

`REC-24` — Both settlement models grant create, write and delete to the **billing** tier — and, in a second grant the draft missed, to the **warehouse-manager** role, which holds full create, write and delete on the partial-settlement record. **No isolation rule of any kind exists on either model** (`A VERIFIED ABSENCE`, scope = every configuration file of the target root referencing those two models). The five eligibility guards live in the calling routine, not in the models, so a direct write reaches none of them; the only self-check is that both currency fields are populated. `FACT VERIFIED`; reachability by a given user is `C NOT YET SEARCHED`.

## 8A. The one database-level protection in the settlement graph

`REC-25` — **Corrected after independent review.** The package had characterised the settlement graph as having no persistence-layer protection. It has exactly one, and it is the only such object in the accounting layer: the settlement record's two item references are **required with no explicit delete behaviour**, which resolves to **restrict**. An item participating in a settlement therefore cannot be deleted at the database layer, whatever the application does. `FACT VERIFIED`.

This does not soften `REC-24`: the record can still be created and deleted freely by two ordinary roles with no isolation rule. What it changes is the claim that nothing below application code protects an accounting relationship — one thing does, and it is worth carrying into the design as the pattern to generalise.

## 9. Requirements

| ID | Candidate requirement |
|---|---|
| `P08-RQ-REC-01` | A settlement is a first-class accounting fact with its **own event date**, its own actor, and its own immutability. It is never destroyed; it is superseded. |
| `P08-RQ-REC-02` | A settlement is bounded by the residual it discharges. Over-settlement is structurally impossible, not merely unlikely. |
| `P08-RQ-REC-03` | A settlement has exactly **one owning company**. Cross-company settlement is refused unless an explicit intercompany construct owns it, and that construct posts symmetrically in both sets of books. |
| `P08-RQ-REC-04` | Settlement state is derived and never authoritative, and the derivation is reconstructible from the immutable facts alone. |
| `P08-RQ-REC-05` | Line-level and document-level settlement use one test in one currency model. |
| `P08-RQ-REC-06` | Un-settling in a closed period is refused, like any other change to a closed period. |
| `P08-RQ-REC-07` | No settlement mechanism may be switched off by a configuration value with no owning scope. |
