# Interpolação em Python 🔄

A interpolação em Python refere-se ao processo de incorporar valores de variáveis ou expressões em strings. Existem várias maneiras de realizar interpolação em Python, cada uma com suas próprias vantagens e sintaxes. Vamos explorar algumas dessas técnicas!

## Uso do Operador de Formatação (%) 🛠️

```python
nome = "Maria"
idade = 30
mensagem = "Olá, %s! Você tem %d anos." % (nome, idade)
print(mensagem)
# Saída: Olá, Maria! Você tem 30 anos.
```

## Utilizando o operador de formatação (%) com múltiplos valores

```python
print('O hexadecimal de %d,%d,%i é %02x %02x %02x' % (255,70,30,255,70,30))
# Saída: O hexadecimal de 255,70,30 é ff 46 1e

```

## Utilizando o operador de formatação (%) com letras maiúsculas

```python
print('O hexadecimal de %d,%d,%i é %02X %02X %02X' % (255,70,30,255,70,30))
# Saída: O hexadecimal de 255,70,30 é FF 46 1E

```

## Uso do Método format() 🔄

O método format() é uma técnica mais flexível e legível para interpolação em Python. Ele permite inserir valores em uma string usando chaves como marcadores de posição e especificando os valores como argumentos do método. Por exemplo:

```python
nome = "João"
idade = 25
mensagem = "Olá, {}! Você tem {} anos.".format(nome, idade)
print(mensagem)
# Saída: Olá, João! Você tem 25 anos.
```

## Uso de F-Strings (Formatted String Literals) 🚀

As F-strings são uma técnica de interpolação introduzida no Python 3.6. Elas oferecem uma sintaxe mais simples e eficiente para interpolação, permitindo inserir valores diretamente em uma string prefixada com o caractere 'f'. Por exemplo:

```python
nome = "Ana"
idade = 35
mensagem = f"Olá, {nome}! Você tem {idade} anos."
print(mensagem)
# Saída: Olá, Ana! Você tem 35 anos.
```


