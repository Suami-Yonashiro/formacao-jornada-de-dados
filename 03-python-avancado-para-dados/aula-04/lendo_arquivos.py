import csv

# Caminho para o arquivo CSV.
caminho_do_arquivo: str = "exemplo.csv"

# Inicializa uma lista vazia para armazenar os dados.
arquivo_csv: list = []

# Usa o gerenciador de contexto 'with' para abrir e fechar o arquivo
# com o término da função.
with open(file=caminho_do_arquivo, mode="r", encoding="utf-8") as arquivo:
    # Cria um objeto leitor de CSV.
    leitor_csv = csv.DictReader(arquivo)

    # Converte cada linha do CSV para um dicionário e adiciona à lista.
    for linha in leitor_csv:
        arquivo_csv.append(linha)

# Exibe os dados lidos do arquivo CSV.
print(arquivo_csv)
