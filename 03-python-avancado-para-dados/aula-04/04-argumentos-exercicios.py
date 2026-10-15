# Exercício 1 – Argumentos posicionais.
# Crie uma função chamada apresentar_jogador que receba:
# nome
# posicao
# A função deve exibir uma mensagem semelhante a:
# Jogador: Marta | Posição: Atacante
# Faça a chamada da função passando os dois argumentos por posição.
# Exemplo:
# apresentar_jogador("Marta", "Atacante")


def apresentar_jogador(jogador: str, posicao: str) -> None:
    print(f"Jogador: {jogador} | Posição: {posicao}")


apresentar_jogador("Marta", "Atacante")
