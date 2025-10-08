from os import system
from NodoCola import Nodo

class Cola:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def __del__(self):
        self.liberaMemoria()

    def estaVacia(self):
        return self.primero==None and self.ultimo==None
        
    def push(self, dato):
        if self.estaVacia():
            self.primero = Nodo(dato, None)
            self.ultimo = self.primero

        else:
            self.ultimo.siguiente = Nodo(dato, None)
            self.ultimo = self.ultimo.siguiente
    
    def pop(self):
        dato =  self.primero.dato
        if self.primero == self.ultimo:
            del self.primero
            self.primero = None
            self.ultimo = None

        else:
            aux = self.primero
            self.primero = self.primero.siguiente
            del aux
        return dato
    
    def liberaMemoria(self):
        while not self.estaVacia():
            # print(f'Se elimina {self.pop()}')
            self.pop()

if __name__ == '__main__':
    system('cls')

    C = Cola()

    C.push(5)
    C.push(3)
    C.push(7)
    C.push(-4)
    
    print(C.pop())
    print(C.pop())

    C.push(9)

    print(C.pop())
    print(C.pop())
    print(C.pop())

    # Jamás se le debe hacer pop() a una Cola vacía
    # print(C.pop())
