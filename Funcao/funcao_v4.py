#! python
def resultado(**podium):
    for posicao, piloto in podium.items():
        print(f'{posicao} -> {piloto}')


resultado(Primeiro='L.Marcio', Segundo='Bistro',
          Terceiro='Vertap', Quarto='Ligon')
