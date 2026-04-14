from __future__ import annotations

from typing import Any, Dict


def build_prompt(spec: Dict[str, Any]) -> str:
    return f"""
You are a senior QA engineer.
Generate a concise but thorough JSON array of test cases for this API.

API Title: {spec.get('title')}
Method: {spec.get('method')}
Endpoint: {spec.get('endpoint')}
Description: {spec.get('description', '')}
Headers: {spec.get('headers', {})}
Request: {spec.get('request', {})}
Response Examples: {spec.get('response', {})}
Constraints: {spec.get('constraints', [])}

Return ONLY valid JSON. Each test case must contain:
- id
- title
- type (positive, negative, edge)
- priority (high, medium, low)
- preconditions
- steps
- expected_result
- data
- tags
""".strip()
