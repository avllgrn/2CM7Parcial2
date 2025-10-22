from os import system

if __name__ == '__main__':
    system('cls')

    listaInt = [11, 22, 33, 44, 55]
    listaFloat = [1.1, 2.2, 3.3, 4.4, 5.5]
    listaStr = ['uno', 'dos', 'tres', 'cuatro', 'cinco']
    
    print(f'   listaInt = {listaInt}')
    for dato in listaInt:
        print(f'{dato}')
    print()

    print(f'   listaFloat = {listaFloat}')
    for dato in listaFloat:
        print(f'{dato}')
    print()

    print(f'   listaStr = {listaStr}')
    for dato in listaStr:
        print(f'{dato}')
    print()
