# Argumento posicional.


def cadastrar_produto(nome: str, preco: float, estoque: int) -> None:
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque} unidades")


cadastrar_produto("Teclado", 150.00, 20)


# Argumento nomeado.
cadastrar_produto(nome="Mouse", preco=200.50, estoque=50)


# Parâmetros com valores padrão.
def cadastrar_produto_vp(
    nome: str, preco: float, estoque: int = 0, ativo: bool = True
) -> None:
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque}")
    print(f"Ativo: {ativo}")


cadastrar_produto_vp("Fone de Ouvido", 300.00, estoque=50, ativo=False)


# *args
def calcular_total_modo_raiz(valor1: float, valor2: float, valor3: float) -> float:
    return valor1 + valor2 + valor3


total_raiz = calcular_total_modo_raiz(89.9, 200.0, 510.0)
print(total_raiz)


def calcular_total(*valores: float) -> float:
    print(valores)
    return sum(valores)


total = calcular_total(89.9, 200.0, 510.0, 731.21, 922.20)
print(f"{total:.2f}")


def mostrar_produtos(*produtos: str) -> None:
    print(produtos)


mostrar_produtos("Teclado", "Fone de Ouvido", "Mouse")


def calcular_total_pedido(*valores: float) -> float:
    # total = 0
    print(valores)

    # for valor in valores:
    #     total += valor

    return sum(valores)


total = calcular_total_pedido(120.0, 89.9, 45.5, 199.9, 491.34)
print(f"Total do pedido: R${total:.2f}")

# Parâmetros normais + *args.


def registrar_pedido(numero_pedido: int, *produtos: str) -> None:
    print(f"Pedido: #{numero_pedido}")

    for produto in produtos:
        print(f"• {produto}")


registrar_pedido(1025, "Notebook", "Mouse", "Fone de ouvido")

# **kwargs

# def cadastrar_cliente(nome: str, email: str, telefone: str, cidade: str, estado: str): # substitui pelo **kwargs pois nem sempre todos os dados estarão disponiveis.


def cadastrar_cliente(**dados) -> None:
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")


cadastrar_cliente(nome="Luiza", email="luiza@élegal.com", cidade="Recife")

# Parâmetros normais + **kwargs.


def cadastrar_cliente(nome: str, email: str, **dados_adicionais) -> None:
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")

    for k, v in dados_adicionais.items():
        print(f"{k.capitalize()}: {v.capitalize()}")


cadastrar_cliente(
    nome="Luiza",
    email="luiza@élegal.com",
    cidade="Recife",
    estado="Pernambuco",
    profissao="Engenheira de Dados",
)

# *args + **kwargs juntos.


def registrar_venda(cliente: str, *produtos: str, **dados_adicionais) -> None:
    print(f"Cliente: {cliente}")

    print("\nProdutos: ")
    for produto in produtos:
        print(f"• {produto.capitalize()}")

    print("\nInformações da venda: ")
    for k, v in dados_adicionais.items():
        print(f"{k.capitalize()}: {v}")


registrar_venda(
    "Luiza",
    "Notebook",
    "Telefone",
    "Mouse",
    forma_pagamento="PIX",
    vendedor="Caio",
    entrega=True,
)
