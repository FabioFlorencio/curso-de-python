
texto = """
Python é uma linguagem de programação poderosa e versátil.
É amplamente utilizada em desenvolvimento web, ciência de dados, 
inteligência artificial e muito mais.
"""

# localiza posição do ponto e vírgula
posicao_ponto = texto.find('.')
posicao_virgula = texto.find(',')


if posicao_ponto!= posicao_virgula:
    
    retirar_texto = texto[posicao_ponto + 1:posicao_virgula]
    print("Texto retirado entre o ponto e a vírgula:", retirar_texto)
else:
    print("Ponto e vírgula não foram encontrados no texto.")
