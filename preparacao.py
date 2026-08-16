import pandas as pd


# ============================================================
# AJUSTE DE PERCENTUAIS
# ============================================================

def ajustar_percentuais_100(df, coluna="percent", casas=1):
    df = df.copy()

    # Arredonda os percentuais
    df[coluna] = df[coluna].round(casas)

    # Calcula a diferença para 100
    diferenca = round(100 - df[coluna].sum(), casas)

    # Se não somar 100, ajusta a maior categoria
    if diferenca != 0:
        indice = df[coluna].idxmax()

        df.loc[indice, coluna] = round(
            df.loc[indice, coluna] + diferenca,
            casas
        )

    return df


# ============================================================
# JULHO — 16ª EDIÇÃO
# ============================================================

def carregar_dados(
    arquivo="Respostas_16ed.xlsx"
):
    """
    Carrega, renomeia, filtra e padroniza
    os dados da pesquisa de julho de 2026.
    """

    # --------------------------------------------------------
    # 1. Leitura das respostas
    # --------------------------------------------------------

    df = pd.read_excel(arquivo)

    # --------------------------------------------------------
    # 2. Leitura do dicionário de colunas
    # --------------------------------------------------------

    colunas = pd.read_excel(
        arquivo,
        sheet_name=1
    )

    dicionario = dict(
        zip(
            colunas["nome_original"],
            colunas["novo_nome"]
        )
    )

    # --------------------------------------------------------
    # 3. Renomear colunas
    # --------------------------------------------------------

    df = df.rename(
        columns=dicionario
    )

    # ============================================================
    # CORREÇÕES ESPECÍFICAS DA 16ª EDIÇÃO
    # ============================================================

    for coluna in df.columns:

        if "importância" in str(coluna).lower() and \
        "economia solidária" in str(coluna).lower():

            df = df.rename(
                columns={
                    coluna: "importancia_apoio_economia_solidaria"
                }
            )

    # --------------------------------------------------------
    # 4. Manter somente moradores do Rio
    # --------------------------------------------------------

    df = df[
        df["mora_na_cidade_rj"].astype(str).str.strip() == "Sim"
    ].copy()

    # --------------------------------------------------------
    # 5. Padronizar respostas
    # --------------------------------------------------------

    replacing = {
        "Ótima": "Ótimo",
        "Boa": "Bom",
        "Péssima": "Péssimo",
        "Não concordo nem discordo":
            "Não concordo, nem discordo"
    }

    df.replace(
        replacing,
        inplace=True
    )

    return df


# ============================================================
# MARÇO — 15ª EDIÇÃO
# ============================================================

def carregar_dados_marco(
    arquivo="Respostas_15ed.xlsx"
):
    """
    Carrega, renomeia, filtra e padroniza
    os dados da pesquisa de março de 2026.
    """

    # --------------------------------------------------------
    # 1. Leitura das respostas
    # --------------------------------------------------------

    df = pd.read_excel(arquivo)

    # --------------------------------------------------------
    # 2. Leitura do dicionário de colunas
    # --------------------------------------------------------

    colunas = pd.read_excel(
        arquivo,
        sheet_name=1
    )

    dicionario = dict(
        zip(
            colunas["nome_original"],
            colunas["novo_nome"]
        )
    )

    # --------------------------------------------------------
    # 3. Renomear colunas pelo dicionário
    # --------------------------------------------------------

    df = df.rename(
        columns=dicionario
    )

    # --------------------------------------------------------
    # 4. CORREÇÕES ESPECÍFICAS DA 15ª EDIÇÃO
    # --------------------------------------------------------

    coluna_educacao = None

    for coluna in df.columns:

        texto = str(coluna).lower()

        if (
            "ex prefeito eduardo paes" in texto
            and "gestão da" in texto
            and "educação" in texto
        ):
            coluna_educacao = coluna
            break

    if coluna_educacao is not None:

        df = df.rename(
            columns={
                coluna_educacao: "avaliacao_educacao"
            }
        )

    # --------------------------------------------------------
    # 5. Garantir também os nomes utilizados pelo dashboard
    # --------------------------------------------------------

    # Avaliação geral de Eduardo Paes
    if "avaliacao_governo_paes" in df.columns:
        df["avaliacao_governo_paes"] = df[
            "avaliacao_governo_paes"
        ]

    # Avaliação pessoal de Eduardo Paes
    if "avaliacao_pessoa_eduardo_paes" in df.columns:
        df["avaliacao_pessoa_eduardo_paes"] = df[
            "avaliacao_pessoa_eduardo_paes"
        ]

    # --------------------------------------------------------
    # 6. Manter somente moradores do Rio
    # --------------------------------------------------------

    df = df[
        df["mora_na_cidade_rj"].astype(str).str.strip() == "Sim"
    ].copy()

    # --------------------------------------------------------
    # 7. Padronizar respostas
    # --------------------------------------------------------

    replacing = {
        "Ótima": "Ótimo",
        "Boa": "Bom",
        "Péssima": "Péssimo",
        "Não concordo nem discordo":
            "Não concordo, nem discordo"
    }

    df.replace(
        replacing,
        inplace=True
    )

    return df