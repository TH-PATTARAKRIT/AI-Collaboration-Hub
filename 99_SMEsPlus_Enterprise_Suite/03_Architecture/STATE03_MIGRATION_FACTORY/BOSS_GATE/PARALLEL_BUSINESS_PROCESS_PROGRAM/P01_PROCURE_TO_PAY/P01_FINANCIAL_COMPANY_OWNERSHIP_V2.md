# P01 — FINANCIAL COMPANY OWNERSHIP v2

Session: `SMEPLUS-26-09-05-…-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Layer: **1.** Produced under an explicit **disproof** assignment.
Assessed under the scope-aware constitution: `PLATFORM` · `TENANT` · `COMPANY`.
**`REQUIRED OWNERSHIP CANNOT BE PROVEN = DENY`.**

---

## 1. CLASSIFICATION

> ### `INFERRED ONLY`
>
> The disproof **did not break it**. It refined it, corrected two of P01's own attributions, and
> **produced deployed proof the prior position lacked.**

---

## 2. THE DEPLOYED PROOF — NEW, AND DECISIVE

The prior rounds argued ownership was *unproven* from mechanism. The deployment now shows the
consequence directly:

> **533 of 563 posted journal-item rows in the 44-company estate sit in a company that does not
> own the account they post to.** One of sixteen moves uses another company's journal.

So "the company owning the financial effect" is **at least three diverging values** — the move's
company, the account's company, the journal's company — **with no ownership assertion anywhere
reconciling them**.

**Expert-reported; not re-derived by this session.** It is the strongest single piece of
evidence in the P01 ownership thread and it should be re-derived before it is relied on.

Supporting configuration facts, same source:
- The later series makes the chart **multi-company**, and **one payable control account is shared
  between two companies**.
- Only **11 of 44** companies have any account at all.
- One company's intercompany bill journal **belongs to a different company**.

---

## 3. THE REACHABILITY PATH — CORRECTED

The prior position named the **partner hierarchy** as the reachable path. The disproof found a
shorter and more mundane one:

> **A single active, non-superuser account holds membership in 28 of 44 companies, spanning all
> four corporate root trees.** Three of thirty-eight users are cross-root.

**No hierarchy trick is needed.** An ordinary user simply *is* in most of the estate.

That is a **stronger** finding than the prior one and it does not depend on any elevated
privilege.

---

## 4. THE GUARD ANALYSIS — CONFIRMED, AND ONE GUARD RE-CHARACTERISED

| Guard | Status |
|---|---|
| The declared access check on the creating user | **Confirmed inert.** The framework coerces superuser mode for the superuser identity, and the deployed "create as" user is that identity on 44 of 44 companies. **The expert adds that this superuser is inactive — and the field's own domain explicitly re-admits inactive users**, so the configuration is not accidental |
| **The company-consistency check** | **Re-characterised — it DOES execute.** The prior analysis never named it. It is **satisfied, not bypassed**, because **2,993 of 2,993 corporate partners are company-less** — so there is no inconsistency for it to catch |
| The purchase order's own company-consistency automation | **Never evaluated** — the model does not enable it in either generation, so its company-scoped field declarations are inert |

The second row matters: **a control that passes because the data makes it vacuous is not a
control.** This is the "prove the executor" discipline reaching its most refined result in P01 —
the guard runs, and proves nothing.

---

## 5. TWO CORRECTIONS TO P01's OWN ATTRIBUTION

### 5.1 The trigger of the cross-company **bill** path is a **sale** document
P01 stated in two rounds that *"posting a vendor bill whose partner resolves to another company
creates a document in that other company."* **Verified wrong by this session.** The routine
filters for **sale documents**; the inverse map turns a customer invoice into a **vendor bill in
the target company**.

> **The trigger is a P02 object. The output is a P01 object.**

The *other* path — order approval creating a sales order in another company — **is** triggered by
a P01 object, and that attribution stands.

Recorded as `ERR-P01-21`. Routed to **P02**.

### 5.2 A seventh cross-company path was omitted
An additional intercompany module is installed and carries three further call sites, including
one on the goods-movement path. **Not analysed by P01 — class C.**

---

## 6. THE SIX ACTOR PATHS

| Actor path | Ownership of the resulting company-scoped effect |
|---|---|
| Normal user | **not proven** — and a single ordinary account spans 28 of 44 companies |
| Multi-company user | **not proven** — this is the ordinary case here, not an edge case |
| Superuser | **not proven** — and it is the configured creator on 44 of 44 |
| Shared catalogue object | **not proven** — all corporate partners are company-less, which is what makes the consistency check vacuous |
| Elevated-privilege path | **not proven** |
| Auto-post path | **not proven** — enabled on three companies |

---

## 7. NEVER EXECUTED

> **Zero auto-generated documents exist in any deployment.**

So the whole mechanism is **capability, not history**. The risk is real and **unrealised**, and
P01 says so rather than implying a breach occurred.

---

## 8. DISPOSITION

| Item | Status |
|---|---|
| Classification | **`INFERRED ONLY`** |
| Tolerance-zero | **HOLD** — `EC-04` forbids passing over it |
| Deployed proof of diverging company attribution | **expert-reported; re-derivation required before reliance** |
| Reachability | **an ordinary user, no privilege trick** |
| Executed anywhere | **no** |
| Trigger ownership | **path 1 = P01; path 2 = P02** (corrected) |
| Decision owner | **SaaS / Platform Architecture and P11.** P01 decides nothing |
