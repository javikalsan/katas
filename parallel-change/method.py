class AuthenticationService:
    ROLES_AVAILABLE = ['admin', 'normal']

    def is_authenticated(self, id, role):
        if role in self.ROLES_AVAILABLE:
            return id == 12345


class AuthenticationClient:
    def __init__(self, authentication_service):
        self.authentication_service = authentication_service

    def run(self):
        authenticated = self.authentication_service.is_authenticated(33, 'normal')
        print("is authenticated: ", str(authenticated))


class YetAnotherClient:
    def run(self):
        AuthenticationService().is_authenticated(100, 'normal')


if __name__ == "__main__":
    client = AuthenticationClient(AuthenticationService())
    client.run()
