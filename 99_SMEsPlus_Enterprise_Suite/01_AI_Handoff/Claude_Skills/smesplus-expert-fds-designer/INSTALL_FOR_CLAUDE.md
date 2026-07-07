# Install Guide: smesplus-expert-fds-designer

## Status

Prepared for SMEsPlus /L99.99 control.

This folder stores the Claude Skill content for repository-native use by Claude Code and as source material for Claude.ai Skill upload packaging.

## Files

- `SKILL.md` — main Claude Skill instructions.

## Recommended Use

### Claude Code / Repository Use

Open Claude Code inside the repository and instruct Claude:

```text
Use the SMEsPlus Expert FDS Designer Skill from:

99_SMEsPlus_Enterprise_Suite/01_AI_Handoff/Claude_Skills/smesplus-expert-fds-designer/SKILL.md

Apply this skill for all Functional Specification drafting, revision, gap analysis, evidence register, traceability matrix, UI handoff draft, and Boss Decision Pack draft work.

Before starting, declare Execution Mode.
Final status must be:
PREPARED ONLY / NOT APPROVED / REQUIRES CHATGPT L99 REVIEW
```

### Claude.ai Web Upload Use

To upload as a Claude.ai Skill, package the folder:

```text
smesplus-expert-fds-designer/
└── SKILL.md
```

into a ZIP file and upload it in Claude.ai Skills settings if the account supports custom Skills.

## Control Notes

- This Skill does not grant GitHub, Jira, Make, terminal, or external system access by itself.
- Claude must declare execution mode before work.
- Claude must not self-approve.
- ChatGPT L99 verifies evidence.
- PMO verifies governance.
- Boss gives final approval.

## GitHub Repository Copy

Repository:
`TH-PATTARAKRIT/AI-Collaboration-Hub`

Branch:
`SMEsPlus`

Path:
`99_SMEsPlus_Enterprise_Suite/01_AI_Handoff/Claude_Skills/smesplus-expert-fds-designer/`

## Final Required Statement

PREPARED ONLY / NOT APPROVED / REQUIRES CHATGPT L99 REVIEW
