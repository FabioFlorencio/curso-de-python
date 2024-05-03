'''

    126 - aula Introdução ao tipo set em pyton(conjuntos)
    Representados graficamente pelo diagrama de venn
    Sets em python são mutáveis, porém aceitam apenas
    Tipos imutáveis como valor interno, exemplo incluir uma list dentro de sets
    mas uma tupla aceita

    set é parecido com dicionário, mas não tem chave
    sets são eficientes para remover valores duplicados
    - Não aceitam valores mutáveis
    - Não aceita set dentro de set
    - Não aceita dentro de set dados mutáveis(list,dicionário)
    - Seus valores serão sempre únicos;
    - Não tem índexes;
    - Não garantem ordem;
    - São iteráveis (for, in, not in)

'''

# s1 = {1,2,3, [1,2,3]}
# Set não aceita valores mutáveis
# print(s1)

s2 = {1, 2, 3, (4, 5, 6)}
# Convertendo o conjunto em uma lista e acessando o elemento
lista_s2 = list(s2)

print(lista_s2[3])  
print(lista_s2[3][0]) # Saída: 4

print('Existe o número 5 na lista?',5 in lista_s2[3])


