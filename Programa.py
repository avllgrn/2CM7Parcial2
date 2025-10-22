from os import system

if __name__ == '__main__':
    system('cls')

    listaInt = [11, 22, 33, 44, 55]
    listaFloat = [1.1, 2.2, 3.3, 4.4, 5.5]
    listaStr = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
    
    print(f'   listaInt = {listaInt}')
    nInt = len(listaInt)
    posicion=0
    while posicion<nInt:
        print(f'listaInt[{posicion}] = {listaInt[posicion]}')
        posicion += 1
    print()

    print(f'   listaFloat = {listaFloat}')
    nFloat = len(listaFloat)
    posicion=0
    while posicion<nFloat:
        print(f'listaFloat[{posicion}] = {listaFloat[posicion]}')
        posicion += 1
    print()

    print(f'   listaStr = {listaStr}')
    nStr = len(listaStr)
    posicion=0
    while posicion<nStr:
        print(f'listaStr[{posicion}] = {listaStr[posicion]}')
        posicion += 1
    print()
