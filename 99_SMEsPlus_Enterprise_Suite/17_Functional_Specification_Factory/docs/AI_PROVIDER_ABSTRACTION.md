# AI Provider Abstraction

Owner: Enterprise Architect AI
Status: Draft

## Purpose
Keep the FDS Factory pipeline provider-agnostic so no single AI vendor is a single
point of failure or lock-in.

## Adapters
- OpenAI Adapter
- Claude Adapter
- Gemini Adapter
- Local LLM Adapter
- Future Provider Adapter (extension point)

## Rules
- No direct hard dependency on one AI vendor's SDK inside pipeline logic; access
  only through the adapter interface.
- API keys must be supplied via environment variables only — never hard-coded or
  committed to the repository.
- `ENABLE_LIVE_API=false` by default; live calls require explicit opt-in per
  environment.
