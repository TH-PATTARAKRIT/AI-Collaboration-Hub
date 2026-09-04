# ACCOUNT WAVE A — `GB-08` EVIDENCE MANIFEST (SHA-256)

Session `SMEPLUS-26-09-04-ACCOUNT-WAVE-A-GB08-001` · Date `2026-09-04`

> **Citable identity of this package = the roll-up digest in §1.** It is content-addressed and has no
> commit-SHA regress: a commit cannot contain its own SHA, so a package that cites its own commit is
> always one commit stale.

---

## 1. Roll-up

| Item | Value |
|---|---|
| Package | `ACCOUNT_WAVE_A_CORE_LEDGER/GB08_DECISION/` |
| Files manifested | **8** — 5 decision documents · 1 re-runnable evidence script · 1 captured output · 1 manifest script |
| **Roll-up digest (SHA-256 of the per-file digest list)** | `9a51f4aaed8e63e94c41a153951dd8d5a62689463bf913854aaa658c0f4c0a72` |
| Regenerate | `cd ACCOUNT_WAVE_A_CORE_LEDGER && bash GB08_DECISION/LAYER2_GB08_EVIDENCE/mkmanifest.sh \| shasum -a 256` |
| Excluded by design | **this file** and `ACCOUNT_WAVE_A_GB08_PUBLICATION_RECORD.md` — both cite the roll-up, so both are outside it. **The roll-up is therefore stable across the publication commit.** |

---

## 2. Per-file digests

```
6bb38d53e185557d872e71beb15cffe50e289a61f97f78cb565c071f37bd048c  ./ACCOUNT_WAVE_A_GB08_AAS_PLUS_PMO_RECOMMENDATION.md
8dc9277f5d6efe8eec08f0458e50a1bf498b5207b2b2136ddc63596111fec6db  ./ACCOUNT_WAVE_A_GB08_BOSS_DECISION_PACKAGE.md
bcabf6bbdafd4a7051ae49e2b4e9ae5448578b94e29ddd1b8bdce761769ce447  ./ACCOUNT_WAVE_A_GB08_DOWNSTREAM_DEPENDENCY_MAP.md
6654d6353f799f6f437f933417ded2edc4bfcde99e8ad95ecd548e7ddf777b4b  ./ACCOUNT_WAVE_A_GB08_EVIDENCE_TRACE.md
e62bd8ee9e91e0c051fee742409a86358a8ffd00d096f77a1bab431fe4367824  ./ACCOUNT_WAVE_A_GB08_OPTIONS_REGISTER.md
e3037ffa0cd58acb4b36b72960187ac67f35bbdb1bc47dd0a7c6e2e891eb793e  ./LAYER2_GB08_EVIDENCE/gb08_evidence.sh
32c8d5522f7903d322a02af87f2d4db761678284820136aa10ca626da27830ec  ./LAYER2_GB08_EVIDENCE/gb08_evidence_output.txt
976a8bd75a81b61e216081660badc372dcb8428276813fea2b2aa4853586456d  ./LAYER2_GB08_EVIDENCE/mkmanifest.sh
```

---

## 3. Re-runnable evidence

| Script | Reproduces |
|---|---|
| `LAYER2_GB08_EVIDENCE/gb08_evidence.sh` | The whole root enumeration and divergence result: the 22-root population from a declared pattern, the nesting test, the 4 distinct `res_currency.py` digests, the `Δ1` test **twice** (comment string and structurally), the `Δ3` `sum_currency` count, the manifested-module count per root, and the resolver-uniqueness search |
| `LAYER2_GB08_EVIDENCE/gb08_evidence_output.txt` | The captured output of the above, as run on `2026-09-04` against `/Volumes/iMacSys` |
| `LAYER2_GB08_EVIDENCE/mkmanifest.sh` | This manifest |

**One command:** `VOL=/Volumes/iMacSys bash GB08_DECISION/LAYER2_GB08_EVIDENCE/gb08_evidence.sh`

---

## 4. Relationship to the `FINAL_CLOSURE` package

| Package | Roll-up digest | Status |
|---|---|---|
| `FINAL_CLOSURE/` **as published at `ba0b747`** | `f6d168fdc95cad5114c6ab9ce3de21e230b9bba607b0ef436533b11491ff3781` | **Verified from `origin`** — recomputed from content extracted with `git archive origin/research/…` |
| `FINAL_CLOSURE/` **after the `GB-08` amendment** | see `FINAL_CLOSURE/ACCOUNT_WAVE_A_FINAL_EVIDENCE_MANIFEST_SHA256.md §1a` | Regenerated in the same commit as this package |
| `GB08_DECISION/` | §1 above | New |

**`FINAL_CLOSURE/` is amended, not replaced.** Two of its files change: the Final Research Gate Report
(publication status, one denominator, and a new `GB-08` section) and the superseded `GB-08` package
(a supersession banner only — its original body is left unaltered so the corrections stay auditable).
