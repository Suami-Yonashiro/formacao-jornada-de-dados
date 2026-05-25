### Desafio - Refatorar o projeto da aula anterior evitando Bugs!
CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome
try:
    nome_usuario = input("Digite o seu nome: ")
    if any(char.isdigit() for char in nome_usuario): #Verifica se você digitou número.
        raise ValueError("Você digitou o nome errado.")
    elif len(nome_usuario) == 0: 
        raise ValueError("Você digitou nada")
    elif nome_usuario.isspace(): #Verifica se você digitou apenas espaços.
        raise ValueError("Você digitou apenas espaço.")
    else:
        print(f"Nome válido: {nome_usuario}.")
except ValueError as e:
    print(e)
    exit()

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante
try:
    salario_usuario = float(input("Digite o seu salario: "))
    if salario_usuario < 0:
        print("Por gentileza, digite um valor positivo para salário.")
except ValueError:
    print("Entrada errada, por gentileza, digite novamente.")
    exit()

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante
try:
    bonus_usuario = float(input("Digite o seu bonus: "))
    if bonus_usuario < 0:
        print("Por gentiliza digite um valor positivo para bônus.")
except ValueError:
    print("Entrada errada, por gentileza, digite novamente.")
    exit()

# 4) Calcule o valor do bônus final
valor_do_bonus = CONSTANTE_BONUS + salario_usuario * bonus_usuario

# 5) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus
print(f"O usuario {nome_usuario} está com o salário de R${salario_usuario} e receberá um bônus de R${valor_do_bonus}.")

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?