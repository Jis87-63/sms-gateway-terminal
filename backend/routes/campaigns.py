from uuid import uuid4
from fastapi import APIRouter
from models.schemas import CampaignCreate
from services.storage import set_item, get_collection, now_iso
router = APIRouter(prefix="/campaign", tags=["campaigns"])
@router.post("/create")
def create_campaign(payload: CampaignCreate):
    cid=str(uuid4()); campaign={"id":cid, **payload.model_dump(), "status":"ACTIVE", "created_at":now_iso()}; set_item("campaigns", cid, campaign)
    for number in payload.numbers:
        mid=str(uuid4()); set_item("messages", mid, {"id":mid,"number":number,"message":payload.message,"campaign_id":cid,"status":"PENDING","gateway_id":None,"attempts":0,"created_at":now_iso(),"updated_at":now_iso()})
    return campaign
@router.get("/list")
def list_campaigns(): return {"campaigns": list(get_collection("campaigns").values())}
