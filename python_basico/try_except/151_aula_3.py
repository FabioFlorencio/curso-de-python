'''

    Aula - 151. try, except, else e finally + Built-in Exceptions


    try sempre precisa de outro bloco
    finally sempre será executado, mesmo que ocorra um erro

'''

try:
    print(111)
    # mesmo com erro, finally será executado
    8/0
except ZeroDivisionError:
    print('Dividiu por zero')
else:
    print('Não deu erro!')            
finally:
    print(2 )

