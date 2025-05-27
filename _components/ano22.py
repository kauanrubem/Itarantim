from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def criar_grafico1_ano22(file_path):
    import pandas as pd
    import plotly.express as px
    from dash import dcc

    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices').dropna(how="all").reset_index(drop=True)
    df.columns = ['Descrição', 'Valor']
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df = df.dropna(subset=['Valor'])
    filter_values = [
        'TOTAL DA RECEITA PARA FINS DE APURAÇÃO DOS ÍNDICES',
        'RECEITAS FUNDEB(IMPOSTOS E COMPLEMENTAÇÃO)',
        'VALOR PARA APLICAÇÃO DIRETA NO MDE (5%)'
    ]
    df_filtered = df[df['Descrição'].isin(filter_values)].copy()

    df_filtered['text'] = df_filtered.apply(
        lambda row: f"{row['Descrição']}<br>R$ {row['Valor']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'),
        axis=1
    )

    fig = px.bar(
        df_filtered,
        y='Descrição',
        x='Valor',
        text='text',
        color='Valor',
        color_continuous_scale=["#0D3327", "#145A32", "#1E8449", "#239B56"],
        orientation='h'
    )

    fig.update_traces(
        textposition='inside',
        textfont=dict(color='white', size=14),
        hovertemplate='<b>%{y}</b><br>%{x:.2f} R$<extra></extra>'
    )

    fig.update_layout(coloraxis_showscale=False)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=16),
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        xaxis=dict(showticklabels=False, showgrid=True, gridcolor='rgba(255,255,255,0.1)', gridwidth=1, zeroline=False),
        margin=dict(l=20, r=20, t=60, b=40)
    )

    return dcc.Graph(figure=fig)

def criar_grafico2_ano22(file_path):
    import pandas as pd
    import plotly.express as px
    from dash import dcc

    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices').dropna(how="all").reset_index(drop=True)
    df.columns = ['Descrição', 'Valor']
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df = df.dropna(subset=['Valor'])
    filter_values = [
        'TOTAL FUNDEB - FONTE 18',
        'TOTAL FUNDEB - FONTE 19',
        'MDE - FONTE 01'
    ]
    df_filtered = df[df['Descrição'].isin(filter_values)].copy()

    df_filtered['text'] = df_filtered.apply(
        lambda row: f"{row['Descrição']}<br>R$ {row['Valor']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'),
        axis=1
    )

    fig = px.bar(
        df_filtered,
        y='Descrição',
        x='Valor',
        text='text',
        color='Valor',
        color_continuous_scale=["#0D3327", "#145A32", "#1E8449", "#239B56"],
        orientation='h'
    )

    fig.update_traces(
        textposition='inside',
        textfont=dict(color='white', size=14),
        hovertemplate='<b>%{y}</b><br>%{x:.2f} R$<extra></extra>'
    )

    fig.update_layout(coloraxis_showscale=False)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=16),
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        xaxis=dict(showticklabels=False, showgrid=True, gridcolor='rgba(255,255,255,0.1)', gridwidth=1, zeroline=False),
        margin=dict(l=20, r=20, t=60, b=40)
    )

    return dcc.Graph(figure=fig)

def criar_grafico3_ano22(file_path):
    import pandas as pd
    import plotly.express as px
    from dash import dcc

    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices').dropna(how="all").reset_index(drop=True)
    df.columns = ['Descrição', 'Valor']
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df = df.dropna(subset=['Valor'])
    filter_values = [
        'RECEITA DE IMPOSTOS LÍQUIDA (I)',
        'RECEITA DE TRANSFERÊNCIAS CONSTITUCIONAIS E LEGAIS (II)',
        'TOTAL DAS RECEITAS PARA APURAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE (III) = I + II',
        'TOTAL DAS DESPESA COM AÇÕES E SEVIÇOS PÚBLICOS EM SAÚDE (VI) = (IV) -(V)'
    ]
    df_filtered = df[df['Descrição'].isin(filter_values)].copy()

    df_filtered['text'] = df_filtered.apply(
        lambda row: f"{row['Descrição']}<br>R$ {row['Valor']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'),
        axis=1
    )

    fig = px.bar(
        df_filtered,
        y='Descrição',
        x='Valor',
        text='text',
        color='Valor',
        color_continuous_scale=["#0D3327", "#145A32", "#1E8449", "#239B56"],
        orientation='h'
    )

    fig.update_traces(
        textposition='inside',
        textfont=dict(color='white', size=14),
        hovertemplate='<b>%{y}</b><br>%{x:.2f} R$<extra></extra>'
    )

    fig.update_layout(coloraxis_showscale=False)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=16),
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        xaxis=dict(showticklabels=False, showgrid=True, gridcolor='rgba(255,255,255,0.1)', gridwidth=1, zeroline=False),
        margin=dict(l=20, r=20, t=60, b=40)
    )

    return dcc.Graph(figure=fig)

def criar_grafico4_ano22(file_path):
    # Carregar a planilha
    xls = pd.ExcelFile(file_path)
    
    # Carregar os dados da aba "Resumo Índices"
    df_resumo_indices = pd.read_excel(xls, sheet_name='Resumo Índices')

    # Limpeza dos dados
    df_resumo_indices_clean = df_resumo_indices.dropna(how="all", axis=0).reset_index(drop=True)
    df_resumo_indices_clean.columns = ['Descrição', 'Valor']
    df_resumo_indices_clean['Valor'] = pd.to_numeric(df_resumo_indices_clean['Valor'], errors='coerce')
    df_resumo_indices_clean = df_resumo_indices_clean.dropna(subset=['Valor'])

    # Filtrar apenas o valor de APLICAÇÃO FUNDEB 70%
    filter_values = ['APLICAÇÃO FUNDEB 70%']
    df_filtered = df_resumo_indices_clean[df_resumo_indices_clean['Descrição'].isin(filter_values)]

    fundeb_value = df_filtered['Valor'].values[0]
    value_percent = fundeb_value * 100
    limit = 70  # limite em 70%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",  # já inclui o número automaticamente
        value=value_percent,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},  # barra do meio transparente
            'steps': [
                {'range': [0, limit], 'color': '#82E0AA'},  # verde claro
                {'range': [limit, min(value_percent, 100)], 'color': '#F1948A'},  # vermelho claro para excesso
                {'range': [max(value_percent, limit), 100], 'color': 'lightgray'},
            ],
        },
        number={
            'suffix': '%',
            'valueformat': '.2f',  # formata com 2 casas decimais
            'font': {'size': 40, 'color': 'white'}
        },
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=16),
        margin=dict(l=40, r=40, t=100, b=100)
    )

    return dcc.Graph(figure=fig)

def criar_grafico5_ano22(file_path):
    # Carregar a planilha
    xls = pd.ExcelFile(file_path)
    
    # Carregar os dados da aba "Resumo Índices"
    df_resumo_indices = pd.read_excel(xls, sheet_name='Resumo Índices')

    # Limpeza dos dados
    df_resumo_indices_clean = df_resumo_indices.dropna(how="all", axis=0)
    df_resumo_indices_clean = df_resumo_indices_clean.reset_index(drop=True)

    df_resumo_indices_clean.columns = ['Descrição', 'Valor']
    df_resumo_indices_clean['Valor'] = pd.to_numeric(df_resumo_indices_clean['Valor'], errors='coerce')
    df_resumo_indices_clean = df_resumo_indices_clean.dropna(subset=['Valor'])

    # Filtrar apenas o valor de APLICAÇÃO FUNDEB 70%
    filter_values = ['APLICAÇÃO MDE FONTE 01 - (PERCENTUAL DA APLICAÇÃO PRÓPRIA)']
    df_filtered = df_resumo_indices_clean[df_resumo_indices_clean['Descrição'].isin(filter_values)]

    # Pegar o valor percentual de APLICAÇÃO FUNDEB 70%
    fundeb_value = df_filtered['Valor'].values[0]  # Valor percentual

    # Calcular o valor com 2 casas decimais e adicionar o símbolo '%'
    fundeb_value_percent = fundeb_value * 100
    fundeb_value_percent_text = f"{fundeb_value_percent:.2f}%"  # Exibe 2 casas decimais e o símbolo '%'

    # Criar o gráfico de gauge com o valor formatado corretamente
    fig = go.Figure(go.Indicator(
        mode="gauge",  # Adiciona o número no gráfico
        value=fundeb_value * 100,  # Multiplicar por 100 para exibir a porcentagem
        gauge={
            'axis': {'range': [0, 100]},  # Definir o intervalo de 0 a 100
            'bar': {'color': "green"},  # Cor da barra
            'steps': [
                {'range': [0, fundeb_value * 100], 'color': "#11492D"},  # Cor verde até o valor da porcentagem
                {'range': [fundeb_value * 100, 100], 'color': "lightgray"}  # Cor cinza para o restante
            ]
        },
        number = None, 
    ))

    # Adicionar o valor formatado ao centro do gráfico
    fig.update_layout(
        annotations=[{
            'text': fundeb_value_percent_text,  # Exibe o valor com 2 casas decimais e '%'
            'x': 0.5, 'y': 0.2, 'font': {'size': 40, 'color': 'white'},
            'showarrow': False
        }],
        plot_bgcolor='rgba(0,0,0,0)',  # Fundo transparente
        paper_bgcolor='rgba(0,0,0,0)', # Fundo externo transparente
        font=dict(color='white', size=16),
        margin=dict(l=40, r=40, t=100, b=100)
    )

    return dcc.Graph(figure=fig)


def criar_grafico6_ano22(file_path):
    # Carregar a planilha
    xls = pd.ExcelFile(file_path)
    
    # Carregar os dados da aba "Resumo Índices"
    df_resumo_indices = pd.read_excel(xls, sheet_name='Resumo Índices')

    # Limpeza dos dados
    df_resumo_indices_clean = df_resumo_indices.dropna(how="all", axis=0).reset_index(drop=True)
    df_resumo_indices_clean.columns = ['Descrição', 'Valor']
    df_resumo_indices_clean['Valor'] = pd.to_numeric(df_resumo_indices_clean['Valor'], errors='coerce')
    df_resumo_indices_clean = df_resumo_indices_clean.dropna(subset=['Valor'])

    # Filtrar apenas o valor desejado
    filter_values = ['APLICAÇÃO FUNDEB VAAT - EDUCAÇÃO INFANTIL - MINIMO DE 50%']
    df_filtered = df_resumo_indices_clean[df_resumo_indices_clean['Descrição'].isin(filter_values)]

    fundeb_value = df_filtered['Valor'].values[0]
    value_percent = fundeb_value * 100
    limit = 50

    fig = go.Figure(go.Indicator(
        mode="gauge+number",  # já inclui número
        value=value_percent,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': [
                {'range': [0, limit], 'color': '#82E0AA'},
                {'range': [limit, min(value_percent, 100)], 'color': '#F1948A'},
                {'range': [max(value_percent, limit), 100], 'color': 'lightgray'},
            ],
        },
        number={
            'suffix': '%',
            'valueformat': '.2f',  # formata com 2 casas decimais
            'font': {'size': 40, 'color': 'white'}
        },
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=16),
        margin=dict(l=40, r=40, t=100, b=100)
    )

    return dcc.Graph(figure=fig)

def criar_grafico7_ano22(file_path):
    import pandas as pd
    import plotly.express as px
    from dash import dcc

    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices').dropna(how="all").reset_index(drop=True)
    df.columns = ['Descrição', 'Valor']
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df = df.dropna(subset=['Valor'])
    filter_values = [
        'RECEITA CORRENTE LÍQUIDA',
        'DESPESA COM PESSOAL (ACUMULADO 12 MESES)',
    ]
    df_filtered = df[df['Descrição'].isin(filter_values)].copy()

    df_filtered['text'] = df_filtered.apply(
        lambda row: f"{row['Descrição']}<br>R$ {row['Valor']:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.'),
        axis=1
    )

    fig = px.bar(
        df_filtered,
        y='Descrição',
        x='Valor',
        text='text',
        color='Valor',
        color_continuous_scale=["#0D3327", "#145A32", "#1E8449", "#239B56"],
        orientation='h'
    )

    fig.update_traces(
        textposition='inside',
        textfont=dict(color='white', size=14),
        hovertemplate='<b>%{y}</b><br>%{x:.2f} R$<extra></extra>'
    )

    fig.update_layout(coloraxis_showscale=False)
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=16),
        yaxis=dict(showticklabels=False, showgrid=False, zeroline=False),
        xaxis=dict(showticklabels=False, showgrid=True, gridcolor='rgba(255,255,255,0.1)', gridwidth=1, zeroline=False),
        margin=dict(l=20, r=20, t=60, b=40)
    )

    return dcc.Graph(figure=fig)

def criar_grafico8_ano22(file_path):
    # Carregar a planilha
    xls = pd.ExcelFile(file_path)
    
    # Carregar os dados da aba "Resumo Índices"
    df_resumo_indices = pd.read_excel(xls, sheet_name='Resumo Índices')

    # Limpeza dos dados
    df_resumo_indices_clean = df_resumo_indices.dropna(how="all", axis=0).reset_index(drop=True)
    df_resumo_indices_clean.columns = ['Descrição', 'Valor']
    df_resumo_indices_clean['Valor'] = pd.to_numeric(df_resumo_indices_clean['Valor'], errors='coerce')
    df_resumo_indices_clean = df_resumo_indices_clean.dropna(subset=['Valor'])

    filter_values = ['% APURADO NOS ULTIMOS 12 MESES']
    df_filtered = df_resumo_indices_clean[df_resumo_indices_clean['Descrição'].isin(filter_values)]

    fundeb_value = df_filtered['Valor'].values[0]
    value_percent = fundeb_value * 100
    limit = 54  # limite em 54%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value_percent,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},  # barra do meio transparente
            'steps': [
                {'range': [0, limit], 'color': '#82E0AA'},  # verde claro
                {'range': [limit, min(value_percent, 100)], 'color': '#F1948A'},  # vermelho claro para excesso
                {'range': [max(value_percent, limit), 100], 'color': 'lightgray'},
            ],
        },
        number={
            'suffix': '%',
            'valueformat': '.2f',
            'font': {'size': 40, 'color': 'white'}
        }
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=16),
        margin=dict(l=40, r=40, t=100, b=100)
    )

    return dcc.Graph(figure=fig)

def criar_grafico9_ano22(file_path):
    # Carregar a planilha
    xls = pd.ExcelFile(file_path)

    # Carregar os dados da aba "Resumo Índices"
    df_resumo_indices = pd.read_excel(xls, sheet_name='Resumo Índices')

    # Limpeza dos dados
    df_resumo_indices_clean = df_resumo_indices.dropna(how="all", axis=0).reset_index(drop=True)
    df_resumo_indices_clean.columns = ['Descrição', 'Valor']
    df_resumo_indices_clean['Descrição'] = df_resumo_indices_clean['Descrição'].astype(str).str.strip()
    df_resumo_indices_clean['Valor'] = pd.to_numeric(df_resumo_indices_clean['Valor'], errors='coerce')
    df_resumo_indices_clean = df_resumo_indices_clean.dropna(subset=['Valor'])

    df_filtered = df_resumo_indices_clean[
        df_resumo_indices_clean['Descrição'].str.contains(
            "PERCENTUAL DE APLICAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE",
            case=False, na=False
        )
    ]

    if df_filtered.empty:
        return html.Div("Dado não encontrado para o gráfico 9.")

    fundeb_value = df_filtered['Valor'].values[0]
    value_percent = fundeb_value * 100
    limit = 7  # limite em 7%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value_percent,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},  # barra do meio transparente
            'steps': [
                {'range': [0, limit], 'color': '#82E0AA'},  # verde claro
                {'range': [limit, min(value_percent, 100)], 'color': '#F1948A'},  # vermelho claro para excesso
                {'range': [max(value_percent, limit), 100], 'color': 'lightgray'},
            ],
        },
        number={
            'suffix': '%',
            'valueformat': '.2f',
            'font': {'size': 40, 'color': 'white'}
        }
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=16),
        margin=dict(l=40, r=40, t=100, b=100)
    )

    return dcc.Graph(figure=fig)

def criar_grafico10_ano22(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    df = df.dropna(how="all", axis=0).reset_index(drop=True)
    df.columns = ['Descrição', 'Valor']
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df = df.dropna(subset=['Valor'])

    filtro = df['Descrição'].str.strip() == 'APLICAÇÃO FUNDEB VAAT - DESPESA CAPITAL - MÍNIMO DE 15%'
    df_filtrado = df[filtro]

    if df_filtrado.empty:
        return html.Div("Dado não encontrado para o gráfico 10.")

    valor = df_filtrado['Valor'].values[0]
    valor_percent = valor * 100
    limit = 15  # limite em 15%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",  # mostra número formatado automaticamente
        value=valor_percent,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},  # barra do meio transparente
            'steps': [
                {'range': [0, limit], 'color': '#82E0AA'},  # verde claro
                {'range': [limit, min(valor_percent, 100)], 'color': '#F1948A'},  # vermelho claro para excesso
                {'range': [max(valor_percent, limit), 100], 'color': 'lightgray'},
            ],
        },
        number={
            'suffix': '%',
            'valueformat': '.2f',  # formato com 2 casas decimais
            'font': {'size': 40, 'color': 'white'}
        },
    ))

    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='white', size=16),
        margin=dict(l=40, r=40, t=100, b=100)
    )

    return dcc.Graph(figure=fig)

ano22_layout = html.Div([
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("Índices Constitucionais e Legais", className="card-title"),
            criar_grafico1_ano22("dataset/ACOMPANHAMENTO ITARANTIM 2022.xlsx")
        ]), className="grafico-card"), width=4),

        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("Despesa Total em Aplicações na Educação", className="card-title"),
            criar_grafico2_ano22("dataset/ACOMPANHAMENTO ITARANTIM 2022.xlsx")
        ]), className="grafico-card"), width=4),

        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("Apuração em Saúde", className="card-title"),
            criar_grafico3_ano22("dataset/ACOMPANHAMENTO ITARANTIM 2022.xlsx")
        ]), className="grafico-card"), width=4),
    ]),

    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("APURAÇÃO FUNDEB E EDUCAÇÃO", className="card-title mb-4"),
            dbc.Row([
        dbc.Col([
            html.H6("APLICAÇÃO FUNDEB 70%", className="card-title"),
            criar_grafico4_ano22("dataset/ACOMPANHAMENTO ITARANTIM 2022.xlsx")
        ], width=3),

        dbc.Col([
        html.H6("APURAÇÃO MDE FONTE 01", className="card-title"),
        criar_grafico5_ano22("dataset/ACOMPANHAMENTO ITARANTIM 2022.xlsx")
        ], width=3),

        dbc.Col([
            html.H6("APLICAÇÃO EDUCAÇÃO 50%", className="card-title"),
            criar_grafico6_ano22("dataset/ACOMPANHAMENTO ITARANTIM 2022.xlsx")
        ], width=3),

        dbc.Col([
            html.H6("APLICAÇÃO CAPITAL 15%", className="card-title"),
            criar_grafico10_ano22("dataset/ACOMPANHAMENTO ITARANTIM 2022.xlsx")
        ], width=3),
    ])

        ]), className="grafico-card-trio"), width=12),
    ]),
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("APURAÇÃO LIMITE DESPESA COM PESSOAL", className="card-title mb-4"),
            dbc.Row([
                dbc.Col([
                    html.H6("RECEITA CORRENTE LÍQUIDA", className="card-title"),
                    criar_grafico7_ano22("dataset/ACOMPANHAMENTO ITARANTIM 2022.xlsx")
                ], width=6),

                dbc.Col([
                    html.H6("DESPESA COM PESSOAL 54%", className="card-title"),
                    criar_grafico8_ano22("dataset/ACOMPANHAMENTO ITARANTIM 2022.xlsx")
                ], width=6),
            ])
        ]), className="grafico-card-dupla"), width=8),

        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("PERCENTUAL DE APLICAÇÃO EM AÇÕES E SERVIÇOS PÚBLICOS DE SAÚDE 7%", className="card-title"),
            criar_grafico9_ano22("dataset/ACOMPANHAMENTO ITARANTIM 2022.xlsx")
        ]), className="grafico-card-9"), width=4),
    ]),
])  

