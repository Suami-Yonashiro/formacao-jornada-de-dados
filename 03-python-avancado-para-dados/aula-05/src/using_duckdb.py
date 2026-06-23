import duckdb
import time
from pathlib import Path

# Constante de configuração usando Path.
FILENAME = Path("data/measurements.txt")

def criar_relatorio_duckdb(path_do_txt: Path):
    """Executa a query analítica no DuckDB e retorna os dados estruturados."""
    
    # Usamos o as_posix() para garantir a barra do Windows '\' virem '/' no SQL
    query = f"""
        SELECT station,
            MIN(temperature) AS min_temperature,
            CAST(AVG(temperature) AS DECIMAL(3,1)) AS mean_temperature,
            MAX(temperature) AS max_temperature
        FROM read_csv('{path_do_txt.as_posix()}', AUTO_DETECT=FALSE, sep=';', header=FALSE, columns={{'station':'VARCHAR', 'temperature': 'FLOAT'}})
        GROUP BY station
        ORDER BY station
    """
    
    # Executa a query e transforma em DataFrame (permite reuso dos dados)
    return duckdb.sql(query).df()

if __name__ == "__main__":
    print("Iniciando a execução do script com DuckDB...")
    start_time = time.time()
    
    if not FILENAME.exists():
        print(f"Erro: O arquivo {FILENAME} não foi localizado.")
        exit()
        
    # Armazena o resultado na variável em vez de apenas printar na tela
    df_resultado = criar_relatorio_duckdb(FILENAME)
    
    # Exibe os dados de forma profissional
    print("\n-- Resultados (Primeiras Linhas) ---")
    print(df_resultado.head())
    
    took = time.time() - start_time
    print(f"\nDuckdb Otimizado levou: {took:.2f} segundos.")
    
# Resultados:
# 1 milhão 0.55 segundos
# 10 milhões 1.34 segundos
# 100 milhões 7.20 segundos