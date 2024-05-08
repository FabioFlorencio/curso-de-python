''''
    Aula 74 - Como o for funciona por baixo dos panos? (next, iter, iterável e iterador)

    Iterável -> str, range, etc (__iter__)
    Iterável -> è um método que entrega uma coisa por vez
    Iterável -> Todo iterável tem um método iter
    next -> me entregue o próximo valor disponível
    iter -> me entregue seu iterador

    Obs. Quando se utiliza um for a primeira coisa que solicitada é o método iter

'''

texto = 'Fábio'.__iter__() # __iter__()


print('Utilizar a função ou método iter, terá acesso o local da mémoria.')
print('Usando o método iter',texto)
#print('Usando a função iter:',iter(texto),'\n')

# Para usar o método next é necessário utilizar antes o método iter

print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())


