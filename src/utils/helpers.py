from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict


def load_json_file(path: str | Path) -> Dict[str, Any]:
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_text_file(path: str | Path) -> str:
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return f.read()


def ensure_parent_dir(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)
