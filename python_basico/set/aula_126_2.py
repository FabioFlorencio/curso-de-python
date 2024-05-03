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

s2 = {1,2,3}
print(3 in s2)


