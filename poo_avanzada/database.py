from typing import Callable


class Database:
    content = {'users': []}  # {'users': [{'username': 'Rebe', 'password': 123, 'access': 'admin'}, {...}]}

    @classmethod
    def insert(cls, data: dict):
        cls.content.get('users').append(data)

    @classmethod
    def find(cls, f: Callable):  # lambda user: user.get('username') == 'Rebeca'
        return [x for x in cls.content.get('users') if f(x)]

    @classmethod
    def remove(cls, f: Callable):  # lambda user: user.get('username') == 'Rebeca'
        return [x for x in cls.content.get('users') if not f(x)]
