"""
2 - Criar um vetor A com 8 elementos inteiros. Construir um vetor B de
mesmo tipo e tamanho e com os elementos do vetor A multiplicados
por 2, ou seja: B[i] = A[i] * 2.
"""

vetor_a,vetor_b = zip(*[(num,num *2) for num in range(1,9)])

print('Vetor A:',vetor_a)
print('Vetor B:',vetor_b)