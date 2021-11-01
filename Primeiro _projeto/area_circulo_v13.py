import math
import sys


def circulo(raio):
    return math.pi * float(raio) ** 2


def help():
    print("""É necessário informar o raio do círculo.
Sintaxe: {} <raio>""".format(sys.argv[0]))


if len(sys.argv) < 2:
    help()
    sys.exit(1)
# else:
raio = sys.argv[1]
area = circulo(raio)
print('Area do', area)
