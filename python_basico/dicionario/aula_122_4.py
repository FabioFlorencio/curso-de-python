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
'''
print(id(pessoa))
pessoa.update({
    'nome': 'novo valor',
    'altura': '1.75'
})
'''
# usando argumentos nomeados
#pessoa.update(nome='novo valor',altura = 1.75)
# não esqueça a virgula no final, senão vai gerar um erro
# tupla = ('nome','novo valor'),
# tupla = (('nome','novo valor'),('altura', 1.75))
lista = [['nome', 'novo valor'],['altura', 1.75]]


# outra forma de usar update
pessoa.update(lista)


print(pessoa)
print(type(pessoa))