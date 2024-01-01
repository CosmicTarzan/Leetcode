import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    df = person.groupby("email", as_index=False).count()
    return df[df['id'] > 1][['email']]
