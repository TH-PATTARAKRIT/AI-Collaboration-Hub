# DISPATCHER_CONTROL_PACKET_TEMPLATE.md

CONTROL_EVENT_ID: <unique-id>
EVENT_TYPE: <NEW_CONTROL_PROMPT_COMMITTED | NEW_PEER_MATERIAL_DELTA | READY_TO_RESUME | DEPENDENCY_RESOLVED | CORRECTION_REQUIRED | READY_FOR_CORE_RECONCILIATION | READY_FOR_BOSS_FINAL_GATE>
PROJECT: SMEsPlus ENTERPRISE SUITE
PROCESS: <P01..P11 or domain>
LOGICAL_SESSION_ID: <id>
TARGET_MODE: <OLD_SESSION | CHILD_TASK | MANUAL_LAUNCHER>
TARGET_SESSION_NAME: <if known>
REPOSITORY: TH-PATTARAKRIT/AI-Collaboration-Hub
BRANCH: <branch>
BASE_SHA: <sha>
PROMPT_ID: <prompt-id>
PROMPT_PATH: <path>
LAST_VERIFIED_CHECKPOINT: <checkpoint>
CURRENT_CHECKPOINT: <checkpoint>
NEXT_EXACT_ACTION: <action>
MATERIAL_DELTA_REASON: <reason>
PEER_LAST_CONSUMED_SHA: <process=sha list>
OPEN_BLOCKERS: <ids>
OPEN_CONTRADICTIONS: <ids>
AAS_PLUS_STATE: <state>
PMO_STATE: <state>
BOSS_GATE_STATE: <state>
DISPATCHER_MODEL: Claude Sonnet 5
DISPATCHER_EFFORT: MEDIUM
WORKER_MODEL: <model>
WORKER_EFFORT: <effort>
AUTO_CONTINUE: true
AUTO_RESUME: true
NO_IDLE: true
BOSS_CONTACT: FINAL_GATE_ONLY

DISPATCHER INSTRUCTION:
Read only this control packet and the minimum state needed to route the work. Do not perform the worker's deep research. Route or prepare the correct launcher, record the dispatch state, then stop.

WORKER INSTRUCTION:
Read the full Prompt, AUTO_RESUME_STATE and CHECKPOINT_REGISTER from GitHub. Consume material delta only. Execute to the current terminal state, commit/push evidence, update checkpoint/resume state, then stop without idle waiting.
