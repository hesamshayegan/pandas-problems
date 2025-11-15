# stratascratch - easy

import pandas as pd

ms_employee_salary.head()

ms_employee_salary['rn'] = (
    ms_employee_salary
        .sort_values(by=['salary', 'department_id'], ascending=False)
        .groupby('id')
        .cumcount() + 1
)

ms_employee_salary.loc[ms_employee_salary['rn'] == 1, ['id', 'first_name', 'last_name', 'department_id', 'salary']]

# result = ms_employee_salary[ms_employee_salary['rn'] == 1].drop(columns='rn')


# .groupby() and .cumcount() simulates ROW_NUMBER() behavior.