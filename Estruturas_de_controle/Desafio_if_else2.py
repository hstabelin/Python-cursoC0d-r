def faixa_etaria(idade):
    if idade in range(0, 18):
        return 'Menor de Idade'
    elif idade in range(19, 40):
        return 'Adulto'
    elif idade in range(41, 64):
        return 'Quarentao'
    elif idade in range(65, 100):
        return 'Melhor idade'
    elif idade > 100:
        return 'Centenario'
    else:
        return 'Valor inválido'


idades = (7, 8, 9, 22, 35, 65, 79, 51, 99, 102)
for idade in idades:
    print(f'{idade}: {faixa_etaria(idade)}')
