from database import Database
from abc import ABC, abstractmethod, ABCMeta


# Clase abstracta -> crear una plantilla que sea obligatoria seguir su estructura
# especificas los métodos abstractos (obligatorios)
# ABC = Abstract Base Classes
# No puedes instanciarlas = no puedes crear un objeto a partir de esa clase.


class Savable(metaclass=ABCMeta):  # = a escribir (ABC)

    @abstractmethod
    def to_dict(self):
        pass

    def save(self):
        Database.insert(self.to_dict())


ronny = Savable()
