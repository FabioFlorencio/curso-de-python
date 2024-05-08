'''
    Aula 58 -  tipos built-in, documentação, tipo imutáveis,

'''


txt = 'Fábio Florêncio'
# da posição 4 acrescenta o argumento "ÓÓÓ"
outra_variavel = f'{txt[:4]}óóó{txt[5:]}'
outra_variavel2 = f'{txt[:4]}óóó{txt[:7]}'


print(txt)
print(outra_variavel,'\n')
print(outra_variavel2,'\n')

print(id(txt))
print(id(outra_variavel),'\n')


num1 = 1
print(type(num1))

num1 = 'oi'
print(type(num1),'\n')

print(len(outra_variavel))

