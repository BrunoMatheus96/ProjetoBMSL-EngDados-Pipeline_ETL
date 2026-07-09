from google.cloud import bigquery
from google.oauth2 import service_account

from src.config.env import CREDENTIALS_PATH, PROJECT_ID


def get_bigquery_client():

    credentials = service_account.Credentials.from_service_account_file(
        CREDENTIALS_PATH
    )

    client = bigquery.Client(
        credentials=credentials,
        project=PROJECT_ID
    )

    return client