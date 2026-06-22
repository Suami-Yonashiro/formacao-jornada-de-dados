import dask
import dask.dataframe as dd
import time
from pathlib import Path

# Constante de configuração robusta 
FILENAME = Path("data/measurements.txt")

def criar_dataframe_dask(path_do_txt: Path):
    """Configura o grafo de computação paralela do Dask para as temperaturas.
    Essa função não executa o cálculo imediatamente devido à natureza 'lazy' do
    Dask. Ela epenas mapeia como o arquivo será quebrado e processado.

    Args:
        path_do_txt (Path): Objeto Path apontado para o arquivo de medições.

    Returns:
        dask.dataframe.DataFrame: O objeto de computação tardia (lazy).
    """
    # Ativa o planejamento e otimização de queries na engine do Dask
    dask.config.set({'dataframe.query-planning': True})
    
    # Lendo o arquivo texto de forma particionada.
    # CORREÇÃO: Adicionado o encoding='utf-8' para blindar contra o padrão do Windows
    df = dd.read_csv(
        path_do_txt,
        sep=";",
        header=None,
        names=["station", "measure"],
        encoding="utf-8"
    )
    
    # Agrupando por 'station' e calculando o máximo, mínimo e média de 'measure'
    # O Dask realiza operações de forma lazy, então esta parte apenas define o cálculo
    grouped_df = df.groupby("station")['measure'].agg(['max', 'min', 'mean']).reset_index()

    # O Dask não suporta a ordenação direta de DataFrames agrupados/resultantes de forma eficiente
    # Mas você pode computar o resultado e então ordená-lo se o dataset resultante não for muito grande
    # ou se for essencial para a próxima etapa do processamento
    # A ordenação será realizada após a chamada de .compute(), se necessário
    return grouped_df

if __name__ == "__main__":
    # 1M 0.55 segundos
    print("Iniciando a execução do script com Dask...")
    start_time = time.time()
    
    if not FILENAME.exists():
        print(f"Erro: O arquivo {FILENAME} não foi localizado.")
        exit()
    
    # Constrói o plano de execução (rápido e sem uso de RAM)
    df_lazy = criar_dataframe_dask(FILENAME)
    
    print("Grafo de tarefas criado. Disparando os motores em paralelo (.compute())...")
    # O .compute() aciona todas as CPUs do seu PC para ler e processar os blocos de verdade  
    # O cálculo real e a ordenação são feitos aqui
    result_df = df_lazy.compute().sort_values("station")
    
    took = time.time() - start_time

    print("\n--- Resultados Finais (Dask) ---")
    print(result_df.head())
    print(f"\nDask otimizado levou: {took:.2f} segundos.")