PALAVRAS_PROIBIDAS = ('futebol', 'religiao', 'politica')

textos = ['João gosta de futebol',
          'Marcio gosta de politica',
          'A praia esta otima']


for texto in textos:
    found = False
    for palavra in texto.lower().split():
        if palavra in PALAVRAS_PROIBIDAS:
            print('Texto possui palavra proibida:', palavra)
            found = True
            break

    if not found:
        print('Texto autorizado: ', texto)
