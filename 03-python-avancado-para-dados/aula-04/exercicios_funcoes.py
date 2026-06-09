### Exercícios de Funções.

# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
# Resposta:
lista_de_numeros: list[int] = [5, 3, 8, 2]


def somar_numeros(lista_de_numeros):
    # Começar com um acumulador em 0.
    total = 0

    # Olhar número por número (repetição).
    for numero in lista_de_numeros:
        # Atualizar o total acumulado o número atual.
        total += numero

    # Devolver o resultado final.
    return total


resultado = somar_numeros(lista_de_numeros)
print(f"O resultado da soma dos números da lista é: {resultado}.")

# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.
