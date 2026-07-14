from typing import List
from services.storage import get_collection, update_item, now_iso, push_log

MAX_ATTEMPTS = 3

def claim_tasks(gateway_id: str, limit: int = 5) -> List[dict]:
    messages = get_collection("messages")
    claimed = []
    for task_id, msg in messages.items():
        if len(claimed) >= limit:
            break
        if msg.get("status") != "PENDING":
            continue
        if int(msg.get("attempts", 0)) >= MAX_ATTEMPTS:
            update_item("messages", task_id, {"status": "FAILED", "updated_at": now_iso()})
            continue
        update = {"status": "PROCESSING", "gateway_id": gateway_id, "attempts": int(msg.get("attempts", 0)) + 1, "updated_at": now_iso()}
        update_item("messages", task_id, update)
        msg.update(update); msg["id"] = task_id; claimed.append(msg)
    if claimed:
        push_log("queue_claimed", {"gateway_id": gateway_id, "count": len(claimed)})
    return claimed

def complete_task(task_id: str, gateway_id: str, status: str, error: str | None = None):
    update = {"status": status, "gateway_id": gateway_id, "updated_at": now_iso()}
    if error:
        update["error"] = error
    update_item("messages", task_id, update)
    push_log("message_completed", {"task_id": task_id, "gateway_id": gateway_id, "status": status, "error": error})
    return update
