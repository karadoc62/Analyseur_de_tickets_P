from app.ai.fake_model import FakeAIModel
from app.models.ticket import TicketAnalysis, TicketRequest

def analyze_ticket(ticket: TicketRequest) -> TicketAnalysis:
    model = FakeAIModel()
    return model.analyze(ticket)