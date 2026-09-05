import io, os, re, sys

LOCKS = ["fiscalyear_lock_date", "tax_lock_date", "sale_lock_date",
         "purchase_lock_date", "hard_lock_date"]


def cols(schema_path):
    ddl = io.open(schema_path, encoding='utf-8', errors='replace').read()
    m = re.search(r"CREATE TABLE public\.res_company \((.*?)\n\);", ddl, re.S)
    if not m:
        return None
    return [l.strip().split()[0] for l in m.group(1).strip().split("\n")]


def rows(data_path):
    out, inb = [], False
    for line in io.open(data_path, encoding='utf-8', errors='replace'):
        if line.startswith('COPY '):
            inb = True
            continue
        if inb:
            if line.startswith('\\.'):
                inb = False
                continue
            out.append(line.rstrip("\n").split("\t"))
    return out


for label, schema, data in [(a, b, c) for a, b, c in
                            (x.split(",") for x in sys.argv[1:])]:
    if not (os.path.exists(schema) and os.path.exists(data)):
        print("%s: MISSING artefact" % label)
        continue
    c = cols(schema)
    r = rows(data)
    print("%s | res_company columns=%d rows=%d | schema bytes=%d data bytes=%d"
          % (label, len(c) if c else -1, len(r),
             os.path.getsize(schema), os.path.getsize(data)))
    for lk in LOCKS:
        if c and lk in c:
            i = c.index(lk)
            vals = [x[i] for x in r if i < len(x)]
            setv = [v for v in vals if v not in ("\\N", "", None)]
            print("    %-24s present | set in %d of %d | values=%s"
                  % (lk, len(setv), len(vals), sorted(set(setv))[:5]))
        else:
            print("    %-24s ABSENT from res_company" % lk)
