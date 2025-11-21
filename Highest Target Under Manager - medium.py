# stratascratch - medium

import pandas as pd

df = salesforce_employees

team = df[df["manager_id"] == 13]

team["rank"] = team["target"].rank(method="dense", ascending=False)

top_performers = team.loc[team["rank"] == 1, ["first_name", "target"]]
