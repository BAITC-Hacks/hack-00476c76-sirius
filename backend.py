from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="IdeaMatch API")

WEIGHTS = {
    "context": 20, "data": 20, "expected": 15,
    "success": 15, "constraints": 10, "users": 10, "contact": 10
}

class TaskCard(BaseModel):
    context: str = ""
    data: str = ""
    expected: str = ""
    success: str = ""
    constraints: str = ""
    users: str = ""
    contact: str = ""

@app.get("/health")
def health():
    return {"status": "ok", "service": "IdeaMatch"}

@app.post("/api/readiness")
def readiness(card: TaskCard):
    values = card.model_dump()
    score = sum(WEIGHTS[k] for k, value in values.items() if value.strip())
    missing = [k for k, value in values.items() if not value.strip()]
    level = "draft" if score < 40 else "working" if score < 70 else "ready" if score < 90 else "priority"
    return {"score": score, "level": level, "missing": missing, "weights": WEIGHTS}

@app.post("/api/clarify")
def clarify(card: TaskCard):
    # No invented facts: only returns questions for missing fields.
    questions = {
        "context": "What exact problem should be solved?",
        "data": "What data or materials are available?",
        "expected": "What result do you expect?",
        "success": "How will success be measured?",
        "constraints": "What constraints must be respected?",
        "users": "Who are the target users?",
        "contact": "How can the team communicate with the business?"
    }
    values = card.model_dump()
    return {"questions": [questions[k] for k, v in values.items() if not v.strip()][:6]}
