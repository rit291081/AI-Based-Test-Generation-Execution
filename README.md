# 🚀 AI-Based Test Generation & Execution Framework

## 🧠 Overview
This project demonstrates an end-to-end **AI-powered QA system** that:

- Generates test cases using Large Language Models (LLMs)
- Executes tests against a live API (FastAPI)
- Validates responses with automated pass/fail reporting

It showcases how AI can be integrated into the **full QA lifecycle**, not just test generation.

---

## ✨ Key Features

- 🤖 AI-driven test case generation (OpenAI)
- ⚙️ FastAPI-based test application (System Under Test)
- 🧪 Automated test execution engine
- ✅ Validation for positive, negative, and edge cases
- 🔁 Deterministic test runs using reset API
- 📊 Structured pass/fail reporting

---

## 🏗️ Architecture
API Spec → AI Generator → Test Cases → Runner → FastAPI → Results

---

## ⚙️ Tech Stack

- Python
- FastAPI
- OpenAI API
- Requests
- Pydantic

---

## 📂 Project Structure


ai-test-generation-framework/
│
├── src/
│ ├── main.py # Generates test cases using AI
│ ├── run_tests.py # Executes generated tests
│ ├── engine/ # LLM-based generation logic
│ └── execution/ # Test execution layer
│
├── app.py # FastAPI test application
├── sample_input.json # API contract input
├── generated_tests.json # AI-generated test cases
├── requirements.txt
└── README.md

---

## ▶️ How to Run

### 1️⃣ Start the API (System Under Test)
```bash
uvicorn app:app --reload --port 8090

2️⃣ Generate Test Cases using AI
python src/main.py sample_input.json > generated_tests.json

3️⃣ Run Tests
export BASE_URL=http://127.0.0.1:8090
python src/run_tests.py generated_tests.json

🧪 Sample Output
INFO:   127.0.0.1:59247 - "POST /users HTTP/1.1" 201 Created
PASS | Successful user creation with valid data | expected=201 | actual=201
INFO:   127.0.0.1:59248 - "POST /users HTTP/1.1" 201 Created
PASS | Successful admin user creation | expected=201 | actual=201
INFO:   127.0.0.1:59249 - "POST /users HTTP/1.1" 401 Unauthorized
PASS | Missing Authorization header | expected=401 | actual=401
INFO:   127.0.0.1:59250 - "POST /users HTTP/1.1" 400 Bad Request
PASS | Duplicate email error | expected=400 | actual=400

🙌 Acknowledgment

This project was inspired by:
https://github.com/halovivek/ai-test-generation-framework
and extended with:
--execution engine
--FastAPI integration
--validation layer
--deterministic testing approach

📌 Author
Ritesh Srivastava


