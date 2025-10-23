from os import system
from random import randrange

def muestraMatriz(M):
    m = len(M)
    n = len(M[0])

    for i in range(m):
        for j in range(n):
            print(M[i][j], end='\t')
        print()

def generaIdentidad(n):
    M = []
    m = n
    for i in range(m):
        renglon = []
        for j in range(n):
            if i==j:
                renglon.append(1)
            else:
                renglon.append(0)
        M.append(renglon)
    return M

if __name__ == '__main__':
    system('cls')

    n = int(input('¿Cuántas filas y columnas? '))

    I = generaIdentidad(n)

    print('\nI')
    muestraMatriz(I)
    print()
