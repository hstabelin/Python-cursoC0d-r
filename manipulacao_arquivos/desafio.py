import csv
from urllib import request


def read(url):
    with request.urlopen(url) as entrada:
        # guarda o arquivo da url na variavel entrada
        with open('cidades.txt', 'w') as saida:
            # criei o arquivo de saida e dei permissão
            print('Baixando CSV....')
            dados = entrada.read().decode('latin1')
        # pegou o arquivo da variavel entrada, leu e salvou em dados
            print('Download Completo!')
            for cidade in csv.reader(dados.splitlines()):
                # Roda o for a ler os dados do csv armazenados
                #  na variavel dados
                print(f'{cidade[8]}: {cidade[3]}', file=saida)
                # printa os dados armazenados em cidade,
                #  das colunas 9[8] e 3[4]


read(r'http://files.cod3r.com.br/curso-python/desafio-ibge.csv')
# informei na função a url onde está o arquivo
# o r na frente, é para que ele não intreprete o url, seja literal
print('Arquivo salvo')
