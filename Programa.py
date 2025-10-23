from os import system
from random import randrange

def muestraMatriz(M):
    m = len(M)
    n = len(M[0])

    for i in range(m):
        for j in range(n):
            print(M[i][j], end='\t')
        print()

def generaInicializada(m, n):
    M = []
    for i in range(m):
        renglon = []
        for j in range(n):
            renglon.append(0)
        M.append(renglon)
        # print(M)
    return M

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

def suma(A, B):
    if len(A)==len(B) and len(A[0])==len(B[0]):
        m = len(A)
        n = len(B[0])

        C = generaInicializada(m, n)
        for i in range(m):
            for j in range(n):
                C[i][j] = A[i][j]+B[i][j]
        return C
    else:
        return [[]]

def resta(A, B):
    if len(A)==len(B) and len(A[0])==len(B[0]):
        m = len(A)
        n = len(B[0])

        C = generaInicializada(m, n)
        for i in range(m):
            for j in range(n):
                C[i][j] = A[i][j]-B[i][j]
        return C
    else:
        return [[]]

if __name__ == '__main__':
    system('cls')

    print('Para A')
    mA = int(input('¿Cuántas filas? '))
    nA = int(input('¿Cuántas columnas? '))
    print('Para B')
    mB = int(input('¿Cuántas filas? '))
    nB = int(input('¿Cuántas columnas? '))

    if mA!=mB or nA!=nB:
        print('Error! No pueden sumarse ni restarse')
    else:

        A = generaConRandrange(mA, nA, 0, 11)
        B = generaConRandrange(mB, nB, 0, 11)
        C = suma(A, B)
        D = resta(A, B)

        print('\nA')
        muestraMatriz(A)
        print()

        print('\nB')
        muestraMatriz(B)
        print()

        print('\nA+B')
        muestraMatriz(C)
        print()

        print('\nA-B')
        muestraMatriz(D)
        print()
