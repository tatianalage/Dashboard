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
    .stApp {{ background:#FFFFFF; color:{TEXTO}; }}
    .main {{ background:#FFFFFF; }}
    .block-container {{ max-width:1400px; padding-top:2rem; padding-bottom:4rem; padding-left:3rem; padding-right:3rem; }}

    section[data-testid="stSidebar"] {{ background:#F7F8FA; border-right:1px solid #E5E7EB; }}
    section[data-testid="stSidebar"] > div {{ padding-top:2rem; }}
    section[data-testid="stSidebar"] div[role="radiogroup"] {{ gap:0.25rem; }}
    section[data-testid="stSidebar"] div[role="radiogroup"] label {{ border-radius:8px; padding:0.65rem 0.75rem; transition:all 0.15s ease; }}
    section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{ background:#EAF5FB; }}
    section[data-testid="stSidebar"] div[role="radiogroup"] label p {{ font-size:0.92rem; font-weight:500; }}

    h1,h2,h3 {{ color:{TEXTO}; }}
    h1 {{ font-weight:750; letter-spacing:-0.025em; }}
    h2 {{ font-weight:700; letter-spacing:-0.02em; }}
    h3 {{ font-weight:650; }}

    .rio21-section-title {{ color:{TEXTO}; font-size:32px; font-weight:750; letter-spacing:-0.025em; line-height:1.2; margin-bottom:0.7rem; }}
    .rio21-section-description {{ color:{CINZA_TEXTO}; font-size:19px; line-height:1.55; max-width:1000px; margin-bottom:1.5rem; }}

    [data-testid="stMetric"] {{ background:#FFFFFF; border:2px solid {AZUL}; border-radius:12px; padding:1.2rem 1.3rem; }}
    [data-testid="stMetricLabel"] {{ color:{CINZA_TEXTO}; font-size:18px; }}
    [data-testid="stMetricValue"] {{ color:{AZUL}; font-weight:800; font-size:40px; }}

    .stPlotlyChart {{ width:100% !important; margin-bottom:2rem; }}
    div[data-testid="stPlotlyChart"] {{ width:100%; }}

    .stButton > button {{ border-radius:8px; border:1px solid {AZUL}; color:{AZUL}; background:#FFFFFF; font-weight:600; }}
    .stButton > button:hover {{ background:#EAF5FB; color:{AZUL}; }}

    .rio21-source {{ border-top:1px solid {BORDA}; margin-top:2rem; padding-top:1rem; color:#7A8288; font-size:14px; line-height:1.5; }}

    @media (max-width:900px) {{
        .block-container {{ padding-left:1.2rem; padding-right:1.2rem; }}
        .rio21-section-title {{ font-size:28px; }}
        .rio21-section-description {{ font-size:18px; }}
    }}
    </style>
    """, unsafe_allow_html=True)


def mostrar_logo_sidebar():
    caminho = os.path.join(os.path.dirname(os.path.abspath(__file__)), "logo.png")

    if os.path.exists(caminho):
        st.image(caminho, width=170)
    else:
        st.markdown(f"""
        <div style="width:100%;text-align:center;font-size:1.5rem;font-weight:800;color:{AZUL};padding:0.2rem 0 1.6rem 0;">
            RIO21
        </div>
        """, unsafe_allow_html=True)