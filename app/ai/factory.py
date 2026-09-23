from app.ai.base import AIModel
from app.ai.fake_model import FakeAIModel

def create_ai_model(model_name: str) -> AIModel:
    if model_name == "fake":
        return FakeAIModel()
    
    raise ValueError(f"Modèle IA inconnu : {model_name}")
