import pandas as pd

def extracao():
    df_extraido = pd.read_csv("data/csv/netflix_dataset.csv")
    print(df_extraido.head())