from tablero import Buscaminas
from funciones_globales import menu_movimientos
juego1 = Buscaminas(8, 8)
juego1.crear_tablero()
#tablero, coordenadas = juego1.insertar_minas()
#juego1.mostrar_tablero(tablero)
juego1.movimientos(menu_movimientos)