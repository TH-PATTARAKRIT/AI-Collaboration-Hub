#!/usr/bin/env python3
"""
State 03 Architecture Package Validator
Session: [SMEPLUS-26-07-10-001]  Control Level: /L99.99

Controlled, read-only validation of the State 03 Architecture package.
Automated validation is NOT independent architecture approval and does NOT
approve any gate or mark any deliverable VERIFIED. It only checks structural
and evidence-integrity conditions defined by the L99 correction order (P1-02).

Usage:
    python3 validate_state03_package.py            # run checks, print summary
    python3 validate_state03_package.py --report   # also write STATE03_VALIDATION_REPORT.md

Exit code 0 if all checks pass, 1 otherwise.
"""
import os
import re
import sys
import hashlib

VALIDATOR_VERSION = "1.0.0"
PKG = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(PKG, "..", "..", ".."))

MANIFEST = "PACKAGE_MANIFEST_SHA256_STATE03_ARCHITECTURE.txt"
REPORT = "STATE03_VALIDATION_REPORT.md"
VALIDATOR = os.path.basename(__file__)
# Files excluded from the SHA-256 manifest (documented volatile artifacts).
MANIFEST_EXCLUSIONS = {MANIFEST, REPORT}

ARC_WP_FILES = [
    "SAAS_ARCHITECTURE_PRINCIPLES.md",
    "TENANT_COMPANY_BRANCH_MODEL.md",
    "SUBSCRIPTION_ENTITLEMENT_MODEL.md",
    "ENTERPRISE_CONTROL_LAYER.md",
    "APPLICATION_MODULE_BOUNDARY.md",
    "SYSTEM_CONTEXT_ARCHITECTURE.md",
    "LOGICAL_COMPONENT_ARCHITECTURE.md",
    "MULTI_TENANT_DATA_ISOLATION_OPTIONS.md",
    "IDENTITY_ACCESS_ARCHITECTURE.md",
    "INTEGRATION_EVENT_ARCHITECTURE.md",
    "NON_FUNCTIONAL_ARCHITECTURE_REQUIREMENTS.md",
    "ARCHITECTURE_DECISION_REGISTER.md",
    "ARCHITECTURE_RISK_ASSUMPTION_REGISTER.md",
]
CONTROL_FILES = [
    "STATE03_EVIDENCE_REGISTER.md",
    "STATE03_DELIVERABLE_INDEX.md",
    "STATE03_EXECUTION_SUMMARY.md",
    "STATE03_GAP_REGISTER.md",
    "STATE03_REVIEW_HANDOFF.md",
    MANIFEST,
]
REQUIRED_FILES = ARC_WP_FILES + CONTROL_FILES

# Documents that must contain at least one Mermaid diagram.
MERMAID_REQUIRED = [
    "TENANT_COMPANY_BRANCH_MODEL.md",
    "SUBSCRIPTION_ENTITLEMENT_MODEL.md",
    "ENTERPRISE_CONTROL_LAYER.md",
    "APPLICATION_MODULE_BOUNDARY.md",
    "SYSTEM_CONTEXT_ARCHITECTURE.md",
    "LOGICAL_COMPONENT_ARCHITECTURE.md",
    "INTEGRATION_EVENT_ARCHITECTURE.md",
]

ADR_FIELDS = [
    "ADR ID:", "Title:", "Architecture Domain:", "Decision Required:", "Status:",
    "Context:", "Options:", "Recommended Option:", "Rationale:",
    "Positive Consequences:", "Negative Consequences", "Dependencies:",
    "Architecture Owner:", "Independent Reviewer:", "Target Decision Date:",
    "Evidence References:", "Related Risks:", "Gate Impact:",
]

results = []  # (check_id, title, passed, details[])


def add(check_id, title, passed, details):
    results.append((check_id, title, passed, details))


def read(fname):
    with open(os.path.join(PKG, fname), encoding="utf-8") as fh:
        return fh.read()


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# Check 1 — required files exist
def check_files_exist():
    missing = [f for f in REQUIRED_FILES if not os.path.isfile(os.path.join(PKG, f))]
    add("01", "Required State 03 files exist", not missing,
        ["Missing: " + m for m in missing] or ["All %d required files present" % len(REQUIRED_FILES)])


# Check 2 — evidence register paths resolve
def check_evidence_paths():
    text = read("STATE03_EVIDENCE_REGISTER.md")
    paths = sorted(set(re.findall(
        r"99_SMEsPlus_Enterprise_Suite/03_Architecture/STATE03_ARCHITECTURE_ACCELERATION/[A-Za-z0-9_]+\.md",
        text)))
    missing = [p for p in paths if not os.path.isfile(os.path.join(REPO_ROOT, p))]
    add("02", "Evidence Register paths resolve", not missing,
        ["Unresolved: " + m for m in missing] or ["All %d evidence paths resolve" % len(paths)])


# Check 3 — 26 sections in every ARC-WP document
def check_26_sections():
    bad = []
    for f in ARC_WP_FILES:
        text = read(f)
        missing = [n for n in range(1, 27) if not re.search(r"(?m)^##\s+%d\." % n, text)]
        if missing:
            bad.append("%s missing sections %s" % (f, missing))
    add("03", "Every ARC-WP document contains the required 26 sections", not bad,
        bad or ["All %d ARC-WP documents have sections 1..26" % len(ARC_WP_FILES)])


# Check 4 — every ADR contains all mandatory fields
def check_adr_fields():
    text = read("ARCHITECTURE_DECISION_REGISTER.md")
    blocks = re.split(r"(?m)^###\s+ADR-ARC-(\d{3})\s*$", text)
    bad = []
    ids = []
    # re.split yields [pre, id1, body1, id2, body2, ...]
    for i in range(1, len(blocks), 2):
        adr_id = blocks[i]
        body = blocks[i + 1]
        ids.append(adr_id)
        missing = [fld for fld in ADR_FIELDS if fld not in body]
        if missing:
            bad.append("ADR-ARC-%s missing %s" % (adr_id, missing))
    if len(ids) != 19:
        bad.append("Expected 19 ADR detail blocks, found %d" % len(ids))
    add("04", "Every ADR contains all mandatory fields (19 ADRs)", not bad,
        bad or ["All 19 ADRs contain the 18 mandatory fields"])


# Check 5 — no prohibited approval statuses asserted
def check_no_prohibited_status():
    # Prohibited when ASSERTED as an approval/status, not when prohibited/discussed.
    negation = re.compile(r"(?i)\b(not|never|no|must not|cannot|prohibit|do not|avoid|without|remain|reserved)\b")
    patterns = {
        "APPROVED BY BOSS (AI must not assign)": re.compile(r"(?i)status:\s*APPROVED BY BOSS"),
        "READY FOR BUILD": re.compile(r"(?i)\bREADY FOR BUILD\b"),
        "RELEASE READY": re.compile(r"(?i)\bRELEASE READY\b"),
        "PRODUCTION READY": re.compile(r"(?i)\bPRODUCTION READY\b"),
        "BUILD READY (declared)": re.compile(r"(?i)\bBUILD READY\b"),
    }
    hits = []
    for f in REQUIRED_FILES:
        for ln, line in enumerate(read(f).splitlines(), 1):
            for label, pat in patterns.items():
                if pat.search(line) and not negation.search(line):
                    hits.append("%s:%d asserts %s -> %s" % (f, ln, label, line.strip()[:80]))
    add("05", "No prohibited approval status asserted", not hits,
        hits or ["No asserted prohibited approval statuses (prohibitions/discussion excluded)"])


# Check 6 — no Architecture Gate marked PASS
def check_no_gate_pass():
    neg = re.compile(r"(?i)\b(not|never|no|must not|cannot|prohibit|do not|does not|without|instead of)\b")
    pat = re.compile(r"(?i)gate\s*[abcd]\b[^.\n]{0,40}\bpass\b|\bpass\b[^.\n]{0,20}gate\s*[abcd]\b")
    hits = []
    for f in REQUIRED_FILES:
        for ln, line in enumerate(read(f).splitlines(), 1):
            if pat.search(line) and not neg.search(line):
                hits.append("%s:%d -> %s" % (f, ln, line.strip()[:80]))
    add("06", "No Architecture Gate marked PASS", not hits,
        hits or ["No gate is asserted as PASS"])


# Check 7 — no deliverable marked VERIFIED
def check_no_verified():
    # 'NOT VERIFIED' allowed; 'independently verified' in negated control statements allowed.
    neg = re.compile(r"(?i)\b(not|never|no|only the|may only|cannot|has not been|reserved)\b")
    pat = re.compile(r"(?i)(?<!not )\bVERIFIED\b")
    hits = []
    for f in REQUIRED_FILES:
        for ln, line in enumerate(read(f).splitlines(), 1):
            for m in re.finditer(r"(?i)\bVERIFIED\b", line):
                start = max(0, m.start() - 4)
                if line[start:m.start()].upper().endswith("NOT "):
                    continue
                if neg.search(line):
                    continue
                hits.append("%s:%d -> %s" % (f, ln, line.strip()[:80]))
                break
    add("07", "No deliverable marked VERIFIED by Claude", not hits,
        hits or ["No deliverable asserts VERIFIED status"])


# Check 8 — markdown code fences balanced
def check_fences():
    bad = []
    for f in REQUIRED_FILES + [VALIDATOR.replace(".py", ".py")]:
        if not f.endswith(".md"):
            continue
        n = read(f).count("```")
        if n % 2 != 0:
            bad.append("%s has odd fence count %d" % (f, n))
    add("08", "Markdown code fences balanced", not bad,
        bad or ["All markdown code fences balanced"])


# Check 9 — mermaid present where required
def check_mermaid():
    bad = []
    for f in MERMAID_REQUIRED:
        if "```mermaid" not in read(f):
            bad.append("%s missing mermaid block" % f)
    add("09", "Mermaid blocks present where required", not bad,
        bad or ["All %d diagram documents contain a mermaid block" % len(MERMAID_REQUIRED)])


# Check 10 — SHA-256 manifest matches current files
def check_manifest():
    mtext = read(MANIFEST)
    recorded = {}
    for line in mtext.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            recorded[parts[-1]] = parts[0]
    current = {}
    for f in os.listdir(PKG):
        if (f.endswith(".md") or f.endswith(".py")) and f not in MANIFEST_EXCLUSIONS:
            current[f] = sha256_file(os.path.join(PKG, f))
    problems = []
    for f, h in current.items():
        if f not in recorded:
            problems.append("%s not in manifest" % f)
        elif recorded[f] != h:
            problems.append("%s hash mismatch" % f)
    for f in recorded:
        if f not in current and f not in MANIFEST_EXCLUSIONS:
            problems.append("%s in manifest but missing/excluded" % f)
    add("10", "SHA-256 manifest matches current files (excl. manifest+report, documented)",
        not problems, problems or ["Manifest matches %d package files" % len(current)])


# Check 11 — no missing Owner or Reviewer
def check_owner_reviewer():
    bad = []
    for f in ARC_WP_FILES:
        text = read(f)
        if "Architecture Owner" not in text:
            bad.append("%s missing Architecture Owner" % f)
        if "Independent Reviewer" not in text and "ChatGPT L99" not in text:
            bad.append("%s missing Independent Reviewer" % f)
    add("11", "No missing Owner or Reviewer", not bad,
        bad or ["All ARC-WP documents name an Owner and Reviewer"])


# Check 12 — no missing Gate Impact
def check_gate_impact():
    bad = [f for f in ARC_WP_FILES if not re.search(r"(?mi)^##\s+24\.\s+Gate Impact", read(f))]
    add("12", "No missing Gate Impact section", not bad,
        ["Missing Gate Impact: " + b for b in bad] or ["All ARC-WP documents contain a Gate Impact section"])


# Check 13 — no evidence path points outside the approved package without explanation
def check_paths_scope():
    text = read("STATE03_EVIDENCE_REGISTER.md")
    ext = sorted(set(re.findall(r"99_SMEsPlus_Enterprise_Suite/[A-Za-z0-9_./-]+\.(?:md|txt)", text)))
    outside = [p for p in ext if "STATE03_ARCHITECTURE_ACCELERATION" not in p]
    # Any outside reference must be an explained cross-reference; none expected in the register.
    add("13", "No evidence path points outside the approved package without explanation",
        not outside, ["Outside package: " + o for o in outside] or
        ["All evidence paths are within the State 03 package"])


def main():
    for fn in (check_files_exist, check_evidence_paths, check_26_sections, check_adr_fields,
               check_no_prohibited_status, check_no_gate_pass, check_no_verified, check_fences,
               check_mermaid, check_manifest, check_owner_reviewer, check_gate_impact,
               check_paths_scope):
        try:
            fn()
        except Exception as exc:  # a failed check must not crash the validator
            add("ERR", fn.__name__, False, ["Exception: %r" % exc])

    passed = sum(1 for *_, ok, _ in [(r[0], r[1], r[2], r[3]) for r in results] if ok)
    total = len(results)
    all_ok = passed == total

    print("State 03 Package Validation: %d/%d checks passed" % (passed, total))
    for cid, title, ok, details in results:
        print("  [%s] %-4s %s" % ("PASS" if ok else "FAIL", cid, title))
        if not ok:
            for d in details:
                print("        - %s" % d)

    if "--report" in sys.argv:
        write_report(passed, total, all_ok)
    return 0 if all_ok else 1


def write_report(passed, total, all_ok):
    lines = []
    lines.append("# State 03 Architecture Package — Automated Validation Report")
    lines.append("")
    lines.append("Session: [SMEPLUS-26-07-10-001]  Control Level: /L99.99  Gate Status: HOLD")
    lines.append("Validation Timestamp: 2026-07-14")
    lines.append("Branch: claude/state-03-architecture-deliverables-su8cg6")
    lines.append("Correction Commit SHA: PENDING (recorded in PR #26 and Evidence Register after commit)")
    lines.append("Validator: %s  Version: %s" % (VALIDATOR, VALIDATOR_VERSION))
    lines.append("")
    lines.append("> Automated validation is NOT independent architecture approval. "
                 "It does not approve any gate and does not mark any deliverable VERIFIED. "
                 "Independent ChatGPT L99 review and Boss final decision remain mandatory.")
    lines.append("")
    lines.append("## Result: %s (%d/%d checks passed)" % (
        "ALL CHECKS PASSED" if all_ok else "FAILURES PRESENT", passed, total))
    lines.append("")
    lines.append("| Check | Description | Result |")
    lines.append("|---|---|---|")
    for cid, title, ok, _ in results:
        lines.append("| %s | %s | %s |" % (cid, title, "PASS" if ok else "FAIL"))
    lines.append("")
    lines.append("## Details")
    for cid, title, ok, details in results:
        lines.append("")
        lines.append("### Check %s — %s — %s" % (cid, title, "PASS" if ok else "FAIL"))
        for d in details:
            lines.append("- %s" % d)
    if all_ok:
        lines.append("")
        lines.append("## Failed Items")
        lines.append("- None.")
    lines.append("")
    lines.append("## Control Statement")
    lines.append("Automated validation confirms structural and evidence-integrity checks only. "
                 "It is not independent architecture approval. No Architecture Gate has been approved, "
                 "and no deliverable has been independently verified.")
    lines.append("")
    with open(os.path.join(PKG, REPORT), "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print("Wrote %s" % REPORT)


if __name__ == "__main__":
    sys.exit(main())
