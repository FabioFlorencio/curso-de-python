

lista = [10,20,30,40,'Fábio']

lista.append(50)

print('nova lista', lista)

# o menos -1 sempre será o último item da minha lista, dessa forma fica mais fácil retirar esse item
del lista[-1]

print('qtd:',len(lista))

# Limpa lista
lista.clear()
print('Função limpar lista:',lista)

# print(lista)

