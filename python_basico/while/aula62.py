'''

    Aula 62 - while + continue - pulando alguma repetição
    fala sobre continue
    continue -> pula a instrução

'''

contador = 0

while contador <= 100:
    contador+= 1    

    if contador == 6:
        print('Não vou mostrar o número 6.') 
        continue    

    if contador >= 10 and contador <= 20:
        print('não vou mostrar o número ',contador)
        continue

    print(contador)

    if contador == 30:
        break

