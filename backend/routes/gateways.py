import secrets
from fastapi import APIRouter
from models.schemas import GatewayRegister, Heartbeat
from services.storage import set_item, update_item, get_collection, get_item, now_iso, push_log
router = APIRouter(prefix="/gateway", tags=["gateways"])
@router.post("/register")
def register_gateway(payload: GatewayRegister):
    token = payload.token or secrets.token_urlsafe(24)
    data = payload.model_dump(); data.update({"token": token, "status":"ONLINE", "last_seen": now_iso(), "sent_count":0})
    set_item("gateways", payload.gateway_id, data); push_log("gateway_connected", data)
    return data
@router.get("/list")
def list_gateways(): return {"gateways": list(get_collection("gateways").values())}
@router.post("/heartbeat")
def heartbeat(payload: Heartbeat):
    update_item("gateways", payload.gateway_id, {"status":"ONLINE", "battery":payload.battery, "sent_count":payload.sent_count, "last_seen":now_iso()})
    return {"status":"ok"}
@router.get("/status")
def status(gateway_id: str): return get_item("gateways", gateway_id) or {"status":"UNKNOWN"}
