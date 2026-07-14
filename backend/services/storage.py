from datetime import datetime, timezone
from typing import Any, Dict
from firebase.firebase_config import ref

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def set_item(collection: str, key: str, data: Dict[str, Any]):
    ref(f"/{collection}/{key}").set(data)
    return data

def update_item(collection: str, key: str, data: Dict[str, Any]):
    ref(f"/{collection}/{key}").update(data)

def get_collection(collection: str) -> Dict[str, Any]:
    return ref(f"/{collection}").get() or {}

def get_item(collection: str, key: str):
    return ref(f"/{collection}/{key}").get()

def push_log(event: str, payload: Dict[str, Any]):
    item = {"event": event, "payload": payload, "created_at": now_iso()}
    ref("/logs").push(item)
    return item
