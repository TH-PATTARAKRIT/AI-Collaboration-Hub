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

  const masterContinue = deriveIdempotency({
    ...sample,
    event_id: "EVT-EXAMPLE-MASTER-CONTINUE-0001",
    event_type: "MASTER_AUTO_CONTINUE",
    producer_role: "MASTER",
    consumer_role: "A1",
    parent_event_id: "EVT-EXAMPLE-A3-MASTER-0001",
    critical_crq_count: 0,
    high_crq_count: 0,
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
