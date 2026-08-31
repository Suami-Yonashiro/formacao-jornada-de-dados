# # Recuperando input(), while e validção.

autores_gols = ["Luiza", "Vini Jr.", "Snoopy", "Luciano"]
# # Registrar quem fez cada gol -> nome -> guardar na lista autores_gols.
# # while (uma condição que até acertar, ficará rodando), if, lista.
# jogadores = ["Luiza", "Vini Jr.", "Snoopy", "Luciano"]

# while True: # Enquanto for verdadeiro.
#     jogador: str = input("Digite quem marcou ou escreva 'fim' para encerrar: ")

#     if jogador.lower() == "fim":
#         break

#     if jogador in jogadores:
#         autores_gols.append(jogador)

#     else:
#         print("Jogador não foi encontrado na escalação.")

# print(autores_gols)

# Recuperando try/except.
gols_adversario = 0
while True:
    try:
        gols_adversario = int(input("Quantos gols o adversário marcou: "))

        if gols_adversario >= 0:
            break
        print("Digite um número maior ou igual a zero.")

    except ValueError:
        print("Digite um número inteiro.")

partida = ("Brasil", "México", "Estádio central", "20:00")
# Desempacotamento.
selecao = partida[0]
adversario = partida[1]
estadio = partida[2]
horario = partida[3]

# Descobrindo o resultado da partida.
autores_gols = [
    "Vini Jr.",
    "Rodrygo",
    "Vini Jr.",
]

gols_brasil = len(autores_gols)

if gols_brasil > gols_adversario:
    resultado = f"Vitória do {selecao}."
elif gols_brasil < gols_adversario:
    resultado = f"Derrota do {selecao}."
else:
    resultado = "Empate"

# Gerando os dados finais.
jogadores_que_marcaram_gols = set(autores_gols)
gols_por_jogador = {}

for jogador in autores_gols:
    if jogador in gols_por_jogador:
        gols_por_jogador[jogador] += 1
    else:
        gols_por_jogador[jogador] = 1

print("\n" + "=" * 40)
print("RELATÓRIO DA PARTIDA")
print("=" * 40)

print(f"\n{selecao} x {adversario}")
print(f"Estádio: {estadio}")
print(f"Horário: {horario}")

print(f"\nGols do {selecao}: {gols_brasil}")
print(f"\nGols do {adversario}: {gols_adversario}")

print("\nJogadores que marcaram: ")

for jogador in jogadores_que_marcaram_gols:
    print(f"- {jogador}")

print("\nGols por jogador: ")

for jogador, gols in gols_por_jogador.items():
    print(f"{jogador}: {gols}")

print(f"\nResultado: {resultado}")

"""
01 - Qual estrutura escolher?

02 - Guardando os jogadores
     ➝ list

03 - Percorrendo a escalação
     ➝ for

04 - Guardando as informações fixas
     ➝ tuple

05 - Registrando gols
     ➝ list

06 - Quem marcou?
     ➝ set

07 - Quantos gols cada um marcou?
     ➝ dict

08 - Fazendo o usuário registrar gols
     ➝ while + input

09 - Validando informações
     ➝ if + try/except

10 - Construindo relatório
     ➝ Tudo junto
"""
