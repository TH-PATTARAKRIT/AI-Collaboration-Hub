# AI02 — P09_ANALYTIC_ALLOCATION_ALGEBRA

**Session:** SMEPLUS-26-09-04-ACC-P09-P2A-REV2-001 · continuation `…ANALYTIC-ECONOMIC-INTEGRITY-001`
**Layer:** 1 — clean-room. The reference-product call chain with file and line citations is in the Layer 2 quarantine companion `AI02-L2`.

---

## 1. THE CALL CHAIN, IN BUSINESS TERMS

```
entry is posted
   └─ the posting action calls analytic-line creation over the entry's WHOLE row set
        └─ obligation validation runs first  (gated twice: execution context, then row type)
        └─ for EACH row:
             └─ if the row carries a non-empty allocation:
                  └─ for EACH key in the allocation:
                       └─ compute the analytic amount
                       └─ create one management record, unless the amount rounds to zero
```

Two properties of this chain decide everything that follows, and both are **absences**:

- **A1 — there is no account-type test anywhere on this path.** Nothing asks whether the row is a profit-and-loss row or a balance-sheet row.
- **A2 — there is no row-type test on the creation path.** A row-type restriction exists, but only inside the *obligation validation* that runs before creation; it constrains whether a **complaint** is raised, never whether a **record** is created.

**Eligibility is therefore decided by exactly one thing: whether the row was given an allocation.** See `AI03`.

## 2. THE ALGEBRA

### 2.1 Definitions

For an accounting entry `E` with rows `r_1 … r_n`:

- `b_i` = the signed balance of row `i`, in company currency (debit positive, credit negative).
- **Double-entry invariant:** `Σ_i b_i = 0`.
- `D_i` = the allocation carried by row `i`: a map from a key to a percentage share. A key names one or more analytic accounts.
- `s_{i,A}` = the share of row `i` allocated to analytic account `A`, as a percentage; `0` if row `i` carries no allocation, or if `A` does not appear in it.

### 2.2 The amount of one management record

For row `i` and key `k`:

```
a(i,k)  =  − b_i × s_k / 100
```

with one variant: when the running total of shares for a key's **root plan** reaches exactly 100 % at the configured percentage precision, the completing record takes the remainder instead of its own share —

```
a(i,k)  =  − b_i × (100 − Σ shares already applied to that root plan) / 100
```

Both forms coincide when the shares are exact. A record is suppressed when `a(i,k)` rounds to zero at the row's currency precision.

**The negation is the sign convention:** a debit row (positive balance) produces a **negative** analytic amount, which is the convention for cost; a credit row produces a positive one, the convention for revenue.

### 2.3 Net analytic effect of an entry on one analytic account

```
N(A,E)  =  Σ_i  a(i, keys containing A)
        =  − (1/100) · Σ_i  b_i · s_{i,A}
```

### 2.4 Gross analytic movement

```
G(A,E)  =  Σ_i | a(i, keys containing A) |
        =  (1/100) · Σ_i | b_i · s_{i,A} |
```

## 3. THE ZEROING THEOREM

> **Theorem.** Let `S ⊆ {r_1 … r_n}` be the set of rows carrying a share for analytic account `A`, and suppose every row in `S` carries the *same* share `s`. Then
> ```
> N(A,E) = − (s/100) · Σ_{i ∈ S} b_i
> ```
> and therefore `N(A,E) = 0` **if and only if** the balances of the rows in `S` sum to zero.

> **Corollary 1 — the both-legs case.** If `S` is the entire row set of the entry, then by the double-entry invariant `Σ_{i∈S} b_i = 0`, hence
> ```
> N(A,E) = 0
> ```
> **unconditionally** — independent of the amount, the share, the currency, the accounts, the analytic plan, the company, and the configuration.

> **Corollary 2 — gross is not zero.** In the same case, for a two-row entry with balances `+X` and `−X`:
> ```
> G(A,E) = 2 · (s/100) · X        while        N(A,E) = 0
> ```
> Two management records exist, each of magnitude `(s/100)·X`, and they annihilate.

> **Corollary 3 — the correctness condition.** `N(A,E)` equals the intended attribution **iff** the rows carrying `A`'s share are exactly the rows whose balances sum to the economic effect being attributed. For a cost attribution that is the profit-and-loss rows **alone**. Including the balance-sheet counterpart is not an approximation of the right answer — it is the exact negation of it.

### 3.1 Classification of Corollary 1

**FACT VERIFIED — as a conditional.** It is arithmetic over a source-stated formula plus the double-entry invariant, and needs no runtime and no data.

> **CORRECTION, ISSUED AFTER AN ADVERSARIAL CHALLENGE CONTRADICTED THE FIRST DRAFT.**
> The first draft attached the word *unconditionally* to the **theorem** and then applied the theorem to a **list of five mechanisms**. The theorem is fine. **The application was wrong for two of the five.** An independent reviewer, tasked to disprove, established that two mechanisms **do not satisfy the antecedent at all** — their counterpart's allocation is *re-derived*, not copied — and that a third satisfies it only when a precondition holds.
>
> The corollary is unconditional **given its antecedent**. It says nothing about a mechanism until that mechanism is shown to satisfy it. Restating a conditional as a property of a mechanism list is exactly the error the project's own denominator discipline exists to prevent, committed here in the algebra rather than in a count.

### 3.2 WHICH MECHANISMS SATISFY THE ANTECEDENT

| Mechanism | Same allocation on every row of a balanced set? | Net |
|---|---|---|
| asset depreciation **when the asset carries an allocation** | **yes** — copied verbatim to both rows | **zero** |
| deferred expense / deferred revenue recognition | **yes** — same builder | **zero** |
| cut-off / change-period accrual | **yes** — the two rows are an explicit debit/credit swap carrying the same allocation | **zero** |
| cash-basis base pair | **yes** — and on the **same account** | **zero** |
| cash-basis tax pair | **yes** | **zero** |
| **change-account transfer** | **NO — the counterpart's allocation is re-derived from money amounts** | **not zero** — see §5.1 |
| **accrued orders** | **NO — the counterpart carries a re-derived weighted aggregate, and it is not a two-row pair at all** | **not zero** — see §5.1 |

**Five mechanisms satisfy the antecedent, not seven.** The two that do not fail in a different and separately serious way.

## 4. APPLIED TO ASSET DEPRECIATION

The depreciation entry is built with exactly two rows:

| Row | Account | Side (for a positive depreciation amount `X`) | Balance `b` | Analytic amount at share `s` |
|---|---|---|---|---|
| row 1 | the asset's **depreciation account** — accumulated depreciation, a **balance-sheet** account | credit `X` | `− X` | `+ (s/100)·X` |
| row 2 | the asset's **depreciation expense account** — a **profit-and-loss** account | debit `X` | `+ X` | `− (s/100)·X` |

The asset's allocation is written onto **both** rows, under an explicit source guard whose stated reason is that omitting the key would otherwise let the rows compute their own.

```
N(cost centre, depreciation entry) = + (s/100)·X  −  (s/100)·X  =  0
G(cost centre, depreciation entry) = 2 · (s/100)·X
```

**The cost centre is debited and credited by the same posting.** For a 100 % allocation of a 1,000 depreciation charge: two management records of 1,000 and −1,000, net 0, gross 2,000.

The same two-row shape holds for the deferred-expense and deferred-revenue variants the asset mechanism also produces: in each, one leg is a balance-sheet account and one is a profit-and-loss account, and both receive the allocation.

## 5. THE OTHER FAILURE MODES THE SAME ALGEBRA PRODUCES

### 5.1 Re-derived counterpart — allocates neither correctly nor to zero

Where a counterpart's allocation is **re-derived** rather than copied, the shares on the two sides differ, so the terms do not cancel:

```
N(A,E) = − (1/100) · [ Σ_source b_i·s_{i,A}  +  b_counterpart·s'_A ]
```

Two independent reasons the re-derived share `s'_A` is short, **both established by adversarial challenge**:

1. **Source rows carrying no allocation still enter the denominator.** The re-derivation divides each accumulated analytic amount by the counterpart's **total balance**, but only rows that *have* an allocation contribute to the numerator. Every unallocated source row therefore dilutes the counterpart's percentages, which then sum to **less than 100** while the source side sums to 100.
2. **Percentage rounding.** Every share is rounded to the configured precision (default two digits) on write. A three-way split re-derived as `33.33 × 3 = 99.99` never reaches the exact-100 branch, so the completing row takes its own rounded share rather than the remainder, and that side is short by 0.01 % of the balance.

**The residue is not noise — it is a number with no economic meaning that survives on the cost centre.** A clean zero at least announces itself; a residue looks like a real cost.

### 5.2 Independent per-row derivation — a one-sided attribution

Where the source object carries **no** allocation at all, the key is deliberately omitted so that each row derives its own from the rule set, keyed on **its own account**. The two rows have different accounts, and the shipped rule mechanism selects by **account prefix** — so a rule written for expense accounts matches the profit-and-loss row and not the balance-sheet row.

```
N(A,E) = − (X/100) · ( s_{expense row} − s_{balance-sheet row} )
```

which is **non-zero and one-sided**. This is not a bug in the arithmetic; it is the arithmetic working correctly on an eligibility decision made per row.

### 5.3 The three modes together

| Mode | Precondition | Net effect | Detectability |
|---|---|---|---|
| **symmetric cancellation** | one allocation copied to every row of a balanced set | **exactly zero** | invisible on net-balance surfaces; visible on account-bucketed ones, except the cash-basis case |
| **re-derived counterpart** | counterpart's shares computed from amounts | **small residue** | looks like a real cost |
| **independent per-row derivation** | no allocation on the source object | **one-sided, non-zero** | looks correct, and may be correct |

**All three come from the same root cause** — the allocation is carried per row and the attribution's subject is the event.

## 6. WHAT THE ALGEBRA DOES **NOT** SETTLE

| Question | Status | Where it is settled |
|---|---|---|
| which events actually put the same allocation on both legs | not settled by algebra | `AI07` event sweep |
| what each management surface displays for a net-zero pair | not settled by algebra | `AI08` |
| whether real deployed data contains such pairs | not settled by algebra | `AI05` |
| whether the design *intends* a balanced analytic subledger | **cannot be settled from source at all** — the source carries no statement of intent; see `AI08` §4 | routed as a design question |

## 7. CHECKPOINT

**CP-AI02 — SOURCE ALGEBRA PROVED, AND ITS SCOPE CORRECTED BY ADVERSARIAL CHALLENGE.** The theorem is FACT VERIFIED as a conditional; **five** mechanisms satisfy its antecedent, not seven; the two that do not fail in a separately serious way. Auto-continue.
