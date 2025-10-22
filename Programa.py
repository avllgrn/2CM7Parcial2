from os import system

if __name__ == '__main__':
    system('cls')

    listaInt = [11, 22, 33, 44, 55]
    listaFloat = [1.1, 2.2, 3.3, 4.4, 5.5]
    listaStr = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
    
    print(f'   listaInt = {listaInt}')
    nInt = len(listaInt)
    for posicion in range(nInt):
        print(f'listaInt[{posicion}] = {listaInt[posicion]}')
    print()

    print(f'   listaFloat = {listaFloat}')
    nFloat = len(listaFloat)
    for posicion in range(nFloat):
        print(f'listaFloat[{posicion}] = {listaFloat[posicion]}')
    print()

    print(f'   listaStr = {listaStr}')
    nStr = len(listaStr)
    for posicion in range(nStr):
        print(f'listaStr[{posicion}] = {listaStr[posicion]}')
    print()
