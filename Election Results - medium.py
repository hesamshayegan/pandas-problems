# stratascratch - medium

import pandas as pd

voting_results.head()

df = voting_results

# count how many candidates each voter voted for
n_votes = (
    df
    .groupby("voter")
    .agg(n_candidates=("candidate", "count"))
    .reset_index()
)

# compute each voter’s fractional vote
n_votes["vote_weight"] = 1 / n_votes["n_candidates"]

# merge weight back to original df
merged = df.merge(n_votes, on="voter", how="left")

# sum vote weights per candidate
result = (
    merged
    .groupby("candidate")["vote_weight"]
    .sum()
    .reset_index()
    .sort_values("vote_weight", ascending=False)
)

result["candidate"].head(1)