# 03 — P04 ASSET EVENT REGISTER

Layer: **2 — audit quarantine**.

Every event that can act on an asset record, its trigger, its state effect, and
whether it produces an accounting effect. Derived from primary source
(`EV-CODE`, `EV-CUST`) this session.

## 1. Declared enumeration

| Element | Declaration |
|---------|-------------|
| POPULATION | Every method, interface button and server action reachable on the asset model, or on an accounting document when an asset link is set |
| PATTERN | State-literal comparison sweep over the asset module's model and wizard files; button and action sweep over its view files; import-chain read of every package initialiser and of the manifest data list |
| PATH SET | The asset module, the loans module, the project–asset bridge (`EV-CODE`); the custom equipment-sequence and advance-expense modules (`EV-CUST`) |
| UNIT | One distinct event, defined as a trigger that changes state or writes an accounting entry |

**Result: 22 distinct events.** All asset accounting behaviour lives in
**three files** — the asset model, the accounting-document extension, and the
modify wizard. Every other module that touches assets reads, links or reports;
none writes an accounting effect.

## 2. Event register

| ID | Event | Trigger | State effect | Accounting effect | Owner |
|----|-------|---------|--------------|-------------------|-------|
| **EV-01** | Create — manual | User saves the asset form | ∅ → draft (**forced**) | none | P04 |
| **EV-02** | Create — as model | "Save as model" from a running asset | ∅ → model | none | P04 |
| **EV-03** | Create — automatic from posted bill | **Posting** of a purchase-type document with a qualifying line | ∅ → draft | none at creation | P01 → P04 |
| **EV-04** | Create — automatic and confirm | As EV-03 where the account's mode is "create and validate" | ∅ → draft → running | **the entire depreciation schedule is posted immediately** | P01 → P04 |
| **EV-05** | Create — from selected journal items | User action on posted journal items, then saves | ∅ → draft | none | P04 |
| **EV-06** | Create — import / data load | ORM create, import, or XML data load | ∅ → draft (**state in the data file is overridden**) | none | P04 |
| **EV-07** | Create — revaluation child | Modify wizard, net value increase | ∅ → draft → running | **an entry is posted first, then the child is created from its debit line** | P04 |
| **EV-08** | Create — duplicate | Record duplication | ∅ → draft | none. **The link to source journal items is not copied** | P04 |
| **EV-09** | Confirm | Button, or automatic under EV-04 | draft → running | every unposted schedule line is posted | P04 |
| **EV-10** | Compute schedule | Button, on a draft asset | none | draft entries created; only posted if the asset is running | P04 |
| **EV-11** | Depreciation posting | Schedule line reaching its date | none | Dr depreciation expense / Cr accumulated depreciation | P04 → P08 |
| **EV-12** | Reverse one depreciation entry | Standard entry reversal | none | a reversal entry, **plus** the reversed amount is silently re-added to the next draft line, or a new line is appended one period later | P04 |
| **EV-13** | Pause | Modify wizard | running → on-hold | **a catch-up depreciation is posted** to the pause date; all later lines are cancelled | P04 |
| **EV-14** | Resume | Button | on-hold → running | normally none. Paused days accumulate and shift the schedule | P04 |
| **EV-15** | Re-evaluate (value, duration or rate) | Modify wizard | running → running | up to **three** entries: catch-up, then either an increase entry (EV-07) or a decrease entry posted to **depreciation expense** | P04 |
| **EV-16** | Cancel asset | Button, running state only | running → cancelled | **every posted entry is reversed**; every draft entry is force-deleted; the paused-day counter is reset | P04 |
| **EV-17** | Set to draft | Button, visible only when there are **no** depreciation entries | running/cancelled → draft | none | P04 |
| **EV-18** | Re-open a closed asset | Button | closed → running | if residual value remains, the modify machinery runs at today's date. **The disposal entry is not automatically reversed** | P04 |
| **EV-19** | Sell | Modify wizard, proceeds taken from a **posted customer invoice** | running/on-hold → closed, **and every child too** | catch-up posted, **then the disposal entry — created in DRAFT** | P02 → P04 |
| **EV-20** | Dispose | Modify wizard, no proceeds | running/on-hold → closed, and every child | catch-up posted, **then the disposal entry — created in DRAFT** | P04 |
| **EV-21** | Archive | Archive flag; blocked unless closed or model | any → archived | none | P04 |
| **EV-22** | Delete | Record deletion; blocked for running, on-hold, closed, and for any asset with a posted entry | draft/model → ∅ | none; a note is written to each source document | P04 |

### 2.1 Two events triggered from the source accounting document

| ID | Event | Behaviour | Class |
|----|-------|-----------|-------|
| **EV-23** | Cancelling the source bill | Attempts to **archive** every asset created from its lines, with **no state filter**, while the archive guard raises unless the asset is closed or a model. Every automatically created asset is draft or running, so **the guard always raises**. Corrected after independent challenge: this is not an unresolved reachability question. **Cancelling a vendor bill that auto-created an asset is hard-blocked, with an error about archiving** — a message that does not describe the situation | **FACT VERIFIED** |
| **EV-24** | Resetting the source bill to draft | Refuses if any linked asset is beyond draft; **deletes** linked draft assets | FACT VERIFIED |

## 3. Event-level control findings

| ID | Finding | Class | Severity |
|----|---------|-------|----------|
| **P04-F-13** | **The derecognition entry is created in draft and is never posted by the system.** The asset is written to the closed state first. An asset can therefore read "Closed" indefinitely while its derecognition entry sits unposted. Confirmed as intended behaviour by the estate's own test, which asserts that the depreciation-schedule report changes once a user posts it manually | FACT VERIFIED | **High** |
| **P04-F-14** | Reversals used to cancel future depreciation are dated **on the original entry's date**, not on the event date. Where a hashed journal or audit-trail rule forces reversal rather than deletion, the reversal lands **in the future period being cancelled** | FACT VERIFIED | **High for period integrity** |
| **P04-F-15** | The downward-revaluation entry is **labelled as an ordinary depreciation** in the ledger. The wizard passes a distinguishing reference that the entry builder never reads. Only a stored type code distinguishes it | FACT VERIFIED | Medium |
| **P04-F-16** | Confirmation posts an asset's **entire life** in one action. Combined with the absence of a lock-date check on confirm, a single action can post into a closed period | PRIOR EVIDENCE (P2 `UNR-09`), re-confirmed | **High** |
| **P04-F-17** | Writing to the asset rewrites accounts on **already-posted** depreciation entries **by line ordinal** — even-numbered lines take the accumulated-depreciation account, odd-numbered lines the expense account. This is applied to the **disposal entry too**, whose lines are asset cost, accumulated depreciation, income and gain/loss — not a two-line depreciation pair | FACT VERIFIED | **High** |
| **P04-F-23** | A blank account link causes the corresponding leg to be **silently dropped**, producing an unbalanced entry. Because the disposal entry is left in draft (P04-F-13), nothing surfaces until a user posts it. *(Identifier corrected: this and the former `P04-F-18` were the same finding under two numbers; `P04-F-18` is withdrawn — see `18` `P04-REV-12`.)* | FACT VERIFIED | **High** |
| **P04-F-19** | The disposal wizard's gain and loss account fields do not reach the entry. They reach it only by **rewriting the company-level default**, executed with elevated privilege. **A disposal in which the wizard's account field is written silently reconfigures the company for all future disposals** | FACT VERIFIED | **High for control** |

**`P04-F-13`, `P04-F-23` and `P04-F-19` compound.** A disposal can leave the company
misconfigured, produce an unbalanced draft entry because of that
misconfiguration, and leave the asset reading "Closed" with nothing posted —
with no error raised at any point in the sequence.

## 4. Events the prompt names that have no host

| Named stage | Register entry | Class |
|-------------|----------------|-------|
| Transfer | none | FACT VERIFIED (scoped negative) |
| Impairment | none | FACT VERIFIED (scoped negative) |
| Scrap | none — must be recorded as EV-20 | FACT VERIFIED (scoped negative) |
| Partial disposal | none. The only granularity available is to capitalize as N separate assets **at creation** and dispose of them individually | FACT VERIFIED |
| Derecognition as a distinct event | none — it is EV-19 / EV-20, and only takes ledger effect when a human posts the draft entry | FACT VERIFIED |
