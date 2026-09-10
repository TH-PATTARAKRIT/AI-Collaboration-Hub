# SC-CONTRA-01 — BOSS RULING `FG-F-06 = READING A`, AND THE GATE CONTRADICTION IT CREATES

> # ⚠ `TWO OPPOSED BOSS RULINGS EXIST ON ONE QUESTION. ONE OF THEM HAS 16 DOWNSTREAM RULINGS ON IT. ONLY BOSS CAN SAY WHICH GOVERNS.`

Session: `[SMEPLUS-26-09-10-ACC-PHASE-SA-SMECORE-CONT-001]`
Branch: `architecture/phase-sa-smes-core-final-scrub-2026-09-10-001`
Head when the ruling was given to this executor: `7eeb5d8e`
Head at recording: **`a8c7054f`**
Executing body: **SMEs CORE** · Boss: **SOLE FINAL APPROVER**

> **Identifier note.** This record was drafted as `SC-BD-02`. **That identifier was taken by
> `SC-BD-02_F4_BOSS_RULING.md` at `89ba9c7d` while this file was being written**, so it is renamed to
> `SC-CONTRA-01`. **Nothing of the other execution's is renamed, moved or altered.**

---

## 1. The ruling given to this executor

> # `FG-F-06 = READING A`
>
> *"`SMEPLUS-DR-EXIT-8C-001` binds Phase SA exit to Phase Pre-Test Matrix. Proceed under `EC-07`. `B-7`
> becomes mandatory before Phase SA exit. Execute the structurally independent review sequence required by
> `EC-07`. Two consecutive clean independent passes are required. … Do not start Phase Pre-Test Matrix. Do
> not declare Phase SA PASS. Return only at the next genuine Boss Authority Gate."*

**Type:** scope clarification of a Boss-approved instrument — **not** a decision family.
**Rejected alternative:** Reading B, its grounds preserved (operative nouns are *Module*/*State*; no Boss
designation found; §2.3/§5 are State-level; six rounds never invoked `EC-07`; the one precedent is §9).
**SMEs Core recommendation at the time:** **none** — `NO AUTHORITY TO SELF-SELECT` was published and held.

---

## 2. ⚠ The contradiction, stated before anything is built on it

| Record | Ruling | Published | What it authorised |
|---|---|---|---|
| **`SC-BD-01`** | **`READING B` — does not bind** | `e113258f`, 07:53 | `EC-07` not engaged · `B-7` blocks nothing · **`F1`–`F8` gate OPENED** |
| **`SC-CONTRA-01`** (this) | **`READING A` — binds** | this commit | `EC-07` engaged at **`0 of 2`** · **`B-7` MANDATORY** · **`F1`–`F8` must NOT be ruled yet** |

### 2.1 It has already propagated — this is the material change since the ruling

At **`89ba9c7d`** the Reading B path recorded:

- **`SC-BD-02`…`SC-BD-10` — 16 of the 23 decisions ruled**, covering `F4`, `F6`, `F7`, `F1`, `F5`, `F2`,
  `F3`, `F8` and the Boss acts;
- `SC-11` propagation register and `SC-12` closure requalification, terminating **`TERMINAL D — HOLD`**
  on `RC-D-03` / `RC-D-04`.

> **Under Reading A, those 16 rulings were taken inside a gate that was not open.** The governing prompt
> §3 states: *"**Do not rule the 23 decisions until `EC-07` is satisfied** or Boss explicitly changes the
> governing scope/rule."* Under Reading A, `EC-07` stands at **`0 of 2`**.
>
> **And it has continued.** At **`a8c7054f`** a further Boss prompt —
> `04_SMEPLUS_PHASE_SA_SMES_CORE_GAP_REMEDIATION_AND_REMAINING_DECISION_PROMPT.md` — was published on the
> Reading B path, directing remediation of its `TERMINAL D` gap. **Recorded as a fact, not as an
> inference: SMEs Core does not read it as settling `FG-F-06`, because it does not address `FG-F-06`.**
>
> **This file does not challenge the substance of any of the 16 rulings, does not re-open them, and does
> not touch their records.** Each is a Boss ruling and each stands or falls on Boss's word, not on this
> executor's. **What is recorded is narrower and factual: their gate precondition is disputed and
> undispositioned.**

### 2.2 What is established, and what SMEs Core refuses to infer

**Established.** Both records exist and cite real heads. `SC-BD-01`'s head (`6d08bcc5`) precedes this
ruling's (`7eeb5d8e`). Sixteen family rulings now rest on `SC-BD-01`.

**NOT established, and not inferable by SMEs Core:** whether Reading A supersedes Reading B as a later
instruction; whether the two rulings were given to two executors in mutual ignorance, exactly as the two
executions themselves ran; whether either record mis-transcribes Boss's intent; **which ruling governs.**

> **A later commit timestamp is evidence about when a record was written, not about which instruction Boss
> intends to stand.** Choosing between two Boss rulings is not an evidence problem. It is the definition of
> Boss authority, and `CF-D-01` fixes it: ***"only Boss may state what a Boss ruling covers."***

---

## 3. Why it cannot be worked around — in the constitution's own words

**`EC-05` — Contradiction Resolution Complete:**

> *"Every material contradiction between … **or prior canonical evidence** must be dispositioned with
> traceable evidence and lineage. **No material contradiction may remain merely as an unresolved
> difference of opinion.**"*

**Two contradictory Boss decision records are prior canonical evidence in contradiction. `EC-05` is OPEN.**

**`EC-07` — the clean-pass criteria include *"new Gate-changing contradiction."***

> **The contradiction exists before pass 1.** Under Reading A's own rule — the rule Boss instructed this
> executor to apply — **no independent pass run while it stands can be clean.** Boss's instruction says a
> Gate-changing contradiction means *"correct it, re-verify it, and restart the consecutive clean-pass
> count."* **Correcting it here means dispositioning it, and that is Boss's act, not a reviewer's.**
>
> **Commissioning a reviewer now would spend an appointed cycle to rediscover a known defect and return the
> count to `0`.** That is why the sequence is **prepared and not opened.**

---

## 4. Affected scope

| | |
|---|---|
| **Families / atomic IDs** | **None directly.** The 23 are unchanged in content, count and ownership by either ruling — `F1` 2 · `F2` 3 · `F3` 1 · `F4` 2 · `F5` 6 · `F6` 4 · `F7` 4 · `F8` 1. **What is disputed is whether they may be ruled now, not what they are** |
| **Vetoes** | **NONE. 6 in force · 0 discharged · 0 self-discharged.** `RC-V-01` still bars implementation start on either reading — **that requirement issues from AAS+/RC, not from `8C-001`** |
| **Pre-Test entry** | Under B: not gated by independence. Under A: **`B-7` gate-blocking, `EC-07` at `0 of 2`.** Category 3 remains `0` on both |
| **`8C-001`** | **Not amended, narrowed or set aside** by either ruling |

---

## 5. What SMEs Core did under this ruling, and where it stopped

**Executed** — all of it valid under either ruling, so no cycle is wasted whichever governs:

| Artefact | Content |
|---|---|
| this record | the ruling, and the contradiction on its face |
| **`SC-EC07-01`** | `EC-01`…`EC-08` status under Reading A. **Three criteria do not pass, and only one is `EC-07`** |
| **`SC-EC07-02`** | `B-7` appointment card — eligibility controls, frozen baseline, attack targets, the six reset triggers, reviewer prohibitions, terminal ladder |

**NOT executed, with the ground for each:**

| Not done | Ground |
|---|---|
| The independent passes | **A party cannot be structurally independent of itself.** Gate prompt §8 forbids claiming it |
| Appointing the challenger | **`Q-BOSS-02` control 2** forbids a session selecting its own verifier |
| Ruling, re-opening or disturbing any of the 16 rulings | They are Boss rulings. **Not this executor's to touch** |
| Choosing between `SC-BD-01` and `SC-CONTRA-01` | **Boss authority** |
| Modifying any controlling artefact | Verified: `SC-BD-01`, `SC-08`, `SC-09`, `SC-10` and all `SC-BD-02`…`SC-BD-10`, `SC-11`, `SC-12` **byte-identical** |

---

## 6. ⚠ The two findings Boss should weigh alongside the route question

Both are in `SC-EC07-01` and both survive **regardless** of which ruling governs, because they are about
the criteria themselves:

1. **`EC-04` does not pass, and Reading A leaves no path to close it.** **`0 of 3`** tolerance-zero
   boundaries are evidence-closed; `CONDITIONAL PASS` is expressly forbidden for them; closing them needs
   execution, execution needs a build, and **`RC-V-01` bars implementation start**. **Two clean passes do
   not close `EC-04`** — a reviewer can verify a control is specified, not make it executed.
2. **`EC-07` may not terminate.** It requires two consecutive passes with **no new material finding
   class** — and **every Phase SA round so far has produced one**, including both executions of this
   session. **Boss should say in advance what happens if passes keep finding things.**

---

## 7. Authority

> **Boss is the SOLE FINAL APPROVER.**
>
> This record documents a ruling Boss gave this executor. **It does not overwrite, withdraw, amend or
> supersede `SC-BD-01`, does not claim priority over it, and does not disturb the 16 rulings that rest on
> it.** Both paths are preserved as lineage.
>
> **It is not a `PASS`, not a Phase SA closure, not a Pre-Test authorisation, and not a veto discharge.**
> **Phase SA is NOT closed.** Structurally independent passes remain **`0`** and none is claimed.

---

## 8. The question returned to Boss

> ## `WHICH RULING GOVERNS — SC-BD-01 (READING B), OR SC-CONTRA-01 (READING A)?`
>
> **If `SC-BD-01` governs:** the 16 rulings stand; the path continues at its own `TERMINAL D` (SMEs Core
> must supply recommendations for `RC-D-03` and `RC-D-04`); `EC-07` is not engaged.
>
> **If `SC-CONTRA-01` governs:** `EC-05` must first be dispositioned; **then** `B-7` is appointed and the
> `EC-07` sequence opens against a re-frozen baseline; **and `EC-04` still does not pass** (§6.1). Boss
> should also state what becomes of the 16 rulings already recorded — **SMEs Core does not presume they are
> void, and does not presume they are safe.**

No Evidence = No Progress. Never Skip Gate. Boss must not be the first detector.
Boss remains the sole Final Approver.
