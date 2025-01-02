import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    max_salaries = employee.groupby('departmentId')['salary'].transform('max')
    employee = employee[employee['salary'] == max_salaries]
    employee = pd.merge(
        employee,
        department,
        left_on = 'departmentId',
        right_on = 'id',
        how = 'inner'
    )
    employee = employee[['name_y', 'name_x', 'salary']]
    employee.columns = ['Department', 'Employee', 'Salary']

    return employee