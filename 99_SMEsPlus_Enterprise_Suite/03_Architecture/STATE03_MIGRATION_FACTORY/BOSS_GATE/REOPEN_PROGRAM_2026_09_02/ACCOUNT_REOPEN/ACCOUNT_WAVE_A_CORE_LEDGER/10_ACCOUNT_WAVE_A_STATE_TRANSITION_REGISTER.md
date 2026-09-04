# 10 — ACCOUNT_WAVE_A_STATE_TRANSITION_REGISTER

Layer 1 clean-room · Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-CORE-001`

## 1. The declared state space is not the real one

The reference entry declares three states — draft, posted, cancelled. That is **not** the real state
space. Four orthogonal flags persist independently of it, and two of them are irreversible:

| Dimension | Values | Reversible? |
|---|---|---|
| Declared state | draft · posted · cancelled | yes |
| Has ever been posted | no · **yes** | **no** |
| Secured by hash | no · **yes** | **no** |
| Number consumed | no · yes | only by clearing the number |
| Deferred posting | none · at date · recurring | yes |

The effective state space is therefore **3 × 2 × 2 × 2** in the dimensions that matter, and the
accounting meaning of "draft" differs completely depending on the second flag: a never-posted draft
is a proposal, while a draft that has been posted before is a **retracted fact** — the same declared
state carrying two opposite accounting meanings.

`RECOMMENDATION:` SMEsPlus should make this explicit rather than inherit the conflation. A retracted
fact and an unsubmitted proposal are different things and should not share a state name.

## 2. Transition table

`Destroys` names data lost with no recovery path. `Emits` names a new accounting event.

| From | Trigger | To | Destroys | Emits | Guard | Guard owner |
|---|---|---|---|---|---|---|
| — | create | draft | — | — | balanced-entry check | **application, suppressible** (`COR-07`) |
| draft | edit document date (non-sale) | draft | the intended accounting date | `AE-03` **re-dating with no lock configured** | none | none — automatic (`COR-02`) |
| draft | post | posted | — | `AE-01`, possibly `AE-02` re-dating, possibly `AE-09` hashing | permission; completeness; balance; journal active; **deprecated-account block** (`COR-03`) | application |
| draft | post, future-dated, soft mode | draft + deferred | — | — | date comparison | application |
| draft | delete | — | the draft | — | mid-chain deletion needs elevated rights | application |
| posted | reset to draft | draft, has-been-posted | **all analytic lines; all matching records** | `AE-05` | not hashed; not an exchange or cash-basis entry; period not locked | application |
| posted | cancel | cancelled | **same as above — routes through reset** | `AE-07` | same as reset | application |
| posted | reverse | posted + new posted | — | `AE-06`, possibly auto-match | — | application |
| posted | delete | — | **the accounting fact** | `AE-08` | deletion-protection flag, **bypassable by context; the bypass logs outside the database** | **configuration** (`EV-011`) |
| posted | edit substance | refused | — | — | frozen-field list, **bypassed at seven production sites** | **the calling module** (`COR-15`) |
| posted | edit reference or narration | posted | — | — | **none** | none |
| posted | write balance on a hashed entry | posted | — | — | **guard fails open; detector still catches it** | `CONTRA-01a` |
| posted | write transaction-currency amount on a hashed entry | posted | — | — | **neither guard nor detector** | `CONTRA-01b` |
| posted, unhashed | secure | posted, hashed | — | `AE-09` | — | configuration |
| posted, hashed | any of: reset to draft, delete, edit hashed fields | **refused** | — | — | hash presence | **the only unconditional immutability in Wave A** |
| cancelled | reset to draft | draft | — | — | as reset | application |
| any | account merge | unchanged state, **different account** | **the original account record and the posting's provenance** | `AE-20` | **none — executed by direct statement past the ORM's own guards; nothing is logged** | **none** (`COR-08`) |

## 3. Reconciliation state transitions

| From | Trigger | To | Emits |
|---|---|---|---|
| open | partial match | partially matched, marker `P` | `AE-10`; possibly `AE-11` exchange difference; possibly `AE-13` cash-basis tax |
| partially matched | further match to zero residual | fully matched | full-match record created |
| fully matched | unmatch | open | `AE-12` — **the exchange entry is reversed by a new posted entry** |
| any matched | the entry is reset to draft | **open, silently** | none — the match records are simply deleted (`EV-012`) |

The last row is the important one: matching state can be destroyed by an operation performed on the
*entry*, with no reconciliation-level action and no record that a match ever existed.

## 4. Period state transitions

There is no period object, so there are no period states — only dates moving.

| From | Trigger | To | Reversible |
|---|---|---|---|
| open | soft lock moved forward | locked for that range | **yes, freely, by anyone who may edit company settings** |
| locked | soft lock moved backward | open again | yes — **this is reopening, and it requires no distinct authority** |
| locked | exception granted | open for the named user or for **everyone**, optionally **forever** | by revocation — **by the same role that granted it** (`COR-04`) |
| open or locked | hard lock set | permanently locked | **never** |
| — | hard lock set on a parent company | every subsidiary's effective lock advances | never |

## 5. What the transition analysis establishes

1. **Three transitions destroy data with no recovery path**, and in two of them the destruction is
   invisible: reset-to-draft (matches and analytic lines), delete (the fact), merge (the account and
   the provenance).
2. **Cancel is not a distinct transition.** It routes through reset-to-draft and therefore carries
   the same destruction, while presenting to the user as the safe option.
3. **Only one guard in the entire register is unconditional** — the hash. Every other guard is owned
   by application code, configuration, or the calling module, and at least three are routinely
   bypassed in shipped code paths.
4. **The most consequential transition has no guard at all**: the merge.

`RECOMMENDATION:` for SMEsPlus, a transition that destroys an accounting fact or its lineage must not
exist. Where the business need is real (a mis-posted entry, a retired account), the transition should
be *additive* — reversal, succession — so that the state machine only ever moves forward.
