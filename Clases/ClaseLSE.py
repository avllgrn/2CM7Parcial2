from NodoCola import Nodo
from ClaseCola import Cola
from os import system

class LSE ( Cola ):
    def __init__(self):
        super().__init__()
        self.tamano = 0

    def __str__(self):
        cadena = ''
        aux = self.primero
        while aux!=None:
            cadena += str(aux)
            aux=aux.siguiente
        return cadena + f'  Nodos: {self.tamano}'
    
    def muestraLista(self):
        print(self)
    
    def push(self, dato):
        super().push(dato)
        self.tamano += 1

    def insertaAlUltimo(self, dato):
        self.push(dato)

    def pop(self):
        self.tamano -= 1
        return super().pop()

    def eliminaAlPrimero(self):
        return self.pop()

    def insertaAlPrimero(self, dato):
        if self.estaVacia():
            self.push(dato)

        else:
            self.primero = Nodo(dato, self.primero)
            self.tamano += 1

    def eliminaAlUltimo(self):
        if self.primero==self.ultimo:
            return self.pop()

        else:
            dato = self.ultimo.dato
            aux = self.primero
            while aux.siguiente!=self.ultimo:
                aux=aux.siguiente
            del self.ultimo
            aux.siguiente = None
            self.ultimo = aux

            self.tamano -= 1
            return dato

    def busca(self, dato):
        pos = 0
        aux = self.primero
        while aux!=None:
            if dato==aux.dato:
                return pos
            aux = aux.siguiente
            pos += 1
        return None

    def __contains__(self, dato):
        return self.busca(dato)!=None

    def __getitem__(self, posicion):
        aux = self.primero
        for i in range(posicion):
            aux = aux.siguiente

        return aux.dato

    def __setitem__(self, posicion, dato):
        aux = self.primero
        for i in range(posicion):
            aux = aux.siguiente

        aux.dato = dato

    def __delitem__(self, posicion):
        if posicion == 0:
            self.pop()

        elif posicion == self.tamano-1:
            self.eliminaAlUltimo()

        else:
            aux2 = self.primero
            for i in range(posicion):
                aux1 = aux2
                aux2=aux2.siguiente

            aux1.siguiente = aux2.siguiente
            del aux2

            self.tamano -= 1


if __name__=='__main__':
    system('cls')

    L = LSE()

    # Pruebas de push, pop y __str__
    print('Pruebas de push, pop y  __str__\n\n')
    L.push(1)
    print(L)
    L.push(3)
    print(L)
    L.push(5)
    print(L)
    L.push(7)
    print(L)
    L.push(9)
    print(L)
    print('')

    while not L.estaVacia():
        print(f'Sale {L.pop()}')
        print(L)
    input('\n\n\nPresiona cualquier tecla para continuar...')
    system('cls')

    # Pruebas de insertaAlUltimo, eliminaAlPrimero y muestraLista
    print('Pruebas de insertaAlUltimo, eliminaAlPrimero y muestraLista\n\n')
    L.insertaAlUltimo(1)
    L.muestraLista()
    L.insertaAlUltimo(3)
    L.muestraLista()
    L.insertaAlUltimo(5)
    L.muestraLista()
    L.insertaAlUltimo(7)
    L.muestraLista()
    L.insertaAlUltimo(9)
    L.muestraLista()
    print('')

    while not L.estaVacia():
        print(f'Sale {L.eliminaAlPrimero()}')
        L.muestraLista()
    input('\n\n\nPresiona cualquier tecla para continuar...')
    system('cls')

    # Pruebas de insertaAlPrimero, eliminaAlUltimo
    print('Pruebas de insertaAlPrimero, eliminaAlUltimo\n\n')
    L.insertaAlPrimero(1)
    L.muestraLista()
    L.insertaAlPrimero(3)
    L.muestraLista()
    L.insertaAlPrimero(5)
    L.muestraLista()
    L.insertaAlPrimero(7)
    L.muestraLista()
    L.insertaAlPrimero(9)
    L.muestraLista()
    print('')

    while not L.estaVacia():
        print(f'Sale {L.eliminaAlUltimo()}')
        L.muestraLista()
    input('\n\n\nPresiona cualquier tecla para continuar...')
    system('cls')

    # Pruebas de busca y __contains__
    print('Pruebas de busca y __contains__\n\n')

    for i in range(1,10,2):
        L.push(i)
    print(L)
    print()

    for i in range(10):
        print(f'{i} está en la posición: {L.busca(i)}')
    print()

    for i in range(10):
        print(f'Está {i} en la lista? {i in L}')

    input('\n\n\nPresiona cualquier tecla para continuar...')
    system('cls')

    # Pruebas de __getitem__, __setitem__ y __delitem__
    print('Pruebas de __getitem__, __setitem__ y __delitem__\n\n')

    print(L)
    print()
    print(f' L[3] = {L[3]}')
    print('\n\n\n')
    
    print(f'Se ejecuta: L[3] = 33')
    print()
    L[3] = 33
    print(L)
    print()
    print(f'Ahora, L[3] = {L[3]}')
    print('\n\n\n')

    print(f'Se ejecuta: del L[3]')
    print()
    del L[3]
    print(L)
    print()
    print(f'Ahora, L[3] = {L[3]}')
    print('\n\n\n')

    # Pruebas del destructor y de liberaMemoria
    print('Fin del programa\n\n\n')
