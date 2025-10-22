from os import system

def generaListaCeros(n):
    lista = []   # lista vacia
    for i in range(n):
        lista.append(0)
    return lista

def muestraLista(L):
    n = len(L)
    for i in range(n):
        print(f'[{i}] = {L[i]}')

if __name__ == '__main__':
    system('cls')

    n = int(input('¿Cuántos datos? '))

    ceros = generaListaCeros(n)

    print(f'ceros = {ceros}')
    muestraLista(ceros)
    print()
