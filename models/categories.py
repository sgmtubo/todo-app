from sqlalchemy.orm import Mapped
from database import Base

class CategoryORM(Base):
    __tablename__ = "categories"

    name: Mapped[str]