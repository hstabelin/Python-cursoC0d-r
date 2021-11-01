def fibonacci(pen, ult):
    # se o valor do ultimo for maior que 500 ele sai da funcao
    if ult > 500:
        return
    print(ult)
    # condicao não atingida, ele adiciona a funcao os novos valores
    fibonacci(ult, ult + pen)


fibonacci(0, 1)
