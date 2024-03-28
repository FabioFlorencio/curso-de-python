'''

     Aula 46 - Fatiamento de strings e a função len
     Em python as strings iteráveis ou seja é possível acessar uma string letra por letra  
     Fatiamento de strings | pega uma parte da string
     012345678
    -987654321
    i = índice
    f = fim
    p = passo
    Fatiamento [i:f]:p [::]


'''

variavel = 'Olá_mundo'
print(variavel)
print(f'fatia palavra do índice 0 ao 4, mas não inclui a posição 4:  {variavel[0:4]}')  
print(f'fatia palavra do índice -9 ao -6, mas não inclui a posição -6:  {variavel[-9:-6]}') 
print(f'Nesse exemplo não é necessário colocar índice\n{variavel[:5]}')
print(f'\nExemplo usando índice negativo:{variavel[-8:-2]}')
print(f'Usando o passo 2: {variavel[0:len(variavel):2]}')
print(f'Usando o passo 3: {variavel[0:9:3]}')
print(f'Usando passo negativo: {variavel[-1:-10:-2]}')
print(f'Inverte:  {variavel[::-1]}')

