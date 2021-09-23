from copy import deepcopy  # Alt+Enter
from random import randint
from typing import Callable
import os  # Te permite acceder a to_do el contenido de tu sistema operativo

os.system('cls')


class Buscaminas:
    """Plantilla para crear los tableros de buscaminas"""

    def __init__(self, filas: int, columnas: int):
        self.filas = filas
        self.columnas = columnas
        self.tablero_base = []
        self.coordenadas = []
        self.tablero_oculto = []

    def crear_tablero(self) -> list[list]:
        """
        Esta función se encarga de crear el tablero base para el juego de buscaminas,
        mediante los valores proporcionados por el usuario.

        :return: una matriz de dimensión filas x columnas.
        """

        self.tablero_base = [['-' for _ in range(self.columnas)] for _ in range(self.filas)]
        self.tablero_oculto = [[0 for _ in range(self.columnas)] for _ in range(self.filas)]

        return deepcopy(self.tablero_base)

    @staticmethod
    def mostrar_tablero(tablero: list[list] = None):
        """
        Esta función se encarga de imprimir el tablero de buscaminas creado por el usuario.
        :return: str
        """
        for i in tablero:
            for j in i:
                print(j, end=' ')
            print()

    def insertar_minas(self):
        """
        Esta función se encarga de insertar el numero de minas dado en el tablero base de forma aleatoria.
        :return: list[list]
        """
        nro_minas = round((self.filas * self.columnas) / 8)
        for minas in range(nro_minas):
            i = randint(0, self.filas - 1)
            j = randint(0, self.columnas - 1)
            self.coordenadas.append((i, j))
            self.tablero_oculto[i][j] = 9
        return self.tablero_oculto, self.coordenadas

    def tablero_pistas(self):
        """
        Esta función genera un tablero de pistas asociado al número de minas y a la posición de las mismas.
        """
        for i in range(self.filas):
            for j in range(self.columnas):
                if self.tablero_oculto[i][j] == 9:
                    for x in range(-1, 2):
                        for y in range(-1, 2):
                            if 0 <= i + x <= self.filas - 1 and 0 <= j + y <= self.columnas - 1:
                                if self.tablero_oculto[i + x][j + y] != 9:
                                    self.tablero_oculto[i + x][j + y] += 1

        return self.tablero_oculto

    def tablero_posicion_inicial(self):
        """
        Esta función se encarga de generar el tablero con la posición inicial del jugador.
        """
        limite_sup_i = round(len(self.tablero_base) / 2 + 1)
        limite_inf_i = round(len(self.tablero_base) / 2 - 1)
        limite_inf_j = round(len(self.tablero_base) / 2 - 1)
        limite_sup_j = round(len(self.tablero_base) / 2 + 1)
        i = randint(limite_inf_i, limite_sup_i)
        j = randint(limite_inf_j, limite_sup_j)
        posicion_inicial = self.tablero_base[i][j]
        self.tablero_base[i][j] = 'x'
        self.mostrar_tablero(self.tablero_base)
        return posicion_inicial, i, j

    def algoritmo_difusion(self, i: int, j: int):
        """
        Función algoritmo de difusión para descubrir el tablero.
        """
        lista_coordenadas = [(i, j)]  # Agrego las coordenadas a una lista
        while len(lista_coordenadas) != 0:  # TRICKY!!!!!
            f, c = lista_coordenadas.pop()  # saco las coordenadas
            for x in range(-1, 2):
                for y in range(-1, 2):  # para las posiciones circundantes:
                    if 0 <= f + x <= self.filas - 1 and 0 <= c + y <= self.columnas - 1:  # compruebo que estoy dentro del rango
                        if self.tablero_base[f + x][c + y] == '-' and self.tablero_oculto[f + x][c + y] == 0:
                            self.tablero_base[f + x][c + y] = ' '  # la abro y le pongo el cero

                            if (f + x, c + y) not in lista_coordenadas:  # si la coordenada lo esta en la lista
                                lista_coordenadas.append((f + x, c + y))  # la agrego
                        else:
                            self.tablero_base[f + x][c + y] = self.tablero_oculto[f + x][c + y]  # la muestro
        return self.tablero_base

    def movimientos(self, mov: Callable):
        """
        Esta función simula el click del jugador en la casilla del buscaminas.
        """
        self.crear_tablero()
        posicion, i, j = self.tablero_posicion_inicial()
        tablero_oculto, coordenadas = self.insertar_minas()
        self.tablero_pistas()
        condicion = True

        while condicion:
            ejecutar = mov()

            if ejecutar == 'w':
                if i == 0:
                    pass
                else:
                    self.tablero_base[i][j] = posicion  # 'x' ---> '-'
                    posicion = '-'
                    i -= 1
                    if self.tablero_base[i][j] == '-':
                        self.tablero_base[i][j] = 'x'  # '-' --> 'x'

            elif ejecutar == 's':
                if i == self.filas - 1:
                    pass
                else:
                    self.tablero_base[i][j] = posicion  # 'x' ---> '-'
                    posicion = '-'
                    i += 1
                    if self.tablero_base[i][j] == '-':
                        self.tablero_base[i][j] = 'x'  # '-' --> 'x'

            elif ejecutar == 'a':
                if j == 0:
                    pass
                else:
                    self.tablero_base[i][j] = posicion  # 'x' ---> '-'
                    posicion = '-'
                    j -= 1
                    if self.tablero_base[i][j] == '-':
                        self.tablero_base[i][j] = 'x'  # '-' --> 'x'

            elif ejecutar == 'd':
                if j == self.columnas - 1:
                    pass
                else:
                    self.tablero_base[i][j] = posicion  # 'x' ---> '-'
                    posicion = '-'
                    j += 1
                    if self.tablero_base[i][j] == '-':
                        self.tablero_base[i][j] = 'x'  # '-' --> 'x'

            elif ejecutar == 'm':
                self.tablero_base[i][j] = '#'
                posicion = self.tablero_base[i][j]

            elif ejecutar == 'n':
                self.tablero_base[i][j] = '-'
                posicion = self.tablero_base[i][j]

            elif ejecutar == 'z':
                q = self.tablero_oculto[i][j]

                if coordenadas.count((i, j)) != 0:  # if q == 9:
                    self.tablero_base[i][j] = '@'
                    condicion = False
                elif q != 0:
                    self.tablero_base[i][j] = q
                    posicion = q
                elif q == 0:
                    self.tablero_base[i][j] = ' '
                    self.algoritmo_difusion(i, j)
                    for i in range(self.filas):
                        for j in range(self.columnas):
                            if self.tablero_base[i][j] == 0:
                                self.tablero_base[i][j] = ' '
                    posicion = q
            else:
                print('Error. Ingrese una opción válida\n')

            os.system('cls')

            self.mostrar_tablero(self.tablero_base)

        os.system('cls')
        self.mostrar_tablero(self.tablero_base)
        print('\nPerdiste :(')
