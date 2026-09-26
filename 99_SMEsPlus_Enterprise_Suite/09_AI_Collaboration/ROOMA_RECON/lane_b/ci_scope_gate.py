#!/usr/bin/env python3
"""
LANE B — CI SCOPE GATE  v1.00
SMEsPlus Enterprise Suite · ROOM A

Enforces, by machine, the three rules that the charter states in words:

  J1-a  a NEXT_PHASE module may never be the subject of a record
  J1-b  SCOPE_UNCERTAIN must carry a SCOPE_NOTE
  J1-c  the join key MODULE + QID must be present and well formed

A rule that cannot be enforced is not a rule; it is a request.

Usage:
    python3 ci_scope_gate.py records.yaml [more.yaml ...]

Exit codes:
    0  all records pass
    1  at least one record rejected
    2  the gate could not run (missing scope list, unreadable input)
"""

import sys, os, re, csv

HERE = os.path.dirname(os.path.abspath(__file__))
SCOPE_TSV = os.path.join(HERE, "SCOPE_LIST_V2.01.tsv")
SCOPE_TSV_SHA256 = "f748eee0dcee533c765de7becddfbb5f550f1681edb9a0b00c8ba28cff9690c7"

QID_RE = re.compile(r"^(STD-Q\d{2}|G\d{2}-[A-Z0-9_]+-Q\d+)$")


def load_scope():
    if not os.path.exists(SCOPE_TSV):
        sys.exit(f"GATE ABORT: {SCOPE_TSV} not found. Cannot verify scope. (exit 2)")
    import hashlib
    got = hashlib.sha256(open(SCOPE_TSV, "rb").read()).hexdigest()
    if got != SCOPE_TSV_SHA256:
        sys.exit(f"GATE ABORT: scope list hash mismatch.\n  expected {SCOPE_TSV_SHA256}\n  got      {got}\n"
                 "The scope list was altered. Stop and report a control finding. (exit 2)")
    current, deferred = set(), set()
    with open(SCOPE_TSV, newline="") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            (current if row["phase"] == "CURRENT_STUDY" else deferred).add(row["module"])
    return current, deferred


def load_records(path):
    """Minimal YAML list reader — no dependency on PyYAML.
    Accepts the charter §5 record shape: a list of '- KEY: value' blocks."""
    try:
        import yaml
        with open(path) as fh:
            return yaml.safe_load(fh) or []
    except ImportError:
        recs, cur = [], None
        for raw in open(path):
            line = raw.rstrip("\n")
            if not line.strip() or line.lstrip().startswith("#"):
                continue
            m = re.match(r"^-\s+([A-Z_]+):\s*(.*)$", line)
            if m:
                if cur:
                    recs.append(cur)
                cur = {m.group(1): m.group(2).strip()}
                continue
            m = re.match(r"^\s{2,}([A-Z_]+):\s*(.*)$", line)
            if m and cur is not None:
                cur[m.group(1)] = m.group(2).strip()
        if cur:
            recs.append(cur)
        return recs


def truthy(v):
    return str(v).strip().lower() in ("true", "yes", "1")


def check(rec, idx, current, deferred):
    """Return a list of rejection reasons for one record."""
    out = []
    oid = rec.get("OBS_ID") or f"<record #{idx}>"
    mod = (rec.get("MODULE") or "").strip()
    qid = (rec.get("QID") or "").strip()

    # --- join key ---
    if not mod:
        out.append(f"{oid}: MODULE is missing — the record cannot be reconciled.")
    if not qid:
        out.append(f"{oid}: QID is missing — the record answers no frozen question.")
    elif not QID_RE.match(qid):
        out.append(f"{oid}: QID '{qid}' is malformed. Expected STD-Qnn or Gnn-MODULE-Qn.")

    # --- J1-a  scope ---
    if mod:
        if mod in deferred:
            out.append(f"{oid}: MODULE '{mod}' is NEXT_PHASE. "
                       "A deferred module may never be the subject of a record (charter §3A J1-a).")
        elif mod not in current:
            out.append(f"{oid}: MODULE '{mod}' is not in the frozen scope list at all. "
                       "Either the module name is wrong or the runtime changed — escalate, do not guess.")

    # --- J1-b  scope uncertainty ---
    if truthy(rec.get("SCOPE_UNCERTAIN", "false")):
        if not (rec.get("SCOPE_NOTE") or "").strip():
            out.append(f"{oid}: SCOPE_UNCERTAIN is true but SCOPE_NOTE is empty (charter §3A J1-b). "
                       "State what was observed and what could not be determined.")

    # --- charter invariants worth catching here rather than at the ROOM B gate ---
    if not (rec.get("BUSINESS_STATEMENT") or "").strip():
        out.append(f"{oid}: BUSINESS_STATEMENT is empty — nothing travels to the Reconciler.")
    if not (rec.get("EVIDENCE_ARTIFACT") or "").strip():
        out.append(f"{oid}: EVIDENCE_ARTIFACT is empty. No artifact, no record.")
    tier = (rec.get("EVIDENCE_TIER") or "").strip()
    if tier and tier != "OBSERVED":
        out.append(f"{oid}: EVIDENCE_TIER is '{tier}'. Lane B may only write OBSERVED.")
    return out


def main(argv):
    if len(argv) < 2:
        sys.exit("usage: ci_scope_gate.py records.yaml [more.yaml ...]   (exit 2)")
    current, deferred = load_scope()
    total, rejected, reasons = 0, 0, []

    for path in argv[1:]:
        if not os.path.exists(path):
            sys.exit(f"GATE ABORT: {path} not found. (exit 2)")
        for i, rec in enumerate(load_records(path), 1):
            if not isinstance(rec, dict):
                continue
            total += 1
            bad = check(rec, i, current, deferred)
            if bad:
                rejected += 1
                reasons.extend(f"  [{os.path.basename(path)}] {r}" for r in bad)

    print("LANE B CI SCOPE GATE v1.00")
    print(f"  scope list       : {os.path.basename(SCOPE_TSV)} (hash verified)")
    print(f"  in scope         : {len(current)} modules")
    print(f"  deferred         : {len(deferred)} modules")
    print(f"  records checked  : {total}")
    print(f"  records rejected : {rejected}")
    if reasons:
        print("\nREJECTIONS")
        for r in reasons:
            print(r)
        print("\nRESULT: FAIL — fix every rejection above. Nothing in this batch is accepted.")
        return 1
    print("\nRESULT: PASS — every record names an in-scope module and a frozen question.")
    print("This gate checks scope and form only. It does not verify that the observation is true.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
