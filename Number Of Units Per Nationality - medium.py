# stratascratch - medium

import pandas as pd

# hosts under 30
hosts_u30 = airbnb_hosts.loc[airbnb_hosts["age"] < 30, ["host_id", "nationality"]]

# apartment listings only
apts = airbnb_units.loc[airbnb_units["unit_type"] == "Apartment", ["host_id", "unit_id"]]

# merge on host_id
merged_hosts = pd.merge(hosts_u30, apts, on="host_id")

# count unique apartments per nationality
result = (
    merged_hosts
    .groupby("nationality")["unit_id"]
    .nunique()
    .reset_index(name="n_apartments")
)

result.sort_values("n_apartments", ascending=False)
