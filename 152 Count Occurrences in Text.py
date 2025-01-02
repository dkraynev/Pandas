import pandas as pd

def count_occurrences(files: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame({
        'word': ['bull', 'bear'],
        'count': [
            files['content'].str.contains(' bull ').sum(),
            files['content'].str.contains(' bear ').sum()
            ]
    })