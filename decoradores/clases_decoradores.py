from typing import Callable
import functools

# Base de datos
usuarios = {'username': 'Rebeca123',
            'access_level': 'guest'}


# Esto es un decorador. Agrega funcionalidad extra a la función (o a un método)
def user_has_permission(access_level: str = 'admin'):
    """ Decorador para comprobar el nivel de acceso."""
    def wrapper(f: Callable):
        @functools.wraps(f)  # para usar los atributos especiales de la función original
        def inner_wrapper(*args, **kwargs):  # envuelve la funcionalidad interna
            """ Función que da una funcionalidad extra. """
            if usuarios['access_level'] == access_level:
                return f(*args, **kwargs)
        return inner_wrapper
    return wrapper


@user_has_permission()
def my_unsafe_function(panel):  # función 'insegura'
    """ Función que devuelve la contraseña del administrador. """
    return f'Password for {panel} panel is: 1234'


@user_has_permission('guest')
def another():
    return 'hello :)'


print(my_unsafe_function('rebe'))

