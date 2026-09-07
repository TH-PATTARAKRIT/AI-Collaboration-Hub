#!/usr/bin/env python3
"""P11 CORR3 intake instrument — PIN-HONOURING REPAIR (CO-F-01)

SUPERSEDES, does not replace, `intake_derivations.py` @ 002748d, which is preserved
as lineage. The superseded file declared a (peer, sha, branch) pin table and then
resolved BOTH trees as "origin/"+branch. The `sha` column was bound and never read.
Proof: changing the P09 pin 4778792 -> 92de8a1 left stdout and union output
BYTE-IDENTICAL (RUN A vs RUN B).

WHAT THIS REPAIR CHANGES, AND ONLY THIS:
  1. both tree resolutions resolve the declared PIN, never "origin/"+branch;
  2. the pin table is validated and the instrument FAILS CLOSED, before any
     derivation, if any pin is missing / malformed / unresolvable / not a commit /
     not an ancestor of its declared branch / non-substantive under P11-G-10.

WHAT THIS REPAIR DELIBERATELY DOES NOT CHANGE:
  the four inline defects E2-C2/C7/C8/C15 (raw-substring peer match, integer-sort
  regex, unjustified TAIL=5, basename key). They are recorded, not repaired, because
  repairing them would move the population for a second, unrelated reason and make
  the pin delta unreadable. The instrument remains NOT CERTIFIED; B-35 stands.

P11-G-10 (governing control, from Q-P11-01): a frozen peer SHA must be a substantive
research commit. 92de8a1 was a PROMPT commit. Enforced here as a fail-closed check.
"""
import subprocess, re, collections, sys, os

PEERS = [("P01","b820b29","research/account-p01-procure-to-pay-2026-09-04-001"),
         ("P02","7cb1c27","research/account-p02-order-to-cash-2026-09-04-001"),
         ("P03","bc767a8","research/account-p03-manufacture-to-cost-2026-09-04-001"),
         ("P04","65b8841","research/account-p04-acquire-to-retire-2026-09-04-001"),
         ("P05","205e0ac","research/account-p05-expense-to-pay-2026-09-04-001"),
         ("P06","1b018c1","research/account-p06-bank-to-reconcile-2026-09-04-001"),
         ("P07","ee2be30","research/account-p07-th-tax-compliance-2026-09-04-001"),
         ("P08","00ccd66","research/account-p08-record-to-report-2026-09-04-001"),
         ("P09","4778792","research/account-p09-plan-to-analyze-2026-09-04-001"),
         ("P10","1fea562","research/account-p10-time-based-recognition-2026-09-04-001")]

TOKENS = ("CORE_RECON","P11","POST_PUBLICATION","CORRECTION","SUPERSED","WITHDRAW")
TAIL = 5
SERIES_RE = re.compile(r'^([A-Za-z]{0,3})(\d+)_')
SHA_RE = re.compile(r'^[0-9a-f]{7,40}$')
PROMPT_RE = re.compile(r'^\s*prompt\b', re.I)      # P11-G-10 non-substantive marker

def sh(args):
    return subprocess.run(args, capture_output=True, text=True)

def die(peer, why):
    print("PIN VALIDATION FAILED  peer=%s  %s" % (peer, why), file=sys.stderr)
    print("FAIL-CLOSED: no derivation performed.", file=sys.stderr)
    sys.exit(3)

def validate_pins():
    """Fail closed before any derivation. Prints the exact pin table actually used."""
    print("== PIN TABLE HONOURED BY THIS RUN ==")
    seen = set()
    for peer, sha, br in PEERS:
        if not sha:                        die(peer, "pin MISSING")
        if not SHA_RE.match(sha):          die(peer, "pin MALFORMED: %r" % sha)
        r = sh(["git","rev-parse","--verify","--quiet", sha+"^{commit}"])
        if r.returncode != 0 or not r.stdout.strip():
                                           die(peer, "pin UNRESOLVED or not a commit: %s" % sha)
        full = r.stdout.strip()
        if full in seen:                   die(peer, "pin DUPLICATE across peers: %s" % sha)
        seen.add(full)
        anc = sh(["git","merge-base","--is-ancestor", full, "origin/"+br])
        if anc.returncode != 0:            die(peer, "pin NOT AN ANCESTOR of declared branch %s" % br)
        subj = sh(["git","log","-1","--format=%s", full]).stdout.strip()
        if PROMPT_RE.match(subj):          die(peer, "pin NON-SUBSTANTIVE under P11-G-10 "
                                                     "(prompt commit): %s %r" % (sha, subj))
        print("   %-4s %s  %s" % (peer, full, subj[:72]))
    print("== all %d pins resolved, substantive, ancestors of their declared branch ==\n" % len(PEERS))

def tree(ref):
    return sh(["git","ls-tree","-r","--full-tree","--name-only",ref]).stdout.split("\n")

def carries_peer_id(basename, peer):
    return peer in basename          # E2-C2/E4-R3 preserved, not repaired

def main():
    if sh(["git","rev-parse","--show-toplevel"]).returncode != 0:
        print("not a git repository", file=sys.stderr); sys.exit(2)
    validate_pins()
    D1,D2,D3 = set(), set(), set()
    for peer, sha, br in PEERS:
        ref = sha                                     # <-- THE REPAIR (was "origin/"+br)
        files = [f for f in tree(ref) if f.endswith(".md")]
        for f in files:
            b = f.rsplit("/",1)[-1]
            if carries_peer_id(b,peer) and any(t in b for t in TOKENS):
                D1.add((peer,b))
        out = sh(["git","grep","-l","-E",r'^#{1,4} .*P11', ref,"--","*.md"]).stdout.split("\n")
        for line in out:
            if ":" in line:
                D2.add((peer, line.split(":",1)[1].rsplit("/",1)[-1]))
        series = collections.defaultdict(list)
        for f in files:
            d,_,b = f.rpartition("/")
            if not carries_peer_id(b,peer): continue
            m = SERIES_RE.match(b)
            if m: series[(d,m.group(1))].append((int(m.group(2)), b))
        for key, items in series.items():
            items.sort()
            for _, b in items[-TAIL:]:
                D3.add((peer,b))
    U = D1|D2|D3
    for name,s in (("D1",D1),("D2",D2),("D3",D3),("UNION",U)):
        print("%-6s %d"%(name,len(s)))
    outname = os.environ.get("P11_UNION_OUT","union_pinned.txt")
    with open(outname,"w") as fh:
        for p,b in sorted(U): fh.write("%s|%s\n"%(p,b))
    print("A_INTERSECT_B", len(D1&D2), " A_MINUS_B", len(D1-D2), " B_MINUS_A", len(D2-D1))

if __name__ == "__main__":
    main()
