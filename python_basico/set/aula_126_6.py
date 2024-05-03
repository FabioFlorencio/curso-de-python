'''

    126 - aula Introdução ao tipo set em pyton(conjuntos)
    Representados graficamente pelo diagrama de venn
    Sets em python são mutáveis, porém aceitam apenas
    Tipos imutáveis como valor interno, exemplo incluir uma list dentro de sets
    mas uma tupla aceita

    set é parecido com dicionário, mas não tem chave
    sets são eficientes para remover valores duplicados
    
    Operadores úteis:

    União | união (union) - une
    Intersecção & (intersection) - itens presentes em ambos
    diferença - Itens presentes apenas no set da esquerda
    diferença simétrica ^ - itens que não estão em ambos

'''

s1 = {1, 2, 3}
s2 = {2, 3, 4}

s3 = s1 | s2
print('Conjunto união:',s3)

s3 = s1 & s2
print(f'Intersecção de s1 e s2: {s3}')

s3 = s1 - s2
print(f'Verifica o valor que é diferente de s1 em comparação com s2: {s3}')

s3 = s2 -s1
print(f'Verifica o valor que é diferente de s2 em comparação com s1: {s3}')


s3 = s1 ^ s2
print('Itens que não estão presentes em ambos:' ,s3)








