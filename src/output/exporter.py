from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List

from ..utils.helpers import ensure_parent_dir
from .formatter import format_csv, format_json


def export_output(test_cases: List[Dict[str, Any]], output_path: str, format_type: str = "json", metadata: Dict[str, Any] | None = None) -> str:
    ensure_parent_dir(output_path)
    fmt = format_type.lower()

    if fmt == "csv":
        content = format_csv(test_cases)
    else:
        content = format_json(test_cases, metadata=metadata)

    Path(output_path).write_text(content, encoding="utf-8")
    return output_path
