"""
Desafio Final — Sistema da Copa do Mundo

Desenvolva um programa para cadastrar partidas da Copa do Mundo.

O programa deverá permanecer em execução até que o usuário decida encerrá-lo.

Para cada partida, solicite:

Seleção mandante
Seleção visitante
Gols da seleção mandante
Gols da seleção visitante

Cada partida deverá ser armazenada em um dicionário, e todos os dicionários deverão ser armazenados em uma lista.

Ao finalizar o cadastro, exiba:

A quantidade de partidas cadastradas.
Todas as partidas registradas.
Quantas partidas terminaram empatadas.
A partida com o maior número total de gols.
A média de gols por partida.

Requisitos:

Utilize listas e dicionários.
Utilize while para controlar o cadastro.
Utilize for para percorrer as partidas.
Utilize if, elif e else para identificar o resultado de cada jogo.
Utilize try/except para validar os gols informados.
Utilize len() para calcular a quantidade de partidas cadastradas.
"""

# Lista para armazenar todas as partidas (onde cada partida será um dicionário).
lista_partidas = []

print("\n--- Cadastro das partidas da Copa do Mundo ---")

# Loop do cadastro.
while True:
    print(
        "\nDigite as informações da partida ou 'fim' a qualquer momento para encerrar."
    )

    mandante = input("Seleção mandante: ").strip()
    if mandante.lower() == "fim":
        break

    visitante = input("Seleção visitante: ").strip()
    if visitante.lower() == "fim":
        break

    while True:
        try:
            gols_mandante = int(input(f"Gols do(a) {mandante}: "))
            if gols_mandante < 0:
                print("O número de gols não pode ser negativo!")
                continue
            break

        except ValueError:
            print("Digite um número inteiro válido para gols.")

    while True:
        try:
            gols_visitante = int(input(f"Gols do(a) {visitante}: "))
            if gols_visitante < 0:
                print("O número de gols não pode ser negativo")
                continue
            break

        except ValueError:
            print("Digite um número inteiro válido para gols.")

    # Criando o dicionário da partida.
    partida = {
        "mandante": mandante,
        "visitante": visitante,
        "gols_mandante": gols_mandante,
        "gols_visitante": gols_visitante,
        "total_gols": gols_mandante + gols_visitante,
    }

    # Adicionando o dicionário na lista de partidas.
    lista_partidas = lista_partidas + [partida]
    print("Partida cadastrada com sucesso.")

# Exibição dos resultados.
qtd_partidas = len(lista_partidas)

if qtd_partidas > 0:
    empatadas = 0
    total_gols_campeonato = 0
    maior_gols_partida = -1
    partida_mais_gols = None

    print("\n" + "=" * 40)
    print("     RELATÓRIO DAS PARTIDAS     ")
    print("\n" + "=" * 40)
    print(f"Quantidade de partidas cadastradas: {qtd_partidas}.")
    print(" TODAS AS PARTIDADES REGISTRADAS ")

    # Loop para percorrer cada partida.
    for p in lista_partidas:
        print(
            f"{p['mandante']} {p['gols_mandante']} x {p['visitante']} {p['gols_visitante']}"
        )

        total_gols_campeonato = total_gols_campeonato + p["total_gols"]

        # Identificando o resultado.
        if p["gols_mandante"] == p["gols_visitante"]:
            empatadas = empatadas + 1
        elif p["gols_mandante"] > p["gols_visitante"]:
            pass  # Vitória do mandante.
        else:
            pass  # Vitória do visitante.

        if p["total_gols"] > maior_gols_partida:
            maior_gols_partida = p["total_gols"]
            partida_mais_gols = p

    # Cálculos finais fora do loop.
    media_gols = total_gols_campeonato / qtd_partidas

    print("\n--- ESTATÍSTICAS ---")
    print(f"Partidas empatadas: {empatadas}.")
    print(f"Médias de gols: {media_gols:.2f}.")

    if partida_mais_gols:
        print(
            f"A partida com maior número de gols ({partida_mais_gols['total_gols']} gols): "
            f"{partida_mais_gols['mandante']} {partida_mais_gols['gols_mandante']} x "
            f"{partida_mais_gols['gols_visitante']} {partida_mais_gols['visitante']}"
        )

else:
    print("\nNenhuma partida foi cadastrada.")
