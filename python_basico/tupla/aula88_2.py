'''

    Aula 88 - Tipo de tuple(tuplas)
    
    tipo tupla - Uma lista imutável
    Seria uma lista que não vai ser removido ou adicionado valor, que se mantém estática.
    Exemplo: lista de cidades, estados
    Obs. Tupla são mais eficientes e rápidas

'''

# exempo de criação de tupla
nomes = (('Fábio', 'Francisca', 'Vitória') , ('José', 'Clodoaldo','Juliana') , ['Maria José' , 'Jones', (1,2,3,4)])

print(nomes)
print('Linha 0 coluna 0:',nomes[0][0])
print('Linha 1 coluna 1:', nomes[1][1])
print('Linha 2 coluna 2 item 2:', nomes[2][2][2])
print('Imprime a linha inteira 2:',nomes[2])

# Atribuir valor em uma list
nomes[2][1] = 'Mendonça'

print()

print('Imprime somente os númros:',nomes[2][2])
print(nomes)
print(type(nomes[2]))
print(type(nomes[2][2]))




