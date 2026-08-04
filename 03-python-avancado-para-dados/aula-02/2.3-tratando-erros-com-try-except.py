# 1) Código quebra se o usuário digitar errado.

gols: int = int(input("Quantos gols o Brasil fez? "))
print(f"O Brasil fez {gols} gols.")

# 2) ValueError acontecendo.

numero: int = int("três")
print(numero)

# 3) Tratando o erro ao digitar os gols do Brasil.

try:
    gols: int = int(input("Quantos gols o Brasil fez? "))
    print(f"O Brasil fez {gols} gols.")
except ValueError:
    print("Você precisa digitar um número inteiro.")

# 4) Analisando os gols do Brasil usando try/except com if.

try:
    gols: int = int(input("Quantos gols o Brasil fez? "))

    if gols >= 3:
        print("O Brasil fez muitos gols.")
    elif gols == 1 or gols == 2:
        print("O Brasil marcou, mas poderia ter feito mais.")
    else:
        print("O Brasil não marcou gol.")

except ValueError:
    print("Você precisa digitar um número inteiro.")

# 5) Pedindo os gols até o usuário digitar um número válido.

numero_valido: bool = False

while not numero_valido:
    try:
        gols: int = int(input("Quantos gols o Brasil fez? "))

        numero_valido = True

    except ValueError:
        print("Valor inválido, digite um número inteiro.")

print(f"O Brasil fez {gols} gols.")

# 6) Somando o gols do Brasil em três jogos.

total_gols = 0

for jogo in range(1, 4):
    numero_valido = False

    while not numero_valido:
        try:
            gols: int = int(input(f"Quantos gols o Brasil fez no jogo {jogo}? "))

            numero_valido = True

        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    total_gols += gols

print(f"Total de gols do Brasil: {total_gols}.")

# 7) Mostrando o desempenho do Brasil em cada jogo.

total_gols: int = 0

for jogo in range(1, 4):
    numero_valido = False

    while not numero_valido:
        try:
            gols: int = int(input(f"Quantos gols o Brasil fez no jogo {jogo}? "))

            numero_valido = True

        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    total_gols += gols

    if gols == 0:
        print("O Brasil não marcou nesse jogo.")
    elif gols == 1:
        print("O Brasil marcou 1 gol nesse jogo.")
    else:
        print(f"O Brasil marcou {gols} gols nesse jogo.")

print(f"O total de gols do Brasil foi de {total_gols} gols")

media: float = total_gols / 3

print(f"A média de gols foi de {media:.2f}, nesses 3 jogos.")

# 8) Código extra na aula para estudos: campanha do Brasil na copa.

total_gols_brasil: int = 0
total_gols_adversario: int = 0
pontos: int = 0

for jogo in range(1, 4):
    print(f"Jogo {jogo}")

    numero_valido: bool = False

    while not numero_valido:
        try:
            gols_brasil: int = int(input("Quantos gols o Brasil fez? "))

            numero_valido: bool = True

        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    numero_valido: bool = False

    while not numero_valido:
        try:
            gols_adversario: int = int(input("Quantos gols o adversário fez? "))

            numero_valido: bool = True

        except ValueError:
            print("Valor inválido. Digite um número inteiro.")

    total_gols_brasil += gols_brasil
    total_gols_adversario += gols_adversario

    if gols_brasil > gols_adversario:
        print("Vitória do Brasil.")
        pontos += 3
    elif gols_brasil == gols_adversario:
        print("Jogo empatado.")
        pontos += 1
    else:
        print("Brasil foi derrotado.")

    print("--------------------")

print("Resumo da fase dos grupos.")
print(f"Total de gols do Brasil: {total_gols_brasil}.")
print(f"Total de gols sofridos: {total_gols_adversario}.")
print(f"Pontuação final: {pontos}.")

if pontos >= 6:
    print("Brasil classificado para a próxima fase.")
elif pontos >= 4:
    print("Brasil ainda tem chance, mas depende do grupo.")
else:
    print("Brasil desclassificado na fase dos grupos.")
