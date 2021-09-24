from tablero import Buscaminas
from funciones_globales import menu_movimientos


juego1 = Buscaminas()
juego1.movimientos(menu_movimientos)
#juego1.mostrar_tablero(juego1.tablero_oculto)
#juego1.mostrar_tablero(juego1.algoritmo_difusion(3,3))