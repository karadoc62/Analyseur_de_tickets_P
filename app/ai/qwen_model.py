import httpx
import json

from app.ai.base import AIModel
from app.models.ticket import TicketAnalysis, TicketRequest


class QwenModel(AIModel):
    
    def __init__(self, base_url: str = "http://localhost:11434", model_name: str = "qwen3:1.7b") -> None:
        self.base_url = base_url
        self.model_name = model_name

    
    def analyze(self, ticket: TicketRequest) -> TicketAnalysis:
        # prompt: str = "Analyse ce ticket informatique et résume le en une phrase.\n" + f"Ticket : {ticket.text}"
        prompt: str = ("Analyse ce ticket informatique.\n"
        "Réponds uniquement avec un objet JSON valide.\n"
        "Le JSON doit avoir exactement cette structure :\n"
        "{\n"
        '  "category": "NETWORK | SOFTWARE | HARDWARE | ACCOUNT | OTHER",\n'
        '  "priority": "LOW | MEDIUM | HIGH",\n'
        '  "summary": "résumé court du problème"\n'
        "}\n"
        "N'ajoute aucun texte avant ou après le JSON.\n\n"
        f"Ticket : {ticket.text}" )
        
        response = httpx.post(
            f"{self.base_url}/api/generate", 
            json={
            "model": self.model_name,
            "prompt": prompt,
            "stream": False,
            "format": json, # pour doubler la contrainte json en + du prompt qui est interprétable
            },
            timeout=30.0
        )
        
        response.raise_for_status()
        
        data = response.json()
        
        raw_content = data["response"] # ici raw_content est toujours un str
        # il faut transformer cette chaine JSON en objet python -> import json
        parsed_data = json.loads(raw_content) # json.loads signifie charge du json depuis une chaine de caracteres
        
        
        # return TicketAnalysis(
        #     category=parsed_data["category"],
        #     priority=parsed_data["priority"],
        #     summary=parsed_data["summary"]
        # )
        
        # plus directement avec pydantic:
        return TicketAnalysis.model_validate(parsed_data)