# 10 — JT-01 Targeted Resolution: Which Concept Owns Valuation Policy

Source fact package: Fact Verification session file `08_JT01_FACT_PACKAGE.md`.

## 1. What Is Known (cited)

- Product Category is the reference ERP's default policy-carrying record for Costing Method and Stock/Valuation accounts; Product-level fields override some (not all) Category defaults, for the versions/fields directly evidenced.
- The "Category owns, Product overrides" framing is this research's own interpretation, not a directly-quoted vendor statement.
- Eight distinct sub-unknowns block treating this as an adoptable answer: field-meaning mode-polymorphism (`CGS-U06`), re-class behavior on ownership change (`CGS-U07`, `CGS-U08`), fallback-layer existence (`CGS-U09`), Fiscal Position override scope (`CGS-U11`), incomplete current-version mapping (`CGS-U12`), company-exclusivity of the accounting package (`CGS-U13`), and company-scoping of Category itself (`CGS-U42`).

## 2. What Is Genuinely Unknown

Whether SMEsPlus should adopt a Category-owns/Product-overrides model at all (never demonstrated as a requirement, only as the reference pattern), and — even if it does — how that model behaves under ownership change, multi-company isolation, and the four-way precedence ambiguity (Category / Product / Fiscal Position / possible Journal-level fallback).

## 3. Classification of the Unknown Itself

`JT-01` is a **DESIGN DECISION**. Unlike `JT-04`/`JT-05`, it is not gated on a single dominant business-policy or statutory question — it is gated on eight parallel FACT/CONFIGURATION unknowns about the reference pattern's own mechanics, none of which is itself a policy choice. This makes `JT-01` structurally different: it is closer to "insufficient fact base to design from" than "facts exist, a ruling is needed."

## 4. Evidence That Would Resolve It

All eight sub-items in file `04` (P0 gate blocker register) under the `JT-01` gate: `CGS-U06`, `CGS-U07`, `CGS-U08`, `CGS-U09`, `CGS-U11`, `CGS-U12`, `CGS-U13`, `CGS-U42`. Six of the eight (`CGS-U06`, `U09`, `U11`, `U12`, `U13`, `U42` partially) are answerable by a bounded documentation re-fetch; two (`CGS-U07`, `CGS-U08`) explicitly require a live reference-instance test per the source register.

## 5. Owner

- Six re-fetchable items → Docs/Research owner.
- Two live-instance items (`CGS-U07`, `CGS-U08`) → Research owner, blocked pending live-instance access.
- The ultimate design choice (adopt Category-as-owner, adapt it, or design something SMEsPlus-native) → **Boss / Architecture owner**, informed by but not decided by the above facts.

## 6. Can It Be Parallelized?

Yes, extensively. All eight sub-items are independent of each other and can be researched concurrently; none blocks the others from starting. This is the most parallelizable of the three priority items.

## 7. Does It Block a Gate?

Yes — `JT-01` is named as blocking the valuation report, close process, landed cost, and category design (per its own source definition in `12_INVENTORY_RISK_GAP_DECISION_REGISTER_V1.md`), making it arguably the broadest-reaching of the three priority items even though it is evidentially the least contested (no vendor-admitted gap, unlike `JT-05`; no version-contradiction, unlike `JT-04` — its blockers are simply incomplete evidence).

## 8. Disposition: NOT DECIDABLE

**NOT DECIDABLE this session.** Missing: six re-fetchable documentation facts (not available this session — no working live-fetch tool confirmed, file `01` §2) and two live-instance-only facts (not available this session).

This session evaluated whether `JT-01` could be **DECIDABLE WITH CONTROL** — e.g., "adopt Category-as-owner now, with a mandatory manual review gate on any category reassignment until `CGS-U07`/`CGS-U08` are resolved." This is closer to viable for `JT-01` than for `JT-04`/`JT-05`, because the missing facts are narrower and more mechanical (not business-policy-dependent). However, it is still rejected as this session's classification because `CGS-U42` (whether Category is even company-scoped) is a precondition for a multi-tenant SMEsPlus to safely adopt Category as the owning concept at all — proceeding without that fact risks a cross-tenant data-isolation defect, which is a higher-severity risk than the convenience of an earlier decision. **NOT DECIDABLE** stands, with a note that this is the priority item closest to reclassification once the six re-fetchable items are resolved (potentially without even needing the two live-instance items, if `CGS-U42` and `CGS-U06` alone are cleared favorably).

## 9. One-Line Reason (for the final report)

Eight parallel documentation/live-instance facts about the reference ownership pattern remain unresolved, including whether the candidate "owner" concept is even multi-tenant-safe — none of the eight was answerable with this session's tool access.
