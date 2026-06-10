### Exercícios de Funções.

from typing import Any

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
# Resposta:
numero: int = int(input("Digite um número e descubra se é um número primo: "))


def descobrir_primo(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True

    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False

    return True


# print(f"Resultado: ", descobrir_primo(numero))

# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
# Resposta:
palavra: str = input("Digite uma palavra para recebe-la invertida: ")


def palavra_invertida(palavra: str) -> str:
    resultado_invertido = ""

    for letra in palavra:
        resultado_invertido = letra + resultado_invertido

    return resultado_invertido


print(f"O resultado da palavra {palavra} é {palavra_invertida(palavra)}.")

# Ou

palavra: str = input("Digite uma palavra para recebe-la invertida: ")


def palavra_invertida(palavra: str) -> str:
    return palavra[::-1]


print(f"O resultado da palavra {palavra} é {palavra_invertida(palavra)}.")

# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
# Resposta:
numeros: list[int] = [2, 4, 3, 5, 7]
alvo: int = int(input("Digite o seu número alvo: "))


def encontrar_pares(numeros: list[int], alvo: int) -> list[tuple[int, int]]:
    pares_encontrados = []

    for n1 in range(len(numeros)):
        for n2 in range(n1 + 1, len(numeros)):
            if numeros[n1] + numeros[n2] == alvo:
                pares_encontrados.append((numeros[n1], numeros[n2]))

    return pares_encontrados


print(f"As combinações encontradas são:", encontrar_pares(numeros, alvo))

# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas.
# Resposta:
dicionario: dict[str, Any] = {"Carlos": 991, "Ana": 992, "Bruno": 993}


def dicionario_ordenado(dicionario: dict[str, Any]) -> list[tuple[str, Any]]:
    lista_completa = []

    for nome, valor in dicionario.items():
        lista_completa.append((nome, valor))

    return sorted(lista_completa)


print(f"O dicionário ordenado: ", dicionario_ordenado(dicionario))

# Ou

dicionario: dict[str, Any] = {"Carlos": 991, "Ana": 992, "Bruno": 993}


def dicionario_ordenado(dicionario: dict[str, Any]) -> list[tuple[str, Any]]:
    return sorted(dicionario.items())


print(f"O dicionário ordenado:", dicionario_ordenado(dicionario))
