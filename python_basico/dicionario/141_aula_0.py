"""
    Aula 141 - Dictionary Comprehension e Set Comprehension

"""


produto = {
    'nome' : 'caneta azul',
    'preco' : 2.5,
    'categoria' : 'escritório'    
}

for chave,valor in produto.items():
    print(chave,valor)


dc = {
    chave: valor 
    for chave, valor
    in produto.items()

}
print(dc)