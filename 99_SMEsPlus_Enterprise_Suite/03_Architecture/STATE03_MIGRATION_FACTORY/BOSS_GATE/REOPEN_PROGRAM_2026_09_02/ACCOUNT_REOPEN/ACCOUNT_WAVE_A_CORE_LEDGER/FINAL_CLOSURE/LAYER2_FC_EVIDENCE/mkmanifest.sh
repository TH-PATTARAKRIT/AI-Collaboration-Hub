#!/bin/bash
# Regenerate the FC evidence manifest. Run from ACCOUNT_WAVE_A_CORE_LEDGER.
cd FINAL_CLOSURE || exit 1
find . -type f \( -name '*.md' -o -name '*.sh' \) ! -name 'ACCOUNT_WAVE_A_FINAL_EVIDENCE_MANIFEST_SHA256.md' -print0 \
  | sort -z | xargs -0 shasum -a 256
