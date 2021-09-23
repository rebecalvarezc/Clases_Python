from tablero import Buscaminas
from funciones_globales import menu_movimientos


juego1 = Buscaminas(12, 15)
juego1.crear_tablero()
juego1.insertar_minas()
juego1.tablero_pistas()
juego1.movimientos(menu_movimientos)