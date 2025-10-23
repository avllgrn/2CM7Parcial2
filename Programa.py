from os import system
from random import randrange

def generaCalificacionesRandrange(n):
    return [randrange(0, 101)/10 for i in range(n)]

def calculaPromedios(P1, P2, P3):
    return [(P1[i]+P2[i]+P3[i]) / 3 for i in range(n)]

def muestraCalificaciones(P1, P2, P3, Prom):
    n = len(P1)
    print('\nAlumno\t| P1\t| P2\t| P3\tProm\n')

    for i in range(n):
        print(f'{i+1}\t|{P1[i]}\t|{P2[i]}\t|{P3[i]}\t|{Prom[i]}')
    print()

if __name__ == '__main__':
    system('cls')

    n = int(input('Cuántos alumnos? '))

    Parcial1 = generaCalificacionesRandrange(n)
    Parcial2 = generaCalificacionesRandrange(n)
    Parcial3 = generaCalificacionesRandrange(n)
    
    Promedio = calculaPromedios(Parcial1, Parcial2, Parcial3)

    muestraCalificaciones(Parcial1, Parcial2, Parcial3, Promedio)
