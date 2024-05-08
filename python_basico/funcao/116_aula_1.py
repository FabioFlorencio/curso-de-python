'''

    Aula 116 - Closure e funções que retornam outras funções


'''

nomes = ['Maria','Joana','Luiz']

def criar_saudacao(saudacao):    
    def saudar(nome):
        return f'{saudacao}, {nome}'
    return saudar

s1 = criar_saudacao('Bom dia')
s2 = criar_saudacao('Boa noite')


for nome in nomes:
    print(s1(nome))




