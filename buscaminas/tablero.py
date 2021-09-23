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
        nro_minas = round((self.filas * self.columnas) / 3)
        for minas in range(nro_minas):
            i = randint(0, self.filas - 1)
            j = randint(0, self.columnas - 1)
            self.coordenadas.append((i, j))
            self.tablero_oculto[i][j] = 9

        return self.tablero_oculto, self.coordenadas

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

    def movimientos(self, mov: Callable):
        """
        Esta función simula el click del jugador en la casilla del buscaminas.
        """
        posicion, i, j = self.tablero_posicion_inicial()

        condicion = True

        while condicion:
            ejecutar = mov()
            if ejecutar == 'w':
                if i == 0:
                    pass
                else:
                    self.tablero_base[i][j] = posicion  # 'x' ---> '-'
                    i -= 1
                    self.tablero_base[i][j] = 'x'  # '-' --> 'x'
            elif ejecutar == 's':
                if i == self.filas - 1:
                    pass
                else:
                    self.tablero_base[i][j] = posicion  # 'x' ---> '-'
                    i += 1
                    self.tablero_base[i][j] = 'x'  # '-' --> 'x'
            elif ejecutar == 'a':
                if j == 0:
                    pass
                else:
                    self.tablero_base[i][j] = posicion  # 'x' ---> '-'
                    j -= 1
                    self.tablero_base[i][j] = 'x'  # '-' --> 'x'
            elif ejecutar == 'd':
                if j == self.columnas - 1:
                    pass
                else:
                    self.tablero_base[i][j] = posicion  # 'x' ---> '-'
                    j += 1
                    self.tablero_base[i][j] = 'x'  # '-' --> 'x'
            elif ejecutar == 'm':
                self.tablero_base[i][j] = '#'
                posicion, i, j = self.tablero_posicion_inicial()
                self.tablero_base[i][j] = 'x'
            elif ejecutar == 'n':
                self.tablero_base[i][j] = '-'
                posicion, i, j = self.tablero_posicion_inicial()
                self.tablero_base[i][j] = 'x'
            else:
                print('Error. Ingrese una opción válida\n')
            os.system('cls')
            self.mostrar_tablero(self.tablero_base)
