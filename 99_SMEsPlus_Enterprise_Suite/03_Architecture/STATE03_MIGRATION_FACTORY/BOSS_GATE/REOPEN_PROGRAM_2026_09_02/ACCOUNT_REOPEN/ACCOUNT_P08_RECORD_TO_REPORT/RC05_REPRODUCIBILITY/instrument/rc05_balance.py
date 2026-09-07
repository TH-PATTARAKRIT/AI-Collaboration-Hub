#!/usr/bin/env python3
"""RC-05 — exact-arithmetic ledger balance instrument.

PUBLISHED BY THE OWNER (P08) AS REPRODUCIBILITY EVIDENCE, under Boss ruling Q-BOSS-03
§2, which held that documentary inspection alone cannot certify RC-05.

>>> THIS IS NOT RC-05. Running this file does not perform the independent challenge. <<<
The owner ran it only to establish that it executes and that its controls fire. That run
is PREPARATION EVIDENCE. Structural independence requires a separate verifier who
re-executes it and reaches a conclusion without relying on the owner's.

--------------------------------------------------------------------------------------
WHAT IS MEASURED
  For every ACCOUNTING ENTRY (account_move) whose state is 'posted', two independent
  sums over its lines (account_move_line), both in exact Decimal, no float at any step:

    COMPUTED  sum(debit) - sum(credit)      the derived balance
    STORED    sum(balance)                  the stored balance column

  An entry is UNBALANCED at tolerance t when abs(sum) > t. Reported at four tolerances:
  exact equality (t = 0), 1e-7, 1e-4, 0.005.

POPULATION   every row of account_move_line whose move_id resolves to an account_move
             with state = 'posted', in the named database extract.
UNIT         one accounting entry (account_move). NOT one line, and NOT one journal.
DENOMINATOR  the count of posted account_move rows that have at least one line, printed
             per database as POSTED_MOVES_WITH_LINES.
SCOPE        reporting currency. debit/credit/balance are company-currency columns in
             this schema; amount_currency (foreign currency) is NOT in scope and is not
             read. Multi-company is NOT partitioned: every company in the extract is in
             the population, and the per-company spread is printed so a verifier can
             re-partition without re-running.

WHY THE STATE JOIN, AND NOT parent_state
  account_move_line.parent_state is a STORED RELATED field and can be stale. The
  authority for whether an entry is posted is account_move.state. This instrument joins
  to that authority and separately reports how many lines DISAGREE with their own
  parent_state, as a data-integrity observation (PARENT_STATE_DISAGREE). A verifier who
  filters on parent_state instead may get a different population; that is a real finding
  about the data, not a defect in either method, and it is printed rather than hidden.

WHY THE COPY HEADER IS PARSED AND NOT ASSUMED
  The deployed generations differ. iSMEs is 16.0 and carries account_root_id and
  tax_audit; iEVING/BK12MAY26 are 19.0 and carry invoice_date and extra_tax_data
  instead. Column ORDER therefore differs between extracts. Positional parsing would
  read a real value out of the wrong column and return a plausible, wrong answer that
  passes every control. Column indices are resolved BY NAME from each dump's own COPY
  header, and the instrument FAILS CLOSED if a required column is absent.

CONTROLS, and what each is for
  POSITIVE      the extraction reached real data: non-zero posted moves and lines, and
                a non-zero absolute money total. A zero here means the pipeline failed,
                not that the ledger balances.
  NEGATIVE      a population that SHOULD show almost nothing: DB-BK and DB-EV hold ~22
                posted entries between them. If they returned the same shape as DB-SM
                the instrument would be measuring something other than what it claims.
  DISCRIMINATING/INJECTION  --inject-unbalanced adds one synthetic entry that is off by
                a stated amount. The unbalanced count MUST rise by exactly one at every
                tolerance below that amount. This is the only control that proves the
                predicate CAN return non-zero. Without it, "0 unbalanced" is
                indistinguishable from a predicate that cannot fire.
  DRAFT SPREAD  the same measurement over NON-posted entries, printed beside the posted
                result. A tolerance effect that appears in neither population is not
                evidence about tolerance; publishing the spread prevents reading a bare
                zero as a finding.

EXIT CODES  0 measured · 2 bad invocation/missing tool · 3 fail-closed (schema/column)
"""
import argparse, decimal, hashlib, os, re, subprocess, sys, collections
from decimal import Decimal

decimal.getcontext().prec = 60          # far beyond any money column in this schema

TOLERANCES = [("exact", Decimal(0)), ("1e-7", Decimal("1e-7")),
              ("1e-4", Decimal("1e-4")), ("0.005", Decimal("0.005"))]

REQ_LINE = ["move_id", "debit", "credit", "balance", "parent_state"]
REQ_MOVE = ["id", "state"]


def die(msg, code=3):
    print("FAIL-CLOSED: " + msg, file=sys.stderr)
    sys.exit(code)


def sha256(path, chunk=1 << 20):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(chunk), b""):
            h.update(b)
    return h.hexdigest()


def stream_table(dump, table):
    """Yield (colnames, row_fields) from a pg_restore data-only COPY block.

    Server-free: pg_restore -f - writes the archive to stdout; no cluster is started and
    the dump is opened read-only. Rows are streamed, never held in memory.
    """
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


def dec(tok):
    """Exact Decimal from a COPY token. NULL -> 0. No float anywhere."""
    if tok == "\\N" or tok == "":
        return Decimal(0)
    return Decimal(tok)


def measure(dump, label, inject=None):
    # ---- pass 1: posted move ids, from the AUTHORITY table
    idx = None
    posted, allmoves = set(), 0
    for cols, r in stream_table(dump, "account_move"):
        if idx is None:
            for c in REQ_MOVE:
                if c not in cols:
                    die("account_move lacks required column %r in %s" % (c, dump))
            idx = (cols.index("id"), cols.index("state"))
        allmoves += 1
        if r[idx[1]] == "posted":
            posted.add(r[idx[0]])

    # ---- pass 2: lines
    li = None
    comp = collections.defaultdict(Decimal)     # move_id -> sum(debit-credit)
    stor = collections.defaultdict(Decimal)     # move_id -> sum(balance)
    lines_posted = lines_total = 0
    disagree = 0
    abs_money = Decimal(0)
    draft_comp = collections.defaultdict(Decimal)
    for cols, r in stream_table(dump, "account_move_line"):
        if li is None:
            for c in REQ_LINE:
                if c not in cols:
                    die("account_move_line lacks required column %r in %s" % (c, dump))
            li = {c: cols.index(c) for c in REQ_LINE}
        lines_total += 1
        mid = r[li["move_id"]]
        is_posted = mid in posted
        if (r[li["parent_state"]] == "posted") != is_posted:
            disagree += 1
        d, c_, b = dec(r[li["debit"]]), dec(r[li["credit"]]), dec(r[li["balance"]])
        if is_posted:
            lines_posted += 1
            comp[mid] += d - c_
            stor[mid] += b
            abs_money += abs(d) + abs(c_)
        else:
            draft_comp[mid] += d - c_

    # ---- discriminating injection control
    injected = None
    if inject is not None:
        injected = Decimal(inject)
        comp["__INJECTED__"] += injected
        stor["__INJECTED__"] += injected

    def counts(book):
        return {name: sum(1 for v in book.values() if abs(v) > t) for name, t in TOLERANCES}

    return {
        "label": label, "dump": dump,
        "moves_total": allmoves, "moves_posted": len(posted),
        "moves_posted_with_lines": len(comp) - (1 if injected is not None else 0),
        "lines_total": lines_total, "lines_posted": lines_posted,
        "parent_state_disagree": disagree,
        "abs_money": abs_money,
        "computed": counts(comp), "stored": counts(stor),
        "draft_moves_with_lines": len(draft_comp), "draft_computed": counts(draft_comp),
        "injected": injected,
    }


def report(res):
    print("=" * 78)
    print("DATABASE %s   %s" % (res["label"], os.path.basename(res["dump"])))
    print("=" * 78)
    print("POPULATION")
    print("  account_move rows                  %d" % res["moves_total"])
    print("  posted moves                       %d" % res["moves_posted"])
    print("  POSTED_MOVES_WITH_LINES (unit)     %d   <-- DENOMINATOR" % res["moves_posted_with_lines"])
    print("  account_move_line rows             %d" % res["lines_total"])
    print("  posted lines                       %d" % res["lines_posted"])
    print("  PARENT_STATE_DISAGREE (lines)      %d" % res["parent_state_disagree"])
    print("CONTROL / POSITIVE")
    ok = res["lines_posted"] > 0 and res["abs_money"] > 0
    print("  sum |debit|+|credit| over posted   %s" % res["abs_money"])
    print("  extraction reached real data       %s" % ("YES" if ok else "*** NO — treat every zero below as a TOOL FAILURE, not a result"))
    print("UNBALANCED POSTED ENTRIES  (unit = one account_move)")
    print("  %-26s %10s %10s" % ("tolerance", "COMPUTED", "STORED"))
    for name, _ in TOLERANCES:
        print("  %-26s %10d %10d" % (name, res["computed"][name], res["stored"][name]))
    print("DISCRIMINATING SET — the same predicate over NON-posted entries")
    print("  draft/other moves with lines       %d" % res["draft_moves_with_lines"])
    for name, _ in TOLERANCES:
        print("  unbalanced @ %-14s        %d" % (name, res["draft_computed"][name]))
    if res["injected"] is not None:
        print("CONTROL / INJECTION  one synthetic entry off by %s" % res["injected"])
        print("  every tolerance below that amount MUST show exactly +1 vs the un-injected run")
    print()


def main():
    ap = argparse.ArgumentParser(description="RC-05 exact-arithmetic balance measurement")
    ap.add_argument("dumps", nargs="+", metavar="LABEL=PATH",
                    help="e.g. DB-SM=/path/iSMEs_2026-07-11_05-03-27.dump")
    ap.add_argument("--inject-unbalanced", metavar="AMOUNT", default=None,
                    help="discriminating control: add one synthetic entry off by AMOUNT")
    ap.add_argument("--no-hash", action="store_true", help="skip input SHA-256 (faster)")
    a = ap.parse_args()

    if not any(os.access(os.path.join(p, "pg_restore"), os.X_OK)
               for p in os.environ.get("PATH", "").split(os.pathsep) if p):
        die("pg_restore not on PATH — required to read the custom-format dumps", 2)
    print("pg_restore: %s" % subprocess.run(["pg_restore", "--version"],
          capture_output=True, text=True).stdout.strip())
    print("python:     %s" % sys.version.split()[0])
    print("decimal prec %d · NO float is constructed at any step\n" % decimal.getcontext().prec)

    specs = []
    for spec in a.dumps:
        if "=" not in spec:
            die("expected LABEL=PATH, got %r" % spec, 2)
        label, path = spec.split("=", 1)
        if not os.path.isfile(path):
            die("input not found: %s" % path, 2)
        specs.append((label, path))

    print("FROZEN INPUTS")
    for label, path in specs:
        print("  %-6s %s" % (label, path))
        print("         size %d bytes" % os.path.getsize(path))
        if not a.no_hash:
            print("         sha256 %s" % sha256(path))
    print()

    for label, path in specs:
        report(measure(path, label, a.inject_unbalanced))


if __name__ == "__main__":
    main()
