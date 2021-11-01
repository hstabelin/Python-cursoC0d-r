#! python
def risco(*riscos):
    lista = ''.join(f'Risco: {risco}; ' for risco in riscos)
    return lista


print(risco('Risco 1', 'Risco 2', 'Risco 3'))
