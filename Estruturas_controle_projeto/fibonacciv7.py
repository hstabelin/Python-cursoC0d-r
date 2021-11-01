def fibonacci(quantidade):
    #   quantidade está atrelado a função e define a quantidade de valores
    #   que comparados com a lista
    resultado = [1, 2]
# while resultado[-1] < limite: tiramos o limite do while e vamos
# usar o infinito (True)
    while True:
        resultado.append(sum(resultado[-2:]))
#       condicação para o break ser executado
#       se a qntdade de valores na lista "len", for igual o valor
#       informado na função "quantidade", ele exect o break
        if len(resultado) == quantidade:
            break
    return resultado


for fib in fibonacci(10):
    print(fib)
