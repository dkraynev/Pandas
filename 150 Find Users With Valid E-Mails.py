import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users['mail'].str.contains(r'^[a-zA-Z][a-zA-Z0-9._-]*@leetcode\.com$')]