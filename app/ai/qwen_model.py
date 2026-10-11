import httpx
import json

from app.ai.base import AIModel
from app.ai.exceptions import AIConnectionError, AIResponseError, AITimeoutError
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
        
        
        try:
            response = httpx.post(
                f"{self.base_url}/api/generate", 
                json={
                "model": self.model_name,
                "prompt": prompt,
                "stream": False,
                "format": TicketAnalysis.model_json_schema(), # pour doubler la contrainte json en + du prompt qui est interprétable. La on contraint Ollama a générer dans du json valide aussi
                },
                timeout=30.0
            )
            
            response.raise_for_status()  # permet à httpx de lever une exception au lieu de continuer si le statut n'est pas 200 OK
        
        except httpx.TimeoutException as exc:
            raise AITimeoutError("Le serveur Ollama a mis trop longtemps pour répondre") from exc
        
        except httpx.ConnectError as exc:
            raise AIConnectionError("Impossible de joindre le serveur Ollama") from exc
        
        except httpx.HTTPStatusError as exc:
            raise AIResponseError("Ollama a retoruné une erreur HTTP") from exc
        
        data = response.json()  # transforme le JSON renvoyé par Ollama en doctionnaire python
        
        print("Réponse brute Ollama :", data, flush=True)
        print("Contenu généré :", data["response"], flush=True)
        
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