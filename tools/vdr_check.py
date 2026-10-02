#!/usr/bin/env python3
"""STATE03 VDR CANDIDATE PORTABLE GATE (not accepted by Boss).

Usage:
    python3 -B tools/vdr_check.py --read-only <restricted.md> <neutral.md> [<handoff_packet.json>]

Paths are repository-relative (or absolute inside this repository). Rules are
taken from 00_CONTROL/WORKER_SPEC_L2_L3.md section 3.1 (claim table), 3.2
(neutral file), section 4 (gate checks) and the B02 handoff rules (CPM-01 unit
key, CPM-03 gate status/result form).

Contract:
  * Read-only: no file writes, deletes, redirects, commits, pushes or network.
    The only child processes are read-only git plumbing calls
    (ls-files, hash-object without -w, rev-parse) with GIT_OPTIONAL_LOCKS=0.
  * Deterministic: no timestamps, sorted output, single JSON document on stdout.
  * Source pointers are verified only against git-tracked, unmodified files of
    an approved source root. A Unit with zero canonical claims FAILs.
  * Until Boss accepts this gate (ACCEPTED = False) every result is reported as
    formal_result "NOT PROVEN / NON-FORMAL". It never creates a Gate PASS,
    Formal Coverage, or STATE03 status.

Exit codes: 0 candidate PASS, 1 candidate FAIL, 3 NOT PROVEN (blocked), 2 usage.
"""
import json
import os
import re
import subprocess
import sys

sys.dont_write_bytecode = True

GATE_ID = "tools/vdr_check.py"
GATE_STATUS = "CANDIDATE PORTABLE GATE — NOT ACCEPTED"
ACCEPTED = False
REPO = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
VDR_REL = ("99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/"
           "TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3")
FIXTURE_REL = "tools/vdr_gate_fixtures"

# Evidence root -> (source root, Function-ID index, blocker when source is unavailable).
# The Odoo 19 Community tree is not a git checkout (SOURCE_TREE_PROVENANCE_OBSERVATIONS
# SP-02); Boss rule: source access only via a dedicated git-tracked STATE03 read-only
# worktree. Until one is registered here, Odoo pointers cannot be verified.
EVIDENCE_ROOTS = (
    (FIXTURE_REL, FIXTURE_REL + "/source", FIXTURE_REL + "/00_CONTROL/FUNCTION_ID_INDEX.json", None),
    (VDR_REL, None, VDR_REL + "/00_CONTROL/EXISTING_FUNCTION_ID_INDEX_53.json",
     "Odoo source not available as a git-tracked STATE03 read-only worktree (SP-02)"),
    ("", None, VDR_REL + "/00_CONTROL/EXISTING_FUNCTION_ID_INDEX_53.json",
     "Odoo source not available as a git-tracked STATE03 read-only worktree (SP-02)"),
)

BANNER = "RESTRICTED — TECHNICAL EVIDENCE — NOT FOR NEUTRAL DISTRIBUTION"
NEUTRAL_SECTIONS = ("WHAT", "WHY", "BUSINESS RULE", "STATE", "OPTIONALITY",
                    "DEPENDENCY", "CONSTRAINT", "RISK", "UNKNOWN")
CLASSES = ("FACT", "OBSERVATION", "INFERENCE", "UNKNOWN")
FLAG_TOKENS = ("RT", "CONTRA")
NO_FLAG = ("—", "-")
NO_FUNCTION = "FUNCTION MAPPING REQUIRED"
PACKET_STATUSES = ("GATE-PASS", "GATE-FAIL", "NOT PROVEN")
B02_MARKER = "DEEPSEEK-CORRECTED / PENDING STATE03 RE-VERIFICATION"
GATE_RESULT_RE = re.compile(
    r"^(NOT PROVEN|(PASS|FAIL) \(claim-checks=\d+, neutral-leak-tokens=\d+"
    r"(, structure-checks=\d+, packet-checks=\d+)?\))$")
UNIT_FILE_RE = re.compile(r"^(U\d{3,4})_")
POINTER_RE = re.compile(r"^([A-Za-z0-9_]+)/([A-Za-z0-9_./-]+):(\d+)$")
CELL_SPLIT_RE = re.compile(r"(?<!\\)\|")
EVIDENCE_REF_RE = re.compile(r"(01_RESTRICTED_TECHNICAL_EVIDENCE|02_NEUTRAL_KNOWLEDGE)/(U\d{3,4}[^/]*\.md)$")

# Neutral-file forbidden token detectors (WORKER_SPEC section 3.2).
LEAK_PATTERNS = (
    ("code/backtick", re.compile(r"`")),
    ("snake_case identifier", re.compile(r"\b[A-Za-z0-9]+(?:_[A-Za-z0-9]+)+\b")),
    ("dotted technical name", re.compile(r"\b[a-z][a-z0-9_]+(?:\.[a-z_][a-z0-9_]+)+\b")),
    ("file extension", re.compile(r"\w\.(?:py|xml|csv|js|json|sql|po|pot|scss|css|html|rng)\b")),
    ("path-like token", re.compile(r"\b[\w.-]+(?:/[\w.-]+){2,}")),
    ("line-number pointer", re.compile(r"[A-Za-z_]:\d+\b")),
    ("CamelCase class name", re.compile(r"\b[A-Z][a-z0-9]+(?:[A-Z][a-z0-9]+)+\b")),
    ("code keyword", re.compile(r"\bdef\s+\w+|\bself\.|\bsuper\(|\bclass\s+\w+\(|\bimport\s+\w+\.\w+")),
    ("SQL statement", re.compile(r"\b(?:SELECT|INSERT|UPDATE|DELETE)\b.*\b(?:FROM|INTO|SET)\b")),
)
VENDOR_RE = re.compile(r"\bOdoo\b")
VENDOR_HEADER_LINES = 10


def absolute(rel):
    return os.path.realpath(os.path.join(REPO, rel))


def inside(path, root):
    return path == root or path.startswith(root + os.sep)


def rel(path):
    return os.path.relpath(path, REPO)


def read_lines(path):
    with open(path, encoding="utf-8") as handle:
        return handle.read().splitlines()


def git(args):
    env = {"PATH": os.environ.get("PATH", ""), "GIT_OPTIONAL_LOCKS": "0", "LC_ALL": "C"}
    proc = subprocess.run(["git", "-C", REPO] + args, env=env, stdin=subprocess.DEVNULL,
                          capture_output=True, text=True, timeout=60, shell=False)
    return proc.returncode, proc.stdout.strip()


class SourceRoot:
    """Git-tracked, unmodified source files under one approved root."""

    def __init__(self, root_rel):
        self.root = absolute(root_rel)
        self.cache = {}

    def lines(self, module, path):
        key = (module, path)
        if key in self.cache:
            return self.cache[key]
        result = (None, "source file not found")
        full = os.path.realpath(os.path.join(self.root, module, path))
        if inside(full, self.root) and os.path.isfile(full):
            code, staged = git(["ls-files", "-s", "--", rel(full)])
            if code != 0 or not staged:
                result = (None, "source file not git-tracked")
            else:
                index_blob = staged.split()[1]
                code, work_blob = git(["hash-object", "--", rel(full)])
                if code != 0 or work_blob != index_blob:
                    result = (None, "source file modified against git index")
                else:
                    result = (read_lines(full), index_blob)
        self.cache[key] = result
        return result


def evidence_root(path):
    for root_rel, source_rel, index_rel, blocker in EVIDENCE_ROOTS:
        root = absolute(root_rel) if root_rel else REPO
        if inside(path, root):
            return root_rel, source_rel, index_rel, blocker
    return None


def function_ids(index_rel):
    path = absolute(index_rel)
    if not os.path.isfile(path):
        return None
    with open(path, encoding="utf-8") as handle:
        data = json.load(handle)
    return {item.get("id") for item in data if isinstance(item, dict)}


def parse_claims(unit, lines):
    """Return (claims, row_failures). Claim rows start with '| VDR-'."""
    claims, failures = [], []
    id_re = re.compile(r"^VDR-%s-C\d{3}$" % unit)
    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped.startswith("| VDR-"):
            continue
        cells = [c.strip() for c in CELL_SPLIT_RE.split(stripped.strip("|"))]
        if len(cells) != 9:
            failures.append({"line": number, "check": "row has %d columns (need 9)" % len(cells)})
            continue
        claim = dict(zip(("claim_id", "function_id", "pointer", "anchor", "class", "condition",
                          "flags", "statement", "neutral_ref"), cells))
        claim["line"] = number
        if not id_re.match(claim["claim_id"]):
            failures.append({"line": number, "check": "Claim-ID not VDR-%s-C###" % unit})
            continue
        claims.append(claim)
    return claims, failures


def check_claim(claim, unit, source, blocker, known_functions, neutral_ids):
    """Return (failures, blocked) for one claim."""
    failures = []
    fids = [f.strip() for f in claim["function_id"].split(",") if f.strip()]
    if not fids:
        failures.append("Function-ID empty")
    for fid in fids:
        if fid != NO_FUNCTION and (known_functions is None or fid not in known_functions):
            failures.append("Function-ID %s not in existing index" % fid)
    if claim["class"] not in CLASSES:
        failures.append("Class %r not in %s" % (claim["class"], "/".join(CLASSES)))
    if not claim["condition"]:
        failures.append("Condition empty")
    if not claim["statement"]:
        failures.append("Technical statement empty")
    flags = claim["flags"]
    if flags not in NO_FLAG:
        tokens = [t for t in re.split(r"[,/ ]+", flags) if t]
        if not tokens or any(t not in FLAG_TOKENS for t in tokens):
            failures.append("Flags %r not in RT/CONTRA/—" % flags)
    ref = claim["neutral_ref"]
    if not re.match(r"^N-%s-\d{3}$" % unit, ref):
        failures.append("Neutral-ref %r not N-%s-###" % (ref, unit))
    elif ref not in neutral_ids:
        failures.append("Neutral-ref %s missing from neutral file" % ref)

    anchor = claim["anchor"]
    if anchor.startswith("`") and anchor.endswith("`") and len(anchor) > 1:
        anchor = anchor[1:-1]
    if not anchor or len(anchor.split()) > 6:
        failures.append("Anchor empty or longer than 6 words")

    blocked = None
    if claim["class"] == "UNKNOWN" and claim["pointer"] in NO_FLAG:
        return failures, blocked
    match = POINTER_RE.match(claim["pointer"])
    if not match or ".." in match.group(2).split("/"):
        failures.append("Pointer %r not <module>/<relative path>:<line>" % claim["pointer"])
        return failures, blocked
    if source is None:
        return failures, blocker
    module, path, line_no = match.group(1), match.group(2), int(match.group(3))
    text, detail = source.lines(module, path)
    if text is None:
        failures.append("Pointer %s: %s" % (claim["pointer"], detail))
    elif line_no < 1 or line_no > len(text):
        failures.append("Pointer %s: line beyond end of file (%d lines)" % (claim["pointer"], len(text)))
    elif anchor and not any(anchor in text[i] for i in range(max(0, line_no - 4), min(len(text), line_no + 3))):
        failures.append("Anchor %r not within ±3 lines of %s" % (anchor, claim["pointer"]))
    return failures, blocked


def scan_neutral(unit, lines):
    leaks, structure = [], []
    ids = set(re.findall(r"\[(N-%s-\d{3})\]" % unit, "\n".join(lines)))
    foreign = sorted(set(re.findall(r"\[(N-U\d{3,4}-\d{3})\]", "\n".join(lines))) - ids)
    for tag in foreign:
        structure.append("neutral id %s belongs to another Unit" % tag)
    vendor_seen = 0
    for number, line in enumerate(lines, 1):
        for label, pattern in LEAK_PATTERNS:
            for match in pattern.finditer(line):
                leaks.append({"line": number, "type": label, "token": match.group(0)})
        for match in VENDOR_RE.finditer(line):
            vendor_seen += 1
            if number > VENDOR_HEADER_LINES or vendor_seen > 1:
                leaks.append({"line": number, "type": "vendor name outside header", "token": match.group(0)})
    headings = [l.lstrip("#").strip().upper() for l in lines if l.lstrip().startswith("#")]
    for section in NEUTRAL_SECTIONS:
        if not any(re.search(r"(^|[^A-Z])%s([^A-Z]|$)" % section, h) for h in headings):
            structure.append("neutral section heading %s missing" % section)
    return ids, leaks, structure


def check_packet(unit, path, restricted, neutral):
    failures = []
    try:
        with open(path, encoding="utf-8") as handle:
            packet = json.load(handle)
    except (ValueError, OSError) as exc:
        return ["packet not valid JSON: %s" % exc]
    if not isinstance(packet, dict):
        return ["packet is not a JSON object"]
    if packet.get("unit") != unit:
        failures.append("CPM-01: packet 'unit' is %r, expected %r" % (packet.get("unit"), unit))
    if "unit_id" in packet:
        failures.append("CPM-01: packet carries legacy 'unit_id' key")
    if packet.get("status") not in PACKET_STATUSES:
        failures.append("CPM-03: status %r not in %s" % (packet.get("status"), "/".join(PACKET_STATUSES)))
    gate_result = packet.get("gate_result")
    if not isinstance(gate_result, str) or not GATE_RESULT_RE.match(gate_result):
        failures.append("CPM-03: gate_result %r not in canonical form" % (gate_result,))
    if "b02_correction" in packet and packet.get("marker") != B02_MARKER:
        failures.append("B02: marker missing or not %r" % B02_MARKER)
    expected = {"01_RESTRICTED_TECHNICAL_EVIDENCE": os.path.basename(restricted),
                "02_NEUTRAL_KNOWLEDGE": os.path.basename(neutral)}
    stack = [packet]
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            stack.extend(node.values())
        elif isinstance(node, list):
            stack.extend(node)
        elif isinstance(node, str):
            match = EVIDENCE_REF_RE.search(node.strip())
            if match and match.group(2).startswith(unit + "_") and match.group(2) != expected[match.group(1)]:
                failures.append("packet references %s, gated file is %s"
                                % (match.group(0), expected[match.group(1)]))
    return sorted(set(failures))


def usage(message):
    print(json.dumps({"gate": GATE_ID, "error": message,
                      "usage": "vdr_check.py --read-only <restricted.md> <neutral.md> [<handoff_packet.json>]"},
                     sort_keys=True))
    return 2


def main(argv):
    args = argv[1:]
    if not args or args[0] != "--read-only":
        return usage("--read-only is required")
    paths = args[1:]
    if len(paths) not in (2, 3):
        return usage("expected 2 or 3 paths")
    resolved = []
    for value in paths:
        full = absolute(value) if not os.path.isabs(value) else os.path.realpath(value)
        if not inside(full, REPO) or not os.path.isfile(full):
            return usage("path not a file inside the repository: %s" % value)
        resolved.append(full)
    restricted, neutral = resolved[0], resolved[1]
    packet = resolved[2] if len(resolved) == 3 else None

    out = {"gate": GATE_ID, "gate_status": GATE_STATUS, "accepted": ACCEPTED,
           "inputs": {"restricted": rel(restricted), "neutral": rel(neutral),
                      "packet": rel(packet) if packet else None},
           "blockers": []}
    match = UNIT_FILE_RE.match(os.path.basename(restricted))
    unit = match.group(1) if match else None
    structure = []
    if not unit:
        structure.append("restricted file name does not start with U###_")
    for other in [p for p in (neutral, packet) if p]:
        if unit and not os.path.basename(other).startswith(unit + "_"):
            structure.append("%s does not belong to %s" % (os.path.basename(other), unit))
    if not os.path.basename(neutral).endswith("_NEUTRAL.md"):
        structure.append("neutral file name does not end with _NEUTRAL.md")
    out["unit"] = unit

    roots = evidence_root(restricted), evidence_root(neutral)
    if roots[0] is None or roots[0] != roots[1]:
        structure.append("restricted and neutral files are not under the same approved evidence root")
    root_rel, source_rel, index_rel, source_blocker = roots[0] or (None, None, None, "no approved root")
    out["source_root"] = source_rel
    source = None
    if source_rel:
        source = SourceRoot(source_rel)
        code, head = git(["rev-parse", "HEAD"])
        out["source_revision"] = {"repository_head": head if code == 0 else None,
                                  "note": "pointer files verified against the git index blob"}
    else:
        out["source_revision"] = None

    restricted_lines = read_lines(restricted)
    neutral_lines = read_lines(neutral)
    if not any(BANNER in line for line in restricted_lines[:15]):
        structure.append("restricted banner missing from header")

    neutral_ids, leaks, neutral_structure = scan_neutral(unit or "U0000", neutral_lines)
    structure.extend(neutral_structure)
    claims, row_failures = parse_claims(unit or "U0000", restricted_lines)
    if not claims:
        structure.append("zero canonical VDR-%s-C### claims" % (unit or "U###"))
    seen, claim_failures, blocked = {}, list(row_failures), set()
    known = function_ids(index_rel) if index_rel else None
    for claim in claims:
        failures, claim_blocked = check_claim(claim, unit, source, source_blocker, known, neutral_ids)
        if claim["claim_id"] in seen:
            failures.append("duplicate Claim-ID (first at line %d)" % seen[claim["claim_id"]])
        seen.setdefault(claim["claim_id"], claim["line"])
        for failure in failures:
            claim_failures.append({"line": claim["line"], "claim_id": claim["claim_id"], "check": failure})
        if claim_blocked:
            blocked.add(claim_blocked)
    packet_failures = check_packet(unit, packet, restricted, neutral) if packet and unit else []

    for reason in sorted(blocked):
        out["blockers"].append(reason)
    counts = {"claims": len(claims),
              "claims_by_class": {c: sum(1 for x in claims if x["class"] == c) for c in CLASSES},
              "neutral_ids": len(neutral_ids),
              "claim_check_failures": len(claim_failures),
              "neutral_leak_tokens": len(leaks),
              "structure_check_failures": len(structure),
              "packet_check_failures": len(packet_failures),
              "claims_pointer_unverified": sum(1 for c in claims if source is None
                                                and not (c["class"] == "UNKNOWN" and c["pointer"] in NO_FLAG))}
    failed = any(counts[k] for k in ("claim_check_failures", "neutral_leak_tokens",
                                     "structure_check_failures", "packet_check_failures"))
    verdict = "FAIL" if failed else ("NOT PROVEN" if out["blockers"] else "PASS")
    out["counts"] = counts
    out["candidate_verdict"] = verdict
    out["candidate_gate_result"] = verdict if verdict == "NOT PROVEN" else (
        "%s (claim-checks=%d, neutral-leak-tokens=%d, structure-checks=%d, packet-checks=%d)"
        % (verdict, counts["claim_check_failures"], counts["neutral_leak_tokens"],
           counts["structure_check_failures"], counts["packet_check_failures"]))
    out["formal_result"] = verdict if ACCEPTED else "NOT PROVEN / NON-FORMAL"
    out["details"] = {"claim_failures": claim_failures, "neutral_leaks": leaks,
                      "structure_failures": structure, "packet_failures": packet_failures}
    print(json.dumps(out, indent=2, ensure_ascii=False, sort_keys=True))
    return {"PASS": 0, "FAIL": 1, "NOT PROVEN": 3}[verdict]


if __name__ == "__main__":
    sys.exit(main(sys.argv))
