from savable import Savable


class User(Savable):

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @staticmethod
    def login():
        return 'Logged in.'

    def __str__(self):
        return f'User {self.username}.'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password
        }