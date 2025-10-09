from os import system

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos datos? '))

    L = [0 for i in range(n)]
    
    print()
    print(f'L {L} con {len(L)} dato(s).')
