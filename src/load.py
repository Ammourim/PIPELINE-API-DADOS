import pandas as pd
import os

def salvar_parquet(df, campeonatos_ingleses):
    diretorio = "data"

    if not os.path.exists(diretorio):
        os.makedirs(diretorio)
        print(f"Pasta {diretorio} criada com sucesso.")

    caminho_completo = os.path.join(diretorio, f"{campeonatos_ingleses}.parquet")

    try:
        df.to_parquet(caminho_completo, index=False)
        return True
    except Exception as e:
        print(f"Erro: {e}")
        return False