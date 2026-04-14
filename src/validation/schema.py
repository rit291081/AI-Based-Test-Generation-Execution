from __future__ import annotations

REQUIRED_FIELDS = {
    "id": str,
    "title": str,
    "type": str,
    "priority": str,
    "preconditions": list,
    "steps": list,
    "expected_result": str,
    "data": dict,
    "tags": list,
}

ALLOWED_TYPES = {"positive", "negative", "edge"}
ALLOWED_PRIORITIES = {"high", "medium", "low"}
