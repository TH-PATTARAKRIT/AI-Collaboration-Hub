# U190 — res.partner.bank: Neutral Knowledge Reference
**Unit:** U190 | **Group:** G03 | **Priority:** P1  
**Date:** 2026-10-02

---

## CONCEPT OVERVIEW

Odoo separates the concept of a **bank institution** (`res.bank`) from a **bank account** (`res.partner.bank`). The institution holds the BIC/SWIFT code and address; the account holds the account number and links to a partner (the account holder). This two-level design allows multiple accounts at the same institution and multiple institutions per country.

---

## NEUTRAL KNOWLEDGE CLAIMS

| # | Claim ID | Topic | Plain-Language Statement |
|---|----------|-------|--------------------------|
| 1 | U190-N01 | Data model | A bank institution record stores the institution name, BIC/SWIFT code, country, and contact details. It is independent of any partner or company. |
| 2 | U190-N02 | Data model | A bank account record belongs to exactly one partner (the account holder) and optionally links to one bank institution. The account number is the primary identifier. |
| 3 | U190-N03 | Sanitization | When a bank account number is stored, all spaces, dashes, and punctuation are removed and letters are uppercased to produce a canonical form used for comparisons. |
| 4 | U190-N04 | Uniqueness | The system prevents the same canonical account number from being stored twice for the same partner. Two different partners may legitimately share the same account number in different contexts. |
| 5 | U190-N05 | Account type | Every bank account is classified as either a plain bank account or an IBAN account. The classification is determined automatically by testing whether the number passes IBAN validation rules, not by user selection. |
| 6 | U190-N06 | IBAN validation | An IBAN is valid if: it starts with a recognized two-letter country code, its total length matches the published national format for that country, and when digits and letter-to-number conversions are rearranged and divided by 97 the remainder is 1. |
| 7 | U190-N07 | IBAN formatting | When a number is recognized as a valid IBAN, it is automatically reformatted and stored in groups of four characters separated by spaces, regardless of how it was entered. |
| 8 | U190-N08 | BIC handling | Bank Identifier Codes (BIC/SWIFT) are stored in uppercase only. The system forces uppercase conversion on every save regardless of input case. |
| 9 | U190-N09 | Company scope | A bank account's company association is inherited from the partner who owns the account. There is no direct company field; the link is derived automatically. |
| 10 | U190-N10 | Journal link | In accounting, a bank-type journal may be linked to exactly one bank account record. The system enforces that the bank account's owning partner matches the company behind the journal. |
| 11 | U190-N11 | Soft delete | Deleting a bank account does not remove the database record. Instead the record is archived (marked inactive). Archived accounts are hidden in normal searches but their history is preserved. |
| 12 | U190-N12 | Archive guard | If a bank account for a given partner and number was previously archived, the system prevents creating a new record with the same details. The user is prompted to unarchive instead. |
| 13 | U190-N13 | Trust/fraud control | A bank account must be explicitly marked as trusted before it can be used for outgoing payments. This marking requires a specific permission group and, once applied, locks the account number and partner from modification. |
| 14 | U190-N14 | Payment providers | Online payment gateways (credit cards, PayPal, etc.) are managed through a separate payment-provider model and are not stored as bank account records. |
| 15 | U190-N15 | Thai PromptPay | Thailand's PromptPay instant-payment system is implemented by attaching a proxy identifier to a bank account record. The proxy can be a mobile number, a merchant tax ID, or an e-wallet ID. |
| 16 | U190-N16 | Thai proxy validation | A Thai merchant tax ID proxy must be exactly 13 digits. A Thai mobile number proxy must be exactly 10 digits. These are validated every time the record is saved. |
| 17 | U190-N17 | Thai QR encoding | When generating a PromptPay QR code for a Thai account, the mobile number's leading zero is replaced with the country code 66 and the result is padded to 13 characters before encoding. |
| 18 | U190-N18 | Thai currency restriction | Thailand PromptPay QR codes can only be generated for transactions in Thai Baht (THB). Other currencies produce an error. |
| 19 | U190-N19 | IBAN country coverage | Thailand (TH) does not use the IBAN standard. Thai bank accounts are always classified as plain bank accounts and never receive the IBAN type designation. |

---

## MIGRATION RELEVANCE SUMMARY

When migrating SMEsPlus to Odoo 19 Community with Thai operations:

1. Thai bank accounts use `proxy_type` and `proxy_value` fields added by `l10n_th` (which depends on `account_qr_code_emv`). Both modules must be installed.
2. The `allow_out_payment` flag defaults to False on all imported accounts — outgoing payment capability must be explicitly granted by an authorized user after import.
3. The uniqueness constraint is per-partner, not global. Migrated data must ensure no duplicate `(sanitized_acc_number, partner_id)` pairs.
4. No `l10n_th_bank_branch` field exists in Community 19 source — branch information is not a native field in this codebase.
5. `company_id` on bank accounts is read-only and cannot be set directly during import; it flows from the partner's company assignment.
