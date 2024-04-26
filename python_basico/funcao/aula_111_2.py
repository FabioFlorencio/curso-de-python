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

# args é uma convenção comum para se referir a uma sequência de argumentos
# Dessa forma seria uma forma de não declarar vários argumentos
def soma(*args):    
    return sum(args)

print()

test = soma(1,2,3)

print(test)
