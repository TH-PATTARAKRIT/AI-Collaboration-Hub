# 28 — 9 Veto Council Findings — COGS Deep Research

Session: `SMEPLUS-26-09-02-COGS-DR-001` | Jira: `ERPPLUS-142` | Control Level: `/L9999.9999`
Status: `CHALLENGE OUTPUT — NOT APPROVAL, NOT A GATE DECISION, NOT INDEPENDENT VERIFICATION`

---

## 0. Independence Disclosure — Read This First

Per the Inventory Final Solution v1.0 precedent (file `13` of that package) and per this program's carried `RISK-U07` charter conflict, this disclosure is repeated rather than assumed: **this is single-session synthesis.** All nine lanes below were run in sequence by the coordinating executor of this session, over material produced by fourteen delegated research passes operating under this executor's own brief and reviewed by this executor before publication (per `CV-06`, file `00`). They are structured self-review lenses, not independent parties. No lane was executed by a separate reviewer; no lane can verify this package from outside it.

A lane that says "accepted, no material objection" means *this executor, wearing that lens, found no objection* — not that the research has been externally validated. The lanes share a blind spot common to all of them: none has field access to a live instance of the reference ERP (this was a documentation-only research pass, per governing prompt §3's Layer A boundary), and several material findings rest on secondary/community corroboration rather than a single verbatim primary-page quote (flagged `PROVISIONAL` throughout files `02`–`27`).

No lane below approves anything. No lane grants Team B, Team C, Development, Production, or Release authorization. No lane declares `PASS`. This file's evaluation standard is itself subject to the unresolved `RISK-U07` charter ruling carried from the Inventory package.

---

## 1. Nine Veto Lanes

### V-1 — Audit VETO
*Lens: is every assertion traceable to evidence, and is every gap visible?*

| Verdict | Item |
|---|---|
| **Accepts** | Every one of files `02`–`27` uses the mandatory `Reference ERP official documentation — <topic>, version <N>, retrieved 2026-09-02` citation form (`CV-02`); every material cell carries a Fact Status (`VERIFIED`/`PROVISIONAL`/`CONFLICTING`/`HOLD`); an independent mechanical clean-room scan of all 26 files found zero vendor-name leaks, zero forbidden code tokens, and zero fenced code blocks (verified directly by this executor, not only self-reported by the delegated passes). |
| **Accepts** | Version-drift risk — the single most dangerous failure mode this session was warned against (§5 of the governing prompt) — is not merely acknowledged but *actively evidenced*: the pre-19/19.0+ Perpetual-trigger instability is independently corroborated across at least seven separate research passes (files `02`, `06`, `09`, `12`, `13`, `14`, `16`, `18`), each arriving at it from a different documentation surface, which is the strongest possible evidentiary posture a single-session package can produce for a claim this material. |
| **Rejects** | Nothing in what is written. |
| **HOLD** | A meaningful fraction of the `19.0`-specific evidence throughout files `02`–`10` rests on search-index reconstruction rather than a successful direct page fetch (two direct-fetch attempts on the primary `19.0` Accounting settings page failed with empty-content errors — file `03` §3). This is disclosed honestly everywhere it occurs, but it means a materially large slice of this package's most-current-version evidence is `PROVISIONAL, HIGH CONFIDENCE` rather than `VERIFIED`, and a dedicated re-fetch pass is a real prerequisite before any of it is treated as settled. |
| **To Boss** | Whether an independent re-audit of *this* package is required before any downstream use — this executor cannot self-certify, and the volume of cross-corroborated `PROVISIONAL` findings in this package is high enough that a second independent read would materially de-risk any future Joint session that leans on it. |

### V-2 — TBRAC VETO
*Lens: Thai business reality — would a real Thai SME recognise this as their business?*

| Verdict | Item |
|---|---|
| **Accepts** | File `24`'s Thai evidence pass materially exceeds this lane's expectation for a single-session documentation pass: it obtained and directly read primary Revenue Department text (Revenue Code §65 bis (6), Order Por.79/2541, Practice Guideline Mor Kor 4/2546, delegation Order Tor.228/2552) and the Federation of Accounting Professions' own TAS 2 explanatory manual with worked NRV write-down/reversal examples — six topics landed `AUTHORITATIVE / VERIFIED`, not merely `INTERPRETATION`. |
| **Rejects** | Any reading of the reference-ERP evidence (files `02`–`23`, `25`–`27`) as describing how a Thai SME accountant actually works. Every Layer A finding in this package describes one benchmark system's documented behavior; none of it has been shown to a Thai accountant, bookkeeper, or SME owner. The Thai-fit rows in file `14`'s comparison matrix (Periodic vs Perpetual, row 13) are explicitly marked `HOLD / EVIDENCE REQUIRED` for exactly this reason and this lane insists that HOLD be preserved, not quietly narrowed by the strength of file `24`'s statutory findings — statutory compliance and operational fit are different questions. |
| **HOLD** | Whether a Thai SME accountant, in practice, actually operates closer to the "Continental/Periodic" pattern (monthly manual closing, physical count driven) or the "Anglo-Saxon/Perpetual" pattern is not answered anywhere in this package — file `24` supplies the statutory floor (cost-or-market, consistency rule, worked NRV examples), not the operational-workflow answer this lane needs. |
| **To Boss** | Commission a small Thai-accountant validation pass (three to five practicing SME bookkeepers/accountants) specifically on the Periodic-vs-Perpetual operational-fit question once `JT-03` is otherwise ready to convene — this lane's position, consistent with the Inventory package's own S-2 counter-lane, is that a lightweight validation is proportionate here, not a formal panel that would stall the programme. |

### V-3 — IBPV VETO
*Lens: business-process validity — does the cost lifecycle hold together end to end?*

| Verdict | Item |
|---|---|
| **Accepts** | The full Periodic (file `12`) and Perpetual (file `13`, both regimes) end-to-end lifecycles are each internally coherent and answer every one of the governing prompt's §8.1/§8.2 research questions explicitly, with no blank cells — every unresolved point carries a named `HOLD`/`PROVISIONAL` status and a routing target rather than a guessed answer. |
| **Accepts** | The 32-scenario register (file `16`) genuinely runs every mandatory scenario through both accounting patterns and produces a "why this is/isn't COGS" note for each — this is real depth, not a checklist gesture; ten of the 32 scenarios reach a clean, low-ambiguity Layer A finding in both modes, which gives the process model a solid, evidenced core even where the edges remain open. |
| **Rejects** | Any reading of the Periodic model's "COGS as a derived period residual" finding (file `12` §4.9, file `27` §5.2) as a settled formula. File `27` proves directly that the naive `Opening + Purchases − Closing = COGS` identity silently absorbs scrap/shrinkage/write-down unless those are separately measured and subtracted first — this is not a minor caveat, it is a live risk of overstating COGS and understating a distinct loss line, and this lane rejects any process description that omits the correction. |
| **HOLD** | The bill-before-receipt sub-case under Perpetual (file `17` §7, §10 item 1) is flagged by its own author as the weakest-evidenced timing sub-case in the entire purchase-side chain — inferred by structural symmetry only, never independently confirmed. This lane holds it as a genuine process-completeness gap, not a resolved edge case. |
| **To Boss** | Nothing new beyond what is already registered in file `30`. |

### V-4 — IDTM VETO
*Lens: data truth and identity — will the numbers be provable?*

| Verdict | Item |
|---|---|
| **Accepts** | File `27`'s reconciliation-identity register is the correct discipline: five identities tested, none declared unconditionally `VERIFIED` except Identity 3 (Cost Release → COGS or another explicitly approved classification), which is verified only as a **governing constraint**, explicitly not as evidence any classification rule set yet satisfies it. This is honest, provable-numbers thinking, not a false sense of completeness. |
| **Rejects** | Any assumption that the reference ERP's own account balances are self-reconciling. File `27` §6.2 shows the reference system's own closing-entry mechanism exists *because* the Inventory-subledger-to-General-Ledger identity is expected to diverge between closings, not because it never diverges — a design that assumed continuous reconciliation would be building on a premise the reference system's own evidence contradicts. |
| **Rejects** | Treating Case 8 of file `11` (product changes category with existing stock) as a low-materiality configuration event. This lane calls it what file `11` itself calls it — the single most material unresolved item in that file — because no evidence was found either confirming or ruling out that the reference ERP automatically re-classes accumulated Stock Valuation balance on category reassignment. If it does not, every historical migration and every live reassignment risks stranding un-reconciled inventory value, a direct threat to the Cross-System Reconciliation identity. |
| **HOLD** | The FIFO customer-return layer-consumption discrepancy (file `19` §2, corroborated by file `09` §7.3) — a returned unit valued at the *current* costing layer rather than its *original* issue cost, producing a residual, unexplained balance in the interim/clearing account — is exactly the kind of un-provable-number risk this lane exists to flag. It directly feeds `JT-05`/`C-03` and is not resolved by this package. |
| **To Boss** | Whether Case 8 (file `11`) and the FIFO return-layer discrepancy (file `19`) should be escalated to a targeted, non-documentation-only verification pass (a live reference-instance walkthrough) before the Joint Cross-Proof session, given that documentation-only research could not resolve either. |

### V-5 — IESA VETO
*Lens: enterprise and multi-tenant architecture soundness.*

| Verdict | Item |
|---|---|
| **Accepts** | File `25`'s narrow, honest scoping: it explicitly declines to re-derive or resolve the Inventory-side multi-tenant invariant set (`RISK-U03`/`GAP-FS-10`, already Boss-blocking per the Inventory package) and instead adds a genuinely new, narrower Accounting-side observation rather than duplicating or silently assuming that gap is closed. |
| **Rejects** | Nothing in what is written. |
| **HOLD** | File `25`'s central finding is exactly this lane's central concern: whether Product Category (the policy-carrying record for Costing Method and Stock Input/Output/Valuation accounts) is company-scoped by default could **not** be confirmed against official documentation — only secondary/non-official sources address it (file `25` §2.4). The confirmed analogous case (Product Cost, which is explicitly company-specific even on an otherwise-shared product record, file `25` §2.3) shows the reference ERP is capable of exactly this kind of narrow per-company carve-out, but does not prove it exists for the category-level policy fields. |
| **HOLD** | This is the sharpest cross-cutting architectural finding in the whole package: **a completed Inventory-side multi-tenant invariant set (`RISK-U03`/`GAP-FS-10`) would not, by itself, guarantee costing-policy isolation across companies** — two companies in one deployment could silently inherit the same costing method through a shared category even while their inter-company transfer legs are correctly modeled as two independent facts (file `25` §5, §6). |
| **To Boss** | `RISK-U03`/`GAP-FS-10`'s eventual resolution must explicitly cover the Accounting-side policy-sharing question this file surfaces, not only the Inventory-side fact/movement-scoping question it already names. This is new scope for that existing gap, not a new gap. |

### V-6 — Financial / Accounting Interface VETO
*Lens: will the accountant be able to close the books, and is COGS trustworthy?*

| Verdict | Item |
|---|---|
| **Accepts** | The foundational rule ("Inventory emits facts; Accounting decides postings") is held without exception across all 26 research files — nowhere does any file have Inventory select an account or decide recognition timing, and the boundary is actively used as an analytical tool (e.g., file `20`'s master decision table, file `22`'s RM→WIP→FG chain) rather than merely recited. |
| **Accepts** | The Thai-evidence pass (file `24`) independently arrived at, and directly quotes, the exact same principle the governing prompt exists to prove: TAS 2's own recognition-as-expense section distinguishes ordinary cost-of-sales recognition on sale, write-down/loss recognition in the period incurred, reversal as a COGS reduction, and re-allocation to another asset class as depreciation over that asset's life — four textually distinct recognition events, not one undifferentiated "inventory decrease." This is now `AUTHORITATIVE`, not merely a design preference. |
| **Rejects** | Any suggestion that "COGS recognition timing" (`JT-04`) is close to resolvable. The single most repeated, most heavily cross-corroborated finding across this entire package (at least seven files) is that the reference ERP's own documentation is internally unstable on this exact question across its own major versions — pre-19 ties the P&L expense debit to the customer invoice event with the inventory-asset side already moved at delivery (itself only `PROVISIONAL` in its precise timing); 19.0+ ties the *entire* value-affecting event, both asset and expense, unambiguously to the invoice/bill. This is not a detail Joint can paper over by picking "the reference behavior" — there is no single reference behavior to pick. |
| **HOLD** | The Menu B/C "dual account-type-by-mode" finding (file `03` §2.5, file `04` field `B-04`) — the same "Expense Account" field expected to hold a Current-Asset-type account under Periodic and an Expense/Cost-of-Revenue-type account under Perpetual — is a concrete, evidence-backed control risk: a configuration built for one mode and carried into the other misclassifies the account on the financial statements. No SMEsPlus mitigation is proposed by this package; it is flagged, not designed. |
| **HOLD** | No dedicated "close the stock period" wizard exists in the reference ERP at all (file `08` §1) — closing is a cadence-driven journal-generation configuration (Manual/Daily/Monthly), not a formal ceremony, and it remains materially ambiguous whether the documented "Option 1/Option 2" closing mechanisms describe routine recurring closing, a one-time Periodic-to-Perpetual migration procedure, or both (file `08` §2.3). This must be resolved before `JT-07` (period close design) can be scoped correctly. |
| **To Boss** | Convene the Joint Accounting ↔ Inventory session on `JT-04` with this package's evidence in hand, but be told plainly: the reference ERP cannot supply a single "how it's normally done" answer to lean on. `JT-04` will have to be decided on SMEsPlus's own evidence (Thai matching-principle requirement, per file `24` §2.4) and business judgment, not by adopting either reference regime wholesale. |

### V-7 — Security / Privacy / Resilience VETO
*Lens: can this be abused, and does it fail safely?*

| Verdict | Item |
|---|---|
| **Accepts** | The Lock Date / Hard Lock mechanism documented in file `08` §2.6 and file `23` §2.6 (named grantor, written reason, expiry, permanent audit-chatter log for the soft exception; a genuinely irreversible Hard Lock for statutory inalterability) is structurally consistent with, and corroborates rather than contradicts, the Inventory-side period guard already fixed in the Inventory Final Solution v1.0 package. |
| **Rejects** | The reference ERP's "everyone" exception scope for the soft lock (file `08` §2.6, file `23` §2.6) as something SMEsPlus should adopt — this session's own evidence-gathering files already flag it as structurally close to the global-bypass toggle the Inventory-side design explicitly rejected as unauditable, and file `23`'s candidate `L23-C03` correctly declines to carry it forward. |
| **HOLD** | No mechanism was found anywhere in this package's evidence for attributing a late-arriving supplier cost back to the *specific prior period* it should have affected — a late cost is simply absorbed into the current period's Variation account at the next close (file `08` §2.7). This is a genuine control gap in the reference system itself, directly material to `JT-06`, and this package does not resolve it. |
| **HOLD** | File `20` §5 flags that the reference ERP's "loss is not COGS" separation is *configuration-dependent* — a distinct Inventory Loss location/account must be deliberately set up — and no documented fallback account was found for an unconfigured loss. "Scrap defaults to non-COGS" is therefore not a safe unconditional assumption; without deliberate configuration, a scrap or shrinkage event could silently inflate the COGS figure exactly as file `27` §5.2 warns against for the naive Periodic formula. |
| **To Boss** | Nothing new beyond registration in file `30`; both items above are control gaps in the *reference* system, evidenced honestly rather than assumed benign, and must inform (not be inherited by) whatever SMEsPlus's own late-cost and loss-classification controls become. |

### V-8 — Clean-Room / IP / Provenance VETO
*Lens: is this package genuinely SMEsPlus-owned, and is the clean-room boundary honestly held?*

| Verdict | Item |
|---|---|
| **Accepts** | This executor's own independent mechanical scan (not merely the delegated passes' self-reports) across all 26 files found zero occurrences of the vendor/product name, zero forbidden code tokens (`stock.*`, `product.*`, `ir.*`, `quant`, `orderpoint`, `picking(-type)`, `_action_*`, `sudo(`, `.py`), and zero fenced code blocks. Two self-caught leaks (an accidental vendor-name mention inside a quoted forum-thread title in files `21`/`22`, and one inside file `13`'s own citation table) were found and scrubbed by the authoring passes themselves before this executor's independent check — evidence the discipline was applied during authoring, not only at final review. |
| **Accepts** | The `CV-02` citation convention (topic+version, no raw vendor-domain URL) is applied with complete consistency across all 26 files — a deliberate, disclosed resolution of the tension between the governing prompt's URL-citation ask and this program's established never-name-the-vendor discipline, stated openly in file `00` rather than silently deviated from. |
| **Rejects** | Nothing found requiring rejection. |
| **HOLD** | This package is explicitly Layer 2 controlled evidence (`CV-04`), not Layer 1 clean-room design — every Layer A section in every file names reference-ERP account labels, field names, and mechanisms in detail, which is appropriate for a Layer 2 evidence package but means this package **must not** be cited directly by any future Layer 1 SMEsPlus design document without first passing through the same neutral-business-meaning transformation the Inventory Final Solution v1.0 package applied to its own Layer 2 predecessor (`INVENTORY_MENU_DEEP_CHALLENGE`). This lane flags that transformation step as still-required, not yet performed. |
| **To Boss** | Confirm this package's Layer-2 status explicitly at gate review, and confirm that a future "COGS Final Solution" session (analogous to `INVENTORY_FINAL_SOLUTION_V1`) is the intended vehicle for producing the Layer 1 candidate design — consistent with `CV-04`. |

### V-9 — AI Control / Automation VETO
*Lens: is automation bounded, explainable, and free of fabrication?*

| Verdict | Item |
|---|---|
| **Accepts** | No journal entry, account code, or cost figure was fabricated anywhere in this package. Every numeric worked example that appears (e.g., file `21`'s $100/$10 price-difference illustration, file `04`'s "25 vs 26" receipt/bill variance example) is explicitly attributed to the cited source as that source's own illustrative figure, never asserted as an SMEsPlus candidate value — this is checked directly by this executor, not only self-reported. |
| **Accepts** | Every file terminates with an explicit non-closure statement for the Joint decisions it touches (e.g., file `13` §9, file `27` §9, file `15` §9), and no file anywhere declares `PASS`, `FINAL`, `APPROVED`, or grants any team/build/release authorization — independently confirmed by this executor's own targeted grep pass (file `28` §0 disclosure notwithstanding — see the checkpoint log's clean-room verification record). |
| **Rejects** | Any automation path that would let this package's `CANDIDATE` or `HOLD` markings silently harden into a decision through repeated citation. This lane records the boundary explicitly so a later session cannot quietly treat "cited five times" as equivalent to "resolved." |
| **HOLD** | The migration/idempotency candidates `AC-01`–`AC-05` (file `26` §5.2) are explicitly and correctly scoped as candidate requirements only, silent on trigger mechanism (human-run, scheduled, or AI-assisted) — this lane accepts that framing and notes it is the correct posture: whatever eventually triggers a migration/opening posting, the posting-level idempotency key and reversal-only correction rule must apply uniformly, with no automated or AI-assisted path held to a weaker duplicate-posting standard than a human-run one (file `26` §10, explicitly pre-flagged for this file). |
| **To Boss** | Nothing new; the AI-assisted-path-parity principle in file `26` §10 is affirmed here as the standing rule for any future COGS-related automation design. |

---

## 2. Cross-Lane Tensions Worth Boss's Attention

| # | Tension | Lanes |
|---|---|---|
| `T-COGS-1` | Is the version-19+ reconstruction (search-index only, direct fetch failed) reliable enough to inform `JT-04` now, or must a direct re-fetch happen first? | V-1 vs. V-6 — V-1 flags the evidentiary weakness; V-6 needs the evidence to convene Joint on `JT-04` regardless |
| `T-COGS-2` | Does Case 8 (category reassignment with existing stock, file `11`) and the FIFO-return discrepancy (file `19`) require a live reference-instance walkthrough (documentation-only research cannot resolve either), or is Boss/Joint willing to proceed on the corrected-formula candidate in file `27` §5.2 without it? | V-4 — a genuine, decidable question for Boss |
| `T-COGS-3` | Should `RISK-U03`/`GAP-FS-10` (Inventory-side multi-tenant invariant set) be re-scoped now to explicitly include the Accounting-side policy-sharing question file `25` surfaces, or should that wait for the invariant set's own dedicated session? | V-5 |
| `T-COGS-4` | Is a lightweight Thai-accountant validation (three to five practitioners) on Periodic-vs-Perpetual operational fit proportionate now, or should it wait until after `JT-03` narrows the field? | V-2 — mirrors the Inventory package's own unresolved `T-3` tension |

---

## 3. Challenge Roll-Up

| | Lanes | Accepted with no material objection | Raised at least one rejection | Raised at least one HOLD | Escalated to Boss |
|---|---:|---:|---:|---:|---:|
| Veto Council | 9 | 1 (V-9 rejects one thing but accepts most; counted by dominant posture — see note) | 5 | 9 | 6 |

Note: every lane accepted at least one item and raised at least one HOLD; "accepted with no material objection" above counts only lanes with zero rejections (V-5, V-8, and V-9 in substance — V-9's "rejects" row is a boundary statement, not a finding against this package's own content).

---

## 4. What This Challenge Layer Concludes

This package is **sufficient as a Boss-facing research evidence record and insufficient as a Final Solution basis** — exactly the posture the governing prompt requires (§21). The single most material, most heavily cross-corroborated finding is that the reference ERP's own "Perpetual" accounting pattern is not one stable benchmark across its version history, which means `JT-03` and `JT-04` cannot be resolved by adopting reference behavior wholesale and must be decided on SMEsPlus's own evidence — a conclusion this package supports with unusual strength precisely because it could not find a single stable answer to hand Joint. The second most material finding is that the Thai statutory evidence base (file `24`) is stronger than a documentation-only session typically produces, and materially advances four of the nine pre-existing `TH-HOLD-*` items with primary-source citations.

No lane approves. No lane declares `PASS`. No lane authorizes any team, any merge, any release, or any implementation. Boss remains the sole Final Approver.

No Evidence = No Progress. Never Skip Gate. Boss = Sole Final Approver.
