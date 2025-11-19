from fastapi import APIRouter
from fastapi import HTTPException,status
from app.services.scraping_service import scraping_trigger

router = APIRouter(prefix="/scraping", tags=["Scraping"])

@router.get("/trigger")
def scraping_init():
    content=scraping_trigger("https://books.toscrape.com/")
    if content:
        return{"message":"Sucesso ao realizar o scrap dos livros!"}
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Falha ao realizar o web scrap dos livros!")
