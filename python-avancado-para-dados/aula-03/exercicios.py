### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
# Resposta:
# quantidade = int(input("Digite a quantidade do produto: "))
# preco = float(input("Digite o preço: R$"))
# if quantidade > 0 and preco > 0:
#     print("Dados válidos")
# else:
#     print("Dados inválidos!")

### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Resposta:
# Temperatura < 18°C é 'Baixa' | Temperatura >= 18°C e <= 26°C é 'Normal' | Temperatura > 26°C é 'Alta'
# temperatura = float(input("Leitura da temperatura (°C): "))
# if temperatura < 18: 
#     print("Baixa")
# elif temperatura < 26:
#     print("Normal")
# else:
#     print("Atenção: Alta")

### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# Resposta:
# pasta_erros = []
# pasta_avisos = []
# pasta_sucessos = [] # temos o log como dicionário acima, porém essa analise muitas vezes vem de uma lista e criamos as pastas para separar as ocorrências.
# for log in logs:
#     if log['level'] == 'ERROR':
#         pasta_erros.append(log['message'])
#     elif log['level'] == 'WARNING':
#         pasta_avisos.append(log['message'])
#     elif log['level'] == 'SUCCESS':
#         pasta_sucessos.append(log['message'])
#     else:
#         print(f"Aviso: Nível desconhecido encontrado: {log['level']}")

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# Resposta:
# nome, idade_texto, email = input("Digite nome, idade e e-mail (separados por espaço): ").split()
# idade = int(idade_texto)
# print("n\\--- Analisando Dados---")
# if idade < 18:
#     print(f"Erro: {nome} deve ter pelo menos 18 anos.")
# elif idade > 65:
#     print(f"Erro: {nome} deve ter no máximo 65 anos.")
# elif ('@' not in email) and ('.com' not in email):
#     print("O formato do e-mail está errada.")
# else:
#     print(f"Dados do usuário válidos! Bem-vindo(a) {nome}.")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# Resposta:
# transacao = {'valor': 12000, 'hora': 20}
# valor = transacao['valor']
# hora = transacao['hora']
# if valor > 10000 or hora <9 or hora > 18:
#     print("Transação suspeita detectada, ação bloqueada!")
# else:
#     print("Transação realizada com sucesso!")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
# Resposta: 
# texto_usuario = input("Digite o seu texto aqui: ")
# texto_minusculo = texto_usuario.lower()
# pontuacoes = ".,;:!?()-\"'"
# texto_limpo = texto_minusculo
# for pontuacao in pontuacoes:
#     texto_limpo = texto_limpo.replace(pontuacao, "")
# palavras = texto_limpo.split()
# contagem = {}
# for palavra in palavras:
#     if palavra in contagem:
#         contagem[palavra] += 1
#     else:
#         contagem[palavra] = 1
# print(contagem)     
    
### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# Resposta:
# dados = [10, 20, 30, 40, 50]
# valor_min = min(dados)
# valor_max = max(dados)
# dados_normalizados = []
# for x in dados: 
#     x_norm = (x - valor_min) / (valor_max - valor_min)
#     dados_normalizados.append(x_norm)
# print(f"Dados originais: {dados}")
# print(f"Dados normalizados: {dados_normalizados}")

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando.
# Resposta:
# usuarios = [
#     {"nome": "Priscila", "email": "priscila@email.com"},
#     {"nome": "Suami", "email": None}, 
#     {"nome": "Carlos", "email": "carlos@email.com"},
#     {"nome": "Paula"}
# ]
# usuarios_completos = []
# usuarios_dados_faltantes = []
# for usuario in usuarios:
#     email = usuario.get("email")
#     if email is None:
#         usuarios_dados_faltantes.append(usuario)
#     else:
#         usuarios_completos.append(usuario)
# print(f"Usuários com os dados completos: {usuarios_completos}.")
# print(f"Usuários com dados faltantes: {usuarios_dados_faltantes}.")

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
# Resposta:
# numeros = range(1, 11)
# pares = []
# impares = []
# for numero in numeros:
#     if numero % 2 == 0:
#         pares.append(numero)
#     else:
#         impares.append(numero)
# print(f"Os número pares são: {pares}.")

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# Resposta:
# vendas = [
#     {"produto": "Teclado", "categoria": "Eletrônicos", "preco": 150},
#     {"produto": "Camiseta", "categoria": "Vestuário", "preco": 80},
#     {"produto": "Mouse", "categoria": "Eletrônicos", "preco": 90},
#     {"produto": "Calça Jeans", "categoria": "Vestuário", "preco": 120},
#     {"produto": "Caderno", "categoria": "Papelaria", "preco": 30}
# ]
# faturamento_por_categoria = {}
# for venda in vendas:
#     categoria = venda["categoria"]
#     preco = venda["preco"]
#     if categoria in faturamento_por_categoria:
#         faturamento_por_categoria[categoria] += preco
#     else:
#         faturamento_por_categoria[categoria] = preco
# print(faturamento_por_categoria)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
# Resposta:
# dados_coletados = []
# while True:
#     entrada = input("Digite um dados (para encerrar digite 'sair): ")
#     if entrada.lower() == "sair":
#         print("\n[Sair detectado. Encerrando coleta!]")
#         break
#     dados_coletados.append(entrada)
# print(f"Total de registros: {len(dados_coletados)}.")
# print(f"Dados coletados: {dados_coletados}.")

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
# Resposta:
# Validador que solicita uma nota de satisfação do cliente de 1 a 5.
# while True:
#     entrada = input("Digite uma nota de 1 a 5: ").strip()
#     if entrada.lstrip('-').isdigit():
#         nota = int(entrada)
#         if 1 <= nota <= 5:
#             print(f"\nObrigado nota {nota} registrada com sucesso.")
#             break
#         else:
#             print("ERRO. A nota deve ser de 1 a 5, tente novamente!")
#     else:
#         print("ERRO. Você deve digitar um número inteiro, tente novamente!")
   
### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
# Resposta:
# import time
# def obter_dados_da_api(pagina: int) -> list:
#     banco_de_dados_da_api = {
#         1: [{"id": 1, "cliente": "Ana"}, {"id": 2, "cliente": "Bruno"}],
#         2: [{"id": 3, "cliente": "Carlos"}, {"id": 4, "cliente": "Daniela"}],
#         3: [{"id": 5, "cliente": "Eduardo"}, {"id": 6, "cliente": "Fernanda"}]
#     }
#     return banco_de_dados_da_api.get(pagina, [])
# pagina_atual = 1
# todos_os_clientes = []
# while True:
#     dados_da_pagina = obter_dados_da_api(pagina_atual)    
#     if len(dados_da_pagina) == 0:
#         print(f"\nFim da página encontrado. Nenhum dados na {pagina_atual}")
#         break
#     for registro in dados_da_pagina:
#         todos_os_clientes.append(registro)
#     time.sleep(0.5)
#     pagina_atual += 1
# print(f"Total de páginas lidas com dados: {pagina_atual - 1}.")
# print(f"Total de registros importados: {len(todos_os_clientes)}.")
# print(f"Dados finais salvos: {todos_os_clientes}.")

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
# Resposta:
# import random
# tentativas_max = 5
# tentativa = 1

# while tentativa <= tentativas_max:
#     print(f"Tentativa {tentativa} de {tentativas_max}.")
#     sucesso = random.choices([True, False], weights=[15, 85])[0]
#     if sucesso:
#         print("Conexão bem-sucedida!")
#         break
#     print("Falha na conexão atual, tentando novamente!")
#     tentativa += 1
# else:
#     print("Falha de conexão, após 5 tentativas seguidas!")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.
# Resposta:
leitura_sensores = [22.5, 23.1, 24.0, 21.8, 999, 25.2]
posicao = 0 
while posicao < len(leitura_sensores):
    temperatura = leitura_sensores[posicao]
    if temperatura == 999:
        print(f"\n[ALERTA: Valor de parada ({temperatura}) encontrado no índice {posicao}! Interrompendo esteira...]")
        break
    print(f"Processando temperatura estável {temperatura}°C.")
    posicao += 1              