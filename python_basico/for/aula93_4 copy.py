'''
    Aula 93 - split, join e strip são métodos muito úteis da str
    split e join com list e str
    split - divide uma string
    join - une uma string

'''

frase = 'Olha só que, coisa interessante!'
lista_frases = frase.split(',')
print(type(lista_frases))


for i,frase in enumerate(lista_frases):
    print(lista_frases[i])

print(lista_frases)  






