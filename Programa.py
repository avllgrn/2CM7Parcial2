from os import system

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos datos? '))

    L = []
    for i in range(n):
        print(f'L {L} con {len(L)} dato(s).')
        cadena = input(f'Ingresa cadena {i} ')
        L.append(cadena)
    
    print()
    print(f'L {L} con {len(L)} dato(s).')
