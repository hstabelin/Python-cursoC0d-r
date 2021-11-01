def fibonacci(limite):
    pen = 0
    ult = 1
    print(f'{pen}, {ult}', end=',')
    while ult < limite:
        pen, ult = ult, pen + ult
        print(ult, end=',')


fibonacci(1000000)
