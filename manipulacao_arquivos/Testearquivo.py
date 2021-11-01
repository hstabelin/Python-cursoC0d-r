with open('Teste_Risco.csv') as arquivo:
    with open('teste risco.txt', 'w') as said:
        for registro in arquivo:
            doc = registro.strip().split(';')
            print('Risco: {}, Controle: {}, Teste: {}'.format(*doc), file=said)
