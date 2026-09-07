#!/usr/bin/env python3
"""P11 CORR3 intake instrument

DEFECT (fifth instrument failure, caught on first publication run):
  `git ls-tree` scopes to the CURRENT DIRECTORY PREFIX unless --full-tree is given.
  Run from a subdirectory it returned 0 for every derivation. The original CORR3 run
  happened to execute from the repo root, so the published numbers are unaffected --
  but the script as first written was not portable, and a reader running it from the
  instrument directory would have got zeros and concluded the population was empty.
  Fixed with --full-tree. This is the same class as every other failure in this round:
  an unstated assumption about context.
 — PUBLISHED AFTER THE CHALLENGE, per B-27 / E2-C1 / E4-M-1.

This is the exact code that produced D1=55, D2=48, D3=155, UNION=212 at 9356557.
It is published so a reader can re-execute and disagree. It is NOT a certified
instrument: the challenge established four defects in it, recorded inline below.
"""
import subprocess, re, collections, sys

PEERS = [("P01","b820b29","research/account-p01-procure-to-pay-2026-09-04-001"),
         ("P02","7cb1c27","research/account-p02-order-to-cash-2026-09-04-001"),
         ("P03","bc767a8","research/account-p03-manufacture-to-cost-2026-09-04-001"),
         ("P04","65b8841","research/account-p04-acquire-to-retire-2026-09-04-001"),
         ("P05","205e0ac","research/account-p05-expense-to-pay-2026-09-04-001"),
         ("P06","1b018c1","research/account-p06-bank-to-reconcile-2026-09-04-001"),
         ("P07","ee2be30","research/account-p07-th-tax-compliance-2026-09-04-001"),
         ("P08","00ccd66","research/account-p08-record-to-report-2026-09-04-001"),
         ("P09","4778792","research/account-p09-plan-to-analyze-2026-09-04-001"),  # re-pinned 2026-09-07 (Q-P11-01): 92de8a1 was a PROMPT commit
         ("P10","1fea562","research/account-p10-time-based-recognition-2026-09-04-001")]

TOKENS = ("CORE_RECON","P11","POST_PUBLICATION","CORRECTION","SUPERSED","WITHDRAW")
TAIL = 5   # DEFECT E2-C8 / E4-R1: unjustified. D26 sits at -2, so TAIL=2 would pass.
           # The 10-member control returns 10/10 at TAIL=2,3,4,5 while D3 moves 117->207.
SERIES_RE = re.compile(r'^([A-Za-z]{0,3})(\d+)_')   # DEFECT E2-C2 / E4-M-2: never published in prose.

def tree(ref):
    return subprocess.run(["git","ls-tree","-r","--full-tree","--name-only",ref],
                          capture_output=True,text=True).stdout.split("\n")

def carries_peer_id(basename, peer):
    # DEFECT E2-C2 / E4-R3: RAW SUBSTRING, no word boundary.
    # 'P04' matches 'STEP0401'; 26 State-02 migration artefacts enter under P04 alone.
    return peer in basename

def main():
    D1,D2,D3 = set(), set(), set()
    for peer, sha, br in PEERS:
        files = [f for f in tree("origin/"+br) if f.endswith(".md")]
        # ---- D1: basename carries peer id AND one of six tokens
        for f in files:
            b = f.rsplit("/",1)[-1]
            if carries_peer_id(b,peer) and any(t in b for t in TOKENS):
                D1.add((peer,b))
        # ---- D2: file CONTENT has a markdown heading naming P11
        out = subprocess.run(["git","grep","-l","-E",r'^#{1,4} .*P11',"origin/"+br,"--","*.md"],
                             capture_output=True,text=True).stdout.split("\n")
        for line in out:
            if ":" in line:
                D2.add((peer, line.split(":",1)[1].rsplit("/",1)[-1]))
        # ---- D3: last TAIL members of every (directory, series-prefix) group
        series = collections.defaultdict(list)
        for f in files:
            d,_,b = f.rpartition("/")
            if not carries_peer_id(b,peer): continue
            m = SERIES_RE.match(b)
            if m: series[(d,m.group(1))].append((int(m.group(2)), b))
        for key, items in series.items():
            items.sort()          # DEFECT E2-C7 / E4-C3: sorts by the PARSED INTEGER where the
                                  # regex matches, but the regex matches only NN_-style names.
                                  # Un-numbered groups never enter D3 at all under this regex,
                                  # which is why P11's D3 (155) is smaller than a reader's
                                  # reconstruction from the prose (212). The PROSE, not the code,
                                  # is what was published -- E2-C1.
            for _, b in items[-TAIL:]:
                D3.add((peer,b))
    # DEFECT E2-C15: the (peer, BASENAME) key collapses distinct paths.
    # P09_CHECKPOINT_REGISTER.md exists at 5 paths, P09_AUTO_RESUME_STATE.md at 5;
    # the DIRECTORY is the only generation discriminator. 10 paths -> 2 keys.
    U = D1|D2|D3
    for name,s in (("D1",D1),("D2",D2),("D3",D3),("UNION",U)):
        print("%-6s %d"%(name,len(s)))
    with open("union_212.txt","w") as fh:
        for p,b in sorted(U): fh.write("%s|%s\n"%(p,b))
    print("A_INTERSECT_B", len(D1&D2), " A_MINUS_B", len(D1-D2), " B_MINUS_A", len(D2-D1))

if __name__ == "__main__":
    main()
