from app.ai.base import AIModel
from app.ai.fake_model import FakeAIModel
from app.ai.qwen_model import QwenModel


def create_ai_model(model_name: str) -> AIModel:
    if model_name == "fake":
        return FakeAIModel()
    elif model_name == "qwen3:1.7b":
        return QwenModel()
    
    raise ValueError(f"Modèle IA inconnu : {model_name}")
