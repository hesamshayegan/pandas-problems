# stratascratch - easy

import pandas as pd

employee.head()

avg_salary_dpt = (
    employee
        .groupby("department")["salary"]
        .mean()
        .reset_index(name="avg_salary_dpt")
    )
    
merged = pd.merge (
        employee,
        avg_salary_dpt,
        on="department",
        how="left"
    )
    
result = merged[["department", "first_name", "salary", "avg_salary_dpt"]]


# using transform

# employee['avg_salary'] = employee.groupby(['department'])['salary'].transform('mean')
# result = employee[['department', 'first_name', 'salary', 'avg_salary']]
# result = result.sort_values(by='department')


