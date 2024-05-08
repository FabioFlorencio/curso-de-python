'''

    Aula 150. (Parte 2) try e except para tratar exceções    

    Pascal Case é a prática de escrever palavras compostas ou frases de modo que cada palavra
    ou abreviatura comece com uma letra maiúscula.
 
    Exception trata qualquer erro, como se fosse uma classe superior   

    # É possível tratar dois erros ao mesmo tempo, mas não é recomendado 

'''


try:
    a = 18
    b = 0
    #print(b[0])    
    print('Linha 1'[1000])
    print('Linha 23')

except NameError:
    print('Nome b não está definido!')
     
except (TypeError, IndexError) as error:
    # error é uma instância de uma classe
    print('TypeError + IndexError')
    print('Mensagem:',error)
    print('Nome do erro:', error.__class__.__name__)       
except Exception:
    print('ERRO DESCONHECIDO.')
print('Continuar')    