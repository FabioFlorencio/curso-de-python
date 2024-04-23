# Lista de chaves e valores alternados
lista = ["a", 1, "b", 2, "c", 3]

# Criar dicionário a partir da lista usando um loop for
dicionario = {}
for i in range(0, len(lista), 2):
    chave = lista[i]
    print(chave,i)
    valor = lista[i + 1]
    dicionario[chave] = valor

print(dicionario)
print(type(dicionario))