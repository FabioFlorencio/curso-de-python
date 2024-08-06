"""
1 - Criar um vetor A com 5 elementos inteiros. Construir um vetor B de
mesmo tipo e tamanho e com os "mesmos" elementos do vetor A, ou
seja, B[i] = A[i].
"""

vetor_a = [num for num in range(1,6)]
vetor_b = vetor_a.copy()

print('Vetor A:', vetor_a)
print('Vetor B:', vetor_b)
