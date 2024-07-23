'''
    Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
    da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros 
    quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões
    de 3,6 litros, que custam R$ 25,00.

    Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor.
    Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.

'''


import math

def calcular_latas(area):
    litros_necessarios = area / 6 * 1.1  
    latas = math.ceil(litros_necessarios / 18)
    custo = latas * 80
    return latas, custo

def calcular_galoes(area):
    litros_necessarios = area / 6 * 1.1 
    galoes = math.ceil(litros_necessarios / 3.6)
    custo = galoes * 25
    return galoes, custo


def calcular_mistura(area):
    litros_necessarios = area / 6 * 1.1  
    latas = math.floor(litros_necessarios / 18)
    restante_litros = litros_necessarios - (latas * 18)
    galoes = math.ceil(restante_litros / 3.6)
    custo = (latas * 80) + (galoes * 25)
    return latas, galoes, custo

# Programa principal
def main():
    area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

    latas, custo_latas = calcular_latas(area)
    print(f"Usando apenas latas de 18 litros: {latas} latas, Custo: R${custo_latas:.2f}")

    galoes, custo_galoes = calcular_galoes(area)
    print(f"Usando apenas galões de 3,6 litros: {galoes} galões, Custo: R${custo_galoes:.2f}")

    latas, galoes, custo_mistura = calcular_mistura(area)
    print(f"Usando uma mistura de latas e galões: {latas} latas e {galoes} galões, Custo: R${custo_mistura:.2f}")

if __name__ == "__main__":
    main()










