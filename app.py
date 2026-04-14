from fastapi import FastAPI, HTTPException, Header, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, EmailStr, constr
from typing import Optional, Literal

app = FastAPI()

# -------------------------------
# Seed Data
# -------------------------------
SEED_USERS = [
    {
        "name": "John Doe",
        "email": "john@example.com",
        "password": "SeedPass123!",
        "role": "user",
    }
]

users = []


def reset_users():
    global users
    users = [u.copy() for u in SEED_USERS]


@app.on_event("startup")
def startup_event():
    reset_users()


@app.post("/_reset")
def reset_state():
    reset_users()
    return {"message": "State reset"}


# -------------------------------
# Convert 422 → 400
# -------------------------------
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=400,
        content={"message": "Validation failed", "detail": exc.errors()},
    )


# -------------------------------
# User Model (STRICT VALIDATION)
# -------------------------------
class User(BaseModel):
    name: constr(min_length=1, max_length=256)
    email: EmailStr
    password: constr(min_length=8)
    role: Literal["user", "admin"]


# -------------------------------
# Health Check
# -------------------------------
@app.get("/")
def root():
    return {"message": "API is running"}


# -------------------------------
# Create User API
# -------------------------------
@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: User, authorization: Optional[str] = Header(default=None)):
    if authorization is None:
        raise HTTPException(status_code=401, detail="Missing Authorization header")

    if len(user.name) > 256:
        raise HTTPException(status_code=400, detail="Name exceeds maximum length")

    for u in users:
        if u["email"].lower() == user.email.lower():
            raise HTTPException(status_code=400, detail="User already exists")

    users.append(user.model_dump())
    return {"message": "User created successfully", "user": user}
