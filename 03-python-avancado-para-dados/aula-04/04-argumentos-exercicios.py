# Exercício 1 – Argumentos posicionais.
# Crie uma função chamada apresentar_jogador que receba:
# nome
# posicao
# A função deve exibir uma mensagem semelhante a:
# Jogador: Marta | Posição: Atacante
# Faça a chamada da função passando os dois argumentos por posição.
# Exemplo:
# apresentar_jogador("Marta", "Atacante")


def apresentar_jogador(nome: str, posicao: str) -> None:
    """
    Exibe uma mensagem formatada com o nome e a posição de um jogador de futebol.

    Args:
        nome (str): O nome do jogador.
        posicao (str): A posição em que o jogador atua em campo.
    """
    print(f"Jogador: {nome} | Posição: {posicao}")


apresentar_jogador("Marta", "Atacante")
