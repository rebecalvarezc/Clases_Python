from exceptions import EdadIncorrecta, Error

usuario = int(input('Introduce tu edad: \n--> '))
if type(usuario) == int:
    if usuario >= 18:
        print('Eres mayor de edad :)')
    elif usuario < 18:
        print('Eres menor de edad :(')
else:
    raise EdadIncorrecta(usuario) # Me sigue saliendo el mensaje del ValueError
