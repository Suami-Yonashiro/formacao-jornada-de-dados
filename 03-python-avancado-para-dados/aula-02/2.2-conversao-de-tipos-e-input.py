total_gols: int = 0

for jogo in range(1, 4):
    gols: int = int(input(f"Quantos gols o Brasil fez no jogo {jogo}? "))

    total_gols += gols

    if gols == 0:
        print("O Brasil não marcou nesse jogo.\n")
    elif gols == 1:
        print("O Brasil marcou 1 gol nesse jogo.\n")
    else:
        print(f"O Brasil marcou {gols} gols nesse jogo.\n")

print(f"O total de gols do Brasil: {total_gols}.\n")

media: float = total_gols / 3

print(f"A média de gols do Brasil foi de {media:.2f}.")
