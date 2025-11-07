from fastapi import FastAPI
from app.api.v1.routes import books,scraping

app = FastAPI(title="Tech Challenge Módulo 1", version="1.0.0")

app.include_router(books.router)
app.include_router(scraping.router)

@app.get("/")
def root():
    return {"message": "API funcionando"}
