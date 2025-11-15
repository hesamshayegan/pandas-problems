# stratascratch - easy

import pandas as pd

worker.head()

merged = pd.merge(
        worker,
        title,
        left_on="worker_id",
        right_on="worker_ref_id",
        how="inner"
        )
        
# max_salary = merged[
#     merged["salary"] == merged["salary"].max()
# ][["worker_title"]]

# how="left" -> Keeps all workers from worker, even those without a matching title.
# how="inner" -> Keeps only workers who have a matching title.

max_sal = merged['salary'].max()
max_salary_titles = merged.loc[merged['salary'] == max_sal, 'worker_title']