# stratascratch - easy

import pandas as pd

sf_restaurant_health_violations.head()

df = sf_restaurant_health_violations

roxanne = df[df["business_name"] == "Roxanne Cafe"]

roxanne["inspection_date"] = pd.to_datetime(roxanne["inspection_date"]).dt.year

roxanne.dropna(subset=["business_name"], inplace=True)

roxanne_viloation = (
    roxanne
    .groupby("inspection_date")["violation_id"]
    .count()
    .reset_index(name="violations_count")
    )