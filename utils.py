import pandas as pd
import requests
from io import BytesIO

def carregar_dados_2021(sheet_name='Resumo Índices'):
    file_id = "1fDsUmXXERZT5cp-sp6pxXQNxxSwPpDwH"  # ID correto da sua planilha
    url = f"https://drive.google.com/uc?export=download&id={file_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_excel(BytesIO(response.content), sheet_name=sheet_name, engine='openpyxl')
    else:
        raise Exception(f"Erro ao baixar planilha do Google Drive: {response.status_code}")

def carregar_dados_2022(sheet_name=''):
    file_id = ""  # ID correto da sua planilha
    url = f"={file_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_excel(BytesIO(response.content), sheet_name=sheet_name, engine='openpyxl')
    else:
        raise Exception(f"Erro ao baixar planilha do Google Drive: {response.status_code}")
    
def carregar_dados_2023(sheet_name=''):
    file_id = ""  # ID correto da sua planilha
    url = f"={file_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_excel(BytesIO(response.content), sheet_name=sheet_name, engine='openpyxl')
    else:
        raise Exception(f"Erro ao baixar planilha do Google Drive: {response.status_code}")

def carregar_dados_2024(sheet_name=''):
    file_id = ""  # ID correto da sua planilha
    url = f"={file_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return pd.read_excel(BytesIO(response.content), sheet_name=sheet_name, engine='openpyxl')
    else:
        raise Exception(f"Erro ao baixar planilha do Google Drive: {response.status_code}")