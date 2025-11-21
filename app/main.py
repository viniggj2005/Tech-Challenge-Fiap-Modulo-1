from fastapi import FastAPI
from app.api.v1.routes import books, health, scraping, categories, authentication

app = FastAPI(title="Tech Challenge Módulo 1", version="1.0.0")

app.include_router(books.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")
app.include_router(scraping.router, prefix="/api/v1")
app.include_router(categories.router, prefix="/api/v1")
app.include_router(authentication.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "API funcionando"}
