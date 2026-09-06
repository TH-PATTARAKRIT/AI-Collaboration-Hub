# P09_DIMENSION_AND_ALLOCATION_BOUNDARY_REGISTER

**Prompt:** `SMEPLUS-26-09-06-P09-P2A-DOMAIN-PURE-BOUNDED-CLOSURE-002` · **Phase S** · **AI EOS NOT ACTIVE**
**Layer:** 1 — clean-room. **Answers `CQ-P09-03` and `CQ-P09-06`.**

---

## 1. THE FIVE DIMENSION ROLES, SEPARATED

The prompt requires identity, classification, allocation, attribution and reporting to be distinguished. In the reference pattern **all five are carried by one object**, which is why they are so easily confused.

| Role | The question it answers | Carrier | P09-owned? |
|---|---|---|---|
| **identity** | *which accountable thing is this?* | **NO CARRIER** — there is no cost object; identity is inferred from whichever field a producer populated | **P09 must author it** |
| **classification** | *what kind of thing is it?* | none — ten de facto cost-object kinds share one record type with no discriminator | **P09 must author it** |
| **allocation** | *what share of this amount belongs here?* | a schemaless percentage payload, no foreign key, no integral sum | **P09-owned rule** |
| **attribution** | *which dimension value ends up carrying the amount?* | the management record | **P09-owned effect** |
| **reporting** | *how is it aggregated and presented?* | read-time aggregation over the management records | **P09-owned, with one contested crossing** |

**DA-01 — Four of the five roles are load-bearing and only two have a carrier.** Identity and classification are absent, which is the same finding as the missing cost object, restated in the prompt's own vocabulary.

---

## 2. THE AXIS IS SCHEMA, NOT DATA — RESTATED AT THE P09 BOUNDARY

Held from prior rounds; **not re-researched**, and unchanged.

| Property | Consequence for P09 ownership |
|---|---|
| creating an axis performs data-definition work on a shared table | the axis is **a property of the database**, not of a tenant — so P09 cannot own it at TENANT scope as its semantics require |
| deleting an axis drops the column and its history | management history is destructible by an ordinary administrative act |
| re-parenting rewrites prior values by direct statement | prior-period comparisons are not stable |
| one axis is privileged by a database-global parameter | a PLATFORM artefact carries a TENANT decision — a scope violation by construction |

**DA-02 — P09 cannot own its own primary structure in the reference pattern.** The dimension type is the one object P09 most clearly should own, and it is the one object that is physically global and unscoped.

---

## 3. WHICH ALLOCATION SEMANTICS ARE GENUINELY P09-OWNED

This is the prompt's sharpest question, and the answer separates P09 from its neighbours cleanly.

| Semantic | Owner | Reasoning |
|---|---|---|
| **the allocation instruction** — *this cost centre takes 60 %* | **P09** | it is a management policy, carrying no financial effect |
| **the assignment rule** that pre-fills it from master data | **P09** | same |
| **the obligation rule** — whether an axis must be filled | **P09** | a management control |
| **the arithmetic** — management amount = negated row balance × share | **P09** | it defines what a management record means |
| **which rows a producer chooses to allocate** | `EXTERNAL DOMAIN BOUNDARY` | the producing domain decides; P09 only observes the consequence |
| **whether a producing event writes one allocation onto both legs of a balanced pair** | `EXTERNAL DOMAIN BOUNDARY` | this is the zeroing mechanism, and its cause is **not P09's** |
| **the conversion of an allocation into postings** | `EXTERNAL DOMAIN BOUNDARY` — and P09 recommends against it existing | it produces financial truth under a management rule |

**DA-03 — The zeroing result is a P09 *consequence* of an adjacent-domain *cause*.** P09 owns the arithmetic that makes annihilation inevitable once both legs are allocated. It does not own the decision to allocate both legs. **Stating it any other way would be domain contamination in the direction of claiming too much**, which is the less obvious of the two failure modes.

---

## 4. THE ALLOCATION'S FOUR INTEGRITY GAPS

| Gap | Behaviour | Class |
|---|---|---|
| **no referential integrity** | the payload has no foreign key; dangling references are a normal state | `FACT VERIFIED — P09` |
| **no completeness** | shares need not total 100 % unless a mandatory axis and an opted-in caller coincide; no storage-level constraint | `FACT VERIFIED — P09` |
| **no residual** | where shares never reach 100 %, the remainder has **no management representation at all** — it is an absence, not a figure | `FACT VERIFIED — P09` |
| **no immutability** | the allocation is absent from every lock-date list, every integrity-hash list and the tracked-field set | `FACT VERIFIED — P09` |

**DA-04 — The unallocated remainder is the most dangerous of the four**, because the other three are visible as defects and this one is invisible as a number. Cost that no one claimed simply does not appear.

---

## 5. CANDIDATE REQUIREMENTS (meaning only, not design)

| # | Requirement |
|---|---|
| **DA-R1** | a cost object shall exist as a first-class identity with a declared type, scope and closing state |
| **DA-R2** | an axis shall be tenant-scoped **data**, versioned and retirable, never physical schema, and no axis shall be privileged |
| **DA-R3** | an allocation shall carry referential integrity and shall be complete, or shall carry a **named, visible residual** |
| **DA-R4** | an allocation on a closed period shall be immutable; correction shall be a dated reallocation event referencing what it corrects |
| **DA-R5** | management aggregation shall occur within one declared scope; any widening shall be explicit, authorised and marked |

**None is authorised here.** All are candidate meanings for Boss decision.

---

## 6. DISPOSITIONS

| ID | Disposition |
|---|---|
| `DA-01` … `DA-04` | `FACT VERIFIED — CLOSED FOR CURRENT P09 EVIDENCE` |
| `DA-R1` … `DA-R5` | `BOSS DECISION REQUIRED — DECISION PACKAGE READY` |
| producer-side allocation decisions | `EXTERNAL DOMAIN BOUNDARY — CANDIDATE HANDOFF RECORDED` |
