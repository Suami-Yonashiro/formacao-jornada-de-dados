import polars as pl
import time
from pathlib import Path

FILENAME = Path("data/measurements.txt")

# Polars, created by Koen Vossen, 
# Github: https://github.com/koenvo
# Twitter/x Handle: https://twitter.com/mr_le_fox
# https://x.com/mr_le_fox/status/1741893400947839362?s=20

def criar_dataframe_polars(path_do_txt: Path):
    """Processar arquivo usando o motor de streaming otimizado do Polars."""
    # Define o tamanho do bloco para esteira de streaming 
    pl.Config.set_streaming_chunk_size(1000000)
    
    # pl.scan_csv inicia o modo "lazy". Ele apenas scaneia a estrutura do arquivo.
    return (
        pl.scan_csv(
            path_do_txt,
            separator=";",
            has_header=False,
            new_columns=["station", "measure"],
            # Lemos tudo inicialmente como string para não quebrar a leitura
            schema={"station": pl.String, "measure": pl.String},
            encoding="utf8-lossy",
        )
        # Tratamento explícito da coluna: Substitui ',' por '.' se necessário e converte para Float64
        .with_columns(
            pl.col("measure").str.replace(",", ".").cast(pl.Float64)
        ) 
        .group_by("station")
        .agg(
            max = pl.col("measure").max(),
            min = pl.col("measure").min(),
            mean = pl.col("measure").mean()
        )
        .sort("station")
        # O .collect(streaming=True) é o gatilho que liga os motores em Rust para processar
        .collect(engine="streaming")
    )

if __name__ == "__main__":
    # 1M 0.11 segundos
    print("Iniciando a execução do script com Polars...") 
    start_time = time.time()
    
    if not FILENAME.exists():
        print("Erro: O arquivo {FILENAME} não foi localizado.")
        exit()
        
    df = criar_dataframe_polars(FILENAME)
    took = time.time() - start_time
    
    print("\n--- Resultados Finais (Polars) ---")
    print(df.head())
    print(f"\nPolars concluído em: {took:.2f} segundos.")