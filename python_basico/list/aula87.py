'''

    Esse código não faz parte do curso. São exercícios baseado nas aulas

'''


altura = [1.50, 1.65, 1.20, 1.89, 1.1, 1, 1.55, 1.40, 1.27, 1.77, 0.9, 0.2]
altura.sort()
cont = len(altura)
print(altura)
print('Posição do vetor:',cont -2 ,',valor:', altura[cont - 2])
print('Maior número do vetor altura:', max(altura))
print('Menor número do vetor altura:', min(altura))
print('Soma todos os valores do vetor:',    sum(altura))



numeros = [3.2, 1, 4, 1, 5, 9, 2, 6, 5]
numeros.sort()  # Classifica em ordem crescente
print(numeros)  # Saída: [1, 1, 2, 3, 4, 5, 5, 6, 9]

numeros.sort(reverse=True)  # Classifica em ordem decrescente
print(numeros)  # Saída: [9, 6, 5, 5, 4, 3, 2, 1, 1]




