#!/bin/bash
# Regenerate the GB-08 evidence manifest. Run from ACCOUNT_WAVE_A_CORE_LEDGER.
#
# Two files are excluded by design, and the reason is the same in both cases:
# a document cannot contain its own digest.
#   - ACCOUNT_WAVE_A_GB08_EVIDENCE_MANIFEST_SHA256.md  -> holds the roll-up
#   - ACCOUNT_WAVE_A_GB08_PUBLICATION_RECORD.md        -> a receipt ABOUT the package,
#                                                         written after it is published,
#                                                         and it cites the roll-up
# The roll-up digest is therefore stable across the publication commit.
cd GB08_DECISION || exit 1
find . -type f \( -name '*.md' -o -name '*.sh' -o -name '*.txt' \) \
     ! -name 'ACCOUNT_WAVE_A_GB08_EVIDENCE_MANIFEST_SHA256.md' \
     ! -name 'ACCOUNT_WAVE_A_GB08_PUBLICATION_RECORD.md' -print0 \
  | sort -z | xargs -0 shasum -a 256
