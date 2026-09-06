# P04 — DEPLOYED-CODE IDENTITY DELTA

**LAYER 2 — AUDIT QUARANTINE.** `MD-P04-01`. Affects `CQ-P04-01`, `-02`, `-03`, `-12`.

---

## 1. Material Delta declaration

| Field | Value |
|---|---|
| **Material Delta ID** | `MD-P04-01` |
| **Affected CQ** | `CQ-P04-12` primary; `CQ-P04-01`, `-02`, `-03` bounded |
| **Trigger** | P03 `MD-01` at `bc767a8`: source series read ≠ deployment series, undetected for four rounds |
| **Bounded evidence surface** | The deployment/version evidence **already enumerated** in this package (`13` `EV-DB`) — no new archive discovery, no new census |
| **Why prior evidence insufficient** | `P04-F-85` established that the generations differ. It never asked whether the matching source is **obtainable** |
| **Stop condition** | Every asset-bearing identity has a stated series, and the closability of the source gap is answered once |

## 2. P04 does not reproduce P03's defect

| Test | P03 | P04 |
|---|---|---|
| Deployment series established before source was read? | **No** — four rounds | **Yes** — `P04-F-85`, published 2026-09-05 |
| Findings labelled with the generation they belong to? | Retrofitted at closure | **Already per-identity**: `iSMEs` **v16** · `iEVING`, `BK12MAY26`, `iTEST02` **v19** · `idemo18_uat` **v18** |
| A published mislabel? | The whole source basis | **One, self-corrected**: the v19 databases were once called *"v18-line"* and `iSMEs` *"an older generation"*; `P04-F-85` calls the first **wrong** and the second an understatement of a **two-generation** gap |

> **The rule P03 missed is the rule P04 had already applied.** Neither package deserves
> credit for foresight: P04 applied it because `smeplus-version-basis-defect-rule` was on
> file from P09's failure, and P04 had itself been the session that recorded it.

## 3. What this run adds — the gap is not closable here

P03 enumerated a declared path set (`/Volumes/iMacSys`, `/Volumes/iMac`, `/Volumes/ChatGPT
Installer`, `$HOME` less `~/Library`) with a positive control firing **28 times**, and found
**no series-16 source**.

> **P04 relies on that enumeration and does not repeat it.** Repeating it would be a
> whole-estate sweep, forbidden by §6 of the Constitution and by §4 of the prompt.
> **Reliance is declared:** P04 did not independently enumerate for series-16 source.

**Consequence, stated once and applied to every source claim in this closure:**

| Class | Basis | Status |
|---|---|---|
| **Runtime / population findings** | read from database archives, per identity, series stated | **Unaffected.** `iSMEs` 683/685 daily, 669 real assets, 22 linked / 647 unlinked — these are v16 facts read from v16 data |
| **Source findings** (this closure: `CQ-P04-01`, `-02`, `-03`, `-04`) | read in the **series-18** reference tree and the **18.0.x** custom addons | **Bounded to series 18.** They describe the code that is on this host and installed in the 361-module v18 deployment. They are **not** asserted as behaviour of the v16 `iSMEs` deployment |
| **The v16 source itself** | — | **`UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`.** Not repairable by more searching |

## 4. The one place the bound bites hardest

`CQ-P04-02`. The day-count implementation is read in series-18 source, while the only
population with **683 of 685 assets on daily computation** is `iSMEs`, at **series 16**.

> The convention **used** is a v16 data fact. The convention **implemented** as traced in §2
> of the day-convention closure is a v18 source fact. **They are two claims about two
> generations and this package now says so on the same line.**

## 5. Disposition

> **`MD-P04-01` — `FACT VERIFIED — CLOSED FOR CURRENT EVIDENCE`** for the *test*: P04's
> evidence carries its version basis.
> **The residual source gap is `UNRESOLVED — SPECIFIC EVIDENCE UNAVAILABLE`**, owner named:
> it closes only if a series-16 addons tree is mounted. **Routed to `P04-B-51`.**
