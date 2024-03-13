'''

    Aula 26 - Operadores
    
    Divisão / = sempre retorna um número de ponto flutuante
    Divisão // = sempre retorna um númento inteiro desde que a conta permita

'''

adicao = 10 + 10
print('Adição: ', adicao)

subtracao = 10 - 5
print('Subtração:', subtracao)

multiplicacao = 10 * 10
print('Multiplicação:', multiplicacao)

divisao = 10 / 2.2
print('Divisão:', divisao ,' ', type(divisao))

# dessa forma o resultado vai sair "truncado"
divisao_inteira = 10 // 2.2
print('Divisão interira:', divisao_inteira , '' , type(divisao_inteira))

divisao1 = 10 / 3
print('Divisão:', divisao1)

divisao2 = 10 // 3
print('Divisão: ', divisao2)

exponenciacao = 2 ** 10
print('Exponenciaçao:', exponenciacao)

modulo = 55 % 2
print('Módulo', modulo)

print(10 % 3)
print(10 % 2 == 0)


