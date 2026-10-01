# Correction packet U10-R2 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer: no vendor structure. Supersedes the neutral statements named in the restricted packet header.

- **WHAT:** What happens when an accounting entry is posted with a date inside a closed period.
- **BUSINESS RULE:** Posting does not fail; the entry is re-dated to the first open date and posted. [N-U10R2-001]
- **CONSTRAINT:** Once entries are posted, changing their date or state, resetting them or deleting them inside a closed period is refused. [N-U10R2-002]
- **DEPENDENCY:** Automatically generated entries, including the stock closing entry and valuation entries, follow the same re-dating rule. [N-U10R2-003]
- **RISK:** A closed period can therefore receive no new postings but reports for the following period can change; designs that assume rejection of back-dated automatic postings are wrong. [N-U10R2-003]
- **UNKNOWN:** The exact date assigned for each type of lock, and its effect on numbering and period reports, require runtime confirmation.
