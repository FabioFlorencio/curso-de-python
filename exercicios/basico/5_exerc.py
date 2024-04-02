'''

    Faça um Programa que converta metros para centímetros.    

'''

und_metros = input(f'Digite um número para ser convertido de metros para centímetros:')

conv_und_cent = float(und_metros) * 100
print(f'Metros equivalem a {conv_und_cent:.2f} centímetros\n')


# Usando a função pow

und_metros = input(f'Digite um número para ser convertido de metros para centímetros:')

conv_und_cent = float(und_metros) * pow(10,2)
print(f'Metros equivalem a {conv_und_cent:.2f} centímetros\n')


