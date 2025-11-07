from fastapi import APIRouter

router = APIRouter(prefix="/books", tags=["Books"])


@router.get("/")
def list_books():
    return [{"id": 1, "name": "Alice"}, {"id": 2, "name": "Bob"}]