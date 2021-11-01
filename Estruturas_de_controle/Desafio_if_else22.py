def riqueza(valor):
    if valor in range(0, 100000):
        return 'Pobre'
    elif valor in range(100001, 1000000):
        return 'Rico'
    elif valor in range(1000000, 10000000):
        return 'Milionario'
    elif valor > 10000001:
        return 'Bilionario'
    else:
        return 'Valor invalido'


Patrimonio = (50000, 500000, 10000, 102435235, 1331331, 13143243, 3141431, 0.1)
for valor in Patrimonio:
    print(f'{valor}: {riqueza(valor)}')
