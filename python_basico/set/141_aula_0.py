"""

    Aula 141 - Dictionary Comprehension e Set Comprehension

"""

lista = [
    {'a','valor a'},
    {'b','valor b'},
    {'c','valor c'},
]

dc = {
    chave: valor
    for chave, valor in lista
}

s1 = {i for i in range(10)}
print(s1)
print(dc)
