from tablero import Buscaminas

def mostrar_tablero_jugador(tablero: list[list[str]]):
    for i in tablero:
        print(i, end='\n')

def menu_movimientos():
    print('''Desde su posición puede realizar los siguientes movimientos:
            1) w = arriba
            2) s = abajo
            3) a = izquierda (<---)
            4) d = derecha (--->)
            ''')
    movimiento = input('Indique el movimiento que desea realizar: \n--> ').lower()
    #if de condicion del while de movimientos
    return movimiento


