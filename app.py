import streamlit as st
import plotly.graph_objects as go

from preparacao import (
    carregar_dados,
    carregar_dados_marco,
    ajustar_percentuais_100
)

from processamento import (
    calcular_ponderacoes,
    calcular_ponderacoes_marco
)

from graficos import (
    grafico_sexo,
    grafico_idade,
    grafico_raca,
    grafico_ocupacao,
    grafico_renda_sm,
    grafico_barra_horizontal,
    grafico_avaliacao_interativo,
    grafico_fator_interativo,
    grafico_concordancia_interativo,
    grafico_economia_solidaria_interativo,
    grafico_concordancia_economia_interativo,
    grafico_escala_interativo
)

from estilo import (
    aplicar_estilo,
    mostrar_logo_sidebar
)

# CONFIGURAÇÃO

st.set_page_config(page_title="Pesquisa de Opinião — Rio21", page_icon="📊", layout="wide", initial_sidebar_state="expanded")

aplicar_estilo()

def ajustar_ponderacoes(ponderacoes):
    if not isinstance(ponderacoes, dict):
        return ponderacoes
    ponderacoes_ajustadas = {}
    for chave, resultado in ponderacoes.items():
        if hasattr(resultado, "columns") and "percent" in resultado.columns:
            resultado = ajustar_percentuais_100(resultado, coluna="percent", casas=1)
        ponderacoes_ajustadas[chave] = resultado
    return ponderacoes_ajustadas

def mostrar_grafico(fig, altura=None):
    if fig is None:
        return
    fig.update_layout(margin=dict(l=30, r=40, t=35, b=80), autosize=True)
    try:
        fig.update_xaxes(automargin=True)
    except Exception:
        pass
    try:
        fig.update_yaxes(automargin=True)
    except Exception:
        pass
    try:
        fig.update_layout(legend=dict(orientation="h", yanchor="bottom", y=-0.25, xanchor="center", x=0.5))
    except Exception:
        pass
    if altura is not None:
        fig.update_layout(height=altura)
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False, "responsive": True})

def titulo_pergunta(texto):
    st.markdown(
        f"""
        <div style="
            font-size:1.35rem;
            font-weight:750;
            color:#20252A;
            margin-top:1.5rem;
            margin-bottom:0.8rem;
            line-height:1.35;
        ">
            {texto}
        </div>
        """,
        unsafe_allow_html=True
    )

def titulo_periodo(texto):
    st.markdown(
        f"""
        <div style="
            font-size:24px;
            font-weight:800;
            color:#687078;
            text-transform:uppercase;
            letter-spacing:0.08em;
            margin-bottom:0.25rem;
        ">
            {texto}
        </div>
        """,
        unsafe_allow_html=True
    )
# ============================================================
# DADOS — JULHO
# ============================================================

df_julho_2026 = carregar_dados()

amostra_julho_2026, ponderacoes_julho_2026 = calcular_ponderacoes(
    df_julho_2026
)

ponderacoes_julho_2026 = ajustar_ponderacoes(
    ponderacoes_julho_2026
)


# ============================================================
# ECONOMIA SOLIDÁRIA
# ============================================================

ponderacoes_economia_2026 = ponderacoes_julho_2026

if isinstance(ponderacoes_economia_2026, dict):

    if "prioridade_fortalecer_economia_solidaria" in ponderacoes_economia_2026:

        ponderacoes_economia_2026[
            "prioridade_fortalecer_economia_solidaria"] = ponderacoes_economia_2026["prioridade_fortalecer_economia_solidaria"].replace(
            {"Facilitar o acesso a crédito e financiamentoão 4Facilitar o acesso a crédito e financiamento":"Facilitar o acesso a crédito e financiamento",
             "Incentivar compras públicas de empreendimentos solidáriosIncentivar compras públicas de empreendimentos solidários": 
             "Incentivar compras públicas de empreendimentos solidários"})

    if "ouviu_falar_economia_solidaria" in ponderacoes_economia_2026:

        ponderacoes_economia_2026[
            "ouviu_falar_economia_solidaria"] = ponderacoes_economia_2026[
            "ouviu_falar_economia_solidaria"].replace({"Apenas ouvi fakar":"Apenas ouviu falar"})


# ============================================================
# MARÇO — 15ª EDIÇÃO
# ============================================================

df_marco_2026 = carregar_dados_marco()

amostra_marco_2026, ponderacoes_marco_2026 = calcular_ponderacoes_marco(df_marco_2026)

ponderacoes_marco_2026 = ajustar_ponderacoes(ponderacoes_marco_2026)


# SIDEBAR

with st.sidebar:

    mostrar_logo_sidebar()

    st.markdown(
        """
        <div style="
            color:#55A6D9;
            font-size:20px;
            font-weight:800;
            letter-spacing:0.10em;
            text-transform:uppercase;
            margin-bottom:1.8rem;
            line-height:1.5;
            white-space:normal;
        ">
            RIO21 · PESQUISA DE OPINIÃO
        </div>
        """,
        unsafe_allow_html=True
    )

    pagina = st.radio(
        "Navegação",
        [
            "Visão geral",
            "Gestão municipal",
            "Percepções e expectativas",
            "Economia Solidária",
            "Perfil da amostra"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    st.caption(
        "Pesquisa Rio21 · 16ª edição"
    )

# ============================================================
# VISÃO GERAL
# ============================================================

if pagina == "Visão geral":

    # ========================================================
    # CABEÇALHO
    # ========================================================

    st.title("Avaliação da Gestão Municipal do Rio de Janeiro")

    st.subheader("O que pensa a população carioca sobre os governos, "
        "os serviços públicos e o futuro da cidade.")

    st.write("**16ª edição · Julho de 2026**  ·  ")

    st.divider()


    # ========================================================
    # PESQUISA EM NÚMEROS
    # ========================================================


    st.markdown(
        """
        <div style="
            color:#55A6D9;
            font-size:0px;
            font-weight:800;
            letter-spacing:0.10em;
            text-transform:uppercase;
            margin-top:1rem;
            margin-bottom:0.8rem;
        ">
            A PESQUISA EM NÚMEROS
        </div>
        """,
        unsafe_allow_html=True
    )
    

    st.header("Principais informações")

    st.markdown("""
            <div style = "font-size:24px">
                        Dados básicos desta edição do levantamento.
                        </div>""", unsafe_allow_html = True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Entrevistas",
            value="593",
            delta="respondentes",
            delta_color="off"
        )

    with col2:
        st.metric(
            label="Variáveis",
            value="43",
            delta="questões e indicadores analisados",
            delta_color="off"
        )

    with col3:
        st.metric(
            label="Ponderação",
            value="Censo 2022",
            delta="referência para a população carioca",
            delta_color="off"
        )


    st.divider()


    # ========================================================
    # SOBRE A PESQUISA
    # ========================================================

    st.markdown(
    """
    <div style="
        color:#55A6D9;
        font-size:30px;
        font-weight:750;
        line-height:1.25;
        margin-top:1.5rem;
        margin-bottom:1rem;
    ">
        SOBRE A PESQUISA
    </div>
    """,
    unsafe_allow_html=True)
    st.header("Objetivo do levantamento")

    with st.container(border=True):

        st.markdown("""
        <div style = "font-size:24px">
                    A pesquisa busca compreender a percepção da população 
                    carioca sobre as ações do Governo Municipal, os serviços 
                    públicos, as condições da cidade e as expectativas para 
                    os próximos meses.
                    </div>""", unsafe_allow_html = True)

        st.markdown("""
                <div style = "font-size:24px">
                            O levantamento integra a série de pesquisas de opinião 
                            pública realizadas pelo Rio21 e permite acompanhar 
                            mudanças nas percepções dos cariocas ao longo do tempo.
                            </div>""", unsafe_allow_html = True)
        

    st.divider()


    # ========================================================
    # INFORMAÇÕES DO LEVANTAMENTO
    # ========================================================

    st.markdown(
    """
    <div style="
        color:#55A6D9;
        font-size:30px;
        font-weight:800;
        letter-spacing:0.10em;
        text-transform:uppercase;
        margin-top:1.5rem;
        margin-bottom:0.8rem;
    ">
        INFORMAÇÕES DO LEVANTAMENTO
    </div>
    """,
    unsafe_allow_html=True
)

    st.header("Dados básicos da pesquisa")

    

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("Período de coleta")

            st.markdown("""
                    <div style = "font-size:24px">
                                 Questionário aplicado online entre 
                                21 de julho e 4 de agosto de 2026.
                                </div>""", unsafe_allow_html = True)
            

          
    with col2:

        with st.container(border=True):

            st.subheader("Amostra")

            st.markdown("""<div style = "font-size:24px">
                        Amostra não probabilística composta por 593 respondentes.
                        </div>""", unsafe_allow_html = True)



    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("Ponderação")

            st.markdown("""<div style = "font-size:24px">
                        Os dados foram ponderados segundo sexo, cor/raça 
                        e faixa etária, utilizando como referência a
                        composição da população carioca segundo o Censo 2022.
                                    </div>""", unsafe_allow_html = True)

    with col2:

        with st.container(border=True):

            st.subheader("Comparação entre edições")

            st.markdown("""<div style = "font-size:24px">
                                    As análises comparativas utilizam os dados da 
                                    15ª edição, realizada em março de 2026, e da 
                                    16ª edição, realizada em julho de 2026.
                                                </div>""", unsafe_allow_html = True)


    st.divider()


    # ========================================================
    # O QUE A PESQUISA ANALISA
    # ========================================================


    st.markdown(
    """
    <div style="
        color:#55A6D9;
        font-size:30px;
        font-weight:800;
        letter-spacing:0.10em;
        text-transform:uppercase;
        margin-top:1.5rem;
        margin-bottom:0.8rem;
    ">
        CONTEÚDO DA PESQUISA
    </div>
    """,
    unsafe_allow_html=True
)

    st.header("O que a pesquisa analisa")

    st.markdown("""<div style = "font-size:24px">
                O questionário reúne diferentes dimensões da percepção 
                dos cariocas sobre a cidade e seus governos.
                                                    </div>""", unsafe_allow_html = True)

    # ========================================================
    # ÁREAS ANALISADAS
    # ========================================================

    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("Gestão pública")

            st.markdown("""<div style = "font-size:20px">
                            Avaliação dos governos municipal e estadual, 
                            além de aspectos relacionados à saúde, educação, 
                            transportes, assistência social, preservação 
                            ambiental e conservação urbana e patrimonial.
                                                                </div>""", unsafe_allow_html = True)


    with col2:

        with st.container(border=True):

            st.subheader("Percepções e expectativas")

            st.markdown("""<div style = "font-size:20px">
                            Preocupações recentes, orgulho de ser carioca, 
                            expectativas para os próximos meses e percepção 
                            de representação política.
                                                                </div>""", unsafe_allow_html = True)


    col1, col2 = st.columns(2)

    with col1:

        with st.container(border=True):

            st.subheader("Economia Solidária")

            st.markdown("""<div style = "font-size:20px">
                                        Conhecimento, importância atribuída ao tema, 
                                        prioridades e concordância com afirmações
                                        relacionadas à Economia Solidária.
                                                                            </div>""", unsafe_allow_html = True)


    with col2:

        with st.container(border=True):

            st.subheader("Perfil da amostra")

            st.markdown("""<div style = "font-size:20px">
                                                    Características sociodemográficas e 
                                                    socioeconômicas dos respondentes, considerando 
                                                    os dados ponderados.
                                                                                        </div>""", unsafe_allow_html = True)


    # ========================================================
    # FONTE
    # ========================================================

    st.divider()

    st.caption(
        "Fonte: Pesquisa Rio21 — 16ª edição, julho de 2026. "
        "Dados ponderados por sexo, cor/raça e faixa etária, "
        "com base no Censo 2022."
    )

# ============================================================
# GESTÃO MUNICIPAL
# ============================================================

elif pagina == "Gestão municipal":

    st.title("Avaliação da Prefeitura")

    st.subheader("Comparação entre a percepção dos cariocas sobre o Governo Eduardo Paes e o Governo Eduardo Cavaliere.")

    st.markdown(
            """
            <div style="
                color:#55A6D9;
                font-size:30px;
                font-weight:800;
                letter-spacing:0.10em;
                text-transform:uppercase;
                margin-top:1rem;
                margin-bottom:0.8rem;
            ">
                Avaliação dos governos 
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("## Governo Municipal")

    col1, col2 = st.columns(2)

    with col1:
        mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_marco_2026, "avaliacao_governo_paes", "Março de 2026 — Governo Municipal"))

    with col2:
        mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_julho_2026, "avaliacao_governo_cavaliere", "Julho de 2026 — Governo Municipal"))

    st.divider()

    st.markdown("## Saúde")

    col1, col2 = st.columns(2)

    with col1:
        mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_marco_2026,"avaliacao_saude", "Março de 2026 "))

    with col2:
        mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_julho_2026,"avaliacao_saude","Julho de 2026"))

    st.divider()

    st.markdown("## Transportes")

    col1, col2 = st.columns(2)

    with col1:
        mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_marco_2026,"avaliacao_transportes", "Março de 2026 "))

    with col2:
        mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_julho_2026,"avaliacao_transportes", "Julho de 2026 "))

    st.divider()

    st.markdown("## Conservação urbana e patrimonial")

    col1, col2 = st.columns(2)

    with col1:
        mostrar_grafico(
            grafico_avaliacao_interativo(ponderacoes_marco_2026,"avaliacao_conservacao_urbana_patrimonial","Março de 2026"))

    with col2:
        mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_julho_2026,"avaliacao_conservacao_urbana_patrimonial","Julho de 2026"))

    st.divider()

    st.markdown("## Preservação ambiental")
    
    col1, col2 = st.columns(2)
    
    with col1:
            mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_marco_2026,"avaliacao_preservacao_ambiental","Março de 2026"))
    
    with col2:
            mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_julho_2026,"avaliacao_preservacao_ambiental","Julho de 2026"))
                

    st.markdown("## Assistência social")

    col1, col2 = st.columns(2)

    with col1:
        mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_marco_2026,"avaliacao_assistencia_social","Março de 2026"))
            

    with col2:
        mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_julho_2026,"avaliacao_assistencia_social","Julho de 2026"))

    st.divider()
        
    st.markdown("## Educação")
    
    col1, col2 = st.columns(2)
    
    with col1:
            mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_marco_2026,"avaliacao_educacao","Março de 2026"))
    
    with col2:
            mostrar_grafico(grafico_avaliacao_interativo(ponderacoes_julho_2026,"avaliacao_educacao","Julho de 2026"))


    st.divider()
    
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
                """
                <div style="
                    color:#55A6D9;
                    font-size:30px;
                    font-weight:800;
                    letter-spacing:0.10em;
                    text-transform:uppercase;
                    margin-top:1rem;
                    margin-bottom:0.8rem;
                ">
                    Imagem dos gestores
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("## Avaliação pessoal dos prefeitos")

    col1, col2 = st.columns(2)

    with col1:
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                "avaliacao_pessoa_eduardo_paes",
                "Março de 2026 — Pessoa de Eduardo Paes"
            )
        )

    with col2:
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "avaliacao_pessoa_cavaliere",
                "Julho de 2026 — Pessoa de Eduardo Cavaliere"
            )
        )


# ============================================================
# PERCEPÇÕES E EXPECTATIVAS
# ============================================================

elif pagina == "Percepções e expectativas":

    st.title("Como os cariocas percebem a cidade?")

    st.subheader("Percepções sobre o momento atual, identidade carioca, representação política e expectativas para os próximos meses")

    st.write("16ª edição · Julho de 2026")

    st.markdown(
                """
                <div style="
                    color:#55A6D9;
                    font-size:30px;
                    font-weight:800;
                    letter-spacing:0.10em;
                    text-transform:uppercase;
                    margin-top:1rem;
                    margin-bottom:0.8rem;
                ">
                    Percepção dos cariocas
                </div>
                """,
                unsafe_allow_html=True
            )

    

    st.markdown("## Preocupações e identidade")

    mostrar_grafico(grafico_fator_interativo(ponderacoes_julho_2026,"fator_maior_preocupacao_ultimos_tres_meses", 
                                             titulo="Fatores de preocupação nos últimos três meses"))
    st.divider()

    mostrar_grafico(grafico_escala_interativo(ponderacoes_julho_2026,"eduardo_cavaliere_espirito_carioca",
                                              titulo="Quanto o Eduardo Cavaliere representa o espírito carioca?" ))

    st.divider()

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
                    """
                    <div style="
                        color:#55A6D9;
                        font-size:30px;
                        font-weight:800;
                        letter-spacing:0.10em;
                        text-transform:uppercase;
                        margin-top:1rem;
                        margin-bottom:0.8rem;
                    ">
                        Percepções sobre a cidade
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.markdown("## Nível de concordância")
    
    st.markdown("### Tenho orgulho de ser carioca")

    col1, col2 = st.columns(2)

    with col1:
        titulo_periodo("Março de 2026")
        mostrar_grafico(
            grafico_concordancia_interativo(
                ponderacoes_marco_2026,
                "concordancia_orgulho_ser_carioca",
                titulo=""
            )
        )

    with col2:
        titulo_periodo("Julho de 2026")
        mostrar_grafico(
            grafico_concordancia_interativo(
                ponderacoes_julho_2026,
                "concordancia_orgulho_ser_carioca",
                titulo=""
            )
        )

    st.divider()
    st.markdown("### Acredito que o Rio terá um futuro melhor")

    col1, col2 = st.columns(2)

    with col1:
        titulo_periodo("Março de 2026")
        mostrar_grafico(
            grafico_concordancia_interativo(
                ponderacoes_marco_2026,
                "concordancia_rio_tera_futuro_melhor",
                titulo=""
            )
        )

    with col2:
        titulo_periodo("Julho de 2026")
        mostrar_grafico(
            grafico_concordancia_interativo(
                ponderacoes_julho_2026,
                "concordancia_rio_tera_futuro_melhor",
                titulo=""
            )
        )

    st.divider()
    st.markdown("### Me sinto representado pela Prefeitura")

    col1, col2 = st.columns(2)

    with col1:
        titulo_periodo("Março de 2026")
        mostrar_grafico(
            grafico_concordancia_interativo(
                ponderacoes_marco_2026,
                "concordancia_me_sinto_representado_prefeitura",
                titulo=""
            )
        )

    with col2:
        titulo_periodo("Julho de 2026")
        mostrar_grafico(
            grafico_concordancia_interativo(
                ponderacoes_julho_2026,
                "concordancia_me_sinto_representado_prefeitura",
                titulo=""
            )
        )
    st.divider()
    st.markdown("### Me sinto representado pelo prefeito")

    col1, col2 = st.columns(2)

    with col1:
        titulo_periodo("Março de 2026")
        mostrar_grafico(
            grafico_concordancia_interativo(
                ponderacoes_marco_2026,
                "concordancia_me_sinto_representado_prefeito",
                titulo=""
            )
        )

    with col2:
        titulo_periodo("Julho de 2026")
        mostrar_grafico(
            grafico_concordancia_interativo(
                ponderacoes_julho_2026,
                "concordancia_me_sinto_representado_prefeito",
                titulo=""
            )
        )

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
                    """
                    <div style="
                        color:#55A6D9;
                        font-size:30px;
                        font-weight:800;
                        letter-spacing:0.10em;
                        text-transform:uppercase;
                        margin-top:1rem;
                        margin-bottom:0.8rem;
                    ">
                        Expectativas
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    st.markdown("## Expectativa para os próximos três meses")
       
    col1, col2 = st.columns(2)

    with col1:
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                "expectativa_proximos_tres_meses_eduardo_cavaliere",
                titulo="Março de 2026 — Eduardo Cavaliere"
            )
        )

    with col2:
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "expectativa_proximos_tres_meses_eduardo_cavaliere",
                titulo="Julho de 2026 — Eduardo Cavaliere"
            )
        )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                "expectativa_proximos_tres_meses_claudio_castro",
                titulo="Março de 2026 — Cláudio Castro"
            )
        )

    with col2:
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "avaliacao_proximos_tres_meses_governo_estado",
                titulo="Julho de 2026 — Governo do Estado"
            )
        )

    st.divider()
    col1, col2 = st.columns(2)

    with col1:
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                "expectativa_proximos_tres_meses_lula",
                titulo="Março de 2026 — Lula"
            )
        )

    with col2:
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "expectativa_proximos_tres_meses_lula",
                titulo="Julho de 2026 — Lula"
            )
        )

    st.markdown("<br>", unsafe_allow_html=True)
    st.divider()

    st.markdown( """
                        <div style="
                            color:#55A6D9;
                            font-size:30px;
                            font-weight:800;
                            letter-spacing:0.10em;
                            text-transform:uppercase;
                            margin-top:1rem;
                            margin-bottom:0.8rem;
                        ">
                            Avaliação dos governos
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
    
    st.markdown("## Avaliação dos últimos três meses")

    
    col1, col2 = st.columns(2)

    with col1:
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                "avaliacao_ultimos_tres_meses_claudio_castro",
                titulo="Março de 2026 — Cláudio Castro"
            )
        )

    with col2:
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "avaliacao_ultimos_tres_meses_governo_estado",
                titulo="Julho de 2026 — Governo do Estado"
            )
        )

    st.divider()

    mostrar_grafico(
        grafico_avaliacao_interativo(
            ponderacoes_julho_2026,
            "avaliacao_governador",
            titulo="Avaliação do Governador interino Ricardo Couto"
        )
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                "avaliacao_ultimos_tres_meses_lula",
                titulo="Março de 2026 — Lula"
            )
        )

    with col2:
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "avaliacao_ultimos_tres_meses_lula",
                titulo="Julho de 2026 — Lula"
            )
        )


# ============================================================
# ECONOMIA SOLIDÁRIA
# ============================================================

elif pagina == "Economia Solidária":

    st.title("O que os cariocas pensam sobre Economia Solidária?")

    st.subheader("Conhecimento, importância, prioridades e práticas relacionadas à Economia Solidária")

    st.write("16ª edição · Julho de 2026")

    st.markdown(
                        """
                        <div style="
                            color:#55A6D9;
                            font-size:30px;
                            font-weight:800;
                            letter-spacing:0.10em;
                            text-transform:uppercase;
                            margin-top:1rem;
                            margin-bottom:0.8rem;
                        ">
                            Conhecimento e percepção
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

    
    mostrar_grafico(
            grafico_economia_solidaria_interativo(
                ponderacoes_economia_2026,
                "ouviu_falar_economia_solidaria",
                "Já ouviu falar em Economia Solidária?"
            ),
            altura=500
        )
    st.divider()


    mostrar_grafico(
            grafico_economia_solidaria_interativo(
                ponderacoes_economia_2026,
                "importancia_apoio_economia_solidaria",
                "Qual é a importância da Prefeitura do Rio de Janeiro desenvolver políticas de apoio à economia solidária?"
            ),
            altura=500
        )
    st.divider()

    mostrar_grafico(
        grafico_economia_solidaria_interativo(
            ponderacoes_economia_2026,
            "prioridade_fortalecer_economia_solidaria",
            "Qual das ações a seguir deve ser a prioridade para fortalecer a economia solidária?"
        ),
        altura=500
    )

    st.divider()

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown(
                            """
                            <div style="
                                color:#55A6D9;
                                font-size:30px;
                                font-weight:800;
                                letter-spacing:0.10em;
                                text-transform:uppercase;
                                margin-top:1rem;
                                margin-bottom:0.8rem;
                            ">
                                Percepções
                            </div>
                            """,
                            unsafe_allow_html=True
                        )

    st.markdown("## Nível de concordância com as afirmações")
        

    mostrar_grafico(
            grafico_concordancia_economia_interativo(
                ponderacoes_economia_2026,
                "pagar_mais_produtos",
                "Estou disposto a pagar um pouco mais por produtos produzidos de forma socialmente justa ou ambientalmente sustentável"), altura=600)
    
    st.divider()

    mostrar_grafico(
            grafico_concordancia_economia_interativo(
                ponderacoes_economia_2026,
                "comprar_feiras_locais",
                "Comprar em feiras locais fortalece a economia do bairro"),altura=600)

    st.divider()
   
    mostrar_grafico(
            grafico_concordancia_economia_interativo(
                ponderacoes_economia_2026,
                "moedas_sociais_fortalecer_economia",
                "Moedas sociais podem ajudar a fortalecer a economia das comunidades"),altura=600)

    st.divider()

    mostrar_grafico(
            grafico_concordancia_economia_interativo(
                ponderacoes_economia_2026,
                "empreendimentos_coletivos",
                "Empreendimentos coletivos são uma boa alternativa para a inclusão produtiva"),altura=600)

    st.divider()

    mostrar_grafico(
        grafico_concordancia_economia_interativo(
            ponderacoes_economia_2026,
            "bancos_comunitarios_acesso_credito",
            "Bancos comunitários ampliam o acesso ao crédito"),altura=600)


# ============================================================
# PERFIL DA AMOSTRA
# ============================================================

elif pagina == "Perfil da amostra":

    st.title("Quem respondeu à pesquisa?")

    st.subheader("Perfil sociodemográfico e socioeconômico dos entrevistados, considerando os dados ponderados segundo sexo, cor/raça e faixa etária.")

    st.write("16ª edição · Julho de 2026 · Amostra não probabilística")

    st.markdown(
                                """
                                <div style="
                                    color:#55A6D9;
                                    font-size:30px;
                                    font-weight:800;
                                    letter-spacing:0.10em;
                                    text-transform:uppercase;
                                    margin-top:1rem;
                                    margin-bottom:0.8rem;
                                ">
                                    Perfil sociodemográfico
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

    st.markdown(
        """
    
        <div class="rio21-section-title">
            Características dos entrevistados
        </div>

        <div class="rio21-section-description">
            Distribuição da amostra ponderada por sexo,
            faixa etária e cor/raça.
        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        mostrar_grafico(grafico_sexo(ponderacoes_julho_2026["sexo"]),altura=430)

    with col2:
        mostrar_grafico(grafico_idade(ponderacoes_julho_2026["idade"]),altura=430)

    with col3:
        mostrar_grafico(grafico_raca(ponderacoes_julho_2026["raca"]),altura=430)

    st.markdown("<br>", unsafe_allow_html=True)

    st.divider()

    st.markdown("""
                <div style="
                color:#55A6D9;
                font-size:30px;
                font-weight:800;
                letter-spacing:0.10em;
                text-transform:uppercase;
                margin-top:1rem;
                margin-bottom:0.8rem;">
                Perfil socioeconômico
                </div>""",
                unsafe_allow_html=True)

    st.markdown(
        """
        <div class="rio21-section-title">
            Condições sociais e econômicas
        </div>

        <div class="rio21-section-description">
            Distribuição dos entrevistados segundo ocupação,
            escolaridade, renda familiar e região de moradia.
        </div>
        """,
        unsafe_allow_html=True
    )

    mostrar_grafico(grafico_ocupacao(ponderacoes_julho_2026["ocupacao"]),altura=600)
    
    st.divider()

    mostrar_grafico(grafico_barra_horizontal(ponderacoes_julho_2026["escolaridade"], "Escolaridade"),altura=600)

    st.divider()

    mostrar_grafico(grafico_renda_sm(ponderacoes_julho_2026["renda_familiar_mensal"]),altura=500)
                    
    st.divider()

    mostrar_grafico(grafico_barra_horizontal(ponderacoes_julho_2026["regiao_onde_mora"], "Região de Moradia"),altura=500)

    st.divider()

    st.markdown(
        """
        <div class="rio21-source">
            Fonte: Pesquisa Rio21 — 16ª edição, julho de 2026.
            Dados ponderados por sexo, cor/raça e faixa etária,
            com base no Censo 2022.
        </div>
        """,
        unsafe_allow_html=True
    )

