# 29 — 9 Special Team Findings and Learning Absorption

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `SPECIAL TEAM SYNTHESIS — DERIVED FROM FILES 02–27 — NO NEW EVIDENCE ASSERTED, NO DECISION MADE`

---

## 0. Purpose

Governing prompt §16 requires all nine Special Teams to report on this material given its Accounting × Inventory backbone materiality. Each team below reports current understanding, evidence, hypothesis, unknowns, contradictions, what was tried, findings, what the Owning Team (future COGS Final Solution / Joint session) must absorb, a reusable reasoning pattern, and a future trigger to detect the same problem again. No Special Team is or becomes the owner of COGS/Accounting knowledge — ownership stays with the Accounting Owning Team, tested in file `32`'s Teach-Back.

---

## S1 — COGS / Financial Accounting

**Current understanding.** COGS is not one event type in the reference ERP — it is a configuration-dependent outcome of (accounting standard × valuation cadence × version). Under Continental/Periodic, COGS is a period-end residual, never a per-transaction figure. Under Anglo-Saxon/Perpetual, COGS is a per-transaction figure, but *which* transaction triggers it changed materially across major versions (delivery-adjacent, pre-19, `PROVISIONAL`; unambiguously customer-invoice, 19.0+, `VERIFIED`).

**Evidence.** Files `12`, `13`, `14`, `18` — the single most cross-corroborated finding in the whole package (also independently touched by files `02`, `06`, `09`, `16`).

**Hypothesis.** SMEsPlus cannot adopt "the reference ERP's COGS timing" as a design shortcut because no single stable answer exists to adopt; `JT-04` must be decided from first principles (Thai matching-principle requirement, file `24` §2.4) plus SMEsPlus's own control objectives.

**Unknowns.** Exact pre-19 posting instant (invoice-post vs. some other reconciliation moment) remains `PROVISIONAL`; whether invoice-before-delivery is permitted, gated, or warned against under either Perpetual regime is `HOLD`.

**Contradictions.** File `13` §4.4 records the reference ERP's own pre-19 documentation containing two sentences that are not self-consistent read literally ("COGS reported when sold or delivered" vs. "cost recorded as expense only when invoiced").

**What was tried.** Direct fetch of the current-version Finance/Accounting settings page (twice, both failed with empty-content errors); fallback to search-index reconstruction plus a companion Inventory-app cheat-sheet page that did fetch successfully, cross-checked against an official conference/release source.

**Findings absorbed by the Owning Team.** COGS recognition timing is the single highest-priority item for the eventual `JT-04` Joint session; the version instability itself, not any one version's behavior, is the deliverable.

**Reusable reasoning pattern.** When a reference system's own documentation disagrees with itself within one version (file `13` §4.4) or across versions (file `02` §4.1), record both readings, synthesize the most defensible resolution explicitly labeled `PROVISIONAL`, and never silently pick one.

**Future trigger.** Any future research pass touching COGS timing must re-check whether a *newer* reference-ERP major version has again changed the trigger event before citing "current" reference behavior.

---

## S2 — Inventory Costing

**Current understanding.** Three costing methods are natively selectable (Standard, AVCO, FIFO); Specific Identification is not a reference-ERP UI option but is independently a live Thai/IAS-2-family requirement for non-interchangeable or project-segregated inventory (file `15` §4.4, corroborated `AUTHORITATIVE` by file `24` §2.2's TAS 2 cost-formula list).

**Evidence.** File `15` (full method-by-method matrix), file `24` §2.2 (Thai-authoritative cost-formula list: specific identification, FIFO, weighted average — LIFO explicitly not permitted).

**Hypothesis.** Removal strategy (physical picking order) and costing method (financial valuation) are documented as independent, only coincidentally-aligned concepts — a same-named "FIFO" trap the reference ERP's own documentation warns against conflating.

**Unknowns.** Existing-stock conversion mechanics on a costing-method change (all three methods, both directions) — consistently `HOLD` across files `04`, `15`; negative-stock behavior for Standard Cost and AVCO — only FIFO's negative-stock compensation mechanism is well-evidenced (file `07` §2.9, file `15` §4.3).

**Contradictions.** Price Difference Account scope is `CONFLICTING` across the version range — one source ties it to Standard Price only, another to FIFO/AVCO "cost adjustments" (file `02` §7, file `15` §6).

**What was tried.** Cross-checked the removal-strategy/costing-method independence claim against multiple version-pinned Removal Strategies pages; the independence finding itself is `PROVISIONAL`, corroborated by search-tool synthesis rather than a single verbatim sentence.

**Findings absorbed by the Owning Team.** Thailand's costing-method consistency rule (Revenue Code §65 bis (6)) is framed entirely at the whole-taxpayer-entity level in every primary source located — whether it could bind at product-category granularity is unconfirmed (new item `TH-HOLD-COGS-03`) and is a hard constraint on whatever precedence model SMEsPlus's Menu B/C track eventually proposes.

**Reusable reasoning pattern.** Never assume a UI-observed method taxonomy is the complete statutory taxonomy; test the reference-UI absence of a method (Specific Identification) against authoritative Thai/IAS-2 sources before concluding it is unneeded.

**Future trigger.** Re-check `TH-HOLD-COGS-03` before any SMEsPlus design finalizes category-level costing-method configurability.

---

## S3 — Product Category & Product Accounting Configuration

**Current understanding.** A three-level precedence chain (variant > product template > category, with a `PROVISIONAL` journal-level fourth fallback) governs Income/Expense Account resolution; Costing Method and Valuation Cadence are category-only (pre-19) or company-default-with-category-override (19.0, `PROVISIONAL`) with **no confirmed product-level override** for either — a material asymmetry against the Income/Expense precedence chain.

**Evidence.** Files `04`, `05`, `11` (the full 12-case precedence matrix), cross-checked against file `03`'s Menu A findings.

**Hypothesis.** A location-keyed third inheritance axis exists (file `10` §5.1, `C-H4`) for Inventory Loss/Production accounts specifically, not anticipated by the Menu B/C-only framing of the original precedence matrix scope.

**Unknowns.** Case 8 — whether the reference ERP re-classes accumulated Stock Valuation balance when a product's category changes with existing stock — is this file's single most material open item (file `11` §4), with no evidence either way.

**Contradictions.** None found within this team's own evidence; the Expense Account dual-account-type-by-mode finding (file `03` §2.5) is a control-risk finding, not an internal contradiction.

**What was tried.** File `11` was authored in parallel with, and without access to, files `04`/`05`'s exact wording, and independently re-derived the same general precedence mechanism — the convergence of two independently-sourced passes on the same three-level chain is corroborating evidence, disclosed explicitly (file `11` §0) rather than presented as if it were a single unified pass.

**Findings absorbed by the Owning Team.** File `11`'s Case 8 and file `10`'s `C-H4` (location as a third axis) must both be explicitly resolved or explicitly excluded — not silently omitted — before any Joint precedence design is finalized.

**Reusable reasoning pattern.** When two research passes converge independently on the same structural finding without having read each other's output, that convergence is itself evidence worth recording, not merely a coincidence to discard.

**Future trigger.** Re-verify Case 8 with a live-instance walkthrough before any migration design assumes category reassignment is a safe, no-op-for-existing-stock operation.

---

## S4 — Periodic Accounting

**Current understanding.** Periodic ties the *entire* financial lifecycle to two events only — vendor-bill posting (purchase side) and the stock-closing entry (everything else) — with physical receipt and delivery never individually generating a journal entry in any version reviewed.

**Evidence.** File `12` (full stage-by-stage model), file `08` (closing mechanism, including the explicit finding that no dedicated closing wizard exists), file `17` §4.2/§5.2 (purchase-side archetypes).

**Hypothesis.** The Periodic pattern has no confirmed dedicated "received, not billed" accrual visibility mechanism — the gap is only discovered once per period, at close, folded into the Variation Account (file `12` §6). This is a material asymmetry against the Perpetual pattern's named interim accounts.

**Unknowns.** Whether "received into stock" (the earliest-version conceptual framing) or "vendor bill posted" is the true documented Continental trigger — the two framings are not proven identical (file `14` §5.1); return handling before/after closing under Periodic specifically is `HOLD` (file `12` §5 row 8).

**Contradictions.** None internal to Periodic itself; the tension is with Perpetual's better-evidenced interim-account mechanism, not within Periodic's own documentation.

**What was tried.** Direct fetch of the version-19.0 Inventory Valuation page (succeeded) plus cross-checks against 17.0/18.0 Automatic Inventory Valuation pages for the pre-19 architecture; several Periodic-specific claims remain `PROVISIONAL` because the exact debit/credit account pairing for the vendor-bill-as-expense-by-nature posting was not independently confirmed against raw page markup.

**Findings absorbed by the Owning Team.** The "no dedicated closing wizard" finding (file `08` §1) must inform `JT-07`'s scope directly — Periodic's close is a configuration outcome (cadence + manual/scheduled trigger), not a discrete ceremony to design around.

**Reusable reasoning pattern.** Test a pattern's claimed simplicity ("no per-transaction posting") against what it does *not* tell you (no visibility into received-not-billed positions) rather than treating "simpler" as "safer."

**Future trigger.** Any future SMEsPlus design that adopts a Periodic-style default must independently design the received-not-billed/delivered-not-invoiced visibility the reference pattern itself lacks.

---

## S5 — Perpetual Accounting

**Current understanding.** Perpetual is not one pattern but at least two, sharing one policy name across the version history studied: pre-19 posts real-time at every physical stock movement with named interim (Stock Input/Output) accounts clearing move-by-move; 19.0+ posts at the invoice/bill level only, with Stock Input/Output retired in favor of a single Variation buffer plus explicit accrual entries, and the closing process demoted from primary mechanism (pre-19) to gap-filler (19.0+).

**Evidence.** File `13` (the full dual-regime model, the package's single richest evidence file on this point), file `18` (sales-side mirror), file `09` (vendor-bill/customer-invoice consumption), file `08` §2.5.

**Hypothesis.** The version-19 architecture change is vendor-acknowledged, not this research's inference — a "Discover why we changed" cross-reference was observed directly in the 19.0 cheat-sheet page (file `06` §3).

**Unknowns.** Partial receipt/delivery mechanics under either regime — inferred from the general stock-move-layer mechanic, never independently confirmed against a worked partial-quantity example (file `13` §7 row 5, file `18` §6.3).

**Contradictions.** The pre-19 "delivery vs invoice" COGS-trigger tension (file `13` §4.4) is the package's clearest internal-documentation contradiction; the 19.0+ regime removes it entirely by naming the invoice unambiguously.

**What was tried.** Direct verbatim quotation was prioritized over paraphrase wherever possible (e.g., "the expense account (COGS) is debited when invoices are posted") specifically to raise the pre-19 vs. 19.0+ contrast above a mere paraphrase-risk finding.

**Findings absorbed by the Owning Team.** The interim/Variation-account mechanism comparison (file `13` §6) is the direct evidentiary answer to "what control exists when physical and financial timing differ" — both regimes solve the same problem differently, and neither is adopted as SMEsPlus's mechanism by this file.

**Reusable reasoning pattern.** When a policy name persists across versions but its mechanism changes, treat the name as unsafe to cite without a version qualifier — this is the direct operational form of the governing prompt's version-delta hard rule.

**Future trigger.** Before any SMEsPlus design cites "Perpetual accounting behaves like X," require the citation to name which of the two regimes it means.

---

## S6 — Returns / Adjustment / Scrap / Landed Cost

**Current understanding.** The reference ERP structurally separates COGS from every non-sale inventory-value decrease it documents (adjustment gain/loss, scrap, and by extension write-down) via a location-type mechanism (Inventory Loss location + configured Loss Account), landing each in its own distinct P&L expense line — but this separation is **configuration-dependent**, not automatic, and no documented fallback exists for an unconfigured loss (file `20` §5).

**Evidence.** Files `19`, `20`, `21` — three files, each independently reaching the same structural conclusion the governing prompt asserts as its central COGS-classification principle.

**Hypothesis.** Returns are the package's single weakest-evidenced financial-recognition area: the reference ERP's own feature-level "how to click Return" documentation is completely silent on cost basis, and the valuation answer must be assembled from an entirely separate documentation surface that does not cross-reference it (file `19` §2) — a genuine, evidenced usability/documentation gap in the reference system itself.

**Unknowns.** FIFO's exact return-layer-consumption behavior is only community-corroborated, not primary-documented (file `19` §2, file `09` §7.3); the exact posting mechanism for a landed-cost residual on fully-sold stock is `CONFLICTING` across two secondary sources (auto-books-to-COGS vs. a 19.0+ manual-entry-via-clearing-account requirement, file `21` §3.3).

**Contradictions.** File `19` §4/§6 documents the reference ERP's own admission of a **discrepancy risk** between a credit note's financial-reversal amount and the inventory-valuation reversal's independently-computed amount — the reference system does not auto-reconcile this gap; its own documentation says "manual adjustment."

**What was tried.** File `21` explicitly built on, and did not contradict, the Inventory-side landed-cost rules (`LC-01`–`LC-07`) already fixed in the Inventory Final Solution v1.0 package, treating them as a constraint rather than re-deriving them from scratch.

**Findings absorbed by the Owning Team.** Scenario 11 (landed cost after full sale, file `16`) is the single most material item in the 32-scenario register precisely because it combines a version-behavior inconsistency, a reported case of a valuation change posting with no journal entry at all, and direct `JT-04`/`JT-08` exposure.

**Reusable reasoning pattern.** When a mechanism's classification behavior (loss ≠ COGS) is proven only under a specific configuration precondition, state the precondition explicitly — "COGS-safe by default" and "COGS-safe when configured" are different claims with very different risk profiles.

**Future trigger.** Any future scrap/loss/return design must re-verify that a fallback (unconfigured) path does not silently default to COGS.

---

## S7 — Manufacturing Cost

**Current understanding.** RM consumption and WIP completion are both asset-to-asset reclassifications, never COGS — corroborating evidence for the governing prompt's central boundary rule, applied to the manufacturing case specifically (file `22` §5). Two structurally different, version-separated WIP mechanisms exist: an always-on Production-location clearing account (documented through 18.0) and a distinct, manually-triggered, auto-reversing "Post WIP Accounting Entry" feature (19.0-only in evidence retrieved).

**Evidence.** File `22`, cross-referenced against file `10` §4 (Menu H's WIP account fields) and file `06` §2.6.

**Hypothesis.** Whether the two WIP mechanisms coexist or are mutually exclusive on the same manufacturing order was not found in any documentation page retrieved — a genuine, named gap, not an inferred negative.

**Unknowns.** Labor/overhead absorption variance treatment at completion; whether WIP posting/reversal mechanics branch by Periodic vs. Perpetual company mode.

**Contradictions.** None found between sources; the two WIP mechanisms are treated as a version delta, not a contradiction.

**What was tried.** Explicitly restated `GAP-FS-19` (whether Manufacturing is even in SMEsPlus v1.0 scope) verbatim at the top of file `22` before any archetype content, framing the entire file as evidence-in-reserve rather than a scope decision this session is authorized to make.

**Findings absorbed by the Owning Team.** No documented production/manufacturing standard-cost variance posting mechanism exists anywhere in the material reviewed — a sharp asymmetry against the well-evidenced Price Difference Account for *purchasing*. If SMEsPlus ever supports Standard Cost for manufacturing, there is no reference precedent to adapt; it would be original design work, not adaptation work.

**Reusable reasoning pattern.** An absence finding (no variance-posting mechanism found) is only trustworthy after searching the documentation trees a positive finding would have appeared in (here: the same Inventory Valuation / Manufacturing settings surface that does document WIP and Cost-of-Production accounts) — this file did that, and states the absence with the appropriate confidence level rather than either over- or under-claiming it.

**Future trigger.** Re-check whether a newer reference-ERP version introduces a manufacturing variance-posting feature before assuming the gap persists indefinitely.

---

## S8 — Thai Accounting / Tax / Audit Reality

**Current understanding.** Primary Thai statutory and standard-setter evidence is materially stronger than a documentation-only pass typically produces: the Revenue Code's cost-or-market rule and consistency requirement, the Revenue Department's scrap/destruction witness procedure, and the Federation of Accounting Professions' own TAS 2 explanatory manual (with worked NRV write-down/reversal examples and a literal COGS-matching recognition paragraph) were all directly opened and read, not merely searched.

**Evidence.** File `24`, the package's single deepest evidence file by primary-source density — 6 topics landed `AUTHORITATIVE / VERIFIED`.

**Hypothesis.** The Section 65 bis (6) consistency/change-of-method rule is framed at the whole-taxpayer level in every primary source found; whether it could bind at product-category granularity is unconfirmed and directly constrains the Menu B/C precedence work (`TH-HOLD-COGS-03`).

**Unknowns.** The statutory stock-report form's exact format/columns (`TH-HOLD-01`) remains `NOT FOUND / HOLD`; the "witnessed annual physical count" question narrows to two distinct, non-overlapping regimes (audit-observation under TSA 501, and destruction-witnessing under Order Por.79/2541) rather than one general rule, but neither regime independently establishes a standalone annual-count mandate (`TH-HOLD-07`, partially advanced).

**Contradictions.** None found within Thai primary sources themselves; the one discounted claim (a vendor-marketing blog's assertion that reference-ERP costing flexibility "supports" IAS 2 compliance) was explicitly identified as uncorroborated commentary and excluded from evidence, per the governing prompt's instruction not to treat commentary as authority.

**What was tried.** Direct PDF binary extraction via the Read tool where WebFetch could not parse compressed PDF streams — this succeeded for the operative Revenue Code register and the Por.79/2541 order, but the **gazetted TAS 2 standard text itself** (as opposed to TFAC's own explanatory manual) could not be extracted in the time available; the manual is classified `AUTHORITATIVE` because TFAC is the standard-setter and the manual is TFAC's own official publication, with the gap to the operative gazetted text disclosed honestly (file `24` §2.4 caveat) rather than smoothed over.

**Findings absorbed by the Owning Team.** Four new `TH-HOLD-COGS-*` items were opened (normal-vs-abnormal waste threshold; NRV testing granularity vs. category-level account design; the entity-vs-category consistency-rule scope; and an explicit flag that this file's DBD presentation finding must not be used to close the unrelated Account-module blocker `N-04`).

**Reusable reasoning pattern.** Classify every finding by evidentiary tier (`AUTHORITATIVE`/`INTERPRETATION`/`NOT FOUND`) at the point of writing, not retroactively — this discipline is what let file `24` distinguish six genuinely `AUTHORITATIVE` findings from four `INTERPRETATION` ones without either overclaiming or underclaiming.

**Future trigger.** Re-attempt extraction of the gazetted TAS 2 standard text (not the explanatory manual) before any downstream file cites a TAS 2 paragraph number as authoritative rather than as TFAC's own restatement of it.

---

## S9 — Migration / Replay / AI Control

**Current understanding.** Accounting-side duplicate-posting risk is **not** automatically solved by Inventory-side movement-fact idempotency (`C-02`/`IV-06`) — a cardinality mismatch exists because the Periodic model posts one aggregate closing entry per period covering many movement facts, so a fact-level guarantee does not propagate to a posting-level guarantee (file `26` §5.1).

**Evidence.** File `26` (the full accounting-side idempotency analysis, candidates `AC-01`–`AC-05`), cross-referenced against the Inventory package's still-unresolved `T-1` tension (mandatory-everywhere vs. blocking-only-for-automated-paths).

**Hypothesis.** `GAP-FS-08` (the migration provenance reference that does not yet exist) is the single blocking prerequisite for implementing any of the accounting-side candidates — they can be designed for, but not built, until it exists.

**Unknowns.** Whether the reference ERP's initial-stock quantity action also carries a value/cost input, and what account any resulting entry uses, is `HOLD` — the retrieved documentation page is quantity-only evidence (file `26` §2.2); whether any structural (system-enforced, as opposed to procedural) duplicate-import block exists for the opening-inventory-value posting is also `HOLD`.

**Contradictions.** None found; the community clearing-account pattern (file `26` §2.4) is explicitly labeled secondary, non-authoritative, and is preserved only as a problem-shape illustration per its own file's Clean-Room VETO pre-flag.

**What was tried.** This file explicitly stated a hard boundary rather than leaving it implicit: pre-cutover COGS is not re-derivable inside a new system from an opening balance alone — it is either a carried static comparative figure or absent, never recomputed — and ties this directly to the governing prompt's "no fabricated cost" rule.

**Findings absorbed by the Owning Team.** Regardless of how `T-1` is eventually ruled by Inventory/Joint, Accounting cannot outsource its own duplicate-posting risk to that ruling — the posting-level idempotency key (`AC-01`) is required either way, and becomes *more* load-bearing, not less, if `T-1` is ruled to bind only automated paths.

**Reusable reasoning pattern.** When one domain's control (Inventory's fact-level idempotency) is assumed to satisfy another domain's need (Accounting's posting-level duplicate-prevention), explicitly test the unit-of-guarantee match before assuming propagation — here the units differ (one fact vs. one aggregate posting) and the assumption would have been wrong.

**Future trigger.** Before any migration tooling is built, confirm `GAP-FS-08` has been closed by a joint Accounting × Inventory provenance design, not assumed solved by either side's existing controls alone.

---

## Cross-Team Convergence Note

Independently, S1, S4, S5, S6, and S9 all separately arrived at some form of the same conclusion: **the reference ERP does not supply one stable, adoptable pattern for any of the questions this session was commissioned to answer** — not for COGS timing, not for closing mechanics, not for return cost basis, not for migration safety. This is not five separate weak findings; it is one strong, repeatedly-independently-corroborated finding that `JT-01` through `JT-12` must be decided on SMEsPlus's own evidence and judgment, with the reference ERP serving only as a catalogue of possible mechanisms to weigh — never as a default to inherit.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
