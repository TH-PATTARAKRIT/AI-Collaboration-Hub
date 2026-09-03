# 09 — JT-04 Fact Package: Cost-of-Goods-Sold Recognition Timing

Source definition: `12_INVENTORY_RISK_GAP_DECISION_REGISTER_V1.md` — "`JT-04` | Cost-of-goods-sold recognition timing. | Delivery flow"

This is one of the two priority clusters the parent prompt names as previously found "not decidable from documentation alone."

## 1. What Is Already Established (Fact)

- The reference ERP has **two internally-contradictory documented answers** to "when is COGS recognized," corroborated across at least seven separate DR research files (`CGS-U01`):
  - **Pre-major-version-19:** COGS recognized at **delivery** (physical stock movement) — real-time interim posting.
  - **19.0+:** COGS recognized at **invoice/bill posting**, with the delivery-time mechanism demoted to a period-close gap-filler.
- Invoicing-policy (ordered vs. delivered quantities) interaction with this trigger table is **entirely undocumented** in any source reviewed (`CGS-U20`).
- Whether invoice-before-delivery is permitted, gated, or produces a matching-principle risk (COGS recognized before goods leave the seller's control) is `HOLD` under a strict reading of the 19.0+ rule (`CGS-U31`).
- Bill-before-receipt on the purchase side (the mirror-image timing question) is the weakest-evidenced sub-case in the entire package, inferred only by structural symmetry (`CGS-U30`).

## 2. Fact vs. Configuration vs. Interpretation vs. Assumption vs. Target Design

| Layer | Statement |
|---|---|
| **FACT** | The reference ERP's own version history contains two different, mutually exclusive recognition-timing rules, each independently documented. |
| **CONFIGURATION** | Which rule a given reference-ERP deployment follows depends on its version — this is externally observable, not a hidden internal state. |
| **INTERPRETATION** | Framing this as "the reference system changed its mind" (DR file `33` §3 point 1) is this research's own synthesis of the corroborating evidence, not a single quoted admission from the vendor. |
| **ASSUMPTION** | There is no evidence anywhere in the reviewed material that either timing rule is *required* by Thai accounting standards specifically — TAS-level guidance on COGS timing was not the subject of a dedicated primary-source pull in DR file `24`, and this session did not add one. This is a genuine remaining gap, distinct from the reference-ERP version-instability fact. |
| **TARGET DESIGN** | SMEsPlus's own recognition event (delivery, invoice, a combination, or configuration-dependent) is not decided by this file. That is exactly what `JT-04` must rule on. |

## 3. Why This Cannot Be Closed by Documentation Alone

Selecting a recognition event by "match what the reference does" fails because the reference does not have one behavior to match — this is not a research gap that more reading would fix, it is a structural fact about the benchmark's own history (file `33` §6 point 3, independently reconfirmed by this session against file `30` §11 in `02_PARENT_BASELINE_VERIFICATION.md`). Closing `JT-04` requires either:

1. **A Boss/Accounting-Owning-Team ruling** on which event SMEsPlus itself will use, informed by these facts but not derivable from them; or
2. **Thai-specific statutory guidance** on COGS/revenue-matching timing that was not separately, directly researched (a genuine open item, not previously flagged this precisely — see `12_BUSINESS_SME_QUESTION_REGISTER.md` and `13_THAI_ACCOUNTING_EVIDENCE_REGISTER.md` for how this session routes it).

## 4. Disposition

**HOLD — EVIDENCE REQUIRED, WITH A DECISION LAYER ON TOP.** The underlying fact (the reference system has no single answer) is FACT VERIFIED. The question `JT-04` actually needs answered for SMEsPlus (what event *SMEsPlus* uses) is not a fact-finding question at all past this point — it is a ruling. This session does not manufacture that ruling. It also newly identifies that the Thai statutory angle on recognition timing (as distinct from the reference-ERP version-history angle) has not been directly, primarily researched, and recommends that as the single highest-value next evidence step before Boss rules on `JT-04` (see file `13`).

## 5. Does New Evidence Materially Change the Proposed Disposition?

No new runtime/database evidence was acquired (per the evidence ceiling, file `05`). This session's contribution is: (a) confirming the "not decidable from docs alone" finding is accurate and traceable, not narrative drift, and (b) identifying the Thai-statutory-timing angle as a distinct, not-yet-pulled evidence thread that could narrow — though not eliminate — the decision Boss must make. This does not change the disposition from HOLD, but it does give the next session a concrete, bounded research action instead of "read the same documents again."
