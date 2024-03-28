'''

    Aula 47 - Exercício

    Peça ao usuário para digitar seu nome
    Peça ao usuário para digitar sua idade
    Se nome e idade forem digitados:
        Exiba:
            Seu nome é {nome}
            Seu nome é  invertido é {nome invertido}
            Se nome contém (ou não) espaços
            Seu nome tem {n} letras
            A primeira letra do seu nome é {letra}
            A última letra do seu nome é {letra}
    Se nada for digitado em nome ou idade:
        exiba "Desculpe, você deixou campo vazios:"
'''

nome = input(f'Digite seu nome completo:')
idade = input(f'Digite seu idade:')

if nome and idade != "":
    print(f'Seu nome é {nome}')
    print(f'Seu nome invertido é:{nome[::-1]}')
    if ' ' in nome: 
        print(f'Seu nome tem espaços!')    
    else:    
        print(f'Não tem espaços!')

    print(f'Você nome tem {len(nome)} letra(s).')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[len(nome) - 1]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print(f'Desculpe, você deixou os campos vazios:')