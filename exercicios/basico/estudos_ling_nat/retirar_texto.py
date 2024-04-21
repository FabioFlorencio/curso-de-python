'''

    Com base no texto abaixo faça um código para extrair o texto que está entre o primeiro (.) e a primeira (,)
    Utilize a função find para localizar as posições do ponto e da virgula no texto e em seguida faça um laço for
    para gerar um texto novo com os caracteres entre o ponto e a virgula


'''


texto = """
Python é uma linguagem de programação poderosa e versátil.
É amplamente utilizada em desenvolvimento web, ciência de dados, 
inteligência artificial e muito mais.
"""

# localiza posição do ponto e vírgula
posicao_ponto = texto.find('.')
posicao_virgula = texto.find(',')

print(posicao_ponto)
print(posicao_ponto + 1)
print(posicao_virgula)


if posicao_ponto!= posicao_virgula:
    
    # Acrescente + 1 para não imprimir o número 1
    retirar_texto = texto[posicao_ponto + 1:posicao_virgula]
    print(f"Texto retirado entre o ponto e a vírgula:{retirar_texto}")
else:
    print("Ponto e vírgula não foram encontrados no texto.")
