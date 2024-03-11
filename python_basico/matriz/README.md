# Matrizes em Python 🧮

Em Python, uma matriz é uma coleção bidimensional de elementos, organizados em linhas e colunas. Embora Python não tenha um tipo de dados nativo chamado `matriz`, você pode representá-la facilmente usando listas aninhadas.

## O que é uma Matriz?

Uma matriz em Python é essencialmente uma lista de listas, onde cada lista interna representa uma linha da matriz. As operações com matrizes, como adição, multiplicação e acesso aos elementos, podem ser realizadas usando técnicas simples de indexação.

## Exemplo de uma Matriz em Python 🐍

Vamos criar uma matriz simples e realizar algumas operações básicas:

```python
# Criando uma matriz 2x3
matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

# Acessando elementos da matriz
print(matriz[0][0])  # Saída: 1
print(matriz[1][2])  # Saída: 6

# Iterando sobre os elementos da matriz
for linha in matriz:
    for elemento in linha:
        print(elemento, end=" ")
    print()
# Saída:
# 1 2 3 
# 4 5 6

```

## Operações com Matrizes em Python 🛠️
Você pode realizar várias operações com matrizes em Python, como adição, multiplicação, transposição, entre outras. Aqui está um exemplo simples de adição de matrizes:

```python
# Definindo duas matrizes
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

# Inicializando uma matriz para armazenar o resultado da adição
resultado = [[0, 0], [0, 0]]

# Adicionando as matrizes A e B
for i in range(len(A)):
    for j in range(len(A[0])):
        resultado[i][j] = A[i][j] + B[i][j]

# Exibindo o resultado
for linha in resultado:
    print(linha)
# Saída:
# [6, 8]
# [10, 12]

```
