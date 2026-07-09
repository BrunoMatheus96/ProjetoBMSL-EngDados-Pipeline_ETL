
from src.services.carregamento_service import carregar_data_frame
from src.tasks.carregamento_task import carregamento
from src.tasks.transformacao_task import transformacao
from src.tasks.extracao_task import extracao


def pipeline_ETL():
    df = extracao()
    df = transformacao(df)
    df = carregamento(df)
    carregar_data_frame(df)
