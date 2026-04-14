# src/models.py
from pydantic import BaseModel
from typing import List, Literal, Optional

class APIInput(BaseModel):
    name: str
    method: str
    endpoint: str
    fields: List[str]

class TestCase(BaseModel):
    name: str
    type: Literal["positive", "negative", "edge"]
    input: dict
    expected_status: Optional[int] = None
    notes: Optional[str] = None

class TestCaseBatch(BaseModel):
    test_cases: List[TestCase]
