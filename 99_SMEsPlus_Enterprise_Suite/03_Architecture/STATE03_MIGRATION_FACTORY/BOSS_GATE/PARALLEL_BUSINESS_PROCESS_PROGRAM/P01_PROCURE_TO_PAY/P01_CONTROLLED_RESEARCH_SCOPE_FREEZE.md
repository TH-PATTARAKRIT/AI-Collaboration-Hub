# P01 — CONTROLLED RESEARCH SCOPE FREEZE

Session: `SMEPLUS-26-09-05-G01-P01-P2P-CONTROLLED-SCOPE-FREEZE-HANDOFF-001`
Group **G01 — Supply / Cost / Payable** · Branch `research/account-p01-procure-to-pay-2026-09-04-001`
Baseline `a02ec8b6628daf145c03fa49397448a7f29605ea`

---

## 1. WHAT IS AND IS NOT BEING FROZEN

**This freezes the CURRENT RESEARCH SCOPE against CURRENT EVIDENCE.** It means:

- **no new broad source / database / estate sweep from P01 without Material Delta**;
- current evidence **and its limitations** are preserved;
- unresolved cross-process matters remain **OPEN** and are **routed to named owners**;
- **Boss may reopen P01** at any time on Material Delta.

**It is explicitly NOT:** a Final Freeze · a whole-domain or canonical freeze · PASS · merge authority ·
design approval · authorisation to implement anything.

**Nothing was deleted.** Every superseded statement remains in place with its correction beside it.

---

## 2. WHY STOPPING BROAD RESEARCH IS DEFENSIBLE NOW

| Question | Position |
|---|---|
| Has the estate's most material deployment been read? | **Yes** — `45a8e08e`, the only one with substantial accounting history (183,590 entries), read this round |
| Do source and deployment overlap same-generation? | **Yes**, on series **16, 18 and 19**. The two published claims that they did not are corrected (`ERR-P01-23`, `ERR-P01-41`) |
| Is the mechanism P01 described actually observable? | **Yes** — 57,863 of 74,982 layers link in series 16. The programme's first positive control |
| Are remaining questions answerable by more P01 sweeping? | **Mostly no.** They need runtime authorisation, statutory authority, another process's model, or a targeted test in a *named* deployment |
| Would another broad sweep be cheap? | **No** — and the last one, correctly classified `OVERBROAD_SCAN`, ran 9h18m at a 0.048% duty cycle |

**The strongest argument against freezing is stated, not hidden:** `GAP-P01-07` — **41 of 651 tables (6.3%)
were extracted with no declared selection rule.** That is a real bound on every negative in round 6, and it is
carried as an open dependency rather than resolved by assertion. **A targeted challenge was assigned to
attack this freeze directly**; its result is in `P01_G01_CLOSURE_AAS03_CHALLENGE.md`.

---

## 3. THE RESEARCH RECORD, HONESTLY STATED

Six rounds. **The last one corrected seven of its own published statements** — six found by challengers, none
by the author after publication — including a headline that **inverted in sign**.

| Round | Self-caught before publication | Corrected by challenge after |
|---|---|---|
| 6 (series-16) | 5 | **7** |

**Every one of the seven was a boundary defect: a state basis, a population, a unit, a predicate. None was a
reasoning error.** That is the settled pattern of this programme across ~25 recorded corrections, and it is
not improving. It is the single most useful thing P01 hands downstream.

---

## 4. THE METHOD CONTROLS EARNED, FOR DOWNSTREAM USE

1. **Every aggregate over journal items declares its state basis in the same line as the number.**
   Posted-only is the default. P01 published ฿72,097,814.25 where the posted figure is −฿7,048,692.08.
2. **Choose a claim's population from the claim's own subject, never from the side you already searched.**
   *"The GL is intact"* was tested on 25 entries reachable from 30 subledger rows; from the ledger it is false.
3. **Identify deployed custom code by the field set its model declares in the deployment's `ir_model_fields`
   registry** (`METHOD-P01-03`) — four `_cert` variants share one version string here.
4. **An installed module that modifies a writer's INPUT changes behaviour without being a writer**
   (`purchase_mrp`). Enumerating writers is correct and not sufficient.
5. **Assert every join key exists in the generation under study** — a padding parser will let you join on an
   absent column and return a plausible, inverted answer (`ERR-P01-42`).
6. **A negative about a stored setting cannot be tested by querying only the rows that still exist** — a
   reverted `ir_property` leaves none.
7. **A correction is not immune to the defect it corrects** (`ERR-P01-43`).

---

## 5. FREEZE CONDITIONS

**In force from this commit.** P01 will not open a new broad sweep. P01 will still:
- answer targeted questions from P03, P05, P06, P07, P08 or P11 against **already-extracted** evidence;
- execute `S16-B-02` (advance lineage), which needs **no new evidence**;
- act immediately on any Material-Delta trigger in `P01_FINAL_OPEN_DEPENDENCY_REGISTER.md`.

**P01 has not started, and will not start, P03, P08 or P11 work. No merge to `SMEsPlus` has occurred.**
