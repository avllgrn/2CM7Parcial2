from os import system

class Nodo:
    def __init__(self, dato=0, inferior=None):
        self.dato = dato
        self.inferior = inferior

    def __str__(self):
        cadena = f'| {self.dato} |'

        if self.inferior != None:
            cadena += ' -> '

        return cadena

if __name__ == '__main__':
    system('cls')

    A = Nodo(1, None)
    B = Nodo(3, A)
    C = Nodo(5, B)
    
    print(C)
    print()

    print(B)
    print()
    
    print(A)
    print()
