from tablero import Buscaminas
juego1 = Buscaminas(2, 3, 1)
juego1.crear_tablero()
juego1.insertar_minas()
tabla1, tabla2 = juego1.mostrar_tablero_minas()
print(tabla1, tabla2)

print(juego1.tablero_minas, juego1.tablero_oculto, juego1.tablero_base)
print(juego1.filas, juego1.columnas, juego1.nro_minas, juego1.coordenadas)