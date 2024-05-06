'''

    Aula 149. (Parte 1) try e except para tratar exceções

    Nesse exemplo demostra uma má prática, sendo necessário tratar o erro.
    
'''

try:
    a = 18
    b = 0
    print('Linha 10')
    c = a / b
    print('Linha 2')
except:
    print('Dividiu por zero!')    

print('Continuar')    