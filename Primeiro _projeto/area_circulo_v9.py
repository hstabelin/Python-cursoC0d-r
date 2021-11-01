import math


def circulo(raio):
    return math.pi * float(raio) ** 2


raio = input('Informe o Raio: ')
area = circulo(raio)
print('Area do', area)
