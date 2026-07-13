# STATE 01 SOURCE OF TRUTH POLICY

Document ID: SMEPLUS-STATE01-SOT-001  
Version: 1.0  
Status: APPROVED BASELINE  
Approval Date: 2026-07-13

## Authority Rule

GitHub repository `TH-PATTARAKRIT/AI-Collaboration-Hub`, branch `SMEsPlus`, path `99_SMEsPlus_Enterprise_Suite/` is the authoritative controlled project baseline.

Google Drive is a collaboration and working-document location. A document becomes a controlled baseline only after it is published to GitHub with a traceable commit SHA and the required review/approval record.

Jira is the execution source for task ownership, status, blockers, and acceptance tracking. Jira status does not override GitHub evidence or gate records.

Figma is the design authority for approved screen and component designs. Figma evidence must include file URL, frame/component identifier, version/date, owner, and review status.

## Conflict Rule

When copies differ:

1. Use the latest approved GitHub baseline.
2. Do not treat Drive, chat, email, or AI output as approved unless linked to the GitHub baseline.
3. Record the conflict and owner.
4. Keep the affected gate on HOLD until the authoritative version is confirmed.

## Evidence Minimum

Every controlled deliverable requires item ID, owner, GitHub path or approved evidence location, timestamp, reviewer, verification status, and gate impact.