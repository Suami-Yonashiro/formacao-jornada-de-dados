### Exercícios de Listas e Dicionários resolvidos.

# 1. Lista de números ao quadrado. 
# Reposta:
numeros: list[int] = list(range(0, 11))
for numero in numeros:
    quadrado = numero**2
    print(f"O quadrado de:\n{numero} = {quadrado}")

# 2.

# 3. Informações de um livro. Crie um dicionário para armazenar informações de um livro. 
# from typing import Dict, Any
# livro: dict[str, Any] = {
#     "Titulo": "Game of Thrones A Guerra dos Tronos",
#     "Autor": "George R. R. Martin",
#     "Ano": 1996, 
# }
# for chave, valor in livro.items():
#     print(f"{chave}: {valor}") 