import streamlit as st
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
from estilo import aplicar_estilo, mostrar_logo_sidebar

# ============================================================
# CONFIGURAÇÃO
# ============================================================

st.set_page_config(
    page_title="Pesquisa de Opinião — Rio21",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

aplicar_estilo()

# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def ajustar_ponderacoes(ponderacoes):
    if not isinstance(ponderacoes, dict):
        return ponderacoes
    for chave, resultado in ponderacoes.items():
        if hasattr(resultado, "columns") and "percent" in resultado.columns:
            ponderacoes[chave] = ajustar_percentuais_100(
                resultado,
                coluna="percent",
                casas=1
            )
    return ponderacoes

def mostrar_grafico(fig, altura=None):
    if fig is None:
        return

    fig.update_layout(
        autosize=True,
        margin=dict(
            l=25,
            r=25,
            t=75,
            b=45
        ),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.10,
            xanchor="center",
            x=0.5
        )
    )

    fig.update_xaxes(
        automargin=True
    )

    fig.update_yaxes(
        automargin=True
    )

    if altura:
        fig.update_layout(height=altura)

    st.plotly_chart(
        fig,
        use_container_width=True,
        config={
            "displayModeBar": False,
            "responsive": True
        }
    )

def titulo_secao(texto):
    st.markdown(
        f"""
        <div class="titulo-secao">
            {texto}
        </div>
        """,
        unsafe_allow_html=True
    )

def titulo_periodo(texto):
    st.markdown(
        f"""
        <div style="
            color:#687078;
            font-size:24px;
            font-weight:800;
            text-transform:uppercase;
            letter-spacing:0.08em;
            margin-bottom:0.25rem;
        ">
            {texto}
        </div>
        """,
        unsafe_allow_html=True
    )

def texto_grande(texto, tamanho=24):
    st.markdown(
        f'<div class="texto-grande" style="--tamanho-texto:{tamanho}px">{texto}</div>',
        unsafe_allow_html=True
    )

def comparacao_grafico(variavel_marco, variavel_julho=None):
    if variavel_julho is None:
        variavel_julho = variavel_marco
    col1, col2 = st.columns(2)
    with col1:
        titulo_periodo("Março de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                variavel_marco,
                titulo=""
            )
        )
    with col2:
        titulo_periodo("Julho de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                variavel_julho,
                titulo=""
            )
        )

def comparacao_concordancia(variavel, pergunta):
    st.markdown(f"### {pergunta}")
    col1, col2 = st.columns(2)
    with col1:
        titulo_periodo("Março de 2026")
        mostrar_grafico(
            grafico_concordancia_interativo(
                ponderacoes_marco_2026,
                variavel,
                titulo=""
            )
        )
    with col2:
        titulo_periodo("Julho de 2026")
        mostrar_grafico(
            grafico_concordancia_interativo(
                ponderacoes_julho_2026,
                variavel,
                titulo=""
            )
        )

# ============================================================
# DADOS
# ============================================================

df_julho_2026 = carregar_dados()

amostra_julho_2026, ponderacoes_julho_2026 = calcular_ponderacoes(
    df_julho_2026
)

ponderacoes_julho_2026 = ajustar_ponderacoes(
    ponderacoes_julho_2026
)

df_marco_2026 = carregar_dados_marco()

amostra_marco_2026, ponderacoes_marco_2026 = calcular_ponderacoes_marco(
    df_marco_2026
)

ponderacoes_marco_2026 = ajustar_ponderacoes(
    ponderacoes_marco_2026
)

# ============================================================
# ECONOMIA SOLIDÁRIA
# ============================================================

ponderacoes_economia_2026 = ponderacoes_julho_2026

if isinstance(ponderacoes_economia_2026, dict):
    if "prioridade_fortalecer_economia_solidaria" in ponderacoes_economia_2026:
        ponderacoes_economia_2026[
            "prioridade_fortalecer_economia_solidaria"
        ] = ponderacoes_economia_2026[
            "prioridade_fortalecer_economia_solidaria"
        ].replace({
            "Facilitar o acesso a crédito e financiamentoão 4Facilitar o acesso a crédito e financiamento":
                "Facilitar o acesso a crédito e financiamento",
            "Incentivar compras públicas de empreendimentos solidáriosIncentivar compras públicas de empreendimentos solidários":
                "Incentivar compras públicas de empreendimentos solidários"
        })
    if "ouviu_falar_economia_solidaria" in ponderacoes_economia_2026:
        ponderacoes_economia_2026[
            "ouviu_falar_economia_solidaria"
        ] = ponderacoes_economia_2026[
            "ouviu_falar_economia_solidaria"
        ].replace({
            "Apenas ouvi fakar": "Apenas ouviu falar"
        })

# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:
    mostrar_logo_sidebar()
    st.markdown(
        """
        <div style="
            color:#55A6D9 !important;
            font-size:20px;
            font-weight:800;
            letter-spacing:0.10em;
            text-transform:uppercase;
            margin-bottom:1.8rem;
            line-height:1.5;
        ">
            RIO21 · PESQUISA DE OPINIÃO
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        section[data-testid="stSidebar"] {
            background:#FFFFFF !important;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] {
            background:#FFFFFF !important;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label {
            color:#000000 !important;
            background:#FFFFFF !important;
            opacity:1 !important;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label p {
            color:#000000 !important;
            font-size:16px !important;
            font-weight:600 !important;
            opacity:1 !important;
            visibility:visible !important;
            display:block !important;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label span {
            color:#000000 !important;
            opacity:1 !important;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label:hover {
            background:#F2F2F2 !important;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
            background:#EAF5FB !important;
        }
        section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
            color:#000000 !important;
            font-weight:700 !important;
        }
        @media (max-width:768px) {
            section[data-testid="stSidebar"] {
                background:#FFFFFF !important;
            }
            section[data-testid="stSidebar"] div[role="radiogroup"] label {
                min-height:48px !important;
                padding:0.8rem 0.9rem !important;
                background:#FFFFFF !important;
            }
            section[data-testid="stSidebar"] div[role="radiogroup"] label p {
                color:#000000 !important;
                font-size:17px !important;
                font-weight:600 !important;
                line-height:1.3 !important;
                white-space:normal !important;
                overflow:visible !important;
                visibility:visible !important;
                opacity:1 !important;
            }
            section[data-testid="stSidebar"] div[role="radiogroup"] label span {
                color:#000000 !important;
            }
            section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {
                background:#EAF5FB !important;
            }
            section[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {
                color:#000000 !important;
            }
        }
        </style>
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
    st.divider()
    st.caption("Pesquisa Rio21 · 16ª edição")

# ============================================================
# VISÃO GERAL
# ============================================================

if pagina == "Visão geral":
    st.title("Avaliação da Gestão Municipal do Rio de Janeiro")
    st.subheader(
        "O que pensa a população carioca sobre os governos, "
        "os serviços públicos e o futuro da cidade."
    )
    st.write("**16ª edição · Julho de 2026**")
    st.divider()
    titulo_secao("A pesquisa em números")
    st.header("Principais informações")
    texto_grande("Dados básicos desta edição do levantamento.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Entrevistas", "593", "respondentes", delta_color="off")
    with col2:
        st.metric("Variáveis", "43", "questões e indicadores analisados", delta_color="off")
    with col3:
        st.metric("Ponderação", "Censo 2022", "referência para a população carioca", delta_color="off")
    st.divider()
    titulo_secao("Sobre a pesquisa")
    st.header("Objetivo do levantamento")
    with st.container(border=True):
        texto_grande(
            "A pesquisa busca compreender a percepção da população "
            "carioca sobre as ações do Governo Municipal, os serviços "
            "públicos, as condições da cidade e as expectativas para "
            "os próximos meses."
        )
        texto_grande(
            "O levantamento integra a série de pesquisas de opinião "
            "pública realizadas pelo Rio21 e permite acompanhar "
            "mudanças nas percepções dos cariocas ao longo do tempo."
        )
    st.divider()
    titulo_secao("Informações do levantamento")
    st.header("Dados básicos da pesquisa")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("Período de coleta")
            texto_grande(
                "Questionário aplicado online entre "
                "21 de julho e 4 de agosto de 2026."
            )
    with col2:
        with st.container(border=True):
            st.subheader("Amostra")
            texto_grande(
                "Amostra não probabilística composta por 593 respondentes."
            )
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("Ponderação")
            texto_grande(
                "Os dados foram ponderados segundo sexo, cor/raça "
                "e faixa etária, utilizando como referência a "
                "composição da população carioca segundo o Censo 2022."
            )
    with col2:
        with st.container(border=True):
            st.subheader("Comparação entre edições")
            texto_grande(
                "As análises comparativas utilizam os dados da "
                "15ª edição, realizada em março de 2026, e da "
                "16ª edição, realizada em julho de 2026."
            )
    st.divider()
    titulo_secao("Conteúdo da pesquisa")
    st.header("O que a pesquisa analisa")
    texto_grande(
        "O questionário reúne diferentes dimensões da percepção "
        "dos cariocas sobre a cidade e seus governos."
    )
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("Gestão pública")
            texto_grande(
                "Avaliação dos governos municipal e estadual, além "
                "de aspectos relacionados à saúde, educação, "
                "transportes, assistência social, preservação "
                "ambiental e conservação urbana e patrimonial.",
                20
            )
    with col2:
        with st.container(border=True):
            st.subheader("Percepções e expectativas")
            texto_grande(
                "Preocupações recentes, orgulho de ser carioca, "
                "expectativas para os próximos meses e percepção "
                "de representação política.",
                20
            )
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("Economia Solidária")
            texto_grande(
                "Conhecimento, importância atribuída ao tema, "
                "prioridades e concordância com afirmações "
                "relacionadas à Economia Solidária.",
                20
            )
    with col2:
        with st.container(border=True):
            st.subheader("Perfil da amostra")
            texto_grande(
                "Características sociodemográficas e "
                "socioeconômicas dos respondentes, considerando "
                "os dados ponderados.",
                20
            )
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
    st.subheader(
        "Comparação entre a percepção dos cariocas sobre o "
        "Governo Eduardo Paes e o Governo Eduardo Cavaliere."
    )
    st.markdown("## Avaliação do Governo Municipal")
    comparacao_grafico(
        "avaliacao_governo_paes",
        "avaliacao_governo_cavaliere"
    )
    st.divider()
    st.markdown("## Avaliação da Gestão Municipal da Saúde no Rio de Janeiro")
    comparacao_grafico("avaliacao_saude")
    st.divider()
    st.markdown("## Avaliação da Gestão Municipal dos Transportes no Rio de Janeiro")
    comparacao_grafico("avaliacao_transportes")
    st.divider()
    st.markdown("## Avaliação da Gestão Municipal da Conservação urbana e patrimonial no Rio de Janeiro")
    comparacao_grafico("avaliacao_conservacao_urbana_patrimonial")
    st.divider()
    st.markdown("## Avaliação da Gestão Municipal da Preservação ambiental no Rio de Janeiro")
    comparacao_grafico("avaliacao_preservacao_ambiental")
    st.divider()
    st.markdown("## Avaliação da Gestão Municipal Assistência social no Rio de Janeiro")
    comparacao_grafico("avaliacao_assistencia_social")
    st.divider()
    st.markdown("## Avaliação da Gestão Municipal da Educação no Rio de Janeiro")
    comparacao_grafico("avaliacao_educacao")
    st.divider()
    titulo_secao("Imagem dos gestores")
    st.markdown("## Avaliação pessoal dos prefeitos")
    col1, col2 = st.columns(2)
    with col1:
        titulo_periodo("Março de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                "avaliacao_pessoa_eduardo_paes",
                titulo="Eduardo Paes"
            )
        )
    with col2:
        titulo_periodo("Julho de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "avaliacao_pessoa_cavaliere",
                titulo="Eduardo Cavaliere"
            )
        )

# ============================================================
# PERCEPÇÕES E EXPECTATIVAS
# ============================================================

elif pagina == "Percepções e expectativas":
    st.title("Como os cariocas percebem a cidade?")
    st.subheader(
        "Percepções sobre o momento atual, identidade carioca, "
        "representação política e expectativas para os próximos meses"
    )
    st.write("16ª edição · Julho de 2026")
    titulo_secao("Percepção dos cariocas")
    st.markdown("## Preocupações e identidade")
    st.markdown("### Fatores de preocupação nos últimos três meses")
    mostrar_grafico(
        grafico_fator_interativo(
            ponderacoes_julho_2026,
            "fator_maior_preocupacao_ultimos_tres_meses",
            titulo=""
        )
    )
    st.divider()
    st.markdown("### Quanto o Eduardo Cavaliere representa o espírito carioca?")
    mostrar_grafico(
        grafico_escala_interativo(
            ponderacoes_julho_2026,
            "eduardo_cavaliere_espirito_carioca",
            titulo=""
        )
    )
    st.divider()
    titulo_secao("Percepções sobre a cidade")
    st.markdown("## Nível de concordância")
    comparacao_concordancia(
        "concordancia_orgulho_ser_carioca",
        "Tenho orgulho de ser carioca"
    )
    st.divider()
    comparacao_concordancia(
        "concordancia_rio_tera_futuro_melhor",
        "Acredito que o Rio terá um futuro melhor"
    )
    st.divider()
    comparacao_concordancia(
        "concordancia_me_sinto_representado_prefeitura",
        "Me sinto representado pela Prefeitura"
    )
    st.divider()
    comparacao_concordancia(
        "concordancia_me_sinto_representado_prefeito",
        "Me sinto representado pelo prefeito"
    )
    st.markdown("<br>", unsafe_allow_html=True)
    titulo_secao("Expectativas")
    st.markdown("## Expectativa para os próximos três meses")

    st.markdown("## Eduardo Cavaliere")
    col1, col2 = st.columns(2)
    with col1:
        titulo_periodo("Março de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                "expectativa_proximos_tres_meses_eduardo_cavaliere",
                titulo=""
            )
        )
    with col2:
        titulo_periodo("Julho de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "expectativa_proximos_tres_meses_eduardo_cavaliere",
                titulo=""
            )
        )
    st.divider()

    st.markdown("## Governo do Estado do RJ")
    col1, col2 = st.columns(2)
    with col1:
        titulo_periodo("Março de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                "expectativa_proximos_tres_meses_claudio_castro",
                titulo=""
            )
        )
    with col2:
        titulo_periodo("Julho de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "avaliacao_proximos_tres_meses_governo_estado",
                titulo=""
            )
        )
    st.divider()

    st.markdown("## Lula")
    col1, col2 = st.columns(2)
    with col1:
        titulo_periodo("Março de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                "expectativa_proximos_tres_meses_lula",
                titulo=""
            )
        )
    with col2:
        titulo_periodo("Julho de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "expectativa_proximos_tres_meses_lula",
                titulo=""
            )
        )
    st.markdown("<br>", unsafe_allow_html=True)
    titulo_secao("Avaliação dos governos")
    st.markdown("## Avaliação dos últimos três meses")

    st.markdown("## Governo do Estado do RJ")
    col1, col2 = st.columns(2)
    with col1:
        titulo_periodo("Março de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                "avaliacao_ultimos_tres_meses_claudio_castro",
                titulo=""
            )
        )
    with col2:
        titulo_periodo("Julho de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "avaliacao_ultimos_tres_meses_governo_estado",
                titulo=""
            )
        )
 
    st.markdown("## Lula")
    col1, col2 = st.columns(2)
    with col1:
        titulo_periodo("Março de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_marco_2026,
                "avaliacao_ultimos_tres_meses_lula",
                titulo=""
            )
        )
    with col2:
        titulo_periodo("Julho de 2026")
        mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "avaliacao_ultimos_tres_meses_lula",
                titulo=""
            )
        )

    st.divider()
    
    st.markdown("### Avaliação do Governador interino Ricardo Couto")
    mostrar_grafico(
            grafico_avaliacao_interativo(
                ponderacoes_julho_2026,
                "avaliacao_governador",
                titulo=""
            )
        )
    st.divider()
    

# ============================================================
# ECONOMIA SOLIDÁRIA
# ============================================================

elif pagina == "Economia Solidária":
    st.title("O que os cariocas pensam sobre Economia Solidária?")
    st.subheader(
        "Conhecimento, importância, prioridades e práticas "
        "relacionadas à Economia Solidária"
    )
    st.write("16ª edição · Julho de 2026")
    titulo_secao("Conhecimento e percepção")
    st.markdown("### Já ouviu falar em Economia Solidária?")
    mostrar_grafico(
        grafico_economia_solidaria_interativo(
            ponderacoes_economia_2026,
            "ouviu_falar_economia_solidaria",
            ""
        )
    )
    st.divider()
    st.markdown(
        "### Qual é a importância da Prefeitura do Rio de Janeiro desenvolver políticas de apoio à economia solidária?"
    )
    mostrar_grafico(
        grafico_economia_solidaria_interativo(
            ponderacoes_economia_2026,
            "importancia_apoio_economia_solidaria",
            ""
        )
    )
    st.divider()
    st.markdown(
        "### Qual das ações a seguir deve ser a prioridade para fortalecer a economia solidária?"
    )
    mostrar_grafico(
        grafico_economia_solidaria_interativo(
            ponderacoes_economia_2026,
            "prioridade_fortalecer_economia_solidaria",
            ""
        )
    )
    st.divider()
    titulo_secao("Percepções")
    st.markdown("## Nível de concordância com as afirmações")
    economia = [
        (
            "pagar_mais_produtos",
            "Estou disposto a pagar um pouco mais por produtos "
            "produzidos de forma socialmente justa ou "
            "ambientalmente sustentável"
        ),
        (
            "comprar_feiras_locais",
            "Comprar em feiras locais fortalece a economia do bairro"
        ),
        (
            "moedas_sociais_fortalecer_economia",
            "Moedas sociais podem ajudar a fortalecer a economia "
            "das comunidades"
        ),
        (
            "empreendimentos_coletivos",
            "Empreendimentos coletivos são uma boa alternativa "
            "para a inclusão produtiva"
        ),
        (
            "bancos_comunitarios_acesso_credito",
            "Bancos comunitários ampliam o acesso ao crédito"
        )
    ]
    for variavel, pergunta in economia:
        mostrar_grafico(
            grafico_concordancia_economia_interativo(
                ponderacoes_economia_2026,
                variavel,
                pergunta
            )
        )
        st.divider()

# ============================================================
# PERFIL DA AMOSTRA
# ============================================================

elif pagina == "Perfil da amostra":
    st.title("Quem respondeu à pesquisa?")
    st.subheader(
        "Perfil sociodemográfico e socioeconômico dos entrevistados, "
        "considerando os dados ponderados segundo sexo, cor/raça "
        "e faixa etária."
    )
    st.write(
        "16ª edição · Julho de 2026 · Amostra não probabilística"
    )

    titulo_secao("Perfil sociodemográfico")

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
        mostrar_grafico(
            grafico_sexo(
                ponderacoes_julho_2026["sexo"]
            ),
            altura=380
        )

    with col2:
        mostrar_grafico(
            grafico_idade(
                ponderacoes_julho_2026["idade"]
            ),
            altura=380
        )

    with col3:
        mostrar_grafico(
            grafico_raca(
                ponderacoes_julho_2026["raca"]
            ),
            altura=380
        )

    st.divider()

    titulo_secao("Perfil socioeconômico")

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

    mostrar_grafico(
        grafico_ocupacao(
            ponderacoes_julho_2026["ocupacao"]
        ),
        altura=500
    )

    st.divider()

    mostrar_grafico(
        grafico_barra_horizontal(
            ponderacoes_julho_2026["escolaridade"],
            "Escolaridade"
        ),
        altura=500
    )

    st.divider()

    mostrar_grafico(
        grafico_renda_sm(
            ponderacoes_julho_2026["renda_familiar_mensal"]
        ),
        altura=500
    )

    st.divider()

    mostrar_grafico(
        grafico_barra_horizontal(
            ponderacoes_julho_2026["regiao_onde_mora"],
            "Região de Moradia"
        ),
        altura=500
    )

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