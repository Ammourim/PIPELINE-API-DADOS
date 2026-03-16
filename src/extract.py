import requests
from dotenv import load_dotenv #para importar as credenciais no arquivo .env
import os

load_dotenv() #carregando as credenciais do arquivo .env

def buscar_campeonatos():
    url = "https://sofascore.p.rapidapi.com/tournaments/list?categoryId=1"
    api_key= os.getenv('RAPID_API_KEY')
    api_host= os.getenv('RAPID_API_HOST')

    headers = {
	 "x-rapidapi-host":api_host,
	 "x-rapidapi-key":api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f'Erro na extracao:{response.status_code}')
        return None


if __name__ == "__main__":
    dados = buscar_campeonatos()
    if dados:
        print("Conexão bem-sucedida!")
        # Vamos ver apenas o primeiro grupo de campeonatos para não encher a tela
        print(dados.get('groups')[0] if 'groups' in dados else "Dados não encontrados")