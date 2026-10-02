# U173 — res.currency: Multi-Currency Rate Management and Conversion Chain
**Unit**: U173 | **Module**: base + account | **GAP**: G01
**Date**: 2026-10-02 | **Status**: GATE-PASS

## Currency Model Architecture

Each currency record stores a three-character ISO code as its identifying name, a display symbol, a rounding factor, and a symbol position (before or after the amount). A uniqueness constraint prevents duplicate currency codes. Currencies may be active or inactive; only active currencies are accessible for transaction entry. A group-membership mechanism automatically enables or disables the multi-currency user interface based on whether more than one currency is currently active.

## Decimal Precision Derivation

The number of decimal places is not stored directly; it is derived from the rounding factor using a logarithm formula at store time. A rounding factor of 0.01 produces two decimal places. A rounding factor of 1.0 or greater produces zero decimal places. The derived value is stored for query performance. This approach means decimal precision is always consistent with the rounding factor — there is no way to set them independently.

## Exchange Rate Records

Each exchange rate is identified by a date (the effective date), a currency, and an optional company. Only one rate per combination of date, currency, and company is permitted. The rate value expresses the relationship of the currency to the system's reference currency. Rates must be strictly positive. Branch companies are blocked from creating rates directly; only root-level companies may own rate records.

## Rate Lookup Algorithm

When a conversion rate is needed for a given date and company, the system first searches for the most recent rate on or before that date for the matching currency and company (including company-neutral global rates). If no such rate exists, it falls back to the oldest available rate for that currency and company. If no rate exists at all, a default of 1.0 is returned. This three-tier resolution (exact-or-before → earliest-fallback → 1.0) means conversions never fail due to a missing rate.

## Conversion Formula

Converting an amount from one currency to another multiplies the amount by an inverse-rate quotient derived from the rate records. The result is optionally rounded using the destination currency's rounding factor and HALF-UP tie-breaking. Zero amounts bypass the rate engine entirely and return 0.0 directly. When converting within the same currency, the multiplier is exactly 1 without any rate lookup.

## Rounding Behaviour

All currency rounding uses HALF-UP semantics by default: tie values round away from zero. The implementation normalises the value before rounding to avoid IEEE-754 floating-point representation errors, applying a small epsilon correction to push borderline values in the correct direction before the integer rounding step.

## Multi-Company Rate Sharing

Rate records always belong to root companies. The conversion chain resolves any company to its root before performing lookups. Rates with no company set are treated as global fallbacks visible to all companies. Branch companies transparently inherit their root's rates — they cannot be given private rates.

## Inverse Rate Display

The currency view exposes two user-facing rate fields: one showing how many units of the foreign currency equal one unit of the base currency, and an inverse showing how many units of the base currency equal one unit of the foreign currency. The column headers for these fields are dynamically relabelled to name the viewing company's base currency, so the user always sees labels like "EUR per Unit" rather than generic field names.

## Thai Baht Standard Configuration

Thai Baht (THB) is defined in Odoo's standard currency dataset with a rounding factor of 0.01 (two decimal places), symbol ฿, and a "Satang" subunit. It is shipped inactive by default and must be manually enabled per company. This means no special rounding override is needed for Thai accounting — standard two-decimal-place behaviour applies.

## Account Move Currency Integration

A journal entry's currency is computed from a priority chain: the bank statement line's foreign currency if present, then the journal's own currency, then the existing value, then the company's base currency. The field is required and stored, making every journal entry explicitly currency-aware. An exchange gain/loss journal on the company record receives all foreign-currency revaluation entries; this journal must be of the general type.

## Cash-Basis Tax Exigibility Flag

A Boolean flag on journal entries marks non-invoice entries as always tax-due regardless of cash-basis tax settings. This flag is computed as true whenever the entry is not an invoice and has no pending cash-basis tax values, ensuring that manually created journal entries with tax lines are not incorrectly deferred.
