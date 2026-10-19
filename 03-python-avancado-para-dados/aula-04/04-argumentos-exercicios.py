# # Exercício 1 – Argumentos posicionais.
# # Crie uma função chamada apresentar_jogador que receba:
# # nome
# # posicao
# # A função deve exibir uma mensagem semelhante a:
# # Jogador: Marta | Posição: Atacante
# # Faça a chamada da função passando os dois argumentos por posição.
# # Exemplo:
# # apresentar_jogador("Marta", "Atacante")


# def apresentar_jogador(nome: str, posicao: str) -> None:
#     """
#     Exibe uma mensagem formatada com o nome e a posição de um jogador de futebol.

#     Args:
#         nome (str): O nome do jogador.
#         posicao (str): A posição em que o jogador atua em campo.
#     """
#     print(f"Jogador: {nome} | Posição: {posicao}")


# apresentar_jogador("Marta", "Atacante")

# # Exercício 2 – A ordem dos argumentos.
# # Crie uma função chamada mostrar_partida que receba:
# # mandante
# # visitante
# # A função deve exibir os dois times no formato:
# # Brasil x Argentina
# # Faça as seguintes chamadas:
# # mostrar_partida("Brasil", "Argentina") mostrar_partida("Argentina", "Brasil")
# # Observe como a ordem dos argumentos posicionais altera o resultado.


# def mostrar_partida(mandante: str, visitante: str) -> None:
#     """
#     Exibe o confronto de uma partida de futebol no formato mandante x visitante.

#     Args:
#         mandante (str): Nome do time que joga em casa (mandante).
#         visitante (str): Nome do time adversário (visitante).
#     """
#     print(f"{mandante} X {visitante}")


# mostrar_partida("Brasil", "Argentina")
# mostrar_partida("Argentina", "Brasil")

# # Exercício 3 – Argumentos nomeados.
# # Crie uma função chamada cadastrar_jogador que receba:
# # nome
# # idade
# # posicao
# # Faça a chamada utilizando argumentos nomeados e passe os valores em uma ordem diferente da definida na função.
# # Exemplo:
# # cadastrar_jogador(posicao="Goleiro", nome="Alisson", idade=33)


# def cadastrar_jogador(nome: str, idade: int, posicao: str) -> None:
#     """
#     Cadastra um jogador de futebol exibindo suas informações básicas na tela.

#     Args:
#         nome (str): Nome do jogador.
#         idade (int): Idade do jogador em anos.
#         posicao (str): A posição em que o jogador atua.
#     """
#     print(f"Nome: {nome} | Idade: {idade} | Posição: {posicao}")


# cadastrar_jogador(posicao="Goleiro", nome="Alisson", idade=33)

# # Exercício 4 – Posicionais e nomeados juntos.
# # Crie uma função chamada registrar_gol que receba:
# # jogador
# # time
# # minuto
# # Na chamada da função:
# # Passe jogador por posição.
# # Passe time por posição.
# # Passe minuto pelo nome.
# # A função deve exibir uma mensagem semelhante a:
# # Vini Jr marcou para o Brasil aos 34 minutos.


# def registrar_gol(jogador: str, time: str, minuto: int) -> None:
#     """
#     Registra e exibe a ocorrência de um gol em uma partida.

#     Args:
#         jogador (str): O nome do jogador que marcou o gol.
#         time (str): O nome do time do jogador.
#         minuto (int): O minuto da partida em que o gol aconteceu.
#     """
#     print(f"{jogador} marcou para o(a) {time} aos {minuto} minutos.")


# registrar_gol("Vini Jr.", "Brasil", minuto = 34)

# # Exercício 5 – Parâmetro com valor padrão.
# # Crie uma função chamada criar_partida que receba:
# # time_a
# # time_b
# # estadio
# # O parâmetro estadio deve possuir o seguinte valor padrão:
# # "Estádio Nacional"
# # Depois, faça duas chamadas:
# # Uma sem informar o estádio.
# # Outra informando um estádio diferente.

# def criar_partida(time_a: str, time_b: str, estadio: str = "Estádio Nacional") -> None:
#     """
#     Cria uma partida de futebol entre dois times em um determinado estádio.

#     Args:
#         time_a (str): O nome do primeiro time.
#         time_b (str): O nome do segundo time.
#         estadio (str, optional): O nome do estádio. O padrão é "Estádio Nacional".
#     """
#     print(f"Partida {time_a} x {time_b}")
#     print(f"Local: {estadio}\n")

# criar_partida("Flamengo", "São Paulo")
# criar_partida("Flamengo", "São Paulo", estadio = "Estádio do Maracanã")

# Exercício 6 – Mais de um valor padrão.
# Crie uma função chamada registrar_jogador com os seguintes parâmetros:
# nome
# posicao="Não informada"
# titular=False
# A função deve mostrar os dados do jogador.
# Teste as seguintes chamadas:
# registrar_jogador("Marta")
# registrar_jogador("Marta", "Atacante")
# registrar_jogador("Marta", "Atacante", True)
# Depois, faça mais uma chamada alterando apenas o valor de titular, utilizando um argumento nomeado.


def registrar_jogador(
    nome: str, posicao: str = "Não informada", titular: bool = False
) -> None:
    """
    Registra as informações de um jogador, definindo valores padrão para posição e titularidade.

    Args:
        nome (str): O nome do jogador.
        posicao (str, optional): A posição do jogador. O padrão é "Não informada".
        titular (bool, optional): Define se o jogador começa jogando. O padrão é False.
    """
    print(f"Nome: {nome}")
    print(f"Posição: {posicao}")
    print(f"Titular: {titular}\n")


registrar_jogador("Marta")
registrar_jogador("Marta", "Atacante")
registrar_jogador("Marta", "Atacante", True)
