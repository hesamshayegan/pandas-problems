# stratascratch - medium

import pandas as pd

# separate launches by year
launches_2019 = car_launches[car_launches["year"] == 2019]
launches_2020 = car_launches[car_launches["year"] == 2020]

# merge on company_name, keep all companies, fill missing values with 0
merged_launches = pd.merge(
    launches_2019,
    launches_2020,
    on="company_name",
    how="outer",
    suffixes=("_2019", "_2020")
).fillna(0)

# keep only companies where product names differ between years
diff_launches = merged_launches[
    merged_launches["product_name_2019"] != merged_launches["product_name_2020"]
]

# count unique products per year for each company
company_counts = (
    diff_launches
    .groupby("company_name")
    .agg({
        "product_name_2019": "nunique",
        "product_name_2020": "nunique"
    })
    .reset_index()
)

# calculate net new products
company_counts["net_new_products"] = (
    company_counts["product_name_2020"] - company_counts["product_name_2019"]
)

# final result
result = company_counts[["company_name", "net_new_products"]]