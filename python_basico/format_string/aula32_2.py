''''

    Aula 32 - Formatação de strings com o método format
    Essa aula sobre parâmetro nomeado


'''

a = 'A'
b = 'B'
c = 1.1

# Aqui foi utilizado parâmetro nomeado -> nome1
string = 'b={1} a={0} a={0} c={nome1:.2f}'


#                             |---> tudo que vier depois do parâmetro tem ser nomeado 
#                             |---> Isso é um parâmetro 
#                             |  
format3 = string.format(a,b,nome1=c)

#

format2 = 'a = {}\t b = {}\t c = {:.3f}'.format(a,b,c)    

print(f'Format-2: {format2}')
print(f'Format-3: {format3}')