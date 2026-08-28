> DOMAIN_01 — Accounting Core | Team A PART 2 (Sonnet) | Input: committed Part 1 evidence | No SMEsPlus design

# 08 — CROSS-SOURCE TRIANGULATION MATRIX (A6, closed to 9/9 addressed)

```
A6 STATUS: 9 / 9 targets addressed (6 with independent evidence this round + 3 carried
           from Part 1). NOT all reach VERIFIED CLOSED — several remain UNKNOWN honestly.
```
No IFRS/TFRS/Thai statutory clause is fabricated anywhere in this pack. Every citation below
was retrieved this session via WebSearch; none is drawn from model memory alone.

| # | Finding | Reference system | Accounting standard | ERP #2 | ERP #3 | Conclusion | Classification |
|---|---|---|---|---|---|---|---|
| T-01 | Debit = credit | App-enforced, suppressible, no DB backstop | Foundational identity — [Wikipedia: Double-entry bookkeeping](https://en.wikipedia.org/wiki/Double-entry_bookkeeping), [Accounting equation](https://en.wikipedia.org/wiki/Accounting_equation) | — | — | **UNIVERSAL PRINCIPLE** (requirement) / vendor-specific (implementation) | A (principle) / E (mechanism) |
| T-02 | Correction by reversal, not deletion | Both reversal (CF-04) AND reset-to-draft (CF-06) available | — | SAP B1: posted entries **cannot** be deleted, only reversed ([sap-business-one-tips.com](https://www.sap-business-one-tips.com/en/reverse-journal-entry/), [SAP Community](https://community.sap.com/t5/enterprise-resource-planning-q-a/how-to-delele-journal-entry-document-in-sap-business-one/qaq-p/482022)) | — | **CROSS-ERP COMMON** for reversal-as-principle; reference system's reset-to-draft path **CONFLICTS** with it | D (principle) / E (reset-to-draft mechanism, divergent) |
| T-03 | Period close prevents posting | 6 lock fields + per-user variants + exception + bypass sentinel | — | NetSuite: 3-state period (Unlocked/Locked/Closed) + 1 override permission ([Oracle NetSuite](https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_N1451780.html)) | — | **CROSS-ERP COMMON** (principle); reference system's *shape* is more fragmented than peer | D (principle) / E (shape) |
| T-04 | Journal / ledger concept | Journal (classification+control unit) → move (header) → move_line (posting atom) | Journal = book of original entry; Ledger = authoritative source for financial reports — [Books of original entry — AccountingTools](https://www.accountingtools.com/articles/what-are-books-of-original-entry.html), [General journal — Wikipedia](https://en.wikipedia.org/wiki/General_journal) | — | — | **UNIVERSAL PRINCIPLE** — journal/ledger distinction is foundational, matched by the reference system's shape | A |
| T-05 | Posting concept | `action_post` transitions draft→posted, assigns sequence number | Posting = transferring/finalizing journal entries into the ledger, classifying phase of accounting — [Post to the Ledger — Lumen Learning](https://courses.lumenlearning.com/suny-finaccounting/chapter/journalizing-and-posting-to-the-general-ledger/), [Posting to the ledger — Accountingverse](https://www.accountingverse.com/accounting-basics/accounting-ledger.html) | — | — | **UNIVERSAL PRINCIPLE** — posting-as-finalization concept matches | A |
| T-06 | Multi-currency accounting principle | Dual amount pair (company-currency debit/credit/balance + `amount_currency`); rate validated at header | IAS 21 distinguishes functional currency from foreign currency; foreign-currency transactions recognised at spot rate, monetary items remeasured at each reporting date — [IFRS — IAS 21](https://www.ifrs.org/issued-standards/list-of-standards/ias-21-the-effects-of-changes-in-foreign-exchange-rates/), [IAS 21 — ICAEW](https://www.icaew.com/technical/corporate-reporting/ifrs/ifrs-accounting-standards-tracker/ias-21-the-effects-of-changes-in-foreign-exchange-rates) | — | — | **REGULATORY REQUIREMENT** (IFRS) for the dual-currency concept; the reference system's dual-amount-pair shape is a reasonable implementation of it | B (principle) / D (implementation shape) |
| T-07 | Audit trail as a statutory obligation | Opt-in per-journal hash chain; company `restrictive_audit_trail` | Thailand: Accounting Act B.E. 2543 requires financial statements be prepared/retained and audited by a licensed CPA; records retained 5–7 years under the Revenue Code — [Emerhub — Financial Audits in Thailand](https://emerhub.com/thailand/financial-audits-in-thailand/), [Accounting Act — samuiforsale.com](https://www.samuiforsale.com/law-texts/accounting-act.html) | — | — | **REGULATORY REQUIREMENT** for retention/auditability in general; **tamper-evidence specifically** confirmed only for e-Tax invoices (T-08), NOT the general ledger | B (retention) / G (general-ledger tamper-evidence mandate) |
| T-08 | Document immutability as a legal requirement (Thailand) | Opt-in hash chain, not default-on for the general ledger | **AUTHORITY UPGRADED (SONNET-CORR-001):** ETDA (Electronic Transactions Development Agency — the official Thai government body) publishes its own terminology: *"'Integrity of content' means that the required invoice or document content has not been altered," "'Authenticity of the origin' means the assurance of the supplier's identity,"* under Recommendation RETS 21-2562 — [ETDA — e-Tax Invoice & e-Receipt Service Provider Certification](https://www.etda.or.th/en/Our-Service/e-tax-Invoice-Receipt-1.aspx). Secondary sources (retained as corroboration, not primary authority): [esignglobal.com](https://www.esignglobal.com/blog/use-digital-signature-e-tax-invoices-thailand-rd), [fiscal-requirements.com](https://www.fiscal-requirements.com/news/4698) | — | — | **REGULATORY REQUIREMENT, now P1/official-source confirmed**, scoped to e-Tax invoices/receipts; **still not proven to extend to every journal entry** | B, upgraded from P4 to P1/P3 confidence (for e-Tax invoices) / G (for the general ledger, unchanged) |
| T-09 | Gapless numbering as a legal requirement (Thailand) | `secure_sequence_number` — gapless, but only on hash-protected journals | **AUTHORITY UPGRADED (SONNET-CORR-001):** fetched directly from the **official Revenue Department of Thailand website** — Section 86 requires a tax invoice to state *"Serial number of tax invoice and, if any, of book"* as one of its mandatory particulars, alongside the registrant's tax ID, the word "tax invoice," description/value of goods, VAT amount, and date of issuance — [Revenue Department of Thailand — Section 85\_86 (English)](https://www.rd.go.th/english/37741.html). **Precision note:** the primary text confirms a serial number is MANDATORY; it does not itself use the word "gapless" or explicitly discuss audit treatment of gaps — that characterization remains sourced only to the secondary compliance summary [Thailand Tax Invoice Requirements](https://invoicedataextraction.com/blog/thailand-tax-invoice-requirements) and is not re-claimed as primary-sourced | — | — | **REGULATORY REQUIREMENT** for tax invoices, mandatory-serial-number element now **P1/official-source confirmed**; the stronger "must be gapless / gaps are audited" claim remains **P4 secondary-source only** | B, split confidence: P1 (serial number required) / P4 (gapless-specifically) (for tax invoices) / G (for all journal entries, unchanged) |

## AUTHORITY UPGRADE SUMMARY (SONNET-CORR-001)
Both Thai statutory findings were re-sourced this round from secondary compliance summaries to
primary/official sources: **Revenue Department of Thailand** (rd.go.th, official English site,
fetched directly — Section 86 text) and **ETDA** (etda.or.th, the government body itself,
publishing its own integrity/authenticity terminology). This is a genuine authority upgrade,
not a re-statement of the same claim with a better-looking citation: the primary Revenue
Department text was read and quoted directly, and it confirms the *mandatory serial number*
requirement precisely while NOT independently confirming the stronger "gapless numbering /
audit-flagged gaps" characterization — that distinction is preserved rather than smoothed over.

## CONFIDENCE NOTE ON T-09 (historical, retained for the record)
The Revenue Code §86 citation is drawn from a **secondary source** (a compliance-focused blog)
summarising the statute, not from the primary Revenue Code text itself. This is recorded as
**Provenance P4** (cross-vendor/compliance documentation), not P1 (primary regulatory text).
The underlying claim — that Thai tax invoices require genuine sequential numbering and that
gaps are an audit red flag — is plausible and consistent with common VAT-invoice practice
across jurisdictions, but a primary-source citation (the Revenue Code itself, or an official
Revenue Department publication) was not obtained this round and should be sought before this
finding is treated as fully regulatory-grade (Class B rather than a stronger-provenance A/B).

## WHAT REMAINS GENUINELY UNKNOWN AFTER THIS ROUND
- Whether Thai law requires tamper-evidence for the **general ledger**, not just e-Tax invoices.
- Whether Thai law requires gapless numbering for **all** accounting entries, not just tax
  invoices under Revenue Code §86.
- Primary-source (statute-text) confirmation of either Thai finding.
These are recorded as unknowns, not resolved by inference from the adjacent, confirmed findings.
