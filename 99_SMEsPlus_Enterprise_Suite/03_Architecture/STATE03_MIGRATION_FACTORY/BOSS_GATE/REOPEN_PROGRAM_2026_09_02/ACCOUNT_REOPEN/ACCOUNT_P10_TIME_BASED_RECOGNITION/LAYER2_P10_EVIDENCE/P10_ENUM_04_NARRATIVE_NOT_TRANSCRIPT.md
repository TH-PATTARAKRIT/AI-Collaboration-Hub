P10-ENUM-04  DEPLOYED LOCK DATES AND ASSET SCHEDULES   (executed 2026-09-05)

WHY THIS EXISTS: P10-ENUM-03 extracted the company table from every archive and
reported only its byte size. The lock-date columns were inside those artefacts
and were never printed. This run prints them.

TOOL: /opt/homebrew/Cellar/postgresql@18/18.6/bin/pg_restore  (already installed)
      -- the earlier run used the default-path binary only, and inferred from its
         error message that archive D was unreadable. It is not.

=== ARCHIVE D REOPENED ===
  pg_restore -l iTEST02_2026-07-14_16-34-51.dump
    Archive created 2026-07-14 ; dbname iTEST02 ; TOC Entries 26804
  schema extract: 6198023 bytes

=== LOCK DATES (positive control: sibling columns populated in the same rows) ===
A  BK12MAY26  res_company columns=195 rows=44 | schema 4323210 B | data 1612691 B
     fiscalyear_lock_date  set in  0 of 44
     tax_lock_date         set in  0 of 44
     sale_lock_date        set in  0 of 44
     purchase_lock_date    set in  0 of 44
     hard_lock_date        set in  0 of 44
B  iEVING     res_company columns=188 rows=44 | schema 4250585 B | data 1459141 B
     all five lock columns  set in  0 of 44
D  iTEST02    res_company columns=263 rows=1  | schema 6198023 B | data  18062 B
     fiscalyear_lock_date  set in  1 of 1   value 2026-02-28
     tax_lock_date         set in  1 of 1   value 2026-02-28
     sale_lock_date        set in  1 of 1   value 2026-02-28
     purchase_lock_date    set in  1 of 1   value 2026-02-28
     hard_lock_date        set in  0 of 1

  -> The silent re-date CANNOT fire in A or B: there is no lock to violate.
     It CAN fire in D, the archive the earlier run declared unreadable.

=== ASSET SCHEDULES (artefact bytes printed beside every count) ===
A  account_asset rows= 36  (artefact   9173 B)
B  account_asset rows= 36  (artefact   9173 B)
C  account_asset rows=685  (artefact 211809 B)
D  account_asset rows= 12  (artefact   4083 B)
  TOTAL 769 asset schedules across the estate.
  -> The class-A claim "no DEFERRAL entry has ever been generated" is correct.
     Its restatement as "zero RECOGNITION entries" was false.

=== DEFERRAL ENTRIES ===
D  account_move_deferred_rel rows=0  (artefact 913 B = header only)
  -> consistent with A and B (886 B each). Zero in every archive carrying the
     structure. C has no such structure at all.

=== DECLARED LIMITATION OF THIS RUN ===
Population still NOT enumerated. This run, like ENUM-03, covers only
$HOME/Downloads/*.dump. At least three further deployed-database artefacts are
known to exist elsewhere on the volume and were NOT read.  Class C.
