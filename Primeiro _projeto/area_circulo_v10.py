import math
import sys


def circulo(raio):
    return math.pi * float(raio) ** 2


if len(sys.argv) < 2:
    print("""\
É necessário informar o raio do círculo.
Sintaxe: {} <raio>""".format(sys.argv[0]))
else:
    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do', area)
