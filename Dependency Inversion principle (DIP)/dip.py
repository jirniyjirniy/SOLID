"""Принцип инверсии зависимостей
    Зависеть от 'абстракций', а не от реализации.
"""

class AuthenticationForUser:
    def __init__(self, connector):
        self.connector = connector

    def authenticate(self, credentials):
        pass

    def is_authenticated(self):
        pass

    def last_login(self):
        pass


class AnonymousAuth(AuthenticationForUser):
    pass


class GitHubAuth(AuthenticationForUser):
    def last_login(self):
        pass


class FacebookAuth(AuthenticationForUser):
    pass


class Persmissions:
    def __init__(self, auth: AuthenticationForUser):
        self.auth = auth

    def has_permissions(self):
        pass


class IsLoggedInPersmissions(Persmissions):
    def last_login(self):
        return auth.last_login