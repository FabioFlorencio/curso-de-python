'''

    Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius.

'''

temp_farenheit = float(input(f'Digite a temperatura em Fahrenheit:'))
temp_celsius = (5 * (temp_farenheit -32) / 9)

print(f'A temperatura convertida em celsius é: {temp_celsius:.2f}')