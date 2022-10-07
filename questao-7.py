from queue import Queue

fila = Queue(maxsize=100)

entrada = 1

while entrada == 1 or entrada == 2:
    print("1 - Adicionar música ")
    print("2 - Mostrar e tocar primeira música")
    print("3 - Sair")
    entrada = int(input())
    if entrada == 1:
        print("Digite o nome da música: ")
        nome = input()
        fila.put(nome)
    if entrada == 2:
        if fila.empty() is False:
            print(fila.get())
        else:
            print("A fila de músicas está vazia")
    if entrada == 3:
        break
