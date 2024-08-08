"""
5 - Criar um vetor A com 10 elementos inteiros. Construir um vetor B de
mesmo tipo e tamanho, sendo que cada elemento do vetor B deverá
ser o respectivo elemento de A multiplicado por sua posição (ou
índice), ou seja:
B[i] = A[i] * i.
"""

vetor_a, vetor_b = zip(*[(num,num * i) for i,num in enumerate(range(1, 11))])

print('Vetor A:', vetor_a)
print('Vetor B:', vetor_b)


