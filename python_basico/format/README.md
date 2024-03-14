# 📝Função `format()` em Python 🐍

## O que é a função `format()`? 🔄

A função `format()` é uma maneira flexível de formatar strings em Python. Ela permite inserir valores de variáveis em strings formatadas de forma dinâmica.

## Como usar a função `format()`? 💡

Para usar a função `format()`, você pode criar uma string com espaços reservados (chamados de "campos de substituição") e depois chamar a função `format()` para substituir esses espaços reservados pelos valores das variáveis. Por exemplo:

```python
nome = "Clodoaldo"
idade = 30
altura = 1.75

mensagem = "Olá, meu nome é {}, tenho {} anos e minha altura é {} metros.".format(nome, idade, altura)
print(mensagem)

```

## O que é o método `format()` com parâmetros nomeados? 🔄

O método `format()` com parâmetros nomeados é uma forma poderosa de formatar strings em Python, permitindo que você especifique os valores das variáveis diretamente na string, usando nomes específicos.

## Como usar o método `format()` com parâmetros nomeados? 🚀

Para usar o método `format()` com parâmetros nomeados, você precisa adicionar nomes específicos nos espaços reservados da string e, em seguida, passar os valores correspondentes como argumentos nomeados para o método `format()`. Por exemplo:

```python
mensagem = "Olá, meu nome é {nome}, tenho {idade} anos e minha altura é {altura} metros.".format(nome="Clodoaldo", idade=30, altura=1.75)
print(mensagem)

```

## O que é o método `format()` com parâmetros nomeados usando índices? 🆔

O método `format()` com parâmetros nomeados usando índices é uma forma conveniente de formatar strings em Python, permitindo que você especifique os valores das variáveis diretamente na string usando índices específicos.

## Como usar o método `format()` com parâmetros nomeados usando índices? 🚀

Para usar o método `format()` com parâmetros nomeados usando índices, você precisa adicionar os índices dos parâmetros na string e, em seguida, passar os valores correspondentes como argumentos nomeados para o método `format()`. Por exemplo:

```python
mensagem = "Olá, meu nome é {0}, tenho {1} anos e minha altura é {2} metros.".format("João", 30, 1.75)
print(mensagem)

```
