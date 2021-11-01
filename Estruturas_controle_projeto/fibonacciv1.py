def fibonacci():
    pen = 0
    ult = 1
    print(f'{pen}, {ult}', end=',')
    while True:
        proximo = pen + ult
        print(proximo)
        pen = ult
        ult = proximo


fibonacci()
