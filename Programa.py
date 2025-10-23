from os import system
from random import randrange

def generaListaRandrage(n, ini, fin):
    if ini>fin:
        aux = ini
        ini=fin
        fin=aux

    lista = [randrange(ini, fin) for i in range(n)]
    return lista

def muestraLista(L):
    n = len(L)
    for i in range(n):
        print(f'[{i}] = {L[i]}')

def suma(L1, L2):
    if len(L1)==len(L2):
        n = len(L1)
        return [L1[i]+L2[i] for i in range(n)]
    else:
        return []

def resta(L1, L2):
    if len(L1)==len(L2):
        n = len(L1)
        return [L1[i]-L2[i] for i in range(n)]
    else:
        return []

if __name__ == '__main__':
    system('cls')

    print('Para A')
    nA = int(input('Cuántos datos? '))

    print('Para B')
    nB = int(input('Cuántos datos? '))

    if nA!=nB:
        print('Error! no pueden sumarse ni restarse...')
    else:
        A = generaListaRandrage(nA, 0, 10)
        B = generaListaRandrage(nA, 0, 10)
        
        C = suma(A, B)
        D = resta(A, B)

        print('A')
        muestraLista(A)
        print()

        print('B')
        muestraLista(B)
        print()

        print('A+B')
        muestraLista(C)
        print()

        print('A-B')
        muestraLista(D)
        print()
