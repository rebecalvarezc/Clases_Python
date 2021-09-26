from exceptions import SalarioFueraDeRango

salario = int(input('Introduzca el salario $: '))
if not 5000 < salario < 15000:
    raise SalarioFueraDeRango(salario)
