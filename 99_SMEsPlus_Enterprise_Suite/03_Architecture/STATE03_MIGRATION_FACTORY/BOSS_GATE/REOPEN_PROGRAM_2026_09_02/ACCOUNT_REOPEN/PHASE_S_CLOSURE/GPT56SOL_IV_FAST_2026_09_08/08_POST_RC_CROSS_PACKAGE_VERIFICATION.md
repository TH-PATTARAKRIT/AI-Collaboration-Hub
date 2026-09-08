# 08_POST_RC_CROSS_PACKAGE_VERIFICATION

Status: **COMPLETE FOR THE CURRENT FROZEN RC SET — MATERIAL PROPAGATION ITEMS REMAIN**

## 1. P07 read-only closure check
P07 frozen evidence: `ee2be30ebf155e241510b3c7133c69419eb060a0`.

`19_P07_CORE_RECON_HANDOFF_PACK.md` was opened read-only. It routes to cross-process reconciliation a ruling on whether tax-reporting grouping may span companies and under what security boundary. **P07 owner mutation is not required by this verification.** P11 still needs to consume/disposition that inbound evidence in its own closure surface (`B-36`).

### B-39 generation reconciliation
P11 registered `P08-HO-14` vs `P07-F-02/-03` as a possible contradiction.

Independent version check shows:
- P08-HO-14 is explicitly keyed `S16c` mechanism + `D16` data: **16.0 custom source / DB-SM**;
- P07-F-02 states the tax-point substitution was **removed in the v19 migration**.

Disposition recommendation: **`VERSION-SPLIT — NO DIRECT CONTRADICTION`**. Both statements can be true of different generations. P11 should update B-39 with this lineage; no P07 repair is required.

## 2. P11 B-36 / B-35 closure blockers
P11 frozen surface remains `TERMINAL B` and still carries:
- `B-36`: P07 core-recon handoff was inside the denominator but never opened by P11;
- `B-35`: intake instrument remains explicitly **NOT CERTIFIED**.

P11's own auto-resume says B-35 is fully executable and requires, before closure:
1. rebuild D3 with timestamp/path/word-boundary discipline and no unjustified tail bound;
2. re-certify on a control set P11 did not choose, full twelve including S06;
3. later propagation/re-challenge items.

RC-02 PASS does not discharge B-35 because RC-02 tested only Q-P11-01/02/03 repairs.

## 3. P06 → P11 propagation
P06 published `P06_TO_P11_COUNT_CORRECTION_NOTICE.md` at `b5f5a21`. P11's frozen auto-resume explicitly records it as genuinely post-snapshot and unconsumed. XRECON found the wrong count figures did not cross into P11 substance. P11 should acknowledge/consume it during final propagation; no P06 re-research is required.

## 4. P09 → P11 propagation
P11 B-38 is frozen against P09 `4778792`. P09 later moved to `2079a25`, where M-1 is owner-marked resolved and M-2 awaited independent challenge. RC-01 now independently fails M-2 and finds additional bounded correction items.

Therefore P11 must **not** refresh B-38 until P09 publishes the RC-01 correction at a new immutable SHA. After that, P11 must re-point B-38 to the final P09 state rather than to `4778792`.

## 5. P08 → P11 propagation
P11 Q-P11-04 consumes the three-DB P08 balance premise. RC-05 independently reproduces a fourth frozen DB. P11 must refresh F-02/CI-01 only after P08 publishes the bounded RC-05 correction; P11 must not re-derive P08 balances itself.

## 6. B-3 / P11-E-49 bounded manifest sweep
Independent tree-vs-manifest checks:
- P11: actual package files 92; hash rows 91; the only unlisted file is `P11_EVIDENCE_MANIFEST.md`; all 91 listed substantive hashes match. Generator explicitly excludes the manifest itself, while prose says “every file”.
- P08 RC05: actual files 8; hash rows 7; only unlisted file is `MANIFEST.md`; listed hashes match.
- P09: 135 documents checksummed against 135-document declared population; no missing/bad rows.
- P06: manifest explicitly declares self-exclusion.

Disposition: **PASS-WITH-NONMATERIAL-FINDINGS** for the bounded P11-E-49 pattern. No substantive evidence omission reproduced on current P11/P08 manifests; P11/P08 should make the self-exclusion wording explicit in their next bounded publication.

## 7. Cross-package terminal
No stale/current conflict discovered requires reset. The material deltas are bounded and owner-identifiable:
P06 RC-04 · P08 RC-05 · P09 RC-01 · P11 RC-06 + pre-existing P11 B-35/B-36 propagation work.