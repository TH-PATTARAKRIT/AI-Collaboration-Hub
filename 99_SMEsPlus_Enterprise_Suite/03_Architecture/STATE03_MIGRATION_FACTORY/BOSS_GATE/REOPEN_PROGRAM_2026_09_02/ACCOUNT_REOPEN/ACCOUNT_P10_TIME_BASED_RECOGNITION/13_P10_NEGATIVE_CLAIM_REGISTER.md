# P10 — NEGATIVE CLAIM REGISTER

Session: `SMEPLUS-26-09-04-ACC-P10-TBR-REV2-001` · Layer 1
Issued under `SMEPLUS_DEEP_RESEARCH_NEGATIVE_CLAIM_STANDARD` and `EC-06`.

`NO EVIDENCE FOUND != FUNCTION DOES NOT EXIST.`
Classes: **A** verified absence *within a stated scope* · **B** not found in searched scope · **C** not yet searched · **D** unknown · **E** contradicted.
**No `B`/`C`/`D` in this register has been upgraded to `A`** — by restatement, by citation, or by summary.

This register was produced as a **separately-tasked step**, not as an expectation on the document authors, per `DR-NC-05`.

---

| # | Negative claim as it would be tempting to write | Permitted form | Class | Scope that actually supports it |
|---|--------------------------------------------------|----------------|-------|----------------------------------|
| `NC-01` | "There are five time-based recognition mechanisms." | "At least eight exist; no exact total is supportable." | **D** | Two enumerations with different patterns returned five and seven; the second disproved its own completeness in the same report. A total requires a pattern that captures every route to a persisted entry, which neither had. |
| `NC-02` | "Deferral entries cannot carry a foreign currency." | "Neither deferral generator propagates the source line's foreign currency or its foreign amount; the spread is performed on the company-currency balance." | **A** in the narrow form, scope = the two generator methods and the report's column list. **B** in the broad form. | The generated lines still acquire a currency field from the ledger's own defaults; the *dimension* is dropped, not the field. The broad form was corrected before publication. |
| `NC-03` | "Nothing prevents duplicate deferral generation." | "The grouped path carries three duplicate controls; two were defeated under challenge. The validation path relies on source-document state." | **E — CONTRADICTED** | A domain filter, an equivalent condition in the query, and a conflict-tolerant relation write all exist. The claim as written must not appear anywhere in this package. |
| `NC-04` | "There is no catch-up mechanism for deferrals." | "No catch-up on the validation path; a structural cumulative catch-up on the grouped path." | **A** for the validation path, scope = the two deferral source files. **E** for the mechanism as a whole. | See `P10-C-01`. |
| `NC-05` | "Reopening a period re-derives nothing." | As written, bounded. | **A**, scope = the company model's write path and the model files of the five accounting modules searched | Nothing revisits entries that were re-dated or suppressed while a period was closed. |
| `NC-06` | "A credit note does not propagate to the deferral schedule." | As written, bounded. | **B** | No propagation path found in the searched scope. Not searched: localisation overlays, subscription-side handling. |
| `NC-07` | "The reference product has no prepayment concept distinct from deferral." | As written, bounded. | **A**, scope = the mechanism enumeration over reference root `RR-1` | Says nothing about other systems or about what SMEsPlus must do. |
| `NC-08` | "No two mechanisms share scheduling, day-count or rounding code." | As written, bounded to the four named helper functions. | **A** for those four; **B** for arbitrary shared utilities | The challenge that produced it declared this boundary itself. |
| `NC-09` | "No caller wraps deferral generation in the document's company context." | As written, bounded. | **A**, scope = the two files named, pattern declared, every hit inspected | Author re-verified. |
| `NC-10` | "The grouped generation handler has no single-company guard." | As written, bounded. | **A**, scope = that handler file | Author re-verified by reading the generation methods. |
| `NC-11` | "The accrual mechanism logs nothing on its source order." | As written, bounded to the wizard file. | **A**, scope = that file, all four occurrences of the identifier inspected | A subclass elsewhere could append; not searched. |
| `NC-12` | "No field anywhere links an accounting entry to the order that an accrual estimated." | As written, bounded to the declared field-name pattern. | **A** for the pattern `accru* = fields.` over all modules of `RR-1`; **B** for a link field named without that stem | The boundary is the pattern, not the path — declared explicitly. |
| `NC-13` | "Assets and loans cannot be denominated in a foreign currency." | As written, bounded. | **B** | The model definitions tie the currency to the company's, but localisation overrides were not searched. |
| `NC-14` | "There is no Python-level guard on changing a deferral window after entries exist." | As written, bounded. | **A** for the deferral source file; **B** for tenant overlay layers | The protection that does exist is view-level and present on one of the two views. |
| `NC-15` | "No multi-company or foreign-currency deferral test exists upstream." | As written, bounded to the two named test files and the declared pattern. | **A** within that scope | Reviewer-supplied; author has not re-run the pattern. Carried as class `A` **within the reviewer's declared scope**, not as a system-wide claim. |
| `NC-16` | "Asset pause, resume, revaluation and disposal produce no duplicate recognition." | **Must not be written.** | **C — NOT SEARCHED** | Five named methods were listed and not read. An empty taxonomy cell means UNSEARCHED, never ABSENT. |
| `NC-17` | "Localisation modules do not alter time-based recognition." | **Must not be written.** | **C — NOT SEARCHED** | No localisation module was examined for recognition overrides. |
| `NC-18` | "The client-side layer adds no recognition behaviour." | **Must not be written.** | **C — NOT SEARCHED** | No client-side code was examined by any of the four challenges or by the primary author. |
| `NC-19` | "A recurring entry never carries a recognition window forward." | As written, bounded. | **A**, scope = the copy helper and every module override of it across `RR-1` | Author-verified pattern; the helper has no override anywhere in the root. |
| `NC-20` | "The deferral date fields are editable on a posted document." | **Must not be written as fact.** | **D — UNKNOWN** | The view carries no read-only attribute, but posted-state protection resolves at runtime. Needs reproduction. |
| `NC-21` | "The foreign-currency amount is never balance-checked." | As written, bounded to the named validation method. | **B** | Reviewer-supplied; not independently re-read by the author. |
| `NC-22` | "The deferral mechanism has no schedule object." | As written, bounded. | **B** | Verified for the two deferral modules; a model declaration scan across all modules of `RR-1` was **not** performed. This is the single negative most likely to be quoted downstream, and it is **not class `A`**. |

---

## Mechanical Scan Result

A scan for `does not exist`, `there is no`, `never`, `always`, `only`, `nothing`, `anywhere`, `cannot`, `no ` was run over every Layer 1 document in this package. Every surviving occurrence either:
- carries a declared boundary and a class letter, or
- is a statement about a *specific cited code path* rather than about the system, or
- was rewritten before publication.

Three claims were rewritten as a result of this scan: `NC-02` (broad → narrow), `NC-03` (deleted as contradicted), `NC-04` (re-scoped by path). Two were downgraded from the author's drafts: `NC-01` (`A` → `D`) and `NC-22` (`A` → `B`).

**All five corrections originated in independent review. None originated with the author.** That ratio is now consistent across six consecutive rounds of this programme and should be treated as a structural property of the method, not as a comment on any individual round.


## Negatives Added by the Deployed-Evidence Correlation (`22`)

| # | Negative claim | Permitted form | Class | Scope that supports it |
|---|----------------|----------------|-------|------------------------|
| `NC-23` | "This session had no database access." | **Withdrawn — the claim was false.** | **E — CONTRADICTED** | Four archives were on the host; three were read. See `P10-C-10` and `14` `P10-R-08`. This was a negative asserted without a search, in the package that enforces the rule against exactly that. |
| `NC-24` | "The deferral function does not exist in database C." | As written, bounded to that database. | **A**, scope = that deployed database, by schema probe with the artefact byte size printed beside each zero | Says nothing about the other deployments or about the product. |
| `NC-25` | "No deferral entry has ever been generated in databases A and B." | As written, bounded. | **A**, scope = the deferral relation table of those two databases; the extraction artefact was 886 bytes, i.e. header only, proving an empty table rather than a failed extraction | The byte-size control is what makes this class `A` rather than class `D`. |
| `NC-26` | "No company in the estate uses the grouped generation path." | As written, bounded to the 44 companies of each of the two databases. | **A** within that scope | Two databases of an estate whose full size is unknown. |
| `NC-27` | "The fourth deployed archive contains no P10 structures." | **Must not be written.** | **C — NOT SEARCHED** | The host's tooling cannot open its archive format. |
| `NC-28` | "The chart of accounts is not shared in the deployed databases." | "1 account of 544 in one database and 0 of 544 in the other belong to more than one company; the schema permits sharing and carries no scalar company column." | **A** in that quantified form | The unquantified form would be false — one shared account exists. |
