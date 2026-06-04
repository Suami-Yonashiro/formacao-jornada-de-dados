### Exercícios de Listas e Dicionários resolvidos.

# 1. Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
# Reposta:
# numeros: list[int] = list(range(0, 11))
# for numero in numeros:
#     quadrado = numero**2
#     print(f"O quadrado de:\n{numero} = {quadrado}")

# 2. Dada a lista `["Python", "Java", "C++", "JavaScript"]`, remova o item "C++" e adicione "Ruby".
# Resposta: 
# linguagens: list[str] = ["Python", "Java", "C++", "JavaScript"]
# linguagens.remove("C++")
# linguagens.append("Ruby")
# print(linguagens)

# 3. Informações de um livro. Crie um dicionário para armazenar informações de um livro. 
# from typing import Dict, Any
# livro: dict[str, Any] = {
#     "Titulo": "Game of Thrones A Guerra dos Tronos",
#     "Autor": "George R. R. Martin",
#     "Ano": 1996, 
# }
# for chave, valor in livro.items():
#     print(f"{chave}: {valor}") 