"""
Exercício 3 — Seleções Classificadas

Durante a fase de grupos, várias seleções foram sendo classificadas.

Peça ao usuário para informar o nome de 8 seleções.

Armazene essas seleções em um set.

Ao final:

Exiba todas as seleções classificadas.
Informe quantas seleções diferentes foram cadastradas.

Depois pergunte ao usuário o nome de uma seleção e informe se ela está classificada utilizando o operador in.

Desafio: explique por que, mesmo digitando uma seleção repetida, ela aparece apenas uma vez no conjunto.
"""

classificados = set()

for c in range(1, 9):
    selecao = input(f"Qual a {c}° seleção classificada? ")
    classificados.add(selecao)

print("-" * 40)
print("SELEÇÕES CLASSIFICADAS NA FASE DE GRUPOS")
print("-" * 40)

print(f"As seleções classificadas foram: {', '.join(classificados)}.")

print(f"\nO total de seleções diferentes cadastradas: {len(classificados)}.")
print("-" * 40)

pergunta = input("Digite o nome da seleção para verificar se ela está classificada: ")

if pergunta in classificados:
    print(f"Sim, a seleção do(a) {pergunta} está classificada.")
else:
    print(f"Não, a seleção do(a) {pergunta} não está entre os classificados.")
