import os
import sqlite3
import pandas as pd

def create_dataframe(in_path):
    if not os.path.exists(in_path):
        raise ValueError("Sorry, the path {} does not exist".format(in_path))
    conn = sqlite3.connect(in_path)
    df = pd.read_sql_query("select category_id, video_id, 'us' as language from USvideos UNION select category_id, video_id, 'ca' as language from CAvideos UNION select category_id, video_id, 'de' as language from DEvideos UNION select category_id, video_id, 'fr' as language from FRvideos UNION select category_id, video_id, 'gb' as language from GBvideos;", conn)
    conn.close()
    return df
