class AuthenticationService:
    ROLES_AVAILABLE = ['admin', 'normal']

    def is_authenticated(self, id):
        return self.is_authenticated_parallel(id)

    def is_authenticated_parallel(self, id, role=None):
        if role in self.ROLES_AVAILABLE:
            return id == 12345
        return id == 12345


class AuthenticationClient:
    def __init__(self, authenticationService):
        self.authenticationService = authenticationService

    def run(self):
        authenticated = self.authenticationService.is_authenticated(33)
        print("is authenticated: ", str(authenticated))


class YetAnotherClient:
    def run(self):
        AuthenticationService().is_authenticated(100)


if __name__ == "__main__":
    client = AuthenticationClient(AuthenticationService())
    client.run()
