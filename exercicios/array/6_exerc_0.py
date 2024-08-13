"""
6 - Criar dois vetores A e B cada um com 10 elementos inteiros. Construir
um vetor C, onde cada elemento de C é a soma dos respectivos
elementos em A e B, ou seja:
C[i] = A[i] + B[i].
"""

import random

def somar_numeros():
    vetor_a, vetor_b = zip(*[(num, num + num) for num in random.sample(range(1,100),5)])
    return vetor_a, vetor_b

array_a, array_b = somar_numeros()

print(array_a)
print(array_b)
    


