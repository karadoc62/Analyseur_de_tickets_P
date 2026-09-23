import os

from fastapi import FastAPI

from app.ai.factory import create_ai_model
from app.services.ticket_analyzer import analyze_ticket
from app.models.ticket import TicketAnalysis, TicketRequest

app = FastAPI()
model_name = os.getenv("AI_MODEL", "fake")
model = create_ai_model(model_name)

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
def analyze_ticket_route(ticket: TicketRequest):
    return analyze_ticket(ticket, model)
