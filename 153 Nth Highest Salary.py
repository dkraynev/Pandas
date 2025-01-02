import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee = employee[['salary']].drop_duplicates()
    employee = employee.sort_values(by='salary', ascending=False).reset_index()
    employee = employee[['salary']]
    if employee.shape[0] < N or N < 1:
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    employee.columns = [f'getNthHighestSalary({N})']
    return employee.loc[[N - 1]]