'''
    Aula 59 -  while e break - Estrutura de repetição (Parte 1)

    Repetições
    while (enquanto)
    Executa uma ação enquanto uma condição for verdadeira
    

'''

valida = True

while valida:
    nome = input(f'Digite seu nome: ')
    print(f'Seu nome é {nome}.')
    valida_saida = input(f'Você quer continuar no programa? Digite "sim" ou "não"')

    if valida_saida == 'não':
        break       

print('Encerrou o programa!')    



