from src.extract import buscar_campeonatos
from src.transform import limpar_campeonatos
from src.load import salvar_parquet

def executar_pipeline():
    print('Iniciando Pipeline...')

    dados_brutos = buscar_campeonatos()

    if dados_brutos:
        tabela_final = limpar_campeonatos(dados_brutos)

        if tabela_final is not None:
            print('Transformação concluída com sucesso.')  
            sucesso_carga = salvar_parquet(tabela_final, "campeonatos_ingleses")
        if sucesso_carga:
            print('Pipeline completo executado com sucesso!')
    else:
        print('Erro na extração. O Pipeline parou.')

if __name__ == "__main__":
    executar_pipeline()