"""
    Aula 141 - Dictionary Comprehension e Set Comprehension
    Dicionário comprehension também é possível colocar condicionais
"""

produto = {
    'nome' : 'caneta azul',
    'preco' : 2.5,
    'categoria' : 'escritório'    
}

for chave,valor in produto.items():
    print(chave,valor)

print()

dc = {
    chave: valor.upper()
    if isinstance(valor, str) else valor
    for chave, valor
    in produto.items()

}
print(dc)