"""
1 - Criar um vetor A com 5 elementos inteiros. Construir um vetor B de
mesmo tipo e tamanho e com os "mesmos" elementos do vetor A, ou
seja, B[i] = A[i].
"""

# zip* descompacta (x,x)
vetor_a, vetor_b = zip(*[(x,x) for x in range(1,6)])
vetor_c = [(x,x) for x in range(1,6)]

vetor_a = list(vetor_a)
vetor_b = list(vetor_b)

print('Vetor A:', vetor_a, id(vetor_a))
print('Vetor B:', vetor_b, id(vetor_b))
print(vetor_c)


