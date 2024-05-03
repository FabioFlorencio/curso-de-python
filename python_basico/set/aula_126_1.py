'''

    126 - aula Introdução ao tipo set em pyton(conjuntos)
    Representados graficamente pelo diagrama de venn
    Sets em python são mutáveis, porém aceitam apenas
    Tipos imutáveis como valor interno, exemplo incluir uma list dentro de sets
    mas uma tupla aceita

    set é parecido com dicionário, mas não tem chave
    sets são eficientes para remover valores duplicados
    - Não aceitam valores mutáveis
    - Seus valores serão sempre únicos;
    - Não tem índexes;
    - Não garantem ordem;
    - São iteráveis (for, in, not in)

'''

s1 = {1,2,3,3,3,3,3,3,1}

print('Sets remove valores repetidos de dados iteráveis:', s1)

l1 = [1,2,3,3,3,3,3,3,1]
# converte lista em set
s2 = set(l1)

print(type(s2))
# converte set em list
l2 = list(s2)

print('Converte sets em lista:',l2)

