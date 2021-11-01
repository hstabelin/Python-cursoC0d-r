def fibonacci(quantidade):
    resultado = [1, 2]
#   while True:
#   substituir o while pelo for, em um range do 2° valor da lista, correr até
#   o valor definido na função "Quantidade"
    for _ in range(2, quantidade):
        #   desta forma ele irá realizar a função do 2° da lista até atingir
        #   o valor de quantiade.
        #   utiziamos o _ no for, para dizer que é uma função não utilizad
        resultado.append(sum(resultado[-2:]))
    return resultado


for fib in fibonacci(20):
    print(fib)
