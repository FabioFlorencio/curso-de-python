''''

    Aula 32 - Formatação de strings com o método format

'''

a = 'A'
b = 'B'
c = 1.1

# nesse exemplo foi utilizado a mudança da posição dos índices
# Pode ser ordenado conforme a escolha
string = 'a = {0} \t b = {2:.4f} \t c ={1}'

# seria uma outra forma de chamar o método format
format1 = string.format(a,b,c)

format2 = 'a = {}\t b = {}\t c = {:.3f}'.format(a,b,c)    

print(format2)
print(format1)