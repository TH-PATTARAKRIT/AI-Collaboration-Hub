# IV EVIDENCE MANIFEST — SHA-256

**Session** `[SMEPLUS-26-09-07-ACC-PHASE-S-INDEPENDENT-RC-VERIFY-001]`
**Branch** `audit/account-phase-s-iv-rc-verify-2026-09-07-001` · base `origin/SMEsPlus` @ `b8666f1`

## Coverage — stated so the exclusion is declared, not netted

| | |
|---|---|
| **POPULATION** | every file under `PHASE_S_IV_RC_VERIFY_2026_09_07/` |
| **PATTERN** | `find . -type f` |
| **UNIT** | one file |
| **`find . -type f` returns** | **15** |
| **Listed and hashed below** | **14** |
| **Declared exclusion** | **1 — `IV_EVIDENCE_MANIFEST_SHA256.md`, this file.** A manifest cannot contain its own hash. **The exclusion is stated; the population is not reduced to match the listing** |
| **Roll-up SHA-256 over the 14 listed lines** | `19c5400815c67fc5a24eaaf16da8825b342d80d1da8e30ece07f55fa1a4990e4` |

> **This form is deliberate.** `IV-R-04` (`07_` §4) records two manifests in this programme that
> declare the same population and pattern and then assert *"`find` returned N, manifest processed N"*
> where `find` in fact returns N+1. **15 ≠ 14 here, and both numbers are printed.**
> P09's `PACKAGE_MANIFEST_SHA256.md` @ `2079a25` is the passing control this follows.
>
> Measured **after** the last edit to any listed file, and re-measured at commit.

```
f784879ecbec01b40a9cd3582a83ff1b2a663d4a7e04655a3e2ff41a216e1f23  00_IV_APPOINTMENT_AND_PRECONDITION.md
039e3620f1ae71a17f33976d4e0d854bd0184fdf3155d2ef10d2b496a4a25170  01_RC01_P09_CHALLENGE.md
37ff0f36d4cb8913c63b1b729a7b6476936f3a4106c82fbfa6eb9fc9f8b1d9b1  02_RC05_P08_CHALLENGE.md
902f47b5ba50fbdd4c322deddb5e6697f54cda9dab1cb5e2897eb5383efe18fa  03_RC02_P11_CHALLENGE.md
4d57dbdf703ffe13525c6775f5cd2dfce4720641c5f21d5639a6510fd328ec52  04_RC06_P11_CHALLENGE.md
5fa5bbad113711fad354496c32e4b5bfd9603134432b4566788c2ee7e78c63a9  05_RC03_P06_IEV_CHALLENGE.md
daa672a8b5058e3b6c81323e9e4e03bcbe5d28fc286c344457e69f4c7346edbc  06_RC04_P06_SOURCE_CHALLENGE.md
de3964b9be7fcbd415b2d833dce3b790d9ee4dcc388bec5428ad6913d8783d92  07_RC_RESULT_REGISTER.md
e6be46bff25a630e2c410bb5cf1795fba41a528d3561a578d6c2a2088dc5d23b  08_POST_RC_CROSS_PACKAGE_VERIFICATION.md
d2038cf06385283de8dbdb2c0debd0bde40716c4dfae68552ff8eba756f22e98  09_VETO_DISPOSITION_RECOMMENDATION.md
d161dedd0c9350cf1e984fe2eab4b29f0b370bd685002c946ff4c3c9c31d394c  10_PHASE_S_CLOSURE_CRITERIA_INDEPENDENT_TEST.md
9046a6cb50ac883ad4f032876d243574fdc852ee9a5a01e7199e4dfe568b98b4  11_PHASE_S_FINAL_BOSS_DECISION_EVIDENCE_PACK.md
c5381d79b37af916bb63305cf96260db49ab00f90d2729ebd2c9147c62a805fc  IV_AUTO_RESUME_STATE.md
a2854ab88f75258222c80cdbe239d517a86d4bf935e139bec585823d09248b6b  IV_CHECKPOINT_REGISTER.md
```
