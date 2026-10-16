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

# Exercício 2 – A ordem dos argumentos.
# Crie uma função chamada mostrar_partida que receba:
# mandante
# visitante
# A função deve exibir os dois times no formato:
# Brasil x Argentina
# Faça as seguintes chamadas:
# mostrar_partida("Brasil", "Argentina") mostrar_partida("Argentina", "Brasil")
# Observe como a ordem dos argumentos posicionais altera o resultado.


def mostrar_partida(mandante: str, visitante: str) -> None:
    """
    Exibe o confronto de uma partida de futebol no formato mandante x visitante.

    Args:
        mandante (str): Nome do time que joga em casa (mandante).
        visitante (str): Nome do time adversário (visitante).
    """
    print(f"{mandante} X {visitante}")


mostrar_partida("Brasil", "Argentina")
mostrar_partida("Argentina", "Brasil")
