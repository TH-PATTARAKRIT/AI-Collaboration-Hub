# G01-P01 — AAS+ CONSOLIDATION AND PMO CLOSURE ASSESSMENT

Session: `SMEPLUS-26-09-05-G01-P01-P2P-CONTROLLED-SCOPE-FREEZE-HANDOFF-001` · Checkpoint `CP-07`

---

## PART A — AAS+ CONSOLIDATION

### A.1 What the four targeted challenges did to the closure package

| | Outcome |
|---|---|
| Findings **overturned** | **0 of the six rounds' findings.** **2 sentences written in this closure run** — the P03 handoff's central claim (`ERR-P01-48`) and the P08/P11 price-difference statement (`ERR-P01-49`) |
| Claims **corrected** | **6** — the C-5 reading of the 144; the period-lock phrasing; the P03 kit mechanism (a docstring reported as behaviour); "LATENT here"; "capitalised into inventory"; "no P&L variance line" |
| Claims **strengthened by enumeration** | 1 — no lock date is set anywhere, now proven across all three surfaces |
| Claims **narrowed** | 1 — the `_get_price_unit` firing set is **18** lines with `qty_received = 0.000000`, not 49 |
| **Material Delta discovered** | **Yes — inside already-extracted evidence** |

### A.2 The consolidated position

**The freeze is challenged on completeness, not on correctness.** Both experts who examined it agree no
**broad** estate sweep is justified — the direction of C-1 is right. What they establish is that a **narrow,
named, cheap** continuation would close questions this package left open, using tables already on disk.

Three items make that unavoidable:

1. **฿1,742,591,244.82 of manual reclassification is the largest single component of P01's own headline
   account, and six rounds never mentioned it.** Its operator-written reason text is the account-mapping
   history that `ir_property` provably cannot show.
2. **`mail_tracking_value`, 571,522 rows, has never been opened** — and three surviving conclusions
   (*immutable reversal*, *no lock*, *posted after the rate was zeroed*) are claims about what happened to
   records **over time**, resting on the one artefact that records exactly that.
3. **Scrap and inventory adjustments post into the purchase clearing account**, and there is **no
   inventory-loss account** — scrap is indistinguishable from consumption in the P&L.

### A.3 Dissent and unresolved matters preserved

- Experts 3 and 4 **did not return before closure** and are **dispositioned OPEN, not assumed**. Their two
  target sentences remain marked under challenge.
- The Buddhist-era extent disagreement (484 values / 14 columns / 11 tables vs 12 pairs / 7 tables) is
  **carried, not averaged**.
- The certificate/payment denominators (1,407 vs 1,405; 1,543 vs 1,488) are **carried**.
- The P05 vendor-advance disagreement is **preserved** — though Expert 1 has now measured the exposure as
  **immaterial** here (9 payments, −฿1,534,955.07), which narrows it without resolving P05's position.

### A.4 AAS+ position

> **RECOMMEND HOLD, and RECOMMEND the narrow continuation `S16-B-06` before any downstream process relies on
> the GRNI decomposition.**

**AAS+ does not veto.** Nothing published is unsafe to hold; the handoffs are bounded and their limits stated.
**AAS+ does not decide** whether the reclassifications are correct, whether scrap should have its own account,
or whether capitalising price variance is right — those are P08, P03 and Boss matters.

---

## PART B — PMO CLOSURE ASSESSMENT

PMO answers only the five questions it was given.

### B.1 Is currently obtainable P01 work exhausted?

> **NO.**

Four items are executable **with no new extraction**: read the 28 reclassification entries; run the origin
decomposition across the remaining 261 accounts; establish the non-PO bill path and the 298 lines that reach
GRNI; explain the 190 return moves with no valuation layer and the 182 GRNI items whose layer points at a
non-`done` move. Two more need only a single table each: `mail_tracking_value`, `ir_model_data`.

**PMO records this as the round's honest finding and declines to report the status as improved because more
files were written.**

### B.2 Are all remaining dependencies named and owned?

> **YES.** `P01_FINAL_OPEN_DEPENDENCY_REGISTER.md` carries every item with an owner and an exact next action,
> including the new `S16-B-06`. No item is parked without one.

### B.3 Is any load-bearing background task still running?

> **NO. All four closure challenges returned and were adopted before publication.**
>
> Two of them **broke sentences written earlier in this same run** — the P03 kit mechanism (`ERR-P01-48`) and
> the P08/P11 price-difference statement (`ERR-P01-49`). **Both handoffs were rewritten before commit; no peer
> received the wrong version.**

### B.4 Is any required evidence local-only or unpublished?

> **PARTIALLY, and it is declared.** All extracts live under the session scratchpad and are **not** committed
> — they are reproducible from the named archive by the documented command. The **archives themselves are
> local-only** (`~/Downloads/iSMEs_…`, `~/OCC_BACKUP/idemo18_uat_…`) and are named, hashed by content only in
> the sense of `database.uuid`, and not published. **No conclusion in the package depends on an artefact that
> is not named with a locator.**

### B.5 Is a new BROAD P01 sweep justified by Material Delta?

> **NO — and the research scope is frozen accordingly.**

Both examining experts agree. The last broad sweep was correctly classified `OVERBROAD_SCAN` (9h18m at a
0.048% duty cycle). **Material Delta exists, but it is entirely inside evidence already extracted**, which is
a narrow continuation, not a sweep.

### B.6 PMO position

> **RECOMMEND HOLD.** Research scope frozen for **broad** research. **Currently obtainable P01 work is NOT
> exhausted**, and the narrow continuation is registered as `S16-B-06`, owned by **P01**, with an exact next
> action.

**PMO notes for the record:** this closure run corrected **six** of its own claims within hours of writing
them, including **the central sentence of two separate cross-process handoffs** — one that described a
docstring rather than the code beneath it, and one that was **false in both halves and directionally wrong**.

**That is the control working.** It is also the **seventh consecutive round** in which the authoring half
published something a challenger had to take back, and the second in two rounds to **repeat a defect the
programme had already withdrawn** — a current-state census that cannot see a reverted row. **PMO records that
the corrections are being found, and that the same class of defect is not being prevented.**
