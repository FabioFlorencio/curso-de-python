'''
    Aula 89 - enumerate para enumerar valores de iteráveis (pegar índices)
    enumerate utiliza o método iterator
    Nesse exemplo não funciona o for devido que o método interator já foi usado

'''

lista = ['Fábio', 'Francisca', 'Vitória']
lista.append('José')

lista_enumerada = enumerate(lista)
print(lista_enumerada)
print(next(lista_enumerada))
print(next(lista_enumerada))
print(next(lista_enumerada))
print(next(lista_enumerada))

print()

# Não funciona o for devido do uso do interator, é como se o "ponteiro permanecesse no final da lista" impedindo retomar o índice
# para contornar essa situação vai ser necessário criar um iterator por vez
# Veja o exemplo aula89_1 para ver o exemplo de como contornar essa situação.

for item in lista_enumerada:
    print(next(item))

print('Teste')    