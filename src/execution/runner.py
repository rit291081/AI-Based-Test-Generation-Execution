# src/execution/runner.py
import requests

BASE_URL = "http://127.0.0.1:8070"

def run_test_case(test_case):
    url = f"{BASE_URL}/users"
    payload = {item["key"]: item["value"] for item in test_case.get("input", [])}

    try:
        response = requests.post(url, json=payload)
        return {
            "name": test_case.get("name"),
            "status_code": response.status_code,
            "response": response.json()
        }
    except Exception as e:
        return {
            "name": test_case.get("name"),
            "error": str(e)
        }
