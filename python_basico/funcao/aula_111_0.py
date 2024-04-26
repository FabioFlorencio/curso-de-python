'''

    Aula 111 - (Parte 1) *args para quantidade de argumentos não nomeados variáveis
    args - Argumento não nomeados
    * - *args (empacotamento e desempacotamento)

'''

#------------- tuple
x, y, *resto = 1,2,3,4   


#     | --------------------- Desempacotamento (1)
#     |   | ----------------- Desempacotamento (2)
#     |   |   |-------------- Empacotamento (3,4) - Gera uma list
print(x , y , resto)
print('Empacotamento gera:',type(resto), resto)


def soma(*args):    
    return sum(*args)

print()


test = soma(resto)    
print(test)
print(type(test))