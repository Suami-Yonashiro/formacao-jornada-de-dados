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

# # Exercício 6 – Mais de um valor padrão.
# # Crie uma função chamada registrar_jogador com os seguintes parâmetros:
# # nome
# # posicao="Não informada"
# # titular=False
# # A função deve mostrar os dados do jogador.
# # Teste as seguintes chamadas:
# # registrar_jogador("Marta")
# # registrar_jogador("Marta", "Atacante")
# # registrar_jogador("Marta", "Atacante", True)
# # Depois, faça mais uma chamada alterando apenas o valor de titular, utilizando um argumento nomeado.


# def registrar_jogador(
#     nome: str, posicao: str = "Não informada", titular: bool = False
# ) -> None:
#     """
#     Registra as informações de um jogador, definindo valores padrão para posição e titularidade.

#     Args:
#         nome (str): O nome do jogador.
#         posicao (str, optional): A posição do jogador. O padrão é "Não informada".
#         titular (bool, optional): Define se o jogador começa jogando. O padrão é False.
#     """
#     print(f"Nome: {nome}")
#     print(f"Posição: {posicao}")
#     print(f"Titular: {titular}\n")


# registrar_jogador("Marta")
# registrar_jogador("Marta", "Atacante")
# registrar_jogador("Marta", "Atacante", True)

# # Exercício 7 – Alterando apenas um valor padrão.
# # Crie uma função chamada configurar_camisa que receba:
# # nome
# # numero
# # tamanho="M"
# # cor="amarela"
# # Faça uma chamada informando uma cor diferente, mas mantendo o tamanho padrão.
# # Exemplo:
# # configurar_camisa("Marta", 10, cor="azul")
# # Observe como o argumento nomeado permite alterar cor sem precisar passar um novo valor para tamanho.


# def configurar_camisa(
#     nome: str, numero: int, tamanho: str = "M", cor: str = "Amarela"
# ) -> None:
#     """
#     Configura os detalhes da camisa de um jogador(a).

#     Args:
#         nome (str): O nome do jogador ou jogadora.
#         numero (int): O número da camisa.
#         tamanho (str, optional): O tamanho da camisa (P, M, G, etc.). O padrão é "M".
#         cor (str, optional): A cor principal da camisa. O padrão é "Amarela".
#     """
#     print(f"Jogador(a): {nome} | Número: {numero} | Tamanho: {tamanho} | Cor: {cor}")


# configurar_camisa("Marta", 10, cor="Azul")

# # Exercício 8 – Recebendo vários argumentos com *args.
# # Crie uma função chamada listar_jogadores que receba uma quantidade variável de nomes utilizando *args.
# # def listar_jogadores(*jogadores):
# # A função deve percorrer os jogadores recebidos e exibir cada nome.
# # Teste a função com diferentes quantidades de argumentos:
# # listar_jogadores("Marta")listar_jogadores("Marta","Vini Jr","Alisson")


# def listar_jogadores(*jogadores: str) -> None:
#     """
#     Exibe uma lista de jogadores recebidos por meio de argumentos variáveis (*args).

#     Args:
#         *jogadores (str): Nomes dos jogadores passados dinamicamente.

#     Returns:
#         _type_: A função apenas imprime os nomes na tela.
#     """
#     for jogador in jogadores:
#         print(f"• {jogador}")
#     print()


# listar_jogadores("Marta")
# listar_jogadores("Marta", "Vini Jr", "Alisson")

# # Exercício 9 – Trabalhando com os valores de *args.
# # Crie uma função chamada somar_gols que receba uma quantidade indefinida de números utilizando *args.
# # A função deve retornar a soma de todos os valores recebidos.
# # Exemplo:
# # total = somar_gols(2, 1, 3, 2)
# # print(total)
# # Resultado esperado: 8


# def somar_gols(*gols: int) -> int:
#     """
#     Calcula o total de gols somando uma quantidade indefinida de números.

#     Args:
#          *gols (int): Uma quantidade variável de gols marcados.

#     Returns:
#         int: A soma total de todos os gols informados.
#     """
#     print(gols)
#     return sum(gols)


# total = somar_gols(2, 1, 3, 2)
# print(total)

# # Exercício 10 – Parâmetro normal e *args.
# # Crie uma função chamada: convocar_selecao(pais, *jogadores)
# # O primeiro argumento deve representar o país da seleção.
# # Todos os argumentos posicionais seguintes devem representar os jogadores convocados.
# # Exemplo de chamada:
# # convocar_selecao("Brasil","Alisson","Marquinhos","Bruno Guimarães","Vini Jr")
# # A função deve mostrar primeiro o país e depois cada jogador convocado.


# def convocar_selecao(pais: str, *jogadores: str) -> None:
#     """
#      Exibe a convocação de uma seleção e lista os jogadores chamados.

#     Args:
#         pais (str): O nome do país da seleção.
#         *jogadores (str): Nomes dos jogadores convocados.
#     """
#     print(f"País: {pais}")
#     print("--- Convocados ---")
#     for jogador in jogadores:
#         print(f" • {jogador}")
#     print()


# convocar_selecao("Brasil", "Alisson", "Marquinhos", "Bruno Guimarães", "Vini Jr")

# # Exercício 11 – Recebendo argumentos nomeados com **kwargs.
# # Crie uma função chamada mostrar_jogador que receba uma quantidade variável de argumentos nomeados utilizando **kwargs.
# # def mostrar_jogador(**dados):
# # Faça uma chamada semelhante a:
# # mostrar_jogador(nome="Marta", idade=40, posicao="Atacante")
# # Dentro da função, percorra os dados recebidos e mostre cada chave junto com seu respectivo valor.


# def mostrar_jogador(**dados) -> None:
#     """
#     Exibe os detalhes de um jogador recebidos via argumentos nomeados variáveis (**kwargs).

#     Args:
#         **dados: Argumentos nomeados contendo informações diversas do jogador (ex: nome, idade, posicao).
#     """
#     for chave, valor in dados.items():
#         print(f"{chave.capitalize()}: {valor}")


# mostrar_jogador(nome="Marta", idade=40, posicao="Atacante")

# # Exercício 12 – Parâmetro normal e **kwargs.
# # Crie uma função chamada:
# # cadastrar_time(nome, **informacoes)
# # O nome do time deve ser obrigatório.
# # As demais informações podem variar de uma chamada para outra.
# # Exemplo:
# # cadastrar_time("Brasil", tecnico="Carlo Ancelotti", continente="América do Sul" ,titulos=5)
# # A função deve mostrar o nome do time e depois todas as informações adicionais recebidas.


def cadastrar_time(nome: str, **informacoes) -> None:
    """
    Cadastra seleção exibindo seu nome e informações adicionais dinâmicas.

    Args:
        nome (str): Nome obrigatório da seleção.
        **informacoes: Dados adicionais variáveis sobre o time (ex: tecnico, titulos, continente).
    """
    print(f"Seleção: {nome}")

    for chave, valor in informacoes.items():
        print(f"{chave.capitalize()}: {valor}")


cadastrar_time(
    "Brasil", tecnico="Carlo Ancelotti", continente="América do Sul", titulos=5
)
