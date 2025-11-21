import io
from fastapi import APIRouter, Response
from app.services.data_service import get_csv_data
from app.services.ml_service import get_data_for_features

router = APIRouter(prefix="/ml", tags=["Machine Learning"])


@router.get("/features")
def get_feature():
    return get_data_for_features()

@router.get("/training-data")
def training_data():
    df = get_csv_data()
    csv_content = df.to_csv(index=False)

    return Response(
        content=csv_content,
        media_type="text/csv",
        headers={
            "Content-Disposition": "attachment; filename=training-data.csv"
        }
    )

@router.post("/predictions")
def get_feature():
    return{"message":"endpoint para receber predições."}