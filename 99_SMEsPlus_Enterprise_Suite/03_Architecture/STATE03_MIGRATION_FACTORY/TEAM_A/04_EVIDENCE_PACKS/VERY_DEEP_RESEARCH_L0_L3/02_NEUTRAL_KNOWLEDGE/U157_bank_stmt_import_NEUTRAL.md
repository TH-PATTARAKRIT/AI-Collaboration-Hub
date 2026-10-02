# U157 — Bank Statement Upload Chain — Neutral Knowledge

**Unit:** U157 | **G Group:** G01 | **Priority:** P1
**Verdict:** ABSENT from Community
**Research date:** 2026-10-02

---

## What was searched

The Odoo 19.0 Community addons tree was inspected for any module providing a bank statement file upload, parsing, and ingestion workflow. The following module names were checked directly: the bank statement file-upload base module, the OFX format sub-module, the CSV format sub-module, and the CAMT or ISO 20022 format sub-module. None were found.

The core accounting module was also inspected for any wizard, controller, or method that accepts a file attachment and produces bank statement transaction records from it. No such artifact was found.

---

## What exists in Community

The core accounting module contains three relevant items that represent the data layer beneath an upload chain:

1. A bank statement header record — a grouping container that links to a journal and carries opening and closing balance figures.

2. A bank statement line record — the individual transaction record. This record uses a delegation relationship to a journal entry, meaning every transaction line is simultaneously a journal entry. The line carries dedicated fields for storing the counterparty name as received from an electronic source, the transaction category code from an electronic file, the raw bank account number before any partner matching, and extended transaction metadata in a structured format.

3. A generic document attachment ingestion framework — an abstract helper used by the invoice processing system. It provides hooks for format detection, embedded file extraction, and a decoder dispatch mechanism, but the base decoder hook has no implementation. Any format-specific behaviour must be contributed by an extension.

---

## What is absent

No upload wizard exists that accepts a file from the user interface and routes it to a parser.

No parser exists for the Open Financial Exchange format, comma-separated value bank files, or the ISO 20022 cash management message format.

No format detection logic exists that inspects a filename extension, MIME type, or file header bytes to select a parsing strategy.

No method exists that converts parsed file data into bank statement line records in bulk.

No automatic reconciliation trigger is wired to a file upload event. Reconciliation logic is present on the statement line model itself, but it operates through the bank reconciliation widget, not as a post-upload step.

No Thailand-specific bank statement file-upload module is present.

---

## Migration implication

Any SMEsPlus deployment that requires loading bank statements from files in OFX, CSV, CAMT, or similar formats must obtain this functionality from outside the Community source tree. The most common source is the Odoo Community Association module family maintained under the account statement upload umbrella. That family provides the wizard layer, the format dispatcher, and individual parser modules for each supported format. Without installing one of these alternatives, users can only create bank statement lines manually or through an online banking synchronisation service.

---

## Neutral-ref compliance note

This document contains no snake case identifiers, no dotted model names, no file extensions, no backtick-quoted code tokens, and no programming keywords. All references to code constructs use plain descriptive prose.
