# This is a sample Python script.
# matriz = [[0 for x in range(3)] for x in range(2)]
def crear_matriz(fila: int, columna: int) -> list[list]:
    matriz_madre = []
    if isinstance(fila, int) and isinstance(columna, int):
        for i in range(fila):
            matriz_madre.append([])
            for j in range(columna):
                while True:
                    try:
                        valor = int(input(f'Escribe el valor para la posición {i + 1},{j + 1}: \n--> '))
                        matriz_madre[i].append(valor)
                    except ValueError:
                        print('Error. Ingresa un número.')
                    else:
                        break
        return matriz_madre
    else:
        print('fila y columna deben ser valores numericos.')


# matriz = [[1, 2, 3], ]
print(crear_matriz(2, 3))

#Tarea: siempre que sea posible, hacer suma/resta y multiplicar matrices (Repasar). hace una función para cada una,
#verificar errores, la transpuesta de una matriz (y rotar una matriz).