'''
    Aula avulsa sobre a função sorted no dicionário

'''


dicionario = {'c': 3, 'a': 1, 'b': 2}

# Ordenar por chave
dicionario_ordenado_por_chave = dict(sorted(dicionario.items()))
print("Ordenado por chave:", dicionario_ordenado_por_chave)

# Ordenar por valor
dicionario_ordenado_por_valor = dict(sorted(dicionario.items(), key=lambda item: item[1]))
print("Ordenado por valor:", dicionario_ordenado_por_valor)

# Ordenar por valor de forma decrescente
dicionario_ordenado_por_valor_desc = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))
print("Ordenado por valor (descrescente):", dicionario_ordenado_por_valor_desc)
