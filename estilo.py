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

    /* =========================
       SIDEBAR
       ========================= */

    section[data-testid="stSidebar"] {{
        background:#FFFFFF !important;
        border-right:1px solid #E5E7EB !important;
    }}

    section[data-testid="stSidebar"] > div {{
        background:#FFFFFF !important;
        padding-top:2rem;
    }}

    section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {{
        background:#FFFFFF !important;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] {{
        gap:0.25rem !important;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label {{
        background:#FFFFFF !important;
        color:#000000 !important;
        border-radius:8px;
        padding:0.65rem 0.75rem;
        transition:all 0.15s ease;
        cursor:pointer;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
        background:#EAF5FB !important;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label p {{
        color:#000000 !important;
        font-size:0.92rem;
        font-weight:600;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label span {{
        color:#000000 !important;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label div {{
        color:#000000 !important;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {{
        background:#EAF5FB !important;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] p {{
        color:#000000 !important;
        font-weight:700;
    }}

    section[data-testid="stSidebar"] div[role="radiogroup"] input {{
        accent-color:{AZUL} !important;
    }}

    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {{
        color:#000000;
    }}

    section[data-testid="stSidebar"] .stCaption {{
        color:#687078 !important;
    }}

    /* =========================
       TEXTOS GERAIS
       ========================= */

    h1,h2,h3 {{
        color:{TEXTO};
        white-space:normal !important;
        overflow-wrap:break-word !important;
        word-wrap:break-word !important;
        word-break:normal !important;
        max-width:100% !important;
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

    .rio21-section-title {{
        color:{TEXTO};
        font-size:32px;
        font-weight:750;
        letter-spacing:-0.025em;
        line-height:1.2;
        margin-bottom:0.7rem;
        white-space:normal !important;
        overflow-wrap:break-word !important;
        word-wrap:break-word !important;
        max-width:100% !important;
    }}

    .rio21-section-description {{
        color:{CINZA_TEXTO};
        font-size:19px;
        line-height:1.55;
        max-width:1000px;
        margin-bottom:1.5rem;
        white-space:normal !important;
        overflow-wrap:break-word !important;
        word-wrap:break-word !important;
    }}

    .titulo-secao {{
        color:{TEXTO};
        font-size:32px;
        font-weight:750;
        letter-spacing:-0.025em;
        line-height:1.2;
        margin-top:1.5rem;
        margin-bottom:1rem;
        white-space:normal !important;
        overflow-wrap:break-word !important;
        word-wrap:break-word !important;
        max-width:100% !important;
    }}

    .texto-grande {{
        color:{CINZA_TEXTO};
        font-size:var(--tamanho-texto, 24px);
        line-height:1.55;
        max-width:1100px;
        margin-bottom:1.2rem;
        white-space:normal !important;
        overflow-wrap:break-word !important;
        word-wrap:break-word !important;
    }}

    /* =========================
       MÉTRICAS
       ========================= */

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

    /* =========================
       GRÁFICOS
       ========================= */

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

    /* =========================
       BOTÕES
       ========================= */

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

    /* =========================
       FONTE
       ========================= */

    .rio21-source {{
        border-top:1px solid {BORDA};
        margin-top:2rem;
        padding-top:1rem;
        color:#7A8288;
        font-size:14px;
        line-height:1.5;
    }}

    /* =========================
       CELULAR
       ========================= */

    @media (max-width:768px) {{

        .block-container {{
            padding-left:1rem !important;
            padding-right:1rem !important;
            padding-top:1.2rem !important;
            padding-bottom:2.5rem !important;
            width:100% !important;
            max-width:100% !important;
        }}

        /* =========================
           SIDEBAR CELULAR
           ========================= */

        section[data-testid="stSidebar"] {{
            width:85vw !important;
            max-width:340px !important;
            background:#FFFFFF !important;
        }}

        section[data-testid="stSidebar"] > div {{
            background:#FFFFFF !important;
            padding-top:1rem !important;
        }}

        section[data-testid="stSidebar"] [data-testid="stSidebarContent"] {{
            background:#FFFFFF !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] {{
            width:100% !important;
            gap:0.35rem !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label {{
            width:100% !important;
            min-height:46px !important;
            padding:0.8rem 0.9rem !important;
            background:#FFFFFF !important;
            color:#000000 !important;
            border-radius:8px !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label p {{
            color:#000000 !important;
            font-size:1rem !important;
            font-weight:600 !important;
            line-height:1.3 !important;
            white-space:normal !important;
            overflow:visible !important;
            text-overflow:clip !important;
            overflow-wrap:break-word !important;
            word-wrap:break-word !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label span {{
            color:#000000 !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label div {{
            color:#000000 !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] {{
            background:#EAF5FB !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label[data-checked="true"] p {{
            color:#000000 !important;
            font-weight:700 !important;
        }}

        /* =========================
           TÍTULOS CELULAR
           ========================= */

        h1,h2,h3 {{
            white-space:normal !important;
            overflow:visible !important;
            text-overflow:clip !important;
            overflow-wrap:break-word !important;
            word-wrap:break-word !important;
            word-break:normal !important;
            max-width:100% !important;
            width:100% !important;
        }}

        h1 {{
            font-size:1.8rem !important;
            line-height:1.2 !important;
        }}

        h2 {{
            font-size:1.45rem !important;
            line-height:1.25 !important;
        }}

        h3 {{
            font-size:1.15rem !important;
            line-height:1.3 !important;
        }}

        .titulo-secao,
        .rio21-section-title {{
            font-size:1.45rem !important;
            line-height:1.25 !important;
            margin-top:1rem !important;
            margin-bottom:0.6rem !important;
            white-space:normal !important;
            overflow:visible !important;
            text-overflow:clip !important;
            overflow-wrap:break-word !important;
            word-wrap:break-word !important;
            max-width:100% !important;
        }}

        .texto-grande {{
            font-size:var(--tamanho-texto, 20px) !important;
            line-height:1.5 !important;
            white-space:normal !important;
            overflow-wrap:break-word !important;
            word-wrap:break-word !important;
        }}

        .rio21-section-description {{
            font-size:1rem !important;
            line-height:1.45 !important;
            white-space:normal !important;
            overflow-wrap:break-word !important;
            word-wrap:break-word !important;
        }}

        /* =========================
           COLUNAS
           ========================= */

        [data-testid="stHorizontalBlock"] {{
            flex-wrap:wrap !important;
            gap:0.8rem !important;
        }}

        [data-testid="column"] {{
            width:100% !important;
            min-width:100% !important;
            flex:1 1 100% !important;
        }}

        /* =========================
           MÉTRICAS
           ========================= */

        [data-testid="stMetric"] {{
            padding:1rem !important;
        }}

        [data-testid="stMetricValue"] {{
            font-size:1.8rem !important;
        }}

        [data-testid="stMetricLabel"] {{
            font-size:0.95rem !important;
        }}

        [data-testid="stMetricDelta"] {{
            font-size:0.85rem !important;
        }}

        /* =========================
           CONTAINERS
           ========================= */

        [data-testid="stVerticalBlockBorderWrapper"] {{
            width:100% !important;
            max-width:100% !important;
        }}

        /* =========================
           GRÁFICOS
           ========================= */

        .stPlotlyChart,
        div[data-testid="stPlotlyChart"],
        .js-plotly-plot,
        .plot-container,
        .plotly {{
            width:100% !important;
            max-width:100% !important;
        }}

        div[data-testid="stPlotlyChart"] iframe {{
            width:100% !important;
            max-width:100% !important;
        }}

        .plotly {{
            overflow-x:hidden !important;
        }}

        /* =========================
           MARKDOWN
           ========================= */

        [data-testid="stMarkdownContainer"] {{
            max-width:100% !important;
            width:100% !important;
            overflow:visible !important;
            overflow-wrap:break-word !important;
            word-wrap:break-word !important;
        }}

        [data-testid="stMarkdownContainer"] h1,
        [data-testid="stMarkdownContainer"] h2,
        [data-testid="stMarkdownContainer"] h3 {{
            white-space:normal !important;
            overflow:visible !important;
            text-overflow:clip !important;
            overflow-wrap:break-word !important;
            word-wrap:break-word !important;
            word-break:normal !important;
            max-width:100% !important;
            width:100% !important;
        }}

        /* =========================
           BOTÕES
           ========================= */

        .stButton > button {{
            width:100% !important;
        }}
    }}

    /* =========================
       CELULARES MUITO PEQUENOS
       ========================= */

    @media (max-width:480px) {{

        .block-container {{
            padding-left:0.8rem !important;
            padding-right:0.8rem !important;
        }}

        section[data-testid="stSidebar"] {{
            width:88vw !important;
            max-width:320px !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label {{
            padding:0.85rem 0.9rem !important;
            min-height:48px !important;
        }}

        section[data-testid="stSidebar"] div[role="radiogroup"] label p {{
            font-size:1rem !important;
            color:#000000 !important;
            font-weight:600 !important;
        }}

        h1,h2,h3 {{
            white-space:normal !important;
            overflow:visible !important;
            text-overflow:clip !important;
            overflow-wrap:break-word !important;
            word-wrap:break-word !important;
            word-break:normal !important;
            width:100% !important;
            max-width:100% !important;
        }}

        h1 {{
            font-size:1.6rem !important;
            line-height:1.2 !important;
        }}

        h2 {{
            font-size:1.3rem !important;
            line-height:1.25 !important;
        }}

        h3 {{
            font-size:1.1rem !important;
            line-height:1.3 !important;
        }}

        .titulo-secao,
        .rio21-section-title {{
            font-size:1.3rem !important;
            line-height:1.25 !important;
        }}

        .texto-grande {{
            font-size:18px !important;
        }}

        .rio21-section-description {{
            font-size:0.95rem !important;
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