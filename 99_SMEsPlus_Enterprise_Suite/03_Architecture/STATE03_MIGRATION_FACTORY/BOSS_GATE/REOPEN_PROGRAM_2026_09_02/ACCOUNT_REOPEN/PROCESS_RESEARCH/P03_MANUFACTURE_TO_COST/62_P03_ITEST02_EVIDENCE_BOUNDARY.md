# 62 — iTEST02 EVIDENCE BOUNDARY

**LAYER 2 — AUDIT QUARANTINE.** `UNR-P03-07`. **No environment change was performed.**

---

## 1. The constraint

Round 3: `pg_restore: error: unsupported version (1.16) in file header`. Round 3 recorded
this as *one tooling upgrade away* and **did not upgrade**, correctly: §17 of this round's
directive confirms an upgrade would be an environment change and is prohibited.

## 2. Safe alternatives, exhausted in order — executed, not assumed

| # | Method | Result |
|---|---|---|
| 1 | Local `pg_restore` | **16.15**; dump is format **1.16-0**, needs 17+ |
| 2 | Other `pg_restore` binaries already on the host | `find /opt/homebrew /usr/local -name pg_restore` → **none besides 16.15** |
| 3 | Other readers already present | `psql`, `sqlite3` — neither reads a PostgreSQL custom archive |
| 4 | Header / metadata inspection | `PGDMP` + `01 10` → v1.16; `file` → *PostgreSQL custom database dump - v1.16-0*. Confirms the format, yields no data |
| 5 | **Containerised tooling already available** | `docker info` → **server 29.5.2 already running**; `colima status` → **already running**; `docker images` → **`postgres:17` and `postgres:18` already cached** |

## 3. Why method 5 is not an environment change

§17 of the directive explicitly permits *"containerized read-only tooling if already
available"*. Every element was already present and was verified so **before** use:

| Property | Evidence |
|---|---|
| Daemon **not started by this session** | `docker info` returned a server version on first query |
| Image **not pulled** | `postgres:17` already in the local image list |
| Dump mounted **read-only** | `-v <dump>:/d.dump:ro` |
| **No network** | `--network none` |
| Container **not persisted** | `--rm` |
| Host unchanged | nothing installed, upgraded, configured or written |
| Database **not restored** | `pg_restore -f -` streams to stdout only; no server was ever connected to |

**No package was installed. No binary was upgraded. No daemon was started. No image was
downloaded. No file was written outside the session scratchpad and the package directory.**

## 4. Disposition

> **`UNR-P03-07` — CLOSED. iTEST02 read read-only, with no environment change.**

Archive: created 2026-07-14, dbname `iTEST02`, **26,804 TOC entries**, format CUSTOM
v1.16-0.

## 5. What it produced

The fourth data point **overturned three round-3 conclusions** (`61` §4) and produced the
first population in which `DEP-13` is answerable (`0 of 60`). It also produced the `DC-07`
live exposure and the `DC-01` overlap test.

> Round 3 called this *"the cheapest open item in the package"*. It was, and it was also the
> most consequential: a single unread file was carrying three incorrect conclusions.

## 6. Honest note on round 3

Round 3 reported the container route as unavailable. **It did not check.** The draft
evidence file for this round initially repeated that, and was corrected when the check was
actually run and found Docker and Colima present and running.

This is the negative-claim standard applied to **the session's own capabilities** — the same
error as the 2026-09-03 Asset session declaring "no code access" from a working-tree search.
Recorded as `RE-P03-18`.
