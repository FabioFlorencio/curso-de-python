'''
    Aula 169 - 
    Crie uma função zipper 
    Exercício - Unir listas
    O trabalho dessa função será unir duas
    lista na ordem.
    Use todos os valores da menor lista.
    ['Salvador', 'Ubatuba', 'Belo Horizonte']
    ['BA', 'SP', 'MG', 'RJ']
    Resultado
    [('Salvador', 'BA'),('Ubatuba','SP'), ('Belo Horizonte', 'MG')]

'''

# Nesse exemplo ignorou rj

def zipper(lista1,lista2):
    cont_list = min(len(lista1), len(lista2))
    unir_list = [(lista1[i], lista2[i]) for i in range(cont_list)]
    return unir_list

l1 = ['Salvador','Ubatuba', 'Belo Horizonte']    
l2 = ['BA', 'SP', 'MG', 'RJ']


unir_list = zipper(l1,l2)

# Se as listas tiverem tamanhos diferentes, o zip vai parar de agrupar quando a menor lista terminar.
print('Juntar lista de forma tradicional:',unir_list, sep='\n')
print('Juntar lista usando a função zip:',unir_list, sep='\n')

