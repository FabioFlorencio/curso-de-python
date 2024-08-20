# @property - um getter no mode Pythônico
#  getter - um método para obter um atributo
# cor -> get_cor()
# modo pytônico - modo do python de fazer coisas
# @property é uma propriedade do objeto, ela é um método que se comporta como um atributo
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo

class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    @property
    def cor(self):
        # sobreescre o atributo da instância
        return self.cor_tinta

    # def get_cor(self):    
    #     return self.cor
    
caneta = Caneta('Azul')    

print('Usando o método property:',caneta.cor)
print(caneta.cor)
print(caneta.cor_tinta)