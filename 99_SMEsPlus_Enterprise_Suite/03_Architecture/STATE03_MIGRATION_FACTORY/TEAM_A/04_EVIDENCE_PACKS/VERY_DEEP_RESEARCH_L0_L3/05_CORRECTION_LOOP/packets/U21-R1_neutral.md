# Correction packet U21-R1 — NEUTRAL KNOWLEDGE

> DEEPSEEK-REPORTED / PENDING CLAUDE VERIFICATION. Neutral layer: no vendor structure. Supersedes the neutral statements named in the restricted packet header.

- **WHAT:** How a certificate's private key is loaded by the outgoing-HTTPS adapter. [N-U21R1-001]
- **BUSINESS RULE:** The adapter always loads the stored key material without a password. When the key record was stored without a password the stored material is unencrypted and loads correctly. [N-U21R1-001] [N-U21R1-002]
- **RISK:** When a key record carries a password the stored key material is encrypted; the adapter's password-free load would fail. Whether this scenario occurs in practice depends on whether keys with passwords are used with certificate-based TLS. [N-U21R1-002]
- **UNKNOWN:** The runtime behaviour (error, silent fallback or bypass) when an encrypted key is used through the adapter requires execution to confirm.
