# stratascratch - easy

import pandas as pd

amazon_shipment.head()

amazon_shipment["year_month"] = amazon_shipment["shipment_date"].dt.to_period("M")
amazon_shipment["unique_key"] = amazon_shipment["shipment_id"].astype(str) + amazon_shipment["sub_id"].astype(str)

monthly_counts = (
    amazon_shipment
        .groupby("year_month")["unique_key"]
        .count()
        .reset_index(name="count")
    )

# groupby("year_month") creates a GroupBy object (a “recipe” for grouping),
# ["unique_key"] selects the column,
# but no aggregation (like count or sum) has been applied yet.

# reset_index converts the Series into a proper DataFrame.