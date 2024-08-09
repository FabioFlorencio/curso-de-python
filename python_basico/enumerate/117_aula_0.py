

'''

    Aula 117 - Exercícios - somando dus listas
    _ é usado como uma convenção para indicar que o valor não será usado

'''

lista_a = [1,2,3,4,5,6,]
lista_b = [1,2,3,4]
lista_soma = []

for i, _ in enumerate(lista_b):
    lista_soma.append(lista_a[i] + lista_b[i])

print(lista_soma)