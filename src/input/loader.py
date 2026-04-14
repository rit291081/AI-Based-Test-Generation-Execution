from __future__ import annotations

from pathlib import Path
from typing import Any, Dict

from ..utils.helpers import load_json_file, load_text_file


def load_input(input_path: str) -> Dict[str, Any]:
    path = Path(input_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    if path.suffix.lower() in {".json"}:
        return load_json_file(path)

    return {"raw_text": load_text_file(path), "title": path.stem}
