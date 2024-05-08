## 1 - Método isdigit(): Retorna True se todos os caracteres da string forem dígitos e a string não estiver vazia.

```python
string = "12345"
print(string.isdigit())  # Saída: True
```
## 2 - Método isnumeric(): Retorna True se todos os caracteres da string forem caracteres numéricos (dígitos) e a string não estiver vazia.

```python
string = "12345"
print(string.isnumeric())  # Saída: True
```

## 3 - Método isdecimal(): Retorna True se todos os caracteres da string forem caracteres decimais (dígitos) e a string não estiver vazia.

```python
string = "12345"
print(string.isdecimal())  # Saída: True
```

## 4 - Conversão com try e except: Você também pode tentar converter a string em um número usando a função int() ou float() e capturar a exceção se a conversão falhar.

```python
string = "12345"
try:
    num = int(string)
    print("É um número inteiro:", num)
except ValueError:
    print("Não é um número inteiro.")

try:
    num = float(string)
    print("É um número decimal:", num)
except ValueError:
    print("Não é um número decimal.")

```