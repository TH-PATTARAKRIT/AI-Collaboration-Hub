# FDS Factory Best Practice

Owner: Functional Specification AI
Reviewers: PMO AI
Status: Draft

## Principles
- Enterprise FDS Factory principle: repeatable, evidence-traceable FDS generation,
  not one-off manual drafting.
- Provider-agnostic AI design: pipeline logic must not hard-depend on one AI vendor.
- Human-in-the-loop: every gate requires a named reviewer before advancing state.
- Evidence register: every requirement traced to MATCHED / PARTIAL / GAP / NEW / RETIRE.
- Traceability matrix: every FDS section links back to a requirement ID and forward
  to acceptance criteria and test cases.

## Stop Rule
If repository, folder, naming, reviewer, or evidence mapping is missing, stop and
report the missing mapping rather than guessing. No Evidence = No Progress.

## No automatic approval
This factory pipeline may produce drafts only. It must never mark its own output
as PASS, Approved, Build Ready, or Production Ready.
