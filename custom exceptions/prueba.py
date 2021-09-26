import exceptions

# Programa para que el usuario adivine un número.

numero = 15

# Estructura

while True:
    try:
        usuario = int(input('Escriba un número: '))
        if usuario < numero:
            raise exceptions.ValorMuyPequeño
        elif usuario > numero:
            raise exceptions.ValorMuyGrande
        else:
            break
    except exceptions.ValorMuyPequeño:
        print('El numero dado es muy pequeño, intenta de nuevo.\n')
    except exceptions.ValorMuyGrande:
        print('El numero dado es muy grande, intenta de nuevo.\n')

print('Felicidades, has adivinado :)')

# Programa para que el usuario introduzca su salario.

from exceptions import SalarioFueraDeRango

salario = int(input('Introduzca el salario $: '))
if not 5000 < salario < 15000:
    raise SalarioFueraDeRango(salario)