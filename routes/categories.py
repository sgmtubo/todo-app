from fastapi import APIRouter
from schemas.categories import CategorySchema, CategoryCreateSchema
from database import categories
from uuid import uuid4

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("")
def read_categories()->list[CategorySchema]:
    return categories

@router.post("")
def create_category(payload: CategoryCreateSchema):
    new_category = CategorySchema(id=str(uuid4()), name=payload.name)
    categories.append(new_category)
    return new_category