import streamlit as st
import os

AZUL = "#55A6D9"
ROXO = "#6451A6"
VERDE = "#9EBF26"
TEXTO = "#20252A"
CINZA_TEXTO = "#687078"
BORDA = "#DDE3E7"

def aplicar_estilo():
    st.markdown(f"""
    <style>
    /* ============================================================
       CONFIGURAÇÃO GERAL
       ============================================================ */

    .stApp {{
        background:#FFFFFF;
        color:{TEXTO};
    }}

    .main {{
        background:#FFFFFF;
    }}

    .block-container {{
        max-width:1400px;
        padding-top:2rem;
        padding-bottom:4rem;
        padding-left:3rem;
        padding-right:3rem;
    }}

    /* ============================================================
       SIDEBAR
       ============================================================ */

    section[data-testid="stSidebar"] {{
        background:#F7F8FA;
        border-right:1px solid #E5E7EB;
    }}

    section[data-testid="stSidebar"] > div {{
        padding-top:2rem;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] {{
        gap:0.25rem;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label {{
        border-radius:8px;
        padding:0.65rem 0.75rem;
        transition:all 0.15s ease;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
        background:#EAF5FB;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label p {{
        font-size:0.92rem;
        font-weight:500;
    }}

    /* ============================================================
       TÍTULOS PADRÃO DO STREAMLIT
       ============================================================ */

    h1,h2,h3 {{
        color:{TEXTO};
    }}

    h1 {{
        font-weight:750;
        letter-spacing:-0.025em;
    }}

    h2 {{
        font-weight:700;
        letter-spacing:-0.02em;
    }}

    h3 {{
        font-weight:650;
    }}

    /* ============================================================
       TÍTULO DAS SEÇÕES
       ============================================================ */

    .titulo-secao {{
        color:{AZUL};
        font-size:30px;
        font-weight:800;
        letter-spacing:0.10em;
        text-transform:uppercase;
        line-height:1.25;
        margin-top:1rem;
        margin-bottom:0.8rem;
    }}

    /* ============================================================
       TEXTO GRANDE
       ============================================================ */

    .texto-grande {{
        font-size:var(--tamanho-texto);
        line-height:1.5;
        color:{TEXTO};
        margin-bottom:0.8rem;
    }}

    /* ============================================================
       TÍTULO E DESCRIÇÃO DE SEÇÕES
       ============================================================ */

    .rio21-section-title {{
        color:{TEXTO};
        font-size:32px;
        font-weight:750;
        letter-spacing:-0.025em;
        line-height:1.2;
        margin-bottom:0.7rem;
    }}

    .rio21-section-description {{
        color:{CINZA_TEXTO};
        font-size:19px;
        line-height:1.55;
        max-width:1000px;
        margin-bottom:1.5rem;
    }}

    /* ============================================================
       MÉTRICAS
       ============================================================ */

    [data-testid="stMetric"] {{
        background:#FFFFFF;
        border:2px solid {AZUL};
        border-radius:12px;
        padding:1.2rem 1.3rem;
    }}

    [data-testid="stMetricLabel"] {{
        color:{CINZA_TEXTO};
        font-size:18px;
    }}

    [data-testid="stMetricValue"] {{
        color:{AZUL};
        font-weight:800;
        font-size:40px;
    }}

    /* ============================================================
       GRÁFICOS
       ============================================================ */

    .stPlotlyChart {{
        width:100% !important;
        margin-bottom:2rem;
    }}

    div[data-testid="stPlotlyChart"] {{
        width:100% !important;
        max-width:100% !important;
    }}

    .js-plotly-plot,
    .plot-container,
    .plotly {{
        width:100% !important;
        max-width:100% !important;
    }}

    /* ============================================================
       BOTÕES
       ============================================================ */

    .stButton > button {{
        border-radius:8px;
        border:1px solid {AZUL};
        color:{AZUL};
        background:#FFFFFF;
        font-weight:600;
    }}

    .stButton > button:hover {{
        background:#EAF5FB;
        color:{AZUL};
    }}

    /* ============================================================
       FONTE
       ============================================================ */

    .rio21-source {{
        border-top:1px solid {BORDA};
        margin-top:2rem;
        padding-top:1rem;
        color:#7A8288;
        font-size:14px;
        line-height:1.5;
    }}

    /* ============================================================
       RESPONSIVIDADE — TABLET
       ============================================================ */

    @media (max-width:900px) {{

        .block-container {{
            padding-left:1.2rem;
            padding-right:1.2rem;
        }}

        .titulo-secao {{
            font-size:26px;
            letter-spacing:0.07em;
        }}

        .texto-grande {{
            font-size:18px !important;
            line-height:1.5;
        }}

        .rio21-section-title {{
            font-size:28px;
        }}

        .rio21-section-description {{
            font-size:18px;
        }}

        [data-testid="stMetricValue"] {{
            font-size:34px;
        }}

        [data-testid="stMetricLabel"] {{
            font-size:16px;
        }}
    }}

    /* ============================================================
       RESPONSIVIDADE — CELULAR
       ============================================================ */

    @media (max-width:768px) {{

        /* Conteúdo principal */

        .block-container {{
            padding-left:1rem !important;
            padding-right:1rem !important;
            padding-top:1.3rem !important;
            padding-bottom:2.5rem !important;
        }}

        /* ========================================================
           COLUNAS
           ======================================================== */

        [data-testid="stHorizontalBlock"] {{
            flex-wrap:wrap !important;
            gap:1rem !important;
        }}

        [data-testid="column"] {{
            width:100% !important;
            min-width:100% !important;
            flex:1 1 100% !important;
        }}

        /* ========================================================
           TÍTULOS
           ======================================================== */

        h1 {{
            font-size:1.8rem !important;
            line-height:1.2 !important;
            letter-spacing:-0.02em;
        }}

        h2 {{
            font-size:1.45rem !important;
            line-height:1.25 !important;
        }}

        h3 {{
            font-size:1.15rem !important;
            line-height:1.3 !important;
        }}

        /* ========================================================
           TÍTULOS DE SEÇÃO
           ======================================================== */

        .titulo-secao {{
            font-size:21px !important;
            letter-spacing:0.05em;
            line-height:1.3;
            margin-top:0.8rem;
            margin-bottom:0.7rem;
        }}

        /* ========================================================
           TEXTO GRANDE
           ======================================================== */

        .texto-grande {{
            font-size:17px !important;
            line-height:1.5;
            margin-bottom:0.7rem;
        }}

        /* ========================================================
           SEÇÕES PERSONALIZADAS
           ======================================================== */

        .rio21-section-title {{
            font-size:22px !important;
            line-height:1.3;
        }}

        .rio21-section-description {{
            font-size:16px !important;
            line-height:1.5;
        }}

        /* ========================================================
           MÉTRICAS
           ======================================================== */

        [data-testid="stMetric"] {{
            width:100% !important;
            padding:1rem !important;
        }}

        [data-testid="stMetricValue"] {{
            font-size:30px !important;
        }}

        [data-testid="stMetricLabel"] {{
            font-size:15px !important;
        }}

        [data-testid="stMetricDelta"] {{
            font-size:13px !important;
        }}

        /* ========================================================
           GRÁFICOS
           ======================================================== */

        .stPlotlyChart {{
            width:100% !important;
            max-width:100% !important;
            margin-bottom:1rem;
        }}

        div[data-testid="stPlotlyChart"] {{
            width:100% !important;
            max-width:100% !important;
        }}

        .js-plotly-plot,
        .plot-container,
        .plotly {{
            width:100% !important;
            max-width:100% !important;
        }}

        /* ========================================================
           SIDEBAR
           ======================================================== */

        section[data-testid="stSidebar"] {{
            width:85vw !important;
        }}

        section[data-testid="stSidebar"] > div {{
            padding-top:1rem;
        }}

        /* ========================================================
           TEXTO GERAL
           ======================================================== */

        p {{
            font-size:1rem !important;
            line-height:1.5 !important;
        }}

        /* ========================================================
           FONTE
           ======================================================== */

        .rio21-source {{
            font-size:13px;
            line-height:1.5;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)


def mostrar_logo_sidebar():
    caminho = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "logo.png"
    )

    if os.path.exists(caminho):
        st.image(caminho, width=170)
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