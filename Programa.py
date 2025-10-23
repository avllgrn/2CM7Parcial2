from os import system
from random import randrange

def muestraLista(Original):
    for i in range(n):
        print(f'[{i}] = {Original[i]}')

def intercambia(L, i, j):
    aux = L[j]
    L[j] =L[i]
    L[i] = aux

def burbuja(L):
    n = len(L)
    conteo=0
    for i in range(n-1):
        # print(f'Intento #{i+1}')
        for j in range(n-1):
            conteo += 1
            # muestraLista(L)
            # print(f'Se compara L[{j+1}]={L[j+1]} con L[{j}]={L[j]}')
            if L[j+1] < L[j]:
                # print(f'Se intercambian, porque L[{j+1}]={L[j+1]} < L[{j}]={L[j]}')
                intercambia(L, j, j+1)
            # print()

    # print(f'posibles intercambios: {conteo}')
    # print(f'\nDespués de intentar intercambiar elementos {n-1} veces:')

if __name__ == '__main__':
    system('cls')

    n = int(input('¿Cuántos datos? '))
    L = [randrange(100) for i in range(n)]

    print('Lista inicial')
    muestraLista(L)
    print()

    burbuja(L)

    print('Lista final')
    muestraLista(L)
    print()
