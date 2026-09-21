#!/usr/bin/env python3
import argparse, os, re, sys

REQ = [
    'QID','MODULE','TYPE','AUTHOR','RISK_TIER','OUTPUT_CLASS',
    'HYPOTHESIS','WHY_IT_MATTERS','DISCONFIRMING_OBSERVATION',
    'EXPECTED_SURFACE','PRECONDITIONS'
]

def parse_module_questions(text, filename):
    blocks = re.findall(r'```yaml\n(.*?)\n```', text, flags=re.S)
    out=[]
    for b in blocks:
        fields={}
        for line in b.splitlines():
            m=re.match(r'^([A-Z_]+):\\s*(.*)$', line)
            if m:
                fields[m.group(1)] = m.group(2).strip()
        if 'QID' not in fields:
            continue
        missing=[k for k in REQ if k not in fields]
        if missing:
            raise ValueError(f'{filename}: {fields.get("QID","<unknown>")} missing {",".join(missing)}')
        if fields['TYPE'] != 'MODULE':
            raise ValueError(f'{filename}: {fields["QID"]} TYPE must be MODULE')
        out.append(fields)
    return out

def parse_standard(text, filename):
    ids=re.findall(r'\\*\\*STD-Q(\\d{2})\\s+—', text)
    if not ids:
        return []
    if len(ids) != 55 or len(set(ids)) != 55 or set(ids) != {f'{i:02d}' for i in range(1,56)}:
        raise ValueError(f'{filename}: STANDARD bank must contain exactly STD-Q01..STD-Q55 once each; found {len(ids)}')
    starts=[m.start() for m in re.finditer(r'\\*\\*STD-Q\\d{2}\\s+—', text)]
    starts.append(len(text))
    for i in range(len(starts)-1):
        block=text[starts[i]:starts[i+1]]
        qid=re.search(r'\\*\\*(STD-Q\\d{2})', block).group(1)
        if 'DISCONFIRM:' not in block:
            raise ValueError(f'{filename}: {qid} missing DISCONFIRM')
    return [f'STD-Q{i:02d}' for i in range(1,56)]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('bank', nargs='+')
    ap.add_argument('--modules', required=True)
    ap.add_argument('--scope')
    a=ap.parse_args()
    allowed=[x.strip() for x in a.modules.split(',') if x.strip()]
    qids=set(); counts={m:0 for m in allowed}; std=0; files=0
    errors=[]
    for p in a.bank:
        files += 1
        if not os.path.exists(p):
            errors.append(f'{p}: file not found')
            continue
        text=open(p,'r',encoding='utf-8').read()
        try:
            s=parse_standard(text,p)
            if s:
                std += len(s)
                for q in s:
                    if q in qids: errors.append(f'duplicate QID {q}')
                    qids.add(q)
            for f in parse_module_questions(text,p):
                q=f['QID']; m=f['MODULE']
                if q in qids: errors.append(f'duplicate QID {q}')
                qids.add(q)
                if m not in counts:
                    errors.append(f'{p}: {q} MODULE {m} not in --modules')
                else:
                    counts[m] += 1
                if not f['DISCONFIRMING_OBSERVATION']:
                    errors.append(f'{p}: {q} empty DISCONFIRMING_OBSERVATION')
        except ValueError as e:
            errors.append(str(e))

    if std not in (0,55):
        errors.append(f'STANDARD count invalid: {std}')

    module_total=sum(counts.values())
    if module_total:
        for m,c in counts.items():
            if c < 40:
                errors.append(f'{m}: module-specific floor not met ({c}/40)')

    if errors:
        print('QUESTION BANK LINT: FAIL')
        for e in errors: print(' -',e)
        return 1

    print('QUESTION BANK LINT: PASS')
    print(f' files={files} standard={std} module_specific={module_total} unique_qids={len(qids)}')
    if module_total:
        for m in sorted(counts): print(f' {m}: {counts[m]} MVQ')
    return 0

if __name__=='__main__':
    sys.exit(main())
