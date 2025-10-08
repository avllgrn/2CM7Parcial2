from os import system

class Nodo:
    def __init__(self, dato=0, siguiente=None):
        self.dato = dato
        self.siguiente = siguiente

    def __str__(self):
        cadena = f'| {self.dato} |'

        if self.siguiente != None:
            cadena += ' -> '

        return cadena
    
if __name__ == '__main__':
    system('cls')

    A = Nodo(1)
    B = Nodo(3, A)
    C = Nodo(5, B)
    D = Nodo(7, C)
    
    print(D, end='')
    print(C, end='')
    print(B, end='')
    print(A, end='')
    