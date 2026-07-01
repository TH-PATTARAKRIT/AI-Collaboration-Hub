# iTEST02 Clean Room Policy

## Scope
Applies to all handling of the iTEST02 database dump, restored databases, derived extracts, diagrams, logs, and AI-assisted analysis.

## Policy
1. Restore only in an isolated, access-controlled environment.
2. Do not expose row-level sensitive data to AI systems.
3. Do not commit dump files or restored extracts to GitHub.
4. Commit only metadata, diagrams, design notes, evidence templates, and masked summaries.
5. Keep restore logs free of secrets.
6. Use owner approval before sharing any derived dataset.

## Decision Rule
No masking evidence means no dataset sharing.
No restore evidence means no migration readiness.
No owner signoff means no business approval.
