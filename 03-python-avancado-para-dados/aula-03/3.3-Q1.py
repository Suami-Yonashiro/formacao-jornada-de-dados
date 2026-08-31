"""
Exercício 1 — Cadastro de Figurinhas

Você foi contratado para desenvolver um sistema simples para
controlar um álbum de figurinhas da Copa do Mundo.

O programa deve permitir que o usuário cadastre figurinhas até
que ele digite a palavra "fim".

Ao final, exiba:

Todas as figurinhas cadastradas.
A quantidade total de figurinhas.
A primeira figurinha cadastrada.
A última figurinha cadastrada.

Desafio: não permita que o usuário cadastre uma figurinha vazia.
"""

minhas_figurinhas = {}
# Dicionário para guardar a figurinha e sua quantidade, para trocas.

ordem_cadastro = []
# Lista auxiliar para lembrar a ordem exata em que foram cadastradas.

print("--- CADASTRO DE FIGURINHAS ---")
print("Digite o número da figurinha ou 'fim' para encerrar.\n")

while True:
    entrada = input("Digite o número da figurinha: ").strip()

    if entrada.lower() == "fim":
        break

    if entrada == "":
        print("ERRO: Entrada não pode ser vazia, digite um número inteiro.")
        continue

    try:
        numero_figurinha = int(entrada)

        if numero_figurinha < 1 or numero_figurinha > 980:
            print("ERRO: O número da figurinha deve estar entre 1 e 980.")
            continue

    except ValueError:
        print("Digito incorreto, tente novamente.")
        continue

    ordem_cadastro.append(numero_figurinha)
    # adiciona o número para validar a ordem de cadastro

    if numero_figurinha in minhas_figurinhas:
        minhas_figurinhas[numero_figurinha] += 1
        print(
            f"Figurinha {numero_figurinha} adicionada! Você tem {minhas_figurinhas[numero_figurinha]} delas."
        )

    else:
        minhas_figurinhas[numero_figurinha] = 1
        print(f"Figurinha {numero_figurinha} cadastrada com sucesso.")

# Exibindo relatório de resultados.
print("\n" + "=" * 40)
print("           RESUMO DA COLEÇÃO           ")
print("=" * 40)

if minhas_figurinhas:
    total = sum(minhas_figurinhas.values())

    print("Figurinhas em posse e suas respectivas quantidades: ")

    for figurinha, quantidade in sorted(minhas_figurinhas.items()):
        status = f"({quantidade - 1} repetida(s))" if quantidade > 1 else "(única)"
        print(f" - Figurinha n° {figurinha}: {quantidade} unidade(s) {status}")

    print(f"\nQuantidade total de figurinhas cadastradas: {total}.")

    print(f"Primeira figurinha cadastrada: {ordem_cadastro[0]}.")

    print(f"última figurinha cadastrada: {ordem_cadastro[-1]}.")

else:
    print("Nenhum figurinha foi cadastrada até o momento.")
