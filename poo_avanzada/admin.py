from user import User


class Admin(User):  # Multiple herencia (User, Savable)

    def __init__(self, username, password, access):
        super().__init__(username, password)
        self.access = access

    def __str__(self):
        return f'Admin {self.username}, access {self.access}'

    def to_dict(self):
        return {
            'username': self.username,
            'password': self.password,
            'access': self.access
        }
