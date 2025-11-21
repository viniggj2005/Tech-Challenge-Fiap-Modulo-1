from fastapi import Query
from fastapi import APIRouter
from app.services.books_service import get_books, get_book_by_id, get_books_by_price_range, get_books_by_search, get_top_rated_books

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/")
def list_all_books():
    return get_books()


@router.get("/search")
def list_books_by_search(title: str | None = Query(None), category: str | None = Query(None)):
    return get_books_by_search(title, category)

@router.get("/top-rated/{amount}")
def call_get_top_rated_books(amount:int):
    return get_top_rated_books(amount)

@router.get("/price-range")
def call_get_top_rated_books(min: float, max: float):
    return get_books_by_price_range(min, max)

@router.get("/{id}")
def list_book_by_id(id: int):
    return get_book_by_id(id)