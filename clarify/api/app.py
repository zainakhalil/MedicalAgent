# api/app.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

# Import our stubbed backend functions
from backend.cost_pipeline import get_cost_options_for_order
from backend.consent_rag import explain_consent, explain_term

app = FastAPI(title="Clairify API")

# ---------- Request models ----------

class CostRequest(BaseModel):
    order_id: int

class ConsentRequest(BaseModel):
    consent_id: str
    language: str = "English"

class TermRequest(BaseModel):
    term: str
    language: str = "English"

# ---------- API endpoints ----------

@app.post("/estimate_cost")
def estimate_cost(req: CostRequest):
    options = get_cost_options_for_order(req.order_id)
    return {
        "order_id": req.order_id,
        "options": options,
    }

@app.post("/consent_summary")
def consent_summary(req: ConsentRequest):
    result = explain_consent(req.consent_id, req.language)
    return result or {"error": "Failed to generate consent explanation"}

@app.post("/explain_term")
def explain_term_api(req: TermRequest):
    result = explain_term(req.term, req.language)
    return result or {"error": "Failed to explain term"}

# ---------- Static frontend ----------

# Serve the static folder (where index.html will live)
app.mount("/static", StaticFiles(directory="api/static"), name="static")

@app.get("/", response_class=HTMLResponse)
def root():
    with open("api/static/index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read())
