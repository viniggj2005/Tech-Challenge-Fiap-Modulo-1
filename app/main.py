from fastapi import FastAPI
from app.models.book import Book
from app.services.db_service import engine, Base
from app.api.v1.routes import books, health, ml, scraping, categories, authentication, stats

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Tech Challenge Módulo 1", version="1.0.0", redoc_url=None)

app.include_router(ml.router, prefix="/api/v1")
app.include_router(stats.router, prefix="/api/v1")
app.include_router(books.router, prefix="/api/v1")
app.include_router(health.router, prefix="/api/v1")
app.include_router(scraping.router, prefix="/api/v1")
app.include_router(categories.router, prefix="/api/v1")
app.include_router(authentication.router, prefix="/api/v1")

from fastapi.openapi.docs import get_redoc_html

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="https://cdn.jsdelivr.net/npm/redoc@2.0.0-rc.55/bundles/redoc.standalone.js",
    )

# @app.get("/")
# def root():
#     return {"message": "API funcionando"}
