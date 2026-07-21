from pydantic import BaseModel, Field
from typing import Optional

# Das Schema für die eingehende Anfrage an den Agenten
class AgentQueryRequest(BaseModel):
    prompt: str = Field(..., description="Die Frage oder Anweisung an den KI-Agenten", example="Wie erstelle ich einen Webhook in n8n?")
    user_id: Optional[str] = Field(default="anonymous", description="Optionale ID des Nutzers")

# Das Schema für die Antwort, die unsere API zurückgibt
class AgentQueryResponse(BaseModel):
    query: str
    response: str
    agent_used: str
    status: str = "success"