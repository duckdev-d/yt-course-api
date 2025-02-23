from fastapi import APIRouter, status

from schemas import STaskAdd, STask, STaskId
from repo import TaskRepo


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_task(task: STaskAdd) -> STaskId:
    task_id = await TaskRepo.add_one(task)
    return {"task_id": task_id}


@router.get("/")
async def get_tasks() -> list[STask]:
    tasks = await TaskRepo.get_all()
    return tasks
