'''
    Aula 93 - split, join e strip são métodos muito úteis da str
    
    split e join com list e str
    split - divide uma string
    strip - corta os espaços do ínicio e do fim
    rstrip - corta o espaço da direira
    lstrip - corta o espaço da esquerda
    join - une uma string

    video (9:20 fala sobre join)

'''

frase = '       Olha só que    , coisa interessante'
print(frase)

# Manter essa list caso precise usar novamente
lista_frases = frase.split(',')
print('Lista_frases tem',len(lista_frases),'itens.')
print('Qual é o tipo de dado:',type(lista_frases))

lista_frases_alterada = []

# enumerate retorna uma tupla com índice e o valor
for i,frase in enumerate(lista_frases):
    lista_frases_alterada.append(lista_frases[i].strip())

print(lista_frases_alterada)    
print()
    
# junta a frase    
frases_unidas = ', '.join(lista_frases_alterada)
print(frases_unidas) 
print()

frases_unidas = '-'.join(lista_frases_alterada)
print(frases_unidas)












