# Implementação do algoritmo de ordenação por seleção.
lista_de_numeros: list = [40, 50, 60, 70, 0, -408593, 1, 50]


def ordenar_lista_de_numeros(numeros: list) -> list:
    nova_lista_de_numeros = numeros.copy()

    for i in range(len(nova_lista_de_numeros)):
        for j in range(i + 1, len(nova_lista_de_numeros)):
            if nova_lista_de_numeros[i] > nova_lista_de_numeros[j]:
                nova_lista_de_numeros[i], nova_lista_de_numeros[j] = (
                    nova_lista_de_numeros[j],
                    nova_lista_de_numeros[i],
                )

    return nova_lista_de_numeros


# Ordenando a lista.
nova_lista = ordenar_lista_de_numeros(lista_de_numeros)
print("Lista ordenada:", nova_lista)

# Função já criada no python para ordenar listas, resumindo o exercício acima.
# lista_de_numeros.sort()
# print("Lista ordenada com o método built-in:", lista_de_numeros)
