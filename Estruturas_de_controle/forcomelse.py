PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')

textos = ['Joao gosta de futebol',
          'Marcio gosta de politica',
          'A praia esta otima']


for texto in textos:
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Palavra proibida:', texto, '** ', palavra, ' **')
            break
    else:
        print('Texto autorizado: ', texto)
