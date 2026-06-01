### Estruturas de Controle de Fluxo
# Integre na solução anterior um fluxo de While que repita o fluxo até que o usuário insira as informações corretas.

nome_valido = False
salario_valido = False
bonus_valido = False

while nome_valido is not True:
    try:
        nome = input("Digite o seu nome: ")
        
        # verifica se o nome está vazio.
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # verifica se há números no nome.
        elif nome.isdigit():
            raise ValueError("O nome não deve conter números.")
        else:
            nome_valido = True
            print(f"Nome válido, bem-vindo {nome}.")
    except ValueError as e:
        print(e)
        
while salario_valido is not True:
    try:
        salario = float(input("Digite o valor do seu salário: "))
        if salario < 0:
            print("Digite um valor positivo.")
        else:
            salario_valido = True
    except ValueError:
        print("Entrada válida para o salário.")

while bonus_valido is not True:
    try:
        bonus = float(input("Digite o valor do bônus recebido: "))
        if bonus < 0:
            print("Por favor, digite um valor positivo para o bônus: ")
        else: 
            bonus_valido = True
    except ValueError:
        print("Entrada válida.")

bonus_recebido = 1000 + salario * bonus # exemplo simples de KPI.
# imprime as informações para o usuário.
print(f"{nome}, seu salário de R${salario:.2f} ficou com o bônus final de R${bonus_recebido:.2f}.")        