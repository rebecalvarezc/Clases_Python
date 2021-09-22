# En este script de Python deberás definir el tablero, y los movimientos de la ficha del jugador en el tablero.
# Puedes hacerlo con clases e implementando sus métodos (recomendado) o directamente con funciones.
# En este archivo te dejaré los respectivos TODOs para las cosas que tienes que hacer.

#  Escribir una función que permita crear un tablero de buscaminas.
#  Esto básicamente consiste en proporcionar una cantidad de filas y columnas para crear una matriz con esas
#  dimensiones. Además, también se le debe dar la posibilidad de rellenar el tablero con un valor determinado.

#  Escribir una función que muestre el tablero.
#  El tablero creado anteriormente estará almacenado en una variable, por lo tanto, la razón de ser de esta función
#  será mostrar dicho tablero.

#  Escribir una función que permita insertar las minas en el tablero y guardar las coordenadas de las minas.
#  Esta función deberá recibir el tablero, sus filas y columnas y la cantidad de minas que se van a insertar en el
#  tablero. Para representar una mina usaremos el número 9. Esta función deberá retornar el tablero con las minas
#  y una lista con las coordenadas de las minas. ¡Las minas se deben insertar en el tablero de manera aleatoria!

#  Escribir una función para mostrar el tablero con las minas en la consola.
#  En esta función mostraremos 2 tableros, un tablero que llamaremos visible (que es el que verá el usuario)
#  en donde cada posición será un guion "-" y otro tablero que llamaremos oculto, que rellenaremos con ceros (0)
#  y es en ese tablero oculto donde se colocarán las minas.

class Buscaminas:
    """Plantilla para crear los tableros de buscaminas"""

    def __init__(self, filas: int, columnas: int, minas: int):
        self.filas = filas
        self.columnas = columnas
        self.nro_minas = minas
        self.tablero_base = []
        self.tablero_minas = []
        self.coordenadas = []
        self.tablero_visible = []
        self.tablero_oculto = []

    def crear_tablero(self, valor: str = '-') -> list[list]:
        """
        Esta función se encarga de crear el tablero base para el juego de buscaminas,
        mediante los valores proporcionados por el usuario.

        :param valor: (opcional) str = 'x'
        :return: una matriz de dimensión filas x columnas.
        """

        self.tablero_base = [[valor for j in range(self.columnas)] for i in range(self.filas)]
        return self.tablero_base

    def mostrar_tablero(self):
        """
        Esta función se encarga de imprimir el tablero de buscaminas creado por el usuario.
        :return: str
        """
        for i in self.tablero_base:
            print(i, end='\n')

    def insertar_minas(self):
        """
        Esta función se encarga de insertar el numero de minas dado en el tablero base de forma aleatoria.
        :return: list[list]
        """
        from copy import deepcopy
        from random import randint
        self.tablero_minas = deepcopy(self.tablero_base)
        for minas in range(self.nro_minas):
            i = randint(0, self.filas - 1)
            j = randint(0, self.columnas - 1)
            self.coordenadas.append([i, j])
            self.tablero_minas[i].insert(j, 9)

        return self.tablero_minas, self.coordenadas

    def mostrar_tablero_minas(self):
        """Esta función se encarga de mostrar dos tableros. El del jugador y el de la computadora."""

        self.tablero_visible = [['-' for x in range(self.columnas)] for x in range(self.filas)]
        for i in range(self.filas):
            self.tablero_oculto.append([])
            for j in range(self.columnas):
                if self.tablero_minas[i][j] != 9:
                    self.tablero_oculto[i].append(0)
                else:
                    self.tablero_oculto[i].append(9)

        return self.tablero_visible, self.tablero_oculto
