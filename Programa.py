from os import system
from random import randrange

def muestraMatriz(M):
    m = len(M)
    n = len(M[0])

    for i in range(m):
        for j in range(n):
            print(M[i][j], end='\t')
        print()

def generaConRandrange(m, n, ini, fin):
    M = []

    if ini>fin:
        aux = ini
        ini=fin
        fin=aux

    for i in range(m):
        renglon = []
        for j in range(n):
            valor = randrange(ini, fin)
            renglon.append( valor )
        M.append(renglon)
        # print(M)

    return M

if __name__ == '__main__':
    system('cls')

    m = int(input('¿Cuántas filas? '))
    n = int(input('¿Cuántas columnas? '))
    ini = int(input('Ingresa inicio de rango '))
    fin = int(input('Ingresa fin de rango '))

    Minput = generaConRandrange(m, n, ini, fin)

    print('\np')
    muestraMatriz(Minput)
    print()
