# P08_FAILURE_EDGE_CASE_REGISTER

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

Failure classes in which **every equation the ledger can check is satisfied and the accounting fact is nonetheless untrue**, plus the classes in which the equation itself does not hold.

| ID | Failure class | Detectable by any control in the benchmark? |
|---|---|---|
| `FE-01` | The same business fact posted twice, producing two lawful entries | **no** — no event identity |
| `FE-02` | An entry posted with no lines, through the non-validating posting door | **no** |
| `FE-03` | An entry balanced in the reporting currency, unbalanced in its transaction currency | **no** |
| `FE-04` | An entry posted with the balance assertion suppressed | **no** — nothing below the application layer would catch it |
| `FE-05` | A journal item re-parented to another entry | **no** |
| `FE-06` | A posted item's account changed in place, restating a prior period | **no** — no check at all on several of the attributes |
| `FE-07` | An entry renumbered after posting, breaking the seal chain's ordering key | **no** |
| `FE-08` | A sealed entry renamed by narrowing the sealed attribute set | **no** |
| `FE-09` | A posted entry deleted with no evidence, on a default installation | **no** |
| `FE-10` | An entry relocated forward out of a locked period — **including the irrevocable lock** — carrying a full annual charge into the wrong fiscal year | **no** — the product's own test asserts the behaviour |
| `FE-11` | A settlement across two companies, with the whole difference posted to one chosen by list order | **no** |
| `FE-12` | A settlement's stored open amount overwritten out of step with its matches | **no** |
| `FE-13` | A document reported paid while its item still carries a reporting-currency balance the ageing report shows | the line-level flag catches it; **the document status does not read that flag** |
| `FE-14` | A foreign-currency posting valued at parity because no rate existed | **no** — indistinguishable from a genuine 1:1 |
| `FE-15` | A foreign-currency posting valued at a rate dated **after** the posting | **no** |
| `FE-16` | A closed period's statement returning a different number on re-run | **no** — at least eleven routes |
| `FE-17` | A statement cell reporting a number no posting supports | **no** — by design, three stored value classes |
| `FE-18` | A consolidated figure translated at parity, or a fact silently dropped from a consolidated statement | **no** — the two translation modes fail differently |
| `FE-19` | A statutory extract bearing one entity's identity over another entity's documents | **no** |
| `FE-20` | A counterparty on a posted fact rewritten from outside accounting, by either of two paths | **no** — one path meets none of the mitigations credited to the other |
| `FE-21` | The ledger erased whole-table, every company, by a settings action | **no** — it never reaches the object layer |
| `FE-22` | Permission and isolation defeated for read, write and delete by a custom access-check override | search stays filtered; **nothing else does** |
| `FE-23` | A subsidiary store (fixed assets, inventory valuation) diverging from the ledger | **no mechanism found** — and P08 did not run that search (`C`) |

**Twenty-three classes. Twenty-one are undetectable by any control in the benchmark; one is detectable by a flag the consuming status does not read; one was not searched.**

The class the taxonomy has no cell for, and which this package therefore names explicitly: **`FE-04` is the case where the equation itself does not hold and the fact posts anyway.** Every other class assumes the ledger's equations hold and asks what is *nonetheless* untrue. A design tested only against the others would never be asked to defend it.
