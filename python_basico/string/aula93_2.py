'''
    Aula 93 - split, join e strip são métodos muito úteis da str
    split e join com list e str
    split - divide uma string
    join - une uma string

'''
frase = 'Olha só que, coisa interessante!'
print(len(frase))

print(type(frase))
# corta o texto quando encontra uma vírgula e um espaço
lista_palavras = frase.split(', ')

print('Corta sempre o texto toda vez que encontra uma vírgula e um espaço:',lista_palavras)
print('È transforma em list',type(lista_palavras))
print('Quantos itens tem na lista? ',len(lista_palavras))


