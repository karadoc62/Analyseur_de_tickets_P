from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class TicketRequest(BaseModel):
    text: str


class TicketAnalysis(BaseModel):
    category: str
    priority: str
    summary: str


@app.get("/")
def get_home():
    return {"message": "AI Ticket Lab"}


@app.get("/health")
def get_health():
    return {"status": "ok"}
    

@app.post(
    "/tickets/analyze",
    response_model = TicketAnalysis
    )
def analyze_ticket(ticket: TicketRequest):
    return {
        "category": "NETWORK",
        "priority": "HIGH",
        "summary": "Problème de connexion Wifi"
    }