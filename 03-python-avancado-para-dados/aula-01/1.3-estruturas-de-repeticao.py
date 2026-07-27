# =========================================================
# 1) CÓDIGO REPETITIVO SEM LOOP
# =========================================================

print("Cobrança de pênalti 1: o jogador ajeita a bola...")
print("Cobrança de pênalti 2: o jogador ajeita a bola...")
print("Cobrança de pênalti 3: o jogador ajeita a bola...")
print("Cobrança de pênalti 4: o jogador ajeita a bola...")
print("Cobrança de pênalti 5: o jogador ajeita a bola...")

# =========================================================
# 2) FOR COM STRING
# Cenário: percorrendo o grito da torcida letra por letra
# =========================================================

grito = "Gol"

for letra in grito:
    print(letra)

print("A torcida acabou de gritar!")

# =========================================================
# 3) FOR COM RANGE
# Cenário: repetindo cobranças de pênalti automaticamente
# =========================================================

for cobranca in range(1, 6):
    print(f"Cobrança de pênalti {cobranca}: o jogador ajeita a bola...")

# =========================================================
# 4) FOR COM RANGE
# =========================================================

for numero in range(1, 11):
    print(numero)

# =========================================================
# 5) FOR COM IF DENTRO
# Cenário: rodadas da Copa do Mundo
# =========================================================

for rodada in range(1, 6):
    if rodada == 5:
        print("A última rodada! Jogo decisivo!")
    else:
        print(f"Rodada {rodada} da copa do mundo")

# =========================================================
# 6) FOR COM INPUT, IF/ELSE E CONTADOR
# Cenário: contar quantos gols o Brasil fez em lances perigosos
# =========================================================

gols_brasil = 0

for lance in range(1, 4):
    print(f"Lance perigoso, número {lance}")

    resultado = input("Foi gol do Brasil? Digite sim ou não: ")

    if resultado == "sim":
        gols_brasil += 1
        print("GOOOL!")
    else:
        print("Não foi gol...")

print("Fim de jogo!")
print(f"O total de gols do Brasil: {gols_brasil}")
