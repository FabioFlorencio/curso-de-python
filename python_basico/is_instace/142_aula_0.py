'''
    aula 142 - isinstace() - para saber se objeto é de determinado tipo

'''

lista = [
    'a', 1, 1.1, True, [0,1,2], (1, 2),
    {0, 1}, {'nome' : 'Fábio'},
    ]



for item in lista:
    # Verifica se dentro da lista tem um item da instância set
    # Tem que passar os parâmetros para validação
    print(item, isinstance(item,set))

print()

for item in lista:
    if isinstance(item,set):
        # add o número 5 na classe sets
        item.add(5)
        print(item, isinstance(item, set))    




