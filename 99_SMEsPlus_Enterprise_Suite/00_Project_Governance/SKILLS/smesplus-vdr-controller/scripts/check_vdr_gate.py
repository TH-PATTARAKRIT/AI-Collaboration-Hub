#!/usr/bin/env python3
"""Deterministic gate check for a SMEsPlus VDR coverage summary.

Input JSON example:
{
  "denominator_status": "FROZEN",
  "dimensions": {"Research": 99, "Runtime": 97, "Configuration": 96},
  "zero_tolerance": 100,
  "critical_gap_open": false,
  "material_contradiction_open": false
}
"""
import argparse
import json
import sys

FLOOR = 96.0
ZERO_TOLERANCE = 100.0


def evaluate(data):
    reasons = []
    denominator = str(data.get("denominator_status", "")).upper()
    formal_coverage_allowed = denominator == "FROZEN"
    if not formal_coverage_allowed:
        reasons.append("DENOMINATOR NOT FROZEN - FORMAL COVERAGE SUSPENDED")

    dimensions = data.get("dimensions") or {}
    below_floor = {}
    for name, value in dimensions.items():
        try:
            score = float(value)
        except (TypeError, ValueError):
            reasons.append(f"INVALID DIMENSION SCORE: {name}")
            continue
        if score < FLOOR:
            below_floor[name] = score
            reasons.append(f"APPLICABLE DIMENSION BELOW 96%: {name}={score:g}%")

    zt = data.get("zero_tolerance")
    if zt is not None:
        try:
            zt_score = float(zt)
            if zt_score < ZERO_TOLERANCE:
                reasons.append(f"ZERO-TOLERANCE BELOW 100%: {zt_score:g}%")
        except (TypeError, ValueError):
            reasons.append("INVALID ZERO-TOLERANCE SCORE")

    if bool(data.get("critical_gap_open")):
        reasons.append("CRITICAL GAP OPEN")
    if bool(data.get("material_contradiction_open")):
        reasons.append("UNRESOLVED MATERIAL CONTRADICTION")
    if bool(data.get("denominator_contamination")):
        reasons.append("DENOMINATOR CONTAMINATION")
    if bool(data.get("uncontrolled_na")):
        reasons.append("UNCONTROLLED N/A")

    disposition = "PASS RECOMMENDATION" if not reasons else "HOLD RECOMMENDATION"
    return {
        "formal_coverage_allowed": formal_coverage_allowed,
        "below_floor": below_floor,
        "disposition": disposition,
        "reasons": reasons,
        "boss_decision": "PENDING",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Path to VDR summary JSON")
    args = parser.parse_args()
    with open(args.input, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    result = evaluate(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["disposition"] == "PASS RECOMMENDATION" else 2


if __name__ == "__main__":
    sys.exit(main())
