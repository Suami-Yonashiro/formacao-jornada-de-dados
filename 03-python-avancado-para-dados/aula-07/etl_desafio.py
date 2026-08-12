import csv
from typing import Dict, List

path_arquivo = "vendas.csv"


def ler_csv(nome_arquivo: str) -> List[Dict[str, str]]:
    """Abre um arquivo CSV e converte suas linhas em uma lista
    de dicionários.

    Args:
        nome_arquivo: O caminho ou o nome do arquivo CSV a ser lido.

    Returns:
        Uma lista de dicionários, onde cada dicionário representa
        uma linha do arquivo com as chaves baseadas no cabeçalho.
    """
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        return list(leitor)


def processar_dados(dados: List[Dict[str, str]]) -> Dict[str, List[Dict[str, str]]]:
    """Agrupa os registros de produtos brutos baseando-se em sua
    categoria.

    Args:
        dados: Uma lista de dicionários contendo os dados dos produtos
        lidos do CSV.

    Returns:
        Um dicionário onde as chaves são os nomes das categorias e os
        valores são listas contenco produtos pertecentes a cada categoria.
    """
    categorias: Dict[str, List[Dict[str, str]]] = {}
    for item in dados:
        categoria = item["Categoria"]
        if categoria not in categorias:
            categorias[categoria] = []
        categorias[categoria].append(item)
    return categorias


def calcular_vendas_categoria(dados: Dict[str, List[Dict[str, str]]]) -> Dict[str, int]:
    """Calcula o faturamento total acumulado para cada categoria
    de produto.
    Realiza a operação matemática multiplicando a quantidade vendida
    pelo valor unitário de cada item e somando os resultados por setor.

    Args:
        dados: O dicionário de categorias estrutura pela função 'processar_dados'.

    Returns:
        Um dicionário onde cada chave é a categoria e o valor é o total faturado.
    """
    vendas_por_categoria: Dict[str, int] = {}
    for categoria, itens in dados.items():
        total_vendas = sum(
            int(item["Quantidade"]) * int(item["Venda"]) for item in itens
        )
        vendas_por_categoria[categoria] = total_vendas
    return vendas_por_categoria


def main() -> None:
    """Função principal que gerencia o fluxo de execução do script.

    Coordena as etapas de leitura do arquivo 'vendas.csv', agrupamento
    dos setores e exibição dos resultados consolidados na tela.
    """
    nome_arquivo = "vendas.csv"
    dados_brutos = ler_csv(nome_arquivo)
    dados_processados = processar_dados(dados_brutos)
    vendas_categoria = calcular_vendas_categoria(dados_processados)

    print("--- Total de Vendas por categoria ---")
    for categoria, total in vendas_categoria.items():
        print(f"{categoria}: ${total:,}")


if __name__ == "__main__":
    main()
