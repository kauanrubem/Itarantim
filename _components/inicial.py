import dash_bootstrap_components as dbc
from dash import html, dcc
import datetime

inicial_layout = dbc.Row([
    dbc.Col([
        dbc.Card([
            html.Div([
                html.Img(src="assets/itarantim - logo.png", className="img-itarantim"),
                html.H1("RESUMO DE ÍNDICES DOS MESES EM ITARANTIM", className="titulo"),
                html.Div([
                html.Img(
                    src='assets/calendário.png',
                    className='calendar-icon'
                ),
                dcc.DatePickerRange(
                id='main_variable',
                start_date=datetime.date.today().replace(month=1, day=1),
                end_date=datetime.date.today(),
                display_format='MMMM Y',
                minimum_nights=0,
                className='calendar-style'
            ),
        ], className='calendar-wrapper'),
                html.Img(src="assets/LOPES CONSULTORIA.png", className="img-lopes"),
            ], className="image-container"),
        ], className="fixed-radio-items"),
    ]),
])
