with open('pessoas.csv') as arquivo:
    with open('pessoas.txt', 'w') as saida:
        # criei o arquivo pessoas e dei permissão de escrita. Nomeei como saida
        for registro in arquivo:
            pessoa = registro.strip().split(',')
            print('Nome: {}, Idade: {}'.format(*pessoa), file=saida)
    # inclui a formatação como variavel pessoa
    # no print, inclui o 2° argumento para exportar o arquivo criado saida.
if arquivo.closed:
    print('arquivo fechado')
