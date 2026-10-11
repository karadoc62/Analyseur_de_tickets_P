import os

from fastapi import FastAPI, HTTPException

from app.ai.factory import create_ai_model
from app.ai.exceptions import AIResponseError, AIConnectionError, AITimeoutError
from app.services.ticket_analyzer import analyze_ticket
from app.models.ticket import TicketAnalysis, TicketRequest

app = FastAPI()
model_name = os.getenv("AI_MODEL", "fake")  # cherche une var d'env appelée AI_MoDEL mais par default fake
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
    try:
        return analyze_ticket(ticket, model)
    
    except AIConnectionError as exc:
        raise HTTPException(
            status_code=503,  # Service Unavailable
            detail=str(exc),
        ) from exc
    
    except AITimeoutError as exc:
        raise HTTPException(
            status_code=504,  
            detail=str(exc)
        ) from exc
        
    except AIResponseError as exc:
        raise HTTPException(
            code_status=502,  # Bad Gateway
            detail=str(exc)
        )
        