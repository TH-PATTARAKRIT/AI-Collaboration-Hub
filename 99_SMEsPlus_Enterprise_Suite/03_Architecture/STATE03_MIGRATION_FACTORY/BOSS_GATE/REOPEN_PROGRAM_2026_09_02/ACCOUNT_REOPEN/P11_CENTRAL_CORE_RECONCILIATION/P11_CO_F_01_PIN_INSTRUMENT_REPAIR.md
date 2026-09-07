# P11 — `CO-F-01` PIN-HONOURING INSTRUMENT REPAIR

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-REMEDIATION-002]`
**Authority** `PHASE-S/Q-BOSS-01` = APPROVED · Boss ruling `Q-BOSS-03` §3.A @ closeout `2e2b8de`
**Base** `corr/p11-phase-s-final-2026-09-07-001` @ `002748d` — **read-only, never rewritten**
**Published on** `corr/p11-phase-s-remediation-2026-09-07-001`

> **This is an owner repair, not a verification.** It is authored by Claude Opus 5, which
> `XRECON/Q-BOSS-01` (`XRD-009`) disqualifies from challenging its own repairs. **`RC-02` must test
> everything below, including the possibility that it is wrong.** No disposition is issued here and
> no PASS is declared.

---

## 1. The defect, reproduced before it was repaired

`intake_derivations.py` @ `002748d` declares a ten-row pin table `PEERS = [(peer, sha, branch), …]`
and then resolves **both** derivation trees as `"origin/" + branch`. **The `sha` column is bound and
never read.**

| Run | Instrument | Change | Result |
|---|---|---|---|
| `RUN A` | the file exactly as published at `002748d` | none | `D1 58 · D2 50 · D3 159 · UNION 216` |
| `RUN B` | same file | **`P09` pin `4778792` → `92de8a1`** | `D1 58 · D2 50 · D3 159 · UNION 216` |

**`RUN A` and `RUN B` are byte-identical on stdout and on the union file**
(`sha256 49f1bdb5475156243e11536aa088a7586db2fbaeef908b0cc5ffab43e2922630`, 216 members).
**Changing a declared pin changes nothing. That is the proof the pin is never read** — not an
inference from reading the source.

**`RUN A` is also the non-determinism proof.** The same published instrument returned `UNION 212` at
CORR3, `UNION 214` when `002748d` was written, and **`UNION 216` today** — because it reads whatever
`origin/<branch>` points to at the instant of execution. **The published denominator is a timestamp,
not a measurement.**

## 2. What was repaired, and what was deliberately not

**Repaired — and only this:**
1. both tree resolutions resolve **the declared pin**, never `"origin/"+branch`;
2. the pin table is validated **before any derivation**, and the instrument **fails closed** on a pin
   that is missing, malformed, unresolvable, not a commit, duplicated across peers, **not an ancestor
   of its declared branch**, or **non-substantive under `P11-G-10`** (a prompt commit);
3. the pin table actually honoured is **printed by the run itself**, so the reader never has to trust
   a table in prose.

**Deliberately NOT repaired.** The four inline defects `E2-C2` / `E2-C7` / `E2-C8` / `E2-C15`
(raw-substring peer match with no word boundary; integer-sort regex that silently excludes un-numbered
groups; unjustified `TAIL=5`; `(peer, basename)` key that collapses distinct paths) are **carried
forward unchanged**. Repairing them here would move the population for a second, unrelated reason and
make the pin delta unreadable. **The instrument remains NOT CERTIFIED. `B-35` stands and is
unaffected by this repair.**

**Superseded, not replaced:** `intake_derivations.py` and `union_212.txt` are **untouched at their
published bytes** and remain the lineage record of what was actually run.

| Artefact | `sha256` | Standing |
|---|---|---|
| `intake_derivations.py` | `567b9b8f0defb75b448145ddf2f432bcad4ef173d3078e074da8c6c7b28d2d3f` | **SUPERSEDED — preserved as lineage** |
| `union_212.txt` (214 members) | `94e7d5977eac563c4f9d9e0a5e2e0490f70c58b915140473be5c9f2adcba1e27` | **SUPERSEDED — floating-head output** |
| `intake_derivations_pinned.py` | `b9fe0b8e6130667813dffb7e2ee3e515dbabfbe237485544709e978c21242508` | **CURRENT — pin-honouring** |
| `union_214_pinned.txt` (214 members) | `80d18bd11694e4e121cbf3683965fda5e19b213ee4b109d64ea45857523e0efc` | **CURRENT — pin-honoured output** |

## 3. The exact pin table used by the repaired run

Printed by the run itself, not transcribed. Every pin resolved, substantive, and an ancestor of its
declared branch.

| Peer | Pin (full) | Commit subject |
|---|---|---|
| `P01` | `b820b29b13f351ec21c724c05ea9aa8da2a15e14` | *research(G01-P01): background-task disposition* |
| `P02` | `7cb1c2783f3f5b9c11bf107d4d7202affe455d7d` | *research(P02): CP-06..CP-10 — challenge record* |
| `P03` | `bc767a81417f6d115f42ec71f477d761b75895e6` | *research(G01-P03): bounded-deep closure* |
| `P04` | `65b8841116d3ad696454c61a48eb08da5612d895` | *research(G01-P04): bounded-deep closure* |
| `P05` | `205e0ac30ae19df7ed2816eaec85a0d1d3cef147` | *research(account-p05): G01 PHASE S closure* |
| `P06` | `1b018c104001eb4683166518a6161a8cd8ab5cee` | *research(account-p06): post-publication record* |
| `P07` | `ee2be30ebf155e241510b3c7133c69419eb060a0` | *research(account): P07 — S02 bounded closure* |
| `P08` | `00ccd663d55d72830c8e0db46e4cc1aa345d0af1` | *P08 Phase-S: challenge record, AAS+ consolidation* |
| `P09` | `4778792196371c460d3e6ca87bf8d9adee760f47` | *research(account): P09 L1-L8 bounded correction* |
| `P10` | `1fea562cb32e23bd44a1c6e6b4a2cf1081d25287` | *research(P10): G02 bounded-deep closure* |

## 4. Determinism — executed twice from clean state

`RUN C1` and `RUN C2`, repaired instrument, clean output directory each time, same frozen inputs:

```
D1 56 · D2 48 · D3 157 · UNION 214 · D1∩D2 19 / D1\D2 37 / D2\D1 29
```

**stdout byte-identical · union file byte-identical**
(`sha256 80d18bd11694e4e121cbf3683965fda5e19b213ee4b109d64ea45857523e0efc`).

## 5. Controls — each fires for its own distinct reason

**A control that fires for the wrong reason is not a control.** Two of this session's first-draft
controls did exactly that and were **discarded and rebuilt**: the intended non-ancestor pin was
another peer's pin and tripped the duplicate check instead, and the intended "valid alternative pin"
`4778792~1` **is** the prompt commit `92de8a1` and tripped the substantiveness check. Both are
re-run below with inputs that isolate the intended condition. **Recorded because the failure is the
finding, not an embarrassment to omit.**

| Control | Pin substituted for `P09` | Expected | Observed |
|---|---|---|---|
| **FAIL-CLOSED — missing** | `""` | exit ≠ 0, no derivation | **exit 3** — *pin MISSING* |
| **FAIL-CLOSED — malformed** | `zzz9999` | exit ≠ 0 | **exit 3** — *pin MALFORMED* |
| **FAIL-CLOSED — unresolved** | `0123456` | exit ≠ 0 | **exit 3** — *pin UNRESOLVED or not a commit* |
| **FAIL-CLOSED — not a commit** | `4b825dc` (the empty tree) | exit ≠ 0 | **exit 3** — *not a commit* |
| **FAIL-CLOSED — non-ancestor** | `c7cfd8a` (substantive, not in table) | exit ≠ 0 | **exit 3** — *NOT AN ANCESTOR of declared branch* |
| **FAIL-CLOSED — non-substantive** | `92de8a1` (prompt commit) | exit ≠ 0 | **exit 3** — *NON-SUBSTANTIVE under `P11-G-10`* |
| **PIN-SENSITIVITY (positive)** | `acf58d2` (valid, substantive, ancestor) | output **must move** | **exit 0**, `D1 54 · D2 48 · D3 154 · UNION 211`; three named `P09` members drop |
| **BEHAVIOUR-PRESERVATION (positive)** | `92de8a1`, validation disabled | must reproduce the published **before** | **`D1 55 · D2 48 · D3 155 · UNION 212 · 19/36/29` — exact** |

**The behaviour-preservation control is the one that matters most.** The repaired instrument, pointed
at the same commit CORR3 actually read, **reproduces CORR3's published figures to the digit**. The
repair therefore changes *which tree is read* and **nothing else** about the derivations.

## 6. Provenance of the published figures — floating heads, proven

`RUN E`: pins set to the branch heads **as they stood when `002748d` was written**
(`P06 1b018c1` · `P08 c7cfd8a` · `P09 150a033`), validation disabled as a diagnostic.

```
D1 57 · D2 49 · D3 157 · UNION 214 · 20/37/29
```

This is **exactly** P11's published "after" table, and the union file it produced is
**byte-identical to the published `union_212.txt`**. **P11's published post-repair figures were
produced by floating heads, not by the declared pins.** Confirmed, not inferred.

## 7. Old output vs repaired output — **by member identity, not cardinality**

**Both unions contain 214 members. They are not the same 214.**

| | Published (floating) | Pin-honoured |
|---|---|---|
| members | 214 | 214 |
| `sha256` | `94e7d59…dcba1e27` | `80d18bd…523e0efc` |

| Direction | Member |
|---|---|
| **In published, NOT in pin-honoured** | `P08 \| 64_P08_NOTIFICATION_TO_P11_Q_P08_01.md` |
| **In pin-honoured, NOT in published** | `P08 \| 59_P08_METHOD_AND_REQUIREMENT_REGISTER.md` |

**Cause:** `64_…` exists only at P08's floating head `c7cfd8a`, not at P08's declared pin `00ccd66`.
Its arrival made P08's numbered series one longer, and `D3`'s `TAIL=5` window slid by one — so one
member left the set as another entered and **the count concealed the substitution**. A reader
checking only the total would have seen `214 = 214` and concluded nothing had changed.

> **`P11-G-12`: a population is identified by its members, never by its cardinality. Two sets of the
> same size are not the same set, and a count is the one comparison that cannot detect a
> substitution.**

**A second consequence, and it is not a small one:** the member the floating run silently pulled in is
**the P08 notification P11 simultaneously asserts it never received** (`CO-F-02`). **P11's own
published population contains the document its prose calls absent.** The two defects are one
event seen from two sides.

## 8. Claims re-stated — bounded to the affected claim class

**Claim class:** every P11 claim whose truth depends on the CORR3 intake population **at the
post-re-pin head**. Enumerated by identifier and by figure across the whole package, not by remembered
phrase. **Claims resting on the `92de8a1` "before" figures are NOT in this class and are NOT touched** —
the behaviour-preservation control (§5) shows they reproduce exactly.

| Carrier | Published | Re-stated | Basis |
|---|---|---|---|
| `P11_OWNER_BOUNDED_CORRECTION_2026_09_07.md` §*material delta* `D1` | **57** | **56** | §4 |
| " `D2` | **49** | **48** | §4 |
| " `D3` | 157 | 157 — **unchanged** | §4 |
| " `UNION` | 214 | 214 in count, **different set** | §7 |
| " `D1∩D2 / D1\D2 / D2\D1` | **20 / 37 / 29** | **19 / 37 / 29** | §4 |
| `P11_AUTO_RESUME_STATE.md`:38 intake denominator | `D1 57 · D2 49 · D3 157 · union 214` | `D1 56 · D2 48 · D3 157 · union 214` | §4 |
| `P11_RESEARCH_ERROR_AND_REVISION_LOG.md` `P11-E-47` | *"the instrument re-runs at `4778792` and reproduces `D1 55 · D2 48 · D3 155 · union 212` unchanged"* | **FALSE at the head it names — WITHDRAWN** | §9 |

**Not widened.** `B-35` (instrument not certified), `B-37`, `B-38`, `AAS+-VETO-04`, the `S06` control
failure, the 12-member control set, `Q-P11-02`, `Q-P11-03` and `Q-P11-04` are **untouched**: none of
them turns on the post-re-pin population. **Terminal state is unchanged —
`TERMINAL B — MATERIAL EVIDENCE-INTEGRITY DEFECT REMAINS`.**

## 9. `P11-E-47` is false at the head it names

`P11-E-47` states the corrected instrument *"re-runs at `4778792` and reproduces `D1 55 · D2 48 ·
D3 155 · union 212` unchanged (the `P09` delta between the two commits does not alter the
derivations)."*

**Both halves are false.**

1. The instrument at `002748d` **cannot re-run "at `4778792`"** — it resolves `origin/<branch>`. The
   sentence describes an execution that the published code cannot perform.
2. A genuinely pin-honoured run at `4778792` returns **`D1 56 · D2 48 · D3 157 · UNION 214`**, not
   `55/48/155/212`. **The `P09` delta does alter the derivations** — by `+1` on `D1` and `+2` on `D3`.

**`P11-E-47`'s correction is `WITHDRAWN AS FALSE`. The defect it reported — that the claim-class sweep
was bounded by file extension and missed the `.py` — is REAL and STANDS, as does `P11-G-11`.** What
falls is only its verification sentence: **the re-pin was written into the file and then not read by
it**, so the "reproduces unchanged" check confirmed nothing. **`P11-E-48`.**

> **`P11-G-13`: an edit to a value a program never reads is not a repair. Before recording a re-pin as
> executed, change the pin to a wrong value and prove the output moves.** Had that control been run at
> `002748d`, `CO-F-01` would have been caught by P11 itself.

## 10. Standing

| | |
|---|---|
| `CO-F-01` | **REPAIRED — UNVERIFIED** |
| Verification | **`RC-02`, by the independent verifier. Not run, not selected, not self-satisfied here** |
| Instrument certification | **STILL NOT CERTIFIED — `B-35` stands** |
| Terminal | **`TERMINAL B` — unchanged** |

**No Evidence = No Progress. Never Skip Gate. Boss is the sole Final Approver.**
