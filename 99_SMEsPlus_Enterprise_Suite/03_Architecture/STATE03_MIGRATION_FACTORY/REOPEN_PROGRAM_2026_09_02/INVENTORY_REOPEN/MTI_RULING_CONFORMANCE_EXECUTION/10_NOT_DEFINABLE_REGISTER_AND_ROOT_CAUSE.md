# [SMEPLUS-26-09-05-INV-MTI-CONTROLLED-REMEDIATION-001]
# 10 — `NOT DEFINABLE` Register And Root Cause

Control Level: `/L9999.9999`
Topology Scope: `SHARED SaaS POOL`
Status: `7 REQUIREMENTS NOT DEFINABLE — 4 ROOT CAUSES — 0 RESOLVED BY THIS SESSION — 3 OF 4 ROOT CAUSES ARE BOSS DECISIONS`

---

## 1. What `NOT DEFINABLE` Means, Precisely

**`NOT DEFINABLE` is not `HARD`, not `DEFERRED`, and not `FAILED`.**

It means: **the proposition itself cannot be stated**, because the capability the proposition would quantify over is unspecified. A requirement that says *"the mapping asserts correspondence without merging identity"* is not a requirement at all if no object called a mapping exists — there is nothing for the words to be about.

The distinction matters for the work order. A `DEFINABLE` requirement waits on an **implementation**. A `NOT DEFINABLE` requirement waits on a **specification or a ruling**, and no amount of implementation effort moves it.

**Seven requirements are `NOT DEFINABLE`. None was resolved by this session, and three of the four root causes are Boss decisions rather than analyses.**

---

## 2. Root Cause 1 — The Privileged-Path Enumeration Does Not Exist

| Field | Content |
|---|---|
| **Blocks** | `RC-P-08` — *"no process merges, links or correlates products by attribute similarity… the path set is enumerated and the enumeration is certified complete"* |
| **What is missing** | The complete set of privileged, system, background, administrative and migration code paths, certified complete |
| **Evidence** | `L9-01` records an audit of privileged bypass paths that was **started and never finished**. `MTI-18` states the target property and is **unverifiable until the path set is enumerated**. `05` §9 of the invariant set lists this among its five explicit non-claims |
| **Why it makes the proposition unstatable** | `RC-P-08`'s acceptance criterion is a **universal** — *no* path does the prohibited thing. A universal over an unenumerated domain is not a testable proposition; it can only ever be tested as a series of existential checks over paths someone happened to think of |
| **What would resolve it** | **Lane R2** — commission the privileged-bypass path audit. **Needs no Boss ruling, needs no COGS evidence, needs no Thai input.** Recorded as available now in every package in this chain, and unstarted in every one |
| **Owner** | Inventory + SaaS Foundation |
| **Class of the negative claim** | The claim *"the enumeration does not exist"* is class **`A` within the four evidence packages**, in which five separate files record it as incomplete. Class **`B`** for the wider programme |
| **Also blocks** | `L9-01`'s completeness claim · `MTP-03`'s scoring · the `EP-W` coverage assertion · `N-07` at `09` · **the credibility of `MTI-17`, the invariant the whole set rests on** |
| **Moved by this session** | **No.** Nothing in a re-specification pass enumerates a code path |

---

## 3. Root Cause 2 — The Controlled Mapping / Provenance Layer Is Unspecified

| Field | Content |
|---|---|
| **Blocks** | `RC-P-20` — a group-level view exists only through an explicit authorized mapping. `RC-P-21` — a mapping asserts correspondence and never merges identity |
| **What is missing** | The object itself. `RC-F-03`: no published design in R4, the review, the invariant set or the consolidation specifies it |
| **Evidence** | `MTI-D-01` rule 5 requires *"an explicit controlled mapping layer"*; rule 8 requires *"an explicit authorized mapping"*. The nearest published construct was `XCR-03`, **which the same ruling eliminates**, and which served the **opposite** purpose: `XCR-03` let a company-scoped record *reference* a shared definition; a mapping layer asserts a *correspondence* between records that remain separate |
| **Why it makes the propositions unstatable** | Both propositions quantify over *"a mapping"*. Ten required **properties** are enumerated at the consolidation's `06` §5.3, and **properties are not an object** — they constrain something that must first exist |
| **The gating that must not be inverted** | **`MTI-D-04` must be ruled first.** `RC-F-04`: properties `M-04`, `M-08` and `M-09` are the properties of `XCR-02`, whose *existence* is `MTI-D-04`'s subject. Specifying the mechanism before the authorization would design the door before Boss decides whether there is one. **Lane R3 is `NOT AVAILABLE` for this reason and not for a resourcing reason** |
| **What would resolve it** | `MTI-D-04` ruled — **including a ruling of "no such grant exists"**, which would settle it — then `RC-D-04` on ownership and commissioning, then the specification |
| **Owner** | **Boss**, then Inventory |
| **Moved by this session** | **No — and `CF-I-06` must not be mistaken for movement.** `CF-I-06` states the **prohibition** that holds in the object's absence, and `CF-P-10` makes that prohibition testable. **Neither states anything about the object.** Theme 6 gains one definable requirement about the absence; it gains nothing about the mapping |
| **What gets worse while it stands** | Under Option B a Thai SME group maintains **several** catalogues instead of one, so the group-view need is **larger**. `MTA-09` records that an unmet group-view need is met by **export**, which the same register names the worst available outcome |

---

## 4. Root Cause 3 — Private Company Escalation Criteria Do Not Exist

| Field | Content |
|---|---|
| **Blocks** | `RC-P-45` classification · `RC-P-46` control-rule delta · `RC-P-48` transition semantics · the **positive half** of `RC-P-47` |
| **What is missing** | The objective published test that moves a requirement from pool to Private Company; the Gate record's required content; the control-rule delta; the proof delta; the transition semantics; and the disposition of pool prohibitions **4** and **5** |
| **Evidence** | `MTI-D-03` §4 establishes that the option exists, may be opened when required, must pass controlled governance, is not a bypass, and requires an explicit Gate record, evidence and a Boss ruling. **It establishes nothing about when it applies, who decides, on what evidence, what the governance is, which control rules change, or whether an existing tenant may migrate into it.** `05` §3.1 of the consolidation sets the two columns side by side |
| **Why it makes the propositions unstatable** | `RC-P-45` requires a test that *"returns exactly one answer per requirement, with no residue"*. `05` §4 of the consolidation applies the available material to seven live requirement classes and gets an answer for **three**. A classification that fails on **4 of 7** is not a test |
| **The `HOLD` this creates is general, not exceptional** | AAS+ advice `29` §7 makes unclassifiability a `HOLD` condition. With no criteria published, **the classification cannot currently be performed for any requirement**, so the `HOLD` is live and general |
| **The specific unanswered half** | Advice `29` §6 gives a directional test covering pool prohibitions **1, 2, 3 and 6** — source, schema, posting and isolation divergence. **It is silent on prohibitions 4 and 5** — authorization-engine divergence and immutable-event-logic divergence. Whether those are Private-Company-eligible or prohibited outright everywhere is `RC-D-03`, **and this session takes no position on it** |
| **What would resolve it** | **`RC-D-03` ruled.** One Boss ruling, then the six specifications enumerated at the consolidation's `05` §5 |
| **Owner** | **Boss**, then Inventory + AAS+ |
| **Moved by this session** | **No — and `CF-I-08` must not be mistaken for movement.** `CF-I-08` requires every artifact to state the topology it was established in. That is a **labelling control**. It prevents a pool-established result being cited as evidence about a Private Company; it supplies no Private Company content and **reduces `RC-F-07` by nothing** |
| **Additional dependency on `RC-P-48`** | Even with criteria, the transition question sits on `MTI-06` — the context spine is immutable by design — and on `GAP-FS-08`, which does not exist. **Both paths out are blocked, and this is the one root cause with a second, independent blocker underneath it** |

---

## 5. Root Cause 4 — Two Structural Gaps Found By This Session

These are `NOT DEFINABLE` **precursors** rather than `NOT DEFINABLE` requirements: they do not block a requirement from being stated, they block one from being **satisfiable**. They are registered here because a reader working the `NOT DEFINABLE` list needs to know why two `DEFINABLE` requirements will nonetheless not be satisfiable.

### 5.1 `CF-F-05` — authorization has no conformance control

| Field | Content |
|---|---|
| **Affects** | `CF-P-06` (`DEFINABLE`, unsatisfiable — the control does not exist) · `CF-P-07` · `RC-P-32`, whose attestation half now references `HF-CTX-11` |
| **Search boundary** | **`B-02`** at `01` §8 — the 50 rows `MTI-01` .. `MTI-50` at `dcb9227`, read in full, layer column plus full invariant text plus every row mentioning authority, permission, role or grant |
| **Result** | **Eight invariants carry the `CONTROL` layer. Seven assert a property of `CTX`; the eighth asserts retention.** `MTI-30` is the only one that touches authority, and it asserts a runtime precondition on one path — a lapsed grant blocks one deferred run — not a continuously asserted conformance property |
| **Class** | **`A` within `B-02`. `B` for the wider system.** `NO EVIDENCE FOUND` is not `DOES NOT EXIST` |
| **Consequence** | The context half of element 10 has a value, an attestation and a control behind it. **The authority half has a value and nothing else** — which is carriage, not guarantee, and is the exact defect element 10's whole treatment exists to remove |
| **Remedy specified** | `CF-I-03` and `HF-CTX-11`. **Specified, not built.** `HF-CTX-11` presently references a control that does not exist, and that is stated wherever it appears rather than smoothed over |
| **Escalated** | `L13-CF-01` |

### 5.2 `CF-F-04` — the operation-type axis has no platform-owned class

| Field | Content |
|---|---|
| **Affects** | `RC-P-16` — pushed from one condition to **two**, a regression · `RC-P-14`'s test-set derivation · `CF-P-03` (`DEFINABLE — CONDITIONAL`) · every platform-level control over an operation type |
| **The composition** | `MTI-D-02` makes operation type an authorization axis over an enumeration that is *"including, but not limited to"* eight examples. `MTI-D-03` makes Operation Type tenant-configurable. **Nothing maps a tenant-configured type to a platform-owned classification** |
| **Consequence** | A platform-level control — *"Scrap requires a second approver"* — cannot be expressed, because `Scrap` is a tenant's label and the platform has no stable term to bind to. `L7-09` segregation of duties becomes **expressible per tenant and unstatable per platform** |
| **Remedy specified** | `CF-I-05`, on the pattern `MTI-33` already sets for reason classification. **The class enumeration's closure is `CF-D-02`, a Boss decision, stated and never chosen** |
| **Escalated** | `L13-CF-02` |

---

## 6. The Seven `NOT DEFINABLE` Requirements

| ID | Requirement | Root cause | Owner | What resolves it | Resolvable by analysis? |
|---|---|---|---|---|:---:|
| `RC-P-08` | No process merges or correlates products by attribute similarity | **1** — path enumeration | Inventory + SaaS Foundation | Lane R2 audit | **Yes — commission it** |
| `RC-P-20` | A group-level view exists only through an authorized mapping | **2** — mapping layer | Boss, then Inventory | `MTI-D-04` ruled, then Lane R3 | **No — a ruling first** |
| `RC-P-21` | A mapping asserts correspondence and never merges identity | **2** | Boss, then Inventory | as `RC-P-20` | **No** |
| `RC-P-45` | Every requirement is classifiable pool-safe or Private-Company-required | **3** — escalation criteria | **Boss** | `RC-D-03` ruled | **No** |
| `RC-P-46` | A Private Company preserves or names every changed control rule | **3** | **Boss**, then Inventory + AAS+ | `RC-D-03`, then the delta | **No** |
| `RC-P-47` positive half | Separation occurs through a Gate record with defined content | **3** | PMO + Boss | Gate record content specified | **No** |
| `RC-P-48` | Movement between pool and Private Company preserves immutable history | **3**, plus `MTI-06` and `GAP-FS-08` | Inventory + Boss | `RC-D-03`, **and** `GAP-FS-08` | **No — two blockers** |

**One of seven is resolvable by commissioning work that needs no decision. Six wait on a Boss ruling, and three of those wait on the same one.**

---

## 7. What Would Change The Count

| Action | Requirements resolved | Lane | Needs a ruling? |
|---|---:|---|---|
| Commission the privileged-bypass path audit | **1** — `RC-P-08` | R2 / A | **No** |
| Rule `MTI-D-04`, then commission the mapping layer | **2** — `RC-P-20`, `RC-P-21` | R4 then R3 / D then A | **Yes** — and *"no such grant exists"* is a perfectly good ruling |
| Rule `RC-D-03` | **3 and a half** — `RC-P-45`, `-46`, `-48`, and the positive half of `-47` | R4 / D | **Yes** |
| Rule `CF-D-02` | **0 `NOT DEFINABLE` resolved**, but `RC-P-16` returns to one condition and `CF-P-03` becomes `DEFINABLE` | R4 / D | **Yes** |
| Build the authorization conformance control | **0 `NOT DEFINABLE` resolved**, but `CF-P-06` and `CF-P-07` become satisfiable and `HF-CTX-11` stops referencing nothing | implementation | No — but `RC-V-01` and `AAS-V-02` both stand in front of it |

**Three rulings and one audit would move all seven.** None of the four is an investigation into an unknown; three are decisions and one is a bounded enumeration that has been recommended in four consecutive packages and started once.

---

## 8. What This Register Does Not Do

| Not done | Why |
|---|---|
| It does not resolve any `NOT DEFINABLE` requirement | Three of four root causes are Boss decisions, and the fourth is a commissioned audit |
| It does not specify the mapping layer, the escalation criteria, or the Gate record content | Each would pre-empt a Boss decision |
| It does not rule `MTI-D-04`, `RC-D-03`, `RC-D-04` or `CF-D-02` | Options at `11` §3, **never chosen** |
| It does not treat `CF-I-06` or `CF-I-08` as reducing root causes 2 or 3 | One is a prohibition in an object's absence; the other is a labelling control. **Both are stated as such wherever they appear** |
| It does not classify the severity of `C-02` | A Boss ruling. Declined by R4, the review, the invariant set, the consolidation, and this session |

---

`No Evidence = No Progress.`
`Never Skip Gate.`
`Boss = Sole Final Approver.`
