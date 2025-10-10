from os import system
from NodoPila import Nodo

class Cola:
    def __init__(self):
        self.L = []

    def __del__(self):
        self.liberaMemoria()

    def push(self, dato):
        self.L.append(dato)

    def pop(self):
        return self.L.pop(0)
        
    def estaVacia(self):
        return len(self.L)==0

    def liberaMemoria(self):
        while not self.estaVacia():
            print(f'Se elimina {self.pop()}')

if __name__ == '__main__':
    system('cls')

    C = Cola()
    
    C.push(5)
    C.push(3)
    C.push(7)
    C.push(-4)

    print(f'Sale: {C.pop()}')
    print(f'Sale: {C.pop()}')

    C.push(9)

    print(f'Sale: {C.pop()}')
    print(f'Sale: {C.pop()}')
    print(f'Sale: {C.pop()}')

    # Jamás se hace pop a 
    # a una pila vacía

    # print(f'Sale: {C.pop()}')
