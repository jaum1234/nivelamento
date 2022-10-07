lista = []
lista.append(1)
lista.append(7)
lista.append(2)
lista.append(9)

i = 6
for i in range(1, 100):
    lista.append(lista[i] + lista[i - 1])

print(lista)


