"""
Exercício 5 — Ranking de Artilheiros

Crie uma lista de dicionários para armazenar informações de jogadores.

O programa deverá perguntar quantos jogadores o usuário deseja cadastrar.

Para cada jogador, solicite:

Nome
Seleção
Quantidade de gols

Cada jogador deverá ser armazenado como um dicionário dentro da lista.

Ao final:

Exiba todos os jogadores cadastrados.
Informe qual jogador marcou mais gols.
Informe a média de gols dos jogadores cadastrados.

Desafio: utilize try/except para validar a quantidade de gols informada pelo usuário.
"""

jogadores = []

print("--- INTORMAÇÕES DOS JOGADORES ---")

# Validação para garantir que o número de jogadores, seja um número inteiro
while True:
    try:
        qtd_jogador = int(input("Quantos jogadores você quer cadastrar: "))
        if qtd_jogador > 0:
            break
        print("ERRO. Digite um número maior que zero!")
    except ValueError:
        print(
            "Entrada inválida, digite um número inteiro maior que 0 para a quantidade de jogadores."
        )

# Loop para cadastrar cada jogador.
for j in range(qtd_jogador):
    print(f"\n--- Cadastro do {j + 1}° jogador ---")
    nome = input(f"Qual o nome do jogador? ")
    selecao = input(f"Qual a seleção do {nome}? ")

    # Validar a quantidade de gols.
    while True:
        try:
            qtd_gols = int(input(f"Qual a quantidade de gols do {nome}? "))
            if qtd_gols >= 0:
                break
            print("A quantidade de gols não pode ser negativa.")
        except ValueError:
            print("Entrada inválida, digite um número inteiro para validar os gols.")

    jogador = {"Nome": nome, "Seleção": selecao, "Gols": qtd_gols}

    # Adiciona o dicionário do jogador na lista principal.
    jogadores.append(jogador)

print("-" * 40)
print("JOGADORES CADASTRADOS")
print("-" * 40)

total_gols = 0
artilheiro = jogadores[0]  # Assumi temporáriamente que é o primeiro.

for joga in jogadores:
    print(
        f"Jogador: {joga['Nome']} | Seleção: {joga['Seleção']} | Gols: {joga['Gols']}."
    )

    total_gols += joga["Gols"]

    if joga["Gols"] > artilheiro["Gols"]:
        artilheiro = joga

media_gols = total_gols / len(jogadores)

print(
    f"\nArtilheiro: {artilheiro['Nome']} da seleção do(a) {artilheiro['Seleção']} com {artilheiro['Gols']} gols."
)
print(f"Média de gols do jogadores: {media_gols:.2f}")
