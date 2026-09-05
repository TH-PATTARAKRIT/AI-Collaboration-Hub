# P01 — DATABASE IDENTITY REPAIR

Session: `SMEPLUS-26-09-05-ACC-P01-P2P-EVIDENCE-VERSION-DEPLOYMENT-INTEGRITY-001`
Supplemental continuation. **No reset. Nothing discarded.**
Layer: **1.**

---

## 1. THE DATABASE THAT WAS DECLARED UNREADABLE

| Field | Value |
|---|---|
| **Archive identity** | the fourth dump in the evidence area, tagged `D4` |
| **Original label** | the archive's own filename — a database name and a timestamp. **No artifact ever asserted a product version for it** |
| **Original claimed version** | none by any artifact; the *"unreadable"* classification was asserted by **this research**, twice |
| **Actual application version** | **series 19.0** — 452 of 453 installed modules carry a `19.0.x` version string, 1 unset |
| **Database engine version** | **PostgreSQL 18.4**, per the archive header (`Dumped from database version: 18.4`) |
| **Dump format** | CUSTOM, **archive header format 1.16** |
| **Tool initially used** | the database restore utility**16.15** |
| **Exact failure** | `the database restore utility: error: unsupported version (1.16) in file header` |
| **Tool that read it** | the database restore utility**18.6**, already installed on the same machine at a sibling path |
| **Installed module registry** | **453 installed** — the fullest module set in the estate |
| **Company population** | **1 company**, created 2026-02-02 |
| **Transaction volume** | **10 journal entries** in total (3 miscellaneous, 5 vendor-side, 2 other) |

---

## 2. THE ROOT CAUSE, PROVEN

The archive is not damaged, not encrypted and not inaccessible. It was produced by a **newer
database engine** than the restore tool that was invoked, and the archive format version it
carries is **higher than that tool supports**.

| Dump | Engine that produced it | Archive readable by restore 16? |
|---|---|---|
| `D1` | PostgreSQL 15.15 | yes |
| `D2` | PostgreSQL 15.18 | yes |
| `D3` | PostgreSQL 15.7 | yes |
| **`D4`** | **PostgreSQL 18.4** | **no — format 1.16** |

Both restore binaries were present throughout. **Nothing was installed or changed to read it.**

---

## 3. WHY IT IS MATERIAL — AND A CORRECTION TO HOW THAT WAS STATED

The previous round called `D4` *"the most relevant database in the estate."* **That is only half
right, and the half that is wrong matters.**

| Dimension | `D4`'s standing |
|---|---|
| Module coverage | **Highest in the estate** — 453 installed, nearly double any other. It is the only deployment with three-way matching, the subcontracting family and the base requisition family installed |
| **Transaction evidence** | **Almost none — 10 journal entries in total** |
| Company population | 1 |
| Therefore | **`D4` is the most fully-*installed* deployment and one of the least *exercised*.** It is decisive for questions of *what is installed* and near-useless for questions of *what actually happens* |

Recorded as `ERR-P01-16`. The earlier phrasing invited the reader to expect operational evidence
that `D4` does not contain.

---

## 4. A SECOND IDENTITY DEFECT FOUND WHILE REPAIRING THE FIRST

> **`D1` and `D2` are the same deployment, not two.**

Their company sets are **identical** — all 44 companies match on both internal identifier and
partner identifier — and both carry the same creation-date span (2026-03-18 to 2026-04-29). They
are two snapshots of one estate, taken eleven days apart.

**Consequences:**

| Previously stated | Corrected |
|---|---|
| Four databases | **Three distinct deployments**, captured in four archives |
| *"across 90 company rows"* | **46 distinct companies** — 44 + 1 + 1. The 90 figure double-counts the 44 |
| Two independent v19 deployments corroborating each other | **One v19 estate observed twice.** Agreement between `D1` and `D2` is **not** independent corroboration |

Recorded as `ERR-P01-17`. This weakens every finding that treated `D1` and `D2` as two
independent witnesses.

---

## 5. THE ESTATE, AS IT ACTUALLY IS

| Deployment | Archives | App series | Companies | Journal entries | Installed modules | Character |
|---|---|---|---|---|---|---|
| **E-1** | `D1`, `D2` | 19.0 | 44 | 16 | 251 / 232 | multi-company, **operationally active in the warehouse, almost inactive in the ledger** |
| **E-2** | `D3` | **16.0** | 1 | **183,590** | 190 | **the only deployment with real accounting history** |
| **E-3** | `D4` | 19.0 | 1 | 10 | **453** | fullest module set, effectively unexercised |

> **Only one deployment in the estate has meaningful accounting history, and it is application
> series 16 — a series for which P01 has read no source at all.**

That is the single most important sentence in this document.

---

## 6. WHAT THIS REPAIR DOES NOT DO

- It does not analyse `D4`'s transaction data beyond the registry and the counts above.
- It does not establish which source tree any deployment was built from — see
  `P01_VERSION_IDENTITY_MATRIX.md`.
- It does not re-open any finding on its own; the falsifications are in
  `P01_DATABASE_FALSIFICATION_REGISTER.md`.

---

# §7 — THE ESTATE, CORRECTED AGAIN (supersedes §3 and §5)

An independent expert established, and this session verified directly, that the characterisation
in §3 was wrong on its second axis too.

## 7.1 The measured shape

| Deployment | Purchase orders | Stock movements | Journal entries | Installed modules | Companies |
|---|---|---|---|---|---|
| `E-1` (two archives, one estate) | 31 | **14,441** | 16 | 251 | 44 |
| `E-2` | 5,881 | **103,949** | **183,590** | 190 | 1 |
| `E-3` | **27,879** | 55 | 10 | **453** | 1 |

## 7.2 What this actually means — each deployment is lopsided differently

| Deployment | Has | Lacks |
|---|---|---|
| `E-1` | **movements** | orders, accounting |
| `E-2` | **orders, movements and accounting** | nothing — **the only complete one** |
| `E-3` | **orders** (the largest population in the estate) and **the fullest module set** | movements, accounting |

> **`E-3` is not "near-empty". It holds the largest purchase-order population in the estate —
> 27,879, nearly five times the operating deployment's — with 55 stock movements and 10 journal
> entries behind them.** The expert characterises it as a bulk-import staging database, and the
> shape is consistent with that.

## 7.3 The consequence for every P01 finding

> **Only one deployment in the estate exercises the full procure-to-pay chain, and it is the
> series for which no core source exists anywhere on this volume.**

Every other deployment can answer *what is installed* and *what is configured*, and **none of
them can answer *what happens*** — because in each, at least one link of the chain is unpopulated.

This is the sharpest statement of P01's evidence position that the programme has produced, and
it took three corrections to reach: the excluded archive, the version mislabelling, and now the
activity profile.

## 7.4 Correction to `ERR-P01-16`

`ERR-P01-16` recorded that calling `E-3` *"the most relevant database"* was half right, because
it measured module coverage and not transaction evidence. **That correction was itself incomplete**:
it then leaned on "10 journal entries" to imply `E-3` is unexercised, which is false for orders.

Amended: `E-3` is **decisive for what is installed, decisive for the order surface, and silent on
movement and accounting.** Three axes, not two.
