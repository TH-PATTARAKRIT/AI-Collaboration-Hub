# P06_BANK_INGESTION_IDENTITY_MATRIX.md

**Session:** P06 Bank-to-Reconcile — TARGETED CONTINUATION (CP-C06)
**Classification:** LAYER 2 — AUDIT QUARANTINE
**Status of the prior finding:** **RE-VERIFIED BY INDEPENDENT SEARCH — SURVIVES UNCHANGED.**

---

## 1. The re-search, and why it was run

`P06-B-40` required every Class-A negative to be re-tested with **independently-worded patterns**, because the programme's own history records that two of three origin failures were naming-variant misses.

Prior round PATTERN: `unique_import_id | online_transaction_identifier | transaction_identifier`.
**This round PATTERN (deliberately disjoint):** `external_id | external_ref | end_to_end | end2end | instruction_id | msg_id | uetr | checksum | fingerprint | dedup | idempot`, over the **whole `$V18E` tree**, `*.py`, case-insensitive.

Whole-tree counts: `external_id` 112 · `external_ref` 16 · `end_to_end` 13 · `end2end` **0** · `instruction_id` 6 · `msg_id` 124 · `uetr` 22 · `checksum` 197 · `fingerprint` 10 · `dedup` 57 · `idempot` 62.

**IIM-F-00 — The finding survives. 3 of 7 doors attach a machine-usable transaction identity; 4 of 7 attach none.**

---

## 2. The matrix

| # | Ingestion door | Identity attached | Scope of the identity | Enforcement | Evidence |
|---|---|---|---|---|---|
| 1 | **OFX import** | `unique_import_id` = `FITID` | value-namespaced (acct#+journal), DB-global constraint | DB UNIQUE + Python pre-search | `account_bank_statement_import_ofx/models/account_journal.py:118` |
| 2 | **CAMT import** | `unique_import_id` from `AcctSvcrRef`, **degrading to `name-date-sequence`** | as above | as above | `..._camt/models/account_journal.py:91`; fallback `lib/camt.py:760-771` |
| 3 | **Online sync** | `online_transaction_identifier` | per journal, Python only | **no DB constraint** | `account_online_synchronization/models/account_bank_statement.py:16` |
| 4 | **QIF import** | **none** | — | — | see §4 |
| 5 | **CSV import** | **none** (statement-level `reference = file_name` only) | — | — | see §4 |
| 6 | **OCR extract** | **none** | — | — | `account_bank_statement_extract/models/account_bank_statement.py:48-53` sets exactly `amount, date, journal_id, payment_ref` |
| 7 | **Manual UI / `create()`** | **none, and not settable** | — | — | `unique_import_id` is `readonly=True` |

**DENOMINATOR:** POPULATION: ingestion doors onto `account.bank.statement.line`. PATTERN: creation sites plus identity-field population. PATH SET: the six `account_bank_statement*` modules, `account_online_synchronization`, and core `account`. UNIT: door. **RESULT = 7**, of which 3 attach identity.
*(The base `account_bank_statement_import` module is a dispatcher, not a door, and is excluded from the count — this is the reconciliation of the "6 vs 7" denominator correction recorded as REV-E-01 in the prior round.)*

---

## 3. What the alternative vocabulary DID surface

**IIM-F-01 — One identity concept the prior round missed: `iso20022_uetr`. It does not close any open door.**
`$V18E/account_iso20022/models/account_payment.py:12-14`:
```
iso20022_uetr = fields.Char(
    string='UETR',
    compute='_compute_iso20022_uetr',
```
generated at `:60` as `uuid4()`, and required for SEPA pain.001.001.09 (`account_journal_sepa_ct.py:15` raises when missing).

**IIM-F-02 — And it sits on the wrong side of the process. This is the important part.**
`iso20022_uetr` lives on `account.payment` — the **outbound instruction**. **There is no counterpart field on `account.bank.statement.line`, and nothing matches an inbound statement line back to a UETR.**
So the reference **generates a globally-unique end-to-end tracker for money leaving, and then discards it when the bank reports back.** That is the single sharpest expression of the identity gap: the identity exists, it is well-formed, and the ingestion layer cannot use it.
**Classification: FACT VERIFIED.** Raised as **`P06-B-48`**.

**IIM-F-03 — CAMT parses the inbound end-to-end identifiers and demotes them to free text.**
`$V18E/account_bank_statement_import_camt/lib/camt.py:616-617` extracts `InstrId` and `EndToEndId`. They are then written into notes, not into an identity field — `.../camt/models/account_journal.py:127,130`:
```
notes.append(_('Instruction ID: %s', instruction_id))
notes.append(_('End to end ID: %s', end_to_end_id))
```
**The one inbound channel that carries the outbound identity throws it into a narrative field.** Combined with IIM-F-02, the round trip is broken at both ends.

**IIM-F-04 — The outbound EndToEndId fallback is truncated, so uniqueness is not guaranteed by construction.**
`$V18E/account_iso20022/models/account_journal.py:244-247` — `EndToEndId.text = (payment.get('end_to_end_id') or PmtInfId.text + str(payment['id']))[-30:].strip()`. The `[-30:]` keeps the **last** 30 characters of a concatenation.
This corroborates the custom-module finding from the prior round (`account_online_payment` builds a wall-clock `end_to_end_id` truncated the same way) — **truncated identifiers are a pattern here, not an isolated slip.**

**IIM-F-05 — `dedup` / `idempot` / `fingerprint` in accounting scope are outbound API request-safety, not transaction identity.**
`$V18E/payment/utils.py:217` — `def generate_idempotency_key(tx, scope=None)`, documented at `:220` as preventing *"API requests from going through twice in a short time"*, consumed by the Adyen, PayPal and Stripe providers.
**NOT FOUND** as a bank-statement-line identity in `$V18E/account*` + `$V18E/payment*`, `*.py`, non-test.
**The system has idempotency for its outbound API calls and none for its inbound bank events.**

---

## 4. QIF and CSV, re-confirmed under a different pattern

PATTERN this round: `unique|identifier|_id'|ref`.

**QIF sets:** `date` (from `D`), `amount` (`T`), `ref` = cheque number (`N`), `payment_ref` = payee+memo (`P`,`M`), `sequence` (positional), and a partner resolved by **name string match** — `models/account_journal.py:93-94`. The parser states the gap itself at `:89`: *"Since QIF doesn't provide account numbers…"*.
**CSV sets:** a statement-header `reference = file_name` (`wizard/account_bank_statement_import_csv.py:136-140`) and a positional index. Nothing per transaction.
`unique_import_id`: **NOT FOUND in either module, all files, PATTERN `unique|identifier`, 0 lines. Class A within that declared scope.**

**IIM-F-06 — And the field is not settable through import mapping either.** `unique_import_id` is `readonly=True` (`account_bank_statement_import/models/account_bank_statement.py:15`), so a CSV column cannot be mapped to it. **The CSV door cannot be fixed by configuration.**

---

## 5. Identity per required dimension

The prompt requires each dimension documented per door.

| Dimension | Status across the seven doors |
|---|---|
| **Source identity** (which file/feed) | CSV only, as a statement-level filename; **absent on the other six** |
| **External transaction identity** | 3 of 7 (OFX, CAMT-when-populated, online sync) |
| **File identity / import batch** | **NOT FOUND** as a first-class object — no import-batch record exists |
| **Bank account identity** | via the journal; QIF explicitly cannot supply it |
| **Company identity** | present on the line, but the dedup filter is a `sudo()` search with **no company domain** |
| **Duplicate-prevention identity** | 1 DB constraint covering 2 of 7 doors |
| **Correction identity** | **NOT FOUND** — no concept of "this line supersedes that one" |

**IIM-F-07 — There is no import-batch object.** A re-import cannot be identified, audited or rolled back as a unit, because the unit does not exist. Raised as **`P06-B-49`**.

---

## 6. Blocker impact

| ID | Status |
|---|---|
| `P06-B-10` identity per door | **remains open**, now **re-verified by independent search** — evidence class upgraded |
| `P06-B-40` Class-A negatives unverified | **PARTIALLY CLOSED** — this negative and the fee negative have now had a second, independently-worded pass |
| `P06-B-48` | **NEW** — a globally-unique outbound tracker with no inbound counterpart |
| `P06-B-49` | **NEW** — no import-batch identity |
| `P06-OQ-01` `sanitize_account_number` | still open, Class D |

---

# End
