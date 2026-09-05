# 69 — AAS-03 RUNTIME-INVERSION CHALLENGE

**LAYER 2 — AUDIT QUARANTINE.** Fresh challenge on material delta only.
Per `smeplus-adversarial-section-not-summary-rule`, **§7 is the citable output.**

Four mandated disproof attempts, each run to succeed.

---

## 1. Challenge classes

`A` evidence population · `B` denominator/counting method · `C` live-vs-latent
classification · `D` cost semantics.
Experts: `E1` Functional · `E2` Database · `E3` Integration/Localization · `E4` Code/UI.

## 2. MANDATED — disprove *"9,807 completed MOs have no conversion-cost activity"*

**`E2` attempts it and PARTIALLY SUCCEEDS.**

The claim is true as stated for `iSMEs`: 0 work centres, 0 routing operations, 0 work
orders, 0 time logs, `extra_cost` non-zero on 0 of 10,764. `_cal_price`'s conversion terms
are structurally zero. **Not disprovable for that database.**

**But the sentence invites a false generalisation.** `E2` shows that the same claim written
without its database name is **false for the product**: `iTEST02` has 60 work centres and
204 work orders. Round 3 wrote conclusions in that unqualified form.

**Result: the claim survives for `iSMEs`; the generalisation is DISPROVED.** `50` §1 now
states the bound in the first sentence.

## 3. MANDATED — disprove *"14/15 defects are latent"*

**`E3` attempts it and SUCCEEDS.**

Measured on four databases: **5 live, 7 latent, 2 unreachable, 1 unknown** (`53` §2).
`DC-06`, `DC-07`, `DC-09`, `DC-15` are **configured and reachable**; `DC-13` is
**observed**. Round 3's *"only `DC-13` is live"* held only while `iTEST02` was unread.

**Result: initially DISPROVED, then RE-ESTABLISHED.** `E3`'s disproof stood only until
`E4`'s challenge (§8) forced the posting gates to be measured. With them measured — periodic
valuation and no valuation layers in `iTEST02` — the live count returns to **1**.

**Round 3's claim survives.** This round's own draft, which briefly recorded 5 live, does
not. `53` §0, `RE-P03-19`. *A disproof that is itself later disproved is recorded in full
rather than deleted, because the intermediate state is what the register looked like when
the next challenge was run.*

## 4. MANDATED — disprove *"the principal live defect is zeroing"*

**`E1` attempts it and PARTIALLY SUCCEEDS.**

Zeroing is the principal live defect **in `iSMEs`**. It is not the principal defect overall:

- `iTEST02`'s principal live defect is **misdirection** — `DC-07`, 60 of 60 work centres.
- `iSMEs` carries a **larger** live defect than its zeroing: `55`'s **−48.7 % valuation
  distortion** and the subsidiary/GL divergence. That is an **explosion**, not a zeroing,
  and round 3 did not find it because it counted valuation rows without reading their values.

**Result: PARTIALLY DISPROVED.** `54` §1 now carries the two-sided verdict.

`E1` presses further — *"is zeroing even a defect, if material-only costing is deliberate
policy?"* **Refused as unanswerable on current evidence**: `52` §3 statement 4 records that
P03 has **no evidence of intent** and declines to infer it. The accounting consequence is a
statutory question already routed. `E1`'s point is preserved as the strongest argument
against the framing.

## 5. MANDATED — disprove *"no fixed-overhead path reaches inventory in the verified deployment"*

**`E4` attempts it and FAILS.**

`E4`'s strongest line: `iTEST02` installs `mrp_maintenance`, `hr_hourly_cost`,
`mrp_landed_costs`, `mrp_accountant` and `mrp_subcontracting` — precisely the modules a
reviewer would expect to supply overhead. If any did, the claim falls.

Checked: `mrp_maintenance` links equipment → work centre and carries **no cost**;
`hr_hourly_cost` prices **direct** time logs; `mrp_landed_costs` has **0 records** in both
databases; the analytic route **nets to zero by construction**.

**Result: NOT DISPROVED, and the claim is STRENGTHENED** — it now rests on a **complete**
installed-module population rather than an unknown one (`58` §2).

## 6. MANDATED — identify another headline/register count mismatch

**`E3` attempts it and SUCCEEDS — one found.**

`53` §2's first draft counted `DC-14` in two exposure classes and asserted a total of
`1+4+1+4+2+2+1` that does not equal 15. **Caught before publication** by the `60` control.
Recorded as `RE-P03-17`; it is the **fifth** instance of this class in the package and the
first caught mechanically rather than by a person.

`E3` also re-ran the nine other counts in `60` §3 and found **no further mismatch**.

## 7. Corrections carried forward — the citable output

| ID | Correction | Effect |
|---|---|---|
| `RC-01` | Round-3 conclusions were written **unqualified** where they held only for three databases | Every round-4 conclusion names its database — `50` §1, `63` |
| `RC-02` | *"14/15 latent"* is wrong in its **reachability** detail — 2 modules are installed after all — but **right in its live count**. This round's draft "5 live" was wrong; the figure is **1 live, 11 latent, 3 unreachable** | `53` §0, §2 |
| `RC-03` | *"principal live defect is zeroing"* is half the picture; **explosion is larger in amount** | `54`, `55` |
| `RC-04` | *"Material cost present"* was an **inference stated as a measurement**; 49 unvalued + 280 zero-valued | `51` §4, `RE-P03-16` |
| `RC-05` | *"containerised tooling unavailable"* was **never checked** and was false | `62` §6, `RE-P03-18` |
| `RC-06` | `53` §2 double-counted a defect | `RE-P03-17` |
| `RC-07` | Fixed-overhead negative **strengthened**, not weakened, by the fourth database | `58` |

**Seven corrections. Five are P03's own errors.**

## 8. What each expert says is still missing

| Expert | Missing |
|---|---|
| `E1` | **Intent.** Nothing establishes whether material-only costing was a decision or an omission, and the accounting consequence differs |
| `E2` | `iTEST02` has **no `stock_valuation_layer` table** — a different schema generation. No finding should cross the two without saying so (`UNR-P03-11`) |
| `E3` | The production-account balance in `iTEST02` was **not** decomposed (`UNR-P03-17`) — the one measurement that would test `DC-03`/`DC-04` directly |
| `E4` | **Answered during the challenge** — measuring it collapsed the draft's live count from 5 to 1 and resolved `DC-04` to UNREACHABLE. `E4`'s remaining point: the company-dependent **fallback** for the 3,977 categories with no explicit valuation was not read from `ir_default`; the conclusion rests on the absent valuation-layer table and the 32-line ledger instead. `UNR-P03-18` |
