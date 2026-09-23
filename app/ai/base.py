from abc import ABC, abstractmethod
from app.models.ticket import TicketAnalysis, TicketRequest

class AIModel(ABC):
    
    @abstractmethod
    def analyze(self, ticket: TicketRequest) -> TicketAnalysis:
        pass
