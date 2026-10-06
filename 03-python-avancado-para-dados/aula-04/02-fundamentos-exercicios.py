# 1. Exibindo uma mensagem.
# Crie uma função chamada exibir_boas_vindas() que exiba a mensagem: Bem-vindo ao sistema!
# Depois, chame a função para executar a mensagem.
# Requisitos:
# Utilize def.
# A função não deve receber parâmetros.
# A função não precisa retornar nenhum valor.


def exibir_boas_vindas() -> None:
    """
    Exibi mensagem de boas-vindas padrão no console.

    Args:
        mensagem (str):
    """
    print("Bem-vindo ao sistema!")


exibir_boas_vindas()

# 2. Identificando um produto.
# Crie uma função chamada exibir_produto() que receba:
# o nome de um produto;
# o preço do produto.
# A função deve exibir uma mensagem no seguinte formato: Produto: Teclado | Preço: R$ 150.00
# Depois, chame a função passando um produto e um preço como argumentos.
# Requisitos:
# Utilize parâmetros.
# Adicione type hints nos parâmetros.
# A função deve retornar None.


def exibir_produto(produto: str, preco: float) -> None:
    """
    Recebe o nome do produto, o preço e exibir essas informações formatadas.

    Args:
        produto (str): Nome do produto.
        preco (float): Preço unitário do produto.
    """
    print(f"Produto: {produto} | Preço: R$ {preco:.2f}")


exibir_produto("Teclado", 150.00)

# 3. Calculando o valor de uma compra.
# Crie uma função chamada calcular_total() que receba:
# o preço de um produto;
# a quantidade comprada.
# A função deve calcular e retornar o valor total da compra.
# Exemplo:
# total = calcular_total(50.0, 3)
# print(total)
# Resultado esperado: 150.0
# Requisitos:
# preco deve possuir type hint float.
# quantidade deve possuir type hint int.
# A função deve indicar que retorna um float.
# Utilize return para devolver o resultado.


def calcular_total(preco: float, quantidade: int) -> float:
    """
    Recebe o preço de um produto, sua quantidade comprada e calcular o valor total.

    Args:
        preco (float): Preço unitário do produto.
        quantidade (int): Quantidade unitária do produto.

    Returns:
        float: Valor final e total da compra.
    """
    total: float = preco * quantidade

    return total


total: float = calcular_total(50.0, 3)
print(f"R$ {total:.2f}")

# 4. Calculando a média de avaliações.
# Uma plataforma armazena três avaliações dadas por usuários para um produto.
# Crie uma função chamada calcular_media_avaliacoes() que receba três notas e retorne a média entre elas.
# Depois, utilize o resultado retornado pela função para exibir a média das avaliações.
# Requisitos:
# Utilize parâmetros e argumentos.
# Adicione type hints.
# Utilize return.
# Adicione uma docstring explicando o que a função recebe e o que retorna.
# Guarde o resultado da função em uma variável antes de exibi-lo.


def calcular_media_avaliacoes(nota1: float, nota2: float, nota3: float) -> float:
    """
    Calcula a média das avaliações a partir de 3 notas.

    Args:
        nota1 (float): Primeira nota da avaliação.
        nota2 (float): Segunda nota da avaliação.
        nota3 (float): Terceira nota da avaliação.

    Returns:
        float: Média das notas das avaliações.
    """
    media: float = (nota1 + nota2 + nota3) / 3

    return media


media_final: float = calcular_media_avaliacoes(8.7, 3.5, 6.8)
print(f"A média das avaliações é: {media_final:.2f}")

# 5. Processando um pedido.
# Você precisa criar duas funções para representar uma pequena parte de um sistema de pedidos.
# A primeira função deve se chamar: calcular_valor_final()
# Ela deve receber:
# preço unitário;
# quantidade;
# desconto em formato decimal.
# Por exemplo, 0.10 representa 10% de desconto.
# A função deve calcular e retornar o valor final do pedido após o desconto.
# Depois, crie uma segunda função chamada: exibir_resumo_pedido()
# Ela deve receber:
# número do pedido;
# valor final.
# E exibir uma mensagem como: Pedido #1025 finalizado. Total: R$ 270.00
# Requisitos:
# As duas funções devem possuir type hints.
# calcular_valor_final() deve retornar um float.
# exibir_resumo_pedido() deve retornar None.
# As duas funções devem possuir docstrings.
# O valor retornado por calcular_valor_final() deve ser passado como argumento para exibir_resumo_pedido().
# Não faça o cálculo diretamente fora da função.


def calcular_valor_final(preco: float, quantidade: int, desconto: float) -> float:
    """
    Calcula o valor final do produto a partir do valor unitário, quantidade e desconto aplicado.

    Args:
        preco (float): Preço unitário do produto.
        quantidade (int): Quantidade comprada.
        desconto (float): Percentual de desconto em formato decimal.

    Returns:
        float: Valor final da compra.
    """
    subtotal: float = preco * quantidade
    valor_desconto: float = subtotal * desconto
    total: float = subtotal - valor_desconto

    return total


def exibir_resumo_pedido(numero_pedido: int, valor: float) -> None:
    """
    Exibe o resumo do pedido finalizado na tela.

    Args:
        numero (int): Identificador do pedido (id).
        valor (float): Valor final do produto.
    """
    print(f"Pedido #{numero_pedido} finalizado. Total R$ {valor:.2f}")


id_pedido: int = 1025
valor_final: float = calcular_valor_final(preco=100, quantidade=3, desconto=0.10)
exibir_resumo_pedido(id_pedido, valor_final)

# 6. Convertendo temperatura.
# Crie uma função chamada converter_celsius_para_fahrenheit().
# A função deve receber uma temperatura em Celsius e retornar o valor convertido para Fahrenheit.
# Use a fórmula: fahrenheit = (celsius * 9 / 5) + 32
# Depois, armazene o resultado em uma variável e imprima a temperatura convertida.
# Requisitos:
# Receba a temperatura por parâmetro.
# Utilize type hint float.
# A função deve retornar um float.
# Utilize return.
# Adicione uma docstring explicando a função.


def converter_celsius_para_fahrenheit(celsius: float) -> float:
    """
    Recebe temperatura em Celsius e retorna o valor em Fahrenheit

    Args:
        celsius (float): Valor da temperatura em Celsius

    Returns:
        float: Valor da temperatura em Fahrenheit
    """
    fahrenheit: float = (celsius * 9 / 5) + 32

    return fahrenheit


valor_celsius: float = 32.1
temperatura_convertida: float = converter_celsius_para_fahrenheit(valor_celsius)
print(f"A temperatura {valor_celsius}°C é igual a {temperatura_convertida:.2f}°F")

# 7. Calculando consumo médio.
# Um veículo percorreu determinada distância utilizando uma quantidade de combustível.
# Crie uma função chamada calcular_consumo_medio() que receba:
# distância percorrida em quilômetros;
# quantidade de litros utilizados.
# A função deve retornar quantos quilômetros o veículo percorreu por litro.
# Exemplo: consumo = calcular_consumo_medio(420.0, 35.0)
# Resultado: 12.0
# Depois, crie uma segunda função chamada exibir_consumo() que receba o resultado e exiba: Consumo médio: {resultado} km/l
# Requisitos:
# As duas funções devem possuir type hints.
# calcular_consumo_medio() deve retornar float.
# exibir_consumo() deve retornar None.
# As duas funções devem possuir docstrings.
# O resultado da primeira função deve ser passado como argumento para a segunda.


def calcular_consumo_medio(distancia: float, litros: float) -> float:
    """
    Calcula o consumo de litros de um carro por cada quilômetro.

    Args:
        distancia (float): Distâcia percorrida pelo carro.
        litros (float): Quantidade de listros consumida.

    Returns:
        float: A média de quantos quilômetros o carro faz por litro (Km/l).
    """
    media: float = distancia / litros
    return media


def exibir_consumo(resultado: float) -> None:
    """
    Exibe o consumo médio formatado na tela.

    Args:
        resultado (float): Consumo médio calculado em km/l
    """
    print(f"Consumo médio: {resultado:.1f} km/l")


distancia_percorrida: float = 420.0
listros_consumido: float = 35.0

consumo_final: float = calcular_consumo_medio(distancia_percorrida, listros_consumido)
exibir_consumo(consumo_final)

# 8. Verificando uma meta de vendas.
# Crie uma função chamada calcular_percentual_meta() que receba:
# 1. valor da meta;
# 2. valor vendido.
# A função deve calcular e retornar o percentual da meta que foi atingido.
# Exemplo: percentual = calcular_percentual_meta(10000.0, 7500.0)
# Resultado: 75.0
# Depois, crie uma função chamada exibir_status_meta() que receba esse percentual.
# Ela deve exibir: Meta atingida!
# caso o percentual seja maior ou igual a 100.
# Caso contrário, deve exibir: Meta ainda não atingida.
# Requisitos:
# Utilize type hints.
# calcular_percentual_meta() deve retornar float.
# exibir_status_meta() deve retornar None.
# Utilize o valor retornado por uma função como argumento da outra.
# Adicione docstrings nas duas funções.
# Não repita o cálculo do percentual fora da função.


def calcular_percentual_meta(meta: float, vendido: float) -> float:
    """
    Calcula e retorna o percentual da meta que foi atingido.

    Args:
        meta (float): Valor da meta estabelecido.
        vendido (float): Valor vendido até o momento.

    Returns:
        float: O percentual alcançado até o momento.
    """
    resultado: float = (vendido / meta) * 100
    return resultado


def exibir_status_meta(resultado: float) -> None:
    """
    Exibe uma mensagem se a meta foi atingida ou não.

    Args:
        resultado (float): Valor do calculo do percentual

    Returns:
        None
    """
    if resultado >= 100:
        print("Meta atingida!")
    else:
        print("Meta ainda não atingida.")


meta_empresa: float = 10000.0
vendas_ate_momento: float = 7500.0
percentual: float = calcular_percentual_meta(meta_empresa, vendas_ate_momento)
exibir_status_meta(percentual)

# 9. Analisando uma entrega.
# Você está desenvolvendo uma pequena parte de um sistema de entregas.
# Crie uma função chamada calcular_tempo_estimado() que receba:
# 1. distância da entrega em quilômetros;
# 2. velocidade média do veículo em km/h.
# A função deve calcular e retornar o tempo estimado da entrega em horas.
# Use: tempo = distancia / velocidade
# Depois, crie uma função chamada classificar_entrega() que receba o tempo calculado e retorne:
# "Entrega rápida" se o tempo for menor ou igual a 1;
# "Entrega normal" se o tempo for maior que 1 e menor ou igual a 3;
# "Entrega demorada" se o tempo for maior que 3.
# Por fim, crie uma terceira função chamada exibir_resumo_entrega() que receba:
# 1. o tempo estimado;
# 2. a classificação.
# Ela deve exibir algo como:
# Tempo estimado: 2.5 horas
# Classificação: Entrega normal
# Requisitos:
# As três funções devem possuir type hints.
# calcular_tempo_estimado() deve retornar float.
# classificar_entrega() deve retornar str.
# exibir_resumo_entrega() deve retornar None.
# Todas devem possuir docstrings.
# O resultado de calcular_tempo_estimado() deve ser utilizado por classificar_entrega().
# Os resultados das duas primeiras funções devem ser utilizados por exibir_resumo_entrega().
# Cada função deve possuir apenas uma responsabilidade.


def calcular_tempo_estimado(distancia: float, velocidade: float) -> float:
    """
    Calcula e retorna o tempo estimado da entrega em horas, a partir da distância e velocidade do entregador.

    Args:
        distancia (float): Valor da distância em quilômetros.
        velocidade (float): Velocidade média do veículo em km/h.

    Returns:
        float: Valor do tempo estimado em horas.
    """
    tempo: float = distancia / velocidade
    return tempo


def classificar_entrega(tempo: float) -> str:
    """
    Recebe o tempo estimado da entrega e retorna uma string classificadora.

    Args:
        tempo (float): Valor do tempo estimado em horas.

    Returns:
        str: Mensagem classificadora referente a entrega efetuada.
    """
    if tempo <= 1:
        return "Entrega rápida."
    elif 1 < tempo <= 3:
        return "Entrega normal."
    else:
        return "Entrega demorada."


def exibir_resumo_entrega(tempo: float, classificacao: str) -> None:
    """
    Exibe na tela as informações do tempo estimado e da classificação recebida.

    Args:
        tempo (float): Valor do tempo estimado em horas.
        classificacao (str): Mensagem classificadora referente a entrega efetuada.
    """
    print(f"Tempo estimado: {tempo:.1f} horas.")
    print(f"Classificação: {classificacao}")


distancia_entrega: float = 115.5
velocidade_entrega: float = 60.0

tempo_entrega: float = calcular_tempo_estimado(distancia_entrega, velocidade_entrega)
mensagem_entrega: str = classificar_entrega(tempo_entrega)
exibir_resumo_entrega(tempo_entrega, mensagem_entrega)

# 10. Sistema de Aprovação de Empréstimo.
# Você está desenvolvendo uma parte de um sistema bancário responsável por analisar solicitações de empréstimo.
# O programa deverá utilizar várias funções, e cada uma terá uma responsabilidade específica.
# 1. Calcular comprometimento da renda
# Crie uma função chamada calcular_comprometimento_renda() que receba:
# 1. renda mensal;
# 2. valor da parcela do empréstimo.
# Ela deve calcular qual percentual da renda mensal seria comprometido pela parcela.
# Use: percentual = (parcela / renda) * 100
# A função deve retornar esse percentual.
# 2. Analisar o empréstimo
# Crie uma segunda função chamada analisar_emprestimo() que receba:
# renda mensal;
# valor solicitado;
# percentual de comprometimento da renda.
# A função deve retornar uma das seguintes classificações:
# "Aprovado"
# "Análise manual"
# "Recusado"
# Utilize estas regras:
# Se o comprometimento da renda for maior que 40%, retorne "Recusado".
# Se o comprometimento for menor ou igual a 40%, mas o valor solicitado for maior que 5 vezes a renda mensal, retorne "Análise manual".
# Caso contrário, retorne "Aprovado".
# 3. Calcular o total do pagamento
# Crie uma terceira função chamada calcular_total_pagamento() que receba:
# valor da parcela;
# quantidade de parcelas.
# Ela deve retornar o valor total que será pago ao final do empréstimo.
# Exemplo:
# Parcela: R$ 850.00
# Quantidade: 24
# Total pago: R$ 20400.00
# 4. Exibir o resultado final
# Por fim, crie uma função chamada exibir_resultado() que receba:
# valor solicitado;
# percentual de comprometimento;
# total que será pago;
# resultado da análise.
# Ela deve apenas exibir um resumo como:
# --- Análise do empréstimo ---
# Valor solicitado: R$ 15000.00
# Comprometimento da renda: 28.3%
# Total a pagar: R$ 20400.00
# Resultado: Aprovado
# Requisitos
# Todas as funções devem possuir type hints.
# Todas devem possuir docstrings.
# calcular_comprometimento_renda() deve retornar float.
# analisar_emprestimo() deve retornar str.
# calcular_total_pagamento() deve retornar float.
# exibir_resultado() deve retornar None.
# Os cálculos devem acontecer dentro das funções responsáveis por eles.
# Não repita cálculos fora das funções.
# Os valores retornados pelas funções devem ser armazenados em variáveis e reutilizados nas próximas etapas.
# A função exibir_resultado() deve apenas receber os resultados já calculados e exibi-los.
# Não utilize *args, **kwargs, parâmetros com valores padrão ou outros recursos ainda não vistos nesta aula.
# Fluxo esperado:
# dados do empréstimo
# ↓
# calcular comprometimento da renda
# ↓
# analisar empréstimo
# ↓
# calcular total do pagamento
# ↓
# exibir resultado final
# O objetivo é organizar um problema maior em funções menores, fazendo com que o retorno de uma etapa seja utilizado pelas próximas.


def calcular_comprometimento_renda(renda: float, parcela: float) -> float:
    """
    Recebe a renda o valor de uma possível parcela de empréstimo e calcula o percentual que essa parcela compromete a renda.

    Args:
        renda (float): Valor da renda mensal (R$).
        parcela (float): Possível valor da parcela do empréstimo.

    Returns:
        float: Percentual que a parcela ocupa no valor da renda mensal.
    """
    percentual: float = (parcela / renda) * 100
    return percentual


def analisar_emprestimo(renda: float, valor: float, percentual: float) -> str:
    """
    Recebe os valores que estão no "Args:" e classifica.

    Args:
        renda (float): Valor da renda mensal (R$).
        valor (float): Valor do empréstimo solicitado (R$).
        percentual (float): Valor percentual de comprometimento da renda.

    Returns:
        str: Classifica o empréstimo solicitado.
    """
    if percentual > 40:
        return "Recusado"
    elif valor > 5 * renda:
        return "Análise manual"
    else:
        return "Aprovado"


def calcular_total_pagamento(parcela: float, quantidade: int) -> float:
    """
    Calcula o total do pagamento do empréstimo sem taxas e juros.

    Args:
        parcela (float): Valor da parcela.
        quantidade (int): Quantidade de parcelas.

    Returns:
        float: Valor total (sem taxas e juros) do pagamento do empréstimo.
    """
    total_pagamento: float = parcela * quantidade
    return total_pagamento


def exibir_resultado(
    valor: float, percentual: float, total_pagamento: float, resultado: str
) -> None:
    """
    Exibe os resultados com os dados do "Args:".

    Args:
        valor (float): Valor do empréstimo solicitado (R$).
        percentual (float): Valor percentual de comprometimento da renda.
        total_pagamento (float): Valor total (sem taxas e juros) do pagamento do empréstimo.
        resultado (str): Classificador do empréstimo solicitado.
    """
    print("--- Análise do empréstimo ---")
    print(f"\nValor solicitado: R$ {valor:.2f}.")
    print(f"Comprometimento da renda: {percentual} %.")
    print(f"Total a pagar: R$ {total_pagamento}.")
    print(f"\nResultado: {resultado}.")


salario: float = 3000.00
valor_solicitado: float = 15000.00
valor_parcela: float = 850.00
qtd_parcela: int = 24

percentual_comprometido: float = calcular_comprometimento_renda(salario, valor_parcela)

classicacao: str = analisar_emprestimo(
    salario, valor_solicitado, percentual_comprometido
)

total_emprestimo: float = calcular_total_pagamento(valor_parcela, qtd_parcela)

exibir_resultado(
    valor_solicitado, percentual_comprometido, total_emprestimo, classicacao
)
