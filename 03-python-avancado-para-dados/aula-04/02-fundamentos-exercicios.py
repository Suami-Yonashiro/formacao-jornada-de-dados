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


def exibir_produto(produto: str, preco: float) -> None:
    """
    Recebe o nome do produto, o preço e exibir essas informações formatadas.

    Args:
        produto (str): Nome do produto.
        preco (float): Preço unitário do produto.
    """
    print(f"Produto: {produto} | Preço: R$ {preco:.2f}")


exibir_produto("Teclado", 150.00)
