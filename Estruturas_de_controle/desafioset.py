PALAVRAS_PROIBIDAS = {'futebol', 'religiao', 'politica'}
textos = ['Joao gosta de futebol',
          'Marcio gosta de politica',
          'A praia esta otima']


for texto in textos:
    intersecao = PALAVRAS_PROIBIDAS.intersection(set(texto.lower().split()))
    if intersecao:
        print('Texto proibido:', texto, intersecao)
    else:
        print('texto autorizado:', texto)
