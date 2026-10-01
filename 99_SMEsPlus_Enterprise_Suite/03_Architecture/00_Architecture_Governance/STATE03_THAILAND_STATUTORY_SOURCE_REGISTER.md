# STATE03 Thailand Statutory Source Register

Document ID: `STATE03-THAILAND-STATUTORY-SOURCE-REGISTER`
Status: `OPEN — SEED PASS (2026-10-02)`. Created per Boss order "Continue U24-U28 automatically" item 3. Purpose: give DeepSeek's `U24` (Thailand localization) and `U28` (Thai entity structures) research, and this session's own reconciliation, a named, citable set of **official regulatory sources** to check Odoo's `l10n_th` implementation against — per item 4 of the same order, **code presence in `l10n_th` is never treated as proof of legal compliance**; every statutory claim in STATE03 must trace to an entry in this register, not to Odoo source alone.

**Evidence tier discipline for every row below**: `PRIMARY` (the issuing agency's own site/document, directly read) vs `SECONDARY-CONFIRMED` (a professional-services/law-firm summary citing a named primary instrument, not yet independently pulled from the agency site itself). **This seed pass was built via `WebSearch` summaries, not direct retrieval of primary PDFs/pages** — every row is `SECONDARY-CONFIRMED` until a primary document is actually fetched and cross-checked. No row in this register is `CLAUDE-VERIFIED CANDIDATE` or any higher status on this pass. Boss remains Sole Final Approver; this register does not assert statutory correctness, only names where to look.

> **SUPERSEDED BY `TXS` (2026-10-02)** — DeepSeek's Atomic Boundary `TXS` (`TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3/07_THAI_TAX_CORE/TXS_thai_statutory_source_register.md`) is now the **authoritative** Thai statutory source register: 120 statements against 55 official primary sources (many read raw, `R`, not just summarised, `S`), verified by this session — see `STATE03_VDR_CLAUDE_VERIFICATION_LOG.md` §20. This seed register is kept for lineage only; do not cite it over `TXS`. Two rows below are specifically **corrected** by `TXS`'s primary-source read (not deleted, flagged in place):
> - §3 ("e-Tax Invoice/e-Receipt XML schema... 'Standard 3-2560'"): **TXS found this citation unsupported** — ETDA's own standards page names "Recommendation 14-2560" (XML/digital-signature/host-to-host) and "21-2562" (information security); "3-2560" does not appear on the official page read. Treat the §3 row as wrong, not merely unconfirmed.
> - §1 ("WHT filing... e-filing mandatory from 2025-01-01"): **TXS found this overstated** — official RD announcements show mandatory e-filing for *employer* withholding forms (PND 1/1 Kor) from B.E. 2567 (2024), and new withholding-form editions effective for payments from 1 Jan 2025 — no official statement was found that PND 3/53 e-filing specifically is mandatory from a single blanket date.
> `TXS` also found a concrete, time-bound fact not in this seed at all: **the current 7% VAT rate (6.3% + 0.7% local-tax share) is a temporary reduced rate under Royal Decree No. 807 B.E. 2569, valid only for VAT liabilities arising 1 Oct 2017 – 30 Sep 2027** — the rate after that date is not established by any source read. `High` last-change-risk.

## 1. Revenue Department (RD) — rd.go.th — tax authority (VAT, Withholding Tax, e-Tax Invoice administration)

| Topic | Instrument / citation (as reported) | Key point | Tier | Next step |
|---|---|---|---|---|
| Withholding Tax (WHT) | Revenue Code provisions on WHT; rates by payment type (1% interest/transport, 3% services/telephone, 5% rent/prizes — as reported) | WHT computed on VAT-exclusive amount; payer remits on recipient's behalf | SECONDARY-CONFIRMED | Pull the Revenue Code's WHT sections and the current rate schedule directly from rd.go.th |
| WHT filing | Monthly filing, due 7th of the following month; e-filing mandatory from 2025-01-01 (as reported) | Determines filing-cycle/period assumptions for any WHT-posting research | SECONDARY-CONFIRMED | Confirm current filing deadline and e-filing mandate wording on rd.go.th |
| VAT | Revenue Code VAT provisions (general reference only, no specific announcement number captured this pass) | Thailand VAT system, standard/zero rates, registration threshold | SECONDARY-CONFIRMED | Pull VAT Act sections directly |
| e-Tax Invoice & e-Receipt | Announcement of the Director-General of the Revenue Department No. 48 (effective 2022-08-19, as reported) — forms, delivery method, storage, information-security requirements | RD, not ETDA, is the administering tax authority for e-Tax Invoice; filing of e-invoice due by the 15th of the month following delivery to the buyer; e-invoices must be digitally signed | SECONDARY-CONFIRMED | Pull Announcement No. 48 text directly from rd.go.th |

## 2. Department of Business Development (DBD) — dbd.go.th — company registration, financial-statement filing

| Topic | Instrument / citation (as reported) | Key point | Tier | Next step |
|---|---|---|---|---|
| Financial statement e-filing | DBD e-Filing system (efiling.dbd.go.th); paper filing discontinued since 2020-04-01 | XBRL is the mandated structured-data submission format; relevant to any statutory-report/e-filing capability research | SECONDARY-CONFIRMED | Confirm current e-Filing system requirements and XBRL taxonomy version on dbd.go.th |
| Filing deadlines | Private limited company: AGM within 4 months of fiscal year-end, DBD filing within 1 month of AGM; foreign-company branch: no AGM, files within 150 days of fiscal year-end; BOJ 5 (shareholder list) within 14 days of AGM (as reported) | Directly relevant to `U28`'s foreign-branch/representative-office research — branches follow a different filing clock than ordinary companies | SECONDARY-CONFIRMED | Confirm BOJ 5 and branch-filing deadline citations directly from DBD regulation text |

## 3. Electronic Transactions Development Agency (ETDA) — etda.or.th — e-document technical standards

| Topic | Instrument / citation (as reported) | Key point | Tier | Next step |
|---|---|---|---|---|
| e-Tax Invoice/e-Receipt XML schema | "Standard 3-2560" (published 2017, as reported) | ETDA sets the *technical/XML schema* standard; RD administers the *tax-law* requirement — the two must not be conflated in any STATE03 finding | SECONDARY-CONFIRMED | Pull Standard 3-2560 directly from etda.or.th |
| Electronic Transactions Act | Electronic Transactions Act B.E. 2544 (2001) and amendments (general reference only, not independently pulled this pass) | Underlying legal basis for electronic signatures/documents in Thailand, relevant to e-invoicing and any digital-signature claim | SECONDARY-CONFIRMED | Pull Act text directly |

## 4. Bank of Thailand (BOT) — bot.or.th — foreign exchange control, cross-border transaction reporting

| Topic | Instrument / citation (as reported) | Key point | Tier | Next step |
|---|---|---|---|---|
| FX transaction reporting | Authorized banks report FX purchase/sale/deposit/withdrawal to BOT; records retained ≥5 years for BOT inspection (as reported) | Directly relevant to `U25` (multi-currency/international transactions) — any SMEsPlus FX-transaction-logging design question should check this threshold/retention rule | SECONDARY-CONFIRMED | Pull the underlying BOT notification/regulation directly |
| FET form threshold | Single FX transaction ≥ USD 50,000 (or equivalent) requires a Foreign Exchange Transaction (FET) form (as reported) | A concrete, checkable threshold — good candidate for a `U25` claim once independently confirmed | SECONDARY-CONFIRMED | Confirm current threshold (reported figures varied — one source cited USD 50,000 for the FET form, another cited USD 200,000 as a newer, stricter documentary-evidence threshold effective 2025-12-29 for inbound transfers — **these may be two different rules (routine FET filing vs. enhanced source-of-funds documentation) and must not be conflated; confirm both directly from BOT** |
| Administration | FX only through commercial banks and BOT-licensed non-bank authorized entities (money changers, money transfer agents) | Scopes who can legally be a counterparty to a company's FX transaction in Thailand | SECONDARY-CONFIRMED | Confirm licensing-authority citation directly |

## 5. Thai Customs Department — customs.go.th — import/export

| Topic | Instrument / citation (as reported) | Key point | Tier | Next step |
|---|---|---|---|---|
| Import declaration | Goods Declaration + supporting documents required at port of entry; goods not legally entered until Customs authorizes release and duties/taxes are paid | Relevant to any `U25`/international-transaction research touching physical goods movement across the Thai border | SECONDARY-CONFIRMED | Pull current Customs Act/regulation text directly |
| e-Import system | Electronic submission, no paper documents required (as reported) | Relevant to any e-document/integration-contract research touching customs | SECONDARY-CONFIRMED | Confirm current e-Customs system scope directly |
| Valuation | Transaction value method, per importer-declared value where determinable | Baseline valuation rule for import duty computation | SECONDARY-CONFIRMED | Pull Customs Act valuation provisions directly |

## 6. Federation of Accounting Professions (TFAC) — tfac.or.th — Thai accounting/financial-reporting standards

| Topic | Instrument / citation (as reported) | Key point | Tier | Next step |
|---|---|---|---|---|
| TFRS / TAS | Thai Financial Reporting Standards (TFRS) and Thai Accounting Standards (TAS), set by TFAC's Accounting Standard Setting Committee under the Accounting Professions Act B.E. 2547 (2004) | TFRS are IFRS-based translations, one-year effective-date lag from IFRS, early adoption permitted; TFRS mandatory for Publicly Accountable Entities (PAEs) | SECONDARY-CONFIRMED | Pull the current TFRS/TAS standard-by-standard list and PAE-vs-NPAE applicability rules directly from tfac.or.th |
| TFRS for NPAEs | Revised TFRS for Non-Publicly-Accountable Entities, effective 2023-01-01 (as reported) | Directly relevant — most SMEsPlus-scale Thai entities are likely NPAE, not PAE; the applicable standard set differs | SECONDARY-CONFIRMED | Confirm NPAE scope/applicability criteria directly from TFAC |

## 7. Discipline rules (per Boss order items 2 and 4 — apply to every row added to this register going forward)

- **Classify Thailand applicability by business behavior and jurisdiction, not by `l10n_*` naming alone.** A capability is Thailand-in-scope because a Thai legal entity (or a foreign entity's Thailand-jurisdiction branch/subsidiary/representative/regional office) needs it to comply with a rule in this register — not merely because an Odoo module happens to be named `l10n_th_*`. Conversely, a non-`l10n_th`-named Odoo mechanism (e.g. a generic engine feature, or a differently-named module) can still be Thailand-relevant if it implements something this register requires.
- **Code presence is not legal compliance proof.** Any STATE03 finding that says "Odoo's `l10n_th` implements X" must be kept in a column/section separate from "Thai law requires Y" — the two are only to be stated as matching when a specific row of this register is cited and cross-checked, never inferred from code alone. Where no register row yet exists for a given Odoo `l10n_th` behavior, the correct status is `UNKNOWN — STATUTORY SOURCE REQUIRED`, not an implied pass.

## 8. What this register is not

Not a legal opinion, not tax/accounting advice, not a Gate PASS, not Formal Coverage, not independently verified against primary agency text (every row is `SECONDARY-CONFIRMED` pending a primary pull). Existence of a row does not mean Odoo's `l10n_th` correctly implements it — that cross-check is separate, future work. Boss/PMO may supply a more authoritative source at any time, which supersedes a row here without deleting it (lineage preserved, per the same discipline used throughout `05_CORRECTION_LOOP/`). Boss remains Sole Final Approver.
