from dash import dcc, html
import pandas as pd
import dash_bootstrap_components as dbc
import re

def limpar_titulo(t):
    return re.sub(r'^[\d\.\-\s]+', '', t).strip().upper()

def dedup_columns(cols):
    seen = {}
    result = []
    for col in cols:
        col_str = str(col)
        if col_str not in seen:
            seen[col_str] = 0
            result.append(col_str)
        else:
            seen[col_str] += 1
            result.append(f"{col_str}.{seen[col_str]}")
    return result

def formatar_valor_ptbr(valor):
    try:
        valor_float = float(valor)
    except:
        valor_float = 0
    return f"R$ {valor_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def criar_totalizador_card_texto(titulo, valor, percentual=False):
    if percentual:
        texto_valor = f"{valor * 100:.2f}%"
    else:
        texto_valor = formatar_valor_ptbr(valor)

    card = dbc.Card(
        dbc.CardBody([
            html.H5(titulo, className="card-title", style={"color": "#2C3E50", "fontWeight": "bold"}),
            html.H2(texto_valor, className="card-value", style={"color": "#E74C3C"})
        ]),
        className="totalizador-card",
        style={"textAlign": "center", "padding": "20px"}
    )
    return dbc.Col(card, width=4)

def criar_graficos_mes24(file_path, meses_selecionados):
    # --- Aba Receitas ---
    df = pd.read_excel(file_path, sheet_name="RECEITAS", header=None)

    header_row_index = None
    for i in range(len(df)):
        if df.iloc[i].astype(str).str.contains("JANEIRO", case=False).any():
            header_row_index = i
            break

    if header_row_index is None:
        return html.Div("Cabeçalho com meses não encontrado na aba Receitas.")

    df.columns = df.iloc[header_row_index]
    df = df[header_row_index + 1:].reset_index(drop=True)
    df.columns = df.columns.astype(str).str.strip().str.upper()
    df.rename(columns={df.columns[0]: 'CATEGORIA'}, inplace=True)
    df['CATEGORIA'] = df['CATEGORIA'].astype(str).str.strip().str.upper()

    meses_selecionados_upper = [mes.upper() for mes in meses_selecionados]
    meses_validos = [mes for mes in meses_selecionados_upper if mes in df.columns]

    categorias_exatas = {
        # Receitas
        "RCL AJUSTADA": "RCL AJUSTADA",
        "RECEITA CORRENTE LIQUIDA 12 MESES": "Despesa Líquida",
        "6- RECEITAS RECEBIDAS DO FUNDEB": "Receitas Recebidas do FUNDEB",
        "FUNDEB - APLICAÇÃO 70%": "FUNDEB - Aplicação 70%",
        "FUNDEB - APLICAÇÃO 30%": "FUNDEB - Aplicação 30%",
        "FUNDEB FR 1542.1070 (VAAT - EDUCAÇÃO INFANTIL)": "FUNDEB VAAT 1070 - EDUCAÇÃO INFANTIL",
        "FUNDEB FR 1542 (VAAT - EDUCAÇÃO INFANTIL)": "FUNDEB VAAT - EDUCAÇÃO INFANTIL",
        "FUNDEB FR 1542 (VAAT - DESPESA CAPITAL)": "FUNDEB VAAT - DESPESA CAPITAL",
        "5- VALOR MÍNIMO A SER APLICADO ALÉM DO VALOR DESTINADO AO FUNDEB - 5% DE ((2.2) + (2.3) + (2.4) + (2.5)) + 25% DE ((1.1) + (1.2) + (1.3) + (1.4) + (2.1.1) + (2.6)+ (2.7))": "Valor Mínimo a Ser Aplicado Além do Valor Destinado ao FUNDEB",
        # Despesas aba Receitas 
        "DESPESA BRUTA COM PESSOAL": "Despesa Bruta com Pessoal",
        "PERCENTUAL COM PESSOAL": "Percentual com Pessoal"
    }

    valores = {}
    for chave_planilha, titulo_limpo in categorias_exatas.items():
        linha = df[df['CATEGORIA'] == chave_planilha.upper()]
        if not linha.empty:
            soma = 0
            for mes in meses_validos:
                try:
                    soma += float(linha.iloc[0][mes])
                except:
                    pass
            valor_float = soma
        else:
            valor_float = 0
        valores[titulo_limpo] = valor_float

    # Soma para FUNDEB VAAT - Educação Infantil (soma das duas categorias)
    valor_fundeb_educ_infantil = valores.get("FUNDEB VAAT 1070 - EDUCAÇÃO INFANTIL", 0) + valores.get("FUNDEB VAAT - EDUCAÇÃO INFANTIL", 0)

    # --- Aba Despesas ---
    df_despesas = pd.read_excel(file_path, sheet_name="Despesas", header=None)

    header_row_index_despesas = None
    for i in range(len(df_despesas)):
        if df_despesas.iloc[i].astype(str).str.contains("JANEIRO", case=False).any():
            header_row_index_despesas = i
            break

    if header_row_index_despesas is None:
        return html.Div("Cabeçalho com meses não encontrado na aba Despesas.")

    df_despesas = df_despesas.iloc[header_row_index_despesas:].reset_index(drop=True)
    df_despesas.columns = dedup_columns(df_despesas.iloc[0])
    df_despesas = df_despesas[1:].reset_index(drop=True)

    df_despesas.rename(columns={df_despesas.columns[0]: 'CATEGORIA'}, inplace=True)
    df_despesas['CATEGORIA'] = df_despesas['CATEGORIA'].astype(str).str.strip().str.upper()

    despesas_desejadas = {
        "DESPESAS PAGAS DO FUNDEB": "Despesas Liquidadas do FUNDEB",
        "DESPESAS MDE": "Despesas MDE",
        "DESPESA TOTAL MDE": "Despesa Total MDE"
    }

    valores_despesas = {}
    for chave_planilha, titulo_limpo in despesas_desejadas.items():
        linha = df_despesas[df_despesas['CATEGORIA'] == chave_planilha.upper()]
        if not linha.empty:
            soma = 0
            for mes in meses_validos:
                try:
                    soma += float(linha.iloc[0][mes])
                except:
                    pass
            valor_float = soma
        else:
            valor_float = 0
        valores_despesas[titulo_limpo] = valor_float

    cards_originais = [
        criar_totalizador_card_texto("RCL Ajustada", valores.get("RCL AJUSTADA", 0)),
        criar_totalizador_card_texto("Despesa Líquida", valores.get("Despesa Líquida", 0)),
        criar_totalizador_card_texto("Receitas Recebidas do FUNDEB", valores.get("Receitas Recebidas do FUNDEB", 0))
    ]

    cards_extra_1 = [
        criar_totalizador_card_texto("FUNDEB - Aplicação 70%", valores.get("FUNDEB - Aplicação 70%", 0)),
        criar_totalizador_card_texto("FUNDEB - Aplicação 30%", valores.get("FUNDEB - Aplicação 30%", 0)),
        criar_totalizador_card_texto("FUNDEB VAAT - Educação Infantil - Mínimo 50,41%", valor_fundeb_educ_infantil)
    ]

    cards_extra_2 = [
        criar_totalizador_card_texto("FUNDEB VAAT - Despesa Capital - Mínimo 15%", valores.get("FUNDEB VAAT - DESPESA CAPITAL", 0)),
        criar_totalizador_card_texto("Valor Mínimo a Ser Aplicado Além FUNDEB", valores.get("Valor Mínimo a Ser Aplicado Além do Valor Destinado ao FUNDEB", 0)),
        criar_totalizador_card_texto("Receitas Recebidas do FUNDEB", valores.get("Receitas Recebidas do FUNDEB", 0))
    ]

    cards_despesas = [
        criar_totalizador_card_texto("Despesa Bruta com Pessoal", valores.get("Despesa Bruta com Pessoal", 0)),
        criar_totalizador_card_texto("Percentual com Pessoal", valores.get("Percentual com Pessoal", 0), percentual=True)
    ]

    cards_despesas_fun = [
        criar_totalizador_card_texto("Despesas Liquidadas do FUNDEB", valores_despesas.get("Despesas Liquidadas do FUNDEB", 0)),
        criar_totalizador_card_texto("Despesas MDE", valores_despesas.get("Despesas MDE", 0)),
        criar_totalizador_card_texto("Despesa Total MDE", valores_despesas.get("Despesa Total MDE", 0))
    ]

    return html.Div([
        html.H4("RECEITAS 2024", style={"color": "black", "margin": "20px 0"}),
        dbc.Row(cards_originais, className="g-2 mb-4"),

        html.H4("EDUCAÇÃO", style={"color": "black", "margin": "20px 0"}),
        dbc.Row(cards_extra_1, className="g-2 mb-3"),
        dbc.Row(cards_extra_2, className="g-2"),

        html.H4("DESPESAS E INDICADOR", style={"color": "black", "margin": "20px 0"}),
        dbc.Row(cards_despesas, className="g-2 mb-4", justify="start"),

        html.H4("DESPESAS FUNDEB E MDE", style={"color": "black", "margin": "20px 0"}),
        dbc.Row(cards_despesas_fun, className="g-2 mb-4", justify="start"),
    ])
