# Aula 04 | Type hint, Tipos complexos (Dicionários vs DataFrames Vs Tabelas Vs Excel) e Funções

Bem-vindos à quarta aula de Python e SQL focada em Engenharia de Dados. Nesta aula você vai aprender sobre: Type Hint, Listas e Dicionários e Funções. Esses elementos são essenciais para a manipulação de dados, ajudando na organização, interpretação e análise eficiente das informações. 

![imagem_01](./pic/1.jpg)

Vamos começar com uma introdução a cada um desses temas para nos prepararmos para o nosso primeiro prsojeto, como ler 1 bilhão de linhas!

![imagem_05](./pic/5.jpeg)

E o nosso workshop de sabado, dia 24 as 9am, como validar 1 bilhão de linhass.

![imagem_06](./pic/6.jpeg)

![imagem_02](./pic/2.jpg)

## 1. Type Hint

O uso de Type Hint ajuda a tornar o código mais legível e seguro, especificando o tipo de dados esperados por funções e variáveis. Na engenharia de dados, isso é especialmente útil para garantir que as funções de manipulação e análise de dados recebam os dados no formato correto, reduzindo erros em tempo de execução.

Para demonstrar como utilizar Type Hints com tipos primitivos em Python, vamos criar quatro variáveis representando os tipos mais comuns: int para números inteiros, float para números de ponto flutuante, str para strings (cadeias de caracteres) e bool para valores booleanos. Type Hints são usados para indicar o tipo de uma variável no momento da sua declaração, melhorando a legibilidade do código e facilitando a detecção de erros.

Sem Type Hint
```python
idade = 30
altura = 1.75
nome = "Alice"
is_estudante = True
```

Com Type Hint
```python
idade: int = 30
altura: float = 1.75
nome: str = "Alice"
estudante: bool = True
```

O uso de Type Hint ajuda a tornar o código mais legível e seguro, especificando o tipo de dados esperados por funções e variáveis. Na engenharia de dados, isso é especialmente útil para garantir que as funções de manipulação e análise de dados recebam os dados no formato correto, reduzindo erros em tempo de execução.

Na Python, a tipagem de funções é facilitada pelo uso de "Type Hints" (Dicas de Tipo), uma característica introduzida no Python 3.5 através do PEP 484. Os Type Hints permitem aos desenvolvedores especificar os tipos de dados esperados para os parâmetros de uma função e o tipo de dado que a função deve retornar. Embora essas dicas de tipo não sejam estritamente aplicadas em tempo de execução, elas são extremamente úteis para ferramentas de análise estática de código, melhorando a legibilidade do código e ajudando na detecção precoce de erros.

### Tipagem Fraca vs. Forte

* **Tipagem Forte**: Em linguagens com tipagem forte, uma vez que uma variável é atribuída a um tipo, não pode ser automaticamente tratada como outro tipo sem uma conversão explícita. Python é um exemplo de linguagem com tipagem forte. Isso significa que operações que misturam tipos incompatíveis (como adicionar um número a uma string) resultarão em erro.
    
* **Tipagem Fraca**: Linguagens com tipagem fraca permitem maior flexibilidade nas operações entre diferentes tipos, fazendo conversões de tipo implícitas. JavaScript é um exemplo clássico, onde você pode adicionar números a strings sem erros, resultando em uma concatenação de texto.
    
### Tipagem Estática vs. Dinâmica

* **Tipagem Estática**: Linguagens de tipagem estática, como Java e C++, exigem que o tipo de cada variável seja declarado explicitamente no momento da compilação. Isso ajuda a detectar erros de tipo antes da execução do programa, aumentando a segurança do tipo e potencialmente melhorando o desempenho.
    
* **Tipagem Dinâmica**: Python é um exemplo de linguagem com tipagem dinâmica, onde os tipos são inferidos em tempo de execução e não precisam ser declarados explicitamente. Isso oferece flexibilidade e rapidez no desenvolvimento, mas pode aumentar o risco de erros de tipo que só serão detectados em tempo de execução.

Exercício será tipar o desafio da aula 03

```python
nome_valido = False
salario_valido = False
bonus_valido = False

while not nome_valido:
    try:
        nome = input("Digite seu nome: ")

        # Verifica se o nome está vazio
        if len(nome) == 0:
            raise ValueError("O nome não pode estar vazio.")
        # Verifica se há números no nome
        elif any(char.isdigit() for char in nome):
            raise ValueError("O nome não deve conter números.")
        else:
            print("Nome válido:", nome)
            nome_valido = True
    except ValueError as e:

# Exibe os dados lidos do arquivo CSV
for registro in dados:
    print(registro)
```

## 4. Funções

### Importância na Engenharia de Dados

Funções permitem modularizar e reutilizar código, essencial para processar e analisar grandes conjuntos de dados. Na engenharia de dados, funções são usadas para encapsular lógicas de transformação, limpeza, agregação e análise de dados, tornando o código mais organizado e mantendo a qualidade do código.

As funções em programação são abstrações poderosas que permitem encapsular blocos de código para realizar tarefas específicas. Elas servem não apenas para organizar o código e torná-lo mais legível, mas também para abstrair complexidades, permitindo que os programadores pensem em problemas em um nível mais alto. Uma função bem projetada pode ser vista como um "mini-programa" dentro de um programa maior, com sua própria lógica e dados de entrada e saída.

Um exemplo clássico dessa abstração é a ordenação de uma lista. Vamos primeiro desenvolver uma função simples em Python que ordena uma lista usando o algoritmo de ordenação por seleção, um método simples mas eficaz para listas pequenas e médias. Em seguida, mostraremos como essa tarefa pode ser realizada de forma mais direta usando o método `sort()` built-in do Python, que é uma abstração fornecida pela linguagem para realizar a mesma tarefa.

### Função de Ordenação Personalizada

```python
# Implementação do algoritmo de ordenação por seleção
lista = [64, 34, 25, 12, 22, 11, 90]

for i in range(len(lista)):
    for j in range(i+1, len(lista)):
        if lista[i] > lista[j]:
            lista[i], lista[j] = lista[j], lista[i]

# Ordenando a lista
print("Lista ordenada com função personalizada:", lista)
```

### Usando o Método Built-in `sort()`

O Python fornece uma abstração poderosa através do método `sort()`, que pode ordenar listas in-place de maneira eficiente e com uma sintaxe simples.

```python
# Lista de exemplo
lista_exemplo = [64, 34, 25, 12, 22, 11, 90]

# Ordenando a lista com sort()
lista_exemplo.sort()

print("Lista ordenada com método built-in:", lista_exemplo)
```

A comparação entre a função de ordenação personalizada e o método `sort()` ilustra perfeitamente como as abstrações em programação, como funções e métodos built-in, podem simplificar significativamente o desenvolvimento de software. Enquanto a implementação manual de um algoritmo de ordenação é uma ótima maneira de entender os princípios da computação e algoritmos, na prática, utilizar abstrações fornecidas pela linguagem pode economizar tempo e evitar erros, permitindo que os desenvolvedores se concentrem na lógica de negócios e nos aspectos de alto nível de seus programas.

#### Exemplo: Transformação de Dados com Funções

Suponhamos a necessidade de limpar e transformar nomes de usuários em um conjunto de dados. Uma função dedicada pode ser implementada para essa tarefa.

```python
def normalizar_nome(nome: str) -> str:
    return nome.strip().lower()

nomes = [" Alice ", "BOB", "Carlos"]
nomes_normalizados = [normalizar_nome(nome) for nome em nomes]
print(nomes_normalizados)
```

Cada um desses temas desempenha um papel crucial na engenharia de dados, permitindo a manipulação eficiente de dados, garantindo a qualidade do código e facilitando a análise de dados complexos. Esses exemplos ilustram como listas, dicionários, type hints e funções podem ser aplicados para resolver problemas comuns encontrados nesse campo.

### Exercícios de Funções

16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
17. Crie uma função que receba um número como argumento e retorne `True` se o número for primo e `False` caso contrário.
18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

O padrão de nomeação de funções em Python segue convenções que são amplamente aceitas pela comunidade Python, conforme recomendado no PEP 8, o guia de estilo para a codificação em Python. Adotar esses padrões não só melhora a legibilidade do código, mas também facilita a compreensão e a manutenção por outros desenvolvedores, incluindo aqueles novos ao projeto.

### Padrões de Nomes de Funções

* **Nomes Claros e Descritivos**: O nome de uma função deve ser descritivo o suficiente para indicar sua finalidade ou o que ela faz. Por exemplo, `calcular_area_circulo` é mais descritivo do que simplesmente `area`.
    
* **Letras Minúsculas com Sublinhados**: Funções em Python devem ser nomeadas usando letras minúsculas, com palavras separadas por sublinhados para melhorar a legibilidade. Este estilo é algumas vezes referido como snake_case. Por exemplo, `carregar_dados_usuario` é um bom exemplo.
    
* **Evitar Nomes Genéricos**: Nomes como `processo`, `executar`, ou `fazer_algo` são muito genéricos e não fornecem informações suficientes sobre o que a função faz. Prefira nomes que ofereçam um nível adequado de detalhe.
    
* **Evitar Abreviações Obscuras**: Embora abreviações possam encurtar o nome de uma função, elas podem tornar o código menos acessível para outros desenvolvedores. Por exemplo, `calc_media_notas` é preferível a `cmn`.
    
* **Prefixos com Verbo**: Muitas vezes, funções realizam ações, então é útil iniciar o nome da função com um verbo que descreve essa ação, como `obter_`, `calcular_`, `processar_`, `validar_` ou `limpar_`.

Na Python, a tipagem de funções é facilitada pelo uso de "Type Hints" (Dicas de Tipo), uma característica introduzida no Python 3.5 através do PEP 484. Os Type Hints permitem aos desenvolvedores especificar os tipos de dados esperados para os parâmetros de uma função e o tipo de dado que a função deve retornar. Embora essas dicas de tipo não sejam estritamente aplicadas em tempo de execução, elas são extremamente úteis para ferramentas de análise estática de código, melhorando a legibilidade do código e ajudando na detecção precoce de erros.

### Tipagem dos Parâmetros

Você pode especificar o tipo de cada parâmetro ao definir uma função. Isso indica claramente o tipo de argumento que a função espera.

```python
def saudacao(nome: str, idade: int) -> str:
    return f"Olá, {nome}, você tem {idade} anos."
```

### Parâmetros com Valores Default

Python permite definir valores default para os parâmetros, o que significa que a função pode ser chamada sem fornecer todos os argumentos, desde que os omitidos tenham um valor padrão definido. A tipagem funciona da mesma forma, com o tipo sendo especificado antes do sinal de igual.

```python
def saudacao(nome: str, idade: int = 30) -> str:
    return f"Olá, {nome}, você tem {idade} anos."
```


![imagem_03](./pic/3.jpg)

Refatorar nosso código usando Dicionário, Type Hint e Funcões.


![imagem_04](./pic/4.jpg)

Duvidas