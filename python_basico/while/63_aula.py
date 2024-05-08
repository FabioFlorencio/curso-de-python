'''

    Aula 63 -  while + while (laços internos)


'''


qtd_linhas = 3 
qtd_colunas = 3

linha = 1

while linha <= qtd_linhas: 
    print('Linha',linha,':',end="")
    coluna = 1
    while coluna <= qtd_colunas:
        print('[',linha, coluna, end=" ")
        print(']', end="")
        coluna +=1
    linha+= 1
    print()

