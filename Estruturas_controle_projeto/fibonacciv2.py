def fibonacci(limite):
    pen = 0
    ult = 1
    print(f'{pen}, {ult}', end=',')
    while ult < limite:
        proximo = pen + ult
        print(proximo, end=',')
        pen = ult
        ult = proximo


fibonacci(1000000)
