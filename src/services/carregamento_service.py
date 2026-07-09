from src.auth.bigquery_auth import get_bigquery_client
from src.config.env import TABLE_ID


def carregar_data_frame(df):

    client = get_bigquery_client()

    job = client.load_table_from_dataframe(df, TABLE_ID)

    job.result()

    print("Dados carregados no BigQuery")

    return True
