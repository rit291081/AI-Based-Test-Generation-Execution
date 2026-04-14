from __future__ import annotations

from typing import Any, Dict, List, Tuple

from .schema import ALLOWED_PRIORITIES, ALLOWED_TYPES, REQUIRED_FIELDS


def validate_test_cases(cases: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[str]]:
    valid: List[Dict[str, Any]] = []
    errors: List[str] = []

    for idx, case in enumerate(cases, start=1):
        prefix = f"Test case {idx}"
        if not isinstance(case, dict):
            errors.append(f"{prefix}: must be an object")
            continue

        missing = [field for field in REQUIRED_FIELDS if field not in case]
        if missing:
            errors.append(f"{prefix}: missing fields {missing}")
            continue

        type_value = case.get("type")
        if type_value not in ALLOWED_TYPES:
            errors.append(f"{prefix}: invalid type '{type_value}'")
            continue

        priority_value = case.get("priority")
        if priority_value not in ALLOWED_PRIORITIES:
            errors.append(f"{prefix}: invalid priority '{priority_value}'")
            continue

        valid.append(case)

    return valid, errors
