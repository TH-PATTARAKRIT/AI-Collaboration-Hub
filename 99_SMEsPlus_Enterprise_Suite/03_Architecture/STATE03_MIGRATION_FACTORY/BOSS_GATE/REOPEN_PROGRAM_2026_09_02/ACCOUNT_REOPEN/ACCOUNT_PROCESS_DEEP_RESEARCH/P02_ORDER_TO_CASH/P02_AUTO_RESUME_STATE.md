# P02 AUTO-RESUME STATE

Created **2026-09-05** under `[SMEPLUS-26-09-05-G02-P02-O2C-TARGETED-CLOSURE-002]`.
**No auto-resume file existed before this date.**

| Field | Value |
|---|---|
| Branch | `research/account-p02-order-to-cash-2026-09-04-001` |
| Baseline this round | `ff8be5128483c3ba49b3265f72f1851b6c6bcd64` |
| Session mode | **OLD SESSION CONTINUATION** — nothing reset, full lineage preserved |
| Resume mode | **AUTO** |
| Background tasks | **0** — verified by `pgrep` at entry and exit; all four expert agents completed and reported |
| Unfinished instrumentation | **1, declared:** the format-width sweep (`-Fp` / `-Ft` / gzip signatures) did not finish. **No zero is claimed from it.** |
| Last verified checkpoint | `CP-G02P02-14` |
| Current checkpoint | `CP-G02P02-FINAL` |
| Terminal state | `G02-P02 TARGETED CLOSURE — HOLD FOR SPECIFIC BOSS AUTHORISATION / EXTERNAL EVIDENCE` |

## Next Exact Actions, In Priority Order

0. **Re-run the artefact sweep with the pattern widened to `-Fp` / `-Ft` / gzip, and reconcile `28`
   against `22`** (`C-48`). The count is **≥40, not 39**; the missing artefact is
   `/Volumes/iMacSys/95_BHPRO_PROJECT/DOCUMENT/iEVING_2026-03-31_06-48-41/dump.sql`, which `22` had
   already added by correction. **Publish the processed-file count beside the result.**
0b. **Re-derive the database count without `database.uuid` as the sole key** (`C-44`, `C-49`). It
   over-counts (one `iEVING` lineage split in two by a rotation five minutes after a backup) and
   under-counts (seven live databases sharing one uuid). Use a composite: uuid + `ir_config_parameter`
   row `create_date` + installed-module fingerprint + `res_company` id-1 `create_date`. **`P02-F-28a` is
   withdrawn and must not be cited.**
1. **Re-scope every consumer of the headline to the corrected denominator** (`C-43`): 493,277
   marker-capable lines, 15 databases, generations 16/18/19. Files to edit: `18`, `19`, `22`, `26`, `27`,
   `37`. **The corrected figure is in `28`'s banner; the consumers still carry the old one.**
2. **Decide, in writing, whether containerised databases are in the P02 population** (`C-47`). Enumerate
   `docker volume ls` (83) and the 11 `postgres:16*` containers read-only. Either answer is defensible;
   silence is not.
3. **Re-derive the database count with a second discriminator** (`C-44`): installed-module fingerprint +
   row-count vector + `res_company` id 1 `create_date`. Report artefacts / uuids / instances as three
   numbers.
4. **Re-measure delivered-not-invoiced on the posted basis for the remaining 7 databases** (`C-34`).
   Only `iSMEs` is corrected; the other rows are floors.
5. **Segment both cut-off directions by the line's product `invoice_policy`** (`P02-F-34e`) before P10
   acts on the 792 and the 2,564.
6. **Finish the format-width sweep** with a coverage assertion and a published positive control.
7. **Disposition `product_brand_sale`** (Expert 4, M-2) — it fully replaces `_create_invoices` and is
   readable; and add the POS and payment-triggered invoice routes to the spine analysis.
8. **Add the selection-membership precondition to every enumerated-value predicate** in the package.
9. **Add an artefact column to `28` §4** and audit the six other multi-artefact uuids.
10. **Rebuild `31`'s standard union from the full v16 root** now located on this host.

## Blocked — Not Resumable Without An External Decision

| Item | Blocked on |
|---|---|
| `C-04` cost-of-sales idempotency | **Boss authorisation** — revised pack at `33` §5, target company `id=1`, `pg_dump` mandatory, v19 counterpart now available |
| Behaviour of 189 unreadable installed modules | External evidence — the deployed addon set |
| Revenue: billing vs performance | **Boss decision** (`BP-03`) |
| Thai VAT / WHT statutory treatment | P07 + statutory source |
| Three scope holds | P11 convergence |

## Standing Rules Adopted This Round

- **A figure names its artefact, not only its `database.uuid`** (`P02-F-30a`).
- **A predicate over an enumerated field carries a selection-membership precondition**, not only an
  injection control (`C-43`).
- **The runtime PATH SET is every running postgres container**, enumerated by command (`C-41`).
- **An unfinished sweep is reported as unfinished, never as a zero** (adopted from Expert 2).
- **Agreement between instruments that share a pattern is not corroboration** (`C-48`). Two instruments
  agreed on 39 and a third agreed later; all three were blind to plain-SQL dumps. **Vary the pattern,
  not just the traversal.**
- **A later round may not silently narrow an earlier round's recorded correction** (`C-48`). Before
  republishing a population, diff it against every prior recorded count and reconcile explicitly.
