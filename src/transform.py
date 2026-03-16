import pandas as pd

def limpar_campeonatos(dados):
    if 'groups' in dados:
        lista_bruta = dados['groups'][0]['uniqueTournaments']
        df = pd.json_normalize(lista_bruta, sep='_')
        colunas_selecionadas = ['id', 'name', 'category_name']
        df_filtrado = df[colunas_selecionadas]
        return df_filtrado
    return None