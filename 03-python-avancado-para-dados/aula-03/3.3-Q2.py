"""
Exercício 2 — Estatísticas da Partida

Crie um programa que solicite ao usuário as seguintes informações de uma partida:

Seleção mandante
Seleção visitante
Gols da seleção mandante
Gols da seleção visitante

Armazene essas informações em um dicionário.

Depois:

Exiba todas as informações utilizando um for com .items().
Informe qual seleção venceu a partida.
Caso os gols sejam iguais, informe que a partida terminou empatada.

Desafio: utilize try/except para garantir que a quantidade de gols seja um número inteiro válido.
"""

informacoes_do_jogo = {}

# Coleta de dados.
while True:
    mandante = input("Qual é a seleção mandante do jogo? ").strip()

    if not mandante:
        print("O nome da seleção não pode ficar em branco.")
        continue

    if mandante.replace(" ", "").isalpha():
        break
    else:
        print("Nome inválido! Use apenas letras!")

while True:
    visitante = input("Qual é a seleção visitante? ").strip()

    if not visitante:
        print("O nome da seleção não pode ficar em branco.")
        continue

    if visitante.replace(" ", "").isalpha():
        break
    else:
        print("Nome inválido! Use apenas letras!")

gols_mandante = 0
while True:
    try:
        gols_mandante = int(input(f"Quantos gols a seleção do(a) {mandante} marcou? "))

        if gols_mandante >= 0:
            break
        print("Digite um número maior ou igual a zero!")

    except ValueError:
        print("Digite um número inteiro.")

gols_visitante = 0
while True:
    try:
        gols_visitante = int(
            input(f"Quantos gols a seleção do(a) {visitante} marcou? ")
        )

        if gols_visitante >= 0:
            break
        print("Digite um número maior ou igual a zero!")

    except ValueError:
        print("Digite um número inteiro.")

# Armazenando o dicionário.
informacoes_do_jogo["Seleção Mandante"] = mandante
informacoes_do_jogo["Seleção Visitante"] = visitante
informacoes_do_jogo["Gols Mandante"] = gols_mandante
informacoes_do_jogo["Gols Visitante"] = gols_visitante

# Lógica do resultado.
if gols_mandante > gols_visitante:
    resultado = f"Vitória do(a) {mandante}."
elif gols_mandante < gols_visitante:
    resultado = f"Vitória do(a) {visitante}."
else:
    resultado = "A partida terminou empatada."

# Exibição.
print("\n" + "=" * 40)
print("INFORMAÇÕES DA PARTIDA")
print("=" * 40)

# Exibindo com FOR e .ITEMS().
for chave, valor in informacoes_do_jogo.items():
    print(f"{chave}: {valor}")

print("-" * 40)
print(f"\nResultado: {resultado}")
print("-" * 40)
