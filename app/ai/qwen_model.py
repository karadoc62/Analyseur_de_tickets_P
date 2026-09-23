import httpx

from app.ai.base import AIModel
from app.models.ticket import TicketAnalysis, TicketRequest


class QwenModel(AIModel):
    
    def __init__(self, base_url: str = "http://localhost:11434", model_name: str = "qwen3:1.7b") -> None:
        self.base_url = base_url
        self.model_name = model_name
        
    
    def analyze(self, ticket: TicketRequest) -> TicketAnalysis:
        prompt: str = "Analyse ce ticket informatique et résume le en une phrase.\n" + f"Ticket : {ticket.text}"
        
        response = httpx.post(
            f"{self.base_url}/api/generate", 
            json={
            "model": self.model_name,
            "prompt": prompt,
            "stream": False
            },
            timeout=30.0
        )
        
        response.raise_for_status()
        
        data = response.json()
        
        return TicketAnalysis(
            category="OTHER",
            priority="MEDIUM",
            summary=data["response"]
        )