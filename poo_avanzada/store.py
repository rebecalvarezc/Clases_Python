from database import Database
from savable import Savable


class Store(Savable):

    def to_dict(self):
        # lógica correspondiente a la clase e independiente de Savable.
