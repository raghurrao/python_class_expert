import sqlite3
import pandas as pd

def query_department_salaries(db_path: str) -> pd.DataFrame:
    """
    Query an SQLite database at db_path containing a table 'employees'
    with columns 'department' and 'salary'.
    
    Run an SQL query that returns:
    - 'department'
    - 'average_salary' (average of salary grouped by department)
    
    Return the result as a Pandas DataFrame.
    """
    # TODO: Implement your solution here
    pass
