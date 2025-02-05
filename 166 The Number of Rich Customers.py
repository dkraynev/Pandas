import pandas as pd

def count_rich_customers(store: pd.DataFrame) -> pd.DataFrame:
    result = store[store['amount'] > 500].drop_duplicates(subset='customer_id')
    count = result.shape[0]
    result = pd.DataFrame({'rich_count': [count]})
    return result