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

def buscaDato(L, dato):
    n = len(L)
    posDato = None
    for i in range(n):
        if dato == L[i]:
            posDato = i
            break
    return posDato

def cuentaDato(L, dato):
    veces = 0
    n = len(L)
    for i in range(n):
        if dato == L[i]:
            veces += 1
    return veces

def acumulaDatos(L):
    n=len(L)
    s = 0
    for i in range(n):
        s = s + L[i]
    return s

def promediaDatos(L):
    if len(L)!=0:
        return acumulaDatos(L)/len(L)
    else:
        return None

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos datos? '))

    L = generaListaRandrage(n, 0, 10)
    print()
    muestraLista(L)

    dato = int(input('¿Qué dato buscas? '))
    posDato = buscaDato(L,dato)
    if posDato!=None:
        print(f'{dato} está en la posición {posDato}')
    else:
        print(f'{dato} NO está en la lista')
    print()

    veces = cuentaDato(L,dato)
    print(f'{dato} está {veces} veces')
    print()

    s = acumulaDatos(L)
    print(f'Los datos en L acumulan {s}')
    print()

    p = promediaDatos(L)
    print(f'Los datos en L promedian {p}')
    print()
