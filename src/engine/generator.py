# src/engine/generator.py
import os
from typing import List, Literal, Optional

from openai import OpenAI
from pydantic import BaseModel, ConfigDict

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class InputField(BaseModel):
    model_config = ConfigDict(extra="forbid")
    key: str
    value: str


class TestCase(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str
    type: Literal["positive", "negative", "edge"]
    input: List[InputField]
    expected_status: Optional[int] = None
    notes: Optional[str] = None


class TestCaseBatch(BaseModel):
    model_config = ConfigDict(extra="forbid")
    test_cases: List[TestCase]


def generate_test_cases_from_spec(api_spec: dict) -> TestCaseBatch:
    prompt = f"""
You are a senior QA engineer.
Generate test cases for this API spec:

{api_spec}

Return a diverse set of positive, negative, and edge test cases.
Represent each input as a list of key/value pairs.
"""

    response = client.responses.parse(
        model="gpt-4.1",
        input=[
            {
                "role": "system",
                "content": "You generate high-quality API test cases in structured JSON only.",
            },
            {"role": "user", "content": prompt},
        ],
        text_format=TestCaseBatch,
    )

    return response.output_parsed
