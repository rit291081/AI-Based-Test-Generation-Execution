import json
import sys
from pathlib import Path

from engine.generator import generate_test_cases_from_spec


def load_spec(input_path: str) -> dict:
    path = Path(input_path)

    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 src/main.py <sample_input.json>", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]

    try:
        api_spec = load_spec(input_path)
        batch = generate_test_cases_from_spec(api_spec)
        print(json.dumps(batch.model_dump(), indent=2, ensure_ascii=False))
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
