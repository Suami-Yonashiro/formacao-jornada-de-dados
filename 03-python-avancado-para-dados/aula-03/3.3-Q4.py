"""
Exercício 4 — Menu do Álbum

Desenvolva um programa que simule um álbum de figurinhas.

Utilize uma lista para armazenar as figurinhas e exiba o seguinte menu:

1 - Adicionar figurinha
2 - Remover figurinha
3 - Buscar figurinha
4 - Mostrar álbum
5 - Encerrar

O menu deve permanecer sendo exibido até que o usuário escolha a opção 5.

Regras:

Ao adicionar, a figurinha deve ser inserida no final da lista.
Ao remover, informe caso a figurinha não exista.
Na busca, informe se a figurinha está ou não no álbum.
Ao mostrar o álbum, exiba todas as figurinhas utilizando um for.

Desafio: utilize if, elif, else e while.
"""

album = []
opcao = 0

while opcao != 5:  # enquanto a opção for diferente de 5, faça.
    print("\n---MENU DO ALBÚM---")
    print("Opção 1 - Adicionar figurinha.")
    print("Opção 2 - Remover figurinha.")
    print("Opção 3 - Buscar figurinha.")
    print("Opção 4 - Mostrar albúm de figurinha.")
    print("Opção 5 - Encerrar.")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        adiciona_figurinha = int(
            input("Digite o número da figuarinha para adicionar: ")
        )
        album.append(adiciona_figurinha)  # adiciona no final
        print(f"Figurinha {adiciona_figurinha} adicionada com sucesso!")

    elif opcao == 2:
        remove_figurinha = int(input("Digite o número da figurinha para remover: "))
        if remove_figurinha in album:  # checa se existe
            album.remove(remove_figurinha)
            print(f"Figurinha {remove_figurinha} removida com sucesso!")
        else:
            print("ERRO: Essa figurinha não existe no albúm.")

    elif opcao == 3:
        busca_figurinha = int(input("Digite o número da figurinha de deseja buscar: "))
        if busca_figurinha in album:
            print(f"Encontrado, a figurinha {busca_figurinha} está no seu albúm.")
        else:
            print(f"ERRO, a figurinha {busca_figurinha} ainda NÃO está no seu albúm.")

    elif opcao == 4:
        print("\n--- SUAS FIGURINHAS ---")
        if len(album) == 0:  # avisa se o albúm estiver vazio.
            print("O albúm está vazio.")
        else:
            for figurinha in album:
                print(f"- {figurinha}")

    elif opcao == 5:
        print("Programa encerrado!")

    else:
        print("Opção inválida, escolha um número de 1 a 5.")
