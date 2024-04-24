'''
    Dicionários em python (tipo dict)
    Dicionários são estruturas de dados do tipo
    par de "chave" e "valor"
    Chaves podem se consideradas como o "índice"
    que vimos na lista e podem ser de tipos imutáveis
    como: str, int, float, bool, tuple, etc.
    O valor pode ser de qualquer tipo, incluindo outro dicionário
    Usamos as chaves - { } - ou a classe dict para criar dicionários
    Imutáveis : str, int, float, bool, tuple
    Mutável: dict, list

    pessoa = {
        'nome' : 'Fábio',
        'sobrenome' : 'Florêncio',
        'idade' : 18,
        'altura' : 1.8,
        'endereços': [
            {'rua:' 'tal tal', 'número': 123}
            {'rua': 'outra rua', 'número': 321}
        ]
    }

'''

pessoa = {
    'nome': 'Fabio',
    'sobrenome': 'Florêncio',
    'idade': 18,
    'altura': 1.75,
    'endereços': [
        {'rua': 'Fatec', 'número': 123},
        {'rua': 'Etec', 'número': 321},
    ],
}

print(pessoa)

# ! dict sobrescreve, mas não permiti imprimir o restante dos dados. Faça o teste
# pessoa = dict(nome='Jones', sobrenome= 'Mendonça')

# acessa
print(pessoa['nome'])

#for chave in pessoa:
#    print(chave)

print()

for chave in pessoa:
    print(chave, pessoa[chave])
