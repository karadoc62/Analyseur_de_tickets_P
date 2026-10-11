from app.ai.fake_model import AIModel
from app.models.ticket import TicketAnalysis, TicketRequest

def analyze_ticket(ticket: TicketRequest, model: AIModel) -> TicketAnalysis:
    return model.analyze(ticket)