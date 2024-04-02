'''
    Aula -  86 - Exercício - exiba os índices da lista (aula com solução)
    exemplo de for com indice

'''

lista = ['Maria', 'Helena', 'Luiz']


# Passa a informação do indice inicial e final de uma lista
indices = range(len(lista))

print(indices)

# Dessa forma utiliza o indice(zero) para iniciar o for e utiliza o indices que recebeu o valor da qtd do conteúdo de lista para controlar o array.

for indice in range(len(lista)):
    print(f'índice: {indice} - {lista[indice]}')

print('\nUtiliza índice "0" para demonstrar a posição do array\n')    

for indice in indices:
    print(f'índice: {indice} - {lista[indice]}')

print('\nUtiliza índice + 1 para demonstrar a posição do array\n')    

for indice in indices:
    print(f'índice: {indice + 1} - {lista[indice]}')    

