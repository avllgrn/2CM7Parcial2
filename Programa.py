from os import system
from random import randrange

def muestraMatriz(M):
    m = len(M)
    n = len(M[0])

    for i in range(m):
        for j in range(n):
            print(M[i][j], end='\t')
        print()

def generaConRandrange(m, n):
    M = []
    for i in range(m):
        renglon = []
        for j in range(n):
            valor = randrange(101)#/10
            renglon.append( valor )
        M.append(renglon)
        # print(M)
    return M

def generaTranspuesta(M):
    MT = []

    m = len(M)
    n = len(M[0])

    mT = n
    nT = m
    for i in range(mT):
        renglon = []
        for j in range(nT):
            renglon.append(0)
        MT.append(renglon)

    for i in range(m):
        for j in range(n):
            MT[j][i] = M[i][j]
    return MT   

if __name__ == '__main__':
    system('cls')

    m = int(input('¿Cuántas filas? '))
    n = int(input('¿Cuántas columnas? '))

    M = generaConRandrange(m, n)
    MT = generaTranspuesta(M)

    print('\nM')
    muestraMatriz(M)
    print()

    print('\nMT')
    muestraMatriz(MT)
    print()
