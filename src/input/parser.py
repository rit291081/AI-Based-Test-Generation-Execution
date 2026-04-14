from __future__ import annotations

from typing import Any, Dict


REQUIRED_KEYS = ["title", "method", "endpoint"]


def parse_spec(raw: Dict[str, Any]) -> Dict[str, Any]:
    if "raw_text" in raw:
        return {
            "title": raw.get("title", "Untitled API Spec"),
            "method": "N/A",
            "endpoint": "N/A",
            "description": raw["raw_text"],
            "headers": {},
            "request": {},
            "response": {},
            "constraints": [],
        }

    parsed = dict(raw)
    for key in REQUIRED_KEYS:
        parsed.setdefault(key, "N/A")
    parsed.setdefault("description", "")
    parsed.setdefault("headers", {})
    parsed.setdefault("request", {})
    parsed.setdefault("response", {})
    parsed.setdefault("constraints", [])
    return parsed
