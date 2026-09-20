#!/usr/bin/env node

import { mkdtemp, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { dirname, resolve } from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";

const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const validatorPath = resolve(scriptDirectory, "validate-event.mjs");
const samplePath = resolve(scriptDirectory, "../events/examples/a1-handoff-ready.json");

function run(path, shouldPass, label, extraArguments = []) {
  const result = spawnSync(process.execPath, [validatorPath, ...extraArguments, path], { encoding: "utf8" });
  const passed = result.status === 0;
  if (passed !== shouldPass) {
    process.stderr.write(result.stdout);
    process.stderr.write(result.stderr);
    throw new Error(`${label}: expected ${shouldPass ? "PASS" : "REJECT"}`);
  }
  console.log(`TEST ${shouldPass ? "PASS" : "REJECT"}: ${label}`);
}

function deriveIdempotency(event) {
  event.idempotency_key = `${event.batch_id}:${event.event_type}:${event.output_manifest_sha256}:${event.attempt}`;
  return event;
}

const temporaryDirectory = await mkdtemp(resolve(tmpdir(), "room-a-validator-"));
try {
  const sample = JSON.parse(await readFile(samplePath, "utf8"));
  run(samplePath, true, "synthetic A1 handoff");
  run(samplePath, true, "approved-root containment", ["--root", resolve(scriptDirectory, "../events")]);
  run(samplePath, false, "out-of-root path", ["--root", temporaryDirectory]);

  const cases = [
    ["module-count-mismatch", { ...sample, module_count: 2 }, false],
    ["forbidden-extra-field", { ...sample, source_code: "x" }, false],
    ["missing-required-crq-count", (() => {
      const value = { ...sample };
      delete value.high_crq_count;
      return value;
    })(), false],
    ["arbitrary-idempotency-text", { ...sample, idempotency_key: `${sample.batch_id}:model.method(field):1` }, false]
  ];

  const a2Question = deriveIdempotency({
    ...sample,
    event_id: "EVT-EXAMPLE-A2-CRQ-0001",
    event_type: "A2_CRQ_OPENED",
    producer_role: "A2",
    consumer_role: "A1",
    parent_event_id: sample.event_id,
    state: "ACTION_REQUIRED",
    crq_ids: ["CRQ-EXAMPLE-HIGH-001"],
    crq_disposition: "OPEN"
  });
  cases.push(["a2-question-to-a1", a2Question, true]);
  const questionMissingIds = { ...a2Question };
  delete questionMissingIds.crq_ids;
  cases.push(["a2-question-missing-crq-ids", questionMissingIds, false]);

  const a1Response = deriveIdempotency({
    ...a2Question,
    event_id: "EVT-EXAMPLE-A1-RESPONSE-0001",
    event_type: "A1_CRQ_RESPONSE_READY",
    producer_role: "A1",
    consumer_role: "A2",
    parent_event_id: a2Question.event_id,
    state: "ANSWER_READY",
    crq_disposition: "ANSWERED_RESTRICTED"
  });
  cases.push(["a1-response-to-a2", a1Response, true]);
  cases.push(["a1-cannot-self-verify", { ...a1Response, crq_disposition: "VERIFIED" }, false]);

  const a2ReviewReady = deriveIdempotency({
    ...sample,
    event_id: "EVT-EXAMPLE-A2-A3-0001",
    event_type: "A2_REVIEW_READY",
    producer_role: "A2",
    consumer_role: "A3",
    parent_event_id: a1Response.event_id,
    state: "READY",
    critical_crq_count: 0,
    high_crq_count: 0,
    open_crq_ids: [],
    blocking_dependencies: []
  });
  cases.push(["a2-review-ready-after-verification", a2ReviewReady, true]);
  cases.push(["a2-review-blocked-by-high-crq", { ...a2ReviewReady, high_crq_count: 1 }, false]);
  cases.push([
    "crq-fields-not-allowed-on-standard-handoff",
    { ...sample, crq_ids: ["CRQ-EXAMPLE-HIGH-001"], crq_disposition: "OPEN" },
    false
  ]);

  const mixedDisposition = deriveIdempotency({
    ...sample,
    event_id: "EVT-EXAMPLE-A2-MIXED-0001",
    event_type: "A2_MIXED_DISPOSITION_READY",
    producer_role: "A2",
    consumer_role: "MASTER",
    parent_event_id: sample.event_id,
    state: "ACTION_REQUIRED",
    cfc_revisions: [
      "CAP-FDN-IDENTITY-COMPANY:r1",
      "CAP-FDN-CONTROL:r1",
      "CAP-FDN-UNIT:r1"
    ],
    capsule_routes: [
      {
        cfc_id: "CAP-FDN-IDENTITY-COMPANY",
        revision: "r1",
        disposition: "CONDITIONAL_PASS_RECOMMENDATION",
        next_role: "A3"
      },
      {
        cfc_id: "CAP-FDN-CONTROL",
        revision: "r1",
        disposition: "CONDITIONAL_PASS_RECOMMENDATION",
        next_role: "A3"
      },
      {
        cfc_id: "CAP-FDN-UNIT",
        revision: "r1",
        disposition: "REJECT_RETURN",
        next_role: "A1"
      }
    ]
  });
  cases.push(["a2-mixed-capsule-disposition", mixedDisposition, true]);
  cases.push([
    "mixed-disposition-without-return-route",
    {
      ...mixedDisposition,
      cfc_revisions: mixedDisposition.cfc_revisions.slice(0, 2),
      capsule_routes: mixedDisposition.capsule_routes.slice(0, 2)
    },
    false
  ]);

  const masterRouteA3 = deriveIdempotency({
    ...mixedDisposition,
    event_id: "EVT-EXAMPLE-MASTER-ROUTE-A3-0001",
    event_type: "MASTER_ROUTE_A3",
    producer_role: "MASTER",
    consumer_role: "A3",
    parent_event_id: mixedDisposition.event_id,
    state: "READY",
    critical_crq_count: 0,
    high_crq_count: 0,
    open_crq_ids: [],
    blocking_dependencies: [],
    cfc_revisions: mixedDisposition.cfc_revisions.slice(0, 2),
    capsule_routes: mixedDisposition.capsule_routes.slice(0, 2)
  });
  cases.push(["master-routes-accepted-subset-to-a3", masterRouteA3, true]);
  cases.push([
    "master-route-a3-blocked-by-high-crq",
    { ...masterRouteA3, high_crq_count: 1, open_crq_ids: ["CRQ-EXAMPLE-HIGH-001"] },
    false
  ]);
  cases.push([
    "master-route-a3-blocked-by-dependency",
    { ...masterRouteA3, blocking_dependencies: ["DEP-EXAMPLE-001"] },
    false
  ]);

  const masterReturnA1 = deriveIdempotency({
    ...mixedDisposition,
    event_id: "EVT-EXAMPLE-MASTER-RETURN-A1-0001",
    event_type: "MASTER_RETURN_A1",
    producer_role: "MASTER",
    consumer_role: "A1",
    parent_event_id: mixedDisposition.event_id,
    state: "READY",
    cfc_revisions: [mixedDisposition.cfc_revisions[2]],
    capsule_routes: [mixedDisposition.capsule_routes[2]]
  });
  cases.push(["master-returns-rejected-subset-to-a1", masterReturnA1, true]);
  cases.push([
    "master-route-a3-cannot-carry-reject",
    {
      ...masterRouteA3,
      cfc_revisions: [mixedDisposition.cfc_revisions[2]],
      capsule_routes: [mixedDisposition.capsule_routes[2]]
    },
    false
  ]);

  const masterContinue = deriveIdempotency({
    ...sample,
    event_id: "EVT-EXAMPLE-MASTER-CONTINUE-0001",
    event_type: "MASTER_AUTO_CONTINUE",
    producer_role: "MASTER",
    consumer_role: "A1",
    parent_event_id: "EVT-EXAMPLE-A3-MASTER-0001",
    critical_crq_count: 0,
    high_crq_count: 0,
    open_crq_ids: [],
    blocking_dependencies: [],
    source_batch_id: sample.batch_id,
    target_batch_id: "EXAMPLE-G01-002"
  });
  cases.push(["master-auto-continue-clean", masterContinue, true]);
  cases.push(["master-auto-continue-with-high", { ...masterContinue, high_crq_count: 1 }, false]);
  cases.push(["master-auto-continue-missing-parent", { ...masterContinue, parent_event_id: null }, false]);

  const hold = deriveIdempotency({
    ...sample,
    event_id: "EVT-EXAMPLE-HOLD-0001",
    event_type: "HOLD",
    producer_role: "CONTROLLER",
    consumer_role: "CONTROLLER",
    parent_event_id: "EVT-EXAMPLE-A2-A3-0001",
    state: "HOLD",
    hold_scope: "BATCH_LOCAL",
    hold_reason_code: "MANIFEST-MISMATCH",
    finding_ids: ["FINDING-EXAMPLE-001"]
  });
  cases.push(["hold-with-required-disposition", hold, true]);
  const missingHoldReason = { ...hold };
  delete missingHoldReason.hold_reason_code;
  cases.push(["hold-missing-reason", missingHoldReason, false]);

  for (const [name, value, expected] of cases) {
    const casePath = resolve(temporaryDirectory, `${name}.json`);
    await writeFile(casePath, `${JSON.stringify(value, null, 2)}\n`, "utf8");
    run(casePath, expected, name);
  }
} finally {
  await rm(temporaryDirectory, { recursive: true, force: true });
}
