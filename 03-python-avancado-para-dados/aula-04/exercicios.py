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

# 4. Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
# Resposta: 
# def contar_caracteres(texto: str) -> dict:
#     contagem: dict = {}
#     for caractere in texto:
#         contagem[caractere] = contagem.get(caractere, 0) + 1
#     return contagem
# texto: str = (input("Digite um texto: "))
# resultado: dict[str, int] = contar_caracteres(texto)
# total_caracteres: int = len(texto)
# print(f"Contagem por caractere: {resultado}.")
# print(f"Contagem total de caracteres (incluindo espaços): {total_caracteres}.")

# 5. Dada a lista `["maçã", "banana", "cereja"]` e o dicionário `{"maçã": 0.45, "banana": 0.30, "cereja": 0.65}`, calcule o preço total da lista de compras.
# Resposta:
lista_compras: list[str] = ["maçã", "banana", "cereja"]
precos: dict[str, float] = {
    "maçã": 0.45,
    "banana": 0.30,
    "cereja": 0.65
}
total: float = sum(precos[item] for item in lista_compras)
print(f"O valor total da compra foi de R${total:.2f}.")

# 6. Eliminação de Duplicatas: Dada uma lista de emails, remover todos os duplicados.
# Resposta: 
emails: list[str] = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))
print(f"Segue a lista limpa, sem e-mails duplicados: \n{emails_unicos}.")
