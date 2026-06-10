### Exercícios de Funções.

# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# Resposta:
# lista_de_numeros: list[int] = [5, 3, 8, 2]


# def somar_numeros(lista_de_numeros):
#     # Começar com um acumulador em 0.
#     total = 0

#     # Olhar número por número (repetição).
#     for numero in lista_de_numeros:
#         # Atualizar o total acumulado o número atual.
#         total += numero

#     # Devolver o resultado final.
#     return total


# resultado = somar_numeros(lista_de_numeros)
# print(f"O resultado da soma dos números da lista é: {resultado}.")

# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
# Resposta:
# numero: int = int(input("Digite um número e descubra se é um número primo: "))


# def descobrir_primo(numero):
#     if numero <= 1:
#         return False
#     if numero == 2:
#         return True

#     for divisor in range(2, numero):
#         if numero % divisor == 0:
#             return False

#     return True


# print(f"Resultado: ", descobrir_primo(numero))

# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# Resposta:

# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.
