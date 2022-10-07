contador = 1
lista = []
n = int(input('Digite o valor de n:'))

if n == 1:
    raise IndexError

while contador <= n:
    print('Digite o comprimento do cabo número ', contador, ':')
    variavel = int(input())
    lista.append(variavel)
    contador += 1

tamanho = len(lista)
lista.sort()
print('OBS: Irá somar os dois comprimentos menores')

while tamanho != 1:
    print('Cabos existentes:', lista)
    soma = lista[0] + lista[1]
    lista[0] = soma
    del (lista[1])
    lista.sort()
    tamanho = len(lista)

print('Resultado final:', lista)