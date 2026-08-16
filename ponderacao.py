import pandas as pd

def getPesos(df):
    """
    Calcula os pesos de cada combinação de sexo, raça e idade.
    """
    
    # lemos os dados da população carioca
    populacao_percent = pd.read_csv("populacao_percent_2022.csv")
    
    # contamos as ocorrências de cada combinação de sexo, cor/raça e idade na amostra
    amostra = df.groupby(["sexo", "raca", "idade"]).size().reset_index(name="freq")
    
    # calculamos o percentual de cada combinação na amostra
    amostra["amostra_percent"] = amostra["freq"] / amostra["freq"].sum()
    
    # juntamos os dados da população com os da amostra
    full_df = amostra.merge(populacao_percent, on=["sexo", "raca", "idade"], how="left")
    
    # calculamos a ponderação
    full_df["peso"] = full_df["pop_percent"] / full_df["amostra_percent"]
    
    # adicionamos uma pequena constante de 0.001 aos pesos iguais a zero
    full_df.loc[full_df["peso"] == 0, "peso"] = 0.001
    
    # pegamos os pesos de cada combinação
    pesos = full_df[["sexo", "raca", "idade", "peso"]]
    
    # juntamos os dados da amostra com os pesos
    df = df.merge(pesos, on=["sexo", "raca", "idade"], how="left")
    
    return df

########################################################################################################################
########################################################################################################################
########################################################################################################################

def getPercents(df, colunas):
    """
    Pondera os dados da amostra.
    A lista de colunas deve ser da forma:
    
    Caso 1: ["variável1", "peso"]
    Caso 2: ["variável1", "variável2", "peso"]
    
    É importante lembrar que, no caso 2, a variável 1 deve ser 
    a variável socioeconômica.
    """
    
    grouped = df.groupby(colunas)[colunas[0]].count().reset_index(name="freq")
        
    # calculamos a ponderação
    grouped["freq_ponderada"] = grouped["freq"] * grouped["peso"]
        
    if len(colunas) == 2:
        # somamos as frequências ponderadas para cada categoria de colunas[0]
        grouped = grouped.groupby(colunas[0])["freq_ponderada"].sum().reset_index()
        
        # calculamos a proporção de cada categoria
        grouped["percent"] = (grouped["freq_ponderada"] / grouped["freq_ponderada"].sum()) * 100
    
    elif len(colunas) == 3:
        # somamos as frequências ponderadas para cada combinação de colunas[0] e colunas[1]
        grouped = grouped.groupby([colunas[0], colunas[1]])["freq_ponderada"].sum().reset_index()
        
        # calculamos o total para cada categoria de colunas[0]
        total_col0 = grouped.groupby(colunas[0])["freq_ponderada"].sum().reset_index(name="total")
        
        # juntamos o total com os dados ponderados
        grouped = grouped.merge(total_col0, on=colunas[0], how="left")
        
        # calculamos a proporção de cada combinação
        grouped["percent"] = (grouped["freq_ponderada"] / grouped["total"]) * 100
        
    return grouped