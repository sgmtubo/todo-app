from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from models import CategoryORM
from schemas.categories import CategorySchema, CategoryCreateSchema, CategoryUpdateSchema
from database import get_db

router = APIRouter(
    prefix="/categories",
    tags=["categories"]
)

@router.get("")
def read_categories(db: Session = Depends(get_db()))->list[CategorySchema]:
    return db.query(CategoryORM).all()

@router.post("")
def create_category(payload: CategoryCreateSchema, db: Session = Depends(get_db)) -> CategorySchema:
    new_category = CategoryORM(name=payload.name)
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category

@router.patch("/{category_id}")
def update_category(category_id: str, payload:CategoryUpdateSchema, db: Session = Depends(get_db)) -> CategorySchema:
    category = db.get(CategoryORM, category_id)
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    if payload.name is not None:
        category.name = payload.name
    db.commit()
    db.refresh(category)
    return category

@router.delete("/{category_id}")
def delete_category(category_id: str, db: Session = Depends(get_db)):
    category = db.get(CategoryORM, category_id)
    if category is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Category not found")
    db.delete(category)
    db.commit()
