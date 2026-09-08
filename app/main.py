from fastapi import FastAPI
from app.services.ticket_analyzer import analyze_ticket
from app.models.ticket import TicketAnalysis, TicketRequest

app = FastAPI()

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
    return analyze_ticket(ticket)
