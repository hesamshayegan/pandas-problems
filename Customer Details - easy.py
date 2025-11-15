# stratascratch - easy

import pandas as pd

customers.head()

merged = pd.merge(
    customers,
    orders,
    left_on="id",
    right_on="cust_id",
    how="left"
    )
    
result = (
        merged[["first_name", "last_name", "city", "order_details"]]
        .sort_values(by=["first_name", "order_details"], ascending=True)
       )