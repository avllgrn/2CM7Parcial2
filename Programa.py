from os import system
from random import randrange

def generaListaRandrage(n, ini, fin):
    lista = []   # lista vacia
    if ini>fin:
        aux = ini
        ini=fin
        fin=aux

    for i in range(n):
        valor = randrange(ini, fin)
        lista.append( valor )
    return lista

def muestraLista(L):
    n = len(L)
    for i in range(n):
        print(f'[{i}] = {L[i]}')

if __name__ == '__main__':
    system('cls')

    n = int(input('¿Cuántos datos? '))
    ini = int(input('Ingresa inicio de rango '))
    fin = int(input('Ingresa fin de rango '))

    lista = generaListaRandrage(n, ini, fin)
    print()

    print(f'lista = {lista}')
    muestraLista(lista)
    print()
