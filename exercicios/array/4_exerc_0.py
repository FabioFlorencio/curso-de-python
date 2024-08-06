"""
4 - Criar um vetor A com 15 elementos inteiros. Construir um vetor B de
mesmo tamanho, sendo que cada elemento do vetor B deverá ser a
raiz quadrada do respectivo elemento de A, ou seja:
B[i] = sqrt(A[i])..
"""
import math

# Criando o vetor A com 15 elementos inteiros (de 1 a 15)
vetor_a = [num for num in range(1, 16)]

vetor_b = [math.sqrt(num) for num in vetor_a]

print('Vetor A:', vetor_a)
print('Vetor b:',[round(num,2)for num in vetor_b])



