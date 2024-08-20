# Aaula - 213 - @property + setter - getter no modo Pythônico
# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que inicia com um ou dois underlines não devem ser usados fora da classe


class Caneta:
    def __init__(self,cor):
        self.cor_tinta = cor
        self._cor = self.cor_tinta


    @property
    def cor(self):
        return self.cor_tinta
    
caneta = Caneta('Azul')    


