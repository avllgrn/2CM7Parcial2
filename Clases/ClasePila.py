from os import system
from NodoPila import Nodo

class Pila:
    def __init__(self):
        self.tope = None

    def __del__(self):
        self.liberaMemoria()

    def push(self, dato):
        self.tope = Nodo(dato, self.tope)

    def pop(self):
        d = self.tope.dato
        aux = self.tope
        self.tope = self.tope.inferior
        del aux
        return d
        
    def estaVacia(self):
        return self.tope==None

    def liberaMemoria(self):
        while not self.estaVacia():
            print(f'Se elimina {self.pop()}')

if __name__ == '__main__':
    system('cls')

    P = Pila()
    
    P.push(5)
    P.push(3)
    P.push(7)
    P.push(-4)

    print(f'Sale: {P.pop()}')
    print(f'Sale: {P.pop()}')

    P.push(9)

    print(f'Sale: {P.pop()}')
    print(f'Sale: {P.pop()}')
    print(f'Sale: {P.pop()}')

    # Jamás se hace pop a 
    # a una pila vacía

    # print(f'Sale: {P.pop()}')
