# list.extend -> serve para incluir mais de um elemento em uma lista, diferente do método append, que deve ser usaso para incluir somente um elemento, caso seja usado incorretamente, o método vai criar mais uma lista dentro o array

vendedores = ['João','Maria','Jones','Camila']
novos_vendedores = ['Fábio','Gabriel']

# Nova lista de vendedores
vendedores.extend(novos_vendedores)

print(vendedores)

novas_contratacoes = ['Dani','Japonês']

# Vai adcionar um novo array a lista dessa forma
vendedores.append(novas_contratacoes)

print(vendedores)


# dessa forma separa o nome letra por letra
vendedores.extend('Mendes')

print(vendedores)
print(len(vendedores))
