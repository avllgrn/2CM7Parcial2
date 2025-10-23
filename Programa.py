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

def multiplica(A, B):
    # A (m x n) B (n x ele) = C (m x ele)

    if len(A[0])==len(B): # La restriccion es que número de columnas de A DEBE ser número de filas de B
        m = len(A)
        n = len(A[0])
        ele = len(B[0])

        C = generaInicializada(m, ele)  # Y resulta una matriz de m x ele
        for i in range(m):
            for j in range(ele):
                for k in range(n):
                    C[i][j] = C[i][j] + A[i][k] * B[k][j]
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

    if nA!=mB:
        print('Error! No pueden multiplicarse')
    else:

        A = generaConRandrange(mA, nA, 0, 11)
        B = generaConRandrange(mB, nB, 0, 11)
        C = multiplica(A, B)

        print('\nA')
        muestraMatriz(A)
        print()

        print('\nB')
        muestraMatriz(B)
        print()

        print('\nA*B')
        muestraMatriz(C)
        print()
