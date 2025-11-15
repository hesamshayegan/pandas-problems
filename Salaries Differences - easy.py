# stratascratch - easy

import pandas as pd

db_employee.head()

merged = pd.merge(
            db_employee,
            db_dept,
            left_on='department_id',
            right_on='id',
            how='left'
            )

max_engineering = merged.loc[merged['department'] == 'engineering'].max()
max_marketing = merged.loc[merged['department'] == 'marketing'].max()

result = abs(max_engineering['salary'] - max_marketing['salary'])