# stratascratch - medium

import pandas as pd

df = premium_accounts_by_day[premium_accounts_by_day["final_price"] > 0].copy()

df["date_plus_7d"] = df["entry_date"] + pd.DateOffset(7)

# shows all customers whose entry_date is exactly 7 days after their first entry.
# if a user came back exactly 7 days later → I get a match.
merged_df = pd.merge(
    df,
    df,
    how="left",
    left_on=["account_id", "date_plus_7d"],
    right_on=["account_id", "entry_date"],
    suffixes=("_left", "_right")
)

result = (
    merged_df.groupby("entry_date_left")
    .agg(
        # counts unique customers who paid on that entry date.
        premium_paid_accounts=("account_id", "nunique"),
        # Counts how many of those customers were still premium after 7 days,
        # by checking how many matches exist in the right side of the merge (notna() means active after 7 days).
        premium_paid_accounts_after_7d=("entry_date_right", lambda x: x.notna().sum())
    )
    .reset_index()
    .rename(columns={"entry_date_left": "entry_date"})
    .sort_values("entry_date")
    .head(7)
)