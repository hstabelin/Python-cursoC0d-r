dobro_pares = [i * 2 for i in range(10) if i % 2 == 0]
print(dobro_pares)

# outra forma
dobros_pare = []
for i in range(10):
    if i % 2 == 0:
        dobros_pare.append(i * 2)
print(dobros_pare)
