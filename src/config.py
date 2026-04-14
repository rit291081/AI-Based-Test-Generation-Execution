from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AppConfig:
    input_path: str
    output_path: str
    format_type: str = "json"
