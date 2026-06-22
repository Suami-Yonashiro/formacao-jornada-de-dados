from csv import reader
from collections import defaultdict
import time
from pathlib import Path

def processar_temperaturas(path_do_txt: Path):
    """Processar um arquivo de temperaturas acumulando estatísticas por estação.
    
    Essa função lê um arquivo de texto contendo registros de estações meteorológicas
    e suas respectivas temperaturas. Ela utilizar uma abordagem de streaming para 
    calcular os valores mínimo, máximo e média de cada estação em tempo real, 
    garantindo baixo consumo de memória RAM. 

    Args:
        path_do_txt (Path): O caminho do objeto Path que aponta para o arquivo
        de medições (ex. 'data/measurements.text').

    Returns:
        _type_: dict: Um dicionário ordenado alfabeticamente onde as chaves são
        nomes das estações e os valores strings formatadas como 'mínimo/média/máximo'.
        Exemplo: {'Lisboa': '12.4/22.1/34.0'}
        
    Raises:
        FileNotFoundError: Se o arquivo no caminho especificado não for encontrado. 
    """
    print("Iniciando o processamento do arquivo.")
    start_time = time.time()  # Tempo de início
    
    # ALTERAÇÃO 1: O dicionário guarda um dicionário interno com o "estado" da cidade
    # Em vez de uma lista gigante de números, guardamos apenas o resumo.
    estatisticas_por_station = defaultdict(lambda: {"min": float('inf'), "max": float('-inf'), "soma": 0.0, "qtd": 0})

    with open(path_do_txt, 'r', encoding="utf-8") as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            nome_da_station, temperatura = str(row[0]), float(row[1])
            
            # ALTERAÇÃO 2: Atualizamos os valores EM TEMPO REAL enquanto lemos a linha
            stats = estatisticas_por_station[nome_da_station]
            
            if temperatura < stats["min"]:
                stats["min"] = temperatura
            if temperatura > stats["max"]:
                stats["max"] = temperatura
                
            stats["soma"] += temperatura
            stats["qtd"] += 1

    print("Dados carregados. Calculando médias finais...")

    # Dicionário para armazenar os resultados calculados
    results = {}
    
    # ALTERAÇÃO 3: O laço de cálculo ficou mais leve e rápido
    for station, stats in estatisticas_por_station.items():
        min_temp = stats["min"]
        max_temp = stats["max"]
        # A média é calculada dividindo a soma acumulada pela quantidade acumulada
        mean_temp = stats["soma"] / stats["qtd"]

        results[station] = (min_temp, mean_temp, max_temp)

    print("Estatística calculada. Ordenando...")
    # Ordenando os resultados pelo nome da estação
    sorted_results = dict(sorted(results.items()))

    # Formatando os resultados para exibição
    formatted_results = {station: f"{min_temp:.1f}/{mean_temp:.1f}/{max_temp:.1f}" for station, (min_temp, mean_temp, max_temp) in sorted_results.items()}

    end_time = time.time()  # Tempo de término
    print(f"Processamento concluído em {end_time - start_time:.2f} segundos.")

    return formatted_results

# Substitua "data/measurements10M.txt" pelo caminho correto do seu arquivo
if __name__ == "__main__":

    # 1M 0.88 segundos
    path_do_txt: Path = Path("data/measurements.txt")
    resultados = processar_temperaturas(path_do_txt)