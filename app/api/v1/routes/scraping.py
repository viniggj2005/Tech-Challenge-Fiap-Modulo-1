from fastapi import APIRouter
from app.services.scraping_service import get_web_content,get_category_and_his_link,get_books,array_to_csv
router = APIRouter(prefix="/scraping", tags=["Scraping"])


@router.get("/init")
def scraping_init():
    content=get_web_content("https://books.toscrape.com/")
    categories=get_category_and_his_link(content)
    books=get_books(categories)
    array_to_csv(books)
    return content