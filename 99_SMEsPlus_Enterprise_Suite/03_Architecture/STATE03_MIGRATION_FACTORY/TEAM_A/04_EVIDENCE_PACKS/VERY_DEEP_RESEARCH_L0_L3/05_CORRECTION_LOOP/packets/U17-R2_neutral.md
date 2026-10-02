# Correction packet U17-R2 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer: no vendor structure. Supersedes the neutral statements named in the restricted packet header.

- **WHAT:** When an automated period-closing challenge hands out its end-of-period rewards.
- **BUSINESS RULE:** For challenges with daily, weekly, monthly or yearly periodicity the end-of-period completion check is a string comparison that always mismatches; end-of-period rewards and final-rank badges are therefore not distributed automatically at period end, only when a challenge is manually closed. [N-U17R2-001] [N-U17R2-002]
- **RISK:** Any design that expects the gamification system to distribute completion rewards automatically at period end would not work. [N-U17R2-002]
- **UNKNOWN:** The runtime effect on a closing call and whether any separate cron triggers the force path require execution confirmation.
