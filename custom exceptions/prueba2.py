from exceptions import EdadIncorrecta, Error

try:
    usuario = int(input('Introduce tu edad: \n--> '))
    if usuario >= 18:
        print('Eres mayor de edad :)')
    elif usuario < 18:
        print('Eres menor de edad :(')
except ValueError:
    raise EdadIncorrecta()
