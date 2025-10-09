from os import system

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos datos? '))

    L = []
    for i in range(n):
        print(f'L {L} con {len(L)} dato(s).')
        L.append(0)
    
    print()
    print(f'L {L} con {len(L)} dato(s).')
