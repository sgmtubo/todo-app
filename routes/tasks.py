from fastapi import APIRouter
from schemas.tasks import TaskSchema, TaskCreateSchema, TaskUpdateSchema
from database import tasks
from uuid import uuid4

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"]
)

@router.get("")
def read_tasks() -> list[TaskSchema]:
    return tasks

@router.post("")
def create_task(payload: TaskCreateSchema) -> TaskSchema:
    new_task = TaskSchema(id=str(uuid4()), title=payload.title, completed=False)

    tasks.append(new_task)
    return new_task

@router.patch("/{task_id}")
def update_task(task_id: str, payload: TaskUpdateSchema):
    for task in tasks:
        if task.id == task_id:
            if payload.title:
                task.title = payload.title
            if payload.completed is not None:
                task.completed = payload.completed
            return task

@router.delete("/{task_id}")
def delete_task(task_id: str):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
