import unicodedata


def transformacao(df_extraido):
    # Corrigir tipos de dados
    df_em_transformacao = df_extraido
    df_em_transformacao = df_em_transformacao.astype(
        {
            "show_id": "string",
            "title": "string",
            "type": "string",
            "release_year": "int",
            "genre": "string",
            "country": "string",
            "rating": "float",
            "duration_min": "int",
            "views_millions": "float",
        }
    )

    # Remover duplicidade
    df_em_transformacao = df_em_transformacao.drop_duplicates()

    # Padronizar textos
    colunas_texto = df_em_transformacao.select_dtypes(include=["string"]).columns

    for coluna in colunas_texto:
        df_em_transformacao[coluna] = (
            df_em_transformacao[coluna]
            .str.strip()  # Remove espaços
            .str.replace(r"\s+", " ", regex=True)  # Reduz espaços duplicados
            .str.lower()  # Padroniza maiusculas e minusculas
            .apply(
                lambda x: remover_acentos(x) if x is not None else x
            )  # Remove acentos
            .str.replace(
                r"[^a-zA-Z0-9\s]", "", regex=True
            )  # Remove caracteres especiais deixando apenas letras e números
        )

    df_transformado = df_em_transformacao

    return df_transformado


def remover_acentos(texto):
    return "".join(
        c
        for c in unicodedata.normalize("NFD", texto)
        if unicodedata.category(c) != "Mn"
    )
