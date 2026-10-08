# Argumento posicional.


# def cadastrar_produto(nome: str, preco: float, estoque: int) -> None:
#     print(f"Produto: {nome}")
#     print(f"Preço: R$ {preco:.2f}")
#     print(f"Estoque: {estoque} unidades")


# cadastrar_produto("Teclado", 150.00, 20)


# # Argumento nomeado.
# cadastrar_produto(nome="Mouse", preco=200.50, estoque=50)

# # Parâmetros com valores padrão.
# def cadastrar_produto_vp( nome: str, preco: float, estoque: int = 0, ativo: bool = True) -> None:
#     print(f"Produto: {nome}")
#     print(f"Preço: R$ {preco:.2f}")
#     print(f"Estoque: {estoque}")
#     print(f"Ativo: {ativo}")


# cadastrar_produto_vp("Fone de Ouvido", 300.00, estoque = 50, ativo = False)

# # *args
# def calcular_total_modo_raiz(valor1: float, valor2: float, valor3: float) -> float:
#     return valor1 + valor2 + valor3


# total_raiz = calcular_total_modo_raiz(89.9, 200.0, 510.0)
# print(total_raiz)

# def calcular_total(*valores: float) -> float:
#     print(valores)
#     return sum(valores)


# total = calcular_total(89.9, 200.0, 510.0, 731.21, 922.20)
# print(f"{total:.2f}")

# def mostrar_produtos(*produtos: str) -> None:
#     print(produtos)


# mostrar_produtos("Teclado", "Fone de Ouvido", "Mouse")


def calcular_total_pedido(*valores: float) -> float:
    total = 0

    for valor in valores:
        total += valor

    return total
