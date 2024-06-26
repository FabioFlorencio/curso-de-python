'''
    Aula 108 - Escopo de funções e módulos em Python + global
    Escopo de funções em python
    O escopo global é o escopo onde todo o código pode atingir.
    Existe o escopo global e local.
    O escopo global é o escopo onde todo o código é alcançavel.
    O escopo local é o escopo onde apenas nomes do mesmo local podem ser alcançados.

'''

x = 1

def escopo():
    global x
    x = 10   
    print(x)

    def outra_funcao():
        global x
        x = 11
        y = 2         
        print(f'{x,y}')
    outra_funcao()
    print(x)
     
    
print(x)
escopo()

print(f'Variavel global:{ x = }')