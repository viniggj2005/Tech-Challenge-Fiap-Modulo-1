from fastapi import APIRouter
from app.services.book_service import get_books,get_book_by_id
router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/")
def list_books():
    return get_books()

@router.get("/{id}")
def list_books(id:int):
    print("chamada certa")
    return get_book_by_id(id)