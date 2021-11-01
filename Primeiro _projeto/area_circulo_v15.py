import math
import sys

ERRO = '\033[91m'
NORMAL = '\033[0m'


def circulo(raio):
    return math.pi * float(raio) ** 2


def help():
    print("""É necessário informar o raio do círculo.
Sintaxe: {} <raio>""".format(sys.argv[0]))


if len(sys.argv) < 2:
    help()
    # sys.exit(1)
elif not sys.argv[1].isnumeric():
    help()
    print(ERRO, 'O raio deve ser numérico.', NORMAL)
else:
    raio = sys.argv[1]
    area = circulo(raio)
    print('Area do', area)
