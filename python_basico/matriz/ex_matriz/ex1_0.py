'''
    Desafio 87

    Execício:

    a) Soma de todos os valores pares digitados.
    b) Soma dos valores da terceira coluna.
    c) O maior valor da segunda linha.
    
'''    
matriz = [[0,0,0],[0,0,0],[0,0,0]]

soma_par = maior_valor_seg_linha = soma_valores_terceira_coluna = 0

for l in range(0,3):    
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para[{l} , {c}]:'))
        if matriz[l][c] % 2 == 0:
            soma_par+= matriz[l][c]
        if c == 2:
            soma_valores_terceira_coluna+= matriz[l][c]                        

print('-=' * 30)

# imprime matriz
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()        

print(f'A soma dos valores pares é:{soma_par}')
print(f'A soma dos valores da terceira coluna é:{soma_valores_terceira_coluna}')


