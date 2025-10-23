from os import system

def generaListaInput(n):
    lista = [float(input(f'Ingresa [{i}] ')) for i in range(n)]
    return lista

def muestraLista(L):
    n = len(L)
    for i in range(n):
        print(f'[{i}] = {L[i]}')

if __name__ == '__main__':
    system('cls')

    n = int(input('¿Cuántos datos? '))

    lista = generaListaInput(n)

    print(f'lista = {lista}')
    muestraLista(lista)
    print()
