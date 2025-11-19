import os
import pandas as pd
from typing import List
from app.schemas.book import BookModel
from fastapi import HTTPException, status


def get_csv_data():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    csv_path = os.path.join(data_dir, "data.csv")

    if not os.path.exists(csv_path):
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="O arquivo com os dados não foi encontrado, rode o trigger do webscraper por favor!",
        )

    return pd.read_csv(csv_path, sep=";")


def array_to_csv(books: List[BookModel]):
    try:
        base_dir = os.path.dirname(os.path.dirname(__file__))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)

        file_path = os.path.join(data_dir, "data.csv")
        df = pd.DataFrame(books)

        df.to_csv(file_path, index=False, sep=";")
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro ao salvar arquivo csv. erro:{str(e)}",
        )
