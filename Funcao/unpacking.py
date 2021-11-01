#! python
def soma_n(*numeros):
    soma = 0
    for n in numeros:
        soma += n
    return soma


print(soma_n(1, 2, 3, 4))
