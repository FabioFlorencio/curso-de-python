'''

A farmácia DrogaLimpa coletou dados de altura (em metros) e peso (em quilogramas) de diversos clientes, disponibilizando os dados em listas conforme abaixo:
altura = [1.65, 1.75, 1.80, 1.70, 1.68, 1.72, 1.78, 1.60, 1.85, 1.73, 1.69, 1.75, 1.62, 1.80, 1.77, 1.68, 1.79, 1.81, 1.76, 1.74]
peso = [65, 70, 75, 80, 60, 68, 72, 58, 90, 72, 65, 70, 55, 78, 79, 62, 85, 88, 70, 75]

Utilize a biblioteca NumPy para calcular o IMC de cada pessoa na amostra e, em seguida, identifique quantas pessoas estão abaixo do peso, dentro do peso normal, com sobrepeso e obesas com base nos intervalos de IMC estabelecidos.


'''

import numpy as np


alt_vet = [1.65, 1.75, 1.80, 1.70, 1.68, 1.72, 1.78, 1.60, 1.85, 1.73, 1.69, 1.75, 1.62, 1.80, 1.77, 1.68, 1.79, 1.81, 1.76, 1.74]
peso_vet = [65, 70, 75, 80, 60, 68, 72, 58, 90, 72, 65, 70, 55, 78, 79, 62, 85, 88, 70, 75]


alt_vet_numpy = np.array(alt_vet)
peso_vet_numpy = np.array(peso_vet)

# calculo IMC
calc_imc = peso_vet_numpy / (alt_vet_numpy ** 2)

BASE_IMC_PESO_ABAIXO = 18.5
BASE_IMC_PESO_NORMAL = 24.9
BASE_IMC_PESO_SOBREPESO = 25
BASE_IMC_OBESO = 30

peso_abaixo = np.sum(calc_imc <= BASE_IMC_PESO_ABAIXO)
peso_normal = np.sum((calc_imc >= BASE_IMC_PESO_ABAIXO) & (calc_imc <= BASE_IMC_PESO_NORMAL))
sobrepeso = np.sum((calc_imc >= BASE_IMC_PESO_SOBREPESO) & (calc_imc <= BASE_IMC_OBESO))
obeso = np.sum(calc_imc >= BASE_IMC_OBESO)


print("Quantidade de pessoas abaixo do peso:", peso_abaixo)
print("Quantidade de pessoas com peso normal:", peso_normal)
print("Quantidade de pessoas com sobrepeso:", sobrepeso)
print("Quantidade de pessoas obesas:", obeso)
