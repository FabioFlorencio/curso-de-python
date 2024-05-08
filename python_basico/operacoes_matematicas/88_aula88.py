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
print('Quantidade de itens na linha zero:',len(nomes[0]))
print('Quantidade de caracter da linha 1, coluna 1:',(len(nomes[1][1])))
print('Soma dos valores da linha 2 coluna 2 é :',sum(nomes[2][2]))

print()

print('Imprime somente os números:',nomes[2][2])
print(nomes)
print(type(nomes[2]))
print(type(nomes[2][2]))




