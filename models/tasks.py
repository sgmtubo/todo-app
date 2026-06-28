from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class TaskORM(Base):
    __tablename__ = "tasks"

    title: Mapped[str]
    completed: Mapped[bool] = mapped_column(default=False)