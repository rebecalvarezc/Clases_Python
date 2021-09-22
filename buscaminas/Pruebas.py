from tablero import Buscaminas
from funciones_globales import menu_movimientos
juego1 = Buscaminas(8, 8)
juego1.crear_tablero()
juego1.movimientos(menu_movimientos)