# 1. Exibindo uma mensagem.
# Crie uma função chamada exibir_boas_vindas() que exiba a mensagem: Bem-vindo ao sistema!
# Depois, chame a função para executar a mensagem.
# Requisitos:
# Utilize def.
# A função não deve receber parâmetros.
# A função não precisa retornar nenhum valor.


# def exibir_boas_vindas() -> None:
#     """
#     Exibi mensagem de boas-vindas padrão no console.

#     Args:
#         mensagem (str):
#     """
#     print("Bem-vindo ao sistema!")


# exibir_boas_vindas()

# 2. Identificando um produto.
# Crie uma função chamada exibir_produto() que receba:
# o nome de um produto;
# o preço do produto.
# A função deve exibir uma mensagem no seguinte formato: Produto: Teclado | Preço: R$ 150.00
# Depois, chame a função passando um produto e um preço como argumentos.
# Requisitos:
# Utilize parâmetros.
# Adicione type hints nos parâmetros.
# A função deve retornar None.


# def exibir_produto(produto: str, preco: float) -> None:
#     """
#     Recebe o nome do produto, o preço e exibir essas informações formatadas.

#     Args:
#         produto (str): Nome do produto.
#         preco (float): Preço unitário do produto.
#     """
#     print(f"Produto: {produto} | Preço: R$ {preco:.2f}")


# exibir_produto("Teclado", 150.00)

# 3. Calculando o valor de uma compra.
# Crie uma função chamada calcular_total() que receba:
# o preço de um produto;
# a quantidade comprada.
# A função deve calcular e retornar o valor total da compra.
# Exemplo:
# total = calcular_total(50.0, 3)
# print(total)
# Resultado esperado: 150.0
# Requisitos:
# preco deve possuir type hint float.
# quantidade deve possuir type hint int.
# A função deve indicar que retorna um float.
# Utilize return para devolver o resultado.


# def calcular_total(preco: float, quantidade: int) -> float:
#     """
#     Recebe o preço de um produto, sua quantidade comprada e calcular o valor total.

#     Args:
#         preco (float): Preço unitário do produto.
#         quantidade (int): Quantidade unitária do produto.

#     Returns:
#         float: Valor final e total da compra.
#     """
#     total: float = preco * quantidade

#     return total


# total: float = calcular_total(50.0, 3)
# print(f"R$ {total:.2f}")

# 4. Calculando a média de avaliações.
# Uma plataforma armazena três avaliações dadas por usuários para um produto.
# Crie uma função chamada calcular_media_avaliacoes() que receba três notas e retorne a média entre elas.
# Depois, utilize o resultado retornado pela função para exibir a média das avaliações.
# Requisitos:
# Utilize parâmetros e argumentos.
# Adicione type hints.
# Utilize return.
# Adicione uma docstring explicando o que a função recebe e o que retorna.
# Guarde o resultado da função em uma variável antes de exibi-lo.


def calcular_media_avaliacoes(nota1: float, nota2: float, nota3: float) -> float:
    """
    Calcula a média das avaliações a partir de 3 notas.

    Args:
        nota1 (float): Primeira nota da avaliação.
        nota2 (float): Segunda nota da avaliação.
        nota3 (float): Terceira nota da avaliação.

    Returns:
        float: Média das notas das avaliações.
    """
    media: float = (nota1 + nota2 + nota3) / 3

    return media


media_final: float = calcular_media_avaliacoes(8.7, 3.5, 6.8)
print(f"A média das avaliações é: {media_final:.2f}")
