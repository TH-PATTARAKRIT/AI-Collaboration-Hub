#!/usr/bin/env python3
"""P08 RC-05 confirmation — module install-state reader.

>>> NEW INSTRUMENT. Frozen in the SAME commit as the pre-run prediction, before it was
>>> executed even once. Required by the one-prompt closure prompt §7 (P08-C3): "If the
>>> instrument changes, freeze that changed instrument together with the pre-run
>>> prediction and disclose the delta."

DELTA vs rc05_balance.py: this reads ir_module_module, not the ledger tables. It shares
rc05_balance.py's two load-bearing habits and nothing else:
  - columns are resolved BY NAME from each dump's own COPY header, never positionally,
    because the deployed generations (16.0 and 19.0) order columns differently;
  - it FAILS CLOSED (exit 3) when a required column or the table itself is absent, so an
    absent table can never be reported as an absent module.

WHY THAT SECOND POINT IS THE WHOLE INSTRUMENT
  The question "is module X installed in this database" has THREE answers, and the naive
  one collapses two of them:
      installed        a row exists with state='installed'
      not installed    a row exists with a different state (uninstalled/to install/...)
      NOT PRESENT      no row at all — the module was never known to this database
  Reporting "not installed" for the third case is the defect class this instrument
  exists to avoid. All three are printed distinctly.

POPULATION   every row of ir_module_module in the named extract.
UNIT         one module row. NOT one addon directory, NOT one manifest.
SCOPE        install state as recorded in the database extract. This is what the
             DEPLOYMENT believed, which is the only authority for an install-state
             claim. It says nothing about whether the code was ever executed.

EXIT CODES  0 measured · 2 bad invocation/missing tool · 3 fail-closed (schema/table)
"""
import argparse, os, re, subprocess, sys


def die(msg, code=3):
    print("FAIL-CLOSED: " + msg, file=sys.stderr)
    sys.exit(code)


def stream_table(dump, table):
    cmd = ["pg_restore", "--data-only", "--no-owner", "--table=" + table, "-f", "-", dump]
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                         text=True, encoding="utf-8", errors="replace", bufsize=1 << 20)
    cols, in_copy = None, False
    for line in p.stdout:
        if not in_copy:
            if line.startswith("COPY ") and (
                    "." + table + " " in line or line.startswith("COPY " + table + " ")):
                m = re.search(r"\((.*?)\)\s+FROM stdin", line)
                if not m:
                    die("COPY header for %s not parseable in %s" % (table, dump))
                cols = [c.strip() for c in m.group(1).split(",")]
                in_copy = True
            continue
        if line.startswith("\\."):
            break
        yield cols, line.rstrip("\n").split("\t")
    p.stdout.close()
    p.wait()
    if cols is None:
        die("no COPY block for table %s in %s (table absent or extract unreadable)"
            % (table, dump))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dumps", nargs="+", metavar="LABEL=PATH")
    ap.add_argument("--module", action="append", required=True,
                    help="module technical name to report; repeatable")
    a = ap.parse_args()

    if not any(os.access(os.path.join(p, "pg_restore"), os.X_OK)
               for p in os.environ.get("PATH", "").split(os.pathsep) if p):
        die("pg_restore not on PATH", 2)
    print("pg_restore: %s" % subprocess.run(["pg_restore", "--version"],
          capture_output=True, text=True).stdout.strip())
    print("python:     %s\n" % sys.version.split()[0])

    for spec in a.dumps:
        if "=" not in spec:
            die("expected LABEL=PATH, got %r" % spec, 2)
        label, path = spec.split("=", 1)
        if not os.path.isfile(path):
            die("input not found: %s" % path, 2)

        idx, rows, total, installed_total = None, {}, 0, 0
        for cols, r in stream_table(path, "ir_module_module"):
            if idx is None:
                for c in ("name", "state"):
                    if c not in cols:
                        die("ir_module_module lacks required column %r in %s" % (c, path))
                idx = (cols.index("name"), cols.index("state"))
            total += 1
            nm, st = r[idx[0]], r[idx[1]]
            if st == "installed":
                installed_total += 1
            if nm in a.module:
                rows[nm] = st

        print("=" * 78)
        print("DATABASE %s   %s" % (label, os.path.basename(path)))
        print("=" * 78)
        print("  ir_module_module rows              %d" % total)
        print("  of which state='installed'         %d   <-- POSITIVE CONTROL" % installed_total)
        for m in a.module:
            if m not in rows:
                print("  %-34s NOT PRESENT  (no row — never known to this database)" % m)
            else:
                print("  %-34s state=%s" % (m, rows[m]))
        print()


if __name__ == "__main__":
    main()
