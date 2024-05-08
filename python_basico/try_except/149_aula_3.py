'''

    Aula 149. (Parte 1) try e except para tratar exceções

    Nesse exemplo demostra uma má prática, sendo necessário tratar o erro.
    Em python exceções são classes

    Em exception utiliza Pascal case

    Pascal Case é a prática de escrever palavras compostas ou frases de modo que cada palavra
    ou abreviatura comece com uma letra maiúscula.
 
    Exception trata qualquer erro, como se fosse uma classe superior   

'''

# execute o código abaixo para gerar o erro e pego o nome da exceção
#b = 0 
#print(b[0])



try:
    a = 18
    b = 0
    print(b[0])    
    print('Linha 21')
    c = a / b
    print('Linha 23')
except ZeroDivisionError:
    print('Dividiu por zero!')  
except NameError:
    print('Nome b não está definido!')
# É possível tratar dois erros ao mesmo tempo       
except (TypeError, IndexError):    
    print('TypeError + IndexError')       
except Exception:
    print('ERRO DESCONHECIDO.')
print('Continuar')    