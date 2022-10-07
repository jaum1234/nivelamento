def selection_sort(lotes):
    for i, _ in enumerate(lotes):
        menor = i
        for j in range(i + 1, len(lotes)):
            if lotes[j] < lotes[menor]:
                menor = j
        lotes[i], lotes[menor] = lotes[menor], lotes[i]

def main(): # deixei esse main + o debaixo pra qm quiser testar no vscode. mas o algoritmo é do selection sorte, tem bastante exemplo no amigo google. Ele vai percorrer o vetor e pegar o menor elemento e trocar de lugar com o primeiro... e assim num looping
    lotes = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    selection_sort(lotes)
    print(lotes)

if __name__ == '__main__':
    main()