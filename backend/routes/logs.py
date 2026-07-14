from fastapi import APIRouter
from services.storage import get_collection
router=APIRouter(prefix="/logs", tags=["logs"])
@router.get("")
def logs(): return {"logs": list(get_collection("logs").values())}
