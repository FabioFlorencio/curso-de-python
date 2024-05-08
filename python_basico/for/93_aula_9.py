'''
    Aula 93 - split, join e strip são métodos muito úteis da str
    
    split e join com list e str
    split - divide uma string
    strip - corta os espaços do ínicio e do fim
    rstrip - corta o espaço da direira
    lstrip - corta o espaço da esquerda
    join - une uma string

'''

frase = '       Olha só que    , coisa interessante'

# Manter essa variável caso precise
lista_frases = frase.split(',')

lista_frases_alterada = []

# enumerate retorna uma tupla com índice e o valor
for i,frase in enumerate(lista_frases):
    lista_frases_alterada.append(lista_frases[i].split())

print(lista_frases)    











