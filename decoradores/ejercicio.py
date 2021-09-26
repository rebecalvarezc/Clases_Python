# Recibir información de usuarios de una base de datos (diccionario, nombre de usuario y nivel de acceso).
# Crear dos decoradores. 1 que chequee el nivel de acceso del usuario
# Otro que chequee que el nombre de usuario empiece con R
# Cuando se cumplan los dos que corra la función
# Si se cumple solo 1: None
from typing import Callable
import functools

# users = {'user_name': 'Rebeca15', 'access_level': 'admin'}
# users = {'user_name': 'Evelio11', 'access_level': 'guest'}
# users = {'user_name': 'Ale03', 'access_level': 'admin'}
users = {'user_name': 'Ronny06', 'access_level': 'guest'}


# Decorador 1
def inicial_usuario(f: Callable):
    """ Función que chequea la inicial del usuario."""

    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        if users['user_name'].lower().startswith('r'):
            return f(*args, **kwargs)
        else:
            print('El nombre de usuario no comienza con "R".')
    return wrapper


# Decorador 2
def check_access_level(access_level: str):
    """ Función que chequea el nivel de acceso del usuario. """

    def wrapper(f: Callable):
        @functools.wraps(f)
        def inner_wrapper(*args, **kwargs):
            if users['access_level'] == access_level:
                return f(*args, **kwargs)
            else:
                print('El usuario no tiene permiso de administrador.')
        return inner_wrapper
    return wrapper


# Función
@check_access_level('guest')
@inicial_usuario
def funcion_chequear():
    """ Chequeo de usuario. """
    return 'Hola :)'


print(funcion_chequear())
