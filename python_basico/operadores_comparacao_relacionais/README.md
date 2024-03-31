# Operadores de Comparação em Python 🔄

Os operadores de comparação em Python são utilizados para comparar valores e expressões. Eles retornam um valor booleano, indicando se a comparação é verdadeira (True) ou falsa (False). Vamos explorar os operadores de comparação mais comuns em Python!

Operadores de Comparação Disponíveis 🛠️
Aqui estão os operadores de comparação disponíveis em Python:

- `==`: Igual a - Verifica se dois valores são iguais.
- `!=`: Diferente de - Verifica se dois valores não são iguais.
- `>`:  Maior que - Verifica se o valor da esquerda é maior que o valor da direita.
- `<`:  Menor que - Verifica se o valor da esquerda é menor que o valor da direita.
- `>=`: Maior ou igual a - Verifica se o valor da esquerda é maior ou igual ao valor da direita.
- `<=` Menor ou igual a - Verifica se o valor da esquerda é menor ou igual ao valor da direita.

## Exemplos de Uso dos Operadores de Comparação 📝

```python
# Verifica se dois valores são iguais
print(5 == 5)   # Saída: True
print(5 == 10)  # Saída: False

# Verifica se dois valores são diferentes
print(5 != 10)  # Saída: True
print(5 != 5)   # Saída: False

# Verifica se o valor da esquerda é maior que o valor da direita
print(10 > 5)   # Saída: True
print(5 > 10)   # Saída: False

# Verifica se o valor da esquerda é menor que o valor da direita
print(5 < 10)   # Saída: True
print(10 < 5)   # Saída: False

# Verifica se o valor da esquerda é maior ou igual ao valor da direita
print(10 >= 5)  # Saída: True
print(5 >= 10)  # Saída: False
print(5 >= 5)   # Saída: True

# Verifica se o valor da esquerda é menor ou igual ao valor da direita
print(5 <= 10)  # Saída: True
print(10 <= 5)  # Saída: False
print(5 <= 5)   # Saída: True

```

## Encadeamento de Operadores de Comparação 🔗

É possível encadear operadores de comparação em Python para criar expressões mais complexas. Por exemplo:

```python
x = 10
print(5 < x < 15)  # Saída: True
print(20 < x < 30) # Saída: False
```