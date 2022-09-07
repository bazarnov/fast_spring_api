# FastSpring Auth

import base64


class FastSpringAuth:
        
    def __init__(
        self, 
        user: str = None,
        password: str = None,
    ):
        """
        @ user: FastSpring API username
        @ password: FastSpring API password
        """
        self.user = user
        self.password = password
        
    def get_auth_header(self):
        token = None
        if self.user and self.password:
            auth_string = f"{self.user}:{self.password}".encode("utf8")
            token = base64.b64encode(auth_string).decode("utf8")
        return {'Authorization': f'Basic {token}'} if token else {}