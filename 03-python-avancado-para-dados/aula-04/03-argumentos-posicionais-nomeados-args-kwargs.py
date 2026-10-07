# Argumento posicional.


def cadastrar_produto(nome: str, preco: float, estoque: int) -> None:
    print(f"Produto: {nome}")
    print(f"Preço: R$ {preco:.2f}")
    print(f"Estoque: {estoque} unidades")


cadastrar_produto("Teclado", 150.00, 20)
