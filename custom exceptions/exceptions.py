# Custom Exceptions

class Error(Exception):
    """ Plantilla para excepciones personalizadas. """
    pass


class ValorMuyPequeño(Error):
    """Se levanta cuando el valor dado es muy pequeño."""
    pass


class ValorMuyGrande(Error):
    """ Se levanta cuando el valor dado es muy grande. """
    pass


# Custom Exceptions, ejm 2.

class SalarioFueraDeRango(Exception):
    """Excepción que se levanta en errores al introducir el salario.

    Atributos:
        salario -- salario introducido que causa el error
        mensaje -- explicación del error
    """

    def __init__(self, salario, mensaje="El salario no está en el rango permitido (5000$, 15000$)."):
        self.salario = salario
        self.mensaje = mensaje
        super().__init__(self.mensaje)  # Esto no lo comprendo bien.
        # Supuestamente permite correr el método __init__ de la clase padre dentro de la clase hijo.

    def __str__(self):
        return f'{self.salario}$ --> {self.mensaje}'
