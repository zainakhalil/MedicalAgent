from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import threading

from pipelines.cost_pipeline import run_engine, get_cost_options
from pipelines.consent_rag import explain_consent, explain_term
from pydantic import BaseModel

app = FastAPI(title="Clairify Backend")

# ----- CORS -----
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ----- START PATHWAY ENGINE -----
@app.on_event("startup")
def start_engine():
    thread = threading.Thread(target=run_engine, daemon=True)
    thread.start()

# ----- API MODELS -----
class CostReq(BaseModel):
    order_id: int

class ConsentReq(BaseModel):
    consent_id: str
    language: str = "English"

class TermReq(BaseModel):
    term: str
    language: str = "English"


# ----- ROUTES -----
@app.post("/estimate_cost")
def estimate_cost(req: CostReq):
    return get_cost_options(req.order_id)

@app.post("/consent_summary")
def consent_summary(req: ConsentReq):
    return explain_consent(req.consent_id, req.language)

@app.post("/explain_term")
def explain_term_api(req: TermReq):
    return explain_term(req.term, req.language)


# ----- SERVE FRONTEND -----
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")
