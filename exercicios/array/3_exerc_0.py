"""
3 - Criar um vetor A com 15 elementos inteiros. Construir um vetor B de
mesmo tipo e tamanho, sendo que cada elemento do vetor B deverá
ser o quadrado do respectivo elemento de A, ou seja:
B[i] = A[i] * A[I].
"""

vetor_a, vetor_b = zip(*[(num, num * num) for num in range(1,16)])

print('Vetor A:', vetor_a)
print('Vetor B:', vetor_b)

