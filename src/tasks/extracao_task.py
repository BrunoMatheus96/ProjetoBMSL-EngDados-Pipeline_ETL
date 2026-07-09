import pandas as pd

def extracao():
    df = pd.read_csv("data/csv/netflix_dataset.csv")
    df_extraido = df.copy()
    return df_extraido