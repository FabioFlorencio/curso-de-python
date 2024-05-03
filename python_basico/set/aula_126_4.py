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

    Métodos úteis:
    add, update, clear, discard
    
    update envia vários valores

'''


s1 = set()
s1.add('Olá mundo')
s1.add(1)

# Dessa forma o update trabalha como iterável, cortando a palavra
# s1.update('hello')


# É necessário colocar parêtenses e a virgula para cortar a palavra
s1.update(('hello',))

print(s1)


