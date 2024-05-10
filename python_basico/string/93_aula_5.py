    '''
    Aula 93 - split, join e strip são métodos muito úteis da str
    split e join com list e str
    split - divide uma string
    strip - corta os espaços do ínicio e do fim
    rstrip - corta o espaço da direira
    lstrip - corta o espaço da esquerda
    join - une uma string

'''

frase = 'Olha só que, coisa interessante!'
lista_frases = frase.split(',')


for i,frase in enumerate(lista_frases):
    print(lista_frases[i])

print()    

for i,frase in enumerate(lista_frases):
    # retira o espaço
    print(lista_frases[i].strip())







