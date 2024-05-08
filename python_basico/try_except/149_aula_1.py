'''

    Aula 149. (Parte 1) try e except para tratar exceções

    Nesse exemplo demostra uma má prática, sendo necessário tratar o erro.
    Em python exceções são classes

    Em exception utiliza Pascal case

    Pascal Case é a prática de escrever palavras compostas ou frases de modo que cada palavra
    ou abreviatura comece com uma letra maiúscula.
 

'''

# Execute o código abaixo para gerar o erro e pegar o nome da exceção
#a = 18
#b = 0
#print('Linha 10')
#c = a / b

try:
    a = 18
    # comente a variável 'b' abaixo para pegar a exceção
    #b = 0
    print('Linha 26')
    c = a / b
    print('Linha 2')
except ZeroDivisionError:
    print('Dividiu por zero!')  
except NameError:
    print('Nome b não está definido!')      

print('Continuar')    