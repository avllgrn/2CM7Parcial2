from os import system

def generaListaInput(n):
    lista = []   # lista vacia
    for i in range(n):
        valor = float(input(f'Ingresa [{i}] '))
        lista.append( valor )
    return lista

def muestraLista(L):
    n = len(L)
    for i in range(n):
        print(f'[{i}] = {L[i]}')

if __name__ == '__main__':
    system('cls')

    n = int(input('¿Cuántos datos? '))
    print()

    lista = generaListaInput(n)
    print()

    print(f'lista = {lista}')
    muestraLista(lista)
    print()
