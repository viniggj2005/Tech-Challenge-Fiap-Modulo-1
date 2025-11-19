from fastapi import Query
from fastapi import APIRouter
from app.services.books_service import get_books,get_book_by_id,get_books_by_search
router = APIRouter(prefix="/books", tags=["Books"])

@router.get("/")
def list_books():
    return get_books()

@router.get("/search")
def list_books(title: str | None = Query(None),
    category: str | None = Query(None)):
    print(title)
    return get_books_by_search(title,category)

@router.get("/{id}")
def list_books(id:int):
    return get_book_by_id(id)

