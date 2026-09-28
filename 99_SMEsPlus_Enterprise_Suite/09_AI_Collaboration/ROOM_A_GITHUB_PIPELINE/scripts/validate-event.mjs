#!/usr/bin/env node

import { readFile, realpath } from "node:fs/promises";
import { dirname, relative, resolve, sep } from "node:path";
import { fileURLToPath } from "node:url";

const scriptDirectory = dirname(fileURLToPath(import.meta.url));
const pipelineRoot = resolve(scriptDirectory, "..");
const schemaPath = resolve(pipelineRoot, "contracts/batch-event.schema.json");
const transitionsPath = resolve(pipelineRoot, "config/state-transitions.json");
const maximumEventBytes = 64 * 1024;
const maximumModules = 857;

const sha256Pattern = /^[a-f0-9]{64}$/;
const eventIdPattern = /^EVT-[A-Z0-9-]+$/;
const strictIdPattern = /^[A-Z0-9-]+$/;
const opaqueIdPattern = /^[A-Z0-9._-]+$/;
const revisionPattern = /^[A-Za-z0-9._:-]+$/;
const forbiddenKeyPattern = /(source.?code|code.?fragment|path.?line|file.?path|class.?name|method.?name|private.?api|xml.?id|credential|password|secret|customer.?data|database.?data)/i;
const forbiddenContentPatterns = [
  /(?:^|\s)(?:class|def|function)\s+[A-Za-z_$][\w$]*/i,
  /(?:^|\s)(?:SELECT|INSERT|UPDATE|DELETE)\s+(?:FROM|INTO|[A-Za-z_])/i,
  /(?:[A-Za-z0-9_.-]+\/(?:[A-Za-z0-9_.-]+\/)+[A-Za-z0-9_.-]+\.(?:py|js|ts|xml|sql))(?::\d+)?/i,
  /-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----/,
  /(?:api[_-]?key|access[_-]?token|password)\s*[:=]/i
];

function fail(message) {
  throw new Error(message);
}

function requireInteger(value, field, minimum = 0) {
  if (!Number.isInteger(value) || value < minimum) {
    fail(`${field} must be an integer >= ${minimum}`);
  }
}

function requireBoundedString(value, field, pattern, maximumLength = 128) {
  if (typeof value !== "string" || value.length === 0 || value.length > maximumLength || !pattern.test(value)) {
    fail(`${field} is not a valid bounded identifier`);
  }
}

function requireStringArray(value, field, pattern, { minimumItems = 0, maximumItems = maximumModules } = {}) {
  if (!Array.isArray(value) || value.some((item) => typeof item !== "string")) {
    fail(`${field} must be an array of strings`);
  }
  if (value.length < minimumItems || value.length > maximumItems) {
    fail(`${field} length must be ${minimumItems}..${maximumItems}`);
  }
  if (new Set(value).size !== value.length) {
    fail(`${field} must not contain duplicates`);
  }
  if (value.some((item) => item.length > 128 || !pattern.test(item))) {
    fail(`${field} contains an invalid identifier`);
  }
}

function scanForbidden(value, trail = "event") {
  if (Array.isArray(value)) {
    value.forEach((item, index) => scanForbidden(item, `${trail}[${index}]`));
    return;
  }
  if (value && typeof value === "object") {
    for (const [key, child] of Object.entries(value)) {
      if (forbiddenKeyPattern.test(key)) fail(`forbidden field name at ${trail}.${key}`);
      scanForbidden(child, `${trail}.${key}`);
    }
    return;
  }
  if (typeof value === "string" && forbiddenContentPatterns.some((pattern) => pattern.test(value))) {
    fail(`source-specific or secret-like content detected at ${trail}`);
  }
}

function requireCapsuleRoutes(value, event) {
  if (!Array.isArray(value) || value.length === 0) fail("capsule_routes must be a non-empty array");
  const allowedKeys = new Set(["cfc_id", "revision", "disposition", "next_role"]);
  const allowedDispositions = new Set([
    "PASS_RECOMMENDATION",
    "CONDITIONAL_PASS_RECOMMENDATION",
    "REJECT_RETURN"
  ]);
  const routeKeys = new Set();
  for (const route of value) {
    if (!route || Array.isArray(route) || typeof route !== "object") fail("capsule route must be an object");
    if (Object.keys(route).some((key) => !allowedKeys.has(key)) || Object.keys(route).length !== allowedKeys.size) {
      fail("capsule route fields must be exactly cfc_id, revision, disposition and next_role");
    }
    requireBoundedString(route.cfc_id, "capsule_routes.cfc_id", /^CAP-[A-Z0-9-]+$/);
    requireBoundedString(route.revision, "capsule_routes.revision", /^r[1-9][0-9]*$/, 16);
    if (!allowedDispositions.has(route.disposition)) fail("invalid capsule route disposition");
    if (!new Set(["A1", "A3"]).has(route.next_role)) fail("invalid capsule route next_role");
    const routeKey = `${route.cfc_id}:${route.revision}`;
    if (routeKeys.has(routeKey)) fail("capsule_routes must not contain duplicate CFC revisions");
    routeKeys.add(routeKey);
  }
  const cfcRevisionSet = new Set(event.cfc_revisions);
  if (routeKeys.size !== cfcRevisionSet.size || [...routeKeys].some((value) => !cfcRevisionSet.has(value))) {
    fail("capsule_routes must exactly match cfc_revisions");
  }
}

async function parseJson(path) {
  return JSON.parse(await readFile(path, "utf8"));
}

async function enforceContainment(inputPath, rootPath) {
  const [canonicalInput, canonicalRoot] = await Promise.all([realpath(inputPath), realpath(rootPath)]);
  const pathFromRoot = relative(canonicalRoot, canonicalInput);
  if (pathFromRoot === "" || pathFromRoot.startsWith(`..${sep}`) || pathFromRoot === ".." || resolve(canonicalInput) === canonicalRoot) {
    fail("event path must be a JSON file below the approved event root");
  }
  if (!canonicalInput.endsWith(".json")) fail("event path must end in .json");
}

async function main() {
  const argumentsList = process.argv.slice(2);
  let approvedRoot = null;
  if (argumentsList[0] === "--root") {
    approvedRoot = argumentsList[1];
    argumentsList.splice(0, 2);
  }
  const inputPath = argumentsList[0];
  if (!inputPath || argumentsList.length !== 1) {
    fail("usage: validate-event.mjs [--root approved-directory] <event.json>");
  }

  if (approvedRoot) await enforceContainment(inputPath, approvedRoot);

  const [raw, schema, transitionConfig] = await Promise.all([
    readFile(resolve(inputPath), "utf8"),
    parseJson(schemaPath),
    parseJson(transitionsPath)
  ]);
  if (Buffer.byteLength(raw, "utf8") > maximumEventBytes) fail("event exceeds 64 KiB limit");

  const event = JSON.parse(raw);
  if (!event || Array.isArray(event) || typeof event !== "object") fail("event must be a JSON object");

  const allowedKeys = new Set(Object.keys(schema.properties));
  for (const key of Object.keys(event)) {
    if (!allowedKeys.has(key)) fail(`unexpected field: ${key}`);
  }
  for (const key of schema.required) {
    if (!(key in event)) fail(`missing required field: ${key}`);
  }
  const configuredEvents = Object.keys(transitionConfig);
  const schemaEvents = schema.properties.event_type.enum;
  if (configuredEvents.length !== schemaEvents.length || configuredEvents.some((name) => !schemaEvents.includes(name))) {
    fail("contract error: schema event types and transition config differ");
  }

  scanForbidden(event);

  requireBoundedString(event.event_id, "event_id", eventIdPattern);
  requireBoundedString(event.batch_id, "batch_id", strictIdPattern);
  requireBoundedString(event.authority_reference, "authority_reference", opaqueIdPattern);
  requireBoundedString(event.execution_lineage_id, "execution_lineage_id", opaqueIdPattern);
  requireBoundedString(event.handoff_artifact_id, "handoff_artifact_id", opaqueIdPattern);
  requireBoundedString(event.payload_manifest_artifact_id, "payload_manifest_artifact_id", opaqueIdPattern);
  requireInteger(event.attempt, "attempt", 1);

  const transition = transitionConfig[event.event_type];
  if (!transition) fail("unsupported event_type");
  if (
    event.producer_role !== transition.producer ||
    event.consumer_role !== transition.consumer ||
    event.state !== transition.required_state
  ) {
    fail(`invalid transition for ${event.event_type}`);
  }

  for (const field of ["corpus_membership_sha256", "input_manifest_sha256", "output_manifest_sha256", "handoff_sha256"]) {
    if (typeof event[field] !== "string" || !sha256Pattern.test(event[field])) {
      fail(`${field} must be a lowercase SHA-256`);
    }
  }

  requireStringArray(event.module_ids, "module_ids", strictIdPattern, { minimumItems: 1 });
  for (const field of ["module_count", "assigned_module_count", "received_module_count"]) {
    requireInteger(event[field], field, 1);
    if (event[field] !== event.module_ids.length) fail(`${field} does not match module_ids length`);
  }
  requireStringArray(event.cfc_revisions, "cfc_revisions", revisionPattern, { minimumItems: 1 });
  requireStringArray(event.blocking_dependencies, "blocking_dependencies", opaqueIdPattern);
  for (const field of [
    "critical_crq_count",
    "high_crq_count",
    "medium_crq_count",
    "low_crq_count",
    "gap_count",
    "runtime_required_count"
  ]) {
    requireInteger(event[field], field, 0);
  }
  requireStringArray(event.open_crq_ids, "open_crq_ids", /^CRQ-[A-Z0-9._-]+$/);
  const openCrqCount =
    event.critical_crq_count + event.high_crq_count + event.medium_crq_count + event.low_crq_count;
  if (event.open_crq_ids.length !== openCrqCount) {
    fail("open_crq_ids length must equal the sum of CRQ severity counts");
  }
  if (!schema.properties.proof_layer.enum.includes(event.proof_layer)) fail("invalid proof_layer");

  if (event.parent_event_id !== null) requireBoundedString(event.parent_event_id, "parent_event_id", eventIdPattern);
  if (event.event_type !== "A1_HANDOFF_READY" && event.parent_event_id === null) {
    fail("non-A1 events require parent_event_id lineage");
  }

  const timestamp = Date.parse(event.created_at);
  if (!Number.isFinite(timestamp) || !/^\d{4}-\d{2}-\d{2}T/.test(event.created_at)) {
    fail("created_at must be an ISO-8601 date-time");
  }

  const expectedIdempotencyKey = `${event.batch_id}:${event.event_type}:${event.output_manifest_sha256}:${event.attempt}`;
  if (event.idempotency_key !== expectedIdempotencyKey) {
    fail("idempotency_key must be derived from batch_id, event_type, output_manifest_sha256 and attempt");
  }

  const crqFields = ["crq_ids", "crq_disposition"];
  if (event.event_type === "A2_CRQ_OPENED") {
    requireStringArray(event.crq_ids, "crq_ids", /^CRQ-[A-Z0-9._-]+$/, { minimumItems: 1 });
    if (event.crq_ids.some((crqId) => !event.open_crq_ids.includes(crqId))) {
      fail("A2_CRQ_OPENED crq_ids must be present in open_crq_ids");
    }
    if (event.crq_disposition !== "OPEN") fail("A2_CRQ_OPENED requires crq_disposition OPEN");
  } else if (event.event_type === "A1_CRQ_RESPONSE_READY") {
    requireStringArray(event.crq_ids, "crq_ids", /^CRQ-[A-Z0-9._-]+$/, { minimumItems: 1 });
    if (event.crq_ids.some((crqId) => !event.open_crq_ids.includes(crqId))) {
      fail("A1_CRQ_RESPONSE_READY crq_ids must remain present in open_crq_ids");
    }
    if (event.crq_disposition !== "ANSWERED_RESTRICTED") {
      fail("A1_CRQ_RESPONSE_READY requires crq_disposition ANSWERED_RESTRICTED");
    }
  } else if (crqFields.some((field) => field in event)) {
    fail("CRQ routing fields are allowed only for A2_CRQ_OPENED or A1_CRQ_RESPONSE_READY");
  }

  if (
    event.event_type === "A2_REVIEW_READY" &&
    (event.critical_crq_count !== 0 || event.high_crq_count !== 0 || event.blocking_dependencies.length !== 0)
  ) {
    fail("A2_REVIEW_READY requires zero Critical/High CRQs and no blocking dependencies");
  }

  const capsuleRouteEvents = new Set([
    "A2_MIXED_DISPOSITION_READY",
    "MASTER_ROUTE_A3",
    "MASTER_RETURN_A1"
  ]);
  if (capsuleRouteEvents.has(event.event_type)) {
    requireCapsuleRoutes(event.capsule_routes, event);
    const roles = new Set(event.capsule_routes.map((route) => route.next_role));
    if (event.event_type === "A2_MIXED_DISPOSITION_READY") {
      if (roles.size !== 2 || !roles.has("A1") || !roles.has("A3")) {
        fail("A2_MIXED_DISPOSITION_READY requires both A1-return and A3-forward routes");
      }
      for (const route of event.capsule_routes) {
        if (route.next_role === "A1" && route.disposition !== "REJECT_RETURN") {
          fail("A1 capsule routes require REJECT_RETURN");
        }
        if (route.next_role === "A3" && route.disposition === "REJECT_RETURN") {
          fail("A3 capsule routes cannot use REJECT_RETURN");
        }
      }
    }
    if (event.event_type === "MASTER_ROUTE_A3") {
      if ([...roles].some((role) => role !== "A3")) fail("MASTER_ROUTE_A3 may route only to A3");
      if (event.capsule_routes.some((route) => route.disposition === "REJECT_RETURN")) {
        fail("MASTER_ROUTE_A3 cannot include rejected capsules");
      }
      if (event.critical_crq_count !== 0 || event.high_crq_count !== 0 || event.blocking_dependencies.length !== 0) {
        fail("MASTER_ROUTE_A3 requires zero Critical/High CRQs and no blocking dependencies in the routed subset");
      }
    }
    if (event.event_type === "MASTER_RETURN_A1") {
      if ([...roles].some((role) => role !== "A1")) fail("MASTER_RETURN_A1 may route only to A1");
      if (event.capsule_routes.some((route) => route.disposition !== "REJECT_RETURN")) {
        fail("MASTER_RETURN_A1 requires REJECT_RETURN for every capsule");
      }
    }
  } else if ("capsule_routes" in event) {
    fail("capsule_routes are allowed only for mixed or MASTER-scoped routing events");
  }

  const autoFields = ["source_batch_id", "target_batch_id"];
  if (event.event_type === "MASTER_AUTO_CONTINUE") {
    for (const field of autoFields) requireBoundedString(event[field], field, strictIdPattern);
    if (event.source_batch_id !== event.batch_id) fail("source_batch_id must equal batch_id");
    if (event.target_batch_id === event.source_batch_id) fail("target_batch_id must differ from source_batch_id");
    if (event.critical_crq_count !== 0 || event.high_crq_count !== 0 || event.blocking_dependencies.length !== 0) {
      fail("MASTER_AUTO_CONTINUE requires zero Critical/High CRQs and no blocking dependencies");
    }
  } else if (autoFields.some((field) => field in event)) {
    fail("source_batch_id and target_batch_id are allowed only for MASTER_AUTO_CONTINUE");
  }

  const holdFields = ["hold_scope", "hold_reason_code", "finding_ids"];
  if (event.event_type === "HOLD") {
    if (!schema.properties.hold_scope.enum.includes(event.hold_scope)) fail("invalid hold_scope");
    requireBoundedString(event.hold_reason_code, "hold_reason_code", opaqueIdPattern);
    requireStringArray(event.finding_ids, "finding_ids", opaqueIdPattern, { minimumItems: 1 });
  } else if (holdFields.some((field) => field in event)) {
    fail("hold fields are allowed only for HOLD events");
  }

  console.log(`VALID ROOM A STRUCTURAL EVENT ${event.event_id} ${event.batch_id} ${event.event_type}`);
  console.log("NON-AUTHORITATIVE: canonical state, identity, parent chain and registry membership were not verified");
}

main().catch((error) => {
  console.error(`INVALID ROOM A EVENT: ${error.message}`);
  process.exitCode = 1;
});
