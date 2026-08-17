# Partida Brasil x México

"""
Titulares:
Alisson
Marquinhos
Gabriel Magalhães
Bruno Guimarães
Raphinha
Rodrygo
Vini Jr.

Gols:
Vini Jr.
Rodrygo
Vini Jr.

México marcou 1 gol.
"""

jogadores = [
    "Alisson",
    "Marquinhos",
    "Gabriel Magalhães",
    "Bruno Guimarães",
    "Raphinha",
    "Rodrygo",
    "Vini Jr.",
]

jogadores.append("Endrick")  # para adicionar um item.

jogadores[3] = "Neymar"  # para substituir o "Bruno Guimarães" pelo "Neymar"
# print(jogadores)

# Imprimi a lista "jogadores" em tópicos:
# print("Jogadores do Brasil")
# for jogador in jogadores:
#     print(f" - {jogador}")

# Imprime indicando o indice, posição do item na lista:
print("Jogadores do Brasil")
for indice, jogador in enumerate(jogadores):
    print(f" - {jogador} | Posição: {indice}")

# Tuplas com informações que não alteram.
partida = ("Brasil", "México", "Estádio Central", "20:00")

# Desempacotamento
selecao = partida[0]
adversario = partida[1]
estadio = partida[2]
horario = partida[3]

print(f"{selecao} x {adversario}")
print(f"Estádio: {estadio}")
print(f"Horário: {horario}")

autores_gols = [
    "Vini Jr.",
    "Rodrygo",
    "Vini Jr.",
]

quantidade_gols = len(autores_gols)
print(quantidade_gols)

jogadores_que_marcaram_gols = set(autores_gols)
print(f"Jogadores que marcaram: {jogadores_que_marcaram_gols}.")
quantidade_de_jogadores_que_marcaram_gols = len(jogadores_que_marcaram_gols)
print(
    f"Quantidade de jogadores que marcaram: {quantidade_de_jogadores_que_marcaram_gols}."
)

# Vini Jr. -> 2
# Rodrygo -> 1

# gols_por_jogador = {
#     "Vini Jr.": 2,
#     "Rodrygo": 1
# }
# print(gols_por_jogador["Vini Jr."])

# Contagem de Gols.
# Adicionar a chave que será o nome do jogador e a quantidade que ele fez no valor.
# for (iterar sobre a lista), if (condições) e o dict. (armazenar os dados).
gols_por_jogador = {}

for jogador in autores_gols:

    if jogador in gols_por_jogador:
        gols_por_jogador[jogador] += 1
    else:
        gols_por_jogador[jogador] = 1

print(f"Gols por jogador: {gols_por_jogador}.")

# .items(), .keys(), .values()
for (
    jogador,
    gols,
) in (
    gols_por_jogador.items()
):  # O items sozinho entrega tuplas, o for entrar para desempacotar.
    print(f"{jogador}: {gols} gol(s).")

# print(gols_por_jogador.keys()) # imprime as chaves do dicionário.
# print(gols_por_jogador.values()) # imprime os valores do dicionário.
