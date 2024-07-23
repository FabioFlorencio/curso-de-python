'''
    Aula 157 - Introdução aos packages (pacotes) em Python

'''

from teste_pacote.arq_teste import soma_do_modulo

import teste_pacote.arq_teste

from teste_pacote import arq_teste

from sys import path

#    Pacote       Arquivo do pacote de origem
#      |             |

print(__name__)
print(soma_do_modulo(1,2))

print(teste_pacote.arq_teste.soma_do_modulo(2,2))

print(arq_teste.soma_do_modulo(3,3))
print(*path, sep='\n')
