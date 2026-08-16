
import pandas as pd
import ponderacao as p


def calcular_ponderacoes(df):
    """
    Calcula os pesos da amostra e as porcentagens
    ponderadas da pesquisa.
    """

    amostra = p.getPesos(df)

    ponderacoes = {}

    for coluna in df.columns:
        ponderacoes[coluna] = p.getPercents(
            amostra,
            [coluna, "peso"]
        )

    return amostra, ponderacoes


def calcular_ponderacoes_marco(df):
    """
    Calcula os pesos da amostra e as porcentagens
    ponderadas da pesquisa de março (15ª edição).
    """

    amostra = p.getPesos(df)

    ponderacoes = {}

    for coluna in df.columns:
        ponderacoes[coluna] = p.getPercents(
            amostra,
            [coluna, "peso"]
        )

    return amostra, ponderacoes

