#!/usr/bin/env python3
"""
BATCH FREEZE  v1.00
SMEsPlus Enterprise Suite · ROOM A

Freezes a question bank for a batch and writes the manifest that both lanes cite.
After a freeze, the questions for that batch cannot change without invalidating every
answer already filed against them (REV-A P5 qualifier, Rolling Batch Freeze permitted).

    python3 freeze_batch.py --batch W1-B01 --modules base,web --bank STANDARD_55.md [MVQ.md ...] \
        --authorization "Boss approve 2026-09-22" --out FREEZE_W1-B01.json

Writes a JSON manifest and prints the freeze hash. Refuses to run if the lint fails.
"""
import sys, os, json, hashlib, argparse, subprocess, datetime

def sha256(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--batch', required=True)
    ap.add_argument('--modules', required=True, help='comma-separated')
    ap.add_argument('--bank', required=True, nargs='+')
    ap.add_argument('--scope')
    ap.add_argument('--authorization', required=True, help='who authorised this freeze, and when')
    ap.add_argument('--out', required=True)
    ap.add_argument('--skip-lint', action='store_true')
    a = ap.parse_args()

    mods = [m.strip() for m in a.modules.split(',') if m.strip()]
    for p in a.bank:
        if not os.path.exists(p):
            sys.exit(f"FREEZE ABORT: {p} not found. (exit 2)")

    if not a.skip_lint:
        lint = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'question_bank_lint.py')
        if os.path.exists(lint):
            cmd = [sys.executable, lint] + a.bank + ['--modules', a.modules]
            if a.scope:
                cmd += ['--scope', a.scope]
            r = subprocess.run(cmd, capture_output=True, text=True)
            print(r.stdout)
            if r.returncode != 0:
                sys.exit("FREEZE ABORT: lint failed. Fix the defects above; do not freeze a defective bank. (exit 1)")
        else:
            print("WARNING: question_bank_lint.py not found next to this script — freezing unlinted.")

    files = {os.path.basename(p): sha256(p) for p in sorted(a.bank)}
    # the freeze hash binds the batch id, the module list and every bank file together
    payload = a.batch + '\n' + '\n'.join(sorted(mods)) + '\n' + \
              '\n'.join(f"{k}:{v}" for k, v in sorted(files.items())) + '\n'
    freeze_hash = hashlib.sha256(payload.encode()).hexdigest()

    manifest = {
        'batch_id': a.batch,
        'frozen_at': datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
        'authorization': a.authorization,
        'modules': sorted(mods),
        'module_count': len(mods),
        'bank_files': files,
        'freeze_hash': freeze_hash,
        'rules': {
            'standard_questions': 55,
            'module_specific_floor': 40,
            'combined_floor': 95,
            'floor_is': 'Minimum Research Depth — not a completion percentage, '
                        'not a Formal Coverage denominator',
            'join_key': 'MODULE + QID (Research Evidence Join Key only)',
            'layer_tag_required': True,
            'formal_coverage': 'NOT AUTHORIZED until a Canonical Function-ID denominator is Boss-frozen',
        },
        'after_freeze': 'Questions for this batch cannot change. A change invalidates every answer '
                        'already filed against them.',
    }
    with open(a.out, 'w') as fh:
        json.dump(manifest, fh, indent=2)
        fh.write('\n')

    print(f"\nBATCH FROZEN  {a.batch}")
    print(f"  modules      : {len(mods)}")
    print(f"  bank files   : {len(files)}")
    for k, v in files.items():
        print(f"     {v[:16]}…  {k}")
    print(f"  FREEZE HASH  : {freeze_hash}")
    print(f"  manifest     : {a.out}  (sha256 {sha256(a.out)[:16]}…)")
    print("\nBoth lanes must cite this freeze hash in every record and every batch report.")
    return 0

if __name__ == '__main__':
    sys.exit(main())
