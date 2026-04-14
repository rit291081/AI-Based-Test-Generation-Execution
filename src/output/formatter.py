from __future__ import annotations

import csv
import io
import json
from typing import Any, Dict, List


def format_json(test_cases: List[Dict[str, Any]], metadata: Dict[str, Any] | None = None) -> str:
    payload = {
        "metadata": metadata or {},
        "count": len(test_cases),
        "test_cases": test_cases,
    }
    return json.dumps(payload, indent=2)


def format_csv(test_cases: List[Dict[str, Any]]) -> str:
    buffer = io.StringIO()
    writer = csv.writer(buffer)
    writer.writerow(["id", "title", "type", "priority", "expected_result", "tags"])
    for case in test_cases:
        writer.writerow([
            case.get("id", ""),
            case.get("title", ""),
            case.get("type", ""),
            case.get("priority", ""),
            case.get("expected_result", ""),
            ";".join(case.get("tags", [])),
        ])
    return buffer.getvalue()
