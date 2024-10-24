# 📋 Tabela de revisão rápida ⚡

Aqui está uma tabela de revisão sobre as principais sintaxes em Python.


- [📋 Tabela de revisão rápida ⚡](#-tabela-de-revisão-rápida-)
  - [🎲 Tipos de dados](#-tipos-de-dados)
  - [🚦 Condicionais](#-condicionais)
    - [if](#if)
    - [If-else](#if-else)
    - [If-elif-else](#if-elif-else)
    - [If aninhados](#if-aninhados)
    - [Assignment expression](#assignment-expression)
    - [Ternários](#ternários)
  - [✔️ Operadores ❌](#️-operadores-)
    - [Operadores Lógicos](#operadores-lógicos)
    - [Operadores in e not in](#operadores-in-e-not-in)
  - [📥 Entrada de dados](#-entrada-de-dados)
    - [Input](#input)
  - [🎯 Interpolação](#-interpolação)
    - [Interpolação com espaçamento](#interpolação-com-espaçamento)
    - [Interpolação com espaçamento controlado](#interpolação-com-espaçamento-controlado)
  - [🛡️ Exceções](#️-exceções)
    - [Try except](#try-except)
  - [🔄 Estrutura de repetição](#-estrutura-de-repetição)
    - [For usando range](#for-usando-range)
    - [For usando reversed](#for-usando-reversed)
    - [For usando enumerate](#for-usando-enumerate)
    - [For usando enumerate e range](#for-usando-enumerate-e-range)
    - [While com contador](#while-com-contador)
    - [While com valor booleano](#while-com-valor-booleano)
  - [⚖️ Operadores relacionais](#️-operadores-relacionais)
    - [Compara valores ou expressões](#compara-valores-ou-expressões)
  - [✍️ Operações com string](#️-operações-com-string)
    - [Tamanho da string](#tamanho-da-string)
    - [Acessar Caracteres](#acessar-caracteres)
    - [Converter para Maiúsculas/Minúsculas](#converter-para-maiúsculasminúsculas)
    - [Remover Espaços em Branco](#remover-espaços-em-branco)
    - [Substituir Substrings](#substituir-substrings)
    - [Dividir e Juntar Strings](#dividir-e-juntar-strings)
    - [Verificar Substrings](#verificar-substrings)
  - [Format](#format)
    - [Format simples](#format-simples)
    - [Format() com parâmetros nomeados](#format-com-parâmetros-nomeados)
    - [Format() com parâmetros nomeados usando índices](#format-com-parâmetros-nomeados-usando-índices)
  - [🧮 Operações matemáticas](#-operações-matemáticas)
    - [Max](#max)
    - [Min](#min)
    - [Sum](#sum)
    - [Mean](#mean)
    - [Count](#count)
    - [Round](#round)
    - [Range](#range)
    - [Random](#random)
      - [Random inteiros](#random-inteiros)
      - [Random float](#random-float)
      - [Random sample](#random-sample)
  - [📋 List](#-list)
    - [List método: append, pop, del](#list-método-append-pop-del)
    - [List método: insert](#list-método-insert)
    - [List método: extend](#list-método-extend)
    - [List método: copy, clear](#list-método-copy-clear)
    - [List método: sort , sort(reverse=True)](#list-método-sort--sortreversetrue)
  - [🧩 zip](#-zip)
    - [zip](#zip)
    - [Desembrulhando listas com zip(\*...):](#desembrulhando-listas-com-zip)
  - [🧩 Utilização de Matriz](#-utilização-de-matriz)
    - [Matriz](#matriz)
  - [🔒 Utilização de Tupla](#-utilização-de-tupla)
    - [Tupla](#tupla)
  - [📖 Utilização de Dicionário](#-utilização-de-dicionário)
    - [Dicionário](#dicionário)
  - [🛠️ Função](#️-função)
    - [Função aninhada](#função-aninhada)
    - [Função simples chamando outra função](#função-simples-chamando-outra-função)
    - [Função passando argumento para outra função](#função-passando-argumento-para-outra-função)
    - [Função usando operadores relacionais no return](#função-usando-operadores-relacionais-no-return)
    - [Função usando lambda simples](#função-usando-lambda-simples)
    - [Função usando lambda com filter](#função-usando-lambda-com-filter)
    - [Função usando lambda com sorted](#função-usando-lambda-com-sorted)
    - [Função usando \*args](#função-usando-args)



## 🎲 Tipos de dados

| Tipos de dados |  Descrição                   |
|:---------------|:-----------------------------|
|`int`           | (números inteiros)           |
|`float`         | (números de ponto flutuante) |
|`str`           | (strings)                    |
|`bool`          | (valores booleanos)          |
|`list`          | (listas)                     |
|`tuple`         | (tuplas)                     | 
|`dict`          | (dicionários)                | 

## 🚦 Condicionais

### if

```python
x = 10
if x > 5:
    print("x é maior que 5")
```

### If-else

```python
x = 3
if x > 5:
    print("x é maior que 5")
else:
    print("x não é maior que 5")
```

### If-elif-else

```python
x = 7
if x > 10:
    print("x é maior que 10")
elif x > 5:
    print("x é maior que 5 mas menor ou igual a 10")
else:
    print("x é 5 ou menor")
```

### If aninhados
```python
x = 8
y = 15

if x > 5:
    if y > 10:
        print("x é maior que 5 e y é maior que 10")
    else:
        print("x é maior que 5 mas y não é maior que 10")
else:
    print("x não é maior que 5")
```

### Assignment expression

```python
idade = 18
genero = "Homem"
valida_alistamento = False
msg_parts= []

if (valida_alistamento := (idade >= 16) & (genero.casefold() == "homem")):
    msg_parts.append("Vai ser analisado seu alistamento. Retorne daqui 15 dias!\n")    
else:
    msg_parts.append("Você não está apto ao alistamento.")    

if valida_alistamento:
    msg_parts.append('Você foi convocado! Bem vindo ao exercito!')    


msg = ''.join(msg_parts)
print(msg)
```
### Ternários

```python
x = 8
mensagem = "{} é maior que 5" if x > 5 else "{} não é maior que 5"
print(mensagem.format(x))
```
---

## ✔️ Operadores ❌


### Operadores Lógicos

```python
numero = int(input("Digite um número: "))

if (numero >= 10 and numero <= 20 and numero % 2 == 0) or (numero >= 21 and numero <= 30 and numero % 2 != 0):
    print(f"O número {numero} é válido.")
else:
    print(f"O número {numero} não é válido.")
```
### Operadores in e not in

```python
nome = 'Fábio'
print('Os caracters "Fá" está no array nome?','Fá' in nome)
print('Não tem "Florêncio" no array nome?',"Florêncio" not in nome)
```
---

## 📥 Entrada de dados

### Input
```python
nome = input("Digite seu nome: ").upper()
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura em metros: "))

print(f"Nome: {nome}, Idade: {idade}, Altura: {altura} metros.")
```
---

## 🎯 Interpolação

### Interpolação com espaçamento

```python


msg ='''
Salário bruto:       R${:>7.2f}
(-)IR (5%):          R${:>7.2f}
(-)INSS (10%):       R${:>7.2f}
(-)Sindicato:        R${:>7.2f}
FGTS (11%):          R${:>7.2f}
Total de descontos:  R${:>7.2f}
Salário Liquido:     R${:>7.2f}
''' 

print(msg.format(*result))
```


### Interpolação com espaçamento controlado

```python
nome = "Alice"
idade = 25
altura = 1.65

# {:<10}: Isso significa que o espaço reservado para o nome terá 10 caracteres de largura, e o nome será alinhado à esquerda
mensagem = "Nome: {:<10} Idade: {:>5} Altura: {:^10.2f}".format(nome, idade, altura)
print(mensagem)
```


---
## 🛡️ Exceções

### Try except

```python
valida = True

while valida:

    primeira_validacao = True

    while primeira_validacao:
       
        num1 = input('Digite um número:')  
                    
        if num1.isnumeric():
            num1 = int(num1)                
            print('Isso é um inteiro:',type(num1),num1)            
            primeira_validacao = False
        else:    
            try:
                num1 = float(num1) 
                print('Isso é um float:',type(num1),num1)                                                                  
                primeira_validacao = False                                                                 
            except ValueError:                               
                print('Isso não é um número.')
                print(type(num1))   

    result = num1 + int('2')
    valida = False    
```

---

## 🔄 Estrutura de repetição

### For usando range 

```python
indice = 0

# Range -> (start,stop,step)
for numero in range(0,22,2):
    print(2,indice,sep=" x ", end=" = ")
    print(numero)
    indice+=1
```

### For usando reversed

```python
indice = 0

lista = [1,2,3,4,5]

for numero in reversed(lista):
    print(numero, end=' ')
```


### For usando enumerate


```python
lista = ['Fábio', 'Francisca', 'Vitória']
for index, item in enumerate(lista):
    print(f'{index}: {item}')
```


### For usando enumerate e range


```python
for i, numero in enumerate(range(0, 22, 2)):
    print(f'2 x {i} = {numero}')
```
### While com contador
```python
contador = 0
while contador <= 10:
    contador+= 1
    print(contador)

print('Acabou')  
```

### While com valor booleano
```python
valida = True
while valida:
    print(valida)
    valida = False    
```

---
## ⚖️ Operadores relacionais

###  Compara valores ou expressões
```python
maior = 2 > 1
maior_ou_igual = 2 >= 2
menor = 1 < 2
menor_ou_igual = 2 <= 2
igual = 'a' == 'a'
diferente = 'a' != 'b'

print(f' 2 é maior que 1: {maior}') 
```
---

## ✍️ Operações com string

###  Tamanho da string
```python
texto = "Olá Mundo"
tamanho = len(texto)
print(tamanho) 
```

### Acessar Caracteres
```python
# Em python as strings são iteráveis, ou seja, é possível acessar uma string letra por letra  
#     Fatiamento de strings | pega uma parte da string
#     012345678
#    -987654321 -> Pode usar números negativos
#    i = índice
#    f = fim
#    p = passo
#    Fatiamento [i:f]:p [::]

texto = "Olá_mundo"
primeiro_caractere = texto[0]
ultimo_caractere = texto[-1]
print(primeiro_caractere)  # Saída: O
print(ultimo_caractere)    # Saída: n
```

### Converter para Maiúsculas/Minúsculas
```python
# Usando os métodos upper() e lower()
texto = "Olá Mundo"
maiusculas = texto.upper()
minusculas = texto.lower()
print(maiusculas)  # Saída: OLÁ MUNDO
print(minusculas)  # Saída: olá mundo
```
### Remover Espaços em Branco
```python
# Usando os métodos strip(), lstrip() e rstrip()
texto = "   Olá Mundo   "
sem_espacos = texto.strip()
print(sem_espacos)  # Saída: Olá Mundo
```
   
### Substituir Substrings
```python
# Usando o método replace()
texto = "Olá Mundo"
novo_texto = texto.replace("Mundo", "Python")
print(novo_texto) 
```

### Dividir e Juntar Strings
```python
# Usando os métodos split() e join()
texto = "Olá Mundo"
palavras = texto.split()  # Divide em uma lista de palavras
print(palavras)  # Saída: ['Olá', 'Mundo']

# Juntando uma lista de strings em uma única string
nova_frase = " ".join(palavras)
print(nova_frase)  # Saída: Olá Mundo
```

###  Verificar Substrings
```python
# Usando o operador in
texto = "Olá Mundo"
contém_olá = "Olá" in texto
print(contém_olá)  # Saída: True
```

## Format

### Format simples

```python
notas = [8, 9, 10] 

media_nota = sum(notas) / len(notas)

msg = []

if media_nota >= 7:        
    msg.append("Aprovado")
    if media_nota == 10:
        msg.append(" com Distinção.")
else:
    msg.append("Reprovado")

# Concatena a mensagem final
txt = ''.join(msg)

print('O aluno foi {}, com média {:.2f}.'.format(txt, media_nota))

```

### Format() com parâmetros nomeados


```python
# Usando f-strings para formatação
nome = "João"
idade = 30
frase = f"Meu nome é {nome} e eu tenho {idade} anos."
print(frase)  # Saída: Meu nome é João e eu tenho 30 anos.

# Usando o método format()
frase_format = "Meu nome é {} e eu tenho {} anos.".format(nome, idade)
print(frase_format)  # Saída: Meu nome é João e eu tenho 30 anos.
```

### Format() com parâmetros nomeados usando índices

```python 
def calc_sal(sal_bruto):

    if sal_bruto > 900:
        if sal_bruto < 1500:
            aliq_aplicada = ALIQ_PERC_5
        elif sal_bruto < 2500:
           aliq_aplicada = ALIQ_PERC_10
        else:
          aliq_aplicada = ALIQ_PERC_20
    else:
        aliq_aplicada = ISENTO

    return sal_bruto, sal_liquido, tot_desc, calc_imposto, calc_inss, calc_sind, calc_fgts
  
sal_bruto = 900         
result = calc_sal(sal_bruto)

# Conte o return para compreender o parâmetro nomeado com índice
msg ='''
Salário bruto:       R${0:>7.2f}
(-)IR (5%):          R${3:>7.2f}
(-)INSS (10%):       R${4:>7.2f}
(-)Sindicato:        R${5:>7.2f}
FGTS (11%):          R${6:>7.2f}
Total de descontos:  R${2:>7.2f}
Salário Liquido:     R${1:>7.2f}
''' 

print(msg.format(*result))
```

---

## 🧮 Operações matemáticas

### Max

```python
# Exemplo com uma lista
lista = [1, 2, 3, 4, 5]
maior_valor = max(lista)
print(f'Maior valor: {maior_valor}')  # Saída: Maior valor: 5

# Exemplo com múltiplos argumentos
maior_valor_args = max(1, 2, 3, 4, 5)
print(f'Maior valor (args): {maior_valor_args}')  # Saída: Maior valor (args): 5
```
### Min

```python
# Exemplo com uma lista
menor_valor = min(lista)
print(f'Menor valor: {menor_valor}')  # Saída: Menor valor: 1

# Exemplo com múltiplos argumentos
menor_valor_args = min(1, 2, 3, 4, 5)
print(f'Menor valor (args): {menor_valor_args}')  # Saída: Menor valor (args): 1
```

### Sum

```python
lista = [1, 2, 3, 4, 5]
# Exemplo com uma lista
soma_valores = sum(lista)
print(f'Soma dos valores: {soma_valores}')  # Saída: Soma dos valores: 15
```
### Mean

```python
import numpy as np

lista = [1, 20, 30, 4, 5,5]

media = np.mean(lista)

print(round(media,4))
```
### Count

```python

lista = [1, 2, 3, 4, 5,5]

elemento = 5
contagem = lista.count(elemento)
print(f'O elemento {elemento} aparece {contagem} vez(es) na lista.')  

# Contando o número de elementos na lista
numero_elementos = len(lista)
print(f'Número de elementos na lista: {numero_elementos}')  
```
### Round

```python
# Exemplo com um número flutuante
numero = 3.14159
arredondado = round(numero, 2)
print(f'Número arredondado: {arredondado}')  # Saída: Número arredondado: 3.14
```

### Range

```python
lista = [numero for numero in range(1,12,2)]

print(lista)
```

### Random

#### Random inteiros

```python
numero_aleatorio = random.randint(1, 10)
print(f'Número aleatório: {numero_aleatorio}')
```

#### Random float

```python
import random

random_floats = []

# Loop para gerar 10 números float aleatórios entre 1 e 100
for i in range(10):
    numero_aleatorio_float = random.uniform(1, 100)
    random_floats.append(round(numero_aleatorio_float,2))

# Imprime a lista de números aleatórios
print(f'Números aleatórios (float): {random_floats}')
```
#### Random sample

```python
import random

vetor_a, vetor_b = zip(*[(num, num + num) for num in random.sample(range(1,100),5)])

print('Vetor a:',vetor_a)
print('Vetor b:',vetor_b)
```

---

## 📋 List

### List método: append, pop, del

```python
list = [1,2,3,4,5]

retira_ultimo_valor = list.pop()
list.append(6)
del list[0]
```
### List método: insert  

```python
list = [1,2,3,4,5]

#            |----------- Indica o índice
#            |
#            |   |------- O valor que será inserido na lista
lista.insert(0 , 4)
```
### List método: extend 


```python
# list.extend -> serve para incluir mais de um elemento em uma lista
vendedores = ['João','Maria','Jones','Camila']
novos_vendedores = ['Fábio','Gabriel']

vendedores.extend(novos_vendedores)
```
### List método: copy, clear


```python
list_a = [1,2,3,4,5]

# Dessa forma gera um novo local de memória para lista B usando o método copy()
list_b = list_a.copy()

# Apaga a lista
list_b = list_a.clear()
```

### List método: sort , sort(reverse=True)


```python
lista = [5,1,3,2,4]

# Ordena de forma crescente
lista.sort()

print(lista)

# Ordena de forma decrescente
lista.sort(reverse=True)

print(lista)

```

## 🧩 zip

### zip

```python
lista1 = [1, 2, 3]
lista2 = ['a', 'b', 'c']

# Usando zip para combinar as duas listas
combinado = zip(lista1, lista2)

# Convertendo para uma lista de tuplas
combinado = list(combinado)
print(combinado)  # [(1, 'a'), (2, 'b'), (3, 'c')]

```

### Desembrulhando listas com zip(*...):

```python
combinado = [(1, 'a'), (2, 'b'), (3, 'c')]

# Desembrulhando as listas
lista1, lista2 = zip(*combinado)

# Convertendo para listas
lista1 = list(lista1)
lista2 = list(lista2)

print(lista1)  # [1, 2, 3]
print(lista2)  # ['a', 'b', 'c']

```

---

## 🧩 Utilização de Matriz

### Matriz

```python
matriz = [[0,0,0],[0,0,0],[0,0,0]]

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()        
```
---

## 🔒 Utilização de Tupla

### Tupla

```python
nomes = 'Fábio', 'Francisca', 'Vitória'
carros = ('Fusca', 'Brasília', 'monza', 'gol')
```

## 📖 Utilização de Dicionário

### Dicionário

```python
pessoa = {
    'nome': 'Fábio',
    'sobrenome': 'Florêncio',
    'idade': 18,
    'altura': 1.75
}

print('Retorna somente as chaves do dicionário:',pessoa.keys())
print('Retorna somente os valores do dicionário',pessoa.values())
print('Retorna somente os itens do dicionário',pessoa.items())
```
---

## 🛠️ Função

### Função aninhada

```python
# Exemplo 4: Função aninhada

def saudacao():
    def mensagem():
        return f'Olá!'
    return mensagem()


print(saudacao())
```

### Função simples chamando outra função

```python
# Exemplo 1: Função simples chamando outra função

def saudacao():
    return "Olá!"

def diga_ola():
    mensagem = saudacao()
    print(mensagem)

diga_ola()
```


### Função passando argumento para outra função

```python
def saudacao(nome):
    return f'Olá! {nome}'

def saudar_pessoas(nomes):
    guard_msg = []
    for nome in nomes:
        guard_msg.append(saudacao(nome))

    return guard_msg

lista_nomes = ['Fábio', 'Maria', 'Julia']
result = saudar_pessoas(lista_nomes)

print(*result,sep='\n')
```

### Função usando operadores relacionais no return

```python
def acima_de_30(numero):
    return numero < 30

lista = [numero for numero in range(10,50,10)]

lista_filtrada = list(filter(acima_de_30, lista))

print(lista_filtrada)
```

### Função usando lambda simples

```python
def soma(num1, mum2):
    return num1 + num2

num1 = num2 = 2

# A função lambda precisa ser atribuida a uma variável antes do uso
soma_lambda = lambda num1, num2: num1 + num2

print(soma_lambda(num1, num2))
print(soma_lambda(5, num2))
```

### Função usando lambda com filter

```python
def acima_de_30(numeros):
    return numeros > 30

lista = [numero for numero in range(10,60,10)]

lista_filtrada = list(filter(lambda numero: numero > 30, lista))

print(lista_filtrada)
```
### Função usando lambda com sorted

```python
alunos = [
    {'nome': 'Luiz', 'nota': 'A'},
    {'nome': 'Letícia', 'nota': 'B'},
    {'nome': 'Fabrício', 'nota': 'A'},
    {'nome': 'Rosemary', 'nota': 'C'},
    {'nome': 'Joana', 'nota': 'D'},
    {'nome': 'João', 'nota': 'A'},
    {'nome': 'Eduardo', 'nota': 'B'},
    {'nome': 'André', 'nota': 'A'},
    {'nome': 'Anderson', 'nota': 'C'}                            
]


alunos_agrupados = sorted(alunos, key=lambda aluno: aluno['nota'])

print(alunos_agrupados)
```
### Função usando *args

```python
def soma(*args):
    total = 0 
    for numero in args:
        total+= numero

    return total    
        
result = soma(2,4,6,7,8,3)        

print(f'Total:',result)
```

---