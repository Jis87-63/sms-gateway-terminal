from fastapi import APIRouter
from services.storage import get_collection
router=APIRouter(prefix="/stats", tags=["stats"])
@router.get("")
def stats():
    msgs=list(get_collection("messages").values()); gates=list(get_collection("gateways").values()); camps=list(get_collection("campaigns").values())
    return {"sent":sum(m.get("status")=="SENT" for m in msgs),"pending":sum(m.get("status")=="PENDING" for m in msgs),"failed":sum(m.get("status")=="FAILED" for m in msgs),"online_gateways":sum(g.get("status")=="ONLINE" for g in gates),"active_campaigns":sum(c.get("status")=="ACTIVE" for c in camps)}
