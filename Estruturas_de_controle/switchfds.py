def get_fds(dia):
    calend = {
        1: 'Domingo - FDS',
        2: 'Segunda - Semana',
        3: 'Terca - Semana',
        4: 'Quarta - Semana',
        5: 'Quinta - Semana',
        6: 'Sexta - Semana',
        7: 'Sabado - FDS',
    }
    return calend.get(dia, '*invalido')


for dia in range(0, 8):
    print(f'{dia}, {get_fds(dia)}')
