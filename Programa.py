from os import system

def muestraMatriz(M):
    m = len(M)
    n = len(M[0])

    for i in range(m):
        for j in range(n):
            print(M[i][j], end='\t')
        print()

def generaConInput(m, n):
    M = []
    for i in range(m):
        renglon = []
        for j in range(n):
            valor = float(input(f'Ingresa [{i}][{j}] '))
            renglon.append( valor )
        M.append(renglon)
        # print(M)
    return M

if __name__ == '__main__':
    system('cls')

    m = int(input('¿Cuántas filas? '))
    n = int(input('¿Cuántas columnas? '))

    Minput = generaConInput(m, n)

    print('\np')
    muestraMatriz(Minput)
    print()
