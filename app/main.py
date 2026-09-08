from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum


app = FastAPI()


class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    
class Category(str, Enum):
    NETWORK = "NETWORK"
    SOFTWARE = "SOFTWARE"
    HARDWARE = "HARDWARE"
    ACCOUNT = "ACCOUNT"
    OTHER = "OTHER"


class TicketRequest(BaseModel):
    text: str


class TicketAnalysis(BaseModel):
    category: Category
    priority: Priority
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