from fastapi import APIRouter
from fastapi import HTTPException, status

from app.services.stats_service import categories_stats, dataset_stats


router = APIRouter(prefix="/stats", tags=["Stats"])


@router.get("/categories")
def get_categories_stats():
    return categories_stats()

@router.get("/overview")
def get_overview_stats():
    return dataset_stats()