from collections import deque
from math import floor

listaEncadeada = deque()

cont = 0
listaEncadeada.append(33)
listaEncadeada.append(8)
listaEncadeada.append(5)
listaEncadeada.append(7)
listaEncadeada.append(99)

meioLista = floor(len(listaEncadeada) / 2)

elementoMeio = 0000000
for i in listaEncadeada:
  cont += 1

  if cont == meioLista:
    elementoMeio = listaEncadeada[cont]

print(elementoMeio)
