'''
    aula 123. (Parte 2) Métodos úteis nos dicionários Python (dict)

    pop - Apaga um item com a chave especifica (del)
    popitem = Apaga o último item adicionado
    update = Atualiza um dicionário com outro

'''

pessoa = {
    'nome' : 'Fábio',
    'sobrenome' : 'Florêncio',
    'idade' : 18
}

#print(pessoa['nome'])
#print(pessoa.get('nome','Não existe'))


# apaga a chave e retorna o valor
nome = pessoa.pop('nome')
# apaga a chave e o valor 
ultima_chave = pessoa.popitem()

print('O valor da chave foi apagada:',nome)
print('A chave e o valor foi apagado:',ultima_chave)
print(pessoa)