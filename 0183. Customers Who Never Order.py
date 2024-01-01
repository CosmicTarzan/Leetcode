import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby("customerId", as_index=False).count()
    df = customers.merge(df, how='left', left_on='id', right_on='customerId')
    return df[df['id_y'].isnull()][['name']].rename(columns={'name': 'Customers'})
