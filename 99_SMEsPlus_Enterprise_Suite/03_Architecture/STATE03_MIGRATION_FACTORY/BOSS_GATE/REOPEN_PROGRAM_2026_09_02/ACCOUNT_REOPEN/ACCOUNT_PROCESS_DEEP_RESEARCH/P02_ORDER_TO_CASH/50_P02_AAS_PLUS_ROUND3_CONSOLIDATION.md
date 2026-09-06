# 50 — P02 AAS+ ROUND-3 CONSOLIDATION

`LAYER 2 — AUDIT QUARANTINE.` **CP-08.** Prompt §13. Baseline `aca211e`.

**Dissent is preserved. No consensus is invented.**

---

## 1. Agreements

| # | Agreed | Held by |
|---|---|---|
| A-1 | **The identity model's six-level distinction is sound; its KEY was wrong twice.** The levels survived attack; both candidate keys failed. | 1, 2, 3, 4 |
| A-2 | **The substantive accounting findings survived every challenge.** Zero `cogs`, 47,801 layers with no accounting entry, the delivered-not-invoiced measure — all reproduced on independent instruments. | 1, 2, 4 |
| A-3 | **The package's published counts were unreliable in this round** — lineages, snapshots, artefacts, coverage and reachability were each wrong. | 1, 2, 4 |
| A-4 | **A correction written in prose does not reach a status field or an owning register.** Found in `46`'s status column and in `13`, which had never received the `RE-30` banner. | 3, 4 |
| A-5 | **Scope-awareness is under-modelled.** COMPANY was absent from the identity model, and a root-delegated field was counted per company. | 3 |

## 2. Dissents — Carried, Not Resolved

| # | Question | Position A | Position B | AAS+ disposition |
|---|---|---|---|---|
| **D-1** | Is `C-04a` closed? | **P02 / Expert 1:** the generator has no dedup — a source fact, and under `BP-02` a design-requirement input | **Expert 4:** proved at *function* level only; `_post` refuses a posted move, so a second pair needs the move **still in draft**, which **is** `C-04b` | **Expert 4 upheld on the logic.** `C-04a` is **not independently closed**. Retained as a **function-level fact** and a **design requirement**; the *system-level* claim is withdrawn. |
| **D-2** | Is the `pfp` pair one lineage or two? | `45` §5: two (founding-company names differ) | Experts 2 and 3, disjoint instruments: **one** | **Experts upheld. LINEAGES = 14.** P02's clause (b) is demoted. |
| **D-3** | Is `C-04b` reachable in deployments? | `47` §3: present in 4 marker-capable deployments, 6 scored "none" | **Expert 4:** `account`'s own validate wizard is a soft-mode poster; `account` is **11 of 11** | **Expert 4 upheld.** Severity was **understated**. |
| **D-4** | Does the 90.7% concentration invalidate the headline? | **Expert 1:** the dominant mass sits on a generation whose standard source is unreadable — the largest gap | **P02 (`C-86`):** a **950-module v16 distribution exists**; `iSMEs` runs **one** non-standard module | **P02 upheld on the fact; Expert 1 upheld on the principle.** The concentration is real and must be published; the *unreadability* is not. |
| **D-5** | Are containerised databases in the population? | `45` §7: enumerated via `docker`, outside the file sweep | **Expert 2:** volatile, and **not re-derivable now** — the runtime is down | **Unresolved.** The count stands with a timestamp and a declared non-reproducibility. **Must be decided in writing.** |

## 3. Contradictions

**24 confirmed (`C-63` … `C-86`), 9 from Expert 1, 8 from Expert 2, 2 from Expert 3, 12 from Expert 4** —
overlapping where two experts found the same thing by different routes. **Two expert claims refuted**
(`49` §4). **None was adopted without P02 re-deriving it.**

**Of the 24, exactly one is a safety finding (`C-74`) and one is a reversal in the package's favour
(`C-86`). The remaining 22 are all the same shape: a correct observation generalised past its evidence** —
a key applied beyond what it identifies, a count applied beyond its unit, a source fact applied beyond
its generation, a module-name match applied as code identity. **That is the thirteenth consecutive round
in which aggregation, not citation, is the defect.**

## 4. Evidence Gaps — Consolidated

| Gap | Status |
|---|---|
| 76,245 candidates not content-tested (39.5%), incl. **807 above the size floor** | **OPEN** — the floor's justification does not cover the 807 |
| 24,258 read failures, and I/O failure still indistinguishable from `NOTDB` (`C-68`) | **OPEN** — instrument must report `enumerated / attempted / classified / failed` |
| Gzipped tar, nested archives, non-`dump.sql` SQL members | **OPEN — declared** |
| `~/Library/Group Containers` — 4 known artefacts, reads blocked this session | **OPEN — access condition, not absence** |
| Content hashes never computed; `ARTEFACTS` is a path count | **OPEN** |
| Per-module versions never extracted; no row may grade above `SOURCE AVAILABLE BUT NOT PROVEN DEPLOYED` | **OPEN** |
| 9 stopped `postgres:16*` containers never enumerated | **OPEN** |
| Non-standard counts re-derived against the corrected union; **the P02-relevant subset has not been** | **OPEN** — `540` is the new total, the P02-relevant split still uses the old union |

## 5. Boss Decisions

`BP-01`, `BP-02`, `BP-03` **stand unchanged.** No expert re-decided them and none was permitted to.
**One breach was found and fixed:** the authorisation pack silently configured the **invoice-triggered**
model `BP-02` declines, without disclaimer (`C-59`). **`C-04a`'s disposition is now explicitly aligned to
`BP-02`:** it concerns a mechanism the target does not adopt, so it is a **design requirement input**,
not a risk carried against the target.

## 6. Mutation Boundary

**Preserved — and it was tested this round and failed on paper.** `C-74` shows the pack would have
authorised a write to a forbidden company. **No mutation occurred at any point**: every expert and every
P02 operation was read-only, and the sandbox is in any case unreachable (`C-78`). **The boundary held in
practice because nothing was executed, not because the pack was correct.**

## 7. AAS+ Position

**The findings are in better shape than the numbers describing them.**

Every substantive accounting conclusion survived four adversarial experts and was reproduced on
independent instruments. Every *count* attached to those conclusions moved. The evidence base is
**larger and more readable** than the package claimed (`C-86`), and the package's **description** of it
was wrong in four separate units.

**AAS+ does not certify P02.** It records that the round did what it was for — the three uncertainty
classes are materially narrowed, the identity model is now testable and has been tested to destruction
twice, and the one thing that could have caused harm was caught **before** it reached a Boss.
