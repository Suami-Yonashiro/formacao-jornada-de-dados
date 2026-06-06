### Exercícios de Listas e Dicionários resolvidos.

from typing import Dict, Any

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
# lista_compras: list[str] = ["maçã", "banana", "cereja"]
# precos: dict[str, float] = {
#     "maçã": 0.45,
#     "banana": 0.30,
#     "cereja": 0.65
# }
# total: float = sum(precos[item] for item in lista_compras)
# print(f"O valor total da compra foi de R${total:.2f}.")

# 6. Eliminação de Duplicatas: Dada uma lista de emails, remover todos os duplicados.
# Resposta: 
# emails: list[str] = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
# emails_unicos = list(set(emails))
# print(f"Segue a lista limpa, sem e-mails duplicados: \n{emails_unicos}.")

# 7. Filtragem de Dados: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
# Resposta: 
# idades: list[int] = [22, 15, 30, 17, 18]
# idades_validas: list[int] = [idade for idade in idades if idade >= 18]
# print(f"Idades permitidas: {idades_validas}.")

# 8. Ordenação Personalizada: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
# Resposta:
# pessoas = [
#     {"nome": "Alice", "idade": 30},
#     {"nome": "Bob", "idade": 25},
#     {"nome": "Carol", "idade": 20}
# ]
# def ordenar_por_nome(lista_pessoas: list[Dict[str, Any]]) -> None:
#     """Ordenar uma lista de dicionários contendo dados pelo campo nome."""
#     lista_pessoas.sort(key=lambda pessoa: pessoa["nome"])
# ordenar_por_nome(pessoas)
# print(f"Dicionário ordenado por nome: \n{pessoas}.")

# 9. Agregação de Dados: Dado um conjunto de números, calcular a média.
# Resposta:
# numeros: list[int] = [10, 20, 30, 40, 50]
# media: int = sum(numeros) / len(numeros)
# print(f"A média dos números da lista é: {media}.")

# 10. Divisão de Dados em Grupos: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
# Resposta:
# valores: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# pares: list[int] = [par for par in valores if par % 2 == 0]
# impares: list[int] = [impar for impar in valores if impar % 2 != 0 ]
# print(f"Da lista valores os números pares são: {pares} \ne os números impares são: {impares}.")

# 11. Atualização de Dados: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
# Atualizar o preço do produto com id 2 para 90
# Resposta: 
# produtos: list[dict[str, Any]] = [
#     {"id": 1, "nome": "Teclado", "preço": 100},
#     {"id": 2, "nome": "Mouse", "preço": 80},
#     {"id": 3, "nome": "Monitor", "preço": 300}
# ]
# for produto in produtos:
#     if produto["id"] == 2:
#         produto["preço"] = 90 
#         break
# print(produtos)

# 12. Fusão de Dicionários: Dados dois dicionários, fundi-los em um único dicionário.
# Resposta: 
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}