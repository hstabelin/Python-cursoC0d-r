def fibonacci(quantidade, sequencia=(0, 1)):
    # quantidade é a quantidade de núermos armazendas. Sequencia
    # é uma tupla que vai receber os números para o calculo,
    if len(sequencia) == quantidade:
        # conta a quantidade valores na sequencia e compara com o valor
        # definido na quantidade.
        return sequencia
        # Se a condicao for atingida ele sai do looping
    return fibonacci(quantidade, sequencia + (sum(sequencia[-2:]),))
    # Com a condicao nao atingida, ele monta a funcao com a tupla, mantendo
    # quantidade, a sequencia anterior e adiciona um novo valor na tupla
    # "simbolo de +", que é a soma dos ultimos elementos da sequencia anterior


for fib in fibonacci(20):
    print(fib)
