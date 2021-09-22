from tablero import Buscaminas


def tablero_posicion_inicial(tablero: list[list[str]]):
    """
    Esta función se encarga de imprimir el tablero con los movimientos del jugador en la pantalla.
    """
    from random import randint
    limite_sup_i = round(len(tablero)/ 2 + 1)
    limite_inf_i = round(len(tablero)/ 2 - 1)
    limite_inf_j = round(len(tablero)/ 2 - 1)
    limite_sup_j = round(len(tablero)/ 2 + 1)
    i = randint(limite_inf_i, limite_sup_i)
    j = randint(limite_inf_j, limite_sup_j)
    tablero[i].insert(j, 'x')
    posición_jugador = list([i,j])
    return tablero

def mostrar_tablero_jugador(tablero: list[list[str]]):
    for i in tablero:
        print(i, end='\n')

def juego(tablero: list[list[str]]):
    """
    Esta función simula el click del jugador en la casilla del buscaminas.
    """

    lista_movimientos = []
    while True:
        tablero_movimientos_jugador(tablero)

        print('''Desde su posición puede realizar los siguientes movimientos:
        1) w = arriba
        2) s = abajo
        3) a = izquierda (<---)
        4) d = derecha (--->)
        ''')
        movimiento = input('Indique el movimiento que desea realizar: \n--> ').lower()
        if movimiento == 'w':
            lista_movimientos.append(movimiento)
            juego = input('Escriba "s" para realizar otro movimiento: \n--> ')
            if juego.lower() == 's':
                continue
            else:
                break
        elif movimiento.lower() == 's':
            lista_movimientos.append(movimiento)
            juego = input('Escriba "s" para realizar otro movimiento: \n--> ')
            if juego.lower() == 's':
                continue
            else:
                break
        elif movimiento.lower() == 'a':
            lista_movimientos.append(movimiento)
            juego = input('Escriba "s" para realizar otro movimiento: \n--> ')
            if juego.lower() == 's':
                continue
            else:
                break
        elif movimiento.lower == 'd':
            lista_movimientos.append(movimiento)
            juego = input('Escriba "s" para realizar otro movimiento: \n--> ')
            if juego.lower() == 's':
                continue
            else:
                break
        else:
            print('Error. Ingrese una opción válida\n')
    return lista_movimientos


juego1 = Buscaminas(12, 15, 8)
juego1.crear_tablero()
juego1.insertar_minas()
tabla1, tabla2 = juego1.mostrar_tablero_minas()
posicion = tablero_movimientos_jugador(tabla1)
print(posicion)