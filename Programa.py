from os import system

def muestraMatriz(M):
    m = len(M)
    n = len(M[0])

    for i in range(m):
        for j in range(n):
            print(M[i][j], end='\t')
        print()

def generaConNumeroDeFila(m, n):
    M = []
    for i in range(m):
        renglon = []
        for j in range(n):
            renglon.append(i)
        M.append(renglon)
        # print(M)
    return M

def generaConNumeroDeColumna(m, n):
    M = []
    for i in range(m):
        renglon = []
        for j in range(n):
            renglon.append(j)
        M.append(renglon)
        # print(M)
    return M

def generaConContador(m, n):
    M = []
    contador = 0
    for i in range(m):
        renglon = []
        for j in range(n):
            renglon.append( contador )
            contador += 1
        M.append(renglon)
        # print(M)
    return M

if __name__ == '__main__':
    system('cls')

    m = int(input('¿Cuántas filas? '))
    n = int(input('¿Cuántas columnas? '))

    MFila = generaConNumeroDeFila(m, n)
    MColumna = generaConNumeroDeColumna(m, n)
    MContador = generaConContador(m, n)

    print('\nMFila')
    muestraMatriz(MFila)
    print()

    print('\nMColumna')
    muestraMatriz(MColumna)
    print()

    print('\nMContador')
    muestraMatriz(MContador)
    print()
