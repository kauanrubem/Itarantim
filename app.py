import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import datetime

from _components.inicial import inicial_layout
from _components.mes21 import criar_graficos_mes21
from _components.mes22 import criar_graficos_mes22
from _components.mes23 import criar_graficos_mes23
from _components.mes24 import criar_graficos_mes24

# Mapeamento dos nomes de mês em inglês para português
mapa_meses = {
    'JANUARY':   'JANEIRO',
    'FEBRUARY':  'FEVEREIRO',
    'MARCH':     'MARÇO',
    'APRIL':     'ABRIL',
    'MAY':       'MAIO',
    'JUNE':      'JUNHO',
    'JULY':      'JULHO',
    'AUGUST':    'AGOSTO',
    'SEPTEMBER': 'SETEMBRO',
    'OCTOBER':   'OUTUBRO',
    'NOVEMBER':  'NOVEMBRO',
    'DECEMBER':  'DEZEMBRO'
}

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

app.title = "Apuração de Dados Itarantim"
app._favicon = "itarantim-logo (1).ico"  # Define o favicon do aplicativo

app.layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(inicial_layout, width=12),
        ]),
        html.Div(id="ano21-container")
    ], fluid=True)
])

@app.callback(
    Output('ano21-container', 'children'),
    [
        Input('main_variable', 'start_date'),
        Input('main_variable', 'end_date')
    ]
)
def update_graph(start_date, end_date):
    if not start_date or not end_date:
        return html.Div("Selecione um intervalo de datas válido.")

    # Converte strings para datetime
    start = datetime.datetime.strptime(start_date[:10], '%Y-%m-%d')
    end   = datetime.datetime.strptime(end_date[:10], '%Y-%m-%d')

    # Gera lista de primeiro dia de cada mês no intervalo
    meses = []
    current = start.replace(day=1)
    end_month = end.replace(day=1)
    while current <= end_month:
        meses.append(current)
        if current.month == 12:
            current = current.replace(year=current.year + 1, month=1)
        else:
            current = current.replace(month=current.month + 1)

    # Traduz para nomes em português
    meses_str = [mapa_meses[dt.strftime('%B').upper()] for dt in meses]
    anos_selecionados = sorted({dt.year for dt in meses})

    containers = []
    # Se abranger mais de um ano, renderiza seção por ano
    if len(anos_selecionados) > 1:
        for ano in anos_selecionados:
            meses_ano     = [m for m in meses if m.year == ano]
            meses_ano_str = [mapa_meses[m.strftime('%B').upper()] for m in meses_ano]

            if str(ano) == '2021':
                graficos = criar_graficos_mes21(f"dataset/ACOMPANHAMENTO ITARANTIM {ano}.xlsx", meses_ano_str)
            elif str(ano) == '2022':
                graficos = criar_graficos_mes22(f"dataset/ACOMPANHAMENTO ITARANTIM {ano}.xlsx", meses_ano_str)
            elif str(ano) == '2023':
                graficos = criar_graficos_mes23(f"dataset/ACOMPANHAMENTO ITARANTIM {ano}.xlsx", meses_ano_str)
            elif str(ano) == '2024':
                graficos = criar_graficos_mes24(f"dataset/ACOMPANHAMENTO ITARANTIM {ano} (1).xlsx", meses_ano_str)
            else:
                graficos = html.Div(f"Visualização mensal para {ano} não disponível.")

            containers.append(html.Div([
                html.H4(
                    f"Total acumulado de {meses_ano_str[0]} até {meses_ano_str[-1]} de {ano}",
                    style={"color": "black", "margin": "20px 0"}
                ),
                graficos
            ], style={'margin-bottom': '40px'}))

        return html.Div(containers)

    # Caso seja somente um ano
    ano = str(anos_selecionados[0])
    if ano == '2021':
        graficos = criar_graficos_mes21(f"dataset/ACOMPANHAMENTO ITARANTIM {ano}.xlsx", meses_str)
    elif ano == '2022':
        graficos = criar_graficos_mes22(f"dataset/ACOMPANHAMENTO ITARANTIM {ano}.xlsx", meses_str)
    elif ano == '2023':
        graficos = criar_graficos_mes23(f"dataset/ACOMPANHAMENTO ITARANTIM {ano}.xlsx", meses_str)
    elif ano == '2024':
        graficos = criar_graficos_mes24(f"dataset/ACOMPANHAMENTO ITARANTIM {ano} (1).xlsx", meses_str)
    else:
        graficos = html.Div(f"Visualização mensal para {ano} não disponível.")

    return html.Div([
        html.H4(
            f"Total acumulado de {meses_str[0]} até {meses_str[-1]} de {ano}",
            style={"color": "black", "margin": "20px 0"}
        ),
        graficos
    ])

if __name__ == '__main__':
    app.run(debug=True)
