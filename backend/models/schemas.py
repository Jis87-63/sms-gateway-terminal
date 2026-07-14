from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class MessageStatus(str, Enum):
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    SENT = "SENT"
    FAILED = "FAILED"

class LoginRequest(BaseModel):
    username: str
    password: str

class GatewayRegister(BaseModel):
    gateway_id: str
    name: str
    model: str = "Android"
    battery: int = 0
    token: Optional[str] = None

class Heartbeat(BaseModel):
    gateway_id: str
    battery: int = 0
    sent_count: int = 0

class MessageCreate(BaseModel):
    number: str
    message: str
    campaign_id: Optional[str] = None

class CampaignCreate(BaseModel):
    name: str
    message: str
    numbers: List[str] = Field(default_factory=list)

class QueueComplete(BaseModel):
    task_id: str
    gateway_id: str
    status: MessageStatus
    error: Optional[str] = None
