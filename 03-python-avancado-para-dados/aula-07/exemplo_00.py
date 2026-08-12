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


# def celsius_para_fahrenheit(temperatura_celsius: List[float]) -> List[float]:
#     lista_fahrenheit = []

#     for celsius in lista_celsius:
#         fahrenheit: float = (celsius * 9 / 5) + 32

#         lista_fahrenheit.append(fahrenheit)

#     return lista_fahrenheit


# Testando a função.

# lista_celsius: List[int] = [-1, 10, 27, -15]

# lista_fahrenheit: List[float] = celsius_para_fahrenheit(lista_celsius)

# print(f"As temperaturas em Celsius: {lista_celsius}")
# print(f"Em Fahrenheit ficam: {lista_fahrenheit}")

# 5. Calcular Desvio Padrão de uma Lista.

# def calcular_desvio_padrao(lista: List[float]) -> float:
#     # verificação de segurança para lista vazia ou 1 elemento.
#     if len(lista) <= 1:
#         return 0.0

#     # passo 1: calcular a média
#     media: float = sum(lista) / len(lista)

#     # passo 2: somar desvios ao quadrado
#     soma_desvios_quadrado = 0.0
#     for numero in lista:
#         distancia = numero - media
#         soma_desvios_quadrado += distancia ** 2 # ** 2 elevado ao quadrado

#     # passo 3: Calcular a variância (dividir pelo total de elementos)
#     variancia: float = soma_desvios_quadrado / len(lista)

#     # passo 4: Calcular a raiz quadrada
#     desvio_padrao: float = variancia ** 0.5

#     return desvio_padrao

# Testando a função.

# dados: List[int] = [10, 12, 23, 23, 16, 23, 21, 16]
# resultado: float = calcular_desvio_padrao(dados)

# print(f"Lista de dados: {dados}.")
# print(f"O desvio padrão é: {resultado:.2f}.")

# 6. Encontrar Valores Ausentes em uma Sequência.


def encontrar_valores_ausentes(sequencia: List[int]) -> List[int]:
    # se a lista estiver vazia ou com menos de 2 elementos, não tem o que comparar.
    if len(sequencia) < 2:
        return []

    # descobrimos onde a sequêcia começa (min) e onde termina (max)
    inicio: int = min(sequencia)
    fim: int = max(sequencia)

    valores_ausentes = []

    # passo 2: passamos por todos os números que deveriam existir nessa sequência.
    for numero in range(
        inicio, fim + 1
    ):  # +1 garante que o último número também seja testado.
        # passo 3:
        if numero not in sequencia:
            # nós o guardamos na lista de ausentes.
            valores_ausentes.append(numero)

    return valores_ausentes


# Testando a função.

sequencia_quebrada = [1, 2, 4, 5, 7, 8, 10]

faltando = encontrar_valores_ausentes(sequencia_quebrada)

print(f"Sequência original: {sequencia_quebrada}.")
print(f"Números ausentes: {faltando}.")
