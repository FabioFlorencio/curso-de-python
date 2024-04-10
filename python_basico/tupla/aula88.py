'''

    Aula 88 - Tipo de tuple(tuplas)
    
    tipo tupla - Uma lista imutável
    Seria uma lista que não vai ser removido ou adicionado valor, que se mantém estática.
    Exemplo: lista de cidades, estados
    Obs. Tupla são mais eficientes e rápidas

'''

nomes = 'Fábio', 'Francisca', 'Vitória'

print(nomes[1])
print(nomes)

# outra forma de criar uma tupla

carros = ('Fusca', 'Brasília', 'monza', 'gol')
print(carros,end='\n\n')

# converter tupla em lista e vice-versa

print('Transformando tupla em lista: ',list(nomes))
print('Transformando tupla em lista: ',list(carros),'\n')

print('Transformando list em tupla',tuple(nomes))
print('Transformando list em tupla',tuple(carros))


for nome in nomes:
    print(nome)





