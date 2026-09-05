import subprocess,re,os
DUMPS={
 "BK12MAY26":"/Users/admin/Downloads/BK12MAY26_2026-08-03_05-48-30.dump",
 "iTEST02":"/Users/admin/Downloads/iTEST02_2026-07-14_16-34-51.dump",
 "iSMEs":"/Users/admin/Downloads/iSMEs_2026-07-11_05-03-27.dump",
 "iEVING":"/Users/admin/Downloads/iEVING_2026-07-23_10-31-06.dump",
}
TABLES=["mrp_workcenter","mrp_production","mrp_workorder","mrp_bom","mrp_workcenter_productivity","account_analytic_account","account_asset","res_company"]
def count(dump,tbl):
    p=subprocess.run(["pg_restore","-f","-","--data-only","-t",tbl,dump],capture_output=True,text=True,errors="replace")
    if p.returncode!=0 and not p.stdout: return "ERR"
    cur=None;n=0;tot=None
    for line in p.stdout.splitlines():
        m=re.match(r'^COPY public\.(\w+) \(',line)
        if m: cur=m.group(1); n=0; continue
        if cur is not None:
            if line=='\\.':
                if cur==tbl: tot=(tot or 0)+n
                cur=None; continue
            n+=1
    return tot if tot is not None else "NO TABLE"
print("=== EXECUTED: row counts across ALL FOUR deployed database dumps ===")
print(f"{'table':<30}"+"".join(f"{d:>14}" for d in DUMPS))
for t in TABLES:
    print(f"{t:<30}"+"".join(f"{str(count(p,t)):>14}" for p in DUMPS.values()))
