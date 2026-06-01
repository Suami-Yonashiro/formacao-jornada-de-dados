import math

# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num_01 = int(input("Digite um número inteiro: "))
num_02 = int(input("Digite outro número inteiro: "))
resultado = num_01 + num_02
print(f"O resultado da soma dos dois numeros é igual a {resultado}.")

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
num = int(input("Digite um número para obter o resto da divisão por 5: "))
resultado = num % 5 
print(f"O resto da divisão por 5 é igual a {resultado}.")

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num_01 = int(input("Multiplicação, digite um número: "))
num_02 = int(input("Digite outro número: "))
resultado = num_01 * num_02
print(f"A multiplicação entre os dois números é igual a {resultado}.")

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num_01 = int(input("Digite um número inteiro: "))
num_02 = int(input("Digite outro número inteiro: "))
resultado = num_01 // num_02
print(f"A divisão inteira do 1° pelo 2° número é igual {resultado}.")

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
num = int(input("Digite um número para saber a sua potência: "))
resultado = num ** 2
print(f"O quadrado do número é igual a {resultado}.")

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
num_01 = float(input("Digite um número flutuante: "))
num_02 = float(input("Digite outro número flutuante: "))
resultado = num_01 + num_02
print(f"O resultado da soma dos dois numeros flutuantes é igual a {resultado}.")

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
num_01 = float(input("Média. Digite um número flutuante: "))
num_02 = float(input("Digite outro número flutuante: "))
media = (num_01 + num_02) / 2
print(f"A média da soma de {num_01} com {num_02} é igual a {media}.")

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
base = float(input("Digite a base de uma potência: "))
expoente = int(input("Digite o seu expoente: "))
resultado = base ** expoente
print(f"A exponenciação de {base} com {expoente} é igual a {resultado}.")

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
temp_celsius = float(input("Conversão. Digite a temperatura em Celsius: "))
conversao = (temp_celsius * 1.8) + 32
print(f"A conversão de {temp_celsius}°C para Fahrenheit é {conversao:.1f}°F.")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Para saber a área digite o raio da circunferência: "))
area = ((raio**2)*math.pi)
print(f"A área é igual a {area:.2f}.")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
palavra = input("Escreva uma palavra para converter para letras maiúsculas: ")
resultado = palavra.upper()
print(f"{resultado}.")

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome = input("Escreva o seu nome completo para converter para todas as letras minúsculas: ")
resultado = nome.lower()
print(f"{resultado}.")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
frase = input("Escreva uma frase: ")
resultado = frase.strip()
print(f"Frase sem espaços nas pontos: {resultado}")

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
data_do_usuario = input("Insira uma data no formato dd/mm/aaaa: ")
lista_dia_mes_ano = data_do_usuario.split("/")
print(f"O dia é: {lista_dia_mes_ano[0]}, o mês é: {lista_dia_mes_ano[1]}, o ano é: {lista_dia_mes_ano[2]}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
word_01 = input("Escreva uma palavra: ")
word_02 = input("Escreva outra palavra: ")
concatenacao = word_01 + " " + word_02
print(f"A concatenação das duas strings é {concatenacao}.")

# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
entr_01 = input("Digite a primeira expresão (True/False): ")
entr_02 = input("Digite a segunda expressão (True/False): ")
valor1 = entr_01.strip().capitalize() == "True"
valor2 = entr_02.strip().capitalize() == "True"
resultado = valor1 and valor2
print(f"{valor1} AND {valor2} é igual a: {resultado}")

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
entr_01 = input("Digite o primeiro valor booleano (True/False): ")
entr_02 = input("Digite o segundo valor booleano (True/False): ")
valor1 = entr_01.strip().capitalize() == "True"
valor2 = entr_02.strip().capitalize() == "True"
resultado = valor1 or valor2
print(f"O resultado de: {valor1} or {valor2} é -> {resultado}.")

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
entr_ = input("Digite um valor booleano (True/False): ")
valor_ = entr_.strip().capitalize() == "True"
resultado = not valor_
print(f"O valor invertido de {valor_} é {resultado}.") 

# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
num_01 = int(input("Digite o primeiro número: "))
num_02 = int(input("Digite o segundo número: "))
resultado = num_01 == num_02
print(f"Os numeros {num_01} e {num_02} são iguais? {resultado}.")

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
num_01 = int(input("Digite o primeiro número: "))
num_02 = int(input("Digite o segundo número: "))
resultado = num_01 != num_02
print(f"Os numeros {num_01} e {num_02} são diferentes? {resultado}.")

# #### try-except e if

# 21: Conversor de Temperatura
print("=== Conversor de Celsius para Fahrenheit ===")
try:
    celsius = float(input("Digite a temperatura em Celsius (°C): "))
    if celsius < -273.15: 
        print("Erro: Essa temperatura é menor que zero absoluto.")
    else:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C equivale a {fahrenheit:.2f}°F.")
except ValueError:
    print("\n[Erro]: Você NÃO digitou um número válido!")

# 22: Verificador de Palíndromo
print("=== Verificador de Palíndromo ===")
try:
    entrada = input("Digite uma palavra ou frase: ")
    if not entrada.strip():
        raise ValueError("Entrada vazia.")
    texto_limpo = entrada.replace(" ", "").lower()
    texto_invertido = texto_limpo[::-1]
    if texto_limpo == texto_invertido:
        print(f"{entrada} é um palíndromo! 🎉")
        print(f"O texto lido ao contrário: {texto_invertido}.")
    else: 
        print(f"O texto não é um palíndromo ❌.")
        print(f"O textlo lido ao contrário: {texto_invertido}. ")
except ValueError:
    print("\n[Erro]: Você digitou nenhuma palavra tente novamente.")

# 23: Calculadora Simples
print("=== Calculadora Simples ===")
try:
    num_01 = float(input("Digite o primeiro número: "))
    num_02 = float(input("Digite o segundo número: "))
    
    print("\nOperações Disponíveis: ")
    print("+ -> Adição.")
    print("- -> Subtração.")
    print("* -> Multiplicação.")
    print("/ -> Divisão.")
    operacao = input("Escolha a operação correspondente (+, -, *, /): ").strip()
    
    if operacao == "+":
        resultado = num_01 + num_02
        print(f"\nResultado: {num_01} + {num_02} = {resultado}")
    elif operacao == "-":
        resultado = num_01 - num_02
        print(f"\nResultado: {num_01} - {num_02} = {resultado}")
    elif operacao == "*":
        resultado = num_01 * num_02
        print(f"\nResultado: {num_01} * {num_02} = {resultado}")
    elif operacao == "/":
        if num_02 == 0:
            print("\n[Erro matemático]: Não é possível dividir um número por zero!")
        else:
            resultado = num_01 / num_02
            print(f"\nResultado: {num_01} / {num_02} = {resultado}")
    else:
        print("\nOperação inválida: Escolha apenas entre +, -, * ou /.")
except ValueError:
    print("\nEntrada inválida: Digite apenas números.")    

# 24: Classificador de Números
print("=== Classificador de Números ===")
try:
    numero = int(input("Digite um número inteiro: "))
    categoria_sinal = ""
    categoria_paridade = ""
    
    if numero > 0:
        categoria_sinal = "Positivo"
    elif numero < 0 :
        categoria_sinal = "Negativo"
    else:
        categoria_sinal = "Zero"
        
    if numero == 0:
        categoria_paridade = "Neutro"
    elif numero % 2 == 0:
        categoria_paridade = "Par"
    else:
        categoria_paridade = "Ímpar"
        
    print(f"Análise do {numero}, sinal {categoria_sinal} e paridade {categoria_paridade}.")
except ValueError:
    print("\n[Erro]: Entrada inválida, digite apenas números inteiros.")

# 25: Conversão de Tipo com Validação
print("=== Detector e Conversor de Tipos ===")
entrada = input("Digite qualquer valor (texto, número, etc: )").strip()
if not entrada:
    print("\n[Erro]: Você não digitou nada.")
else:
    
    try:
        valor_convertido = int(entrada)
        print(f"Tipo detectado: Inteiro (int).")
        print(f"O valor no Python: {valor_convertido}.")

    except ValueError:
        try:
            entrada_ajustada = entrada.replace(",", ".")
            valor_convertido = float(entrada_ajustada)
            print(f"Tipo detectado: Decimal (float).")
            print(f"O valor no Python: {valor_convertido}.")
        except ValueError:
            print(f"O valor {entrada} não pode ser convertido para número.")
            print(f"Tipo detectado: Texto (str).")