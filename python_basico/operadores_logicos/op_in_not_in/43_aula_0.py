'''

    Aula 43 - Operadores in e not in

    Operadores in e not in
    Strings são iteráveis = permiti acessar item a item
    0 1 2 3 4 
    F á b i o
    -5 -4 -3 -2 -1
'''

nome = 'Fábio'

print(nome[1])
print(nome[-4])

print(10 * '-')

print('Os caracters "Fá" está na string nome?','Fá' in nome)
print('Os caracters "Florêncio" está no string nome?',"Florêncio" in nome)

print(10 * '-')

print('Não tem "Florêncio" no string nome?',"Florêncio" not in nome)