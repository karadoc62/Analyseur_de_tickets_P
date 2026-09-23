from app.models.ticket import TicketAnalysis, TicketRequest
from app.ai.base import AIModel


class FakeAIModel(AIModel):
    def analyze(self, ticket: TicketRequest) -> TicketAnalysis:
        return TicketAnalysis(
            category="NETWORK",
            priority="HIGH",
            summary="Problème de connexion Wifi"
        )