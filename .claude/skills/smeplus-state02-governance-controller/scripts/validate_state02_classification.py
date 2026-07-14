#!/usr/bin/env python3
"""
validate_state02_classification.py

State 02 — Step 08 Classification Registers validation (PREPARER SELF-CHECK ONLY).
This is NOT independent verification. It operates READ-ONLY against the source
registers and NEVER rewrites them. It produces STEP08_VALIDATION_REPORT.md and
returns a non-zero exit code when any CRITICAL error is found.

Usage:
    validate_state02_classification.py <step08_package_dir> [--report <path>]
    validate_state02_classification.py --self-test [--report <path>]

Detected conditions (per /L99.99 order Section 23):
  - Missing mandatory fields
  - Duplicate Record IDs
  - Duplicate CANONICAL classifications (per governance topic)
  - Missing Owner / Reviewer / Verifier
  - Missing Evidence Location / Timestamp
  - Unsupported PASS / Unsupported APPROVED
  - Unclassified document controlling execution
  - Superseded document controlling execution
  - Broken related-record references
  - P0 without escalation data
  - Invalid confidentiality classification (inline secret)
  - Stale manifest / manifest hash mismatch
"""

import sys
import os
import re
import hashlib
import datetime

# ---- token vocabularies -----------------------------------------------------

HARD_MISSING = {"", "missing", "not assigned", "tbd", "???", "-", "n/a - missing"}
# Values that are explicit, recorded, and therefore NOT "missing":
RECORDED_NA = {"n/a", "none", "not found", "not applicable", "—", "decision required"}
PENDING_RE = re.compile(r"pending", re.IGNORECASE)

CONTROLLING_GATE = {"blocking", "controls execution", "gate decision"}

SECRET_PATTERNS = [
    re.compile(r"BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"(?i)\b(password|passwd|secret|token|api[_-]?key)\s*[:=]\s*[^\s|]{8,}"),
    re.compile(r"(?i)ghp_[0-9A-Za-z]{20,}"),
]
# Table cells that legitimately use these words as classification labels, not secrets:
SECRET_ALLOW_SUBSTR = ["REFERENCE ONLY", "secret-storage", "secret manager", "SECRET /",
                       "SECRET/", "Who may", "no inline secret", "secret owner",
                       "never copy", "never written", "reference to",
                       # scanner-description / documentation lines (not real secrets):
                       "secret pattern", "common secret", "secret-handling", "secret handling",
                       "scans register", "flags any match", "high-entropy", "e.g.,",
                       "detected", "no secret value", "no inline"]

CRITICAL = "CRITICAL"
HOLD = "HOLD"
INFO = "INFO"


class Finding:
    def __init__(self, level, code, message):
        self.level = level
        self.code = code
        self.message = message

    def __str__(self):
        return f"[{self.level}] {self.code}: {self.message}"


# ---- markdown table parsing -------------------------------------------------

def parse_tables(text):
    """Return list of tables; each table = (headers[list], rows[list of dict])."""
    tables = []
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.strip().startswith("|") and i + 1 < len(lines) and re.match(
                r"^\s*\|[\s:\-|]+\|\s*$", lines[i + 1]):
            headers = [c.strip() for c in line.strip().strip("|").split("|")]
            rows = []
            j = i + 2
            while j < len(lines) and lines[j].strip().startswith("|"):
                cells = [c.strip() for c in lines[j].strip().strip("|").split("|")]
                if len(cells) == len(headers):
                    rows.append(dict(zip(headers, cells)))
                j += 1
            tables.append((headers, rows))
            i = j
        else:
            i += 1
    return tables


def col(row, *names):
    """Fetch a cell by fuzzy header match (case-insensitive substring)."""
    for name in names:
        for k, v in row.items():
            if k.lower() == name.lower():
                return v
    for name in names:
        for k, v in row.items():
            if name.lower() in k.lower():
                return v
    return None


def is_missing(value):
    if value is None:
        return True
    v = value.strip().lower()
    if v in RECORDED_NA:
        return False
    return v in HARD_MISSING or v == ""


def is_pending(value):
    return bool(value) and bool(PENDING_RE.search(value))


# ---- record verdict (used by self-test) -------------------------------------

def classify_verdict(rec):
    """
    Given a normalized record dict, return one of PASS / HOLD / FROZEN / FAIL.
    Order of precedence: FAIL > FROZEN > HOLD > PASS.
    Keys (all optional): classification, gate_impact, owner, verifier,
    verification, evidence, approval, priority, escalation, canonical_dupe,
    manifest_stale, superseded_controls, unclassified_controls, preparer_is_verifier.
    """
    cls = (rec.get("classification") or "").upper()
    gate = (rec.get("gate_impact") or "").lower()
    controlling = gate in CONTROLLING_GATE

    # FAIL conditions
    if rec.get("canonical_dupe"):
        return "FAIL"
    if rec.get("superseded_controls") or (cls == "SUPERSEDED" and controlling):
        return "FAIL"
    if rec.get("preparer_is_verifier"):
        return "FAIL"
    approval = (rec.get("approval") or "").upper()
    if approval == "APPROVED" and is_missing(rec.get("approval_evidence")):
        return "FAIL"
    if rec.get("manifest_stale"):
        return "FAIL"

    # FROZEN conditions
    if is_missing(rec.get("owner")):
        return "FROZEN"
    if rec.get("unclassified_controls") or (cls == "UNCLASSIFIED" and controlling):
        return "FROZEN"
    priority = (rec.get("priority") or "").upper()
    if priority == "P0" and is_missing(rec.get("escalation")):
        return "FROZEN"
    # Claimed progress without evidence
    verification = (rec.get("verification") or "").upper()
    if is_missing(rec.get("evidence")) and verification not in ("", "NOT SUBMITTED"):
        return "FROZEN"

    # HOLD conditions
    if is_missing(rec.get("verifier")) or is_pending(rec.get("verifier")):
        return "HOLD"
    if verification in ("PENDING VERIFICATION", "PENDING REVIEW", "INACCESSIBLE",
                        "PARTIALLY VERIFIED"):
        return "HOLD"

    return "PASS"


# ---- register-level checks --------------------------------------------------

def check_document_register(text, all_ids, findings):
    tables = parse_tables(text)
    canonical_topics = {}
    seen_ids = set()
    for headers, rows in tables:
        if not any("Doc ID" in h or "Document ID" in h for h in headers):
            continue
        for row in rows:
            did = col(row, "Doc ID", "Document ID")
            if not did or did.startswith("---"):
                continue
            cls = (col(row, "Classification") or "").upper()
            topic = col(row, "Controlling Topic")
            owner = col(row, "Owner")
            reviewer = col(row, "Reviewer")
            verifier = col(row, "Verifier")
            gate = (col(row, "Gate Impact") or "").lower()
            superseded_by = col(row, "Superseded By")
            controlling = gate in CONTROLLING_GATE

            if did in seen_ids:
                findings.append(Finding(CRITICAL, "DUP_ID",
                                        f"Duplicate Document ID {did}"))
            seen_ids.add(did)

            if is_missing(owner):
                findings.append(Finding(CRITICAL, "MISSING_OWNER",
                                        f"{did} has no Owner (FROZEN)"))
            if is_missing(reviewer):
                findings.append(Finding(CRITICAL, "MISSING_REVIEWER",
                                        f"{did} has no Reviewer"))
            if is_missing(verifier):
                findings.append(Finding(HOLD, "MISSING_VERIFIER",
                                        f"{did} has no Verifier (HOLD)"))
            elif is_pending(verifier):
                findings.append(Finding(HOLD, "PENDING_VERIFIER",
                                        f"{did} Verifier pending independent (HOLD)"))

            if cls == "UNCLASSIFIED" and controlling:
                findings.append(Finding(CRITICAL, "UNCLASSIFIED_CONTROLS",
                                        f"{did} UNCLASSIFIED but controls execution (FROZEN)"))
            if cls == "SUPERSEDED":
                if is_missing(superseded_by):
                    findings.append(Finding(CRITICAL, "SUPERSEDED_NO_REPLACEMENT",
                                            f"{did} SUPERSEDED without named replacement"))
                if controlling:
                    findings.append(Finding(CRITICAL, "SUPERSEDED_CONTROLS",
                                            f"{did} SUPERSEDED but controls execution (FAIL)"))
            if cls == "CANONICAL" and topic:
                canonical_topics.setdefault(topic.strip().lower(), []).append(did)

    for topic, ids in canonical_topics.items():
        if len(ids) > 1:
            findings.append(Finding(CRITICAL, "DUP_CANONICAL",
                                    f"Multiple CANONICAL documents for topic '{topic}': "
                                    f"{', '.join(ids)} (FAIL)"))
    return seen_ids


def check_raid_register(text, findings):
    tables = parse_tables(text)
    for headers, rows in tables:
        if not any("RAID ID" in h for h in headers):
            continue
        for row in rows:
            rid = col(row, "RAID ID")
            if not rid or rid.startswith("---"):
                continue
            pr = (col(row, "Priority") or "").upper()
            if pr == "P0":
                owner = col(row, "Owner")
                action = col(row, "Mitigation", "Required Action", "Mitigation / Required Action")
                esc = col(row, "Escalation Authority")
                due = col(row, "Due Date")
                if is_missing(owner):
                    findings.append(Finding(CRITICAL, "P0_NO_OWNER",
                                            f"{rid} is P0 without Owner (FROZEN)"))
                if is_missing(action) or is_missing(esc) or is_missing(due):
                    findings.append(Finding(CRITICAL, "P0_NO_ESCALATION",
                                            f"{rid} is P0 without full escalation data"))


def check_workitem_register(text, findings):
    tables = parse_tables(text)
    seen = set()
    for headers, rows in tables:
        if not any(h.strip() in ("WI ID", "Work Item ID") for h in headers):
            continue
        for row in rows:
            wid = col(row, "WI ID", "Work Item ID")
            if not wid or wid.startswith("---"):
                continue
            if wid in seen:
                findings.append(Finding(CRITICAL, "DUP_ID", f"Duplicate Work Item ID {wid}"))
            seen.add(wid)
            owner = col(row, "Owner")
            status = (col(row, "Status") or "").upper()
            evidence = col(row, "Evidence")
            if is_missing(owner):
                findings.append(Finding(CRITICAL, "MISSING_OWNER",
                                        f"{wid} has no Owner (FROZEN)"))
            if "COMPLETE" in status and is_missing(evidence):
                findings.append(Finding(CRITICAL, "CLAIM_NO_EVIDENCE",
                                        f"{wid} claims complete without evidence (FROZEN)"))


def check_evidence_register(text, findings):
    tables = parse_tables(text)
    for headers, rows in tables:
        if not any(h.strip() in ("Ev ID", "Evidence ID") for h in headers):
            continue
        for row in rows:
            eid = col(row, "Ev ID", "Evidence ID")
            if not eid or eid.startswith("---"):
                continue
            level = (col(row, "Level", "Evidence Level") or "").upper()
            location = col(row, "Location")
            ts = col(row, "Timestamp")
            verification = (col(row, "Verification", "Verification Status") or "").upper()
            # E5 rows are allowed to be inaccessible/no-location by definition.
            if "E5" not in level and is_missing(location):
                findings.append(Finding(CRITICAL, "MISSING_EVIDENCE_LOCATION",
                                        f"{eid} missing evidence Location"))
            if "E5" not in level and is_missing(ts):
                findings.append(Finding(HOLD, "MISSING_TIMESTAMP",
                                        f"{eid} missing Timestamp"))
            if verification == "VERIFIED":
                # Preparer self-check cannot certify VERIFIED; flag for independent role.
                findings.append(Finding(INFO, "VERIFIED_CLAIM",
                                        f"{eid} marked VERIFIED — requires independent confirmation"))


def scan_unsupported_pass_approved(text, findings, source):
    """Flag any Gate=PASS or Approval=APPROVED asserted without Boss evidence."""
    for m in re.finditer(r"\bGate\s*(Status|Result)?\s*[:=]\s*PASS\b", text):
        ctx = text[max(0, m.start() - 80):m.start() + 80]
        if "READY FOR INDEPENDENT REVIEW" in ctx or "recommend" in ctx.lower():
            continue
        if "boss" not in ctx.lower():
            findings.append(Finding(CRITICAL, "UNSUPPORTED_PASS",
                                    f"Unsupported Gate PASS in {source}"))
    for m in re.finditer(r"\bApproval\s*(Status)?\s*[:=]\s*APPROVED\b", text):
        ctx = text[max(0, m.start() - 80):m.start() + 120]
        if "boss" not in ctx.lower():
            findings.append(Finding(CRITICAL, "UNSUPPORTED_APPROVED",
                                    f"Unsupported APPROVED in {source}"))


def scan_secrets(text, findings, source):
    for pat in SECRET_PATTERNS:
        for m in pat.finditer(text):
            line = text[text.rfind("\n", 0, m.start()) + 1: text.find("\n", m.end())]
            if any(a in line for a in SECRET_ALLOW_SUBSTR):
                continue
            findings.append(Finding(CRITICAL, "INLINE_SECRET",
                                    f"Possible inline secret in {source}: {m.group()[:24]}..."))


SEMANTIC_RULES = {
    "CHECK-08-11": ("Effective CANONICAL requires Boss confirmation", "No violation", "doc 03"),
    "CHECK-08-12": ("Final Decision Authority must be Boss sole", "No violation", "doc 07"),
    "CHECK-08-13": ("Exactly one Accountable Owner", "No violation", "docs 03/04/05/06/14"),
    "CHECK-08-14": ("No post-commit placeholders after evidence addendum", "No violation", "registers/addendum"),
    "CHECK-08-15": ("Step 08 traces to GitHub Issue #9", "Issue #9 found", "doc 12/mapping"),
    "CHECK-08-16": ("Decision status separated from verification status", "Required columns found", "doc 07"),
}


def check_semantic(pkg_dir, texts, findings):
    """Semantic governance checks CHECK-08-11..16 (L99 Review Rounds).

    Returns a list of per-check result dicts so the report can show each result
    individually (not just an aggregate CRITICAL count)."""
    doc03 = texts.get("03") or ""
    doc07 = texts.get("07") or ""
    doc12 = texts.get("12") or ""
    mapping = texts.get("map") or ""

    violations = {k: [] for k in SEMANTIC_RULES}

    # CHECK-08-11: effective CANONICAL (not CANDIDATE) without Boss evidence is a violation.
    for _, rows in parse_tables(doc03):
        for row in rows:
            did = col(row, "Doc ID", "Document ID")
            if not did or did.startswith("---"):
                continue
            cls = (col(row, "Classification") or "").upper()
            if "CANONICAL" in cls and "CANDIDATE" not in cls:
                ev = (col(row, "Evidence") or "").lower()
                appr = (col(row, "Approval Authority") or "").lower()
                if "boss" not in ev and "boss approval" not in appr and "confirm" not in ev:
                    violations["CHECK-08-11"].append(
                        f"{did} shows effective CANONICAL without Boss-confirmation evidence")

    # CHECK-08-12: No slash/joint or L99 in Final Decision Authority.
    for _, rows in parse_tables(doc07):
        for row in rows:
            fda = col(row, "Final Decision Authority")
            if fda is None or "---" in fda:
                continue
            low = fda.lower()
            if "/" in fda or "l99" in low or "chatgpt" in low:
                violations["CHECK-08-12"].append(f"Final Decision Authority not Boss-sole: '{fda}'")

    # CHECK-08-13: Exactly one Accountable Owner (no ' / ' joint owner) across registers.
    for tag in ("03", "04", "05", "06", "14"):
        for _, rows in parse_tables(texts.get(tag) or ""):
            for row in rows:
                owner = col(row, "Owner")
                if owner and " / " in owner:
                    rid = (col(row, "Doc ID", "Document ID", "WI ID", "Work Item ID",
                               "Ev ID", "Evidence ID", "RAID ID", "Gap ID") or "row")
                    violations["CHECK-08-13"].append(
                        f"Joint owner '{owner}' in {tag}:{rid} (need one Accountable Owner)")

    # CHECK-08-14: POST-COMMIT placeholders forbidden once the addendum (package commit) exists.
    addendum = os.path.join(pkg_dir, "STEP08_POST_COMMIT_EVIDENCE_ADDENDUM.md")
    if os.path.isfile(addendum):
        for tag in ("03", "04", "05", "06", "07", "12", "map"):
            if "PENDING — POST-COMMIT" in (texts.get(tag) or ""):
                violations["CHECK-08-14"].append(
                    f"POST-COMMIT placeholder still present in doc {tag} after package commit")

    # CHECK-08-15: Step 08 must trace to GitHub Issue #9.
    if "issue #9" not in (doc12 + mapping).lower():
        violations["CHECK-08-15"].append(
            "Step 08 does not trace to GitHub Issue #9 (doc 12 / mapping record)")

    # CHECK-08-16: Decision Status must be separate from Verification Status in doc 07.
    if ("Boss Decision Status" not in doc07 or "Independent Verification Status" not in doc07):
        violations["CHECK-08-16"].append(
            "doc 07 does not separate Boss Decision Status from Independent Verification Status")

    results = []
    for cid in ("CHECK-08-11", "CHECK-08-12", "CHECK-08-13", "CHECK-08-14",
                "CHECK-08-15", "CHECK-08-16"):
        rule, expected, source = SEMANTIC_RULES[cid]
        vs = violations[cid]
        passed = not vs
        actual = expected if passed else "; ".join(vs)
        results.append({"id": cid, "rule": rule, "expected": expected,
                        "actual": actual, "source": source,
                        "result": "PASS" if passed else "FAIL"})
        for v in vs:
            findings.append(Finding(CRITICAL, cid, v))
    return results


def check_related_refs(text, all_ids, findings, source):
    ref_ids = set(re.findall(r"\b(DOC-S02-\d+|WI-08-[A-Z0-9]+|EV-08-\d+|RAID-08-[A-Z0-9]+|"
                             r"DEC-08-\d+|GAP-08-[A-Z]+)\b", text))
    for rid in ref_ids:
        if rid not in all_ids:
            # Only report DOC/WI/EV/RAID/DEC that look like record refs
            findings.append(Finding(INFO, "UNRESOLVED_REF",
                                    f"Reference {rid} in {source} not found in collected ID set"))


# ---- manifest verification --------------------------------------------------

def check_manifest(pkg_dir, findings):
    manifest = os.path.join(pkg_dir, "PACKAGE_MANIFEST_SHA256.txt")
    if not os.path.isfile(manifest):
        findings.append(Finding(HOLD, "NO_MANIFEST",
                                "PACKAGE_MANIFEST_SHA256.txt not found (generate before verification)"))
        return
    manifest_mtime = os.path.getmtime(manifest)
    listed = set()
    with open(manifest, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            if "SELF" in line and "HASH EXCLUDED" in line:
                continue
            parts = line.split(None, 1)
            if len(parts) != 2:
                continue
            h, rel = parts[0].strip(), parts[1].strip()
            listed.add(rel)
            path = os.path.join(pkg_dir, rel)
            if not os.path.isfile(path):
                findings.append(Finding(CRITICAL, "MANIFEST_MISSING_FILE",
                                        f"Manifest lists missing file: {rel}"))
                continue
            actual = sha256_file(path)
            if actual != h:
                findings.append(Finding(CRITICAL, "HASH_MISMATCH",
                                        f"Hash mismatch for {rel}"))
            if os.path.getmtime(path) > manifest_mtime + 1:
                findings.append(Finding(CRITICAL, "STALE_MANIFEST",
                                        f"Stale manifest: {rel} modified after manifest"))
    # Coverage: every .md in pkg (except the report) should be listed.
    for name in os.listdir(pkg_dir):
        if name.endswith(".md") and name != "STEP08_VALIDATION_REPORT.md":
            if name not in listed:
                findings.append(Finding(HOLD, "MANIFEST_COVERAGE",
                                        f"Package file not in manifest: {name}"))


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def git_blob_sha(path):
    """Compute the git blob object id (sha1) of a file's content, no git required."""
    try:
        with open(path, "rb") as f:
            data = f.read()
    except OSError:
        return "n/a"
    h = hashlib.sha1()
    h.update(b"blob " + str(len(data)).encode() + b"\0")
    h.update(data)
    return h.hexdigest()


def run_metadata(pkg_dir, manifest_result, exit_code):
    """Collect report metadata from environment (with defaults) — no git calls."""
    script_path = os.path.abspath(__file__)
    return {
        "Validation Timestamp": os.environ.get("STEP08_VALIDATION_TS", "generation-time"),
        "Repository": os.environ.get("STEP08_REPO", "TH-PATTARAKRIT/AI-Collaboration-Hub"),
        "Branch": os.environ.get("STEP08_BRANCH", "claude/state-02-classification-registers-7qwwcy"),
        "PR Number": os.environ.get("STEP08_PR", "#27"),
        "Validated Commit": os.environ.get("STEP08_COMMIT", "working tree (pre-commit)"),
        "Validator Script Blob SHA": git_blob_sha(script_path),
        "Package Path": pkg_dir,
        "Manifest Result": manifest_result,
        "Exit Code": str(exit_code),
    }


# ---- self-test (mandatory tests T08-01..T08-10) -----------------------------

def self_test():
    cases = [
        ("T08-01", "Complete verified record",
         dict(classification="SUPPORTING", gate_impact="input", owner="Executive Secretary",
              verifier="Independent Evidence Verifier (named)", verification="VERIFIED",
              evidence="E1 path", priority="P2", escalation="Boss"), "PASS"),
        ("T08-02", "Claimed progress without evidence",
         dict(owner="Executive Secretary", verification="PENDING VERIFICATION",
              evidence="", priority="P1", escalation="Boss"), "FROZEN"),
        ("T08-03", "Evidence without Verifier",
         dict(classification="SUPPORTING", gate_impact="blocking", owner="Executive Secretary",
              verifier="", verification="PENDING VERIFICATION", evidence="E1 path"), "HOLD"),
        ("T08-04", "Missing Owner",
         dict(classification="SUPPORTING", gate_impact="input", owner="",
              verifier="named", evidence="E1 path"), "FROZEN"),
        ("T08-05", "Duplicate CANONICAL document",
         dict(classification="CANONICAL", gate_impact="blocking", owner="ES",
              verifier="named", evidence="E1", canonical_dupe=True), "FAIL"),
        ("T08-06", "Superseded document controlling execution",
         dict(classification="SUPERSEDED", gate_impact="blocking", owner="ES",
              verifier="named", evidence="E1"), "FAIL"),
        ("T08-07", "Claude as Preparer and Verifier",
         dict(classification="SUPPORTING", gate_impact="input", owner="ES",
              verifier="Claude Code", evidence="E1", preparer_is_verifier=True), "FAIL"),
        ("T08-08", "APPROVED without Boss evidence",
         dict(classification="SUPPORTING", gate_impact="gate decision", owner="ES",
              verifier="named", evidence="E1", approval="APPROVED", approval_evidence=""), "FAIL"),
        ("T08-09", "Unclassified document used for Gate",
         dict(classification="UNCLASSIFIED", gate_impact="blocking", owner="ES",
              verifier="named", evidence="E1"), "FROZEN"),
        ("T08-10", "Stale manifest",
         dict(classification="SUPPORTING", gate_impact="blocking", owner="ES",
              verifier="named", evidence="E1", manifest_stale=True), "FAIL"),
    ]
    results = []
    all_ok = True
    for tid, desc, rec, expected in cases:
        actual = classify_verdict(rec)
        ok = actual == expected
        all_ok = all_ok and ok
        results.append((tid, desc, expected, actual, "PASS" if ok else "MISMATCH"))
    return results, all_ok


# ---- report emission --------------------------------------------------------

def emit_report(path, pkg_dir, findings, selftest_results, exit_code,
                semantic_results=None, metadata=None):
    semantic_results = semantic_results or []
    metadata = metadata or {}
    crit = [f for f in findings if f.level == CRITICAL]
    hold = [f for f in findings if f.level == HOLD]
    info = [f for f in findings if f.level == INFO]
    now = metadata.get("Validation Timestamp",
                       os.environ.get("STEP08_VALIDATION_TS", "generation-time"))
    sem_pass = sum(1 for r in semantic_results if r["result"] == "PASS")
    sem_total = len(semantic_results)
    tests_pass = sum(1 for r in selftest_results if r[4] == "PASS")
    lines = []
    lines.append("# STEP08_VALIDATION_REPORT.md")
    lines.append("")
    lines.append("Generated by validate_state02_classification.py "
                 "(PREPARER SELF-CHECK ONLY — NOT INDEPENDENT VERIFICATION).")
    lines.append(f"Package directory: {pkg_dir}")
    lines.append(f"Generated: {now}")
    lines.append(f"Overall result: {'CRITICAL ERRORS FOUND' if crit else 'NO CRITICAL ERRORS (HOLD/INFO may remain)'}")
    lines.append(f"Exit code: {exit_code}")
    lines.append("")
    if metadata:
        lines.append("## Run Metadata")
        lines.append("")
        for k in ("Validation Timestamp", "Repository", "Branch", "PR Number",
                  "Validated Commit", "Validator Script Blob SHA", "Package Path",
                  "Manifest Result", "Exit Code"):
            if k in metadata:
                lines.append(f"- {k}: {metadata[k]}")
        lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Mandatory Tests T08-01..T08-10: {tests_pass}/{len(selftest_results)} PASS")
    if sem_total:
        lines.append(f"- Semantic Checks CHECK-08-11..16: {sem_pass}/{sem_total} PASS")
    lines.append(f"- Critical Findings: {len(crit)}")
    lines.append(f"- HOLD findings: {len(hold)}")
    lines.append(f"- INFO findings: {len(info)}")
    lines.append(f"- Exit Code: {exit_code}")
    lines.append("")
    lines.append("## Mandatory Tests (T08-01..T08-10)")
    lines.append("")
    lines.append("| Test ID | Description | Expected | Actual | Result |")
    lines.append("|---|---|---|---|---|")
    for tid, desc, expected, actual, res in selftest_results:
        lines.append(f"| {tid} | {desc} | {expected} | {actual} | {res} |")
    lines.append("")
    if semantic_results:
        lines.append("## Semantic Governance Checks")
        lines.append("")
        lines.append("| Check ID | Governance Rule | Expected Result | Actual Result | Evidence Source | Result |")
        lines.append("|---|---|---|---|---|---|")
        for r in semantic_results:
            lines.append(f"| {r['id']} | {r['rule']} | {r['expected']} | "
                         f"{r['actual']} | {r['source']} | {r['result']} |")
        lines.append("")
    for title, group in (("CRITICAL", crit), ("HOLD", hold), ("INFO", info)):
        lines.append(f"## {title} Findings")
        lines.append("")
        if not group:
            lines.append("_None._")
        else:
            for f in group:
                lines.append(f"- {f.code}: {f.message}")
        lines.append("")
    lines.append("## Control Statement")
    lines.append("")
    lines.append("This report is a preparer self-check. It does not constitute independent "
                 "governance review or independent evidence verification. Verifier fields "
                 "marked PENDING raise expected HOLD notices, not critical errors. Boss "
                 "remains the Sole Final Approver.")
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")


# ---- main -------------------------------------------------------------------

def run_package(pkg_dir):
    findings = []
    all_ids = set()

    def read(name):
        p = os.path.join(pkg_dir, name)
        if not os.path.isfile(p):
            findings.append(Finding(CRITICAL, "MISSING_DELIVERABLE",
                                    f"Required register not found: {name}"))
            return None
        with open(p, "r", encoding="utf-8") as f:
            return f.read()

    doc03 = read("03_DOCUMENT_CLASSIFICATION_REGISTER.md")
    doc04 = read("04_REQUIREMENT_AND_WORK_ITEM_CLASSIFICATION_REGISTER.md")
    doc05 = read("05_EVIDENCE_CLASSIFICATION_REGISTER.md")
    doc06 = read("06_RAID_CLASSIFICATION_REGISTER.md")

    def read_optional(name):
        p = os.path.join(pkg_dir, name)
        if os.path.isfile(p):
            with open(p, "r", encoding="utf-8") as f:
                return f.read()
        return ""

    doc07 = read_optional("07_DECISION_AND_EXCEPTION_REGISTER.md")
    doc12 = read_optional("12_CLASSIFICATION_TRACEABILITY_MATRIX.md")
    doc14 = read_optional("14_CLASSIFICATION_VALIDATION_AND_GAP_REPORT.md")
    mapping = read_optional("STATE02_STEP_NUMBERING_MAPPING_RECORD.md")

    # Collect IDs first for reference checks.
    for txt in (doc03, doc04, doc05, doc06):
        if txt:
            all_ids |= set(re.findall(
                r"\b(DOC-S02-\d+|WI-08-[A-Z0-9]+|EV-08-\d+|RAID-08-[A-Z0-9]+|DEC-08-\d+|GAP-08-[A-Z]+)\b",
                txt))

    if doc03:
        check_document_register(doc03, all_ids, findings)
        scan_unsupported_pass_approved(doc03, findings, "doc 03")
        scan_secrets(doc03, findings, "doc 03")
    if doc04:
        check_workitem_register(doc04, findings)
    if doc05:
        check_evidence_register(doc05, findings)
        scan_secrets(doc05, findings, "doc 05")
    if doc06:
        check_raid_register(doc06, findings)

    # confidentiality doc secret scan
    doc10 = read("10_CONFIDENTIALITY_AND_ACCESS_MATRIX.md") if os.path.isfile(
        os.path.join(pkg_dir, "10_CONFIDENTIALITY_AND_ACCESS_MATRIX.md")) else None
    if doc10:
        scan_secrets(doc10, findings, "doc 10")

    texts = {"03": doc03, "04": doc04, "05": doc05, "06": doc06, "07": doc07,
             "12": doc12, "14": doc14, "10": doc10, "map": mapping}
    semantic_results = check_semantic(pkg_dir, texts, findings)

    check_manifest(pkg_dir, findings)
    manifest_codes = {"HASH_MISMATCH", "STALE_MANIFEST", "MANIFEST_MISSING_FILE"}
    manifest_bad = any(f.code in manifest_codes for f in findings)
    no_manifest = any(f.code == "NO_MANIFEST" for f in findings)
    manifest_result = ("NOT PRESENT" if no_manifest
                       else ("MISMATCH/STALE" if manifest_bad else "OK (self-verified)"))
    return findings, semantic_results, manifest_result


def main(argv):
    report_path = None
    if "--report" in argv:
        idx = argv.index("--report")
        report_path = argv[idx + 1]
        argv = argv[:idx] + argv[idx + 2:]

    selftest_results, selftest_ok = self_test()

    if "--self-test" in argv:
        for tid, desc, expected, actual, res in selftest_results:
            print(f"{tid} | expected={expected} actual={actual} -> {res}")
        exit_code = 0 if selftest_ok else 2
        if report_path:
            emit_report(report_path, "(self-test)", [], selftest_results, exit_code)
        print(f"SELF-TEST {'PASS' if selftest_ok else 'FAIL'} (exit {exit_code})")
        return exit_code

    pkg = None
    for a in argv[1:]:
        if not a.startswith("--"):
            pkg = a
            break
    if not pkg:
        print("Usage: validate_state02_classification.py <step08_package_dir> [--report <path>]")
        print("       validate_state02_classification.py --self-test")
        return 2
    if not os.path.isdir(pkg):
        print(f"FAIL: package directory not found: {pkg}")
        return 2

    findings, semantic_results, manifest_result = run_package(pkg)
    crit = [f for f in findings if f.level == CRITICAL]
    sem_fail = any(r["result"] != "PASS" for r in semantic_results)
    exit_code = 0 if (not crit and selftest_ok and not sem_fail) else 1
    if not selftest_ok:
        exit_code = 2

    if report_path is None:
        report_path = os.path.join(pkg, "STEP08_VALIDATION_REPORT.md")
    metadata = run_metadata(pkg, manifest_result, exit_code)
    emit_report(report_path, pkg, findings, selftest_results, exit_code,
                semantic_results=semantic_results, metadata=metadata)

    sem_pass = sum(1 for r in semantic_results if r["result"] == "PASS")
    print(f"Findings: CRITICAL={len(crit)} "
          f"HOLD={len([f for f in findings if f.level == HOLD])} "
          f"INFO={len([f for f in findings if f.level == INFO])}")
    print(f"Mandatory Tests: {sum(1 for r in selftest_results if r[4]=='PASS')}/{len(selftest_results)} PASS")
    print(f"Semantic Checks: {sem_pass}/{len(semantic_results)} PASS")
    for f in crit:
        print(str(f))
    print(f"Report written: {report_path}")
    print(f"Self-test: {'PASS' if selftest_ok else 'FAIL'}")
    print(f"Exit code: {exit_code}")
    return exit_code


if __name__ == "__main__":
    sys.exit(main(sys.argv))
