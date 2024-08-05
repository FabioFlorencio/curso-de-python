# Aula avulsa
# Funções Lambda
# Exemplo usando filter


def acima_de_30(numeros):
    return numeros > 30

lista = [numero for numero in range(10,60,10)]

print(lista)
lista_filtrada = list(filter(acima_de_30, lista))

print(lista_filtrada) # output 40, 50
