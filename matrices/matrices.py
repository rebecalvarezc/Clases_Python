# Suma y resta de matrices.
def menu():
    print('Bienvenido al programa de matrices.')
    print('-----------------------------------')
    print('''\nSeleccione la operación que desea realizar:
        1.- Sumar matrices.
        2.- Restar natrices.''')
    operador = int(input('\n -->: '))
    return operador


def sumar_restar_matrices(matriz1: list[list], matriz2: list[list]) -> list[list]:
    """
    Este es un programa que sirve para sumar o restar matrices.
    La operación a realizar será matriz1 + matriz2 ó matriz1 - matriz2.

    :param matriz1: matriz 1
    :param matriz2: matriz 2
    :return: una matriz que contiene la suma de las matrices anteriores.
    """

    while True:
        try:
            operador = menu()
            resultado = []

            if len(matriz1) == len(matriz2) and len(matriz1[0]) == len(matriz2[0]):
                if operador == 1:
                    for i in range(len(matriz1)):
                        resultado.append([])
                        for j in range(len(matriz1[i])):
                            valor = matriz1[i][j] + matriz2[i][j]
                            resultado[i].append(valor)
                    return resultado
                else:
                    for i in range(len(matriz1)):
                        resultado.append([])
                        for j in range(len(matriz1[i])):
                            valor = matriz1[i][j] - matriz2[i][j]
                            resultado[i].append(valor)
                    return resultado
            else:
                print('No se pueden sumar/ restar matrices de dimensiones diferentes.')
        except ValueError:
            print('Error. Ingrese el operador solicitado. \n')
        else:
            break


# Multiplicación de matrices

def multiplicar_matriz(matriz1: list[list], matriz2: list[list]) -> list[list]:
    """
    Este programa multiplica matrices. La operación se llevará a cabo en el siguiente orden: matriz1 * matriz2.
    :param matriz1:
    :param matriz2:
    :return:
    """

    try:
        fila1 = len(matriz1)
        fila2 = len(matriz2)
        columna2 = len(matriz2[0])
        resultado = []
    except TypeError:
        print('Las matrices deben ser de tipo list. Introduce una lista de listas.')
    except IndexError:
        print('Las matrices deben ser de tipo list. Introduce una lista de listas.')
    except:
        print('Ha ocurrido un error.')
    else:
        if fila1 == columna2:
            for i in range(fila1):
                resultado.append([])
                for j in range(fila2):
                    valor = matriz1[i][j] * matriz2[j][i]
                    resultado[i].append(valor)
            return resultado
        else:
            print('Error. Las matrices no cumplen con los requisitos de la multiplicación de matrices.')


# Traspuesta de una matriz

def traspuesta(matriz: list[list]) -> list[list]:
    """

    # 3x4

    matriz = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

   # === Propuesta 1: ===
    transpuesta = []

    for j in range(len(matriz[0])):
        transpuesta.append([fila[j] for fila in matriz])

    === Propuesta 2: ===
    [[fila[j] for fila in matriz] for j in range(len(matriz[0]))] <- lo mismo que la anterior básicamente

    === Propuesta 3: ===
    list(zip(*matriz)) <- Más optima!

    :param matriz:
    :return:
    """

    '''Esta función recibe una matriz y devuelta su traspuesta.'''

    if isinstance(matriz, list):
        resultado = []
        fila_m = len(matriz)
        columna_m = len(matriz[0])
        for j in range(columna_m):
            resultado.append([])
            for i in range(fila_m):
                resultado[j].append(matriz[i][j])
        return resultado
    else:
        print('La función solo acepta variables de tipo list.')


# Rotar matriz

def rotar_matriz(matriz: list[list]) -> list[list]:
    """ Excelente! """
    resultado = []
    fila_m = len(matriz) - 1
    columna_m = len(matriz[0])

    for i in range(columna_m):
        resultado.append([])
        for j in range(fila_m, -1, -1):
            valor = matriz[j][i]
            resultado[i].append(valor)
    return resultado


if __name__ == '__main__':
    menu()
    matriz1 = [[3, 1], [0, 5]]
    matriz2 = traspuesta(matriz1)

    print(matriz2)

    matriz1 = [[3, 1], [0, 5]]
    matriz2 = [[-1, 2], [2, 5]]

    matriz3 = multiplicar_matriz(matriz1, matriz2)
    print(matriz3)

    matriz1 = [[3, 1], [0, 5]]
    matriz2 = [[-1, 2], [2, 5]]

    suma = sumar_restar_matrices(matriz1, matriz2)
    print(suma)
