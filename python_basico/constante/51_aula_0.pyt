'''
    Aula 51 - Variáveis, constantes e complexidade de código
    Esse exemplo mostra como quebrar a linha de um código muito extenso usando "\" junto de condição
'''

velocidade = 50
local_carro = 100

RADAR_1 = 60
LOCAL_1 = 100
RADAR_RANGE = 1

if velocidade > RADAR_1:
    print('Velocidade carro passou do radar 1')

if local_carro >= (LOCAL_1 - RADAR_RANGE) and \
    local_carro <= (LOCAL_1 + RADAR_RANGE):
    print('Carro multado em radar 1')
