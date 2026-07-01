# iTEST02 Masking Rules

| Data Type | Rule |
|---|---|
| Email | Replace with deterministic synthetic email |
| Phone | Replace with synthetic number |
| Name | Replace with synthetic name or role label |
| Bank account | Redact except last four only if approved |
| Token/key | Remove entirely |
| Password/hash | Remove entirely |
| Address | Generalize to province/country level |
| Salary/payroll | Replace with band or remove |
| Attachment | Exclude unless explicitly approved |
| Vector content | Treat as derived sensitive content and restrict |
