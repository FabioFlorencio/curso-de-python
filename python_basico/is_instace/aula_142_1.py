'''
    aula 142 - isinstace() - para saber se objeto é de determinado tipo

'''

lista = [
    'a', 1, 1.1, True, [0,1,2], (1, 2),
    {0, 1}, {'nome' : 'Fábio'},
    ]

# Verifica se dentro da lista tem um item da instância set
# Tem que passar os parâmetros para validação


for item in lista:    
    if isinstance(item, set):        
        print('SET\n',item, isinstance(item, set))            

    if isinstance(item, str):   
        print('STR\n',item, isinstance(item, str))
        valida = isinstance(item, str)

    if isinstance(item, (int, float)):
        print('NUM\n',item * 2)
        #print('NUM', item, isinstance(item, (int, float)))
    
print(len(lista))
print(valida)





