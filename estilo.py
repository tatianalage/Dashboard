import streamlit as st
import os


# ============================================================
# IDENTIDADE VISUAL RIO21
# ============================================================

AZUL = "#55A6D9"
ROXO = "#6451A6"
VERDE = "#9EBF26"

TEXTO = "#20252A"
CINZA_TEXTO = "#687078"
CINZA_CLARO = "#F5F8FA"
BORDA = "#DDE3E7"
BRANCO = "#FFFFFF"


# ============================================================
# ESTILO GLOBAL
# ============================================================

def aplicar_estilo():

    st.markdown(
        f"""
        <style>

        /* ==================================================
           BASE
        ================================================== */

        .stApp {{
            background: #FFFFFF;
            color: {TEXTO};
        }}

        .main {{
            background: #FFFFFF;
        }}

        .block-container {{
            max-width: 1400px;
            padding-top: 2rem;
            padding-bottom: 4rem;
            padding-left: 3rem;
            padding-right: 3rem;
        }}


        /* ==================================================
           SIDEBAR
        ================================================== */

        section[data-testid="stSidebar"] {{
            background: #F7F8FA;
            border-right: 1px solid #E5E7EB;
        }}

        section[data-testid="stSidebar"] > div {{
            padding-top: 2rem;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] {{
            gap: 0.25rem;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label {{
            border-radius: 8px;
            padding: 0.65rem 0.75rem;
            transition: all 0.15s ease;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
            background: #EAF5FB;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label p {{
            font-size: 0.92rem;
            font-weight: 500;
        }}


        /* ==================================================
           TÍTULOS
        ================================================== */

        h1,
        h2,
        h3 {{
            color: {TEXTO};
        }}

        h1 {{
            font-weight: 750;
            letter-spacing: -0.025em;
        }}

        h2 {{
            font-weight: 700;
            letter-spacing: -0.02em;
        }}

        h3 {{
            font-weight: 650;
        }}


        /* ==================================================
           CABEÇALHO
        ================================================== */

        .rio21-kicker {{
            color:#55A6D9 ;
            font-size: 20px
            font-weight: 800;
            letter-spacing: 0.12em;
            text-transform: uppercase;
            margin-bottom: 1rem;
            line-height: 1.4;
            white-space: normal;
        }}

        .rio21-title {{
            color: {TEXTO};
            font-size: 50px;
            line-height: 1.08;
            font-weight: 800;
            letter-spacing: -0.035em;
            max-width: 1050px;
            margin-bottom: 1rem;
        }}

        .rio21-subtitle {{
            color: {CINZA_TEXTO};
            font-size: 24px;
            line-height: 1.5;
            max-width: 1050px;
            margin-bottom: 1rem;
        }}

        .rio21-meta {{
            color: #7A8288;
            font-size: 1.05rem;
            line-height: 1.5;
        }}

        .rio21-line {{
            height: 5px;
            width: 100%;
            background: {AZUL};
            border-radius: 5px;
            margin-top: 1.7rem;
            margin-bottom: 3rem;
        }}


        /* ==================================================
           SEÇÕES
        ================================================== */

        .rio21-section-kicker {{
            color: #55A6D9;
            font-size: 20px;
            font-weight: 800;
            letter-spacing: 0.10em;
            text-transform: uppercase;
            margin-bottom: 0.6rem;
            line-height: 1.4
        }}

        .rio21-section-title {{
            color: {TEXTO};
            font-size: 32px;
            font-weight: 750;
            letter-spacing: -0.025em;
            line-height: 1.2;
            margin-bottom: 0.7rem;
        }}

        .rio21-section-description {{
            color: {CINZA_TEXTO};
            font-size: 19px;
            line-height: 1.55;
            max-width: 1000px;
            margin-bottom: 1.5rem;
        }}


        /* ==================================================
           VISÃO GERAL — NÚMEROS
        ================================================== */

        .overview-stats {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 0;
            margin-top: 1.5rem;
            margin-bottom: 3.5rem;
            border-top: 1px solid {BORDA};
            border-bottom: 1px solid {BORDA};
        }}

        .overview-stat {{
            padding: 1.8rem 2rem;
            min-height: 170px;
        }}

        .overview-stat:not(:last-child) {{
            border-right: 1px solid {BORDA};
        }}

        .overview-stat-label {{
            color: {CINZA_TEXTO};
            font-size: 14px;
            font-weight: 800;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 0.65rem;
        }}

        .overview-stat-number {{
            color: {AZUL};
            font-size: 50px;
            font-weight: 850;
            line-height: 1;
            letter-spacing: -0.04em;
        }}

        .overview-stat-number-censo {{
            color: {AZUL};
            font-size: 38px;
            font-weight: 850;
            line-height: 1.1;
            letter-spacing: -0.03em;
        }}

        .overview-stat-description {{
            color: {CINZA_TEXTO};
            font-size: 17px;
            line-height: 1.4;
            margin-top: 0.6rem;
            max-width: 280px;
        }}


        /* ==================================================
           VISÃO GERAL — OBJETIVO
        ================================================== */

        .overview-objective {{
            display: grid;
            grid-template-columns: 7px 1fr;
            gap: 1.4rem;
            margin-top: 1.3rem;
            margin-bottom: 3.5rem;
        }}

        .overview-objective-line {{
            background: {AZUL};
            border-radius: 10px;
        }}

        .overview-objective-text {{
            color: {TEXTO};
            font-size: 23px;
            line-height: 1.65;
            max-width: 1050px;
        }}

        .overview-objective-text p {{
            margin: 0 0 1.2rem 0;
        }}

        .overview-objective-text p:last-child {{
            margin-bottom: 0;
        }}


        /* ==================================================
           VISÃO GERAL — INFORMAÇÕES
        ================================================== */

        .overview-info-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1.2rem;
            margin-top: 1.3rem;
            margin-bottom: 3.5rem;
        }}

        .overview-info {{
            border-top: 3px solid {AZUL};
            padding: 1.2rem 0.5rem 1.3rem 0;
        }}

        .overview-info-label {{
            color: {AZUL};
            font-size: 14px;
            font-weight: 800;
            letter-spacing: 0.1em;
            text-transform: uppercase;
            margin-bottom: 0.65rem;
        }}

        .overview-info-text {{
            color: {TEXTO};
            font-size: 21px;
            line-height: 1.55;
        }}

        .overview-info-text strong {{
            color: {AZUL};
            font-weight: 800;
        }}


        /* ==================================================
           VISÃO GERAL — ÁREAS DA PESQUISA
        ================================================== */

        .overview-analysis-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 1px;
            background: {BORDA};
            border: 1px solid {BORDA};
            margin-top: 1.5rem;
            margin-bottom: 3rem;
        }}

        .overview-analysis-card {{
            background: #FFFFFF;
            padding: 1.7rem 1.8rem;
            min-height: 190px;
        }}

        .overview-analysis-number {{
            color: #B7C1C8;
            font-size: 14px;
            font-weight: 800;
            letter-spacing: 0.08em;
            margin-bottom: 0.8rem;
        }}

        .overview-analysis-title {{
            color: {AZUL};
            font-size: 21px;
            font-weight: 800;
            margin-bottom: 0.7rem;
        }}

        .overview-analysis-text {{
            color: {TEXTO};
            font-size: 18px;
            line-height: 1.6;
        }}


        /* ==================================================
           FONTE
        ================================================== */

        .rio21-source {{
            border-top: 1px solid {BORDA};
            margin-top: 2rem;
            padding-top: 1rem;
            color: #7A8288;
            font-size: 14px;
            line-height: 1.5;
        }}


        /* ==================================================
           INDICADORES
        ================================================== */

        .rio21-card-blue,
        .rio21-card-purple,
        .rio21-card-green {{
            background: #FFFFFF;
            border: 2px solid {AZUL};
            border-radius: 16px;
            padding: 1.6rem;
            margin-bottom: 1rem;
            box-shadow: 0 4px 14px rgba(85,166,217,0.10);
        }}

        .rio21-label {{
            color: {CINZA_TEXTO};
            font-size: 18px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.08em;
        }}

        .rio21-number {{
            color: {AZUL};
            font-size: 45px;
            font-weight: 850;
            margin-top: 0.3rem;
        }}

        .rio21-description {{
            color: {CINZA_TEXTO};
            font-size: 19px;
            margin-top: 0.3rem;
        }}


        /* ==================================================
           MÉTRICAS
        ================================================== */

        [data-testid="stMetric"] {{
            background: #FFFFFF;
            border: 2px solid {AZUL};
            border-radius: 12px;
            padding: 1.2rem 1.3rem;
        }}

        [data-testid="stMetricLabel"] {{
            color: {CINZA_TEXTO};
            font-size: 18px;
        }}

        [data-testid="stMetricValue"] {{
            color: {AZUL};
            font-weight: 800;
            font-size: 40px;
        }}


        /* ==================================================
           GRÁFICOS
        ================================================== */

        .stPlotlyChart {{
            width: 100% !important;
            margin-bottom: 2rem;
        }}

        div[data-testid="stPlotlyChart"] {{
            width: 100%;
        }}


        /* ==================================================
           BOTÕES
        ================================================== */

        .stButton > button {{
            border-radius: 8px;
            border: 1px solid {AZUL};
            color: {AZUL};
            background: #FFFFFF;
            font-weight: 600;
        }}

        .stButton > button:hover {{
            background: #EAF5FB;
            color: {AZUL};
        }}


        /* ==================================================
           RESPONSIVO
        ================================================== */

        @media (max-width: 900px) {{

            .block-container {{
                padding-left: 1.2rem;
                padding-right: 1.2rem;
            }}

            .rio21-title {{
                font-size: 38px;
            }}

            .rio21-subtitle {{
                font-size: 21px;
            }}

            .rio21-section-title {{
                font-size: 28px;
            }}

            .rio21-section-description {{
                font-size: 18px;
            }}

            .overview-stats {{
                grid-template-columns: 1fr;
            }}

            .overview-stat:not(:last-child) {{
                border-right: none;
                border-bottom: 1px solid {BORDA};
            }}

            .overview-info-grid {{
                grid-template-columns: 1fr;
            }}

            .overview-analysis-grid {{
                grid-template-columns: 1fr;
            }}

            .overview-objective-text {{
                font-size: 20px;
            }}

            .overview-info-text {{
                font-size: 19px;
            }}

            .overview-analysis-text {{
                font-size: 18px;
            }}
        }}

        </style>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# LOGO
# ============================================================

def mostrar_logo_sidebar():

    caminho = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "logo.png"
    )

    if os.path.exists(caminho):

        st.image(
            caminho,
            width=170
        )

    else:

        st.markdown(
            f"""
            <div style="
                width:100%;
                text-align:center;
                font-size:1.5rem;
                font-weight:800;
                color:{AZUL};
                padding:0.2rem 0 1.6rem 0;
            ">
                RIO21
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# CABEÇALHO
# ============================================================

def mostrar_cabecalho():

    st.markdown(
        f"""
        <div class="rio21-kicker">
            RIO21 · PESQUISA DE OPINIÃO
        </div>

        <div class="rio21-title">
            Avaliação da Gestão Municipal do Rio de Janeiro
        </div>

        <div class="rio21-subtitle">
            O que pensa a população carioca sobre os governos,
            os serviços públicos e o futuro da cidade.
        </div>

        <div class="rio21-meta">
            <strong>16ª edição · Julho de 2026</strong>
            &nbsp;&nbsp;·&nbsp;&nbsp;
            Coleta: 21/07/2026 a 04/08/2026
        </div>

        <div class="rio21-line"></div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# SEÇÃO
# ============================================================

def mostrar_secao(
    titulo,
    kicker=None,
    descricao=None
):

    html = ""

    if kicker:

        html += f"""
        <div class="rio21-section-kicker">
            {kicker}
        </div>
        """

    html += f"""
    <div class="rio21-section-title">
        {titulo}
    </div>
    """

    if descricao:

        html += f"""
        <div class="rio21-section-description">
            {descricao}
        </div>
        """

    st.markdown(
        html,
        unsafe_allow_html=True
    )


# ============================================================
# INDICADOR
# ============================================================

def mostrar_indicador(
    label,
    numero,
    descricao,
    cor="blue"
):

    classe = {
        "blue": "rio21-card-blue",
        "purple": "rio21-card-purple",
        "green": "rio21-card-green"
    }.get(
        cor,
        "rio21-card-blue"
    )

    st.markdown(
        f"""
        <div class="{classe}">
            <div class="rio21-label">
                {label}
            </div>

            <div class="rio21-number">
                {numero}
            </div>

            <div class="rio21-description">
                {descricao}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# VISÃO GERAL — COMPONENTES
# ============================================================

def mostrar_overview_stats():

    st.markdown(
        """
        <div class="overview-stats">

            <div class="overview-stat">

                <div class="overview-stat-label">
                    Entrevistas
                </div>

                <div class="overview-stat-number">
                    593
                </div>

                <div class="overview-stat-description">
                    respondentes
                </div>

            </div>


            <div class="overview-stat">

                <div class="overview-stat-label">
                    Variáveis
                </div>

                <div class="overview-stat-number">
                    43
                </div>

                <div class="overview-stat-description">
                    questões e indicadores analisados
                </div>

            </div>


            <div class="overview-stat">

                <div class="overview-stat-label">
                    Ponderação
                </div>

                <div class="overview-stat-number-censo">
                    Censo 2022
                </div>

                <div class="overview-stat-description">
                    referência para a população carioca
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def mostrar_overview_objetivo():

    st.markdown(
        """
        <div class="overview-objective">

            <div class="overview-objective-line"></div>

            <div class="overview-objective-text">

                <p>
                    A pesquisa busca compreender a percepção da população
                    carioca sobre as ações do Governo Municipal, os serviços
                    públicos, as condições da cidade e as expectativas para
                    os próximos meses.
                </p>

                <p>
                    O levantamento integra a série de pesquisas de opinião
                    pública realizadas pelo Rio21 e permite acompanhar
                    mudanças nas percepções dos cariocas ao longo do tempo.
                </p>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def mostrar_overview_informacoes():

    st.markdown(
        """
        <div class="overview-info-grid">

            <div class="overview-info">

                <div class="overview-info-label">
                    Período de coleta
                </div>

                <div class="overview-info-text">
                    Questionário aplicado online entre
                    <strong>21 de julho e 4 de agosto de 2026</strong>.
                </div>

            </div>


            <div class="overview-info">

                <div class="overview-info-label">
                    Amostra
                </div>

                <div class="overview-info-text">
                    Amostra <strong>não probabilística</strong>
                    composta por <strong>593 respondentes</strong>.
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


def mostrar_overview_analise():

    st.markdown(
        """
        <div class="overview-analysis-grid">

            <div class="overview-analysis-card">

                <div class="overview-analysis-number">
                    01
                </div>

                <div class="overview-analysis-title">
                    Gestão pública
                </div>

                <div class="overview-analysis-text">
                    Avaliação dos governos municipal e estadual,
                    além de aspectos relacionados à saúde, educação,
                    transportes, assistência social, preservação
                    ambiental e conservação urbana e patrimonial.
                </div>

            </div>


            <div class="overview-analysis-card">

                <div class="overview-analysis-number">
                    02
                </div>

                <div class="overview-analysis-title">
                    Percepções e expectativas
                </div>

                <div class="overview-analysis-text">
                    Preocupações recentes, orgulho de ser carioca,
                    expectativas para os próximos meses e percepção
                    de representação política.
                </div>

            </div>


            <div class="overview-analysis-card">

                <div class="overview-analysis-number">
                    03
                </div>

                <div class="overview-analysis-title">
                    Economia Solidária
                </div>

                <div class="overview-analysis-text">
                    Conhecimento, importância atribuída ao tema,
                    prioridades e concordância com afirmações
                    relacionadas à Economia Solidária.
                </div>

            </div>


            <div class="overview-analysis-card">

                <div class="overview-analysis-number">
                    04
                </div>

                <div class="overview-analysis-title">
                    Perfil da amostra
                </div>

                <div class="overview-analysis-text">
                    Características sociodemográficas e
                    socioeconômicas dos respondentes,
                    considerando os dados ponderados.
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
    )