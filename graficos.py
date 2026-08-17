import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ============================================================
# CONFIGURAÇÕES GERAIS
# ============================================================

FONTE_TITULO = 22
FONTE_CATEGORIA = 18
FONTE_PERCENTUAL = 16

# ============================================================
# FUNÇÕES AUXILIARES
# ============================================================

def _altura_horizontal(n_categorias, base=80, por_categoria=34, minimo=280, maximo=520):
    altura = base + (n_categorias * por_categoria)
    return max(minimo, min(altura, maximo))

def _altura_concordancia(n_categorias, base=90, por_categoria=38, minimo=300, maximo=500):
    altura = base + (n_categorias * por_categoria)
    return max(minimo, min(altura, maximo))

# ============================================================
# SEXO
# ============================================================

def grafico_sexo(sexo_df):
    df = sexo_df.copy()
    ordem = ['Feminino', 'Masculino']
    df['sexo'] = pd.Categorical(df['sexo'], categories=ordem, ordered=True)
    df = df.sort_values('sexo')
    fig = px.pie(
        df,
        names='sexo',
        values='percent',
        title='Sexo',
        color='sexo',
        color_discrete_map={'Masculino': '#176FAE', 'Feminino': '#66A9D6'},
        category_orders={'sexo': ordem}
    )
    fig.update_traces(
        texttemplate='%{value:.1f}%',
        textposition='inside',
        textfont=dict(size=FONTE_PERCENTUAL, color='black'),
        hovertemplate='<b>%{label}</b><br>Percentual: %{value:.1f}%<extra></extra>'
    )
    fig.update_layout(
        title=dict(text='Sexo', font=dict(size=FONTE_TITULO, color='black')),
        showlegend=True,
        legend=dict(font=dict(size=FONTE_CATEGORIA, color='black')),
        plot_bgcolor='white',
        paper_bgcolor='white',
        margin=dict(t=60, b=20, l=15, r=15),
        height=350
    )
    return fig

# ============================================================
# FAIXA ETÁRIA
# ============================================================

def grafico_idade(idade_df):
    df = idade_df.copy()
    ordem = [
        '16 a 24 anos',
        '25 a 29 anos',
        '30 a 39 anos',
        '40 a 49 anos',
        '50 a 59 anos',
        '60 anos ou mais'
    ]
    df['idade'] = pd.Categorical(df['idade'], categories=ordem, ordered=True)
    df = df.sort_values('idade')
    cores = ['#C7D6E5', '#A9C4DA', '#7FAED0', '#5F97C2', '#3F7FB3', '#1F5FA3']
    fig = px.bar(
        df,
        x='idade',
        y='percent',
        text='percent',
        title='Faixa etária',
        color='idade',
        color_discrete_sequence=cores,
        category_orders={'idade': ordem}
    )
    fig.update_traces(
        texttemplate='%{text:.1f}%',
        textposition='inside',
        textfont=dict(size=FONTE_PERCENTUAL, color='black'),
        hovertemplate='<b>%{x}</b><br>Percentual: %{y:.1f}%<extra></extra>',
        cliponaxis=False
    )
    fig.update_layout(
        title=dict(text='Faixa etária', font=dict(size=FONTE_TITULO, color='black')),
        showlegend=False,
        xaxis=dict(
            title=None,
            tickfont=dict(size=FONTE_CATEGORIA, color='black'),
            tickangle=-30,
            automargin=True
        ),
        yaxis=dict(
            title=None,
            showticklabels=False,
            showgrid=False,
            range=[0, 100]
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=350,
        margin=dict(t=60, b=70, l=15, r=15)
    )
    return fig

# ============================================================
# RAÇA / COR
# ============================================================

def grafico_raca(raca_df):
    df = raca_df.copy()
    ordem = ['Branca', 'Parda', 'Preta', 'Amarela', 'Indígena']
    df['raca'] = pd.Categorical(df['raca'], categories=ordem, ordered=True)
    df = df.sort_values('raca')
    cores = [
        '#3F7FB3',
        '#5F97C2',
        '#7FAED0',
        '#A9C4DA',
        '#C7D6E5'
    ]
    fig = px.bar(
        df,
        x='raca',
        y='percent',
        text='percent',
        title='Raça/cor',
        color='raca',
        color_discrete_sequence=cores,
        category_orders={'raca': ordem}
    )
    fig.update_traces(
        texttemplate='%{text:.1f}%',
        textposition='inside',
        textfont=dict(size=FONTE_PERCENTUAL, color='black'),
        hovertemplate='<b>%{x}</b><br>Percentual: %{y:.1f}%<extra></extra>',
        cliponaxis=False
    )
    fig.update_layout(
        title=dict(text='Raça/cor', font=dict(size=FONTE_TITULO, color='black')),
        showlegend=False,
        xaxis=dict(
            title=None,
            tickfont=dict(size=FONTE_CATEGORIA, color='black'),
            automargin=True
        ),
        yaxis=dict(
            title=None,
            showticklabels=False,
            showgrid=False,
            range=[0, 100]
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=350,
        margin=dict(t=60, b=55, l=15, r=15)
    )
    return fig

# ============================================================
# OCUPAÇÃO
# ============================================================

def grafico_ocupacao(ocup_df):
    df = ocup_df.copy()
    df = df.sort_values('percent', ascending=True)
    altura = _altura_horizontal(
        len(df),
        base=80,
        por_categoria=34,
        minimo=300,
        maximo=520
    )
    fig = px.bar(
        df,
        x='percent',
        y='ocupacao',
        orientation='h',
        text='percent',
        title='Ocupação',
        color='percent',
        color_continuous_scale='Blues'
    )
    fig.update_traces(
        texttemplate='%{text:.1f}%',
        textposition='inside',
        textfont=dict(size=FONTE_PERCENTUAL, color='white'),
        hovertemplate='<b>%{y}</b><br>Percentual: %{x:.1f}%<extra></extra>',
        cliponaxis=False
    )
    fig.update_layout(
        title=dict(text='Ocupação', font=dict(size=FONTE_TITULO, color='black')),
        coloraxis_showscale=False,
        xaxis=dict(
            title=None,
            showticklabels=False,
            showgrid=False,
            range=[0, 100]
        ),
        yaxis=dict(
            title=None,
            tickfont=dict(size=FONTE_CATEGORIA, color='black'),
            automargin=True
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=altura,
        margin=dict(t=60, l=220, r=15, b=15)
    )
    return fig

# ============================================================
# RENDA FAMILIAR
# ============================================================

def grafico_renda_sm(renda_df):
    df = renda_df.copy()
    mapa_sm = {
        'Até R$ 1.621,00': 'Até 1 SM',
        'De R$ 1.621,01 a R$ 3.036,00': 'De 1 a 2 SM',
        'De R$ 3.036,01 a R$ 4.554,00': 'De 2 a 3 SM',
        'De R$ 4.554,01 a R$ 7.590,00': 'De 3 a 5 SM',
        'De R$ 7.590,01 a R$ 15.180,00': 'De 5 a 10 SM',
        'De R$ 15.180,01 a R$ 21.252,00': 'De 10 a 14 SM',
        'Mais de R$ 21.252,01': 'Mais de 14 SM',
        'Não sei/Prefiro não responder': 'Não sei / Prefiro não responder'
    }
    df['renda_sm'] = df['renda_familiar_mensal'].map(mapa_sm)
    ordem = [
        'Até 1 SM',
        'De 1 a 2 SM',
        'De 2 a 3 SM',
        'De 3 a 5 SM',
        'De 5 a 10 SM',
        'De 10 a 14 SM',
        'Mais de 14 SM',
        'Não sei / Prefiro não responder'
    ]
    df['renda_sm'] = pd.Categorical(
        df['renda_sm'],
        categories=ordem,
        ordered=True
    )
    df = df.sort_values('renda_sm', ascending=False)
    cores_azul = [
        '#0B4F7A',
        '#176FAE',
        '#3E91C4',
        '#66A9D6',
        '#8FC1E8',
        '#B8D9F5',
        '#DCEEFF',
        '#EAF5FF'
    ]
    mapa_cores = dict(zip(ordem, cores_azul))
    altura = _altura_horizontal(
        len(df),
        base=80,
        por_categoria=34,
        minimo=320,
        maximo=500
    )
    fig = px.bar(
        df,
        x='percent',
        y='renda_sm',
        orientation='h',
        text='percent',
        title='Renda familiar mensal',
        color='renda_sm',
        color_discrete_map=mapa_cores,
        category_orders={'renda_sm': ordem}
    )
    fig.update_traces(
        texttemplate='%{text:.1f}%',
        textposition='inside',
        textfont=dict(size=FONTE_PERCENTUAL, color='white'),
        hovertemplate='<b>%{y}</b><br>Percentual: %{x:.1f}%<extra></extra>',
        cliponaxis=False
    )
    fig.update_layout(
        title=dict(text='Renda familiar mensal', font=dict(size=FONTE_TITULO, color='black')),
        showlegend=False,
        xaxis=dict(
            title=None,
            showticklabels=False,
            showgrid=False,
            range=[0, 100]
        ),
        yaxis=dict(
            title=None,
            tickfont=dict(size=FONTE_CATEGORIA, color='black'),
            automargin=True
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=altura,
        margin=dict(t=60, l=230, r=15, b=15)
    )
    return fig

# ============================================================
# BARRA HORIZONTAL
# ============================================================

def grafico_barra_horizontal(df, titulo):
    df = df.copy()
    variavel = [col for col in df.columns if col != 'percent'][0]
    df = df.sort_values('percent', ascending=True)
    altura = _altura_horizontal(
        len(df),
        base=80,
        por_categoria=34,
        minimo=300,
        maximo=520
    )
    cores_azul = [
        '#EAF5FF',
        '#DCEEFF',
        '#B8D9F5',
        '#8FC1E8',
        '#66A9D6',
        '#3E91C4',
        '#176FAE',
        '#0B4F7A',
        '#083B5C',
        '#052C45'
    ]
    cores = [
        cores_azul[min(i, len(cores_azul) - 1)]
        for i in range(len(df))
    ]
    fig = px.bar(
        df,
        x='percent',
        y=variavel,
        orientation='h',
        text='percent',
        title=titulo
    )
    fig.update_traces(
        marker_color=cores,
        texttemplate='%{text:.1f}%',
        textposition='inside',
        textfont=dict(size=FONTE_PERCENTUAL, color='white'),
        hovertemplate='<b>%{y}</b><br>Percentual: %{x:.1f}%<extra></extra>',
        cliponaxis=False
    )
    fig.update_layout(
        title=dict(text=titulo, font=dict(size=FONTE_TITULO, color='black')),
        xaxis=dict(
            title=None,
            showticklabels=False,
            showgrid=False,
            range=[0, 100]
        ),
        yaxis=dict(
            title=None,
            tickfont=dict(size=FONTE_CATEGORIA, color='black'),
            automargin=True
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=altura,
        margin=dict(t=60, l=220, r=15, b=15)
    )
    return fig

# ============================================================
# GRÁFICO DE AVALIAÇÃO
# ============================================================

def grafico_avaliacao_interativo(ponderacoes, variavel, titulo=None):
    df_plot = ponderacoes[variavel].copy()
    df_plot[variavel] = df_plot[variavel].astype(str).str.strip()
    ordem = [
        'Ótimo',
        'Bom',
        'Regular',
        'Ruim',
        'Péssimo',
        'Não sei / Prefiro não responder'
    ]
    df_plot = df_plot[df_plot[variavel].isin(ordem)].copy()
    df_plot[variavel] = pd.Categorical(
        df_plot[variavel],
        categories=ordem,
        ordered=True
    )
    df_plot = df_plot.sort_values(variavel)
    cores = {
        'Ótimo': '#FFD400',
        'Bom': '#2CA25F',
        'Regular': '#3498DB',
        'Ruim': '#3B4CC0',
        'Péssimo': '#6A00A8',
        'Não sei / Prefiro não responder': '#BDBDBD'
    }
    titulos_avaliacao = {
        'avaliacao_governo_cavaliere': 'Avaliação do Governo Eduardo Cavaliere',
        'avaliacao_educacao': 'Avaliação da Educação',
        'avaliacao_saude': 'Avaliação da Saúde',
        'avaliacao_transportes': 'Avaliação dos Transportes',
        'avaliacao_preservacao_ambiental': 'Avaliação da Preservação Ambiental',
        'avaliacao_conservacao_urbana_patrimonial': 'Avaliação da Conservação Urbana e Patrimonial',
        'avaliacao_assistencia_social': 'Avaliação da Assistência Social',
        'avaliacao_pessoa_cavaliere': 'Pessoa do Eduardo Cavaliere'
    }
    if titulo is None:
        titulo = titulos_avaliacao.get(
            variavel,
            variavel.replace('_', ' ').title()
        )
    fig = go.Figure()
    for _, row in df_plot.iterrows():
        categoria = str(row[variavel])
        percentual = float(row['percent'])
        cor_texto = 'black' if categoria in ['Ótimo', 'Não sei / Prefiro não responder'] else 'white'
        fig.add_trace(
            go.Bar(
                x=[percentual],
                y=['Avaliação'],
                orientation='h',
                name=categoria,
                marker_color=cores.get(categoria, '#999999'),
                text=[f'{percentual:.1f}%' if percentual >= 4 else ''],
                textposition='inside',
                insidetextanchor='middle',
                textfont=dict(
                    size=FONTE_PERCENTUAL,
                    color=cor_texto
                ),
                hovertemplate=(
                    f'<b>{categoria}</b><br>'
                    f'Percentual: %{{x:.1f}}%'
                    '<extra></extra>'
                )
            )
        )
        fig.update_layout(
        title=dict(
            text=titulo,
            font=dict(
                size=FONTE_TITULO,
                color='black'
            )
        ),
        barmode='stack',
        xaxis=dict(
            visible=False,
            range=[0, 100],
            fixedrange=True
        ),
        yaxis=dict(
            visible=False,
            fixedrange=True
        ),
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='top',
            y=-0.25,
            xanchor='center',
            x=0.5,
            font=dict(
                size=FONTE_CATEGORIA,
                color='black'
            )
        ),
        height=210,
        margin=dict(
            l=15,
            r=15,
            t=60,
            b=100
        ),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    fig.update_layout(
        title=dict(
            text=titulo,
            font=dict(
                size=FONTE_TITULO,
                color='black'
            )
        ),
        barmode='stack',
        xaxis=dict(
            visible=False,
            range=[0, 100],
            fixedrange=True
        ),
        yaxis=dict(
            visible=False,
            fixedrange=True
        ),
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='top',
            y=-0.25,
            xanchor='center',
            x=0.5,
            font=dict(
                size=FONTE_CATEGORIA,
                color='black'
            )
        ),
        height=210,
        margin=dict(
            l=15,
            r=15,
            t=60,
            b=100
        ),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    return fig
# ============================================================
# GRÁFICO DE FATOR
# ============================================================
def grafico_fator_interativo(ponderacoes, variavel, titulo):
    df_plot = ponderacoes[variavel].copy()
    df_plot = df_plot.sort_values('percent', ascending=True)
    maior_texto = max([len(str(x)) for x in df_plot[variavel]], default=0)
    margem_esquerda = min(max(240, maior_texto * 5), 420)
    fig = go.Figure()
    cores_azul = [
        '#DCEEFF',
        '#B8D9F5',
        '#8FC1E8',
        '#66A9D6',
        '#3E91C4',
        '#176FAE',
        '#0B4F7A'
    ]
    cores = [
        cores_azul[min(i, len(cores_azul) - 1)]
        for i in range(len(df_plot))
    ]
    fig.add_trace(
        go.Bar(
            x=df_plot['percent'],
            y=df_plot[variavel].astype(str),
            orientation='h',
            marker_color=cores,
            text=[f'{p:.1f}%' for p in df_plot['percent']],
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(size=FONTE_PERCENTUAL, color='white'),
            hovertemplate='<b>%{y}</b><br>Percentual: %{x:.1f}%<extra></extra>'
        )
    )
    fig.update_layout(
        title=dict(
            text=titulo,
            font=dict(size=FONTE_TITULO, color='black')
        ),
        xaxis=dict(
            visible=False,
            range=[0, 100]
        ),
        yaxis=dict(
            title='',
            tickfont=dict(size=FONTE_CATEGORIA, color='black'),
            automargin=True
        ),
        showlegend=False,
        height=_altura_horizontal(
            len(df_plot),
            base=80,
            por_categoria=34,
            minimo=300,
            maximo=520
        ),
        margin=dict(l=margem_esquerda, r=40, t=60, b=60),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    return fig

# ============================================================
# GRÁFICO DE ESCALA
# ============================================================

def grafico_escala_interativo(ponderacoes, variavel, titulo):
    df_plot = ponderacoes[variavel].copy()
    df_plot[variavel] = pd.to_numeric(
        df_plot[variavel],
        errors='coerce'
    )
    df_plot = df_plot.dropna(subset=[variavel])
    df_plot = df_plot.sort_values(variavel, ascending=True)
    cores_azul = [
        '#EAF5FF',
        '#DCEEFF',
        '#B8D9F5',
        '#8FC1E8',
        '#66A9D6',
        '#3E91C4',
        '#176FAE',
        '#0B4F7A',
        '#083B5C',
        '#052C45',
        '#031D2F'
    ]
    fig = go.Figure()
    for _, row in df_plot.iterrows():
        nota = int(row[variavel])
        percentual = float(row['percent'])
        cor = cores_azul[min(nota, len(cores_azul) - 1)]
        cor_texto = 'black' if nota <= 2 else 'white'
        fig.add_trace(
            go.Bar(
                x=[percentual],
                y=[str(nota)],
                orientation='h',
                marker_color=cor,
                text=[f'{percentual:.1f}%'],
                textposition='inside',
                insidetextanchor='middle',
                textfont=dict(
                    size=FONTE_PERCENTUAL,
                    color=cor_texto
                ),
                hovertemplate=(
                    f'<b>Nota {nota}</b><br>'
                    f'Percentual: {percentual:.1f}%'
                    '<extra></extra>'
                )
            )
        )
    fig.update_layout(
        title=dict(
            text=titulo,
            font=dict(
                size=FONTE_TITULO,
                color='black'
            )
        ),
        xaxis=dict(
            visible=False,
            range=[0, 100]
        ),
        yaxis=dict(
            title=None,
            tickfont=dict(
                size=FONTE_CATEGORIA,
                color='black'
            ),
            showgrid=False
        ),
        showlegend=False,
        bargap=0.15,
        height=420,
        margin=dict(
            l=70,
            r=15,
            t=60,
            b=20
        ),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    return fig

# ============================================================
# GRÁFICO DE CONCORDÂNCIA
# ============================================================

def grafico_concordancia_interativo(ponderacoes, variavel, titulo=None):
    df_plot = ponderacoes[variavel].copy()
    df_plot[variavel] = df_plot[variavel].astype(str).str.strip()
    ordem = [
        'Concordo totalmente',
        'Concordo',
        'Não concordo, nem discordo',
        'Discordo',
        'Discordo totalmente',
        'Não sei / Prefiro não responder'
    ]
    df_plot = df_plot[df_plot[variavel].isin(ordem)].copy()
    df_plot[variavel] = pd.Categorical(
        df_plot[variavel],
        categories=ordem,
        ordered=True
    )
    df_plot = df_plot.sort_values(variavel)
    cores_azul = {
        'Concordo totalmente': '#0B4F7A',
        'Concordo': '#176FAE',
        'Não concordo, nem discordo': '#3E91C4',
        'Discordo': '#66A9D6',
        'Discordo totalmente': '#8FC1E8',
        'Não sei / Prefiro não responder': '#B8D9F5'
    }
    titulos_concordancia = {
        'concordancia_orgulho_ser_carioca': 'Tenho orgulho de ser carioca',
        'concordancia_rio_tera_futuro_melhor': 'Acredito que o Rio terá um futuro melhor para as próximas gerações',
        'concordancia_me_sinto_representado_prefeitura': 'Me sinto representado pela Prefeitura',
        'concordancia_me_sinto_representado_prefeito': 'Me sinto representado pelo prefeito Eduardo Cavaliere'
    }
    if titulo is None:
        titulo = titulos_concordancia.get(
            variavel,
            variavel.replace('_', ' ').title()
        )
    fig = go.Figure()
    for _, row in df_plot.iterrows():
        categoria = str(row[variavel])
        percentual = float(row['percent'])
        cor_texto = 'white' if categoria not in [
            'Discordo totalmente',
            'Não sei / Prefiro não responder'
        ] else 'black'
        fig.add_trace(
            go.Bar(
                x=[percentual],
                y=['Concordância'],
                orientation='h',
                name=categoria,
                marker_color=cores_azul.get(categoria, '#999999'),
                text=[f'{percentual:.1f}%' if percentual >= 4 else ''],
                textposition='inside',
                insidetextanchor='middle',
                textfont=dict(
                    size=FONTE_PERCENTUAL,
                    color=cor_texto
                ),
                hovertemplate=(
                    f'<b>{categoria}</b><br>'
                    f'Percentual: %{{x:.1f}}%'
                    '<extra></extra>'
                )
            )
        )
    fig.update_layout(
        title=dict(
            text=titulo,
            font=dict(
                size=FONTE_TITULO,
                color='black'
            )
        ),
        barmode='stack',
        xaxis=dict(
            visible=False,
            range=[0, 100],
            fixedrange=True
        ),
        yaxis=dict(
            visible=False,
            fixedrange=True
        ),
        showlegend=True,
        legend=dict(
            orientation='h',
            yanchor='top',
            y=-0.25,
            xanchor='center',
            x=0.5,
            font=dict(
                size=FONTE_CATEGORIA,
                color='black'
            )
        ),
        height=210,
        margin=dict(
            l=15,
            r=15,
            t=60,
            b=100
        ),
        plot_bgcolor='white',
        paper_bgcolor='white'
    )
    return fig

# ============================================================
# ECONOMIA SOLIDÁRIA — BARRAS HORIZONTAIS
# ============================================================

def grafico_economia_solidaria_interativo(ponderacoes, variavel, titulo):
    df_plot = ponderacoes[variavel].copy()
    df_plot[variavel] = df_plot[variavel].astype(str).str.strip()
    df_plot = df_plot.sort_values('percent', ascending=True)
    maior_texto = max([len(str(x)) for x in df_plot[variavel]], default=0)
    margem_esquerda = min(max(240, maior_texto * 5), 420)
    cores_azul = [
        '#DCEEFF',
        '#B8D9F5',
        '#8FC1E8',
        '#66A9D6',
        '#3E91C4',
        '#176FAE',
        '#0B4F7A'
    ]
    cores = [
        cores_azul[min(i, len(cores_azul) - 1)]
        for i in range(len(df_plot))
    ]
    altura = _altura_horizontal(
        len(df_plot),
        base=80,
        por_categoria=34,
        minimo=300,
        maximo=520
    )
    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=df_plot['percent'],
            y=df_plot[variavel],
            orientation='h',
            marker_color=cores,
            text=[f'{valor:.1f}%' for valor in df_plot['percent']],
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(size=FONTE_PERCENTUAL, color='white'),
            hovertemplate='<b>%{y}</b><br>Percentual: %{x:.1f}%<extra></extra>',
            cliponaxis=False
        )
    )
    fig.update_layout(
        title=dict(
            text=titulo,
            font=dict(size=FONTE_TITULO, color='black')
        ),
        showlegend=False,
        xaxis=dict(
            title=None,
            visible=False,
            range=[0, 100]
        ),
        yaxis=dict(
            title=None,
            tickfont=dict(size=FONTE_CATEGORIA, color='black'),
            showgrid=False,
            automargin=True
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=altura,
        margin=dict(t=60, b=15, l=margem_esquerda, r=15)
    )
    return fig

# ============================================================
# ECONOMIA SOLIDÁRIA — CONCORDÂNCIA
# ============================================================

def grafico_concordancia_economia_interativo(ponderacoes, variavel, titulo):
    df_plot = ponderacoes[variavel].copy()
    df_plot[variavel] = df_plot[variavel].astype(str).str.strip()
    ordem = [
        'Concordo totalmente',
        'Concordo',
        'Não concordo, nem discordo',
        'Discordo',
        'Discordo totalmente',
        'Não sei / Prefiro não responder'
    ]
    categorias_existentes = [
        categoria
        for categoria in ordem
        if categoria in df_plot[variavel].values
    ]
    outras = [
        categoria
        for categoria in df_plot[variavel].unique()
        if categoria not in ordem
    ]
    ordem_final = categorias_existentes + outras
    df_plot[variavel] = pd.Categorical(
        df_plot[variavel],
        categories=ordem_final,
        ordered=True
    )
    df_plot = df_plot.sort_values(
        variavel,
        ascending=False
    )
    cores_roxo = [
        '#E8DDF3',
        '#D0B9E5',
        '#B594D1',
        '#976FC0',
        '#7749A8',
        '#582C91',
        '#3B176F'
    ]
    cores = [
        cores_roxo[min(i, len(cores_roxo) - 1)]
        for i in range(len(df_plot))
    ]
    altura = _altura_horizontal(
        len(df_plot),
        base=80,
        por_categoria=34,
        minimo=300,
        maximo=520
    )
    fig = go.Figure()
    y_labels = []
    for categoria in df_plot[variavel].astype(str):
        if categoria == 'Não sei / Prefiro não responder':
            y_labels.append('Não sei / Prefiro não<br>responder')
        else:
            y_labels.append(categoria)
    fig.add_trace(
        go.Bar(
            x=df_plot['percent'],
            y=y_labels,
            orientation='h',
            marker_color=cores,
            text=[f'{valor:.1f}%' for valor in df_plot['percent']],
            textposition='inside',
            insidetextanchor='middle',
            textfont=dict(size=FONTE_PERCENTUAL, color='white'),
            hovertemplate='<b>%{y}</b><br>Percentual: %{x:.1f}%<extra></extra>',
            cliponaxis=False
        )
    )
    fig.update_layout(
        title=dict(
            text=titulo,
            font=dict(size=FONTE_TITULO, color='black')
        ),
        showlegend=False,
        xaxis=dict(
            title=None,
            visible=False,
            range=[0, 100]
        ),
        yaxis=dict(
            title=None,
            tickfont=dict(size=FONTE_CATEGORIA, color='black'),
            showgrid=False,
            automargin=True
        ),
        plot_bgcolor='white',
        paper_bgcolor='white',
        height=altura,
        margin=dict(t=60, b=15, l=235, r=15)
    )
    return fig