"""
    aula 133 - Introdução à função lambda + list.sort e sorted

    A Função ordena está sendo usada para fazer a comparação com a expressão lambda
"""


lista_1 = [    
    {'nome': 'Daniel', 'sobrenome':'Silva'},
    {'nome': 'Eduardo', 'sobrenome': 'Moreira'},
    {'nome': 'Aline', 'sobrenome': 'Souza'}    
]

# a função ordena pode ser apaga que vai funcionar lista_1
def ordena(item):
            
    return item['nome']



lista_1.sort(key=lambda item: item['nome'])

for item in lista_1:
    print(item)

print()



