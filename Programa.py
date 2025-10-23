from os import system

if __name__ == '__main__':
    system('cls')

    M = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(M)
    print()

    m = len(M)
    for i in range(m):
        print( M[i] )
    print()

    n = len(M[0])
    for i in range(m):
        for j in range(n):
            print(M[i][j], end='\t')
        print()
