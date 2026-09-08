from enum import Enum
from pydantic import BaseModel

class Priority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    
class Category(str, Enum):
    NETWORK = "NETWORK"
    SOFTWARE = "SOFTWARE"
    HARDWARE = "HARDWARE"
    ACCOUNT = "ACCOUNT"
    OTHER = "OTHER"


class TicketRequest(BaseModel):
    text: str


class TicketAnalysis(BaseModel):
    category: Category
    priority: Priority
    summary: str