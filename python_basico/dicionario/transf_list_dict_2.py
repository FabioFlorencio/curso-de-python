valores = ["apple", "banana", "cherry"]  # Lista de valores que queremos usar como valores no dicionário
dicionario = {indice: valor for indice, valor in enumerate(valores)}  # Utilizando compreensão de dicionário

# 'enumerate(valores)' cria um iterador que fornece pares de (índice, valor) para cada elemento em 'valores'
# 'indice' será o índice do elemento e 'valor' será o próprio elemento
# A compreensão de dicionário cria um dicionário onde a chave é o índice e o valor é o valor correspondente da lista

print(dicionario)  
print(type(dicionario))
