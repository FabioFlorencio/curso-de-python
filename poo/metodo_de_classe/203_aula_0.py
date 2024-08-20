# Aula 203 - Mantendo estados dentro da classe


class Camera:

    def __init__(self,nome, filmando = False):

        self.nome = nome
        self.filmando  = filmando

    def filmar(self):
        print( f'{self.nome} está filmando!')
        self.filmando = True
    
c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()

print(c1.filmando)
print(c2.filmando)





