# src/run_tests.py
import json
import os
import sys
from typing import Any, Dict, List, Tuple

import requests

DEFAULT_BASE_URL = os.getenv("BASE_URL", "http://127.0.0.1:8070")


def load_generated_tests(path: str) -> List[Dict[str, Any]]:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if "test_cases" not in data or not isinstance(data["test_cases"], list):
        raise ValueError("Invalid test file format: expected top-level 'test_cases' list.")

    return data["test_cases"]


def input_to_payload(input_items: List[Dict[str, Any]]) -> Dict[str, Any]:
    payload: Dict[str, Any] = {}
    for item in input_items:
        key = item.get("key")
        value = item.get("value")
        if key:
            payload[key] = value
    return payload


def execute_test_case(test_case: Dict[str, Any], base_url: str) -> Dict[str, Any]:
    endpoint = "/users"
    method = "POST"
    expected_status = test_case.get("expected_status")
    name = test_case.get("name", "Unnamed Test")
    test_type = test_case.get("type", "unknown")

    payload = input_to_payload(test_case.get("input", []))
    url = f"{base_url}{endpoint}"

    headers = {}
    
    use_auth = test_case.get("use_auth", True)
    if use_auth:
        headers["Authorization"] = "Bearer demo-token"
    
    if "headers" in test_case and isinstance(test_case["headers"], dict):
        headers.update(test_case["headers"])

    try:
        if method.upper() == "POST":
            response = requests.post(url, json=payload, headers=headers, timeout=15)
        else:
            raise ValueError(f"Unsupported method: {method}")

        actual_status = response.status_code

        try:
            response_body = response.json()
        except Exception:
            response_body = response.text

        passed = expected_status == actual_status if expected_status is not None else True

        return {
            "name": name,
            "type": test_type,
            "expected_status": expected_status,
            "actual_status": actual_status,
            "passed": passed,
            "request_payload": payload,
            "response": response_body,
        }

    except requests.RequestException as e:
        return {
            "name": name,
            "type": test_type,
            "expected_status": expected_status,
            "actual_status": None,
            "passed": False,
            "request_payload": payload,
            "error": str(e),
        }


def print_result(result: Dict[str, Any]) -> None:
    status = "PASS" if result["passed"] else "FAIL"
    actual = result.get("actual_status")
    expected = result.get("expected_status")
    name = result.get("name", "Unnamed Test")

    print(f"{status} | {name} | expected={expected} | actual={actual}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 src/run_tests.py <generated_tests.json>")
        sys.exit(1)

    tests_file = sys.argv[1]
    base_url = DEFAULT_BASE_URL

    try:
        test_cases = load_generated_tests(tests_file)
    except Exception as e:
        print(f"Failed to load tests: {e}")
        sys.exit(1)

    requests.post(f"{base_url}/_reset")
    print(f"Running {len(test_cases)} test cases against {base_url}\n")

    results: List[Dict[str, Any]] = []
    passed_count = 0
    failed_count = 0

    for test_case in test_cases:
        result = execute_test_case(test_case, base_url)
        results.append(result)
        print_result(result)

        if result["passed"]:
            passed_count += 1
        else:
            failed_count += 1

    summary = {
        "total": len(test_cases),
        "passed": passed_count,
        "failed": failed_count,
        "results": results,
    }

    print("\nSummary:")
    print(json.dumps(summary, indent=2))

    with open("test_results.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    sys.exit(0 if failed_count == 0 else 1)


if __name__ == "__main__":
    main()
