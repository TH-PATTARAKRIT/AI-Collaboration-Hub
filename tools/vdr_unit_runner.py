#!/usr/bin/env python3
"""STATE03 VDR read-only Unit runner.

Usage:
    python3 -B tools/vdr_unit_runner.py U139

Contract:
  * The Unit ID (U followed by 3-4 digits) is the only variable input.
  * Fixed approved roots only, derived from this file's location inside the
    repository. No absolute machine-specific paths are used or printed.
  * Read-only: no file writes, deletes, redirects, commits, pushes or network.
  * Output is a single JSON document on stdout.
  * The only gate invoked is the portable repository gate:
        tools/vdr_check.py --read-only <restricted> <neutral> <packet>
    If that gate is absent or the Unit's evidence cannot be resolved, the
    result is NOT PROVEN with the exact blocker. A PASS is never inferred.
  * The runner is a transport/control tool, not a gate. While the gate reports
    accepted=false, the result is the gate's formal_result
    ("NOT PROVEN / NON-FORMAL"); the candidate verdict is shown separately.
"""
import json
import os
import re
import subprocess
import sys

sys.dont_write_bytecode = True

REPO = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
VDR_REL = ("99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_MIGRATION_FACTORY/"
           "TEAM_A/04_EVIDENCE_PACKS/VERY_DEEP_RESEARCH_L0_L3")
FIXTURE_REL = "tools/vdr_gate_fixtures"
GATE_REL = "tools/vdr_check.py"
# Canonical VDR root first; repository root holds the legacy evidence dirs;
# the synthetic gate fixtures (U9001+) live last.
APPROVED_ROOTS = (VDR_REL, "", FIXTURE_REL)
RESTRICTED_DIR = "01_RESTRICTED_TECHNICAL_EVIDENCE"
NEUTRAL_DIR = "02_NEUTRAL_KNOWLEDGE"
PACKET_DIR = "04_HANDOFF_PACKETS"
MARKER = "DEEPSEEK-CORRECTED / PENDING STATE03 RE-VERIFICATION"
UNIT_RE = re.compile(r"^U\d{3,4}$")
EVIDENCE_RE = re.compile(r"^(%s|%s)/(U\d{3,4}[^/]*\.md)$" % (RESTRICTED_DIR, NEUTRAL_DIR))


def absolute(rel):
    return os.path.realpath(os.path.join(REPO, rel))


def inside_repo(path):
    return path == REPO or path.startswith(REPO + os.sep)


def rel(path):
    return os.path.relpath(path, REPO) if path else None


def strings(node):
    if isinstance(node, str):
        yield node
    elif isinstance(node, dict):
        for value in node.values():
            yield from strings(value)
    elif isinstance(node, list):
        for value in node:
            yield from strings(value)


def resolve_evidence(unit, packet, root_rel):
    """Return {restricted, neutral} absolute paths under one approved root."""
    found = {RESTRICTED_DIR: set(), NEUTRAL_DIR: set()}
    for value in strings(packet or {}):
        match = EVIDENCE_RE.match(value.strip())
        if match and match.group(2).startswith(unit + "_"):
            path = absolute(os.path.join(root_rel, value.strip()))
            if inside_repo(path) and os.path.isfile(path):
                found[match.group(1)].add(path)
    for sub in found:
        if found[sub]:
            continue
        directory = absolute(os.path.join(root_rel, sub))
        if not os.path.isdir(directory):
            continue
        for name in sorted(os.listdir(directory)):
            is_neutral = name.endswith("_NEUTRAL.md")
            if (name.startswith(unit + "_") and name.endswith(".md")
                    and is_neutral == (sub == NEUTRAL_DIR)):
                path = os.path.realpath(os.path.join(directory, name))
                if inside_repo(path) and os.path.isfile(path):
                    found[sub].add(path)
    return found


def emit(out):
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0


def main(argv):
    if len(argv) != 2 or not UNIT_RE.match(argv[1]):
        print(json.dumps({"error": "usage: vdr_unit_runner.py U###", "argv": argv[1:]}))
        return 2
    unit = argv[1]
    out = {
        "runner": "tools/vdr_unit_runner.py",
        "runner_role": "transport/control only — not a gate",
        "unit": unit,
        "approved_roots": [r or "." for r in APPROVED_ROOTS],
        "blockers": [],
    }

    packet, packet_path, root_rel = None, None, None
    for candidate_root in APPROVED_ROOTS:
        path = absolute(os.path.join(candidate_root, PACKET_DIR, "%s_handoff_packet.json" % unit))
        if inside_repo(path) and os.path.isfile(path):
            packet_path, root_rel = path, candidate_root
            break
    packet_info = {"path": rel(packet_path), "exists": packet_path is not None}
    if packet_path:
        try:
            with open(packet_path, encoding="utf-8") as handle:
                packet = json.load(handle)
            packet_info.update({
                "json_valid": True,
                "unit_key": packet.get("unit"),
                "has_unit_id_key": "unit_id" in packet,
                "status": packet.get("status"),
                "marker": packet.get("marker"),
                "gate_result": packet.get("gate_result"),
            })
        except (ValueError, OSError) as exc:
            packet_info.update({"json_valid": False, "error": str(exc)})
            out["blockers"].append("handoff packet is not valid JSON")
    else:
        out["blockers"].append("handoff packet not found under approved roots")
        root_rel = VDR_REL
    out["packet"] = packet_info

    found = resolve_evidence(unit, packet, root_rel)
    evidence = {}
    for key, sub in (("restricted", RESTRICTED_DIR), ("neutral", NEUTRAL_DIR)):
        paths = sorted(found[sub])
        evidence[key] = [rel(p) for p in paths]
        if len(paths) != 1:
            out["blockers"].append("%s evidence file: %d candidates (need exactly 1)" % (key, len(paths)))
    out["evidence"] = evidence

    gate_path = absolute(GATE_REL)
    gate = {"path": GATE_REL, "available": inside_repo(gate_path) and os.path.isfile(gate_path)}
    if not gate["available"]:
        out["blockers"].append("portable gate %s not present in repository" % GATE_REL)
    out["gate"] = gate

    if out["blockers"]:
        out["result"] = "NOT PROVEN"
        return emit(out)

    restricted, neutral = sorted(found[RESTRICTED_DIR])[0], sorted(found[NEUTRAL_DIR])[0]
    argv_gate = [sys.executable, "-B", gate_path, "--read-only",
                 rel(restricted), rel(neutral), rel(packet_path)]
    gate["argv"] = ["python3", "-B", GATE_REL, "--read-only",
                    rel(restricted), rel(neutral), rel(packet_path)]
    env = {"PATH": os.environ.get("PATH", ""), "PYTHONDONTWRITEBYTECODE": "1", "LC_ALL": "C.UTF-8"}
    try:
        proc = subprocess.run(argv_gate, cwd=REPO, env=env, stdin=subprocess.DEVNULL,
                              capture_output=True, text=True, timeout=300, shell=False)
    except (OSError, subprocess.TimeoutExpired) as exc:
        gate["error"] = str(exc)
        out["blockers"].append("gate execution failed")
        out["result"] = "NOT PROVEN"
        return emit(out)

    gate["exit_code"] = proc.returncode
    gate["stderr"] = proc.stderr.strip() or None
    try:
        report = json.loads(proc.stdout)
    except ValueError:
        gate["stdout"] = proc.stdout
        out["blockers"].append("gate output is not a JSON document")
        out["result"] = "NOT PROVEN"
        return emit(out)
    gate["report"] = report

    accepted = report.get("accepted") is True
    if accepted:
        verdict = report.get("candidate_verdict")
        expect_status = {"PASS": "GATE-PASS", "FAIL": "GATE-FAIL"}.get(verdict, "NOT PROVEN")
        expect_gate_result = report.get("candidate_gate_result")
    else:
        expect_status, expect_gate_result = "NOT PROVEN", "NOT PROVEN"
    checks = {
        "unit_key": packet.get("unit") == unit,
        "no_unit_id_key": "unit_id" not in packet,
        "status_matches_gate": packet.get("status") == expect_status,
        "gate_result_matches_gate": packet.get("gate_result") == expect_gate_result,
    }
    if "b02_correction" in packet:
        checks["marker"] = packet.get("marker") == MARKER
    out["packet_checks"] = checks
    out["expected"] = {"status": expect_status, "gate_result": expect_gate_result}
    out["packet_consistent"] = all(checks.values())
    out["candidate_verdict"] = report.get("candidate_verdict")
    out["result"] = report.get("formal_result") or "NOT PROVEN"
    return emit(out)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
