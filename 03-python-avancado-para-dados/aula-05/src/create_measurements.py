import os
import sys
import random
import time


def check_args(file_args):
    """
    Valida os argumentos de entrada e exibe as instruções de uso
    caso a entrada não seja um número inteiro positivo.
    """
    try:
        if len(file_args) != 2 or int(file_args[1]) <= 0:
            raise ValueError()
    except (ValueError, IndexError):
        print(
            "Uso:  python script.py <número positivo de registros para criar>")
        print("        Você pode usar underscores para números grandes.")
        print("        Exemplo: 1_000_000_000 para um bilhão")
        exit()


def build_weather_station_name_list():
    """
    Coleta os nomes das estações meteorológicas e remove duplicatas
    """
    station_names = []
    with open('./data/weather_stations.csv', 'r', encoding="utf-8") as file:
        file_contents = file.read()
        
    for station in file_contents.splitlines():
        if "#" in station:
            continue
        else:
            station_names.append(station.split(';')[0])
    return list(set(station_names))


def convert_bytes(num):
    """
    Converte bytes para um formato legível (KiB, MiB, GiB)
    """
    for x in ['bytes', 'KiB', 'MiB', 'GiB']:
        if num < 1024.0:
            return "%3.1f %s" % (num, x)
        num /= 1024.0


def format_elapsed_time(seconds):
    """
    Formata o tempo decorrido
    """
    if seconds < 60:
        return f"{seconds:.3f} seconds"
    elif seconds < 3600:
        minutes, seconds = divmod(seconds, 60)
        return f"{int(minutes)} minutes {int(seconds)} seconds"
    else:
        hours, remainder = divmod(seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if minutes == 0:
            return f"{int(hours)} horas {int(seconds)} segundos"
        else:
            return f"{int(hours)} horas {int(minutes)} minutos {int(seconds)} segundos"


def estimate_file_size(weather_station_names, num_rows_to_create):
    """
    Estima o tamanho final do arquivo de teste
    """
    max_string = float('-inf')
    min_string = float('inf')

    for station in weather_station_names:
        if len(station) > max_string:
            max_string = len(station)
        if len(station) < min_string:
            min_string = len(station)
        
    per_record_size = ((max_string + min_string * 2) + len(",-123.4")) / 2

    total_file_size = num_rows_to_create * per_record_size
    human_file_size = convert_bytes(total_file_size)

    return f"O tamanho estimado do arquivo é:  {human_file_size}.\nO tamanho final será provavelmente muito menor (metade)."


def build_test_data(weather_station_names, num_rows_to_create):
    """
    Gera e escreve os dados de teste no arquivo em lotes
    """
    start_time = time.time()
    coldest_temp = -99.9
    hottest_temp = 99.9
    station_names_10k_max = random.choices(weather_station_names, k=10_000)
    
    # Em vez de escrever linha por linha em um arquivo, processe um lote de estações e grave-o em disco
    batch_size = 10000
    
    # Calcula quantos lotes equivalem a 1% do trabalho total
    total_batches = num_rows_to_create // batch_size
    progress_step = max(1, total_batches // 100)
    
    print(f'Criando o arquivo com {num_rows_to_create:,} linhas...')

    try:
        with open("./data/measurements.txt", 'w', encoding="utf-8") as file:
            for s in range(0, num_rows_to_create // batch_size):
                batch = random.choices(station_names_10k_max, k=batch_size)
                prepped_deviated_batch = '\n'.join(
                    [f"{station};{random.uniform(coldest_temp, hottest_temp):.1f}" for station in batch])
                file.write(prepped_deviated_batch + '\n')
                
                # IMPLEMENTAÇÃO DA BARRA: Atualiza a tela apenas a cada 'progress_step' (1%)
                if s % progress_step == 0:
                    percent_complete = (s / total_batches) * 100
                    # O '\r' joga o cursor do terminal pro início da linha
                    sys.stdout.write(f"\rProgresso: [{int(percent_complete)}%]")
                    sys.stdout.flush() # Força o terminal a renderizar o texto imediatamente

        # REATIVADO: Quebra a linha ao final para o próximo print não grudar na barra
        sys.stdout.write('\n')

    except Exception as e:
        print("Algo deu errado ao salvar o arquivo...")
        print(e)
        exit()

    end_time = time.time()
    elapsed_time = end_time - start_time
    file_size = os.path.getsize("./data/measurements.txt")
    human_file_size = convert_bytes(file_size)

    print("Arquivo escrito com sucesso data/measurements.txt")
    print(f"Tamanho final:  {human_file_size}")
    print(f"Tempo decorrido: {format_elapsed_time(elapsed_time)}")


def main():
    """
    Função principal que orquestra o programa
    """
    num_rows_to_create = 1_000_000
    
    if len(sys.argv) > 1:
        check_args(sys.argv)
        num_rows_to_create = int(sys.argv[1])
    
    weather_station_names = build_weather_station_name_list()
    print(estimate_file_size(weather_station_names, num_rows_to_create))
    build_test_data(weather_station_names, num_rows_to_create)
    print("Arquivo de teste finalizado.")


if __name__ == "__main__":
    main()