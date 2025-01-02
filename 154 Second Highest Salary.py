import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee[['salary']].drop_duplicates()
    employee = employee.sort_values(by='salary', ascending=False).reset_index()
    employee = employee[['salary']]
    if employee.shape[0] < 2:
        return pd.DataFrame({'SecondHighestSalary': [None]})
    employee.columns=['SecondHighestSalary']
    return employee.loc[[1]]