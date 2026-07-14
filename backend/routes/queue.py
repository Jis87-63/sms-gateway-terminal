from fastapi import APIRouter
from models.schemas import QueueComplete
from services.queue_manager import claim_tasks, complete_task
router = APIRouter(prefix="/queue", tags=["queue"])
@router.get("/tasks")
def tasks(gateway_id: str, limit: int = 5): return {"tasks": claim_tasks(gateway_id, limit)}
@router.post("/complete")
def complete(payload: QueueComplete): return complete_task(payload.task_id, payload.gateway_id, payload.status.value, payload.error)
