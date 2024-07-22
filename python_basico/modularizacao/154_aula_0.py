'''
    Aula 154 - Modularização - Entendendo os seus próprios módulos e sys.path no Python

    Entendendo os seus próprios módulos Python
    O primeiro módulo executado chama-se __main___
    Você pode importar outro módulo inteiro ou parte do módulo
    O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
    Ele não reconhece pastas e módulos acima do __main__ por padrão
    O Python conhece todos os módulos e pacotes presentes nos caminhos sys.path


'''
import sys

import teste_m
print('Este módulo se chama', __name__)
print(sys.path)
print()
print(*sys.path, sep='\n')