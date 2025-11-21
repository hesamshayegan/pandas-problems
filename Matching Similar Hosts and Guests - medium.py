# stratascratch - medium

import pandas as pd

airbnb_hosts.head()

hosts_unique = airbnb_hosts[["nationality", "gender", "host_id"]].drop_duplicates()
guests_unique = airbnb_guests[["nationality", "gender", "guest_id"]].drop_duplicates()

result = pd.merge(
    hosts_unique,
    guests_unique,
    on=["nationality", "gender"]
    )

result = result[["host_id", "guest_id"]]