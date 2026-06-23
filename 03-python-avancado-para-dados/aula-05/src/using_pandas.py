""" Metodologia:
  1. Leitura em Chunks: O arquivo é lido em pedaços (chunks) para não
     sobrecarregar a memória RAM, permitindo o processamento de arquivos
     maiores que a memória disponível.
  2. Processamento Paralelo (Multiprocessing): Cada chunk é distribuído
     para um processo separado (worker), utilizando todos os núcleos de
     CPU disponíveis para máxima performance.
  3. Agregação em Duas Fases:
     a. Parcial: Cada worker calcula estatísticas intermediárias (min,
        max, soma, contagem) para o seu chunk.
     b. Final: O processo principal coleta os resultados parciais e
        realiza a agregação final para obter os valores globais corretos.

Otimizações Chave:
  - Cálculo Correto da Média: Utiliza 'soma' e 'contagem' para evitar o
    erro matemático da "média das médias".
  - Eficiência de Memória: Especificação de `dtypes` e uso de
    `pool.imap_unordered` para minimizar o consumo de memória de pico.
  - Performance de Leitura: O uso de `dtype='category'` para a coluna de
    estações acelera drasticamente a leitura e o processamento do arquivo.

Uso:
  - Configure as constantes `FILENAME` e `CHUNKSIZE` conforme necessário.
  - Execute o script diretamente a partir de um terminal: `python seu_scri
"""

import pandas as pd
from multiprocessing import Pool, cpu_count
import time
from pathlib import Path

# --- Constantes de Configuração ---
# Define o caminho para o arquivo de dados
FILENAME = Path("data/measurements.txt")

# Define o tamanho de cada "pedaço" do arquivo a ser lido na memória
# Reduzir para 1 milhão para evitar que múltiplos processos estourem a RAM do seu PC de uma vez
CHUNKSIZE = 1_000_000

# Otimização: Especificar os tipos de dados acelera a leitura e economiza memória.
COLUMN_TYPES = {
    'station': 'category',
    'measure': 'float32'
}

def process_chunk(chunk: pd.DataFrame) -> pd.DataFrame:
    """Processa um único chunk de dados para agregação estatística parcial."""
    # Agregação crucial: calcular 'sum' e 'count' para podermos derivar a média correta posteriormente
    # Adicionado `observed=True` para remover o FUTUTREWARNING e adotar o comportamento mais moderno e eficiente
    return chunk.groupby('station', observed=True)['measure'].agg(['min', 'max', 'sum', 'count']).reset_index()

def process_file_in_parallel(filename: Path, chunksize: int) -> pd.DataFrame:
    """Orquestra a leitura concorrente do arquivo e unifica as agregações.
    
    Args:
        filename (Path): Objeto Path apontando para o arquivo de medições.
        chunksize (int): Quantidade de linhas por bloco processado.
        
    Returns:
        pd.DataFrame: DataFrame final ordenado contendo as estatísticas globais.
    """
    print(f"Iniciando o processamento paralelo com {cpu_count()} núcleos de CPU...")

    with Pool(cpu_count()) as pool:
      # CORREÇÃO: Adicionado encoding="utf-8" para evitar falhas no Windows
        with pd.read_csv(
            filename,
            sep=';',
            header=None,
            names=['station', 'measure'],
            chunksize=chunksize,
            dtype=COLUMN_TYPES,
            encoding="utf-8"
        ) as reader:
            intermediate_results = list(pool.imap_unordered(process_chunk, reader))

    print("Agrupando e consolidando os resultados finais...")
    final_df = pd.concat(intermediate_results, ignore_index=True)
    
    # Na agregação final, usamos `observed=False` para garantir que todas as categorias,
    # mesmo que ausentes em alguns chunks, sejam consideradas.
    # No entanto, como concatenamos tudo antes, o comportamento é o mesmo e não gera warning.
    final_aggregated = final_df.groupby('station', observed=False).agg(
        min_measure=('min', 'min'),
        max_measure=('max', 'max'),
        total_sum=('sum', 'sum'),
        total_count=('count', 'sum')
    ).reset_index()

    final_aggregated['mean_measure'] = final_aggregated['total_sum'] / final_aggregated['total_count']
    
    result_df = final_aggregated[['station', 'min_measure', 'mean_measure', 'max_measure']]
    return result_df.sort_values('station')

# --- Ponto de Entrada do Script ---
if __name__ == "__main__":
    print("Iniciando a execução do script com Pandas...")
    start_time = time.time()
    
    # Executa apenas se o arquivo existir para evitar crashes feios
    if not FILENAME.exists():
      print(f"Erro: O arquivo {FILENAME} não foi localizado. Certifique-se de gerá-lo primeiro.")
      exit()
      
    final_dataframe = process_file_in_parallel(FILENAME, CHUNKSIZE)
    took = time.time() - start_time
    
    print("\n--- Processamento concluído! ---")
    print(final_dataframe.head())
    print(f"\nPandas paralelizado levou: {took:.2f} segundos.")
    
# Resultados:
# 1 milhão 1.05 segundos
# 10 milhões 3.84 segundos
# 100 milhões 45.08 segundos