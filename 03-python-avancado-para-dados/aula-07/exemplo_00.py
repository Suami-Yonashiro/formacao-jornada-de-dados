# valor_1 = 4
# valor_2 = 6

# valor_4 = 7
# valor_5 = 9

# def soma(valor_1_da_soma: float, valor_2_da_soma: float) -> float:
#     """
#     uma função simples de soma de valores do tipo float que retorn float
#     """
#     resultado_da_soma = valor_1_da_soma + valor_2_da_soma
#     return resultado_da_soma

# valor_3 = soma(valor_1_da_soma = valor_1, valor_2_da_soma = valor_2)
# valor_6 = soma(valor_4, valor_5)

# print(valor_3)
# print(valor_6)

# Exercícios. Vamos revisar funções adicionando type hints e Pydantic
# 1. Calcular Média de Valores em uma Lista.

from typing import List

# def calcula_media(valores: List[float]) -> float:
#     return sum(valores) / len(valores)

# valores: List = [2, 3, 7, 1, 10]

# media_dos_valores = calcula_media(valores)

# print(media_dos_valores)

# 2. Filtrar Dados Acima de um Limite.

# def filtrar_acima_do_limite(valores: List[int], limite: int) -> List[int]:
#     resultado = []

#     for numero in valores:
#         if numero > limite:
#             resultado.append(numero)

#     return resultado

# Testando a função.

# idades: List[int] = [12, 13, 15, 18, 21, 22, 25, 30]
# limite: int = 18

# maiores_de_idade = filtrar_acima_do_limite(idades, limite)

# print(maiores_de_idade)

# 3. Contar Valores Únicos em uma Lista.

# def contar_valores_unicos(lista: List) -> int:
#     conjunto_unico = set(lista)

#     quantidade_unicos = len(conjunto_unico)

#     return(quantidade_unicos)

# Testando a função.

# compras: List[str] = ["maçã", "banana", "abacaxi", "pêra", "maçã", "uva"]

# lista_valores_unicos = contar_valores_unicos(compras)

# print(f"A lista original: {compras}")
# print(f"A quantidade de itens únicos são {lista_valores_unicos}.")

# 4. Converter Celsius para Fahrenheit em uma Lista.


def celsius_para_fahrenheit(temperatura_celsius: List[float]) -> List[float]:
    lista_fahrenheit = []

    for celsius in lista_celsius:
        fahrenheit: float = (celsius * 9 / 5) + 32

        lista_fahrenheit.append(fahrenheit)

    return lista_fahrenheit


# Testando a função.

lista_celsius: List[int] = [-1, 10, 27, -15]

lista_fahrenheit: List[float] = celsius_para_fahrenheit(lista_celsius)

print(f"As temperaturas em Celsius: {lista_celsius}")
print(f"Em Fahrenheit ficam: {lista_fahrenheit}")
