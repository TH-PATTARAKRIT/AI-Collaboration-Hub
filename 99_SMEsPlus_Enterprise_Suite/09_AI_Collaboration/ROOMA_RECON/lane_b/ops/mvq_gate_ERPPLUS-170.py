#!/usr/bin/env python3
"""
RED TEAM ACCEPTANCE GATE - module question set (MVQ)
Enforces BOSSDEC / Jira ERPPLUS-170, 2026-09-26.

Mechanical only. This tool NEVER authors a question and NEVER judges whether a
question is a good idea - it decides only whether a drafted set is admissible.
Authoring belongs to OVQDT. Approval belongs to Boss.

Usage:  python3 ops/mvq_gate_ERPPLUS-170.py <MVQ_file.md|.yaml> [--json]
Exit 0 = ADMISSIBLE   Exit 1 = REJECTED
"""
import sys, re, json, hashlib, unicodedata, collections

PRIMARY_MIN, RESERVE_MIN = 40, 8
DRAFT_BAND = (50, 52)
REQUIRED = ["HYPOTHESIS", "RATIONALE", "PRECONDITIONS",
            "EXPECTED_EVIDENCE", "DISCONFIRMING_OBSERVATION"]
# a question that reveals an identifier tells the blind lane the answer
VOCAB = re.compile(r"\b(res\.\w+|ir\.\w+|account\.\w+|stock\.\w+|uom\.\w+|"
                   r"sale\.\w+|purchase\.\w+|mrp\.\w+|\w+_id\b|\w+_ids\b|"
                   r"odoo|Odoo|__manifest__|xmlrpc|psql|postgres)\b")

def norm(s):
    s = unicodedata.normalize("NFKC", s or "").lower()
    s = re.sub(r"[^\w฀-๿]+", " ", s)
    return " ".join(s.split())

def parse(path):
    raw = open(path, encoding="utf-8").read()
    chunks = re.split(r"\n(?=\s*(?:-\s*)?(?:QID|ID)\s*:)", raw)
    out = []
    for c in chunks:
        m = re.search(r"(?:QID|ID)\s*:\s*([\w\-\.]+)", c)
        if not m:
            continue
        q = {"QID": m.group(1), "_raw": c}
        for k in REQUIRED + ["CLASS", "QUESTION", "NEW_RISK", "LAYER"]:
            mm = re.search(rf"^\s*(?:-\s*)?{k}\s*:\s*(.+?)\s*$", c, re.M | re.I)
            if mm:
                q[k] = mm.group(1).strip().strip('"')
        out.append(q)
    return out

def gate(path):
    qs = parse(path)
    f = []                                    # findings
    if not qs:
        return qs, [("STRUCTURE", "no questions parsed - check file format")]

    dup = [q for q, c in collections.Counter(x["QID"] for x in qs).items() if c > 1]
    if dup:
        f.append(("STRUCTURE", f"duplicate QID: {dup}"))

    prim = [q for q in qs if (q.get("CLASS", "PRIMARY")).upper().startswith("PRIM")]
    resv = [q for q in qs if (q.get("CLASS", "")).upper().startswith("RES")]
    if len(prim) < PRIMARY_MIN:
        f.append(("COUNT", f"Primary {len(prim)} < {PRIMARY_MIN}"))
    if len(resv) < RESERVE_MIN:
        f.append(("COUNT", f"Reserve {len(resv)} < {RESERVE_MIN}"))

    total = len(qs)
    if total > DRAFT_BAND[1]:
        unjust = [q["QID"] for q in qs if not q.get("NEW_RISK")]
        over = total - DRAFT_BAND[1]
        if len(qs) - len([q for q in qs if q.get("NEW_RISK")]) > DRAFT_BAND[1]:
            f.append(("COUNT", f"{total} questions exceeds {DRAFT_BAND[1]}; "
                               f"{over} need a NEW_RISK justification, "
                               f"{len(unjust)} carry none"))

    for q in qs:                              # 5 mandatory fields
        for k in REQUIRED:
            if not q.get(k):
                f.append(("FIELD", f"{q['QID']} missing {k}"))

    for q in qs:                              # vocabulary leak
        text = " ".join(str(q.get(k, "")) for k in ("QUESTION", "HYPOTHESIS"))
        hit = set(VOCAB.findall(text))
        if hit:
            f.append(("VOCAB", f"{q['QID']} reveals identifier(s): {sorted(hit)}"))

    # semantic duplication: two questions checking the same thing share a
    # disconfirming observation. This is the objective yardstick for
    # "reworded but tests the same thing - does not count as a new question".
    seen = {}
    for q in qs:
        k = hashlib.sha256(norm(q.get("DISCONFIRMING_OBSERVATION", "")).encode()).hexdigest()[:16]
        if q.get("DISCONFIRMING_OBSERVATION"):
            if k in seen:
                f.append(("DEDUP", f"{q['QID']} duplicates {seen[k]} - same "
                                   f"DISCONFIRMING_OBSERVATION, does not count as a new question"))
            else:
                seen[k] = q["QID"]

    # a disconfirming observation that cannot fail is padding
    for q in qs:
        d = norm(q.get("DISCONFIRMING_OBSERVATION", ""))
        thai = bool(re.search(r"[\u0e00-\u0e7f]", d))
        too_short = (len(d) < 25) if thai else (len(d.split()) < 5)
        if d and (too_short or d in ("n a", "none", "tbd", "pending")):
            f.append(("PADDING", f"{q['QID']} DISCONFIRMING_OBSERVATION is not a "
                                 f"concrete falsifiable result"))
    return qs, f

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    qs, f = gate(sys.argv[1])
    prim = sum(1 for q in qs if (q.get("CLASS", "PRIMARY")).upper().startswith("PRIM"))
    resv = sum(1 for q in qs if (q.get("CLASS", "")).upper().startswith("RES"))
    by = collections.Counter(c for c, _ in f)
    if "--json" in sys.argv:
        print(json.dumps({"file": sys.argv[1], "total": len(qs), "primary": prim,
                          "reserve": resv, "findings": [{"type": c, "detail": d} for c, d in f],
                          "verdict": "ADMISSIBLE" if not f else "REJECTED"}, indent=2, ensure_ascii=False))
    else:
        print(f"file     : {sys.argv[1]}")
        print(f"questions: {len(qs)}   Primary {prim} (min {PRIMARY_MIN})   "
              f"Reserve {resv} (min {RESERVE_MIN})   draft band {DRAFT_BAND[0]}-{DRAFT_BAND[1]}")
        if f:
            print(f"\nFINDINGS ({len(f)}): " + ", ".join(f"{k}={v}" for k, v in sorted(by.items())))
            for c, d in f:
                print(f"  [{c:9}] {d}")
        print("\nVERDICT  : " + ("ADMISSIBLE - ready for Boss decision" if not f
                                 else "REJECTED - return to OVQDT"))
        print("This is a RED TEAM admissibility result only. It is not Boss approval.")
    sys.exit(0 if not f else 1)
