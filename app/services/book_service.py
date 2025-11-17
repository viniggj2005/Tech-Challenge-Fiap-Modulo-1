import pandas as pd
import os

def get_books():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    csv_path = os.path.join(data_dir, "data.csv")

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}")

    data = pd.read_csv(csv_path,sep=";")
    data=data[["id","title"]]
    return data.to_dict(orient="records")

def get_book_by_id(id:int):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(base_dir, "data")
    csv_path = os.path.join(data_dir, "data.csv")

    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"Arquivo não encontrado: {csv_path}")
    print("id antes")
    data = pd.read_csv(csv_path,sep=";")
    data=data[data["id"]==id]
    return data.to_dict(orient="records")