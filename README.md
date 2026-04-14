# AI Test Generation Framework

A modular Python CLI for generating QA test cases from API specs.

## Features
- JSON or text input
- Modular pipeline: input -> prompt -> LLM/fallback -> validation -> export
- Optional OpenAI integration
- JSON or CSV output

## Run locally

```bash
pip install -r requirements.txt
python src/main.py --input sample_input.json --output output/test_cases.json --format json
```

If `OPENAI_API_KEY` is not set, the framework uses an offline heuristic generator.

## Sample output
Generated files are written to the path you pass in `--output`.
