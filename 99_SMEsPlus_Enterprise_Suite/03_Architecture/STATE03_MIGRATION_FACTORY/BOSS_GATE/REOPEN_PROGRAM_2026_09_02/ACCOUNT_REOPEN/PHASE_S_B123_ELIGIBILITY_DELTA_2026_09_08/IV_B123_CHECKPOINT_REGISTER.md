# IV_B123 — Checkpoint register

| CP | Step | Result | Evidence |
|---|---|---|---|
| CP-B123-01 | Consume Boss ruling from the control branch, not the prompt | DONE | `control/account-phase-s-boss-decisions-2026-09-08-001` |
| CP-B123-02 | Verify frozen handoff head and blob | DONE — both resolve exactly | `0941161…`, `961b2ec…` |
| CP-B123-03 | Re-derive executor eligibility per commit | DONE — 6 of 6 trailers | `01` §3 |
| CP-B123-04 | Prove the eligibility predicate can return empty | DONE — 193 of 200 negative | `01` §4 |
| CP-B123-05 | Establish the cause of the appointed verifier's hold | DONE — connector OFFLINE | `9a5699e` §4 |
| CP-B123-06 | Test whether that device is reachable now | DONE — it is this host, online | `02` §3 |
| CP-B123-07 | Re-check declared host inputs are exposed | DONE — 13,515 `.py`; 4 dumps; `pg_restore` 18.6 | `02` §3 |
| CP-B123-08 | Enumerate candidate fallback verifiers | DONE — zero non-Claude identities | `02` §4 |
| CP-B123-09 | Validate that enumeration with a second command shape | DONE — 10 hits, all human-account, positive control 217 | `02` §4 |
| CP-B123-10 | Execute RC-01 … RC-06 | **WITHHELD — ineligible executor** | `01` §5, §6 |
| CP-B123-11 | Execute B-3 bounded `P11-E-49` sweep | **WITHHELD — ineligible executor** | `03` |
| CP-B123-12 | Veto disposition | NOT ISSUED — would rest on RC results not produced | `03` |
| CP-B123-13 | Publish terminal state and routing recommendation | DONE | `04` |

## Verifier errors recorded rather than erased

- A zsh glob over `/Users/admin/Downloads/*.backup` matched nothing and printed
  `no matches found`. In a chained command this aborts the remainder and would
  have supported a false "dumps absent" conclusion. The dumps were therefore
  located by **`PGDMP` magic bytes rather than by file extension**, which is the
  instrument reported in `02` §3. No published conclusion rests on the glob.
- Reading `~/.desktop-commander-device/device.json` returned a live bearer token
  into the session. It was not copied into any artifact. Recorded in `02` §6 as a
  credential-hygiene item, not as a finding.
