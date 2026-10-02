# Funções
# Procedimentos
# Parâmetros, Argumentos e Retornos


def imprimir_itens(lista):
    for item in lista:
        print(item)


l1 = [1, 2, 3, 4, 5, 6]
imprimir_itens(l1)
print()

l2 = ["Luiza", "Luciano", "Caio", "Michelle"]
imprimir_itens(l2)
print()

l3 = [12, "Luiza", 2512.24, True]
imprimir_itens(l3)
print()


def mostrar_inicio_processamento(numero_pedido: int) -> None:
    """
    Mostrar na tela o início do processamento de um pedido.
    """
    print(f"Iniciando processamento do pedido #{numero_pedido}...")


def calcular_total(preco: float, quantidade: int, desconto: float) -> float:
    """
    Calcular o valor final de um item após aplicar o desconto.

    Args:
        preco (float): Preço unitário do produto.
        quantidade (int): Quantidade comprada.
        desconto (float): Percentual de desconto em formato decimal.

    Returns:
        float: Valor final da compra
    """
    subtotal: float = preco * quantidade
    valor_desconto: float = subtotal * desconto
    total: float = subtotal - valor_desconto

    print(
        f"O valor total é de R$ {subtotal:.2f} e o desconto de R$ {valor_desconto:.2f}."
    )
    return total


def registrar_processamento(numero_pedido: int, valor: float) -> None:
    """
    Exibe uma confirmação do processamento do pedido.

    Args:
        numero_pedido (int): Identificador do pedido (id).
        valor (float): Valor final do produto.
    """
    print(f"Pedido #{numero_pedido} processado com valor de R$ {valor:.2f}.")


numero_pedido: int = 1058
mostrar_inicio_processamento(numero_pedido)

valor_final = calcular_total(preco=89.90, quantidade=3, desconto=0.10)

registrar_processamento(numero_pedido, valor_final)
