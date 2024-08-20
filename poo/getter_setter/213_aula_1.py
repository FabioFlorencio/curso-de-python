# Aaula - 213 - @property + setter - getter no modo Pythônico
# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que inicia com um ou dois underlines não devem ser usados fora da classe


class Caneta:
    def __init__(self,cor):
        self._cor = cor


    @property
    def cor(self):
        print('oi')
        return self._cor
    
    @cor.setter
    def cor(self, valor):
        print('Estou no setter:' , valor)
        self._cor = valor
    
caneta = Caneta('Azul')    
caneta.cor = 'Rosa'

caneta.cor


