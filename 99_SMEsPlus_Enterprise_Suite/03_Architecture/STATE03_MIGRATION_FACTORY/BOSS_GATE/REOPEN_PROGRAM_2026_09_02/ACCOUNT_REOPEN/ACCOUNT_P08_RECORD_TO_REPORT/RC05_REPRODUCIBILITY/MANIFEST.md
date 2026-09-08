# RC-05 REPRODUCIBILITY PACKAGE — MANIFEST

**POPULATION:** every file under `RC05_REPRODUCIBILITY/` **EXCEPT `MANIFEST.md` itself** · **PATTERN:** `find . -type f` · **UNIT:** one file.

> **`P08-C5`, 2026-09-08 — the self-exclusion is now explicit.** **`MANIFEST.md` is excluded from the substantive file population by definition**, because a manifest cannot contain its own digest: writing the hash changes the bytes that produced it. **7 is the count of substantive files; the manifest is the 8th file on disk and the 0th member of the population it describes.**
>
> **No missing substantive hash was found, and none is invented here.** `RC05-F5` asked only that the exclusion be *stated* rather than left for a reader to infer from a count that does not add up to the directory listing. **An unstated exclusion and an omission are indistinguishable to anyone recounting the directory** — which is the whole reason the clause exists.

| Files | Roll-up SHA-256 |
|---|---|
| **7** | `904a8fdef7bbb927735a4589cb3e67faada15f7139abbea7a67ee9b253f3554e` |

> **Coverage assertion:** `find` returned **7**, manifest processed **7**. Both re-measured in this commit, after the last edit to any listed file (`P11-G-15`).

```
19ca4c315dc7ec48d2514fb5238003d984ce9be4174942b3f21e8e45c985c781  00_RC05_REPRODUCIBILITY_PACKAGE.md
8ddac6fc670617fae48d4ace87365d0855ce3fd314012fd8e16d1f5d85c03599  EXPECTED_CONTROL_BEHAVIOUR.md
2151cd445a4ddb11df7b86315bcaf46b17035d7f29b62adc38ece1b00a2c9ea1  instrument/rc05_balance.py
3a13a4cdc761085697249714ed1f5c3f4311990ed0f9305194f68501eec5130b  owner_preparation_run/RUN_1_all_three.txt
3a13a4cdc761085697249714ed1f5c3f4311990ed0f9305194f68501eec5130b  owner_preparation_run/RUN_2_all_three.txt
71db1b4f6eade0b6a828e5c1ea10edcba1f883084e888f5e99505d6d5b701139  owner_preparation_run/RUN_3_DBSM_injection.txt
5a195c151d5acffa6f6398e18b7eb742870609d89d4a3e4dcd98dc9720a47fe0  owner_preparation_run/RUN_4_all_four_pg18.txt
```
