from os import system

if __name__ == '__main__':
    system('cls')

    L = list()

    n = int(input('Cuántos datos? '))

    for i in range(n):
        print(f'L {L} con {len(L)} dato(s).')
        L.append(0)
    
    print()
    print(f'L {L} con {len(L)} dato(s).')
