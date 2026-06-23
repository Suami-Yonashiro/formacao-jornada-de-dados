from csv import reader
from collections import defaultdict, Counter
from tqdm import tqdm  # barra de progresso
import time
from pathlib import Path

# 1M como padrão seguro para testes locais rápidos
NUMERO_DE_LINHAS = 1_000_000

def processar_temperaturas(path_do_txt: Path) -> dict:
    """Processa dados meteorológicos em streaming exibindo uma barra de progresso.
    
    Lê um arquivo CSV linha por linha e computa de forma otimizada os valores mínimo, 
    máximo e a média de temperatura para cada estação meteorológica, utilizando a 
    biblioteca tqdm para feedback visual de progresso.

    Args:
        path_do_txt (Path): Caminho para o arquivo contendo os dados.

    Returns:
        dict: Dicionário ordenado com as estatísticas formatadas por estação.
    """
    # Centralizado em uma única estrutura para evitar múltiplos lookups na memória
    estatisticas = defaultdict(lambda: {"min": float('inf'), "max": float('-inf'), "soma": 0.0, "qtd": 0})

    with open(path_do_txt, 'r', encoding="utf-8") as file:
        _reader = reader(file, delimiter=';')
        # tqdm encapsula o iterador para renderizar a barra de progresso
        for row in tqdm(_reader, total=NUMERO_DE_LINHAS, desc="Processando"):
            nome_da_station, temperatura = str(row[0]), float(row[1])
            
            stats = estatisticas[nome_da_station]
            
            # Comparações diretas via if são ligeiramente mais rápidas em loops massivos do que min()/max()
            if temperatura < stats["min"]:
                stats["min"] = temperatura
            if temperatura > stats["max"]:
                stats["max"] = temperatura
                
            stats["soma"] += temperatura
            stats["qtd"] += 1
            
    print("Dados carregados. Calculando estatísticas...")

    # Calculando min, média e max para cada estação
    results = {}
    for station, stats in estatisticas.items():
        mean_temp = stats["soma"] / stats["qtd"]
        results[station] = (stats["min"], mean_temp, stats["max"])

    print("Estatística calculada. Ordenando...")
    # Ordena os resultados pelo nome da estação
    sorted_results = dict(sorted(results.items()))

    # Formata os resultados para exibição
    return {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}"
            for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}


if __name__ == "__main__":
    path_do_txt = Path("data/measurements.txt")

    print("Iniciando o processamento do arquivo.")
    start_time = time.time()  # Tempo de início

    resultados = processar_temperaturas(path_do_txt)

    end_time = time.time()  # Tempo de término

    for station, metrics in resultados.items():
        print(station, metrics, sep=': ')

    print(f"\nProcessamento concluído em {end_time - start_time:.2f} segundos.")
    
# Resultados:
# 1 milhão 1.10 segundos
# 10 milhões 12.39 segundos
# 100 milhões 218.75 segundos