from app.services.data_service import get_csv_data


def categories_stats():
    data=get_csv_data()
    stats = (
    data.groupby("category")
    .agg(
        mean_price=("price", "mean"),
        total_items=("price", "count")
    )
    .round(2)
    .reset_index()
    .to_dict(orient="records")
)
    return stats


def dataset_stats():
    data = get_csv_data()

    stats = {
        "mean_price": float(round(data["price"].mean(), 2)),
        "total_items": int(data["price"].count()),
        "ratings_distribution": {
            int(key): int(value)
            for key, value in data["rate"].value_counts().sort_index().to_dict().items()
        },
    }

    return stats
