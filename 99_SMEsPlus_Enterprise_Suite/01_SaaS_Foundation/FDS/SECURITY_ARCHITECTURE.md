# SECURITY_ARCHITECTURE.md

# SMEsPlus Enterprise Suite - Security Architecture

**Version:** 1.0.0
**Status:** Architecture Gate (Draft → Pending Review)
**Authority:** ADR-0001, ADR-0013

---

# SECTION 1: PURPOSE

Defines security architecture covering:
- Authentication (OAuth 2.0, JWT, MFA)
- Authorization (RBAC, ABAC, RLS)
- Encryption (AES-256, TLS 1.3)
- Threat modeling
- Compliance (PDPA, Thai Revenue Code)
- Incident response
- Security testing

---

# SECTION 2: SECURITY PRINCIPLES

Core principles:
- Defense in Depth
- Least Privilege
- Security by Design
- Zero Trust
- Separation of Concerns
- Compliance First

---

# SECTION 3: AUTHENTICATION ARCHITECTURE

Methods: OAuth 2.0, JWT (RS256), Passwords (Bcrypt)
MFA: TOTP support (mandatory for admin/finance)
Token: 15-min access, 30-day refresh

---

# SECTION 4: AUTHORIZATION ARCHITECTURE

Models: RBAC, ABAC, RLS
Database: PostgreSQL RLS policies enforce tenant isolation
Levels: User → Roles → Permissions → Resources

---

# SECTION 5: ENCRYPTION STANDARDS

At Rest: AES-256-CBC via pgcrypto
In Transit: TLS 1.3 (minimum)
Keys: Stored in vault (HashiCorp, AWS Secrets Manager)
Sensitive: Tax ID, bank accounts, employee IDs

---

# SECTION 6-14: DETAILED SECTIONS

API Gateway security, secret management, audit logging, threat modeling, compliance requirements, vulnerability management, incident response, Thai market considerations, security testing.

---

**END OF SECURITY_ARCHITECTURE.md**