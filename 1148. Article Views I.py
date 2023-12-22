import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(views[views['viewer_id'] == views['author_id']]['author_id'].rename('id')).drop_duplicates().sort_values('id')
