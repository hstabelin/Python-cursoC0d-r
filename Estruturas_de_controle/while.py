from random import randint

numero_informado = -1
numero_secreto = randint(0, 8)

while numero_informado != numero_secreto:
    numero_informado = int(input('Informe a senha: '))

print('Numero encontrado')
