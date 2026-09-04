# P08_CONTROL_MATRIX

Session `SMEPLUS-26-09-04-ACC-P08-R2R-REV2-001`

Each control names **the layer at which it is enforced** — the discipline a prior round proposed after finding affirmative safety claims asserted without one. Layers, weakest to strongest: `none` · `configuration` · `application check` · `isolation rule` · `database constraint`.

| ID | Control | Enforcement layer | Defeasible by | Verdict |
|---|---|---|---|---|
| `IC-01` | **Entry balance (debit = credit)** | **application check** | a caller-supplied context parameter | the defining invariant of double-entry is the weakest control in the kernel |
| `IC-02` | Balance in the transaction currency | **none** | — | never asserted |
| `IC-03` | Debit and credit not both non-zero on one item | **database constraint** | — | holds |
| `IC-04` | Sign coherence between the two currency amounts on one item | **database constraint** | — | holds; **magnitude is not checked** |
| `IC-05` | Account required on an accountable item | **database constraint** | — | holds |
| `IC-06` | Null-forcing on presentation-only items | **database constraint** | — | holds |
| `IC-07` | Entry-number uniqueness | **database constraint** (partial index) | scoped to posted, non-placeholder entries only; no company term | holds within its predicate |
| `IC-08` | An item in a settlement cannot be deleted | **database constraint** (restrict) | — | **the only database object protecting an accounting relationship** |
| `IC-09` | Posted-record attribute protection | **application check** | a caller-supplied context parameter; and the list omits the number, reference and narrative | narrow and waivable |
| `IC-10` | Cannot create an entry already posted | **application check** | — | holds |
| `IC-11` | Posting completeness battery (twelve checks) | **application check** | **a generic attribute write bypasses it entirely** | one of two posting doors validates |
| `IC-12` | Period lock | **application check** | resolved by **relocating the entry's date**, not by refusal — including for the irrevocable lock | not an invariant; it re-dates |
| `IC-13` | Irrevocable lock monotonicity | **application check** | — | holds |
| `IC-14` | Tamper seal | **application check** | opt-in per book; attribute set selected by a caller-supplied version | opt-in and caller-tunable |
| `IC-15` | Seal chain ordering | **application check** over a user-visible, re-assignable number | the renumbering tool | the gapless counter it was designed for is dead |
| `IC-16` | Deletion of a posted entry | **application check** ×5 | a caller-supplied parameter defeats all five | ordinary path refused; caller path open |
| `IC-17` | Retention of posted facts | **configuration**, off by default | never enabling it | absent unless chosen |
| `IC-18` | Item deletion leaves an audit record | **application check**, unconditional | dies with the entry if the whole entry is deleted | the one unconditional audit artefact |
| `IC-19` | Control-account discipline | **application check**, gated on the entry being a customer or supplier document | any manual entry | inverted: the account's own status confers nothing |
| `IC-20` | Journal allow-list on an account | **application check** | bypassed for the book's own default and suspense accounts | holes by design |
| `IC-21` | Company isolation on the entry and item | **isolation rule**, strict | — | holds at the object layer |
| `IC-22` | Company isolation on settlement records | **none** | — | **no isolation rule of any kind on either model** |
| `IC-23` | Company isolation on statement definitions | **none** | — | no company dimension at all |
| `IC-24` | Settlement single-company guard | **application check** comparing the **root** of the company tree | two sibling companies pass | the message asserts what the code does not check |
| `IC-25` | Measurement required for a posting | **none** | — | a three-tier silent cascade always returns a number |
| `IC-26` | Rate provenance on a posted fact | **none** | — | not persisted |
| `IC-27` | Maker–checker on posting | **none** | — | the review flag is set by the poster's own action, from a default that is on |
| `IC-28` | Authorisation to write ledger records | **isolation rule** + model permissions | thirteen integrations create with the permission layer off; two post with the posting check off; **a custom module defeats both layers for read, write and delete** | |

**Twenty-eight controls. Six are enforced at the database layer, and five of those six are per-item value checks; the sixth is a partial uniqueness index. One database object protects an accounting relationship. No cross-record accounting invariant in the domain is enforced below the application layer — including the defining invariant of double-entry bookkeeping.**

**Segregation of duties.** Maker and poster are one role. Granting and revoking a period derogation are one role. Closing and reopening are one duty. Authoring a statement definition and producing the statement are one role.
