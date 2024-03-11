# Manipulação de Listas em Python 📋

Listas são estruturas de dados fundamentais em Python, que permitem armazenar uma coleção ordenada de elementos. Vamos explorar como manipular listas e entender os conceitos de mutabilidade e imutabilidade!

## Métodos Comuns de Manipulação de Listas 🛠️

Aqui estão alguns métodos comuns que podem ser usados para manipular listas em Python:

- `append()`: Adiciona um elemento ao final da lista.
- `insert()`: Insere um elemento em uma posição específica da lista.
- `pop()`: Remove e retorna o elemento de uma posição específica da lista.
- `del`: Remove um elemento de uma posição específica da lista.
- `clear()`: Remove todos os elementos da lista.
- `extend()`: Adiciona os elementos de outra lista ao final da lista atual.
- `copy()`: Cria uma cópia da lista.

## Exemplos em Python 🐍

Vamos ver como esses métodos funcionam em ação:

### Exemplo 1: Utilizando `append()` 📝

```python
frutas = ["maçã", "banana", "laranja"]
frutas.append("morango")
print(frutas)  # Saída: ["maçã", "banana", "laranja", "morango"]
```

### Exemplo 2: Utilizando `insert()` 🔍

```python
numeros = [1, 2, 3, 5]
numeros.insert(3, 4)
print(numeros)  # Saída: [1, 2, 3, 4, 5]
```

### Exemplo 3: Utilizando `pop()`🎈

```python
letras = ['a', 'b', 'c', 'd']
letra_removida = letras.pop(2)
print(letras)         # Saída: ['a', 'b', 'd']
print(letra_removida) # Saída: 'c'
```

### Exemplo 4: Utilizando `del`🗑️

```python
frutas = ["maçã", "banana", "laranja", "morango"]
del frutas[2]
print(frutas)  # Saída: ["maçã", "banana", "morango"]
```

### Exemplo 5: Utilizando `clear()`🧹

```python
numeros = [1, 2, 3, 4, 5]
numeros.clear()
print(numeros)  # Saída: []

```
### Exemplo 6: Utilizando `extend()`🚀

``` python
pares = [2, 4, 6]
impares = [1, 3, 5]
pares.extend(impares)
print(pares)  # Saída: [2, 4, 6, 1, 3, 5]

```


### Método `id()` para Identificar Objetos 🆔

O método id() em Python retorna o identificador único de um objeto. Vamos ver como usá-lo:

```python
lista1 = [1, 2, 3]
lista2 = lista1

print(id(lista1))  # Saída: Identificador único da lista1
print(id(lista2))  # Saída: Mesmo identificador que lista1

```

### Conceitos de Mutabilidade e Imutabilidade 🔧

Em Python, listas são mutáveis, o que significa que seus elementos podem ser modificados após a criação da lista. Por outro lado, strings e tuplas são imutáveis, o que significa que seus elementos não podem ser alterados após a criação.

