from fastapi import APIRouter
from schemas.categories import CategorySchema, CategoryCreateSchema, CategoryUpdateSchema
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

@router.patch("/{category_id}")
def update_category(category_id: str, payload:CategoryUpdateSchema):
    for category in categories:
        if category.id == category_id:
            category.name = payload.name
            return category

@router.delete("/{category_id}")
def delete_category(category_id: str):
    for category in categories:
        if category.id == category_id:
            categories.remove(category)
