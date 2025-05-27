from dash import dcc, html
import dash_bootstrap_components as dbc
from dash import dcc, html
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def criar_grafico1_ano24(file_path):
    import pandas as pd
    import plotly.express as px
    from dash import dcc

    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices').dropna(how="all").reset_index(drop=True)
    df = df.iloc[:, :2]
    df.columns = ['Descrição', 'Valor']
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df = df.dropna(subset=['Valor'])
    filter_values = [
        'RECEITA CORRENTE LÍQUIDA DE 2024',
        'RECEITA CORRENTE LÍQUIDA ACUMULADA ÚLTIMOS 12 MESES',
        'RECEITAS DE IMPOSTOS E TRANSFERÊNCIAS DE IMPOSTOS',
        'RECEITAS DO FUNDEB (IMPOSTOS E COMPLEMENTAÇÃO)'
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

def criar_grafico2_ano24(file_path):
    import pandas as pd
    import plotly.express as px
    from dash import dcc

    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices').dropna(how="all").reset_index(drop=True)
    df = df.iloc[:, :2]
    df.columns = ['Descrição', 'Valor']
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df = df.dropna(subset=['Valor'])
    filter_values = [
        'FUNDEB - APLICAÇÃO 70%',
        'FUNDEB - APLICAÇÃO 30%',
        'FUNDEB VAAT - EDUCAÇÃO INFANTIL - MINIMO DE 50,41%',
        'FUNDEB VAAT - DESPESA CAPITAL - MÍNIMO DE 15%'
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

def criar_grafico3_ano24(file_path):
    # Carregar a planilha e aba
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    # Limpar linhas vazias
    df = df.dropna(how='all').reset_index(drop=True)

    # Selecionar as colunas: Descrição (0) e Percentual (2)
    df_filtered = df.iloc[:, [0, 2]]
    df_filtered.columns = ['Descrição', 'Percentual']

    # Limpar strings e converter para número, tratando erros
    df_filtered['Percentual'] = pd.to_numeric(
        df_filtered['Percentual'].astype(str).str.replace('%', '').str.replace(',', '.'), 
        errors='coerce'
    )

    # Remover linhas sem percentual válido
    df_filtered = df_filtered.dropna(subset=['Percentual'])

    # Filtrar a linha do FUNDEB - APLICAÇÃO 70%
    fundeb_row = df_filtered[df_filtered['Descrição'] == 'FUNDEB - APLICAÇÃO 70%']

    if fundeb_row.empty:
        fundeb_value = 0
    else:
        fundeb_value = fundeb_row['Percentual'].values[0] * 100

    limit = 70  # limite em 70%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fundeb_value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': [
                {'range': [0, limit], 'color': '#82E0AA'},        # verde claro faixa fundo
                {'range': [limit, min(fundeb_value, 100)], 'color': '#F1948A'},  # vermelho claro faixa excesso
                {'range': [max(fundeb_value, limit), 100], 'color': 'lightgray'},
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

def criar_grafico4_ano24(file_path):
    # Carregar a planilha e aba
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    # Limpar linhas vazias
    df = df.dropna(how='all').reset_index(drop=True)

    # Selecionar as colunas: Descrição (0) e Percentual (2)
    df_filtered = df.iloc[:, [0, 2]]
    df_filtered.columns = ['Descrição', 'Percentual']

    # Limpar strings e converter para número, tratando erros
    df_filtered['Percentual'] = pd.to_numeric(
        df_filtered['Percentual'].astype(str).str.replace('%', '').str.replace(',', '.'), 
        errors='coerce'
    )

    # Remover linhas sem percentual válido
    df_filtered = df_filtered.dropna(subset=['Percentual'])

    # Filtrar a linha do FUNDEB - APLICAÇÃO 30%
    fundeb_row = df_filtered[df_filtered['Descrição'] == 'FUNDEB - APLICAÇÃO 30%']

    if fundeb_row.empty:
        fundeb_value = 0
    else:
        fundeb_value = fundeb_row['Percentual'].values[0] * 100

    limit = 30  # limite em 30%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fundeb_value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},  # barra do meio transparente
            'steps': [
                {'range': [0, limit], 'color': '#82E0AA'},        # verde claro faixa fundo
                {'range': [limit, min(fundeb_value, 100)], 'color': '#F1948A'},  # vermelho claro faixa excesso
                {'range': [max(fundeb_value, limit), 100], 'color': 'lightgray'},
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

def criar_grafico5_ano24(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    df = df.dropna(how='all').reset_index(drop=True)

    df_filtered = df.iloc[:, [0, 2]]
    df_filtered.columns = ['Descrição', 'Percentual']

    df_filtered['Percentual'] = pd.to_numeric(
        df_filtered['Percentual'].astype(str).str.replace('%', '').str.replace(',', '.'), 
        errors='coerce'
    )

    df_filtered = df_filtered.dropna(subset=['Percentual'])

    fundeb_row = df_filtered[df_filtered['Descrição'] == 'FUNDEB VAAT - EDUCAÇÃO INFANTIL - MINIMO DE 50,41%']

    if fundeb_row.empty:
        fundeb_value = 0
    else:
        fundeb_value = fundeb_row['Percentual'].values[0] * 100

    limit = 50.41  # limite em 50,41%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fundeb_value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': [
                {'range': [0, limit], 'color': '#11492D'},        # verde escuro faixa fundo
                {'range': [limit, min(fundeb_value, 100)], 'color': '#F1948A'},  # vermelho claro faixa excesso
                {'range': [max(fundeb_value, limit), 100], 'color': 'lightgray'},
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

def criar_grafico6_ano24(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    df = df.dropna(how='all').reset_index(drop=True)

    df_filtered = df.iloc[:, [0, 2]]
    df_filtered.columns = ['Descrição', 'Percentual']

    df_filtered['Percentual'] = pd.to_numeric(
        df_filtered['Percentual'].astype(str).str.replace('%', '').str.replace(',', '.'), 
        errors='coerce'
    )

    df_filtered = df_filtered.dropna(subset=['Percentual'])

    fundeb_row = df_filtered[df_filtered['Descrição'] == 'FUNDEB VAAT - DESPESA CAPITAL - MÍNIMO DE 15%']

    if fundeb_row.empty:
        fundeb_value = 0
    else:
        fundeb_value = fundeb_row['Percentual'].values[0] * 100

    limit = 15  # limite corrigido para 15%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fundeb_value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': [
                {'range': [0, limit], 'color': '#0d3327'},        # verde escuro faixa fundo
                {'range': [limit, min(fundeb_value, 100)], 'color': '#F1948A'},  # vermelho claro faixa excesso
                {'range': [max(fundeb_value, limit), 100], 'color': 'lightgray'},
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

def criar_grafico7_ano24(file_path):
    import pandas as pd
    import plotly.express as px
    from dash import dcc

    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices').dropna(how="all").reset_index(drop=True)
    df = df.iloc[:, :2]
    df.columns = ['Descrição', 'Valor']
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df = df.dropna(subset=['Valor'])
    filter_values = [
        'VALOR DESTINADO AO FUNDEB (20%)',
        'VALOR APLICADO COM RECURSO PRÓPRIO DA EDUCAÇÃO (5%)',
        'DESPESAS PARA FINS DE LIMITE MÍNIMO DOS 25%'
    ]
    df_filtered = df[df['Descrição'].isin(filter_values)].copy()
    df_filtered = df_filtered.drop_duplicates(subset=['Descrição'])

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
def criar_grafico8_ano24(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    df = df.dropna(how='all').reset_index(drop=True)

    df_filtered = df.iloc[:, [0, 2]]
    df_filtered.columns = ['Descrição', 'Percentual']

    df_filtered['Percentual'] = pd.to_numeric(
        df_filtered['Percentual'].astype(str).str.replace('%', '').str.replace(',', '.'), 
        errors='coerce'
    )

    df_filtered = df_filtered.dropna(subset=['Percentual'])

    fundeb_row = df_filtered[df_filtered['Descrição'] == 'VALOR DESTINADO AO FUNDEB (20%)']

    if fundeb_row.empty:
        fundeb_value = 0
    else:
        fundeb_value = fundeb_row['Percentual'].values[0] * 100

    limit = 25  # limite corrigido para 25%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fundeb_value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': [
                {'range': [0, limit], 'color': '#0d3327'},        # verde escuro faixa fundo
                {'range': [limit, min(fundeb_value, 100)], 'color': '#F1948A'},  # vermelho claro faixa excesso
                {'range': [max(fundeb_value, limit), 100], 'color': 'lightgray'},
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

def criar_grafico9_ano24(file_path):
    import pandas as pd
    import plotly.express as px
    from dash import dcc

    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices').dropna(how="all").reset_index(drop=True)
    df = df.iloc[:, :2]
    df.columns = ['Descrição', 'Valor']
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df = df.dropna(subset=['Valor'])
    filter_values = [
        'TOTAL DAS DESPEAS COM SAÚDE',
        'VALOR EXCEDENTE AO LIMITE MÍNIMO CONSTITUCIONAL'
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

def criar_grafico10_ano24(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    df = df.dropna(how='all').reset_index(drop=True)

    df_filtered = df.iloc[:, [0, 2]]
    df_filtered.columns = ['Descrição', 'Percentual']

    df_filtered['Percentual'] = pd.to_numeric(
        df_filtered['Percentual'].astype(str).str.replace('%', '').str.replace(',', '.'), 
        errors='coerce'
    )

    df_filtered = df_filtered.dropna(subset=['Percentual'])

    fundeb_row = df_filtered[df_filtered['Descrição'] == 'TOTAL DAS DESPEAS COM SAÚDE']

    if fundeb_row.empty:
        fundeb_value = 0
    else:
        fundeb_value = fundeb_row['Percentual'].values[0] * 100

    limit = 15  # limite em 15%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fundeb_value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': [
                {'range': [0, limit], 'color': '#176739'},        # verde escuro faixa fundo
                {'range': [limit, min(fundeb_value, 100)], 'color': '#F1948A'},  # vermelho claro faixa excesso
                {'range': [max(fundeb_value, limit), 100], 'color': 'lightgray'},
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

def criar_grafico11_ano24(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    df = df.dropna(how='all').reset_index(drop=True)

    df_filtered = df.iloc[:, [0, 2]]
    df_filtered.columns = ['Descrição', 'Percentual']

    df_filtered['Percentual'] = pd.to_numeric(
        df_filtered['Percentual'].astype(str).str.replace('%', '').str.replace(',', '.'), 
        errors='coerce'
    )

    df_filtered = df_filtered.dropna(subset=['Percentual'])

    fundeb_row = df_filtered[df_filtered['Descrição'] == 'VALOR EXCEDENTE AO LIMITE MÍNIMO CONSTITUCIONAL']

    if fundeb_row.empty:
        fundeb_value = 0
    else:
        fundeb_value = fundeb_row['Percentual'].values[0] * 100

    limit = 15  # limite em 15%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fundeb_value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': [
                {'range': [0, limit], 'color': '#176739'},        # verde escuro faixa fundo
                {'range': [limit, min(fundeb_value, 100)], 'color': '#F1948A'},  # vermelho claro faixa excesso
                {'range': [max(fundeb_value, limit), 100], 'color': 'lightgray'},
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

def criar_grafico12_ano24(file_path):
    import pandas as pd
    import plotly.express as px
    from dash import dcc

    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices').dropna(how="all").reset_index(drop=True)
    df = df.iloc[:, :2]
    df.columns = ['Descrição', 'Valor']
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df = df.dropna(subset=['Valor'])
    filter_values = [
        'DESPESA COM PESSOAL SOMENTE DO EXERCÍCIO DE 2024',
        'DESPESA COM PESSOAL (ACUMULADO ÚLTIMOS 12 MESES)'
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

def criar_grafico13_ano24(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    df = df.dropna(how='all').reset_index(drop=True)

    df_filtered = df.iloc[:, [0, 2]]
    df_filtered.columns = ['Descrição', 'Percentual']

    df_filtered['Percentual'] = pd.to_numeric(
        df_filtered['Percentual'].astype(str).str.replace('%', '').str.replace(',', '.'), 
        errors='coerce'
    )

    df_filtered = df_filtered.dropna(subset=['Percentual'])

    fundeb_row = df_filtered[df_filtered['Descrição'] == 'DESPESA COM PESSOAL SOMENTE DO EXERCÍCIO DE 2024']

    if fundeb_row.empty:
        fundeb_value = 0
    else:
        fundeb_value = fundeb_row['Percentual'].values[0] * 100

    limit = 54  # limite em 54%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fundeb_value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': [
                {'range': [0, limit], 'color': '#176739'},        # verde escuro faixa fundo
                {'range': [limit, min(fundeb_value, 100)], 'color': '#F1948A'},  # vermelho claro faixa excesso
                {'range': [max(fundeb_value, limit), 100], 'color': 'lightgray'},
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

def criar_grafico14_ano24(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    df = df.dropna(how='all').reset_index(drop=True)

    df_filtered = df.iloc[:, [0, 2]]
    df_filtered.columns = ['Descrição', 'Percentual']

    df_filtered['Percentual'] = pd.to_numeric(
        df_filtered['Percentual'].astype(str).str.replace('%', '').str.replace(',', '.'), 
        errors='coerce'
    )

    df_filtered = df_filtered.dropna(subset=['Percentual'])

    fundeb_row = df_filtered[df_filtered['Descrição'] == 'DESPESA COM PESSOAL (ACUMULADO ÚLTIMOS 12 MESES)']

    if fundeb_row.empty:
        fundeb_value = 0
    else:
        fundeb_value = fundeb_row['Percentual'].values[0] * 100

    limit = 54  # limite em 54%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fundeb_value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': [
                {'range': [0, limit], 'color': '#176739'},        # verde escuro faixa fundo
                {'range': [limit, min(fundeb_value, 100)], 'color': '#F1948A'},  # vermelho claro faixa excesso
                {'range': [max(fundeb_value, limit), 100], 'color': 'lightgray'},
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

def criar_grafico15_ano24(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    df = df.dropna(how='all').reset_index(drop=True)

    df_filtered = df.iloc[:, [0, 2]]
    df_filtered.columns = ['Descrição', 'Percentual']

    df_filtered['Percentual'] = pd.to_numeric(
        df_filtered['Percentual'].astype(str).str.replace('%', '').str.replace(',', '.'), 
        errors='coerce'
    )

    df_filtered = df_filtered.dropna(subset=['Percentual'])

    fundeb_row = df_filtered[df_filtered['Descrição'] == 'DESPESA COM PESSOAL, EXCLUINDO RECEITA DO PRECATÓRIO DO FUNDEF']

    if fundeb_row.empty:
        fundeb_value = 0
    else:
        fundeb_value = fundeb_row['Percentual'].values[0] * 100

    limit = 54  # limite em 54%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fundeb_value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': [
                {'range': [0, limit], 'color': '#176739'},        # verde escuro faixa fundo
                {'range': [limit, min(fundeb_value, 100)], 'color': '#F1948A'},  # vermelho claro faixa excesso
                {'range': [max(fundeb_value, limit), 100], 'color': 'lightgray'},
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

def criar_grafico16_ano24(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    df = df.dropna(how='all').reset_index(drop=True)

    df_filtered = df.iloc[:, [0, 2]]
    df_filtered.columns = ['Descrição', 'Percentual']

    df_filtered['Percentual'] = pd.to_numeric(
        df_filtered['Percentual'].astype(str).str.replace('%', '').str.replace(',', '.'), 
        errors='coerce'
    )

    df_filtered = df_filtered.dropna(subset=['Percentual'])

    fundeb_row = df_filtered[df_filtered['Descrição'] == 'VALOR MÍNIMO A SER APLICADO']

    if fundeb_row.empty:
        fundeb_value = 0
    else:
        fundeb_value = fundeb_row['Percentual'].values[0] * 100

    limit = 5  # limite em 5%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fundeb_value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': [
                {'range': [0, limit], 'color': '#176739'},        # verde escuro faixa fundo
                {'range': [limit, min(fundeb_value, 100)], 'color': '#F1948A'},  # vermelho claro faixa excesso
                {'range': [max(fundeb_value, limit), 100], 'color': 'lightgray'},
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

def criar_grafico17_ano24(file_path):
    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices')

    df = df.dropna(how='all').reset_index(drop=True)

    df_filtered = df.iloc[:, [0, 2]]
    df_filtered.columns = ['Descrição', 'Percentual']

    df_filtered['Percentual'] = pd.to_numeric(
        df_filtered['Percentual'].astype(str).str.replace('%', '').str.replace(',', '.'), 
        errors='coerce'
    )

    df_filtered = df_filtered.dropna(subset=['Percentual'])

    fundeb_row = df_filtered[df_filtered['Descrição'] == 'VALOR APLICADO COM RECURSO PRÓPRIO DA EDUCAÇÃO (5%)']

    if fundeb_row.empty:
        fundeb_value = 0
    else:
        fundeb_value = fundeb_row['Percentual'].values[0] * 100

    limit = 5  # limite em 5%

    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fundeb_value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': 'rgba(0,0,0,0)'},
            'steps': [
                {'range': [0, limit], 'color': '#176739'},        # verde escuro faixa fundo
                {'range': [limit, min(fundeb_value, 100)], 'color': '#F1948A'},  # vermelho claro faixa excesso
                {'range': [max(fundeb_value, limit), 100], 'color': 'lightgray'},
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

def criar_grafico18_ano24(file_path):
    import pandas as pd
    import plotly.express as px
    from dash import dcc

    xls = pd.ExcelFile(file_path)
    df = pd.read_excel(xls, sheet_name='Resumo Índices').dropna(how="all").reset_index(drop=True)
    df = df.iloc[:, :2]
    df.columns = ['Descrição', 'Valor']
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    df = df.dropna(subset=['Valor'])
    filter_values = [
        'VALOR MÍNIMO A SER APLICADO',
        'VALOR APLICADO COM RECURSO PRÓPRIO DA EDUCAÇÃO (5%)',
        'DÉFICIT DA APLICAÇÃO EM EDUCAÇÃO (NECESSÁRIO APLICAR)'
    ]
    df_filtered = df[df['Descrição'].isin(filter_values)].copy()
    df_filtered = df_filtered.drop_duplicates(subset=['Descrição'])

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

ano24_layout = html.Div([
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("RECEITAS PARA FINS DE APURAÇÕES DOS ÍNDICES", className="card-title"),
            criar_grafico1_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
        ]), className="grafico-card"), width=3),

        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("APLICAÇÕES DO FUNDEB", className="card-title"),
            criar_grafico2_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
        ]), className="grafico-card"), width=3),

        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("APLICAÇÃO EM SAÚDE", className="card-title"),
            criar_grafico9_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
        ]), className="grafico-card"), width=3),

        dbc.Col(dbc.Card(dbc.CardBody([
            html.H6("DESPESA COM PESSOAL", className="card-title"),
            criar_grafico12_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
        ]), className="grafico-card"), width=3),
    ]),

    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("APLICAÇÕES DO FUNDEB", className="card-title mb-4"),
            dbc.Row([
                dbc.Col([
                    html.H6("FUNDEB - APLICAÇÃO 70%", className="card-title-meio"),
                    criar_grafico3_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=3),

                dbc.Col([
                    html.H6("FUNDEB - APLICAÇÃO 30%", className="card-title-meio"),
                    criar_grafico4_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=3),

                dbc.Col([
                    html.H6("FUNDEB VAAT - EDUCAÇÃO INFANTIL - MINIMO DE 50,41%", className="card-title-meio"),
                    criar_grafico5_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=3),

                dbc.Col([
                    html.H6("FUNDEB VAAT - DESPESA CAPITAL - MÍNIMO DE 15%", className="card-title-meio"),
                    criar_grafico6_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=3),
            ])
        ]), className="grafico-card-trio"), width=12),
    ]),
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("APLICAÇÃO DA EDUCAÇÃO MÍNIMO 25%", className="card-title mb-4"),
            dbc.Row([
                dbc.Col([
                    criar_grafico7_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=6),

                dbc.Col([
                    criar_grafico8_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=6),
            ])
        ]), className="grafico-card-dupla"), width=12),

        dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("APLICAÇÃO EM SAÚDE (MÍNIMO 15%)", className="card-title mb-4"),
            dbc.Row([
                dbc.Col([
                    criar_grafico10_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=6),

                dbc.Col([
                    criar_grafico11_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=6),
                ])
            ]), className="grafico-card-dupla"), width=12),
        ]),

        dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("DESPESA COM PESSOAL (LIMITE MÁXIMO 54%)", className="card-title mb-4"),
            dbc.Row([
                dbc.Col([
                    criar_grafico13_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=4),

                dbc.Col([
                    criar_grafico14_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=4),

                dbc.Col([
                    criar_grafico15_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=4),
                ])
            ]), className="grafico-card-dupla"), width=12),
        ]),

        dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("APLICAÇÃO DA EDUCAÇÃO RECURSO PRÓPRIO (5%)", className="card-title mb-4"),
            dbc.Row([
                dbc.Col([
                    criar_grafico16_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=4),

                dbc.Col([
                    criar_grafico17_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=4),

                dbc.Col([
                    criar_grafico18_ano24("dataset/ACOMPANHAMENTO ITARANTIM 2024.xlsx")
                ], width=4),
                ])
            ]), className="grafico-card-dupla"), width=12),
        ]),
    ])  
])

meses24_layout = html.Div([

])