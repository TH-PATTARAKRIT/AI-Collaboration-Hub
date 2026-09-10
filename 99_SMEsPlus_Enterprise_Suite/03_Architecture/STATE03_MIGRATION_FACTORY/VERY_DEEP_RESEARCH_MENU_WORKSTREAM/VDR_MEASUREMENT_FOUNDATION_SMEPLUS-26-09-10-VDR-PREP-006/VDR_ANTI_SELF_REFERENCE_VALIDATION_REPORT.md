# VDR_ANTI_SELF_REFERENCE_VALIDATION_REPORT.md
# The test built to detect self-reference is itself self-referential — **FAILED**

Session `[SMEPLUS-26-09-10-VDR-PREP-006]` · Layer: **LAYER 1 — CLEAN-ROOM.** Checkpoint 08.

> ### VERDICT: **THE ANTI-SELF-REFERENCE TEST FAILS ITS OWN STANDARD.**
> An earlier edition of this document reported *"7 of 7 PASS"* and called the property *"structural, not
> promised."* **That was wrong, and it was wrong in exactly the way the round was convened to prevent.**

---

## 1. What the test did

Each instrument declares the fields it reads. The harness asserts those inputs are disjoint from
`WRITTEN_FIELDS` — the set of fields any instrument writes — and reports the result.

```
WRITTEN_FIELDS = set()              <- the instrument module, a literal
overlap = inputs & WRITTEN_FIELDS   <- the harness, an empty intersection
```

**`WRITTEN_FIELDS` is a literal. It is not computed from anything.** The intersection is empty by
construction, so the assertion **can never fail**, whatever the instruments do.

## 2. The demonstration — run, not argued

An independent validator installed a deliberately mutating instrument that **rewrites the very field
`INS-02` grades**, then re-ran the test. Reproduced here:

```
anti-self-reference verdict with a KNOWN mutating instrument installed: ALL PASS
before mutator: INS-02 -> ABSENT
after  mutator: INS-02 -> OBSERVED     <- the grade was changed by an instrument writing its input
```

**The test reported ALL PASS while an instrument was demonstrably grading a value it had just written.**

## 3. The scope error underneath it

The contract was written as *"no **instrument** writes a field another instrument reads."* The exposure
is *"no field an instrument reads was written by **the measurement process**."*

Under the correct scope, **six of seven instruments violate it:**

| Instrument | Reads | Written by |
|-----------|-------|-----------|
| INS-01 | `source_pointer` | the union script |
| INS-02 | `observed_on` | the union script |
| INS-03 | both | the union script |
| INS-04 | `kind`, `module` | the union script |
| INS-05, INS-07 | `identity` | the union script |

**All seven of those columns are produced by the same run that grades them.** `WRITTEN_FIELDS` declares
`NONE`.

## 4. The consequence, measured

**`INS-03` reproduces a column the measurement process already wrote, on 24,553 of 24,553 rows — 100.00%
identity.** It is not an independent classification of the population; it re-derives `discovery` from
the same two inputs the union script used to write it. An error in `INS-01` propagates into `INS-03`,
and the two then **agree** — manufacturing corroboration.

**`INS-04` returns one value on 24,553 of 24,553 rows. `INS-06` returns one value on 24,553 of 24,553
rows.** The fields they read are not columns of the population at all. Neither can fire on the artefact
it is published beside.

## 5. §13's four questions, answered honestly

| Question | Earlier answer | **Correct answer** |
|----------|---------------|--------------------|
| Can an instrument pass by writing the field it later grades? | NO | **NOT EXCLUDED.** The test that claimed to exclude it cannot fail |
| Can an instrument classify on a value it generated itself? | NO | **NOT EXCLUDED**, and `INS-07`'s verdict string embeds a measurement-process identifier — a direct counter-example |
| Can a result change because the instrument changed its own denominator? | NO | **still NO** — no instrument sees the population. This one survives |
| Can an excluded item disappear without a traceable reason? | NO | **still NO** — the exclusion instrument returns a verdict, never a drop. This one survives |

**Two of four hold. Two do not, and the two that do not are the two the test was built for.**

## 6. What did survive, verified independently

- **No instrument mutates the item it is given.** A static scan for stores and mutating calls on any parameter, plus a dynamic deep-copy-and-diff of all seven on a fully populated item: **zero mutation sites.** The mechanical form of the claim holds.
- **The instruments were not edited to make fixtures pass.** All three preserved fixture runs were reproduced **byte-identically** with the unmodified instruments, corroborated by file timestamps.

**So the code is honest. The test that certified it was not a test.**

## 7. What a real anti-self-reference test requires

1. **`WRITTEN_FIELDS` derived, never declared** — computed by static analysis of every instrument and of every script in the measurement pipeline.
2. **Scoped to the pipeline, not to the instrument** — the question is which fields the *run* produced.
3. **A negative control**: a deliberately self-referential instrument that the test must **reject**. A test with no case it fails is not a test — which is the rule this programme wrote two rounds ago and did not apply to its own instrument.

**None of the three was present. All three are the first work of the next round.**
