'''
    Aula 155 - Como importar coisas do seu próprio módulo (ponto de vista do __main__)

    Entendendo os seus próprios módulos Python
    O primeiro módulo executado chama-se __main___
    Você pode importar outro módulo inteiro ou parte do módulo
    O python conhece a pasta onde o __main__ está e as pastas abaixo dele.
    Ele não reconhece pastas e módulos acima do __main__ por padrão, caso utilizar pasta fora do main,
    vai ser necessário utilizar sys.path
    O Python conhece todos os módulos e pacotes presentes nos caminhos sys.path


'''
import teste_m
from teste_m import variavel_modulo

print('Este módulo se chama', __name__)
print(teste_m.variavel_modulo)

print('Importando somente a variável',variavel_modulo)


