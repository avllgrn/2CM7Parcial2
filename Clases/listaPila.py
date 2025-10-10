from os import system
from NodoPila import Nodo

class Pila:
    def __init__(self):
        self.L = []

    def __del__(self):
        self.liberaMemoria()

    def push(self, dato):
        self.L.append(dato)

    def pop(self):
        return self.L.pop()
        
    def estaVacia(self):
        return len(self.L)==0

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
