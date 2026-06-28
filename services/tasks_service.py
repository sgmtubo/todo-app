from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from models import TaskORM
from schemas.tasks import TaskCreateSchema, TaskUpdateSchema

class TaskService:
    def __init__(self, db: Session):
        self.db = db

    def list_tasks(self):
        return self.db.query(TaskORM).all()

    def create_task(self, payload: TaskCreateSchema):
        task = TaskORM(title=payload.title, completed=False)
        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)
        return task

    def get_task_or_404(self, task_id: str):
        task = self.db.get(TaskORM, task_id)
        if task is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task not found")
        return task

    def update_task(self, task_id: str, payload: TaskUpdateSchema):
        task = self.get_task_or_404(task_id)
        if payload.title is not None:
            task.title = payload.title
        if payload.completed is not None:
            task.completed = payload.completed
        self.db.commit()
        self.db.refresh(task)
        return task

    def delete_task(self, task_id: str):
        task = self.get_task_or_404(task_id)
        self.db.delete(task)
        self.db.commit()