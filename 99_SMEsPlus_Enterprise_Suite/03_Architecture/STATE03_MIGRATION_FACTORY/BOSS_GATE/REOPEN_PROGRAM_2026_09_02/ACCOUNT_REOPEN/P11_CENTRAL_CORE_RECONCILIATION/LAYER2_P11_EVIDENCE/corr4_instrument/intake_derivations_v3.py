#!/usr/bin/env python3
"""P11 CORR4 intake instrument — B-35 REBUILD.

SUPERSEDES, does not replace:
  intake_derivations.py         @ 002748d   (original; pin table bound and never read)
  intake_derivations_pinned.py  @ 9d4ecdc   (CO-F-01 pin repair; six defects preserved,
                                             deliberately, so the pin delta stayed readable)
Both are retained as lineage. This file repairs the six.

>>> WHAT B-35 SAID, AND WHAT IS DONE ABOUT EACH <<<

  1. LEXICAL TAIL              D3 sorted a numeric filename prefix and kept the last N.
                               Filename order is not evidence order.
     REPAIR                    D3 orders by COMMIT CHRONOLOGY - the author date of the
                               last commit that touched each path at the pinned tree -
                               and the ordering is PRINTED so it can be disputed.

  2. GENERATION-DISCARDING KEY The identity key was the basename. Two generations of the
                               same document at different paths collapsed into one member.
     REPAIR                    The key is (peer, FULL PATH). Basenames are printed for
                               readability and are never the key. The instrument REPORTS
                               how many basenames carry more than one path, which is the
                               exact quantity the old key destroyed.

  3. SUBSTRING MEMBERSHIP      `peer in basename` matched any occurrence anywhere.
     REPAIR                    A bounded identifier: the peer token must be delimited on
                               both sides by a non-alphanumeric or a string boundary.
                               The instrument PRINTS what the two rules disagree about,
                               so the repair is measured rather than asserted.

  4. TAUTOLOGICAL BLIND SPOT   A blind-spot table asserted from the instrument's own
                               definitions, published as if executed.
     REPAIR                    NO blind-spot table is emitted. What is emitted is a
                               MEASURED complement: every .md path at each pinned tree
                               that NO derivation selected, counted. A blind spot you can
                               count is evidence; one you can define is a definition.

  5. FITTED TAIL=5             A bound with no sensitivity proof.
     REPAIR                    The population is UNBOUNDED by default. `--tail N` still
                               exists, solely so the sensitivity curve can be printed;
                               the default run applies no bound at all, and the curve is
                               printed so any future bound must argue against real numbers.

  6. VACUOUS FAILURE CONTROL   A control that could not fail.
     REPAIR                    Three controls that CAN fail, run with --controls:
                                 NEG   an impossible pin must FAIL-CLOSED exit 3
                                 NEG2  a prompt commit must FAIL-CLOSED exit 3 (P11-G-10)
                                 POS   an injected synthetic path must ENTER the union,
                                       proving the selector can admit a new member
                               Each prints EXPECTED before OBSERVED.

  7. FROZEN PEER SHAs          Honoured explicitly: every tree resolves the declared pin,
                               never "origin/"+branch. Validated fail-closed before any
                               derivation - resolvable, a commit, unique, an ancestor of
                               its declared branch, and substantive under P11-G-10.

UNIT         one (peer, full path) pair.
POPULATION   every *.md path in the pinned tree of each declared peer.
PATH SET     the pinned tree in full. No directory, volume or depth restriction.
SCOPE        intake selection only. This instrument selects what P11 must READ. It makes
             no claim about any peer's findings and does not re-derive peer evidence.

EXIT  0 measured · 2 bad invocation/not a repo · 3 fail-closed (pin validation)
"""
import argparse, collections, os, re, subprocess, sys

CORR3_PINS = [("P01","b820b29","research/account-p01-procure-to-pay-2026-09-04-001"),
              ("P02","7cb1c27","research/account-p02-order-to-cash-2026-09-04-001"),
              ("P03","bc767a8","research/account-p03-manufacture-to-cost-2026-09-04-001"),
              ("P04","65b8841","research/account-p04-acquire-to-retire-2026-09-04-001"),
              ("P05","205e0ac","research/account-p05-expense-to-pay-2026-09-04-001"),
              ("P06","1b018c1","research/account-p06-bank-to-reconcile-2026-09-04-001"),
              ("P07","ee2be30","research/account-p07-th-tax-compliance-2026-09-04-001"),
              ("P08","00ccd66","research/account-p08-record-to-report-2026-09-04-001"),
              ("P09","4778792","research/account-p09-plan-to-analyze-2026-09-04-001"),
              ("P10","1fea562","research/account-p10-time-based-recognition-2026-09-04-001")]

# 2026-09-08 one-prompt final closure: the three Account owners that published new
# immutable SHAs in this same prompt. P07 is unchanged and READ-ONLY.
FINAL_PINS = [("P01","b820b29","research/account-p01-procure-to-pay-2026-09-04-001"),
              ("P02","7cb1c27","research/account-p02-order-to-cash-2026-09-04-001"),
              ("P03","bc767a8","research/account-p03-manufacture-to-cost-2026-09-04-001"),
              ("P04","65b8841","research/account-p04-acquire-to-retire-2026-09-04-001"),
              ("P05","205e0ac","research/account-p05-expense-to-pay-2026-09-04-001"),
              ("P06","a533fe92d6f6855e0b362179403476520cc9aafa","corr/p06-one-prompt-final-2026-09-08-001"),
              ("P07","ee2be30","research/account-p07-th-tax-compliance-2026-09-04-001"),
              ("P08","f0cf287ac9f4ad37b0c19145df4a0e396af84c13","corr/p08-one-prompt-final-2026-09-08-001"),
              ("P09","ab8c0131c46e8154ad7efae18de2a54af2f17362","corr/p09-one-prompt-final-2026-09-08-001"),
              ("P10","1fea562","research/account-p10-time-based-recognition-2026-09-04-001")]

TOKENS = ("CORE_RECON","P11","POST_PUBLICATION","CORRECTION","SUPERSED","WITHDRAW")
SHA_RE = re.compile(r'^[0-9a-f]{7,40}$')
PROMPT_RE = re.compile(r'^\s*prompt\b', re.I)


def sh(a): return subprocess.run(a, capture_output=True, text=True)


def goto_toplevel():
    """DEFECT 8 REPAIR — cwd independence.

    `git grep <ref> -- "*.md"` and `git log <ref> -- <path>` interpret their pathspec
    RELATIVE TO THE CURRENT DIRECTORY. Run from inside the package, D2 returned 0 and
    every commit time returned 0; run from the repository root, D2 returns real hits.
    A cwd-dependent path set is a silent narrowing: the instrument reported an empty
    derivation as a result rather than as a scope error. Every path-limited command
    below now runs from the toplevel, and `--run-location-control` proves it.
    """
    top = sh(["git", "rev-parse", "--show-toplevel"]).stdout.strip()
    if not top:
        print("not a git repository", file=sys.stderr); sys.exit(2)
    os.chdir(top)
    return top


def die(peer, why):
    print("PIN VALIDATION FAILED  peer=%s  %s" % (peer, why), file=sys.stderr)
    print("FAIL-CLOSED: no derivation performed.", file=sys.stderr)
    sys.exit(3)


def bounded_peer(path_or_name, peer):
    """DEFECT 3 REPAIR. The peer token must be delimited on both sides.

    `peer in name` matched P01 inside 'P011', inside 'XP01', and inside any prose the
    filename happened to carry. This requires a boundary, so a token is a token.
    """
    return re.search(r'(?<![A-Za-z0-9])' + re.escape(peer) + r'(?![0-9])',
                     path_or_name) is not None


def apply_override(pins):
    """Control hook. P11_PIN_OVERRIDE='PEER=SHA' replaces one pin, so the NEG controls
    exercise the real validation path instead of a copy of it. Unset in every real run,
    and the substitution is PRINTED whenever it fires."""
    ov = os.environ.get("P11_PIN_OVERRIDE")
    if not ov or "=" not in ov:
        return pins
    who, sha = ov.split("=", 1)
    print("!! CONTROL OVERRIDE ACTIVE: %s pin replaced by %r" % (who, sha))
    return [(p, sha if p == who else s, b) for p, s, b in pins]


def validate_pins(pins, label):
    print("== PIN TABLE HONOURED BY THIS RUN (%s) ==" % label)
    seen = set()
    for peer, sha, br in pins:
        if not sha:               die(peer, "pin MISSING")
        if not SHA_RE.match(sha): die(peer, "pin MALFORMED: %r" % sha)
        r = sh(["git", "rev-parse", "--verify", "--quiet", sha + "^{commit}"])
        if r.returncode != 0 or not r.stdout.strip():
            die(peer, "pin UNRESOLVED or not a commit: %s" % sha)
        full = r.stdout.strip()
        if full in seen: die(peer, "pin DUPLICATE across peers: %s" % sha)
        seen.add(full)
        if sh(["git", "merge-base", "--is-ancestor", full, "origin/" + br]).returncode != 0:
            die(peer, "pin NOT AN ANCESTOR of declared branch %s" % br)
        subj = sh(["git", "log", "-1", "--format=%s", full]).stdout.strip()
        if PROMPT_RE.match(subj):
            die(peer, "pin NON-SUBSTANTIVE under P11-G-10 (prompt commit): %s %r" % (sha, subj))
        print("   %-4s %s  %s" % (peer, full, subj[:70]))
    print("== all %d pins resolved, substantive, ancestors of their declared branch ==\n" % len(pins))


def commit_time(ref, path):
    """DEFECT 1 REPAIR. Evidence chronology: author time of the last commit touching path."""
    r = sh(["git", "log", "-1", "--format=%at", ref, "--", ":(top)" + path])
    t = r.stdout.strip()
    return int(t) if t.isdigit() else 0


def derive(pins, tail=None, inject=None, quiet=False):
    D1, D2, D3 = set(), set(), set()
    allmd = set()
    substring_only = []            # what the OLD rule would have added and the new one does not
    basename_collisions = 0
    for peer, sha, br in pins:
        ref = sha
        files = [f for f in sh(["git", "ls-tree", "-r", "--full-tree", "--name-only", ref]
                               ).stdout.split("\n") if f.endswith(".md")]
        if inject and peer == inject[0]:
            files = files + [inject[1]]
        for f in files:
            allmd.add((peer, f))
        # DEFECT 2 REPAIR: key on the FULL PATH, never the basename.
        bn = collections.Counter(f.rsplit("/", 1)[-1] for f in files)
        basename_collisions += sum(1 for k, v in bn.items() if v > 1)

        for f in files:
            b = f.rsplit("/", 1)[-1]
            old = peer in b
            new = bounded_peer(b, peer)
            if old and not new:
                substring_only.append((peer, f))
            if new and any(t in b for t in TOKENS):
                D1.add((peer, f))

        for line in sh(["git", "grep", "-l", "-E", r'^#{1,4} .*P11', ref,
                        "--", ":(top,glob)**/*.md", ":(top,glob)*.md"]
                       ).stdout.split("\n"):
            if ":" in line:
                D2.add((peer, line.split(":", 1)[1]))

        # DEFECT 1 + 5 REPAIR: chronological order, UNBOUNDED by default.
        cand = [f for f in files if bounded_peer(f.rsplit("/", 1)[-1], peer)]
        cand.sort(key=lambda f: (commit_time(ref, f), f))
        chosen = cand if tail is None else cand[-tail:]
        for f in chosen:
            D3.add((peer, f))

    U = D1 | D2 | D3
    if not quiet:
        print("SELECTION  (unit = one (peer, FULL PATH) pair)")
        for name, s in (("D1", D1), ("D2", D2), ("D3", D3), ("UNION", U)):
            print("  %-6s %d" % (name, len(s)))
        print("  A_INTERSECT_B %d   A_MINUS_B %d   B_MINUS_A %d"
              % (len(D1 & D2), len(D1 - D2), len(D2 - D1)))
        print()
        print("DEFECT-2 MEASUREMENT — basenames carrying more than one path, per pinned tree")
        print("  %d   <-- members the basename key would have collapsed" % basename_collisions)
        print()
        print("DEFECT-3 MEASUREMENT — selected by RAW SUBSTRING but not by the bounded token")
        if substring_only:
            for p, f in sorted(substring_only)[:40]:
                print("  %-4s %s" % (p, f))
            print("  total %d" % len(substring_only))
        else:
            print("  0 — on THIS population the two rules agree.")
            print("  That is a MEASURED result, not a reason to keep the loose rule:")
            print("  the bounded rule is correct on populations where they differ, and")
            print("  nothing about this population guarantees the next one agrees.")
        print()
        print("DEFECT-4 REPAIR — MEASURED complement, not a defined blind spot")
        print("  *.md paths at the pinned trees            %d" % len(allmd))
        print("  selected by some derivation               %d" % len(U))
        print("  NOT selected by any derivation            %d   <-- the blind spot, counted"
              % (len(allmd) - len(U)))
    return D1, D2, D3, U, allmd


def controls(pins):
    """Three controls that CAN fail. Expected is printed before observed.

    Each NEG control re-invokes this same file as a subprocess with one pin overridden
    through P11_PIN_OVERRIDE (peer=sha), so the control exercises the REAL validation
    path rather than a reimplementation of it.
    """
    import subprocess as _sp
    me = os.path.abspath(__file__)
    ok = True
    print("=" * 78); print("CONTROLS — EXPECTED is printed before OBSERVED"); print("=" * 78)

    def run_with_override(ov):
        env = dict(os.environ); env["P11_PIN_OVERRIDE"] = ov
        return _sp.run([sys.executable, me, "--pinset", "corr3" if pins is CORR3_PINS else "final"],
                       capture_output=True, text=True, env=env)

    print("\nNEG   an unresolvable pin must FAIL-CLOSED")
    print("  EXPECTED  exit 3, message contains 'pin UNRESOLVED'")
    r = run_with_override("P01=0000000")
    first = next((l for l in r.stderr.splitlines() if "PIN VALIDATION" in l), "")
    print("  OBSERVED  exit %d   %s" % (r.returncode, first[:96]))
    ok &= (r.returncode == 3 and "UNRESOLVED" in r.stderr)

    print("\nNEG2  a PROMPT commit must FAIL-CLOSED under P11-G-10")
    print("  EXPECTED  exit 3, message contains 'NON-SUBSTANTIVE'")
    r = run_with_override("P09=92de8a1")
    first = next((l for l in r.stderr.splitlines() if "PIN VALIDATION" in l), "")
    print("  OBSERVED  exit %d   %s" % (r.returncode, first[:96]))
    ok &= (r.returncode == 3 and "NON-SUBSTANTIVE" in r.stderr)

    print("\nNEG3  a pin that is NOT an ancestor of its declared branch must FAIL-CLOSED")
    print("  EXPECTED  exit 3, message contains 'NOT AN ANCESTOR'")
    r = run_with_override("P01=" + sh(["git", "rev-parse", "HEAD"]).stdout.strip())
    first = next((l for l in r.stderr.splitlines() if "PIN VALIDATION" in l), "")
    print("  OBSERVED  exit %d   %s" % (r.returncode, first[:96]))
    ok &= (r.returncode == 3 and "NOT AN ANCESTOR" in r.stderr)

    print("\nPOS   an injected synthetic path must ENTER the union")
    print("  EXPECTED  union grows by exactly 1, and the new member IS the injected path")
    _, _, _, base, _ = derive(pins, quiet=True)
    path = "SYNTHETIC_CONTROL/P06_CORE_RECON_CORRECTION_CONTROL.md"
    _, _, _, grown, _ = derive(pins, inject=("P06", path), quiet=True)
    delta = grown - base
    print("  OBSERVED  union %d -> %d   delta = %s" % (len(base), len(grown), sorted(delta)))
    ok &= (len(grown) == len(base) + 1 and delta == {("P06", path)})

    print("\n%s" % ("CONTROLS — ALL FOUR BEHAVED AS EXPECTED"
                    if ok else "*** CONTROLS — AT LEAST ONE DID NOT BEHAVE AS EXPECTED"))
    return ok


def run_location_control(pinset):
    """A control the previous instrument could not have failed: run the SAME derivation
    from two different working directories and require identical output."""
    import subprocess as _sp
    me = os.path.abspath(__file__)
    top = sh(["git", "rev-parse", "--show-toplevel"]).stdout.strip()
    deep = os.path.dirname(me)
    print("=" * 78)
    print("RUN-LOCATION CONTROL — the derivation must not depend on where it is invoked")
    print("=" * 78)
    print("  EXPECTED  byte-identical stdout from the repo root and from a deep subdirectory")
    outs = {}
    for label, wd in (("toplevel", top), ("deep", deep)):
        r = _sp.run([sys.executable, me, "--pinset", pinset],
                    capture_output=True, text=True, cwd=wd)
        body = "\n".join(l for l in r.stdout.splitlines()
                          if not l.startswith("REPO TOPLEVEL"))
        outs[label] = body
        sel = next((l for l in body.splitlines() if l.strip().startswith("UNION")), "?")
        print("  cwd=%-9s exit %d   %s" % (label, r.returncode, sel.strip()))
    same = outs["toplevel"] == outs["deep"]
    print("  OBSERVED  identical: %s" % same)
    if not same:
        print("  *** the derivation is cwd-dependent — this is a scope defect, not a result")
    return same


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--pinset", choices=["corr3", "final"], default="final")
    ap.add_argument("--tail", type=int, default=None,
                    help="apply a tail bound; DEFAULT IS NONE (unbounded)")
    ap.add_argument("--sensitivity", action="store_true",
                    help="print the tail sensitivity curve instead of asserting a bound")
    ap.add_argument("--controls", action="store_true")
    ap.add_argument("--run-location-control", action="store_true")
    a = ap.parse_args()

    top = goto_toplevel()
    print("REPO TOPLEVEL (all path-limited git commands run from here): %s\n" % top)

    if a.run_location_control:
        sys.exit(0 if run_location_control(a.pinset) else 1)

    pins = CORR3_PINS if a.pinset == "corr3" else FINAL_PINS
    pins = apply_override(pins)
    validate_pins(pins, a.pinset)

    if a.controls:
        sys.exit(0 if controls(pins) else 1)

    if a.sensitivity:
        print("TAIL SENSITIVITY — the curve a bound would have to argue against")
        print("  %-10s %s" % ("tail", "UNION size"))
        for t in (1, 2, 3, 5, 8, 13, 21, None):
            _, _, _, U, _ = derive(pins, tail=t, quiet=True)
            print("  %-10s %d" % ("unbounded" if t is None else t, len(U)))
        return

    derive(pins, tail=a.tail)


if __name__ == "__main__":
    main()
