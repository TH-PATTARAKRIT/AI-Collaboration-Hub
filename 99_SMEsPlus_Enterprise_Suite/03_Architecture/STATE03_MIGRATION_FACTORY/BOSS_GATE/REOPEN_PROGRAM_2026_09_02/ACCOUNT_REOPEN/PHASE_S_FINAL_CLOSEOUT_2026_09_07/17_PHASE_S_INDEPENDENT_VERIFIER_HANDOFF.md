# 17_PHASE_S_INDEPENDENT_VERIFIER_HANDOFF

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-FINAL-CLOSEOUT-001]`
**For** the verifier appointed under `PHASE-S/Q-BOSS-02` @ `2930723`
**Prepared by** Claude Opus 5 — **disqualified from every RC lane below** (`10_` §1)

## 1. Why this is a handoff and not a result

`PHASE-S/Q-BOSS-02` criterion 1 is model/agent separation. **The P06/P08/P09/P11 corrections were
authored by Claude; this session is Claude.** Under dispatch §5 the RC execution lane stopped and
everything else continued. **Every lane below is frozen, immutable and ready.**

## 2. Frozen surfaces — do not challenge a moving branch

| RC | Branch | SHA | Subject |
|---|---|---|---|
| `RC-01` | `corr/p09-phase-s-final-2026-09-07-001` | `2079a25` | `Q-P09-01` `M-1`/`L-4` authority; `Q-P09-02` bounded six-correction surface |
| `RC-02` | `corr/p11-phase-s-final-2026-09-07-001` | `002748d` | `Q-P11-01` re-pin · `-02` `HO-` qualification · `-03` `B-38` |
| `RC-03` | `corr/p06-iev-phase-s-final-2026-09-07-001` | `692ea27` | `Q-P06-01` totals / denominator |
| `RC-04` | `corr/p06-source-phase-s-final-2026-09-07-001` | `b5f5a21` | `Q-P06-03` counts · `Q-P06-04` archive negative · **re-issued `Q-P06-02`** |
| `RC-05` | `corr/p08-phase-s-final-2026-09-07-001` | `c7cfd8a` | `Q-P08-01` exact arithmetic · `Q-P08-02` `HO-` namespace |
| `RC-06` | `corr/p11-phase-s-final-2026-09-07-001` | `002748d` | `Q-P11-04` `F-02` + method-rule withdrawal — **after `RC-05`** |
| `RC-07` | `corr/p08-iev-phase-s-final-2026-09-07-001` | `d685176` | `Q-P08-03` — **pointer-only, no fresh challenge required** |

**Two IV blockers are cleared, and the reasons matter:**
- `RC-03` was `BLOCKED` on the unstable 25-vs-26 total. **Adjudicated: 26**, independently re-executed
  (`09_` §2). **Test that adjudication — do not adopt it.**
- `RC-04` was `NOT READY` because *"the surface does not exist"*. **It exists** at `b5f5a21` and predates
  the report asserting its absence (`16_` §4).

## 3. Recommended order — dependency-aware, parallel where possible

```
start immediately, in parallel:  RC-01   RC-02   RC-03   RC-04
gated:                           RC-05  (evidence gap, §5)
blocked on RC-05:                RC-06
not required:                    RC-07
```

## 4. Leads to TEST, not to adopt

**Everything below was produced by the disqualified model. It is offered as a lead. Treat each as a
hypothesis that may be wrong, and reproduce it independently.**

### `CO-F-01` → `RC-02` — **highest value; test first**

Claim: `LAYER2_P11_EVIDENCE/corr3_instrument/intake_derivations.py` declares a ten-row `(peer, sha, branch)`
table and **never reads the `sha`**; both tree resolutions use `"origin/"+br`.

Reproduction, from the repository root (it returns 0 from any other directory — a broken-test zero):

```
RUN A  the file as published at 002748d
RUN B  same file, P09 pin changed 4778792 → 92de8a1
       → outputs byte-identical  ⇒ the pin is never read
RUN C  both tree resolutions changed to resolve `sha` instead of "origin/"+br
       → D1 56 · D2 48 · D3 157 · UNION 214 · 19/37/29
RUN D  RUN C with P09 pin 92de8a1
       → D1 55 · D2 48 · D3 155 · UNION 212 · 19/36/29   (= P11's published "before", exactly)
RUN E  floating heads as at 002748d's commit time (P06 1b018c1 · P08 c7cfd8a · P09 150a033)
       → D1 57 · D2 49 · D3 157 · UNION 214 · 20/37/29   (= P11's published "after", exactly;
         union file byte-identical to the published union_212.txt)
RUN A today, current heads → UNION 216
POSITIVE CONTROL: git ls-tree over the P08 branch → 1034 .md files (proves the instrument sees the tree)
```

**Specific things to test:** (a) is the published `214` a *different set* from the pin-honoured `214`?
The lead says yes — one-out/one-in on `59_P08_METHOD_AND_REQUIREMENT_REGISTER.md` / `64_P08_NOTIFICATION_TO_P11_Q_P08_01.md`,
because `D3`'s `TAIL=5` window over P08's series shifted when P08 gained a 64th file. (b) Is
`P11-E-47`'s *"reproduces … union 212 unchanged"* false at the head it names?

### `CO-F-02` → `RC-02` — receipt-side freshness

P11 states the P08 notification is *"Not received"* at two lines while `64_P08_NOTIFICATION_TO_P11_Q_P08_01.md`
was committed 2 minutes earlier. A second inbound (`P06_TO_P11_COUNT_CORRECTION_NOTICE.md`) postdates
P11's last commit entirely.

### `XQ-R-02` → `RC-03` — the denominator is **26**

**Warning, from this session's own error:** the naive count returns **27**. The extra member is
`IEV-D-99`, the documented negative-control token matching its own documentation at
`P06_Q_P06_01_02_EXECUTION_RECORD.md:66`. **Validate with a second command shape.**

### `XQ-R-01` → `RC-04` — re-issued `Q-P06-02`

Target corrected from `IEV_006/P06_VERIFICATION_INSTRUMENT_CONTROL_REGISTER.md`:45 (which carries no such
row) to `G02_RECOVERY_2026_09_06/P06_VERIFICATION_TOOL_DEFECT_REGISTER.md`:45 on the **source** track.
**The row is unrepaired at `b5f5a21` by design** — it still reads `65 … max id = 65 … YES`, contradicted
by `:54`. Challenge the re-issue and the repair when it lands.

### Namespace exposure → any lane

Eight bare identifier families are shared across five packages (`11_` §5). **`HO-` had a live collision
and was repaired. `M-` was tested and is disjoint** (P08 zero-pads `M-01..07`; P09 does not). **Six
families are untested and their reachability is unmeasured. Severity is deliberately not ranked.**

## 5. `RC-05` — what must be supplied before it can run

The P08 correction surface at `c7cfd8a` does **not** carry:

1. an independently executable exact-arithmetic instrument;
2. the frozen input/extract location for the balance measurement;
3. population identity for `DB-SM` / `DB-BK` / `DB-EV`;
4. re-executable outputs at exact / `1e-7` / `1e-4` / `0.005`, for **both** computed and stored balance;
5. a discriminating positive control.

**This session did not go looking for the databases**, because locating and running them *is* `RC-05`.

> **Do not read item 2 as "the evidence does not exist."** The tested claim is only that **the frozen
> surface does not carry it**. This programme has repeatedly found primary evidence sitting on the host
> outside the session clone. **Sweep before concluding absence**, and if you conclude absence, publish
> the tool, the path set, the pattern and the output that establish it.

**`RC-01` is not evidence-blocked:** its inputs were checked for existence and are present —
`/Volumes/iMacSys/ODOO/ODOO-COMMUNITY/Odoo18/t8master/addons` (13,515 `.py`) and the `INSTRUMENTS/`
directory with `k1_population.json`. **They were not executed here.** Note `q1.py` reads an **Odoo 18**
tree; **establish the deployed version before relying on that root.**

## 6. Boundary you must keep, and this session kept

Verify the exact frozen SHA · reproduce independently with a control capable of failing · preserve dissent ·
one disposition per finding (`SUPPORTED` / `CONTRADICTED` / `NARROWED` / `MISSING EVIDENCE`) plus material
yes/no · publish on your own branch at an immutable SHA · **mutate no owner evidence · discharge no veto ·
declare no Phase S closure.**
