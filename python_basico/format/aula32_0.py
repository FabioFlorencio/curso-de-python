''''

    Aula 32 - 32. Formatação de strings com o método format

'''

a = 'A'
b = 'B'
c = 1.1
string = 'a = {} | b = {}'

# seria uma outra forma de chamar o método format
format1 = string.format(a,b)


#               |-----------------------> 1º argumento       
#               |       |---------------> 2º argumento        
#               |       |         |-----> 3º argumento
#               |       |         |
formato = 'a = {}\t b = {}\t c = {:.3f}'.format(a,b,c)    

print(formato)
print(format1)