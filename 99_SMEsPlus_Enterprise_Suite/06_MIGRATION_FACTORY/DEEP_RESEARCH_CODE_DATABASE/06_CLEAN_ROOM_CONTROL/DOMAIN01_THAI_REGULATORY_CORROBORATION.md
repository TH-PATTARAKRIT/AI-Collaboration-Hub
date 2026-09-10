# DOMAIN_01 — Thai Regulatory Corroboration

Session: `[SMEPLUS-26-08-28-DEEP-CD-001]`  
Date: 2026-08-29 Asia/Bangkok  
Reviewer: ChatGPT L99  
Status: **PASS WITH CONTROL — NARROW CLAIMS CORROBORATED / BROAD STATUTORY CLOSURE HOLD**

## 1. Objective

Improve the regulatory provenance of DOMAIN_01 Accounting Core using official Thai authority sources, while keeping the exact scope of each legal/regulatory claim explicit.

## 2. Official Source Anchors

### TH-RD-01 — Revenue Department, Revenue Code Section 86/4

Official Revenue Department source: `https://www.rd.go.th/5208.html`

Supported narrow fact:

- a full tax invoice must contain the tax-invoice sequence number and, where applicable, the book sequence number as a minimum item.

Control:

- this does **not** by itself prove that all tax-invoice numbers must be universally gapless;
- it does **not** establish a gapless-numbering requirement for the general ledger or all journal entries.

### TH-RD-02 — Revenue Department VAT Announcement No. 46

Official Revenue Department source: `https://www.rd.go.th/3394.html`

Supported narrow fact for approved cash-register abbreviated tax invoices:

- the sequence number proceeds numerically until the digit capacity is exhausted, subject to the stated restart condition;
- the continuous daily transaction journal paper in that specific cash-register regime is retained for five years.

Control:

- the strict numerical-sequence rule is scoped to this abbreviated-tax-invoice / cash-register regime;
- the five-year retention statement is also scoped to that regime and must not be generalized into a universal accounting-record retention rule without separate authority.

### TH-ETDA-01 — ETDA e-Tax Invoice Standard

Official ETDA source: `https://www.etda.or.th/th/Our-Service/Standard/OID/Information/Our-Works/e-Tax-Invoice/e-Tax-Invoice.aspx`

Supported narrow fact:

- creation of electronic invoice / e-Tax invoice data and digital-signature handling for Revenue Department submission must follow the related electronic transaction standards.

### TH-ETDA-02 — ETDA e-Tax Invoice/e-Receipt FAQ

Official ETDA source: `https://www.etda.or.th/th/contact/faq/e-Tax-Invoice-e-Receipt.aspx`

Supported narrow fact:

- e-Tax Invoice/e-Receipt is electronic document data signed with Digital Signature;
- submission to the Revenue Department uses the prescribed XML standard.

## 3. Claim Disposition

| Claim | Evidence Position | Disposition |
|---|---|---|
| Full tax invoices contain a sequence number | Official Revenue Department support | VERIFIED WITH CONTROL |
| All tax invoices must be globally gapless | Not established by Section 86/4 alone | HOLD / DO NOT GENERALIZE |
| Approved cash-register abbreviated tax invoices use numerical sequence progression | Official Revenue Department support | VERIFIED WITH CONTROL — NARROW SCOPE |
| General ledger entries require gapless numbering under Thai law | Not established by reviewed official evidence | HOLD / UNKNOWN |
| e-Tax Invoice/e-Receipt uses digital signature and prescribed electronic standard | Official ETDA support | VERIFIED WITH CONTROL |
| All general-ledger records require digital signature / tamper-evidence | Not established by reviewed official evidence | HOLD / UNKNOWN |
| Universal 5–7 year accounting-record retention | Not closed by the narrow official sources reviewed here | HOLD / SEPARATE PRIMARY-LAW REVIEW REQUIRED |

## 4. Required Correction to Team A Candidate Input

The sanitized Team B candidate must distinguish:

- `REGULATORY REQUIREMENT — VERIFIED, NARROW SCOPE`;
- `REGULATORY REQUIREMENT — PARTIAL / SECONDARY`;
- `ERP COMMON PATTERN`;
- `INDEPENDENT CONTROL RECOMMENDATION`;
- `UNKNOWN / LEGAL REVIEW REQUIRED`.

No narrow e-Tax or tax-invoice requirement may be promoted into a general-ledger-wide requirement without separate evidence.

## 5. Gate Impact

- Improves source quality for the narrow Thai tax-invoice and e-Tax claims.
- Does **not** close DR-GAP-014 independent legal/license sign-off.
- Does **not** close the broader Domain01 Thai statutory unknowns.
- Supports CORR-002 and a later independent re-audit.

`No Evidence = No Progress.`
