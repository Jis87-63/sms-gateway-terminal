from uuid import uuid4
from fastapi import APIRouter
from models.schemas import MessageCreate
from services.storage import set_item, get_collection, get_item, now_iso
router = APIRouter(prefix="/message", tags=["messages"])
@router.post("/create")
def create_message(payload: MessageCreate):
    mid=str(uuid4()); data={"id":mid, **payload.model_dump(), "status":"PENDING", "gateway_id":None, "attempts":0, "created_at":now_iso(), "updated_at":now_iso()}
    set_item("messages", mid, data); return data
@router.get("/list")
def list_messages(): return {"messages": list(get_collection("messages").values())}
@router.get("/status/{message_id}")
def message_status(message_id: str): return get_item("messages", message_id) or {"status":"NOT_FOUND"}
